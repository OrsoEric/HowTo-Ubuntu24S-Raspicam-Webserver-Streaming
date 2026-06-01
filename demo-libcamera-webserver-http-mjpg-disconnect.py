#!/usr/bin/env python3
import io
import mmap
import socket
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import libcamera
import numpy as np
from PIL import Image

SIZE_W = 1640
SIZE_H = 1232
WARMUP_FRAMES = 5

# -------------------------------------------------
# Clean, Atomic State Controls
# -------------------------------------------------
state_lock = threading.Lock()
current_client_id = None  # Track exactly who owns the camera right now
active_generation = 0    # Incremented every time a new client takes over


# -------------------------------------------------
# LibCameraCapture class
# -------------------------------------------------
class LibCameraCapture:

    def __init__(self, width=SIZE_W, height=SIZE_H):
        self.width = width
        self.height = height

        self.cm = libcamera.CameraManager.singleton()
        self.cam = self.cm.cameras[0]

        self.latest_frame = None
        self.frame_counter = 0
        self.frame_lock = threading.Lock()
        self.frame_event = threading.Event()

        self.running = False
        self.stream = None
        self.stream_cfg = None
        self.allocator = None
        self.buffers = None

    def start(self):
        self.cam.acquire()

        config = self.cam.generate_configuration([
            libcamera.StreamRole.Viewfinder
        ])
        stream_cfg = config.at(0)
        stream_cfg.pixel_format = libcamera.PixelFormat("RGB888")
        stream_cfg.size = libcamera.Size(self.width, self.height)

        self.cam.configure(config)
        self.stream = stream_cfg.stream
        self.stream_cfg = stream_cfg

        self.allocator = libcamera.FrameBufferAllocator(self.cam)
        self.allocator.allocate(self.stream)
        self.buffers = self.allocator.buffers(self.stream)

        self.cam.start()

        # Warm-up frames
        for i in range(WARMUP_FRAMES):
            _ = self.grab()
            print(f"[warmup] frame {i} done")

        self.running = True
        threading.Thread(target=self._capture_loop, daemon=True).start()

    def stop(self):
        self.running = False
        try:
            self.cam.stop()
        finally:
            self.cam.release()

    def grab(self):
        req = self.cam.create_request()
        req.add_buffer(self.stream, self.buffers[0])
        self.cam.queue_request(req)

        ready = []
        while not ready:
            ready = self.cm.get_ready_requests()
            if not ready:
                time.sleep(0.002)

        completed = ready[0]
        fb = completed.buffers[self.stream]
        plane = fb.planes[0]

        with mmap.mmap(
            plane.fd,
            plane.length,
            mmap.MAP_SHARED,
            mmap.PROT_READ,
            offset=plane.offset,
        ) as mm:
            data = mm.read(plane.length)

        stride_bytes = self.stream_cfg.stride
        stride_pixels = stride_bytes // 3

        frame = np.frombuffer(data, dtype=np.uint8)
        frame = frame[: stride_bytes * self.height]
        frame = frame.reshape(self.height, stride_pixels, 3)
        frame = frame[:, : self.width, :]

        return frame

    def _capture_loop(self):
        global current_client_id

        while self.running:
            with state_lock:
                has_active_client = current_client_id is not None

            if not has_active_client:
                time.sleep(0.1)
                continue

            frame = self.grab()

            with self.frame_lock:
                self.latest_frame = frame
                self.frame_counter += 1
                print(f"[capture] frame #{self.frame_counter}")

            self.frame_event.set()
            self.frame_event.clear()


camera = LibCameraCapture()


# -------------------------------------------------
# HTTP MJPEG handler
# -------------------------------------------------
class MJPEGHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt, *args):
        return  # Suppress standard HTTP logs

    def do_GET(self):
        if self.path == "/":
            self._serve_index()
        elif self.path == "/mjpg":
            self._serve_mjpg()
        else:
            self.send_error(404, "Not found")

    def _serve_index(self):
        body = b"""
        <html>
            <body style="background:#111; color:white; text-align:center;">
                <h1>Raspberry Pi MJPEG Stream</h1>
                <img src="/mjpg" style="width:90%; border:2px solid #444;">
            </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _serve_mjpg(self):
        global current_client_id, active_generation
        client_id = id(self)
        my_generation = 0

        # -------------------------------------------------
        # Preemptive Takeover Guard
        # -------------------------------------------------
        with state_lock:
            active_generation += 1
            my_generation = active_generation
            
            if current_client_id is not None:
                print(
                    f"\n[DEBUG][http] NEW REQUEST from {client_id}. Evicting lingering client {current_client_id}..."
                )
            
            # Unconditionally take ownership of the global lock
            current_client_id = client_id
            print(f"[DEBUG][client {client_id}] ===== Granted Camera Ownership (Gen {my_generation}) =====")

        # Configure network behavior options
        self.connection.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

        try:
            self.send_response(200)
            self.send_header(
                "Content-Type", "multipart/x-mixed-replace; boundary=frame"
            )
            self.send_header(
                "Cache-Control", "no-cache, no-store, must-revalidate"
            )
            self.send_header("Pragma", "no-cache")
            self.send_header("Expires", "0")
            self.end_headers()
        except Exception as e:
            print(f"[DEBUG][client {client_id}] Failed during header negotiation: {e}")
            self._cleanup_client(client_id, my_generation)
            return

        sent = 0
        try:
            while True:
                # 1. Generation Check: Has a newer client booted us out?
                with state_lock:
                    if active_generation != my_generation:
                        print(f"[DEBUG][client {client_id}] Loop stopped: Evicted by newer connection.")
                        break

                # 2. Fast Proactive Socket Check
                self.connection.setblocking(False)
                try:
                    data = self.connection.recv(1, socket.MSG_PEEK)
                    if data == b"":
                        print(f"\n[DEBUG][client {client_id}] DISCONNECT DETECTED via empty read (EOF).")
                        break
                except BlockingIOError:
                    pass
                except (ConnectionResetError, BrokenPipeError, OSError) as e:
                    print(f"\n[DEBUG][client {client_id}] DISCONNECT DETECTED via read exception: {e}")
                    break
                finally:
                    self.connection.setblocking(True)

                # 3. Bounded wait for frame production
                flag_triggered = camera.frame_event.wait(timeout=0.2)
                if not flag_triggered:
                    continue

                with camera.frame_lock:
                    if camera.latest_frame is None:
                        continue
                    frame = camera.latest_frame.copy()

                # 4. Compress frame to JPEG
                img = Image.fromarray(frame, "RGB")
                buf = io.BytesIO()
                img.save(buf, format="JPEG", quality=80)
                jpg = buf.getvalue()

                # 5. Formulate payload
                payload = (
                    b"--frame\r\n"
                    b"Content-Type: image/jpeg\r\n"
                    b"Content-Length: " + str(len(jpg)).encode() + b"\r\n\r\n"
                    + jpg
                    + b"\r\n"
                )

                # 6. Push data out to client
                try:
                    self.connection.sendall(payload)
                except (BrokenPipeError, ConnectionResetError, OSError, TimeoutError) as e:
                    print(f"\n[DEBUG][client {client_id}] DISCONNECT DETECTED via sendall failure: {e}")
                    break

                sent += 1
                print(f"[client {client_id}] sent frame #{sent}")

        finally:
            self._cleanup_client(client_id, my_generation)

    def _cleanup_client(self, client_id, my_generation):
        global current_client_id
        with state_lock:
            # ONLY clear the global camera tracking lock if WE are still the current owner.
            # If a newer client evicted us, leaving it alone lets them keep streaming.
            if current_client_id == client_id and active_generation == my_generation:
                current_client_id = None
                print(f"[DEBUG][client {client_id}] ===== Camera cleanly released =====")
            else:
                print(f"[DEBUG][client {client_id}] Releasing thread (Overwritten by newer generation).")


# -------------------------------------------------
# Main entry point
# -------------------------------------------------
if __name__ == "__main__":
    print("[main] starting camera")
    camera.start()

    server = ThreadingHTTPServer(("0.0.0.0", 8000), MJPEGHandler)
    print("[server] starting threaded HTTP on port 8000")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[server] shutting down")
    finally:
        server.server_close()
        camera.stop()
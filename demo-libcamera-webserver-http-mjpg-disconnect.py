#!/usr/bin/env python3
import libcamera
import numpy as np
import mmap
import time
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from PIL import Image
import io

SIZE_W = 1640
SIZE_H = 1232
WARMUP_FRAMES = 5

# -------------------------------------------------
# Global client activity flags
# -------------------------------------------------
active_client_lock = threading.Lock()
client_active_lock = threading.Lock()
client_active = False

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

        config = self.cam.generate_configuration([libcamera.StreamRole.Viewfinder])
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
        frame = frame[:stride_bytes * self.height]
        frame = frame.reshape(self.height, stride_pixels, 3)
        frame = frame[:, :self.width, :]

        return frame

    def _capture_loop(self):
        global client_active

        while self.running:
            with client_active_lock:
                active = client_active

            if not active:
                time.sleep(0.1)
                continue

            frame = self.grab()

            with self.frame_lock:
                self.latest_frame = frame
                self.frame_counter += 1
                print(f"[capture] frame #{self.frame_counter}")

            self.frame_event.set()
            self.frame_event.clear()


# -------------------------------------------------
# HTTP MJPEG handler
# -------------------------------------------------
camera = LibCameraCapture()


class MJPEGHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt, *args):
        # Silence default logging
        return

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
        global client_active

        if not active_client_lock.acquire(blocking=False):
            msg = b"Camera busy\n"
            self.send_response(503)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(msg)))
            self.end_headers()
            self.wfile.write(msg)
            print("[http] rejected /mjpg: another client is active")
            return

        with client_active_lock:
            client_active = True

        client_id = id(self)
        print(f"[client {client_id}] connected /mjpg")

        self.send_response(200)
        self.send_header(
            "Content-Type", "multipart/x-mixed-replace; boundary=frame"
        )
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.end_headers()

        sent = 0
        try:
            while True:
                if self.connection.fileno() == -1:
                    print(f"[client {client_id}] socket closed")
                    break

                camera.frame_event.wait()

                with camera.frame_lock:
                    if camera.latest_frame is None:
                        continue
                    frame = camera.latest_frame.copy()

                img = Image.fromarray(frame, "RGB")
                buf = io.BytesIO()
                img.save(buf, format="JPEG", quality=80)
                jpg = buf.getvalue()

                try:
                    self.wfile.write(b"--frame\r\n")
                    self.wfile.write(b"Content-Type: image/jpeg\r\n\r\n")
                    self.wfile.write(jpg)
                    self.wfile.write(b"\r\n")
                    self.wfile.flush()
                except (BrokenPipeError, ConnectionResetError, OSError) as e:
                    print(f"[client {client_id}] disconnect: {e}")
                    break

                sent += 1
                print(f"[client {client_id}] sent frame #{sent}")

        finally:
            with client_active_lock:
                client_active = False
            print(f"[client {client_id}] releasing active_client_lock")
            active_client_lock.release()


# -------------------------------------------------
# Main entry point
# -------------------------------------------------
if __name__ == "__main__":
    print("[main] starting camera")
    camera.start()

    server = HTTPServer(("0.0.0.0", 8000), MJPEGHandler)
    print("[server] starting bare HTTP on port 8000")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[server] shutting down")
    finally:
        server.server_close()
        camera.stop()

#!/usr/bin/env python3

"""

python demo-libcamera-webserver-http-mjpg.py

"""

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

latest_frame = None
frame_counter = 0
frame_lock = threading.Lock()
frame_event = threading.Event()

active_client_lock = threading.Lock()

# -------------------------
# 1. Initialize libcamera
# -------------------------
cm = libcamera.CameraManager.singleton()
cam = cm.cameras[0]
cam.acquire()

config = cam.generate_configuration([libcamera.StreamRole.Viewfinder])
stream_cfg = config.at(0)
stream_cfg.pixel_format = libcamera.PixelFormat("RGB888")
stream_cfg.size = libcamera.Size(SIZE_W, SIZE_H)

cam.configure(config)
lc_stream = stream_cfg.stream

allocator = libcamera.FrameBufferAllocator(cam)
allocator.allocate(lc_stream)
buffers = allocator.buffers(lc_stream)

cam.start()

# Warm-up
for i in range(WARMUP_FRAMES):
    req = cam.create_request()
    req.add_buffer(lc_stream, buffers[0])
    cam.queue_request(req)
    while not cm.get_ready_requests():
        time.sleep(0.005)
    cm.get_ready_requests()
    print(f"[warmup] frame {i} done")


# -------------------------
# 2. Capture frame
# -------------------------
def capture_frame():
    req = cam.create_request()
    req.add_buffer(lc_stream, buffers[0])
    cam.queue_request(req)

    ready = []
    while not ready:
        ready = cm.get_ready_requests()
        if not ready:
            time.sleep(0.002)

    completed = ready[0]
    fb = completed.buffers[lc_stream]
    plane = fb.planes[0]

    with mmap.mmap(plane.fd, plane.length,
                   mmap.MAP_SHARED, mmap.PROT_READ,
                   offset=plane.offset) as mm:
        data = mm.read(plane.length)

    stride_bytes = stream_cfg.stride
    stride_pixels = stride_bytes // 3

    frame = np.frombuffer(data, dtype=np.uint8)
    frame = frame[:stride_bytes * SIZE_H]
    frame = frame.reshape(SIZE_H, stride_pixels, 3)
    frame = frame[:, :SIZE_W, :]

    return frame


def capture_loop():
    global latest_frame, frame_counter

    while True:
        frame = capture_frame()

        with frame_lock:
            latest_frame = frame
            frame_counter += 1
            print(f"[capture] frame #{frame_counter} "
                  f"min={frame.min()} max={frame.max()}")

        frame_event.set()
        frame_event.clear()


# -------------------------
# 3. HTTP handler
# -------------------------
class MJPEGHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt, *args):
        # Silence default logging; we print our own
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
        # single-client guard
        if not active_client_lock.acquire(blocking=False):
            msg = b"Camera busy\n"
            self.send_response(503)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(msg)))
            self.end_headers()
            self.wfile.write(msg)
            print("[http] rejected /mjpg: another client is active")
            return

        client_id = id(self)
        print(f"[client {client_id}] connected /mjpg")

        self.send_response(200)
        self.send_header("Content-Type",
                         "multipart/x-mixed-replace; boundary=frame")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.end_headers()

        sent = 0
        try:
            while True:
                frame_event.wait()

                with frame_lock:
                    if latest_frame is None:
                        continue
                    frame = latest_frame.copy()

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
            print(f"[client {client_id}] releasing active_client_lock")
            active_client_lock.release()


# -------------------------
# 4. Run server
# -------------------------
if __name__ == "__main__":
    print("Start frame grabber")
    threading.Thread(target=capture_loop, daemon=True).start()

    server = HTTPServer(("0.0.0.0", 8000), MJPEGHandler)
    print("[server] starting bare HTTP on port 8000")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[server] shutting down")
        server.server_close()
        cam.stop()
        cam.release()

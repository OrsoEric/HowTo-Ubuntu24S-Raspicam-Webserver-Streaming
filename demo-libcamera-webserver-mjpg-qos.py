#!/usr/bin/env python3

"""
python demo-libcamera-webserver-mjpg-qos.py

this shows a timestamp on screen
but when clowing webpage and openin will kill fps
"""


import libcamera
import numpy as np
import mmap
import time
from flask import Flask, Response, request
from PIL import Image, ImageDraw, ImageFont
import io

SIZE_W = 640
SIZE_H = 480
WARMUP_FRAMES = 5

app = Flask(__name__)

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

# -------------------------
# 3. MJPEG generator with timestamp
# -------------------------
def mjpeg_generator():
    while True:
        frame = capture_frame()

        # Timestamp
        ts = time.time()

        # Draw timestamp on frame
        img = Image.fromarray(frame, "RGB")
        draw = ImageDraw.Draw(img)
        draw.text((10, 10), f"{ts:.6f}", fill=(255, 255, 0))

        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=80)
        jpg = buf.getvalue()

        # Send timestamp in header + JPEG
        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n"
            + f"X-Timestamp: {ts}\r\n\r\n".encode()
            + jpg
            + b"\r\n"
        )

# -------------------------
# 4. Latency reporting endpoint
# -------------------------
@app.route("/latency", methods=["POST"])
def latency():
    data = request.json
    server_ts = float(data["server_ts"])
    client_ts = float(data["client_ts"])

    now = time.time()
    rtt = now - server_ts
    render_delay = client_ts - server_ts

    print(f"[latency] RTT={rtt*1000:.2f} ms  render={render_delay*1000:.2f} ms")

    return "ok"

# -------------------------
# 5. Web page with JS latency reporter
# -------------------------
@app.route("/")
def index():
    return """
    <html>
    <body style="background:#111; color:white; text-align:center;">
        <h1>MJPEG Stream with Latency Measurement</h1>
        <img id="cam" src="/mjpg" style="width:90%; border:2px solid #444;">
        <script>
            const img = document.getElementById("cam");

            img.onload = () => {
                // Extract timestamp from header via fetch (MJPEG doesn't expose headers to JS)
            };

            // Poll the MJPEG stream manually to extract timestamps
            const stream = new EventSource("/mjpg_headers");
        </script>
    </body>
    </html>
    """

@app.route("/mjpg")
def mjpg():
    return Response(mjpeg_generator(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")

# -------------------------
# 6. Run server
# -------------------------
if __name__ == "__main__":
    print("[server] starting on port 8000")
    app.run(host="0.0.0.0", port=8000, threaded=True)

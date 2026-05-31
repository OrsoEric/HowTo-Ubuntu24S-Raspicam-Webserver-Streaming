#!/usr/bin/env python3

"""
python demo-libcamera-webserver-h264.py

"""


import libcamera
import numpy as np
import mmap
import time
import fcntl
import os
from flask import Flask, Response

SIZE_W = 640
SIZE_H = 480
FPS = 30

# V4L2 constants
VIDIOC_S_FMT = 0x40045602
VIDIOC_REQBUFS = 0x40045608
VIDIOC_QBUF = 0x4004560f
VIDIOC_DQBUF = 0x4004560e
V4L2_BUF_TYPE_VIDEO_OUTPUT_MPLANE = 9
V4L2_BUF_TYPE_VIDEO_CAPTURE_MPLANE = 10

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
stream = stream_cfg.stream

allocator = libcamera.FrameBufferAllocator(cam)
allocator.allocate(stream)
buffers = allocator.buffers(stream)

cam.start()

# Warm-up
for _ in range(5):
    req = cam.create_request()
    req.add_buffer(stream, buffers[0])
    cam.queue_request(req)
    while not cm.get_ready_requests():
        time.sleep(0.005)
    cm.get_ready_requests()

# -------------------------
# 2. Initialize hardware H.264 encoder
# -------------------------
ENCODER = "/dev/video11"   # Pi4 hardware encoder
enc = os.open(ENCODER, os.O_RDWR)

# Set encoder format
class v4l2_format:
    def __init__(self):
        self.type = V4L2_BUF_TYPE_VIDEO_OUTPUT_MPLANE
        self.width = SIZE_W
        self.height = SIZE_H
        self.pixelformat = int.from_bytes(b"H264", "little")

fmt = v4l2_format()
fcntl.ioctl(enc, VIDIOC_S_FMT, fmt)

# -------------------------
# 3. Frame generator
# -------------------------
def h264_generator():
    while True:
        # Capture frame
        req = cam.create_request()
        req.add_buffer(stream, buffers[0])
        cam.queue_request(req)

        ready = []
        while not ready:
            ready = cm.get_ready_requests()
            if not ready:
                time.sleep(0.002)

        completed = ready[0]
        fb = completed.buffers[stream]
        plane = fb.planes[0]

        with mmap.mmap(plane.fd, plane.length,
                       mmap.MAP_SHARED, mmap.PROT_READ,
                       offset=plane.offset) as mm:
            data = mm.read(plane.length)

        # Feed raw RGB to encoder
        os.write(enc, data)

        # Read encoded H.264
        try:
            encoded = os.read(enc, 65536)
            if encoded:
                yield encoded
        except BlockingIOError:
            pass

# -------------------------
# 4. HTTP endpoint
# -------------------------
@app.route("/stream.h264")
def stream_h264():
    return Response(h264_generator(),
                    mimetype="video/H264")

@app.route("/")
def index():
    return """
    <html>
    <body style="background:#111; color:white; text-align:center;">
        <h1>H.264 Hardware Stream</h1>
        <p>Open this in VLC:</p>
        <code>http://PI_IP:8000/stream.h264</code>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, threaded=True)

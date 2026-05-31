#!/usr/bin/env python3

"""
python demo-libcamera-webserver-h264.py


[2:45:36.196486939] [13178]  INFO Camera camera_manager.cpp:340 libcamera v0.7.1+rpt20260429
[2:45:36.197263223] [13182]  INFO IPAManager ipa_manager.cpp:148 libcamera is not installed. Adding '/home/sona/libcamera/build/src/ipa' to the IPA search path
[2:45:36.261378801] [13182]  INFO IPAProxy ipa_proxy.cpp:73 libcamera is not installed. Loading IPA configuration from '/home/sona/libcamera/src/ipa/rpi/vc4/data'
[2:45:36.261481558] [13182]  INFO IPAProxy ipa_proxy.cpp:184 Using tuning file /home/sona/libcamera/src/ipa/rpi/vc4/data/imx219.json
[2:45:36.270722229] [13182]  INFO Camera camera_manager.cpp:223 Adding camera '/base/soc/i2c0mux/i2c@1/imx219@10' for pipeline handler rpi/vc4
[2:45:36.270796710] [13182]  INFO RPI vc4.cpp:445 Registered camera /base/soc/i2c0mux/i2c@1/imx219@10 to Unicam device /dev/media2 and ISP device /dev/media1
[2:45:36.271578290] [13178]  INFO Camera camera.cpp:1216 configuring streams: (0) 640x480-RGB888/sRGB
[2:45:36.272170892] [13182]  INFO RPI vc4.cpp:620 Sensor: /base/soc/i2c0mux/i2c@1/imx219@10 - Selected sensor format: 640x480-SBGGR10_1X10/RAW - Selected unicam format: 640x480-pBAA/RAW
Traceback (most recent call last):
  File "/home/sona/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming/demo-libcamera-webserver-h264.py", line 76, in <module>
    fcntl.ioctl(enc, VIDIOC_S_FMT, fmt)
TypeError: 'v4l2_format' object cannot be interpreted as an integer
[2:45:36.625285998] [13182] ERROR V4L2 v4l2_videodevice.cpp:1322 /dev/video16[14:cap]: Unable to request 0 buffers: Device or resource busy
[2:45:36.630529120] [13182] ERROR V4L2 v4l2_videodevice.cpp:1322 /dev/video15[13:cap]: Unable to request 0 buffers: Device or resource busy
[2:45:36.632982915] [13182] ERROR V4L2 v4l2_videodevice.cpp:1322 /dev/video14[12:cap]: Unable to request 0 buffers: Device or resource busy
[2:45:36.641682687] [13182] ERROR V4L2 v4l2_videodevice.cpp:1322 /dev/video13[11:out]: Unable to request 0 buffers: Device or resource busy
[2:45:36.644830749] [13182] ERROR V4L2 v4l2_videodevice.cpp:1322 /dev/video0[10:cap]: Unable to request 0 buffers: Device or resource busy
[2:45:36.649626675] [13182] FATAL default object.cpp:100 assertion "Thread::current() == thread_ || !thread_->isRunning()" failed in ~Object()
Backtrace:
libcamera::Object::~Object()+0x2c0 (/home/sona/libcamera/build/src/libcamera/base/libcamera-base.so.0.7.1 [0x0000ffff8e09f720])
libcamera::ipa::RPi::IPAProxyRPiThreaded::~IPAProxyRPiThreaded()+0x5c (/home/sona/libcamera/build/src/libcamera/libcamera.so.0.7.1 [0x0000ffff8e16efec])
libcamera::ipa::RPi::IPAProxyRPiThreaded::~IPAProxyRPiThreaded()+0x14 (/home/sona/libcamera/build/src/libcamera/libcamera.so.0.7.1 [0x0000ffff8e16f048])
libcamera::Vc4CameraData::~Vc4CameraData()+0x984 (/home/sona/libcamera/build/src/libcamera/libcamera.so.0.7.1 [0x0000ffff8e232954])
libcamera::Camera::~Camera()+0x188 (/home/sona/libcamera/build/src/libcamera/libcamera.so.0.7.1 [0x0000ffff8e1762cc])
libcamera::Camera::~Camera()+0x14 (/home/sona/libcamera/build/src/libcamera/libcamera.so.0.7.1 [0x0000ffff8e1763c4])
std::_Sp_counted_base<(__gnu_cxx::_Lock_policy)2>::_M_release_last_use_cold()+0x1c (/home/sona/libcamera/build/src/libcamera/libcamera.so.0.7.1 [0x0000ffff8e170a8c])
libcamera::CameraManager::Private::cleanup()+0x110 (/home/sona/libcamera/build/src/libcamera/libcamera.so.0.7.1 [0x0000ffff8e17f4d0])
??? [0x0000ffff8ded1ae0] (/usr/lib/aarch64-linux-gnu/libstdc++.so.6.0.33 [0x0000ffff8ded1ae0])
??? [0x0000ffff8ded1ae0] (/usr/lib/aarch64-linux-gnu/libstdc++.so.6.0.33 [0x0000ffff8ded1ae0])
Aborted (core dumped)

problem with the video transcoder
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

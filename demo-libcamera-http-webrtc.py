#!/usr/bin/env python3

"""
python demo-libcamera-http-webrtc.py

http://192.168.1.227:8080/


"""

import asyncio
import threading
import time
import mmap
import numpy as np
from aiohttp import web
from aiortc import RTCPeerConnection, RTCSessionDescription, VideoStreamTrack
from aiortc.rtcrtpparameters import RTCRtpCodecCapability
import av
from PIL import Image
import libcamera

# ============================================================
# 1. LIBCAMERA INITIALIZATION
# ============================================================

SIZE_W = 1640
SIZE_H = 1232
WARMUP_FRAMES = 5

VIDEO_CODECS = [
    RTCRtpCodecCapability(mimeType="video/VP8", clockRate=90000),
    RTCRtpCodecCapability(mimeType="video/H264", clockRate=90000),
]

latest_frame = None
frame_lock = threading.Lock()
frame_event = threading.Event()

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
    global latest_frame
    while True:
        frame = capture_frame()
        with frame_lock:
            latest_frame = frame
        frame_event.set()
        frame_event.clear()


# ============================================================
# 2. WEBRTC VIDEO TRACK
# ============================================================

class CameraTrack(VideoStreamTrack):
    async def recv(self):
        loop = asyncio.get_event_loop()
        # wait for a new frame in a thread, not blocking the event loop
        await loop.run_in_executor(None, frame_event.wait)
        frame_event.clear()

        with frame_lock:
            frame = latest_frame.copy()

        video_frame = av.VideoFrame.from_ndarray(frame, format="rgb24")
        video_frame.pts = None
        video_frame.time_base = None
        return video_frame



# ============================================================
# 3. EMBEDDED HTML PAGE
# ============================================================

HTML_PAGE = """
<!DOCTYPE html>
<html>
<body style="background:#111; color:white; text-align:center;">
<h1>WebRTC UDP Camera Stream</h1>
<video id="v" autoplay playsinline style="width:90%; border:2px solid #444;"></video>

<script>
async function start() {
    const pc = new RTCPeerConnection();

    pc.ontrack = (event) => {
        document.getElementById("v").srcObject = event.streams[0];
    };

    const offer = await pc.createOffer();
    await pc.setLocalDescription(offer);

    const res = await fetch("/offer", {
        method: "POST",
        body: JSON.stringify(pc.localDescription),
        headers: { "Content-Type": "application/json" }
    });

    const answer = await res.json();
    await pc.setRemoteDescription(answer);
}

start();
</script>
</body>
</html>
"""


# ============================================================
# 4. WEBRTC SIGNALING SERVER
# ============================================================

pcs = set()

async def index(request):
    return web.Response(text=HTML_PAGE, content_type="text/html")


async def offer(request):
    params = await request.json()
    offer = RTCSessionDescription(sdp=params["sdp"], type=params["type"])

    pc = RTCPeerConnection()
    pcs.add(pc)

    # Attach camera track directly
    pc.addTrack(CameraTrack())

    await pc.setRemoteDescription(offer)
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)

    return web.json_response({
        "sdp": pc.localDescription.sdp,
        "type": pc.localDescription.type
    })




# ============================================================
# 5. MAIN ENTRY POINT
# ============================================================

def start_webrtc_server():
    app = web.Application()
    app.router.add_get("/", index)
    app.router.add_post("/offer", offer)
    web.run_app(app, port=8080)


if __name__ == "__main__":
    print("Starting libcamera capture thread…")
    threading.Thread(target=capture_loop, daemon=True).start()

    print("Starting WebRTC UDP server on port 8080…")
    start_webrtc_server()

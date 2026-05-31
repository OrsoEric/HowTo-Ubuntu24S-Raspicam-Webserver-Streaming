#!/usr/bin/env python3

"""
python test-libcamera-h264.py
"""

import libcamera
import time
import sys

DURATION_SEC = 3
WIDTH = 640
HEIGHT = 480

def main():
    cm = libcamera.CameraManager.singleton()
    cams = cm.cameras
    if not cams:
        raise RuntimeError("No cameras found")

    cam = cams[0]
    print("Using camera:", cam.id)
    cam.acquire()

    # Configure video stream
    config = cam.generate_configuration([libcamera.StreamRole.VideoRecording])
    stream_cfg = config.at(0)
    stream_cfg.pixel_format = libcamera.PixelFormat("YUV420")
    stream_cfg.size = libcamera.Size(WIDTH, HEIGHT)

    cam.configure(config)
    stream = stream_cfg.stream

    # Allocate buffers
    allocator = libcamera.FrameBufferAllocator(cam)
    allocator.allocate(stream)
    buffers = allocator.buffers(stream)

    # Create encoder (H.264)
    encoder = libcamera.Encoder("h264")
    encoder.configure(stream_cfg)
    encoder.start()

    # Open output file
    out_path = "demo.h264"
    outfile = open(out_path, "wb")

    # Connect encoder output callback
    def on_encoded(data, keyframe, timestamp):
        outfile.write(data)

    encoder.output.connect(on_encoded)

    # Start camera
    cam.start()

    # Queue all buffers once
    for fb in buffers:
        req = cam.create_request()
        req.add_buffer(stream, fb)
        cam.queue_request(req)

    print("Recording for", DURATION_SEC, "seconds...")
    t_end = time.time() + DURATION_SEC

    while time.time() < t_end:
        ready = cm.get_ready_requests()
        if not ready:
            time.sleep(0.005)
            continue

        req = ready[0]
        fb = req.buffers[stream]

        # Send buffer to encoder
        encoder.encode(fb)

        # Requeue buffer for next frame
        new_req = cam.create_request()
        new_req.add_buffer(stream, fb)
        cam.queue_request(new_req)

    print("Stopping...")

    cam.stop()
    encoder.stop()
    outfile.close()
    cam.release()

    print("Saved", out_path)

if __name__ == "__main__":
    main()

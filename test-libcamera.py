#!/usr/bin/env python3
import libcamera
import numpy as np
import cv2
import mmap
import time

N_WARMUP = 5  # number of frames to discard before saving

#SIZE_W = 640
#SIZE_H = 480

SIZE_W = 1640
SIZE_H = 1232 


def main():
    cm = libcamera.CameraManager.singleton()
    cams = cm.cameras
    if not cams:
        raise RuntimeError("No cameras found")

    cam = cams[0]
    print("Using camera:", cam.id)
    cam.acquire()

    config = cam.generate_configuration([libcamera.StreamRole.StillCapture])
    stream_cfg = config.at(0)

    # try your higher resolution here
    stream_cfg.pixel_format = libcamera.PixelFormat("RGB888")
    stream_cfg.size = libcamera.Size(SIZE_W, SIZE_H)

    cam.configure(config)
    stream = stream_cfg.stream

    allocator = libcamera.FrameBufferAllocator(cam)
    allocator.allocate(stream)
    buffers = allocator.buffers(stream)

    cam.start()

    last_frame = None

    for i in range(N_WARMUP):
        req = cam.create_request()
        req.add_buffer(stream, buffers[0])
        cam.queue_request(req)

        ready = []
        t0 = time.time()
        while not ready and (time.time() - t0) < 2.0:
            ready = cm.get_ready_requests()
            if not ready:
                time.sleep(0.01)

        if not ready:
            raise RuntimeError("Timeout waiting for frame")

        completed = ready[0]
        fb = completed.buffers[stream]
        plane = fb.planes[0]

        with mmap.mmap(plane.fd, plane.length,
                       mmap.MAP_SHARED, mmap.PROT_READ,
                       offset=plane.offset) as mm:
            data = mm.read(plane.length)

        w = stream_cfg.size.width
        h = stream_cfg.size.height
        stride_bytes = stream_cfg.stride          # bytes per line
        stride_pixels = stride_bytes // 3         # RGB888 → 3 bytes per pixel

        frame = np.frombuffer(data, dtype=np.uint8)

        # use full stride * height, then crop to visible width
        frame = frame[:stride_bytes * h]
        frame = frame.reshape(h, stride_pixels, 3)
        frame = frame[:, :w, :]                  # crop padding

        print(f"Frame {i}: min={frame.min()}, max={frame.max()}")
        last_frame = frame


    cam.stop()
    cam.release()

    out_path = "still-libcamera-hires.jpg"
    cv2.imwrite(out_path, last_frame)
    print("Saved", out_path)

if __name__ == "__main__":
    main()

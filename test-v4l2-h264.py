#!/usr/bin/env python3

"""
python test-v4l2-h264.py
"""
#!/usr/bin/env python3
"""
python test-v4l2-h264.py

Capture from /dev/video0 (YUYV) ->
feed frames into /dev/video11 (H.264 encoder) ->
write raw H.264 bitstream to output.h264
"""

import fcntl
import mmap
import os
import select
import struct
import time

import v4l2  # low-level ioctl header, must be patched for Python 3

CAP_DEV = "/dev/video0"   # camera
ENC_DEV = "/dev/video11"  # H.264 encoder
WIDTH = 640
HEIGHT = 480
FPS = 30
DURATION_SEC = 3
NUM_BUFFERS = 4
OUTPUT_FILE = "output.h264"


def xioctl(fd, request, arg):
    while True:
        try:
            return fcntl.ioctl(fd, request, arg)
        except InterruptedError:
            continue


def set_format_capture(fd):
    fmt = v4l2.v4l2_format()
    fmt.type = v4l2.V4L2_BUF_TYPE_VIDEO_CAPTURE
    fmt.fmt.pix.width = WIDTH
    fmt.fmt.pix.height = HEIGHT
    fmt.fmt.pix.pixelformat = v4l2.V4L2_PIX_FMT_YUYV
    fmt.fmt.pix.field = v4l2.V4L2_FIELD_NONE
    xioctl(fd, v4l2.VIDIOC_S_FMT, fmt)


def set_format_output(fd):
    fmt = v4l2.v4l2_format()
    fmt.type = v4l2.V4L2_BUF_TYPE_VIDEO_OUTPUT_MPLANE
    fmt.fmt.pix_mp.width = WIDTH
    fmt.fmt.pix_mp.height = HEIGHT
    fmt.fmt.pix_mp.pixelformat = v4l2.V4L2_PIX_FMT_YUYV
    fmt.fmt.pix_mp.field = v4l2.V4L2_FIELD_NONE
    fmt.fmt.pix_mp.num_planes = 1
    xioctl(fd, v4l2.VIDIOC_S_FMT, fmt)


def set_format_capture_mplane(fd):
    fmt = v4l2.v4l2_format()
    fmt.type = v4l2.V4L2_BUF_TYPE_VIDEO_CAPTURE_MPLANE
    fmt.fmt.pix_mp.width = WIDTH
    fmt.fmt.pix_mp.height = HEIGHT
    fmt.fmt.pix_mp.pixelformat = v4l2.V4L2_PIX_FMT_H264
    fmt.fmt.pix_mp.field = v4l2.V4L2_FIELD_NONE
    fmt.fmt.pix_mp.num_planes = 1
    xioctl(fd, v4l2.VIDIOC_S_FMT, fmt)


def reqbufs(fd, buf_type, memory=v4l2.V4L2_MEMORY_MMAP, count=NUM_BUFFERS):
    req = v4l2.v4l2_requestbuffers()
    req.type = buf_type
    req.memory = memory
    req.count = count
    xioctl(fd, v4l2.VIDIOC_REQBUFS, req)
    return req.count


def mmap_buffers(fd, buf_type, count, mplane=False):
    bufs = []
    for i in range(count):
        buf = v4l2.v4l2_buffer()
        buf.type = buf_type
        buf.memory = v4l2.V4L2_MEMORY_MMAP
        buf.index = i
        if mplane:
            plane_array = (v4l2.v4l2_plane * 1)()
            buf.m.planes = plane_array
            buf.length = 1
        xioctl(fd, v4l2.VIDIOC_QUERYBUF, buf)

        if mplane:
            offset = buf.m.planes[0].m.mem_offset
            length = buf.m.planes[0].length
        else:
            offset = buf.m.offset
            length = buf.length

        mm = mmap.mmap(
            fd,
            length,
            mmap.MAP_SHARED,
            mmap.PROT_READ | mmap.PROT_WRITE,
            offset=offset,
        )
        bufs.append((buf, mm))
    return bufs


def qbuf_all(fd, buf_type, bufs, mplane=False):
    for i, (buf, mm) in enumerate(bufs):
        buf.index = i
        buf.memory = v4l2.V4L2_MEMORY_MMAP
        if mplane:
            buf.length = 1
        xioctl(fd, v4l2.VIDIOC_QBUF, buf)


def stream_on(fd, buf_type):
    buf_type_c = struct.pack("I", buf_type)
    xioctl(fd, v4l2.VIDIOC_STREAMON, buf_type_c)


def stream_off(fd, buf_type):
    buf_type_c = struct.pack("I", buf_type)
    xioctl(fd, v4l2.VIDIOC_STREAMOFF, buf_type_c)


def main():
    cap_fd = os.open(CAP_DEV, os.O_RDWR | os.O_NONBLOCK)
    enc_fd = os.open(ENC_DEV, os.O_RDWR | os.O_NONBLOCK)

    # Configure formats
    set_format_capture(cap_fd)
    set_format_output(enc_fd)
    set_format_capture_mplane(enc_fd)

    # Request buffers
    cap_count = reqbufs(cap_fd, v4l2.V4L2_BUF_TYPE_VIDEO_CAPTURE)
    out_count = reqbufs(enc_fd, v4l2.V4L2_BUF_TYPE_VIDEO_OUTPUT_MPLANE)
    capm_count = reqbufs(enc_fd, v4l2.V4L2_BUF_TYPE_VIDEO_CAPTURE_MPLANE)

    # Map buffers
    cap_bufs = mmap_buffers(
        cap_fd, v4l2.V4L2_BUF_TYPE_VIDEO_CAPTURE, cap_count, mplane=False
    )
    out_bufs = mmap_buffers(
        enc_fd, v4l2.V4L2_BUF_TYPE_VIDEO_OUTPUT_MPLANE, out_count, mplane=True
    )
    capm_bufs = mmap_buffers(
        enc_fd, v4l2.V4L2_BUF_TYPE_VIDEO_CAPTURE_MPLANE, capm_count, mplane=True
    )

    # Queue all capture and encoder capture buffers
    qbuf_all(cap_fd, v4l2.V4L2_BUF_TYPE_VIDEO_CAPTURE, cap_bufs, mplane=False)
    qbuf_all(
        enc_fd,
        v4l2.V4L2_BUF_TYPE_VIDEO_CAPTURE_MPLANE,
        capm_bufs,
        mplane=True,
    )

    # Start streaming
    stream_on(cap_fd, v4l2.V4L2_BUF_TYPE_VIDEO_CAPTURE)
    stream_on(enc_fd, v4l2.V4L2_BUF_TYPE_VIDEO_OUTPUT_MPLANE)
    stream_on(enc_fd, v4l2.V4L2_BUF_TYPE_VIDEO_CAPTURE_MPLANE)

    start_time = time.time()
    out_file = open(OUTPUT_FILE, "wb")

    cap_type = v4l2.V4L2_BUF_TYPE_VIDEO_CAPTURE
    out_type = v4l2.V4L2_BUF_TYPE_VIDEO_OUTPUT_MPLANE
    capm_type = v4l2.V4L2_BUF_TYPE_VIDEO_CAPTURE_MPLANE

    try:
        while time.time() - start_time < DURATION_SEC:
            r, _, _ = select.select([cap_fd, enc_fd], [], [], 1.0)

            # Dequeue from camera, queue to encoder output
            if cap_fd in r:
                buf = v4l2.v4l2_buffer()
                buf.type = cap_type
                buf.memory = v4l2.V4L2_MEMORY_MMAP
                xioctl(cap_fd, v4l2.VIDIOC_DQBUF, buf)
                index = buf.index
                frame_data = cap_bufs[index][1][: buf.bytesused]

                # Get an encoder output buffer
                obuf = v4l2.v4l2_buffer()
                obuf.type = out_type
                obuf.memory = v4l2.V4L2_MEMORY_MMAP
                obuf.length = 1
                plane_array = (v4l2.v4l2_plane * 1)()
                obuf.m.planes = plane_array
                xioctl(enc_fd, v4l2.VIDIOC_DQBUF, obuf)

                oindex = obuf.index
                out_mm = out_bufs[oindex][1]
                out_mm[: len(frame_data)] = frame_data
                obuf.m.planes[0].bytesused = len(frame_data)

                xioctl(enc_fd, v4l2.VIDIOC_QBUF, obuf)

                # Requeue camera buffer
                xioctl(cap_fd, v4l2.VIDIOC_QBUF, buf)

            # Dequeue encoded data from encoder capture
            if enc_fd in r:
                cbuf = v4l2.v4l2_buffer()
                cbuf.type = capm_type
                cbuf.memory = v4l2.V4L2_MEMORY_MMAP
                cbuf.length = 1
                plane_array = (v4l2.v4l2_plane * 1)()
                cbuf.m.planes = plane_array
                try:
                    xioctl(enc_fd, v4l2.VIDIOC_DQBUF, cbuf)
                except OSError:
                    continue

                cindex = cbuf.index
                mm = capm_bufs[cindex][1]
                data = mm[: cbuf.m.planes[0].bytesused]
                if data:
                    out_file.write(data)

                xioctl(enc_fd, v4l2.VIDIOC_QBUF, cbuf)

    finally:
        stream_off(cap_fd, cap_type)
        stream_off(enc_fd, out_type)
        stream_off(enc_fd, capm_type)
        out_file.close()
        os.close(cap_fd)
        os.close(enc_fd)

    print(f"Saved raw H.264 bitstream to {OUTPUT_FILE}")
    print("Convert to MP4 with:")
    print("  ffmpeg -r 30 -i output.h264 -c copy output.mp4")


if __name__ == "__main__":
    main()

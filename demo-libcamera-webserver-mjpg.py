#!/usr/bin/env python3

"""
python demo-libcamera-webserver-mjpg.py

[client 281473301966832] sent frame #27
[capture] min=0 max=255
[client 281473378233584] sent frame #176
[capture] frame #231 min=0 max=255
[client 281473378233584] sent frame #177
[client 281473301966832] sent frame #28
[capture] min=0 max=255
[capture] frame #232 min=0 max=255
[client 281473378233584] sent frame #178
[capture] min=0 max=255
[client 281473301966832] sent frame #29
[capture] frame #233 min=0 max=255
[client 281473378233584] sent frame #179

works but flask is unfit for duty and doesn't detect client disconnect
will keep spawining more webserver if close open

also i'll need to fix the udp this likely uses tcp
"""
#!/usr/bin/env python3
import libcamera
import numpy as np
import mmap
import time
from flask import Flask, Response
from PIL import Image
import io


import threading

SIZE_W = 1640
SIZE_H = 1232 
WARMUP_FRAMES = 5

latest_frame = None
frame_counter = 0
frame_lock = threading.Lock()
frame_event = threading.Event()


#SIZE_W = 640
#SIZE_H = 480




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
lc_stream = stream_cfg.stream   # <-- renamed to avoid Flask shadowing

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

    print(f"[capture] min={frame.min()} max={frame.max()}")

    return frame

def capture_loop():
    global latest_frame, frame_counter

    while True:
        frame = capture_frame()

        with frame_lock:
            latest_frame = frame
            frame_counter += 1
            print(f"[capture] frame #{frame_counter} min={frame.min()} max={frame.max()}")

        frame_event.set()      # wake all clients
        frame_event.clear()    # reset for next frame


# -------------------------
# 3. MJPEG generator
# -------------------------
def mjpeg_generator():
    client_id = id(threading.current_thread())
    sent = 0
    print(f"[client {client_id}] connected")

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

            sent += 1
            print(f"[client {client_id}] sent frame #{sent}")

            try:
                yield (b"--frame\r\n"
                       b"Content-Type: image/jpeg\r\n\r\n" +
                       jpg + b"\r\n")
            except (BrokenPipeError, ConnectionResetError, OSError) as e:
                print(f"[client {client_id}] write error, disconnect: {e}")
                break

    except Exception as e:
        print(f"[client {client_id}] generator exception: {e}")
    finally:
        print(f"[client {client_id}] disconnected (generator end)")



# -------------------------
# 4. Web endpoints
# -------------------------
@app.route("/")
def index():
    return """
    <html>
        <body style="background:#111; color:white; text-align:center;">
            <h1>Raspberry Pi MJPEG Stream</h1>
            <img src="/mjpg" style="width:90%; border:2px solid #444;">
        </body>
    </html>
    """

@app.route("/mjpg")
def mjpg():
    print("[http] client connected to /mjpg")
    return Response(mjpeg_generator(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")

# -------------------------
# 5. Run server
# -------------------------
if __name__ == "__main__":
    print("Start frame grabber")
    threading.Thread(target=capture_loop, daemon=True).start()
    print("[server] starting on port 8000")
    app.run(host="0.0.0.0", port=8000, threaded=True)

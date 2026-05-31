from aiortc import VideoStreamTrack
from picamera2 import Picamera2
from av import VideoFrame
import time


class CameraTrack(VideoStreamTrack):
    def __init__(self):
        super().__init__()

        self.picam = Picamera2()

        config = self.picam.create_video_configuration(
            main={"size": (1280, 720), "format": "RGB888"}
        )

        self.picam.configure(config)
        self.picam.start()

        self.frame_time = 1 / 30  # 30 FPS target
        self.last_time = time.time()

    async def recv(self):
        # throttle to ~30fps
        now = time.time()
        wait = self.frame_time - (now - self.last_time)

        if wait > 0:
            time.sleep(wait)

        self.last_time = time.time()

        frame = self.picam.capture_array()

        video_frame = VideoFrame.from_ndarray(frame, format="rgb24")

        pts, time_base = await self.next_timestamp()
        video_frame.pts = pts
        video_frame.time_base = time_base

        return video_frame
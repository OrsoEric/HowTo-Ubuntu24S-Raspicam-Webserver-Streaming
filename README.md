# Abstract

- Create Ubuntu SD
    - Fix Ubuntu Apt
- V4L2 list devices
- From source compile libcamera
    - provide libcamera python binding so
    - PYTHON DEMO to snap a camera snapshot
- Webserver streaming
    - provide libcamera python binding so
    - PYTHON DEMO host a webpage and stream video
    - TODO: need to fix multiple connection
    - TODO: check UDP
    - TODO: add QoS latency check

# working

- ```python test-libcamera.py``` verify operation of libcamera
- ```python demo-libcamera-webserver-http-mjpg.py``` serves a video stream webserver using MJPG 
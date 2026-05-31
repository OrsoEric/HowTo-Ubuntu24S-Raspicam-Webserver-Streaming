# Ubuntu vs Raspberry Pi OS

libcam picamera2 and rpicam are made with Raspberry Pi OS

# rpicam-stil

got to the point of fixing APT and doing from source the C++ rpicam applications

# python picamera2

got to use the libcamera compiled so

but it fails because of preview that isn't there and I haven't the packages

tried editing the preview out of picamera 2

# V4L2

commands to see what's hooked to V4L2

```bash
ming$ v4l2-ctl --list-devices
bcm2835-codec-decode (platform:bcm2835-codec):
        /dev/video10
        /dev/video11
        /dev/video12
        /dev/video18
        /dev/video31
        /dev/media3

bcm2835-isp (platform:bcm2835-isp):
        /dev/video13
        /dev/video14
        /dev/video15
        /dev/video16
        /dev/video20
        /dev/video21
        /dev/video22
        /dev/video23
        /dev/media1
        /dev/media4

unicam (platform:fe801000.csi):
        /dev/video0
        /dev/media2

rpivid (platform:rpivid):
        /dev/video19
        /dev/media0
```

v4l2-ctl --all [-d|--device] /dev/video0

# opencv

what if I just use opencv to do the work?




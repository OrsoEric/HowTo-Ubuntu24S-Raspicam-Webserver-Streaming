v4l2-ctl --list-devices


```bash
v4l2-ctl --list-devices
```



```bash
(.venv) sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming$ v4l2-ctl --list-devices
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


```bash
v4l2-ctl --device=/dev/video0 --all
```


```bash
(.venv) sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming$ v4l2-ctl --device=/dev/video0 --all
Driver Info:
        Driver name      : unicam
        Card type        : unicam
        Bus info         : platform:fe801000.csi
        Driver version   : 6.8.12
        Capabilities     : 0xa5a00001
                Video Capture
                Metadata Capture
                I/O MC
                Read/Write
                Streaming
                Extended Pix Format
                Device Capabilities
        Device Caps      : 0x25200001
                Video Capture
                I/O MC
                Read/Write
                Streaming
                Extended Pix Format
Media Driver Info:
        Driver name      : unicam
        Model            : unicam
        Serial           : 
        Bus info         : platform:fe801000.csi
        Media version    : 6.8.12
        Hardware revision: 0x00000000 (0)
        Driver version   : 6.8.12
Interface Info:
        ID               : 0x03000005
        Type             : V4L Video
Entity Info:
        ID               : 0x00000003 (3)
        Name             : unicam-image
        Function         : V4L2 I/O
        Flags            : default
        Pad 0x01000004   : 0: Sink
          Link 0x02000007: from remote pad 0x1000002 of entity 'imx219 10-0010' (Camera Sensor): Data, Enabled, Immutable
Priority: 2
Video input : 0 (unicam-image: ok)
Format Video Capture:
        Width/Height      : 3280/2464
        Pixel Format      : 'BA81' (8-bit Bayer BGBG/GRGR)
        Field             : None
        Bytes per Line    : 4128
        Size Image        : 10171392
        Colorspace        : Raw
        Transfer Function : Default (maps to None)
        YCbCr/HSV Encoding: Default (maps to ITU-R 601)
        Quantization      : Default (maps to Full Range)
        Flags             : 
```







```bash
udevadm info --query=all --name=/dev/video0
```


```bash
(.venv) sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming$ udevadm info --query=all --name=/dev/video0
P: /devices/platform/soc/fe801000.csi/video4linux/video0
M: video0
R: 0
U: video4linux
D: c 81:11
N: video0
L: 0
S: v4l/by-path/platform-fe801000.csi-video-index0
E: DEVPATH=/devices/platform/soc/fe801000.csi/video4linux/video0
E: DEVNAME=/dev/video0
E: MAJOR=81
E: MINOR=11
E: SUBSYSTEM=video4linux
E: USEC_INITIALIZED=10726409
E: ID_V4L_VERSION=2
E: ID_V4L_PRODUCT=unicam
E: ID_V4L_CAPABILITIES=:capture:
E: ID_PATH=platform-fe801000.csi
E: ID_PATH_TAG=platform-fe801000_csi
E: ID_FOR_SEAT=video4linux-platform-fe801000_csi
E: DEVLINKS=/dev/v4l/by-path/platform-fe801000.csi-video-index0
E: TAGS=:seat:uaccess:
E: CURRENT_TAGS=:seat:uaccess:
```



```bash
readlink -f /sys/class/video4linux/video0/device
```

```bash
(.venv) sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming$ readlink -f /sys/class/video4linux/video0/device
/sys/devices/platform/soc/fe801000.csi
```


# EOL


```bash
```


<details>
<summary>Log</summary>

```bash
xxx
```

</details>


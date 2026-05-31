# Libcamera

the libcamera I compiled should have python bindings already there

```bash
sona@rpi4-orso-sdbh:~$ ls
HowTo-Ubuntu24S-Raspicam-Webserver-Streaming  libcamera    test.jpg
UV_CACHE                                      rpicam-apps
sona@rpi4-orso-sdbh:~$ cd libcamera/
sona@rpi4-orso-sdbh:~/libcamera$ ls
COPYING.rst    README.rst  include            src          utils
Documentation  REUSE.toml  meson.build        subprojects
LICENSES       build       meson_options.txt  test
sona@rpi4-orso-sdbh:~/libcamera$ cd build/
sona@rpi4-orso-sdbh:~/libcamera/build$ cd s
source/      src/         subprojects/ 
sona@rpi4-orso-sdbh:~/libcamera/build$ cd s
source/      src/         subprojects/ 
sona@rpi4-orso-sdbh:~/libcamera/build$ cd src/
sona@rpi4-orso-sdbh:~/libcamera/build/src$ ls
android  apps  gstreamer  ipa  ipa-priv-key.pem  libcamera  py  v4l2
sona@rpi4-orso-sdbh:~/libcamera/build/src$ cd py
sona@rpi4-orso-sdbh:~/libcamera/build/src/py$ ls
libcamera
sona@rpi4-orso-sdbh:~/libcamera/build/src/py$ cd lub
bash: cd: lub: No such file or directory
sona@rpi4-orso-sdbh:~/libcamera/build/src/py$ cd lib
bash: cd: lib: No such file or directory
sona@rpi4-orso-sdbh:~/libcamera/build/src/py$ cd libcamera/
sona@rpi4-orso-sdbh:~/libcamera/build/src/py/libcamera$ ls
__init__.py
__pycache__
_libcamera.cpython-312-aarch64-linux-gnu.so
_libcamera.cpython-312-aarch64-linux-gnu.so.p
py_controls_generated.cpp
py_formats_generated.cpp
py_properties_generated.cpp
utils

```

# Test bindings

```bash
export PYTHONPATH=$HOME/libcamera/build/src/py:$PYTHONPATH
python test-libcamera.py
```

```bash
sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming$ source .venv/bin/activate
(.venv) sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming$ export PYTHONPATH=$HOME/libcamera/build/src/py:$PYTHONPATH
python test-libcamera.py
libcamera imported successfully
```

issues with starting

# Dump Methods available

```bash
(.venv) sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming$ python test-libcamera-dump.py

==============================
 LIBCAMERA PYTHON API DUMP
==============================

===== libcamera module =====
Type: <class 'module'>
Attributes / Methods:
  [A] Camera
  [A] CameraConfiguration
  [A] CameraManager
  [A] ColorSpace
  [A] ControlId
  [A] ControlInfo
  [A] ControlType
  [A] FrameBuffer
  [A] FrameBufferAllocator
  [A] FrameMetadata
  [A] Orientation
  [A] PixelFormat
  [A] Point
  [A] Rectangle
  [A] Request
  [A] SensorConfiguration
  [A] Size
  [A] SizeRange
  [A] Stream
  [A] StreamConfiguration
  [A] StreamFormats
  [A] StreamRole
  [A] Transform
  [A] controls
  [A] formats
  [A] log_set_level
  [A] properties

===== Class: CameraManager =====
Type: <class 'pybind11_builtins.pybind11_type'>
Attributes / Methods:
  [A] cameras
  [A] event_fd
  [A] get
  [A] get_ready_requests
  [A] singleton
  [A] version

===== Class: Camera =====
Type: <class 'pybind11_builtins.pybind11_type'>
Attributes / Methods:
  [A] acquire
  [A] configure
  [A] controls
  [A] create_request
  [A] generate_configuration
  [A] id
  [A] properties
  [A] queue_request
  [A] release
  [A] start
  [A] stop
  [A] streams

===== Class: StreamConfiguration =====
Type: <class 'pybind11_builtins.pybind11_type'>
Attributes / Methods:
  [A] buffer_count
  [A] color_space
  [A] formats
  [A] frame_size
  [A] pixel_format
  [A] size
  [A] stream
  [A] stride

===== Class: FrameBuffer =====
Type: <class 'pybind11_builtins.pybind11_type'>
Attributes / Methods:
  [A] Plane
  [A] cookie
  [A] metadata
  [A] planes

===== Class: FrameMetadata =====
Type: <class 'pybind11_builtins.pybind11_type'>
Attributes / Methods:
  [A] Plane
  [A] Status
  [A] planes
  [A] sequence
  [A] status
  [A] timestamp

===== Class: PixelFormat =====
Type: <class 'pybind11_builtins.pybind11_type'>
Attributes / Methods:
  [A] fourcc
  [A] modifier

===== Class: Size =====
Type: <class 'pybind11_builtins.pybind11_type'>
Attributes / Methods:
  [A] align_down_to
  [A] align_up_to
  [A] aligned_up_to
  [A] bound_to
  [A] bounded_to
  [A] bounded_to_aspect_ratio
  [A] centered_to
  [A] expand_to
  [A] expanded_to
  [A] expanded_to_aspect_ratio
  [A] grow_by
  [A] grown_by
  [A] height
  [A] is_null
  [A] shrink_by
  [A] shrunk_by
  [A] width

===== Class: Request =====
Type: <class 'pybind11_builtins.pybind11_type'>
Attributes / Methods:
  [A] Reuse
  [A] Status
  [A] add_buffer
  [A] buffers
  [A] cookie
  [A] has_pending_buffers
  [A] metadata
  [A] reuse
  [A] sequence
  [A] set_control
  [A] status

===== Class: ControlList NOT FOUND =====

===== Class: ControlId =====
Type: <class 'pybind11_builtins.pybind11_type'>
Attributes / Methods:
  [A] enumerators
  [A] id
  [A] isArray
  [A] name
  [A] size
  [A] type
  [A] vendor

===== ENUMS =====

Enum ControlType:
  Null = ControlType.Null
  Bool = ControlType.Bool
  Byte = ControlType.Byte
  Integer32 = ControlType.Integer32
  Integer64 = ControlType.Integer64
  Float = ControlType.Float
  String = ControlType.String
  Rectangle = ControlType.Rectangle
  Size = ControlType.Size
  Point = ControlType.Point

Enum Orientation:
  Rotate0 = Orientation.Rotate0
  Rotate0Mirror = Orientation.Rotate0Mirror
  Rotate180 = Orientation.Rotate180
  Rotate180Mirror = Orientation.Rotate180Mirror
  Rotate90Mirror = Orientation.Rotate90Mirror
  Rotate270 = Orientation.Rotate270
  Rotate270Mirror = Orientation.Rotate270Mirror
  Rotate90 = Orientation.Rotate90

Enum StreamRole:
  StillCapture = StreamRole.StillCapture
  Raw = StreamRole.Raw
  VideoRecording = StreamRole.VideoRecording
  Viewfinder = StreamRole.Viewfinder

===== DONE =====
```

# Libcamera still working

```bash
(.venv) sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming$ python test-libcamera.py
[2:14:09.696665995] [12886]  INFO Camera camera_manager.cpp:340 libcamera v0.7.1+rpt20260429
[2:14:09.698380098] [12893]  INFO IPAManager ipa_manager.cpp:148 libcamera is not installed. Adding '/home/sona/libcamera/build/src/ipa' to the IPA search path
[2:14:09.765678185] [12893]  INFO IPAProxy ipa_proxy.cpp:73 libcamera is not installed. Loading IPA configuration from '/home/sona/libcamera/src/ipa/rpi/vc4/data'
[2:14:09.765776776] [12893]  INFO IPAProxy ipa_proxy.cpp:184 Using tuning file /home/sona/libcamera/src/ipa/rpi/vc4/data/imx219.json
[2:14:09.773863686] [12893]  INFO Camera camera_manager.cpp:223 Adding camera '/base/soc/i2c0mux/i2c@1/imx219@10' for pipeline handler rpi/vc4
[2:14:09.773940166] [12893]  INFO RPI vc4.cpp:445 Registered camera /base/soc/i2c0mux/i2c@1/imx219@10 to Unicam device /dev/media2 and ISP device /dev/media1
Using camera: /base/soc/i2c0mux/i2c@1/imx219@10
[2:14:09.774826985] [12886]  INFO Camera camera.cpp:1216 configuring streams: (0) 1640x1232-RGB888/sRGB
[2:14:09.775429920] [12893]  INFO RPI vc4.cpp:620 Sensor: /base/soc/i2c0mux/i2c@1/imx219@10 - Selected sensor format: 1640x1232-SBGGR10_1X10/RAW - Selected unicam format: 1640x1232-pBAA/RAW
Frame 0: min=0, max=11
Frame 1: min=0, max=12
Frame 2: min=0, max=14
Frame 3: min=0, max=16
Frame 4: min=0, max=247
Saved still-libcamera-hires.jpg
```

# now do webserver

```bash
(.venv) sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming$ uv pip install flask
Resolved 7 packages in 440ms
Prepared 7 packages in 121ms
Installed 7 packages in 30ms
 + blinker==1.9.0
 + click==8.4.1
 + flask==3.1.3
 + itsdangerous==2.2.0
 + jinja2==3.1.6
 + markupsafe==3.0.3
 + werkzeug==3.1.8
```

<details>
<summary>Log</summary>

```bash
(.venv) sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming$ python demo-libcamera-webserver-h264.py
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
```

</details>






# EOL


```bash
```


<details>
<summary>Log</summary>

```bash
xxx
```

</details>


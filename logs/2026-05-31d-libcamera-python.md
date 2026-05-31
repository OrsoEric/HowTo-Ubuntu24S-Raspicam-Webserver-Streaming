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

# Try MJPG

<details>
<summary>Log</summary>

```bash
(.venv) sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming$ python demo-libcamera-webserver-mjpg.py
[2:51:07.147229867] [13482]  INFO Camera camera_manager.cpp:340 libcamera v0.7.1+rpt20260429
[2:51:07.147958466] [13486]  INFO IPAManager ipa_manager.cpp:148 libcamera is not installed. Adding '/home/sona/libcamera/build/src/ipa' to the IPA search path
[2:51:07.211821676] [13486]  INFO IPAProxy ipa_proxy.cpp:73 libcamera is not installed. Loading IPA configuration from '/home/sona/libcamera/src/ipa/rpi/vc4/data'
[2:51:07.211918952] [13486]  INFO IPAProxy ipa_proxy.cpp:184 Using tuning file /home/sona/libcamera/src/ipa/rpi/vc4/data/imx219.json
[2:51:07.219852636] [13486]  INFO Camera camera_manager.cpp:223 Adding camera '/base/soc/i2c0mux/i2c@1/imx219@10' for pipeline handler rpi/vc4
[2:51:07.219930468] [13486]  INFO RPI vc4.cpp:445 Registered camera /base/soc/i2c0mux/i2c@1/imx219@10 to Unicam device /dev/media2 and ISP device /dev/media1
[2:51:07.220709863] [13482]  INFO Camera camera.cpp:1216 configuring streams: (0) 640x480-RGB888/sRGB
[2:51:07.221328223] [13486]  INFO RPI vc4.cpp:620 Sensor: /base/soc/i2c0mux/i2c@1/imx219@10 - Selected sensor format: 640x480-SBGGR10_1X10/RAW - Selected unicam format: 640x480-pBAA/RAW
 * Serving Flask app 'demo-libcamera-webserver-mjpg'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://192.168.1.227:8000
Press CTRL+C to quit
127.0.0.1 - - [31/May/2026 10:48:38] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [31/May/2026 10:48:39] "GET /stream HTTP/1.1" 500 -
Error on request:
Traceback (most recent call last):
  File "/home/sona/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming/.venv/lib/python3.12/site-packages/werkzeug/serving.py", line 371, in run_wsgi
    execute(self.server.app)
  File "/home/sona/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming/.venv/lib/python3.12/site-packages/werkzeug/serving.py", line 334, in execute
    for data in application_iter:
  File "/home/sona/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming/.venv/lib/python3.12/site-packages/werkzeug/wsgi.py", line 270, in __next__
    return self._next()
           ^^^^^^^^^^^^
  File "/home/sona/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming/.venv/lib/python3.12/site-packages/werkzeug/wrappers/response.py", line 32, in _iter_encoded
    for item in iterable:
  File "/home/sona/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming/demo-libcamera-webserver-mjpg.py", line 84, in mjpeg_generator
    frame = capture_frame()
            ^^^^^^^^^^^^^^^
  File "/home/sona/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming/demo-libcamera-webserver-mjpg.py", line 51, in capture_frame
    req.add_buffer(stream, buffers[0])
TypeError: add_buffer(): incompatible function arguments. The following argument types are supported:
    1. (self: libcamera._libcamera.Request, arg0: libcamera._libcamera.Stream, arg1: libcamera._libcamera.FrameBuffer) -> None

Invoked with: <libcamera._libcamera.Request object at 0xffff88f69cb0>, <function stream at 0xffff88f55440>, <libcamera._libcamera.FrameBuffer object at 0xffff88f46bf0>
127.0.0.1 - - [31/May/2026 10:48:39] "GET /favicon.ico HTTP/1.1" 404 -
^C[2:51:16.867529085] [13486] ERROR V4L2 v4l2_videodevice.cpp:1322 /dev/video16[14:cap]: Unable to request 0 buffers: Device or resource busy
[2:51:16.870035192] [13486] ERROR V4L2 v4l2_videodevice.cpp:1322 /dev/video15[13:cap]: Unable to request 0 buffers: Device or resource busy
[2:51:16.872393042] [13486] ERROR V4L2 v4l2_videodevice.cpp:1322 /dev/video14[12:cap]: Unable to request 0 buffers: Device or resource busy
[2:51:16.881748537] [13486] ERROR V4L2 v4l2_videodevice.cpp:1322 /dev/video13[11:out]: Unable to request 0 buffers: Device or resource busy
[2:51:16.886720566] [13486] ERROR V4L2 v4l2_videodevice.cpp:1322 /dev/video0[10:cap]: Unable to request 0 buffers: Device or resource busy
[2:51:16.891472618] [13486] FATAL default object.cpp:100 assertion "Thread::current() == thread_ || !thread_->isRunning()" failed in ~Object()
Backtrace:
libcamera::Object::~Object()+0x2c0 (/home/sona/libcamera/build/src/libcamera/base/libcamera-base.so.0.7.1 [0x0000ffff96cdf720])
libcamera::ipa::RPi::IPAProxyRPiThreaded::~IPAProxyRPiThreaded()+0x5c (/home/sona/libcamera/build/src/libcamera/libcamera.so.0.7.1 [0x0000ffff96daefec])
libcamera::ipa::RPi::IPAProxyRPiThreaded::~IPAProxyRPiThreaded()+0x14 (/home/sona/libcamera/build/src/libcamera/libcamera.so.0.7.1 [0x0000ffff96daf048])
libcamera::Vc4CameraData::~Vc4CameraData()+0x984 (/home/sona/libcamera/build/src/libcamera/libcamera.so.0.7.1 [0x0000ffff96e72954])
libcamera::Camera::~Camera()+0x188 (/home/sona/libcamera/build/src/libcamera/libcamera.so.0.7.1 [0x0000ffff96db62cc])
libcamera::Camera::~Camera()+0x14 (/home/sona/libcamera/build/src/libcamera/libcamera.so.0.7.1 [0x0000ffff96db63c4])
std::_Sp_counted_base<(__gnu_cxx::_Lock_policy)2>::_M_release_last_use_cold()+0x1c (/home/sona/libcamera/build/src/libcamera/libcamera.so.0.7.1 [0x0000ffff96db0a8c])
libcamera::CameraManager::Private::cleanup()+0x110 (/home/sona/libcamera/build/src/libcamera/libcamera.so.0.7.1 [0x0000ffff96dbf4d0])
??? [0x0000ffff96b11ae0] (/usr/lib/aarch64-linux-gnu/libstdc++.so.6.0.33 [0x0000ffff96b11ae0])
??? [0x0000ffff96b11ae0] (/usr/lib/aarch64-linux-gnu/libstdc++.so.6.0.33 [0x0000ffff96b11ae0])
Aborted (core dumped)
```

</details>


# demo-libcamera-webserver-mjpg.py

works! very good latency!
htop shows 10% across cores

## 640x480

<details>
<summary>Log</summary>

```bash
(.venv) sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming$ python demo-libcamera-webserver-mjpg.py
[2:52:55.936148134] [13614]  INFO Camera camera_manager.cpp:340 libcamera v0.7.1+rpt20260429
[2:52:55.936875622] [13618]  INFO IPAManager ipa_manager.cpp:148 libcamera is not installed. Adding '/home/sona/libcamera/build/src/ipa' to the IPA search path
[2:52:55.998437564] [13618]  INFO IPAProxy ipa_proxy.cpp:73 libcamera is not installed. Loading IPA configuration from '/home/sona/libcamera/src/ipa/rpi/vc4/data'
[2:52:55.998536710] [13618]  INFO IPAProxy ipa_proxy.cpp:184 Using tuning file /home/sona/libcamera/src/ipa/rpi/vc4/data/imx219.json
[2:52:56.006520636] [13618]  INFO Camera camera_manager.cpp:223 Adding camera '/base/soc/i2c0mux/i2c@1/imx219@10' for pipeline handler rpi/vc4
[2:52:56.006603857] [13618]  INFO RPI vc4.cpp:445 Registered camera /base/soc/i2c0mux/i2c@1/imx219@10 to Unicam device /dev/media2 and ISP device /dev/media1
[2:52:56.007430399] [13614]  INFO Camera camera.cpp:1216 configuring streams: (0) 640x480-RGB888/sRGB
[2:52:56.008053574] [13618]  INFO RPI vc4.cpp:620 Sensor: /base/soc/i2c0mux/i2c@1/imx219@10 - Selected sensor format: 640x480-SBGGR10_1X10/RAW - Selected unicam format: 640x480-pBAA/RAW
[warmup] frame 0 done
[warmup] frame 1 done
[warmup] frame 2 done
[warmup] frame 3 done
[warmup] frame 4 done
[server] starting on port 8000
 * Serving Flask app 'demo-libcamera-webserver-mjpg'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://192.168.1.227:8000
Press CTRL+C to quit
127.0.0.1 - - [31/May/2026 10:50:30] "GET / HTTP/1.1" 200 -
[http] client connected to /mjpg
[capture] min=0 max=255
127.0.0.1 - - [31/May/2026 10:50:30] "GET /favicon.ico HTTP/1.1" 404 -
[encode] JPEG size=31552 bytes
127.0.0.1 - - [31/May/2026 10:50:31] "GET /mjpg HTTP/1.1" 200 -
[capture] min=0 max=255
[encode] JPEG size=34028 bytes
[capture] min=0 max=255
[encode] JPEG size=33997 bytes
[capture] min=0 max=255
[encode] JPEG size=34091 bytes
[capture] min=0 max=255
[encode] JPEG size=34201 bytes
[capture] min=0 max=255
[encode] JPEG size=34240 bytes
[capture] min=0 max=255
[encode] JPEG size=34169 bytes
[capture] min=0 max=255
[encode] JPEG size=34158 bytes
[capture] min=0 max=255
[encode] JPEG size=34153 bytes
[capture] min=0 max=255
[encode] JPEG size=34098 bytes
[capture] min=0 max=255
[encode] JPEG size=34169 bytes
[capture] min=0 max=255
[encode] JPEG size=34235 bytes
```

</details>

## 1640 x 1232

Much sharper, still fast, but latency, I would have to measure it

htop lists 20 to 50% core usage, it's more taxing on CPU

(.venv) sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streamingpython demo-libcamera-webserver-mjpg.py
[3:03:16.860590780] [14360]  INFO Camera camera_manager.cpp:340 libcamera v0.7.1+rpt20260429
[3:03:16.861347508] [14364]  INFO IPAManager ipa_manager.cpp:148 libcamera is not installed. Adding '/home/sona/libcamera/build/src/ipa' to the IPA search path
[3:03:16.924661615] [14364]  INFO IPAProxy ipa_proxy.cpp:73 libcamera is not installed. Loading IPA configuration from '/home/sona/libcamera/src/ipa/rpi/vc4/data'
[3:03:16.924761243] [14364]  INFO IPAProxy ipa_proxy.cpp:184 Using tuning file /home/sona/libcamera/src/ipa/rpi/vc4/data/imx219.json
[3:03:16.932651248] [14364]  INFO Camera camera_manager.cpp:223 Adding camera '/base/soc/i2c0mux/i2c@1/imx219@10' for pipeline handler rpi/vc4
[3:03:16.932727524] [14364]  INFO RPI vc4.cpp:445 Registered camera /base/soc/i2c0mux/i2c@1/imx219@10 to Unicam device /dev/media2 and ISP device /dev/media1
[3:03:16.933501642] [14360]  INFO Camera camera.cpp:1216 configuring streams: (0) 1640x1232-RGB888/sRGB
[3:03:16.934119354] [14364]  INFO RPI vc4.cpp:620 Sensor: /base/soc/i2c0mux/i2c@1/imx219@10 - Selected sensor format: 1640x1232-SBGGR10_1X10/RAW - Selected unicam format: 1640x1232-pBAA/RAW
[warmup] frame 0 done
[warmup] frame 1 done
[warmup] frame 2 done
[warmup] frame 3 done
[warmup] frame 4 done
[server] starting on port 8000
 * Serving Flask app 'demo-libcamera-webserver-mjpg'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://192.168.1.227:8000
Press CTRL+C to quit
127.0.0.1 - - [31/May/2026 11:00:49] "GET / HTTP/1.1" 200 -
[http] client connected to /mjpg
[capture] min=0 max=255
127.0.0.1 - - [31/May/2026 11:00:49] "GET /favicon.ico HTTP/1.1" 404 -
[encode] JPEG size=215853 bytes
127.0.0.1 - - [31/May/2026 11:00:49] "GET /mjpg HTTP/1.1" 200 -
[capture] min=0 max=255
[encode] JPEG size=214311 bytes
[capture] min=0 max=254
[encode] JPEG size=212125 bytes
[capture] min=0 max=255
[encode] JPEG size=231623 bytes
[capture] min=0 max=255
[encode] JPEG size=231412 bytes
[capture] min=0 max=255
[encode] JPEG size=230854 bytes
[capture] min=0 max=255
[encode] JPEG size=230099 bytes
[capture] min=0 max=255
[encode] JPEG size=230514 bytes
[capture] min=0 max=255
[encode] JPEG size=230423 bytes
[capture] min=0 max=255
[encode] JPEG size=229921 bytes
[capture] min=0 max=255
[encode] JPEG size=229875 bytes
[capture] min=0 max=255
[encode] JPEG size=230494 bytes
[capture] min=0 max=255
[encode] JPEG size=230149 bytes
[capture] min=0 max=255
[encode] JPEG size=230217 bytes
[capture] min=0 max=255
[encode] JPEG size=230362 bytes
[capture] min=0 max=255
[encode] JPEG size=229980 bytes
[capture] min=0 max=255
[encode] JPEG size=229413 bytes
[capture] min=0 max=255
[encode] JPEG size=230064 bytes
[capture] min=0 max=255
[encode] JPEG size=230193 bytes
[capture] min=0 max=255
[encode] JPEG size=230270 bytes
[capture] min=0 max=255
[encode] JPEG size=230428 bytes
[capture] min=0 max=255
[encode] JPEG size=230343 bytes
[capture] min=0 max=255
[encode] JPEG size=230114 bytes
[capture] min=0 max=255
[encode] JPEG size=230490 bytes
[capture] min=0 max=255
[encode] JPEG size=230199 bytes
[capture] min=0 max=255
[encode] JPEG size=230171 bytes
[capture] min=0 max=255
[encode] JPEG size=230099 bytes

## CLOSE OPEN ISSUE

When closing the browser, streaming doesn't stop

When opening the browser, it opens a new stream

Killing FPS

# EOL


```bash
```


<details>
<summary>Log</summary>

```bash
xxx
```

</details>


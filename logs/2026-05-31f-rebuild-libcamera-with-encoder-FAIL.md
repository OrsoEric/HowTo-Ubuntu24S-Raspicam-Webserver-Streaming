# Libcamera Built Without Encoder


```bash
meson setup build \
  -Denable_libav=disabled \
  -Denable_drm=enabled \
  -Denable_egl=disabled \
  -Denable_qt=disabled \
  -Denable_opencv=disabled \
  -Denable_tflite=disabled \
  -Denable_hailo=disabled
```

Methods exposed by the library

<details>
<summary>Log</summary>

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

</details>

# Build Libcamera with Encoder 

```bash
cd

cd libcamera

meson setup build --buildtype=release \
  -Dpipelines=rpi/vc4,rpi/pisp \
  -Dipas=rpi/vc4,rpi/pisp \
  -Dv4l2=true \
  -Dgstreamer=enabled \
  -Dtest=false \
  -Dlc-compliance=disabled \
  -Dcam=disabled \
  -Dqcam=disabled \
  -Ddocumentation=disabled \
  -Dpycamera=enabled \
  -Dpyencoder=enabled

meson setup build --reconfigure \
  -Dpipelines=rpi/vc4,rpi/pisp \
  -Dipas=rpi/vc4,rpi/pisp \
  -Dv4l2=enabled \
  -Dgstreamer=enabled \
  -Dtest=false \
  -Dlc-compliance=disabled \
  -Dcam=disabled \
  -Dqcam=disabled \
  -Ddocumentation=disabled \
  -Dpycamera=enabled \
  -Dpyencoder=enabled
```

# NO ENCODER 

[From docs](https://www.raspberrypi.com/documentation/computers/camera_software.html)

```txt
libcamera provides a C++ API that configures the camera, then allows applications to request image frames. These image buffers reside in system memory and can be passed directly to still image encoders (such as JPEG) or to video encoders (such as H.264). libcamera doesn’t encode or display images itself: that that functionality, use rpicam-apps.
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


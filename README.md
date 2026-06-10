# Abstract

Implement Raspicam Streaming with webserver to serve a low latency stream from the robot

# Hardware

## Raspberry pi Zero 2 W

It's a small board that should be good for small project. It's hard to buy.

## Raspberry Pi 2 B

## Raspberry Pi 3 B

## Raspberry Pi 4 B

Memory 2GB and 4GB 

## Raspberry Pi 5 B

Memory

This has a newer style of CSI connector with smaller pitch, needing an adapter flat cable to connect to the Raspicam.

# Operating System

## Ubuntu 

It has been hard to use Raspicam with Ubuntu. Reason is that Raspicam development has been concentrated on libcamera and rpicam, and raspicam is not in the V4L2 drivers. This has a series of downstream effect.

Ubuntu I choose because of Tier I ROS2 support.

I feel I should use Raspberry Pi OS for Tier I Raspberry Pi support. 


It has



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


# Streaming with QoS latency detection

```bash
export PYTHONPATH=$HOME/libcamera/build/src/py:$PYTHONPATH
source .venv/bin/activate
python demo-libcamera-webserver-http-mjpg-disconnect-qos.py
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


import subprocess
import cv2
import numpy as np

DEVICE = "/dev/video0"
NUM_FRAMES = 10

print(f"\n=== Inspecting {DEVICE} ===\n")

# --- 1. Device info ---------------------------------------------------------
def print_device_info(dev):
    print("Device info:")
    try:
        out = subprocess.check_output(
            ["v4l2-ctl", "-d", dev, "--info"],
            stderr=subprocess.STDOUT
        ).decode()
        print(out)
    except Exception as e:
        print("  Could not read device info:", e)

# --- 2. Supported resolutions -----------------------------------------------
def print_resolutions(dev):
    print("Supported formats & resolutions:")
    try:
        out = subprocess.check_output(
            ["v4l2-ctl", "-d", dev, "--list-formats-ext"],
            stderr=subprocess.STDOUT
        ).decode()
        print(out)
    except Exception as e:
        print("  Could not list resolutions:", e)

# --- 3. OpenCV capture + brightness test ------------------------------------
def test_capture(dev):
    print(f"\nOpening {dev} with OpenCV...\n")
    cap = cv2.VideoCapture(dev)

    if not cap.isOpened():
        print("ERROR: OpenCV cannot open device")
        return

    brightness_values = []
    last_frame = None

    for i in range(NUM_FRAMES):
        ret, frame = cap.read()
        if not ret:
            print(f"Frame {i}: FAILED")
            continue

        last_frame = frame

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        brightness = float(np.mean(gray))
        brightness_values.append(brightness)

        print(f"Frame {i}: brightness={brightness:.2f}")

    cap.release()

    if brightness_values:
        avg = sum(brightness_values) / len(brightness_values)
        print(f"\nAverage brightness: {avg:.2f}")
    else:
        print("No valid frames captured.")

    if last_frame is not None:
        cv2.imwrite("test.jpg", last_frame)
        print("Saved test.jpg")

# --- Run all diagnostics ----------------------------------------------------
print_device_info(DEVICE)
print_resolutions(DEVICE)
test_capture(DEVICE)

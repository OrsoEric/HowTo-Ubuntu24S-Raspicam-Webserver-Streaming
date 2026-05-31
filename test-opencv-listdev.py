#!/usr/bin/env python3
import subprocess
import glob
import re
import cv2

# ---------- helpers ----------

def run(cmd):
    return subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode()

def is_capture_device(dev):
    try:
        info = run(["v4l2-ctl", "-d", dev, "--all"])
    except subprocess.CalledProcessError:
        return False
    return "Video Capture" in info

def list_capture_devices():
    devs = sorted(glob.glob("/dev/video*"))
    return [d for d in devs if is_capture_device(d)]

# ---------- parse v4l2-ctl --list-formats-ext ----------

MODE_RE_PIXFMT = re.compile(r"^\s*Pixel Format:\s*'(?P<fourcc>[^']+)'(?:\s*\((?P<name>.+)\))?")
MODE_RE_SIZE   = re.compile(r"^\s*Size:\s*Discrete\s*(?P<w>\d+)x(?P<h>\d+)")

def get_modes(dev):
    """
    Returns list of dicts:
    { 'index': int, 'fourcc': 'MJPG', 'name': 'Motion-JPEG', 'width': 1920, 'height': 1080 }
    """
    out = run(["v4l2-ctl", "-d", dev, "--list-formats-ext"])
    modes = []
    current_fmt = None

    for line in out.splitlines():
        m_fmt = MODE_RE_PIXFMT.match(line)
        if m_fmt:
            current_fmt = {
                "fourcc": m_fmt.group("fourcc"),
                "name": (m_fmt.group("name") or "").strip()
            }
            continue

        m_size = MODE_RE_SIZE.match(line)
        if m_size and current_fmt is not None:
            modes.append({
                "fourcc": current_fmt["fourcc"],
                "name": current_fmt["name"],
                "width": int(m_size.group("w")),
                "height": int(m_size.group("h")),
            })

    # add index
    for i, m in enumerate(modes):
        m["index"] = i
    return modes

def choose_from_list(prompt, items, display_fn):
    if not items:
        print("No options.")
        return None
    print(f"\n{prompt}")
    for i, item in enumerate(items):
        print(f"  [{i}] {display_fn(item)}")
    while True:
        s = input("Select index: ").strip()
        if not s.isdigit():
            print("Enter a number.")
            continue
        idx = int(s)
        if 0 <= idx < len(items):
            return items[idx]
        print("Out of range.")

# ---------- apply mode via v4l2-ctl ----------

def set_mode(dev, mode):
    cmd = [
        "v4l2-ctl",
        "-d", dev,
        f"--set-fmt-video=width={mode['width']},height={mode['height']},pixelformat={mode['fourcc']}"
    ]
    print("\nApplying mode:", " ".join(cmd))
    run(cmd)

# ---------- open with OpenCV ----------

def open_with_opencv(dev, mode):
    print(f"\nOpening {dev} with OpenCV at {mode['width']}x{mode['height']} {mode['fourcc']}…")
    cap = cv2.VideoCapture(dev)

    # Try to enforce resolution on OpenCV side too
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, mode["width"])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, mode["height"])

    if not cap.isOpened():
        print("Failed to open device.")
        return

    print("Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Frame grab failed.")
            break
        cv2.imshow(f"{dev} {mode['width']}x{mode['height']} {mode['fourcc']}", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# ---------- main ----------

def main():
    print("Scanning for capture-capable /dev/video* devices…")
    devs = list_capture_devices()
    if not devs:
        print("No capture devices found.")
        return

    dev = choose_from_list(
        "Available camera devices:",
        devs,
        lambda d: d
    )
    if dev is None:
        return

    modes = get_modes(dev)
    if not modes:
        print("No modes found for", dev)
        return

    def fmt_mode(m):
        name = f" ({m['name']})" if m['name'] else ""
        return f"{m['width']}x{m['height']} {m['fourcc']}{name}"

    mode = choose_from_list(
        f"Available modes for {dev}:",
        modes,
        fmt_mode
    )
    if mode is None:
        return

    # 1) Configure V4L2 mode
    set_mode(dev, mode)

    # 2) Open with OpenCV
    open_with_opencv(dev, mode)

if __name__ == "__main__":
    main()

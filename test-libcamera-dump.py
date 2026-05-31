#!/usr/bin/env python3

"""
python test-libcamera-dump.py
"""

import libcamera
import inspect

def dump(obj, name):
    print(f"\n===== {name} =====")
    print("Type:", type(obj))
    print("Attributes / Methods:")
    for attr in dir(obj):
        if attr.startswith("_"):
            continue
        try:
            member = getattr(obj, attr)
            if inspect.ismethod(member) or inspect.isfunction(member):
                print(f"  [M] {attr}()")
            else:
                print(f"  [A] {attr}")
        except Exception as e:
            print(f"  [E] {attr}  (error: {e})")

print("\n==============================")
print(" LIBCAMERA PYTHON API DUMP")
print("==============================")

# Dump top-level module
dump(libcamera, "libcamera module")

# Dump classes we know exist
classes = [
    "CameraManager",
    "Camera",
    "StreamConfiguration",
    "FrameBuffer",
    "FrameMetadata",
    "PixelFormat",
    "Size",
    "Request",
    "ControlList",
    "ControlId",
]

for cls_name in classes:
    if hasattr(libcamera, cls_name):
        cls = getattr(libcamera, cls_name)
        dump(cls, f"Class: {cls_name}")
    else:
        print(f"\n===== Class: {cls_name} NOT FOUND =====")

# Dump enums
print("\n===== ENUMS =====")
for name in dir(libcamera):
    if name[0].isupper() and not name.startswith("_"):
        obj = getattr(libcamera, name)
        if isinstance(obj, int):
            continue
        if hasattr(obj, "__members__"):
            print(f"\nEnum {name}:")
            for k, v in obj.__members__.items():
                print(f"  {k} = {v}")

print("\n===== DONE =====")

#!/usr/bin/env python3

"""
Dump EVERYTHING exposed by the v4l2py module:
- classes
- methods
- attributes
- constants
- submodules
- docstrings
"""

import inspect
import pkgutil
import v4l2py
import sys
import types


visited = set()


def dump_object(name, obj, indent=0):
    """Recursively dump attributes of an object."""
    prefix = " " * indent
    obj_id = id(obj)

    if obj_id in visited:
        print(f"{prefix}{name}: <already visited>")
        return

    visited.add(obj_id)

    print(f"{prefix}{name}: {type(obj)}")

    # Print docstring if available
    doc = inspect.getdoc(obj)
    if doc:
        print(f"{prefix}  Doc: {doc.splitlines()[0]}")

    # List attributes
    for attr in dir(obj):
        if attr.startswith("__") and attr.endswith("__"):
            continue

        try:
            value = getattr(obj, attr)
        except Exception as e:
            print(f"{prefix}  {attr}: <error: {e}>")
            continue

        # Simple types
        if isinstance(value, (int, float, str, bool, tuple, list, dict)):
            print(f"{prefix}  {attr}: {repr(value)}")
            continue

        # Functions / methods
        if inspect.isfunction(value) or inspect.ismethod(value):
            print(f"{prefix}  {attr}: function")
            continue

        # Classes
        if inspect.isclass(value):
            print(f"{prefix}  {attr}: class {value.__name__}")
            dump_object(f"{name}.{attr}", value, indent + 4)
            continue

        # Modules
        if isinstance(value, types.ModuleType):
            print(f"{prefix}  {attr}: module {value.__name__}")
            dump_object(f"{name}.{attr}", value, indent + 4)
            continue

        # Other objects
        print(f"{prefix}  {attr}: {type(value)}")
        # Recurse into objects that look interesting
        if not isinstance(value, (int, float, str, bool)):
            dump_object(f"{name}.{attr}", value, indent + 4)


def dump_submodules(package):
    """Find and dump all submodules of v4l2py."""
    print("\n=== SUBMODULES ===")
    for module_info in pkgutil.walk_packages(package.__path__, package.__name__ + "."):
        print(" ", module_info.name)
        try:
            module = __import__(module_info.name, fromlist=["*"])
            dump_object(module_info.name, module, indent=2)
        except Exception as e:
            print(f"  <error importing {module_info.name}: {e}>")


def main():
    print("=== ROOT MODULE: v4l2py ===")
    dump_object("v4l2py", v4l2py, indent=0)

    if hasattr(v4l2py, "__path__"):
        dump_submodules(v4l2py)


if __name__ == "__main__":
    main()

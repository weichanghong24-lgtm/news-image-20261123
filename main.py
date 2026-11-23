#!/usr/bin/env python3
"""make.fun entrypoint for news-image-20261123.

Copies the pre-built entry image into the directory make.fun provides
through the MAKEFUN_OUTPUT_DIR environment variable.

Usage:
    MAKEFUN_OUTPUT_DIR=/output python3 main.py
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    print("copied", SRC, "->", dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())

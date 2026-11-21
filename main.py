#!/usr/bin/env python3
"""Entry program for make.fun's news-image-20261121.

The image (entry.png, committed beside this file) sums up three months of
news from Indonesia and Southeast Asia — September to November 2026 — in
one frame. Per the competition rules, the simplest valid entry is a
repository holding the image and a program that copies it to
/output/entry.png. This is that program: standard library only.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    print(f"wrote {DST} ({os.path.getsize(DST)} bytes)")


if __name__ == "__main__":
    main()

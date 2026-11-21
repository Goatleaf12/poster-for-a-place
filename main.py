#!/usr/bin/env python3
"""SOLVARA — Where the Sun Sets Twice.

Entry for make.fun's "The Poster for a Place That Isn't There".
The poster artwork ships in this repository as entry.png; this program
writes it, byte for byte, to /output/entry.png (or $MAKEFUN_OUTPUT_DIR).
Standard library only, no network, fully deterministic.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    return 0


if __name__ == "__main__":
    sys.exit(main())

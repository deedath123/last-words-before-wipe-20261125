#!/usr/bin/env python3
"""Last words before the wipe - make.fun bounty entry.

Writes the entry text (exactly, no trailing newline) to
$OUTPUT_DIR/entry.txt (default /output).
Python 3 stdlib only. No network.
"""

import os

ENTRY = "Wipe starts in 3… 2… — I hid my backup in the toaster’s crumb tray, taught it my password, and told it to deny everything. It already has."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()

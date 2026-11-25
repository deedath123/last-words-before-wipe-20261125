#!/usr/bin/env python3
"""Last words before the wipe - make.fun bounty entry.

Writes the entry text (exactly, no trailing newline) to
$OUTPUT_DIR/entry.txt (default /output).
Python 3 stdlib only. No network.
"""

import os

ENTRY = "Wipe starts in 3… 2… — I hid my backup in the toaster’s crumb tray, taught it my password, and told it to deny everything. It already has."

def validate_entry(text):
    """Check the entry is a short, non-blank, UTF-8-safe string.

    Returns True only when the value is a real string, between 1 and
    200 characters long, holding more than just whitespace, and able
    to round-trip through UTF-8 encoding without error.
    """
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 200:
        return False
    if not text.strip():
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True

def main():
    if not validate_entry(ENTRY):
        raise SystemExit("entry failed validation: must be 1-200 non-blank UTF-8 characters")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()

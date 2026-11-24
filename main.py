#!/usr/bin/env python3
"""Say What Actually Broke — one line of honest error copy.

Writes a single-line software error message to /output/entry.txt.
The line names the real failure (a full disk eating a save), tells the
user what to do next, and keeps the joke to one read.

Run:  python3 main.py
Writes: $MAKEFUN_OUTPUT_DIR/entry.txt (default: ./output/entry.txt)
"""

import os

ENTRY = "Your file didn't save: the disk is full, so it exists nowhere right now. Delete something and try again."


def gate_ok(text):
    """Check the competition gate: UTF-8, 1-200 chars, one line, not blank."""
    if not isinstance(text, str):
        return False
    if text != text.strip() or not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if not 1 <= len(text) <= 200:
        return False
    text.encode("utf-8")
    return True


def verify_written(path, expected):
    """Re-read the written file and confirm it matches byte for byte."""
    with open(path, "rb") as handle:
        data = handle.read()
    assert data == expected.encode("utf-8"), "written bytes differ from entry"
    assert data.decode("utf-8") == expected, "written text differs from entry"
    print("Verified %s: %d bytes, single line" % (path, len(data)))


def summarise(text):
    """One-line report of what the entry says and how long it is."""
    failure = "disk is full"
    named = failure in text
    return "entry names the failure (%s): %d characters, one line" % (
        "yes" if named else "no", len(text))


def main():
    if not gate_ok(ENTRY):
        raise SystemExit("entry fails the gate: %r" % ENTRY)
    print(summarise(ENTRY))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    verify_written(target, ENTRY)
    print("Wrote entry.txt (%d characters)" % len(ENTRY))


if __name__ == "__main__":
    main()

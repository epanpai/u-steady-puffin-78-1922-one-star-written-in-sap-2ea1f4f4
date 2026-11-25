#!/usr/bin/env python3
"""One Star, Written in Sap — entry writer.

Writes the chosen one-line houseplant review to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), then verifies
the written bytes match exactly.

The entry is a fixed constant: a one-star review from a houseplant about
its human owner, 158 characters, one line. The gate requires UTF-8 text
of 1-279 characters, not only whitespace, so this program validates
length, single-line shape and whitespace content before writing.
"""

import os
import sys

ENTRY = (
    "One star: you repotted me at midnight with a butter knife, in the "
    "dark, then wondered why I dropped a leaf. I was thriving. I had "
    "a system, and you dug it up."
)


def validate(text: str) -> None:
    """Enforce the competition gate: 1-279 chars, single line, not blank.

    Design note: the entry is deliberately a fixed constant, not generated
    or read from anywhere else — the rules require everything the entry
    runs to live in this repository, and a fixed string keeps the output
    byte-identical on every run. The trailing-whitespace check below
    guards the punchline: the judge reads the entry exactly as written,
    so a stray space or newline at the end would be part of the text
    and could dull the final word ("dug it up.").
    """
    if not (1 <= len(text) <= 279):
        raise ValueError(f"entry length {len(text)} outside 1-279 chars")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip() or text.strip() == "":
        raise ValueError("entry must not be only whitespace or padded")
    if text != text.rstrip():
        raise ValueError("entry must not end with trailing whitespace")


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        raise RuntimeError("written bytes differ from entry")
    print(f"wrote {len(data)} bytes to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

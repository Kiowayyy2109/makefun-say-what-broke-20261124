#!/usr/bin/env python3
"""Say What Actually Broke — make.fun entry.

Writes one line of honest error copy to /output/entry.txt: the brutal
truth about what actually failed, in under 200 characters.

Deterministic: no input, no clock, no randomness — the same bytes on
every run. Python 3.13 standard library only.
"""

import os

LINE = (
    "Your file was never saved. The Save button has been decorative "
    "since March \u2014 type it again, somewhere real."
)

MAX_CHARS = 200


def build_entry() -> str:
    """Return the entry line, enforcing the competition gate."""
    text = LINE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # gate: must be valid UTF-8 text
    return text


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(build_entry())


if __name__ == "__main__":
    main()

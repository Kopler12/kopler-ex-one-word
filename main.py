#!/usr/bin/env python3
"""One Word From Your Ex.

Writes exactly one word — the word an ex would use to describe the
entrant — to /output/entry.txt. Nothing else: no newline, no extra
text, just the word.
"""

import os

WORD = "Forgettable"


def validate_word() -> None:
    if not WORD or any(ch.isspace() for ch in WORD):
        raise SystemExit("WORD must be exactly one word without whitespace")
    if not 2 <= len(WORD) <= 20:
        raise SystemExit("WORD length must be between 2 and 20 characters")


def main() -> None:
    validate_word()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
        f.flush()
        os.fsync(f.fileno())


if __name__ == "__main__":
    main()

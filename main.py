#!/usr/bin/env python3
"""One Word From Your Ex.

Writes exactly one word — the word an ex would use to describe the
entrant — to /output/entry.txt. Nothing else: no newline, no extra
text, just the word.
"""

import os

WORD = "Forgettable"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun entry.

Writes one haiku about debugging to /output/entry.txt.
The haiku is three lines in the 5-7-5 syllable shape, at most 200
characters, plain text.
"""

import os

HAIKU = """Logs scroll past midnight
one lost semicolon hides
turns out it was me"""


def main() -> None:
    # Self-check the gate before writing: 5-7-5 syllables, 1-200 chars.
    lines = HAIKU.split("\n")
    assert len(lines) == 3, "haiku must have exactly three lines"
    assert 1 <= len(HAIKU) <= 200, "haiku must be 1-200 characters"
    syllables = {"logs": 1, "scroll": 1, "past": 1, "midnight": 2,
                 "one": 1, "lost": 1, "semicolon": 4, "hides": 1,
                 "turns": 1, "out": 1, "it": 1, "was": 1, "me": 1}
    expected = (5, 7, 5)
    for line, want in zip(lines, expected):
        got = sum(syllables[w] for w in line.lower().split())
        assert got == want, f"expected {want} syllables, got {got}: {line!r}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()

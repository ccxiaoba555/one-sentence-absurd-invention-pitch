#!/usr/bin/env python3
"""One-sentence absurd invention pitch.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance to /output/entry.txt, as the make.fun
"One-Sentence Absurd Invention Pitch" bounty requires.
"""

import os

PITCH = (
    "A toothpaste tube that squeezes itself from the bottom, flattens "
    "itself as it empties and quietly judges anyone who still squeezes "
    "the middle, ending the bathroom's oldest war."
)


def main() -> None:
    text = PITCH.strip()
    if not 1 <= len(text) <= 220:
        raise SystemExit(f"pitch is {len(text)} characters, must be 1-220")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to /output/entry.txt")
    print(text)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line (at most 200 characters) about the
entrant's fridge to /output/entry.txt.
"""
import os

ROAST = (
    "My fridge hums all night like it's warming up for a concert, "
    "but the only thing it has ever kept fresh is the smell of "
    "last week's leftovers."
)


def main() -> None:
    line = ROAST.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(line)}")
    if "\n" in line:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()

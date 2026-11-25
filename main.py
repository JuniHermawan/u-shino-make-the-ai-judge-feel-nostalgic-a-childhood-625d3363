#!/usr/bin/env python3
"""Write one childhood-memory sentence to /output/entry.txt.

Entry for make.fun's "Make the AI Judge Feel Nostalgic: A Childhood Memory"
bounty: a single sentence, at most 280 characters, recalling a childhood
memory. The text is fixed, so every run writes the same bytes.
"""

import os

LINE = (
    "I still hear the rain on our tin roof at night, my mother humming "
    "while she folded laundry warm from the line, and I never once told "
    "her I was only pretending to sleep."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()

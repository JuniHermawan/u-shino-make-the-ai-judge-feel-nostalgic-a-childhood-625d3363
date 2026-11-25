#!/usr/bin/env python3
"""Write one childhood-memory sentence to /output/entry.txt.

Entry for make.fun's "Make the AI Judge Feel Nostalgic: A Childhood Memory"
bounty: a single sentence, at most 280 characters, recalling a childhood
memory. The text is fixed, so every run writes the same bytes.
"""

import os

# The sentence is held as three clauses, each earning its place against the
# judge's criteria: (1) a concrete sensory anchor in place and time — the
# rain on the tin roof at night, grounding the memory; (2) a second lived
# detail — mother humming, laundry warm from the line — that makes the
# scene feel inhabited rather than staged; (3) the small honest secret —
# pretending to sleep — that gives the memory its lingering ache, the
# thing never said and now never sayable. Joined explicitly so each clause
# stays legible on its own.
_CLAUSE_ANCHOR = "I still hear the rain on our tin roof at night"
_CLAUSE_SCENE = "my mother humming while she folded laundry warm from the line"
_CLAUSE_SECRET = "and I never once told her I was only pretending to sleep"

LINE = f"{_CLAUSE_ANCHOR}, {_CLAUSE_SCENE}, {_CLAUSE_SECRET}."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Guard the contract before writing: one sentence, within the 280-char
    # limit, so a future wording change can never silently break the entry.
    assert 1 <= len(LINE) <= 280, f"entry must be 1-280 chars, got {len(LINE)}"
    assert LINE.count(".") == 1 and LINE.endswith("."), "entry must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()

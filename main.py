#!/usr/bin/env python3
"""One Star, Five Stars for the Food — entry program.

Writes a single sentence (112 chars) to /output/entry.txt: an alien tourist's
one-star review of Earth that still compliments the food (martabak).

Methodology (see README.md for the full record): 30 candidates drafted from
the published judge brief, each scored 0-5 per judge criterion IN ORDER with
written notes (candidates.md), winner picked by criteria-ordered comparison,
then re-checked against all 50 live titles for byte-identical collision.
No live-judge A/B was run: the shared OpenRouter key is exhausted (HTTP 402)
and no free judge path exists, so scoring is manual and stated as such.
"""

ENTRY = (
    "One star: Earth has one moon that follows you home and no refund "
    "policy, but the martabak is worth the haunting."
)

# Import-time gate self-check: the entry must pass the competition gate
# (UTF-8 text, 1..200 chars, not only whitespace, exactly one sentence)
# before the program ever writes it, so a bad entry fails loudly here
# instead of silently shipping an invalid file.
assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1..200"
assert ENTRY.strip(), "entry is only whitespace"
assert sum(ENTRY.count(c) for c in ".!?") == 1, "entry must be one sentence"


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Write-back verification: read the file back and confirm it is
    # byte-identical to the entry, so a partial write is caught here.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "write-back mismatch: entry.txt != ENTRY"


if __name__ == "__main__":
    main()

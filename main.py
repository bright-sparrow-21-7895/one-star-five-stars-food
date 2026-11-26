"""One-star alien tourist review of Earth, with a food compliment.

An alien visitor rates the planet one star for its heavy gravity
and self-contradicting weather, then admits the noodles alone
are worth crash-landing for. Writes the single entry sentence
to /output/entry.txt for the make.fun bounty.
"""

import os

ENTRY = (
    "One star: your planet's gravity made my tentacles ache, "
    "your weather filed a complaint against itself, and yet your "
    "noodles were so good I would crash-land here again just for "
    "one more bowl."
)


def main() -> None:
    # Gate: the entry must be one sentence of 1-200 characters.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.count(".") == 1 and ENTRY.endswith(".")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

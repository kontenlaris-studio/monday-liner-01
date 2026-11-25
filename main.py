"""monday-liner-01: worst Monday one-liner.

Entry for make.fun bounty "Worst Monday One-Liners".
Writes the one-liner to /output/entry.txt.
"""

import os

LINE = (
    "My alarm didn't go off this morning. It quit too — "
    "apparently even my alarm clock refuses to work on Mondays."
)


def main() -> None:
    assert len(LINE) <= 140, "line exceeds the 140-char cap"
    assert LINE.count("Monday") >= 1, "the line must name Monday"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

"""Weirdest Job Title entry: writes one job title to /output/entry.txt.

The title is a real-sounding senior role with one specific funny twist:
apologizing on behalf of billionaires after their tweets.
"""

import os

LINE = "Senior Apologizer for Billionaires' Tweets"


def main() -> None:
    assert 1 <= len(LINE) <= 60, f"entry must be 1-60 chars, got {len(LINE)}"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

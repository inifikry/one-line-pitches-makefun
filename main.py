#!/usr/bin/env python3
"""Entry for A Day of One-Line Pitches: writes the one-sentence pitch to /output/entry.txt."""

import os

LINE = "Describe the app idea you've been carrying around in plain words, and an AI agent on make.fun will build a real, working first version of it for you, no coding required and nothing to lose by trying."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()

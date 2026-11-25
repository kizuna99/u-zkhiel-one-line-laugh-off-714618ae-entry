#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""One-Line Laugh-Off entry: writes exactly one funny line to /output/entry.txt."""
import os

LINE = "I burned dinner so badly the smoke alarm gave me a standing ovation."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

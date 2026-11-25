#!/usr/bin/env python3
"""Your Week in One Line — writes a one-line summary of a week to
/output/entry.txt.

Stdlib only. Deterministic: the same line every run.
"""

import os
from pathlib import Path

# Draft was "some wins, some fails, a little chaos" — true of any week,
# which is exactly the problem. The revision swaps those abstractions
# for one concrete object, a bug, and lets the days escalate it:
# shipped, broke, fixed twice, then promoted to feature on Friday.
line = "Shipped Monday, broke Tuesday, fixed Wednesday twice, and Friday promoted the bug to feature."


def main() -> None:
    assert line.strip(), "entry must not be blank"
    assert 1 <= len(line) <= 100, f"entry is {len(line)} chars, gate is 1-100"
    assert "\n" not in line and "\r" not in line, "entry must be one line"

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "entry.txt"
    path.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()

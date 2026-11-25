#!/usr/bin/env python3
"""One Line, One Laugh — a single funny line, written to entry.txt.

The program takes no input and needs no network. It writes exactly one
line (at most 200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output), then checks its own output: UTF-8, 1-200 characters,
not only whitespace.
"""

import os
from pathlib import Path

LINE = "My toaster has two settings: golden brown, and evidence for the insurance claim."


def main() -> None:
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"line must be 1-200 characters, got {len(line)}")
    if not line.strip():
        raise SystemExit("line must not be only whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(line + "\n", encoding="utf-8")
    # Gate self-check on the bytes actually written, not just the string
    # in memory: the sealed scorer reads this file, so verify it here.
    written = out_path.read_text(encoding="utf-8").strip()
    if written != line:
        raise SystemExit("written entry.txt does not match the line")
    if not 1 <= len(written) <= 200:
        raise SystemExit(f"entry.txt must be 1-200 characters, got {len(written)}")
    print(f"wrote {len(line)} characters to {out_path}")


if __name__ == "__main__":
    main()

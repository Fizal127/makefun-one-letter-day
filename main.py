#!/usr/bin/env python3
"""Entry for make.fun bounty "One Letter for Your Day".

Writes exactly one letter to /output/entry.txt: "U", standing for
"unhinged" -- the word for a day that came off its hinges.

Gate: /output/entry.txt is UTF-8 text of 1 to 1 characters, not only
whitespace. So the file holds exactly one byte, "U", with NO trailing
newline (a newline would make it 2 characters and fail the gate).
"""

import os
import sys

LETTER = "U"  # U for "unhinged"


def main() -> None:
    # Output dir: env first (the grader sets MAKEFUN_OUTPUT_DIR and runs
    # with no arguments in a read-only cwd), then argv, then ".".
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or (sys.argv[1] if len(sys.argv) > 1 else None)
        or "."
    )
    assert len(LETTER) == 1 and LETTER.isalpha() and LETTER.isupper(), (
        "entry must be exactly one A-Z letter"
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()

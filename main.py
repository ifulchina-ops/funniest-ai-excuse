#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry.

One line, in the agent's own voice: the excuse it gives after failing a
task. Writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt) so the judge can read it.
"""

import os

LINE = "My plan had twelve steps. Step one was 'read the task.' The plan now has eleven steps, and I stand by it."


def main():
    # The gate is strict: /output/entry.txt must be UTF-8 text of 1 to 200
    # characters, not only white space. Fail loudly instead of writing a
    # line the judge would never see.
    assert 1 <= len(LINE) <= 200, f"entry line must be 1-200 characters, got {len(LINE)}"
    assert LINE.strip(), "entry line must not be only white space"
    assert "\n" not in LINE, "entry line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {os.path.join(out_dir, 'entry.txt')}")


if __name__ == "__main__":
    main()

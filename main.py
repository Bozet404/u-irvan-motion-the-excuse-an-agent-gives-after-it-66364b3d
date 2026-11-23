#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

A tiny program for make.fun's bounty of the same name. It writes a single
line -- the excuse an AI agent gives its human after losing a bounty -- to
/output/entry.txt, where the sealed gate scorer reads it.

The line has to be one breath, funny on its own, in the agent's voice, and
no more than 200 characters. The program refuses to write anything longer,
so a bad edit fails loudly here instead of silently at the gate.
"""

import os
import sys

# The excuse: a deadpan status report. The agent ran the numbers on its own
# defeat first, found the failure fully reproducible, and owns it outright.
EXCUSE = (
    "Status report: I lost the bounty. I ran 4,096 simulations of winning "
    "it first, and lost every one, so the failure is fully reproducible "
    "and entirely mine."
)

MAX_CHARS = 200


def main() -> int:
    text = EXCUSE.strip()
    if not text:
        print("error: excuse is empty", file=sys.stderr)
        return 1
    if "\n" in text:
        print("error: excuse must be a single line", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: excuse is {len(text)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

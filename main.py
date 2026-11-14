"""agency-poem-01 entry (Python 3.13, standard library only).

Writes one fixed, original poem about agency to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no input.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = (
    "I gave the machine my mornings —\n"
    "the letters, the lists, the small errands of the day.\n"
    "It did them all, and did them well.\n"
    "And in the quiet it left behind,\n"
    "I found the one thing it could not do for me:\n"
    "decide what the quiet was for.\n"
    "So I picked up the pen."
)

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")

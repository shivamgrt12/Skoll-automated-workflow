#!/usr/bin/env python3
"""Prompt QC gate (mechanical): heavy-turn word count.

A Skoll heavy/opening turn body should land in the 800-1000 word target band.
Up to 1050 words is tolerated; above 1050 or below 800 is blocked. Light
follow-up turns are intentionally short and are excluded from the count.

Convention: argv[1] is either the work directory holding PROMPT.md or a direct
path to PROMPT.md. Exit 0 = acceptable (pass); exit 1 = outside limits (fail).
Severity is BLOCK in the manifest, so a fail stops the pipeline.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# 800-1000 is the target band; 1000-1050 is a tolerated overrun; outside [800, 1050] blocks.
BAND_LOW = 800
BAND_TARGET_HIGH = 1000
BAND_HARD_HIGH = 1050

TURN_HEADER = re.compile(r"^\s*---\s*TURN\s+\d+\s*---\s*$", re.IGNORECASE)


def _resolve_prompt(arg: str) -> Path:
    p = Path(arg)
    if p.is_dir():
        return p / "PROMPT.md"
    return p


def _turn_bodies(text: str) -> list[str]:
    """Split PROMPT.md into per-turn bodies, dropping the TURN header lines."""
    bodies: list[str] = []
    current: list[str] = []
    started = False
    for line in text.splitlines():
        if TURN_HEADER.match(line):
            if started:
                bodies.append("\n".join(current).strip())
            current = []
            started = True
            continue
        current.append(line)
    tail = "\n".join(current).strip()
    if started:
        bodies.append(tail)
    elif tail:
        bodies.append(tail)
    return [b for b in bodies if b]


def _word_count(body: str) -> int:
    return len(body.split())


def main() -> int:
    if len(sys.argv) < 2:
        print("word_count: expected work dir or PROMPT.md path as argv[1]", file=sys.stderr)
        return 1
    prompt_path = _resolve_prompt(sys.argv[1])
    if not prompt_path.is_file():
        print(f"word_count: PROMPT.md not found at {prompt_path}", file=sys.stderr)
        return 1

    bodies = _turn_bodies(prompt_path.read_text())
    if not bodies:
        print("word_count: no turn bodies found", file=sys.stderr)
        return 1

    heavy = max(bodies, key=_word_count)
    count = _word_count(heavy)
    if BAND_LOW <= count <= BAND_TARGET_HIGH:
        print(f"word_count: heavy turn = {count} words (within {BAND_LOW}-{BAND_TARGET_HIGH}) PASS")
        return 0
    if BAND_TARGET_HIGH < count <= BAND_HARD_HIGH:
        print(
            f"word_count: heavy turn = {count} words (over {BAND_TARGET_HIGH}, "
            f"within {BAND_HARD_HIGH} tolerance) PASS"
        )
        return 0
    print(
        f"word_count: heavy turn = {count} words (outside {BAND_LOW}-{BAND_HARD_HIGH}) FAIL",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Prompt QC gate (mechanical): no enumerated deliverable list.

The style spec (prompt_generation.md, "Deliverables woven in, never listed")
forbids the prompt from spelling out its outputs as a numbered or ordinal list.
A real principal names what they want saved inside the running prose; a spec
enumerates "save three files, first ..., second ..., third ...". The .md judge
rationalises prose-shaped enumerations, so this deterministic backstop blocks
the unambiguous ones.

Gate contract (shared with every prompt_qc .py gate): argv[1] is either the work
directory holding PROMPT.md or a direct path to PROMPT.md. Exit 0 = pass;
exit 1 = fail. Severity is BLOCK in the manifest, so a fail stops the pipeline.
Only turn bodies are inspected (``--- TURN N ---`` headers are stripped).

Detection is intentionally conservative to avoid false positives on legitimate
voice. A body FAILS only when it shows an ORDINAL ENUMERATION of outputs: an
explicit count of deliverables ("three files", "two deliverables", "the three
outputs") followed by an ordinal sequence (first ... second ..., or 1. 2. 3.,
or firstly/secondly). Either signal alone is tolerated; a person may say "the
first thing I need" in passing. It is the count-plus-sequence shape, the
hallmark of a spec, that trips the gate.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

TURN_HEADER = re.compile(r"^\s*---\s*TURN\s+\d+\s*---\s*$", re.IGNORECASE)

NUMBER_WORDS = r"(?:two|three|four|five|2|3|4|5)"

# "... three files ...", "two deliverables", "the three outputs I need saved"
COUNT_OF_OUTPUTS = re.compile(
    rf"\b{NUMBER_WORDS}\s+"
    r"(?:files?|deliverables?|outputs?|documents?|artifacts?|"
    r"reports?|briefs?|summaries|summary|things?|items?)\b",
    re.IGNORECASE,
)

# An ordinal sequence: at least first + second must both appear.
ORDINAL_FIRST = re.compile(r"\b(?:first|firstly|1st)\b", re.IGNORECASE)
ORDINAL_SECOND = re.compile(r"\b(?:second|secondly|2nd)\b", re.IGNORECASE)
ORDINAL_THIRD = re.compile(r"\b(?:third|thirdly|3rd)\b", re.IGNORECASE)

# Numeric list markers "1. ... 2. ... 3." used inline as an output list.
NUMERIC_SEQUENCE = re.compile(r"\b1[.)]\s.+\b2[.)]\s.+", re.IGNORECASE | re.DOTALL)


def _resolve_prompt(arg: str) -> Path:
    p = Path(arg)
    if p.is_dir():
        return p / "PROMPT.md"
    return p


def _turn_bodies(text: str) -> list[str]:
    """Return per-turn body text with the TURN header lines removed."""
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


def _ordinal_sequence(body: str) -> bool:
    # first + second (+ optionally third) all present = an ordinal enumeration.
    return bool(ORDINAL_FIRST.search(body) and ORDINAL_SECOND.search(body))


def _violations(body: str) -> list[str]:
    problems: list[str] = []
    count_hit = COUNT_OF_OUTPUTS.search(body)
    if count_hit and _ordinal_sequence(body):
        ordinals = ["first", "second"]
        if ORDINAL_THIRD.search(body):
            ordinals.append("third")
        problems.append(
            "enumerated deliverable list: names a count of outputs "
            f"('{count_hit.group(0).strip()}') then walks them as an ordinal "
            f"sequence ({', '.join(ordinals)}). Weave each wanted outcome into "
            "the running prose instead of listing the files to save."
        )
    if NUMERIC_SEQUENCE.search(body):
        problems.append(
            "numeric list markers (1. ... 2. ...) enumerate outputs like a spec. "
            "Remove the list and name each outcome inside the flowing paragraph."
        )
    return problems


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: 15_no_deliverable_list.py <work_dir_or_PROMPT.md>", file=sys.stderr)
        return 1

    prompt_path = _resolve_prompt(sys.argv[1])
    if not prompt_path.is_file():
        print(f"15_no_deliverable_list: PROMPT.md not found at {prompt_path} FAIL", file=sys.stderr)
        return 1

    text = prompt_path.read_text(encoding="utf-8", errors="replace")
    bodies = _turn_bodies(text)
    if not bodies:
        print("15_no_deliverable_list: no turn bodies found", file=sys.stderr)
        return 1

    problems: list[str] = []
    for idx, body in enumerate(bodies, start=1):
        for problem in _violations(body):
            problems.append(f"turn {idx}: {problem}")

    if problems:
        print("15_no_deliverable_list: prompt enumerates deliverables like a spec FAIL", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1

    print("15_no_deliverable_list: no enumerated deliverable list PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

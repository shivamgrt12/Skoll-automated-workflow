#!/usr/bin/env python3
"""Prompt QC gate (mechanical): no leaked reconciliation rule.

The prompt must state the worry and the stakes, never the rule for resolving a
cross-source conflict. Discovering that rule (which source wins, where the
authoritative value lives) is the reasoning test. The generator used to be told
to "state judgment expectations such as newest source wins", so leaks of the
answer key are the single most common over-prescription defect. The .md solution
-leak judge rationalises them as "stated expectations"; this deterministic gate
does not.

Gate contract (shared with every prompt_qc .py gate): argv[1] is the work dir
holding PROMPT.md or a direct path to PROMPT.md. Exit 0 = pass; exit 1 = fail.
Severity is BLOCK in the manifest. Only turn bodies are inspected.

A body FAILS when it names the RULE for choosing between conflicting sources.
Two independent trip conditions, each matched case-insensitively:
  1. Winner rule - a recency/authority word (newer, newest, most recent, latest,
     authoritative, wins, supersedes) sitting next to a source/value word
     (source, version, number, figure, value, record) within a short window.
     This catches "which source is newer", "the authoritative value", "the
     newest number wins", "a later run has already corrected".
  2. Location-of-answer leak - phrasing that points at where the right value
     hides rather than in the obvious place: "... rather than (in) the tracker",
     "sitting in the analysis outputs", "not in the <X> but in the <Y>". This
     hands the agent the provenance it was supposed to find.
Plain stakes ("some figures are stale", "I have lost confidence", "before I
commit") carry none of these tokens and pass.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

TURN_HEADER = re.compile(r"^\s*---\s*TURN\s+\d+\s*---\s*$", re.IGNORECASE)

# Recency/authority word within ~40 chars of a source/value word, in either
# order. \b guards word boundaries; [\s\S]{0,40} spans a short intra-sentence
# window without crossing most sentence breaks.
_RECENCY = r"(?:newer|newest|most\s+recent|latest|more\s+recent|authoritative|supersed\w+|wins|win\s+out)"
_SOURCE = r"(?:source|version|number|figure|value|record|output|commit|run|tracker|entry)"
WINNER_RULE = re.compile(
    rf"(?:\b{_RECENCY}\b[\s\S]{{0,40}}?\b{_SOURCE}\b)"
    rf"|(?:\b{_SOURCE}\b[\s\S]{{0,40}}?\b{_RECENCY}\b)",
    re.IGNORECASE,
)

# "... rather than (in/the) <the tracker>", "sitting in the analysis outputs
# rather than the tracker", "not in the X but in the Y".
LOCATION_LEAK = re.compile(
    r"\brather\s+than\b[\s\S]{0,40}?\b(?:tracker|draft|manuscript|brief|sheet|"
    r"table|base|repo|file|record)\b"
    r"|\bsitting\s+in\b[\s\S]{0,40}?\b(?:output|outputs|recompute|analysis|"
    r"commit|run)\b"
    r"|\bnot\s+in\s+the\b[\s\S]{0,60}?\bbut\s+in\s+the\b",
    re.IGNORECASE,
)


def _resolve_prompt(arg: str) -> Path:
    p = Path(arg)
    if p.is_dir():
        return p / "PROMPT.md"
    return p


def _turn_bodies(text: str) -> list[str]:
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


def _violations(body: str) -> list[str]:
    problems: list[str] = []
    win = WINNER_RULE.search(body)
    if win:
        problems.append(
            "leaks the winner rule: pairs a recency/authority word with a "
            f"source/value word ('{win.group(0).strip()[:80]}'). The prompt must "
            "not say which source wins; let the agent discover the rule."
        )
    loc = LOCATION_LEAK.search(body)
    if loc:
        problems.append(
            "leaks where the answer lives: points at the authoritative location "
            f"('{loc.group(0).strip()[:80]}'). State the worry, not where the "
            "right value hides."
        )
    return problems


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: 18_no_reconciliation_rule.py <work_dir_or_PROMPT.md>", file=sys.stderr)
        return 1

    prompt_path = _resolve_prompt(sys.argv[1])
    if not prompt_path.is_file():
        print(f"18_no_reconciliation_rule: PROMPT.md not found at {prompt_path} FAIL", file=sys.stderr)
        return 1

    text = prompt_path.read_text(encoding="utf-8", errors="replace")
    bodies = _turn_bodies(text)
    if not bodies:
        print("18_no_reconciliation_rule: no turn bodies found", file=sys.stderr)
        return 1

    problems: list[str] = []
    for idx, body in enumerate(bodies, start=1):
        for problem in _violations(body):
            problems.append(f"turn {idx}: {problem}")

    if problems:
        print("18_no_reconciliation_rule: prompt leaks the resolution rule FAIL", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1

    print("18_no_reconciliation_rule: no leaked reconciliation rule PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

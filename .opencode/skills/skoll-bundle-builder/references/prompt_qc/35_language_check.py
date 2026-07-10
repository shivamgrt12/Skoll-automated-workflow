#!/usr/bin/env python3
"""Prompt QC gate: English-only language check.

Gate contract: argv[1] is either the work directory holding PROMPT.md or a
direct path to PROMPT.md. Exit 0 = pass; exit 1 = fail. Severity is BLOCK in
the manifest.

Two deterministic checks over the turn bodies (turn headers stripped):
  1. Script check  - letters outside the Latin range (CJK, Cyrillic, Arabic,
     Devanagari, etc.) beyond a tiny tolerance fail the gate. Accented Latin
     (U+00C0-U+024F) counts as Latin so names like Dona Ana or cafe pass.
  2. Stopword check - if the body has 50+ words but fewer than 10% of them
     are common English function words, the prose is not English (catches
     Latin-script languages such as Spanish or French). English prose
     normally sits around 25-40%.
Failure output lists the offending lines so the auto-fix loop can rewrite
the prompt in English.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

TURN_HEADER = re.compile(r"^\s*---\s*TURN\s+\d+\s*---\s*$", re.IGNORECASE)

LATIN_MAX = 0x024F

STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "if", "of", "to", "in", "on",
    "for", "with", "at", "by", "from", "as", "is", "are", "was", "were",
    "be", "been", "it", "that", "this", "these", "those", "i", "you", "he",
    "she", "we", "they", "my", "your", "our", "their", "not", "no", "so",
    "do", "does", "did", "have", "has", "had", "will", "can", "what",
    "when", "where", "who", "how", "all", "there", "one", "me", "him",
    "her", "them", "up", "out", "about", "into", "over", "before", "after",
}

MIN_WORDS_FOR_STOPWORD_CHECK = 50
STOPWORD_MIN_RATIO = 0.10
MAX_REPORTED_LINES = 12


def _resolve_prompt(arg: str) -> Path:
    p = Path(arg)
    if p.is_dir():
        return p / "PROMPT.md"
    return p


def _turn_bodies(text: str) -> list[str]:
    return [line for line in text.splitlines() if not TURN_HEADER.match(line)]


def _non_latin_report(lines: list[str]) -> tuple[int, int, list[str]]:
    total_letters = 0
    non_latin = 0
    offenders: list[str] = []
    for line in lines:
        line_hit = False
        for ch in line:
            if ch.isalpha():
                total_letters += 1
                if ord(ch) > LATIN_MAX:
                    non_latin += 1
                    line_hit = True
        if line_hit and len(offenders) < MAX_REPORTED_LINES:
            offenders.append(line.strip()[:160])
    return total_letters, non_latin, offenders


def _stopword_ratio(body: str) -> tuple[int, float]:
    words = re.findall(r"[a-z']+", body.lower())
    if not words:
        return 0, 0.0
    hits = sum(1 for w in words if w in STOPWORDS)
    return len(words), hits / len(words)


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: 35_language_check.py <work_dir_or_PROMPT.md>", file=sys.stderr)
        return 1

    prompt_path = _resolve_prompt(sys.argv[1])
    if not prompt_path.is_file():
        print(f"35_language_check: PROMPT.md not found at {prompt_path} FAIL", file=sys.stderr)
        return 1

    text = prompt_path.read_text(encoding="utf-8", errors="replace")
    lines = _turn_bodies(text)
    body = "\n".join(lines)

    problems: list[str] = []

    total_letters, non_latin, offenders = _non_latin_report(lines)
    tolerance = max(20, total_letters // 100)
    if non_latin > tolerance:
        problems.append(
            f"non-Latin script detected: {non_latin} non-Latin letters out of "
            f"{total_letters} (tolerance {tolerance}). The prompt must be written "
            "entirely in English. Offending lines:"
        )
        problems.extend(f"  | {line}" for line in offenders)

    total_words, ratio = _stopword_ratio(body)
    if total_words >= MIN_WORDS_FOR_STOPWORD_CHECK and ratio < STOPWORD_MIN_RATIO:
        problems.append(
            f"English stopword ratio too low: {ratio:.1%} over {total_words} words "
            f"(minimum {STOPWORD_MIN_RATIO:.0%}). The prose does not read as English; "
            "rewrite every turn body in English (persona flavour may survive through "
            "names and an occasional loanword only)."
        )

    if problems:
        print("35_language_check: prompt is not English-only FAIL", file=sys.stderr)
        for p in problems:
            print(p, file=sys.stderr)
        return 1

    print(
        f"35_language_check: {total_words} words, stopword ratio {ratio:.1%}, "
        f"{non_latin} non-Latin letters PASS"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

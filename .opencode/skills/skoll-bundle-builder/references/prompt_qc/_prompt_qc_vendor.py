#!/usr/bin/env python3
"""
prompt_qc.py - Deterministic prompt QC gate.

Runs the machine-verifiable half of the 71-item PROMPT_QC_CHECKLIST against a
finished prompt artifact (``PROMPT.md`` / ``prompt.txt`` / ``prompts.txt``).
Every check in this file is a pure text fact provable by reading the artifact:
no judgment, no LLM, no cost.  The reading-comprehension half of the checklist
(framing, difficulty, voice, persona, AI-slop, client calibration, multi-agent
forcing) is NOT scriptable and lives in the companion ``PROMPT_QC.md`` rubric.

Checklist items covered here (section.letter + number from the master list):

  C. Forbidden content
    #11  restating context / do-it-yourself  MAJOR  (points agent at its own files)
    #12  service api-handle leak         FAIL   (only the -api/_api form, e.g.
         whatsapp-api; a service named naturally like WhatsApp/Slack is allowed)
    #15  dictated file names             FAIL   (*.pdf/*.csv/*.docx/... tokens)
    #15  explicit file paths             FAIL   (/Users/..., mock_data/..., a/b/c)
    #16  JSON / field-schema tokens      FAIL   ({...:...}, field lists, schemas)
    #18  em dashes                       FAIL   (U+2014, U+2013, "--" ascii pair)
    #19  semicolons in a turn body       FAIL
    #19b parentheses in a turn body      FAIL   (dictation uses no brackets)
    #20  colons in a turn body           FAIL   (allowed only in TURN header)
    #21  temporal lexicon                FAIL   (clock stamps, e.g. 9am/09:30;
         today/tomorrow/weekday names are NOT flagged)
    #21b explicit calendar year          FAIL   (four-digit 1900-2099, e.g. 2026,
         and written-out years like "twenty twenty-six" / "two thousand
         twenty-five"; the model must infer the year from its own context)
    #21c numeric calendar date           FAIL   (ISO 2026-03-14, slash/dot forms
         03/14/2026, 14.03.26)
    #21d month-name date                 FAIL   (a month next to a day or year,
         e.g. "March 14", "14 March", "Jan 2026"; a lone month with no number
         like "in March" is allowed)
  D. Required form
    #23  empty artifact / no turn body   FAIL   (a body-less prompt is invalid)
    #23  one unbroken paragraph per turn WARN   (no blank line inside a body)
    #24  heavy turn 800-1000 words       WARN   (word-band on the heaviest turn)
    #25  light turns 2-5 sentences       WARN   (short follow-up turns)
    #27  header is exactly '--- TURN N ---'  FAIL
  F. Deliverables woven in
    #31  no deliverables heading         FAIL
    #32  no numbered / bulleted output list  FAIL

Verdict policy (per client + manager decision):
  * Forbidden content (#12/#15/#16/#18/#19/#19b/#20/#21) and malformed
    headers (#27), an empty artifact (#23), and deliverable lists (#31/#32) are
    HARD FAIL -- must be fixed before bundle.
  * Form bands (#24/#25) and a blank line inside a body (#23) are WARN --
    flagged for review, non-blocking.

Standard library only, Python 3.7+.  Mirrors the Finding / severity /
compute_verdict / print_task_report shape of ``mock_data_qc.py`` so the two QC
tools read and report identically.
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List, Optional, Tuple


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SEVERITY_RANK = {"FAIL": 4, "MAJOR": 3, "MINOR": 2, "WARN": 1, "INFO": 1, "PASS": 0}

# Candidate artifact filenames, in preference order.
ARTIFACT_NAMES = ("PROMPT.md", "prompt.txt", "prompts.txt", "prompt.md")

# Heavy-turn word band (checklist #24).  A single heavy opening turn should sit
# in this band.  Below floor = probably too thin; above ceiling = narration bloat.
HEAVY_WORD_MIN = 800
HEAVY_WORD_MAX = 1000

# Light follow-up turns (checklist #25): a small clarification / intrusion.
LIGHT_SENTENCE_MIN = 2
LIGHT_SENTENCE_MAX = 5
# A turn under this word count is treated as a "light" follow-up for #25.
LIGHT_WORD_CEILING = 180

# The one and only legal turn header.  Checklist #27: exactly '--- TURN N ---'
# with a single ASCII space each side of TURN and the integer, nothing else.
TURN_HEADER_RE = re.compile(r"^--- TURN (\d+) ---$")
# Anything that looks like an attempt at a turn header (to catch malformed ones).
TURN_HEADER_LOOSE_RE = re.compile(r"^\s*-{2,}\s*turn\b.*$", re.IGNORECASE)

# --- C. Forbidden content patterns -----------------------------------------

# #18 em dash / en dash / ascii double-hyphen used as a dash.
EM_DASH_RE = re.compile(r"\u2014|\u2013")
# ascii "--" used as a dash inside prose (not the TURN header rule, which is
# handled by stripping headers before this check).
ASCII_DDASH_RE = re.compile(r"(?<!-)--(?!-)")

# #19 semicolon anywhere in a body.
SEMICOLON_RE = re.compile(r";")

# #19b parentheses anywhere in a body.  The broader Skoll prose rule treats a
# parenthetical aside as a hard AI-slop tell -- a busy person dictating does not
# open and close brackets.  Hard FAIL alongside the semicolon check.
PARENS_RE = re.compile(r"[()]")

# #20 colon anywhere in a body (headers are excluded before checking).  We allow
# the ``http://`` / ``https://`` colon only if a real URL somehow appears, but
# URLs are themselves a service/system smell, so we do NOT whitelist them here.
COLON_RE = re.compile(r":")

# #21 temporal lexicon: absolute clock stamps.  Relative words (today/tomorrow)
# and weekday names are NOT flagged -- a persona speaks in those naturally.  A
# hard clock stamp like "9am" or "09:30" is a machine-facing timestamp leak and
# fails.
CLOCK_TIME_RE = re.compile(
    r"\b\d{1,2}\s?(?:am|pm)\b|\b\d{1,2}:\d{2}\b",
    re.IGNORECASE,
)

# #21b explicit four-digit calendar year 1900-2099 as a standalone token. A hard
# year anchors the prompt to one point in time; the model must infer the current
# year from its own context, so any literal year is a FAIL.
YEAR_RE = re.compile(r"\b(?:19|20)\d{2}\b")

# #21c numeric calendar dates: ISO (2026-03-14) and slash/dot forms
# (03/14/2026, 14.03.26). Three digit groups separated by / . or - .
NUM_DATE_RE = re.compile(
    r"\b\d{4}-\d{1,2}-\d{1,2}\b"
    r"|\b\d{1,2}[/.]\d{1,2}[/.]\d{2,4}\b",
)

# #21d month-name dates: a month name sitting next to a day or year number
# ("March 14", "14 March", "Jan 2026", "Sept. 3"). A lone month with no adjacent
# number ("in March", "every March") is natural prose and is NOT flagged.
_MONTH_ALT = (
    r"jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|"
    r"jul(?:y)?|aug(?:ust)?|sep(?:t(?:ember)?)?|oct(?:ober)?|"
    r"nov(?:ember)?|dec(?:ember)?"
)
MONTH_DATE_RE = re.compile(
    r"\b(?:%s)\b\.?\s+\d{1,4}\b"
    r"|\b\d{1,2}(?:st|nd|rd|th)?\s+(?:%s)\b" % (_MONTH_ALT, _MONTH_ALT),
    re.IGNORECASE,
)

# #21b written-out years: "twenty twenty-six", "two thousand twenty-five". The
# trailing year word is required, so "two thousand dollars" or a bare "twenty"
# does not match. Note "twenty twenty" (the year 2020) also matches, which is
# the intended reading in a business-dictation prompt.
_YEAR_ONES = (
    r"one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
    r"thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen"
)
WRITTEN_YEAR_RE = re.compile(
    r"\btwenty[\s-]twenty(?:[\s-](?:%s))?\b"
    r"|\btwo\s+thousand\s+(?:and\s+)?(?:twenty[\s-]|thirty[\s-])?(?:%s)\b"
    % (_YEAR_ONES, _YEAR_ONES),
    re.IGNORECASE,
)


# #15 dictated file names: a token that ends in a real file extension.
FILENAME_RE = re.compile(
    r"\b[\w\-]+\.(?:pdf|csv|xlsx?|docx?|pptx?|txt|json|yaml|yml|md|"
    r"png|jpe?g|zip|tsv|html?)\b",
    re.IGNORECASE,
)

# #15/#66 explicit file PATHS: absolute posix (/Users/..., /home/...), the mock
# bundle dirs (mock_data/, persona/, data/, inject/), a path with two or more
# slash-separated segments, or a windows drive path.  A persona dictating a path
# is handing over HOW and leaking the storage layer.
FILEPATH_RE = re.compile(
    r"(?:(?<![\w.])/(?:Users|home|var|tmp|etc|opt|workspace)/[\w./\-]*[\w\-])"
    r"|(?:(?<![\w])(?:mock_data|persona|inject|data|environment|input|output)/"
    r"[\w./\-]*[\w\-])"
    r"|(?:[A-Za-z]:\\[\w\\.\-]*[\w\-])"
    r"|(?:(?<![\w:/])(?:\.{0,2}/)?[\w\-]+/[\w\-]+/[\w\-./]*[\w\-])",
)

# #11 restating context the agent already has, or telling the agent to do what
# it should work out on its own.  These are dictation SMELLS: phrases that point
# the agent at its own files/environment or narrate what it already knows.  This
# is a heuristic surface -- it FLAGS for review (MAJOR), the rubric judges intent.
REDUNDANT_CONTEXT_RE = re.compile(
    r"\byou (?:already )?have (?:access to|all|the)\b"
    r"|\bin your (?:files|inbox|calendar|records|system|environment|memory)\b"
    r"|\bas you (?:know|can see|already know)\b"
    r"|\byou can (?:see|read|find|access) (?:in|from|the)\b"
    r"|\bwhich you (?:have|can access|already have)\b"
    r"|\byour (?:files|environment|tools|system) (?:contain|have|hold)\b"
    r"|\bavailable to you (?:in|from|via)\b"
    r"|\bremember(?:,| that) you\b"
    r"|\byou'?ll (?:find|see) (?:it|them|these|those) in\b",
    re.IGNORECASE,
)

# #16 JSON / field-schema smells.
#   - a brace object with a colon inside: {"foo": ...} or {foo: ...}
#   - explicit schema vocabulary next to "field"/"column"/"key"
JSON_OBJ_RE = re.compile(r"\{[^{}]*:[^{}]*\}")
SCHEMA_WORD_RE = re.compile(
    r"\bjson\b"
    r"|\bschema\b"
    r"|\bfield\s+(?:name|list|schema)s?\b"
    r"|\b(?:name|list|set)\s+of\s+fields\b"
    r"|\bkey\s*[-/]\s*value\b"
    r"|\bpayload\s+shape\b"
    r"|\bcolumn\s+(?:name|header)s?\b",
    re.IGNORECASE,
)

# #12 service / system leak.  A persona may name a service NATURALLY in prose
# ("send it on WhatsApp", "put it in Slack") -- that is how a real person speaks
# and is allowed.  What leaks the system layer is the TECHNICAL handle form: a
# service token suffixed with -api or _api (whatsapp-api, slack_api, gmail-api).
# Only that API-handle form is a hard FAIL.
SERVICE_RE = re.compile(r"\b[\w-]+[-_]api\b", re.IGNORECASE)

# --- F. Deliverables listed (not woven) ------------------------------------

# #31 a deliverables / outputs / produce-this heading.
DELIVERABLE_HEADING_RE = re.compile(
    r"^\s*#*\s*(?:deliverables?|outputs?|produce(?:\s+the\s+following)?|"
    r"what\s+to\s+produce|required\s+outputs?|artifacts?\s+to\s+deliver)\s*:?\s*$",
    re.IGNORECASE,
)
# #32 a numbered or bulleted list line.
LIST_ITEM_RE = re.compile(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)\S")


# ---------------------------------------------------------------------------
# Finding + Verdict  (identical shape to mock_data_qc.py)
# ---------------------------------------------------------------------------

class Finding:
    __slots__ = ("severity", "check", "turn", "message")

    def __init__(
        self, severity: str, check: str, turn: str, message: str
    ) -> None:
        self.severity = severity
        self.check = check       # e.g. "C#18 em-dash"
        self.turn = turn         # e.g. "TURN 2" or "" (artifact-level)
        self.message = message

    def __str__(self) -> str:
        loc = self.check + (f" [{self.turn}]" if self.turn else "")
        return f"  [{self.severity}] {loc}: {self.message}"


def compute_verdict(findings: List[Finding]) -> str:
    sevs = {f.severity for f in findings}
    if "FAIL" in sevs:
        return "FAIL"
    if "MAJOR" in sevs:
        return "MAJOR_ISSUES"
    if "MINOR" in sevs:
        return "MINOR_ISSUES"
    return "PASS"


# ---------------------------------------------------------------------------
# Artifact parsing
# ---------------------------------------------------------------------------

class Turn:
    __slots__ = ("num", "header_line", "body", "start_line")

    def __init__(self, num: Optional[int], header_line: str,
                 body: str, start_line: int) -> None:
        self.num = num
        self.header_line = header_line
        self.body = body
        self.start_line = start_line


def find_artifact(task_dir: Path) -> Optional[Path]:
    """Return the prompt artifact inside a task dir, honouring name priority."""
    for name in ARTIFACT_NAMES:
        cand = task_dir / name
        if cand.exists():
            return cand
    # Fall back to a nested input/ layout (Harness bundles put PROMPT.md there).
    for name in ARTIFACT_NAMES:
        cand = task_dir / "input" / name
        if cand.exists():
            return cand
    return None


def read_text(path: Path) -> str:
    raw = path.read_bytes()
    return raw.decode("utf-8", errors="replace").replace("\r\n", "\n").replace(
        "\r", "\n"
    )


def split_turns(text: str, findings: List[Finding]) -> List[Turn]:
    """
    Split the artifact into turns on '--- TURN N ---' headers.

    Also validates the header form (#27): any line that looks like a turn header
    but does not match the exact canonical form raises a FAIL.
    """
    lines = text.split("\n")
    turns: List[Turn] = []
    cur_num: Optional[int] = None
    cur_header = ""
    cur_body_lines: List[str] = []
    cur_start = 0
    seen_any_header = False

    def flush() -> None:
        if seen_any_header:
            turns.append(Turn(
                cur_num, cur_header, "\n".join(cur_body_lines), cur_start
            ))

    for idx, line in enumerate(lines, start=1):
        m = TURN_HEADER_RE.match(line.strip())
        loose = TURN_HEADER_LOOSE_RE.match(line)
        if m:
            # Canonical header. But guard against trailing whitespace / exact form.
            if line != f"--- TURN {m.group(1)} ---":
                findings.append(Finding(
                    "FAIL", "D#27 turn-header",
                    f"TURN {m.group(1)}",
                    f"header line {idx} has stray whitespace or characters, "
                    f"must be exactly '--- TURN {m.group(1)} ---'",
                ))
            flush()
            cur_num = int(m.group(1))
            cur_header = line
            cur_body_lines = []
            cur_start = idx
            seen_any_header = True
        elif loose and not m:
            # Looks like a turn header but is malformed (day, time, label, comma,
            # parentheses, wrong dashes, lowercase, etc.).
            findings.append(Finding(
                "FAIL", "D#27 turn-header", "",
                f"line {idx} looks like a turn header but is not the exact form "
                f"'--- TURN N ---': {line.strip()!r}",
            ))
            flush()
            cur_num = None
            cur_header = line
            cur_body_lines = []
            cur_start = idx
            seen_any_header = True
        else:
            if seen_any_header:
                cur_body_lines.append(line)
    flush()

    if not seen_any_header:
        # No headers at all -> treat the whole artifact as a single turn body.
        turns.append(Turn(None, "", text, 1))
    return turns


def count_words(body: str) -> int:
    return len(re.findall(r"\b[\w']+\b", body))


def count_sentences(body: str) -> int:
    # Sentence-enders . ! ? followed by space/newline/end, collapsed.
    parts = re.split(r"[.!?]+(?:\s|$)", body.strip())
    return len([p for p in parts if p.strip()])


def strip_for_forbidden(body: str) -> str:
    """
    Remove content that is legitimately allowed to contain a colon/dash so the
    forbidden-content scan does not false-positive on it.  Currently a no-op for
    turn bodies (headers are already split out), kept as a seam for future
    persona-date allowances (#22).
    """
    return body


# ---------------------------------------------------------------------------
# Per-turn checks
# ---------------------------------------------------------------------------

def check_forbidden_content(turn: Turn, findings: List[Finding]) -> None:
    label = f"TURN {turn.num}" if turn.num is not None else "BODY"
    body = strip_for_forbidden(turn.body)

    # #18 em dash / en dash.
    if EM_DASH_RE.search(body):
        findings.append(Finding(
            "FAIL", "C#18 em-dash", label,
            "contains an em dash or en dash (U+2014 / U+2013); rewrite the clause",
        ))
    for m in ASCII_DDASH_RE.finditer(body):
        findings.append(Finding(
            "FAIL", "C#18 em-dash", label,
            f"contains an ascii '--' used as a dash near ...{_ctx(body, m.start())}...",
        ))

    # #19 semicolons.
    if SEMICOLON_RE.search(body):
        findings.append(Finding(
            "FAIL", "C#19 semicolon", label,
            "contains a semicolon; split into separate sentences",
        ))

    # #19b parentheses.
    for m in PARENS_RE.finditer(body):
        findings.append(Finding(
            "FAIL", "C#19 parens", label,
            f"contains a parenthesis near ...{_ctx(body, m.start())}...; "
            f"a dictated aside does not use brackets",
        ))

    # #20 colons (headers already excluded).
    for m in COLON_RE.finditer(body):
        findings.append(Finding(
            "FAIL", "C#20 colon", label,
            f"contains a colon near ...{_ctx(body, m.start())}...",
        ))

    # #21 temporal lexicon (clock stamps).
    for m in CLOCK_TIME_RE.finditer(body):
        findings.append(Finding(
            "FAIL", "C#21 temporal", label,
            f"clock time stamp {body[m.start():m.end()]!r} near "
            f"...{_ctx(body, m.start())}...",
        ))

    # #21b explicit calendar year (digit and written-out forms).
    for m in YEAR_RE.finditer(body):
        findings.append(Finding(
            "FAIL", "C#21b year", label,
            f"explicit year {body[m.start():m.end()]!r} near "
            f"...{_ctx(body, m.start())}...; let the model infer the year from "
            f"its own context",
        ))
    for m in WRITTEN_YEAR_RE.finditer(body):
        findings.append(Finding(
            "FAIL", "C#21b year", label,
            f"written-out year {body[m.start():m.end()]!r} near "
            f"...{_ctx(body, m.start())}...; let the model infer the year from "
            f"its own context",
        ))

    # #21c numeric calendar date.
    for m in NUM_DATE_RE.finditer(body):
        findings.append(Finding(
            "FAIL", "C#21c date", label,
            f"explicit date {body[m.start():m.end()]!r} near "
            f"...{_ctx(body, m.start())}...; name the timing in relative terms",
        ))

    # #21d month-name date.
    for m in MONTH_DATE_RE.finditer(body):
        findings.append(Finding(
            "FAIL", "C#21d date", label,
            f"explicit date {body[m.start():m.end()]!r} near "
            f"...{_ctx(body, m.start())}...; name the timing in relative terms",
        ))

    # #15 dictated file names.
    for m in FILENAME_RE.finditer(body):
        findings.append(Finding(
            "FAIL", "C#15 filename", label,
            f"dictated file name {body[m.start():m.end()]!r}; name the outcome, "
            f"not the file",
        ))

    # #15/#66 explicit file paths.
    for m in FILEPATH_RE.finditer(body):
        findings.append(Finding(
            "FAIL", "C#15 file-path", label,
            f"explicit file path {body[m.start():m.end()]!r}; the agent finds its "
            f"own files, never dictate a path",
        ))

    # #11 restating context / telling the agent what it should do on its own.
    for m in REDUNDANT_CONTEXT_RE.finditer(body):
        findings.append(Finding(
            "MAJOR", "C#11 redundant-context", label,
            f"points the agent at its own context near "
            f"...{_ctx(body, m.start())}...; the agent already has its files and "
            f"environment, state the intent not what it can read for itself",
        ))

    # #16 JSON / field-schema tokens.
    for m in JSON_OBJ_RE.finditer(body):
        findings.append(Finding(
            "FAIL", "C#16 json-schema", label,
            f"JSON-shaped object near ...{_ctx(body, m.start())}...",
        ))
    for m in SCHEMA_WORD_RE.finditer(body):
        findings.append(Finding(
            "FAIL", "C#16 json-schema", label,
            f"schema vocabulary {body[m.start():m.end()]!r}; do not dictate fields",
        ))

    # #12 service api-handle leak.
    for m in SERVICE_RE.finditer(body):
        findings.append(Finding(
            "FAIL", "C#12 service-name", label,
            f"names a service api handle {body[m.start():m.end()]!r}; a person "
            f"says the service naturally, not its api form",
        ))


def check_deliverable_form(turn: Turn, findings: List[Finding]) -> None:
    label = f"TURN {turn.num}" if turn.num is not None else "BODY"
    for i, line in enumerate(turn.body.split("\n"), start=1):
        if DELIVERABLE_HEADING_RE.match(line):
            findings.append(Finding(
                "FAIL", "F#31 deliverable-heading", label,
                f"deliverables/produce heading {line.strip()!r}; weave outputs "
                f"into prose",
            ))
        if LIST_ITEM_RE.match(line):
            findings.append(Finding(
                "FAIL", "F#32 output-list", label,
                f"numbered/bulleted list item {line.strip()[:48]!r}; deliverables "
                f"must be woven, not listed",
            ))


def check_form_bands(turns: List[Turn], findings: List[Finding]) -> None:
    """
    #23 one unbroken paragraph per turn body (no blank line inside a body).
    #24 heaviest turn sits in the 800-1000 word band.
    #25 light follow-up turns are 2-5 sentences.
    """
    real_turns = [t for t in turns if t.body.strip()]
    if not real_turns:
        findings.append(Finding(
            "FAIL", "D#23 form", "", "artifact has no turn body content"
        ))
        return

    # #23 blank line inside a body.
    for t in real_turns:
        label = f"TURN {t.num}" if t.num is not None else "BODY"
        stripped = t.body.strip("\n")
        if re.search(r"\n[ \t]*\n", stripped):
            findings.append(Finding(
                "WARN", "D#23 one-paragraph", label,
                "turn body is broken by a blank line; each body must be ONE "
                "unbroken paragraph",
            ))

    # Identify the heaviest turn -> that is the heavy opening turn for #24.
    heaviest = max(real_turns, key=lambda t: count_words(t.body))
    hw = count_words(heaviest.body)
    hlabel = f"TURN {heaviest.num}" if heaviest.num is not None else "BODY"
    if hw < HEAVY_WORD_MIN:
        findings.append(Finding(
            "WARN", "D#24 heavy-word-band", hlabel,
            f"heaviest turn is {hw} words, below the {HEAVY_WORD_MIN}-"
            f"{HEAVY_WORD_MAX} band; likely too thin to force multi-agent work",
        ))
    elif hw > HEAVY_WORD_MAX:
        findings.append(Finding(
            "WARN", "D#24 heavy-word-band", hlabel,
            f"heaviest turn is {hw} words, above the {HEAVY_WORD_MIN}-"
            f"{HEAVY_WORD_MAX} band; tighten per-clause language",
        ))

    # #25 light follow-up turns (everything that is not the heavy turn and is
    # short) should be 2-5 sentences.
    for t in real_turns:
        if t is heaviest:
            continue
        w = count_words(t.body)
        if w > LIGHT_WORD_CEILING:
            # Not a light follow-up; a second heavy turn is a client-style smell
            # but not deterministically wrong -> leave to the judgment rubric.
            continue
        s = count_sentences(t.body)
        label = f"TURN {t.num}" if t.num is not None else "BODY"
        if s < LIGHT_SENTENCE_MIN or s > LIGHT_SENTENCE_MAX:
            findings.append(Finding(
                "WARN", "D#25 light-turn", label,
                f"light follow-up has {s} sentence(s), expected "
                f"{LIGHT_SENTENCE_MIN}-{LIGHT_SENTENCE_MAX}",
            ))


def _ctx(body: str, pos: int, width: int = 24) -> str:
    lo = max(0, pos - width)
    hi = min(len(body), pos + width)
    snippet = body[lo:hi].replace("\n", " ")
    return snippet.strip()


# ---------------------------------------------------------------------------
# Task driver
# ---------------------------------------------------------------------------

def check_artifact(artifact: Path) -> Tuple[str, List[Finding], int]:
    findings: List[Finding] = []
    text = read_text(artifact)
    turns = split_turns(text, findings)

    for t in turns:
        check_forbidden_content(t, findings)
        check_deliverable_form(t, findings)

    check_form_bands(turns, findings)

    n_turns = len([t for t in turns if t.body.strip()])
    verdict = compute_verdict(findings)
    return verdict, findings, n_turns


def print_task_report(
    task_name: str,
    artifact_rel: str,
    verdict: str,
    findings: List[Finding],
    n_turns: int,
    verbose: bool,
    quiet: bool,
    missing: bool = False,
) -> None:
    if missing:
        if not quiet:
            print(f"\n{'='*62}")
            print(f"TASK: {task_name:<28}  SKIP (no prompt artifact found)")
            print(f"{'='*62}")
        return

    if quiet and verdict not in ("FAIL", "MAJOR_ISSUES"):
        return

    print(f"\n{'='*62}")
    print(f"TASK: {task_name:<28}  {verdict}")
    print(f"artifact: {artifact_rel}   turns: {n_turns}")
    print(f"{'='*62}")

    if verbose:
        show = {"FAIL", "MAJOR", "MINOR", "INFO"}
    elif quiet:
        show = {"FAIL", "MAJOR"}
    else:
        show = {"FAIL", "MAJOR", "MINOR"}

    visible = [f for f in findings if f.severity in show]
    # Stable, useful ordering: severity desc, then check id.
    visible.sort(key=lambda f: (-SEVERITY_RANK[f.severity], f.check, f.turn))
    for f in visible:
        print(str(f))

    warns = [f for f in findings if f.severity == "WARN"]
    if warns and not quiet:
        print(f"  ... plus {len(warns)} WARN (form band) -- non-blocking")

    if not visible and not warns and not quiet:
        print("  (clean -- no deterministic issues)")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Deterministic prompt QC gate: run the machine-verifiable half of "
            "the PROMPT_QC checklist against finished prompt artifacts."
        )
    )
    parser.add_argument(
        "--input-dir", "--tasks-dir", dest="tasks_dir", default=".",
        help="Directory containing task folders (default: current dir)",
    )
    parser.add_argument(
        "--task",
        help="Check only this single task folder name (default: all)",
    )
    parser.add_argument(
        "--file",
        help="Check ONE explicit artifact file path and exit (ignores --task)",
    )
    parser.add_argument(
        "--quiet", action="store_true",
        help="Only show FAIL/MAJOR findings and the summary table",
    )
    parser.add_argument(
        "--verbose", action="store_true",
        help="Show all findings including INFO",
    )
    args = parser.parse_args()

    # Single-file mode.
    if args.file:
        artifact = Path(args.file)
        if not artifact.exists():
            print(f"ERROR: --file does not exist: {artifact}", file=sys.stderr)
            return 2
        verdict, findings, n_turns = check_artifact(artifact)
        print_task_report(
            artifact.parent.name or artifact.name, str(artifact),
            verdict, findings, n_turns, args.verbose, args.quiet,
        )
        _print_summary([(artifact.name, verdict, findings, False)])
        return 1 if verdict == "FAIL" else 0

    tasks_dir = Path(args.tasks_dir)
    if not tasks_dir.exists():
        print(f"ERROR: --input-dir does not exist: {tasks_dir}", file=sys.stderr)
        return 2

    if args.task:
        task_dir = tasks_dir / args.task
        if not task_dir.exists():
            print(f"ERROR: task '{args.task}' not found in {tasks_dir}",
                  file=sys.stderr)
            return 2
        task_dirs = [task_dir]
    else:
        task_dirs = sorted(d for d in tasks_dir.iterdir() if d.is_dir())

    results: List[Tuple[str, str, List[Finding], bool]] = []
    any_fail = False

    for task_dir in task_dirs:
        task_name = task_dir.name
        artifact = find_artifact(task_dir)
        if artifact is None:
            print_task_report(
                task_name, "", "SKIP", [], 0,
                args.verbose, args.quiet, missing=True,
            )
            results.append((task_name, "SKIP (no artifact)", [], True))
            continue

        verdict, findings, n_turns = check_artifact(artifact)
        try:
            rel = str(artifact.relative_to(tasks_dir))
        except ValueError:
            rel = str(artifact)
        print_task_report(
            task_name, rel, verdict, findings, n_turns,
            args.verbose, args.quiet,
        )
        results.append((task_name, verdict, findings, False))
        if verdict == "FAIL":
            any_fail = True

    _print_summary(results)
    return 1 if any_fail else 0


def _print_summary(
    results: List[Tuple[str, str, List[Finding], bool]]
) -> None:
    print(f"\n{'='*62}")
    print("FINAL SUMMARY")
    print(f"{'='*62}")
    hdr = f"{'Task':<44} {'Verdict':<16} Findings"
    print(hdr)
    print("-" * len(hdr))
    for task_name, verdict, findings, skipped in results:
        if skipped:
            print(f"  {task_name:<44} {verdict:<16}")
        else:
            fc = sum(1 for f in findings if f.severity == "FAIL")
            wc = sum(1 for f in findings if f.severity == "WARN")
            mc = sum(1 for f in findings if f.severity == "MAJOR")
            detail = (
                f"FAIL={fc} MAJOR={mc} WARN={wc}" if findings else "clean"
            )
            print(f"  {task_name:<44} {verdict:<16} {detail}")
    print()


if __name__ == "__main__":
    sys.exit(main())

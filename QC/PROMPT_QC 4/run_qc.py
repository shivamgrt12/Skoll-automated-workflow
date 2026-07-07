#!/usr/bin/env python3
"""
run_qc.py -- one-command Prompt QC runner (no manual steps).

A reviewer runs THIS and nothing else. It does two things in one shot:

  1. Deterministic gate. Runs the machine-verifiable half of the checklist
     by reusing prompt_qc.py directly (imported, not duplicated). Prints the
     same report and returns the same FAIL/MAJOR/WARN findings.

  2. Judgment packet. Auto-assembles ONE self-contained file that inlines
     the judgment rubric, the reviewer instructions, the finished prompt
     artifact, and that persona's own files (USER/IDENTITY/TOOLS/MEMORY/
     HEARTBEAT). The reviewer's ONLY manual action is to paste that one file
     into their LLM. Nothing has to be gathered, opened, or copied by hand.

Why a packet instead of an API call: this stays dependency-free (stdlib
only, no API key, no network) while still covering all 71 checklist items.
The persona files are REQUIRED because Section H (persona alignment) cannot
be judged from the prompt text alone -- so the runner inlines them for you.

Design contract
---------------
  * stdlib only, Python 3.7+ (mirrors prompt_qc.py / mock_data_qc.py).
  * Reuses prompt_qc.py: find_artifact, read_text, check_artifact,
    print_task_report, compute_verdict, Finding. No logic is re-implemented.
  * Exit code: 1 if the deterministic gate FAILs (CI-friendly), else 0.
    The judgment pass is advisory here -- its verdict is produced by the
    reviewer's LLM/human from the emitted packet and combined per the table
    in PROMPT_QC.md.

CLI
---
  python3 run_qc.py --task <TASK_DIR>          # one bundle (typical)
  python3 run_qc.py --input-dir <DIR>          # every task folder under DIR
  python3 run_qc.py --task <DIR> --packet-dir <OUT>   # where packets go

Packets are written next to the runner in ./_qc_packets/ by default, one
per task, named <task>__QC_PACKET.md.
"""

import argparse
import sys
from pathlib import Path
from typing import List, Optional, Tuple

# Reuse the deterministic gate wholesale. run_qc.py lives beside prompt_qc.py.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import prompt_qc  # noqa: E402
from prompt_qc import (  # noqa: E402
    Finding,
    check_artifact,
    find_artifact,
    print_task_report,
    read_text,
)

# USER/IDENTITY/TOOLS are load-bearing for Section H. MEMORY/HEARTBEAT verify
# live-situation items 42 and 43. SOUL/AGENTS trail as extra voice context for
# the voice and AI-slop sections when present.
PERSONA_FILES = (
    "USER.md",
    "IDENTITY.md",
    "TOOLS.md",
    "MEMORY.md",
    "HEARTBEAT.md",
    "SOUL.md",
    "AGENTS.md",
)

RUBRIC_NAME = "PROMPT_QC.md"
DEFAULT_PACKET_DIR = "_qc_packets"


def _extract_reviewer_prompt(rubric_text: str) -> str:
    """
    Pull the block between the two '=== REVIEWER PROMPT ===' fences out of
    PROMPT_QC.md. That block is the actual instruction the LLM must follow;
    the surrounding markdown is human documentation we do not need to inline.

    Falls back to the whole rubric if the fences are ever renamed, so the
    packet is never silently empty.
    """
    fence = "=== REVIEWER PROMPT ==="
    end_fence = "=== END REVIEWER PROMPT ==="
    start = rubric_text.find(fence)
    if start == -1:
        return rubric_text.strip()
    start += len(fence)
    end = rubric_text.find(end_fence, start)
    if end == -1:
        return rubric_text[start:].strip()
    return rubric_text[start:end].strip()


def _find_persona_dir(task_dir: Path) -> Optional[Path]:
    """Locate the persona/ folder for a bundle, honouring the nested input/ layout."""
    for cand in (task_dir / "persona", task_dir / "input" / "persona"):
        if cand.is_dir():
            return cand
    return None


def _gather_persona(persona_dir: Optional[Path]) -> List[Tuple[str, str]]:
    """Return (filename, text) for each persona file that exists, in rubric order."""
    out: List[Tuple[str, str]] = []
    if persona_dir is None:
        return out
    for name in PERSONA_FILES:
        p = persona_dir / name
        if p.exists():
            out.append((name, read_text(p)))
    return out


def _gate_summary_line(verdict: str, findings: List[Finding]) -> str:
    fc = sum(1 for f in findings if f.severity == "FAIL")
    mc = sum(1 for f in findings if f.severity == "MAJOR")
    wc = sum(1 for f in findings if f.severity == "WARN")
    return f"deterministic gate: {verdict}  (FAIL={fc} MAJOR={mc} WARN={wc})"


def build_packet(
    task_name: str,
    artifact: Path,
    reviewer_prompt: str,
    persona: List[Tuple[str, str]],
    gate_verdict: str,
    gate_findings: List[Finding],
) -> str:
    """
    Assemble the single self-contained judgment packet.

    Everything the reviewer's LLM needs is inlined: the instruction, the
    prompt artifact, and the persona files. The reviewer pastes this whole
    file in one action, with no gathering or opening other files by hand.
    """
    art_text = read_text(artifact)
    parts: List[str] = []

    parts.append(f"# PROMPT QC JUDGMENT PACKET for {task_name}")
    parts.append("")
    parts.append(
        "PASTE THIS ENTIRE FILE into a fresh capable-model session. The model "
        "will score the judgment half of the checklist and print a verdict. "
        "You do not need to open or attach anything else -- the prompt "
        "artifact and the persona files are already inlined below."
    )
    parts.append("")
    parts.append("Context for the human reviewer (not part of the model input):")
    parts.append(f"- {_gate_summary_line(gate_verdict, gate_findings)}")
    if gate_verdict == "FAIL":
        parts.append(
            "- NOTE the deterministic gate already FAILED. Forbidden content "
            "must be fixed first. The judgment pass below still runs, but the "
            "combined verdict is FAIL until the gate is clean."
        )
    if not persona:
        parts.append(
            "- WARNING no persona files were found for this bundle. Section H "
            "cannot be judged. Supply persona/ or expect H to score N-A."
        )
    parts.append("")
    parts.append("---")
    parts.append("")

    parts.append("## 1. REVIEWER INSTRUCTION")
    parts.append("")
    parts.append(reviewer_prompt)
    parts.append("")
    parts.append("---")
    parts.append("")

    parts.append("## 2. FINISHED PROMPT ARTIFACT (the thing under test)")
    parts.append("")
    parts.append(f"Artifact path for your reference only: {artifact.name}")
    parts.append("")
    parts.append("<<<BEGIN PROMPT ARTIFACT>>>")
    parts.append(art_text.rstrip("\n"))
    parts.append("<<<END PROMPT ARTIFACT>>>")
    parts.append("")
    parts.append("---")
    parts.append("")

    parts.append("## 3. PERSONA FILES (for Section H persona alignment)")
    parts.append("")
    if persona:
        parts.append(
            "These describe who the persona actually is. Judge Section H by "
            "comparing the prompt above against these. In particular, use "
            "TOOLS.md to verify item H2 (no work on a service the persona does "
            "not have), IDENTITY.md for level match, and MEMORY/HEARTBEAT for "
            "live-situation fit."
        )
        parts.append("")
        for name, text in persona:
            parts.append(f"### persona/{name}")
            parts.append("")
            parts.append(f"<<<BEGIN {name}>>>")
            parts.append(text.rstrip("\n"))
            parts.append(f"<<<END {name}>>>")
            parts.append("")
    else:
        parts.append(
            "(No persona files found. Score Section H as N-A and say the "
            "persona files were not supplied.)"
        )
        parts.append("")

    parts.append("---")
    parts.append("")
    parts.append(
        "Now produce the report in the exact output format specified in the "
        "reviewer instruction above, then stop."
    )
    parts.append("")

    return "\n".join(parts)


def run_task(
    task_dir: Path,
    reviewer_prompt: str,
    packet_dir: Path,
    verbose: bool,
    quiet: bool,
) -> Tuple[str, List[Finding], Optional[Path]]:
    """
    Run the gate and emit the packet for one task. Returns
    (gate_verdict, gate_findings, packet_path or None if no artifact).
    """
    task_name = task_dir.name
    artifact = find_artifact(task_dir)
    if artifact is None:
        print_task_report(
            task_name, "", "SKIP", [], 0, verbose, quiet, missing=True
        )
        return "SKIP (no artifact)", [], None

    verdict, findings, n_turns = check_artifact(artifact)
    print_task_report(
        task_name, artifact.name, verdict, findings, n_turns, verbose, quiet
    )

    persona_dir = _find_persona_dir(task_dir)
    persona = _gather_persona(persona_dir)
    packet = build_packet(
        task_name, artifact, reviewer_prompt, persona, verdict, findings
    )
    packet_dir.mkdir(parents=True, exist_ok=True)
    packet_path = packet_dir / f"{task_name}__QC_PACKET.md"
    packet_path.write_text(packet, encoding="utf-8")

    npersona = len(persona)
    print(f"  judgment packet -> {packet_path}  ({npersona} persona files inlined)")
    if npersona == 0:
        print("  WARNING no persona files inlined -- Section H will be N-A")

    return verdict, findings, packet_path


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "One-command Prompt QC: runs the deterministic gate AND emits a "
            "self-contained judgment packet (rubric + prompt + persona files) "
            "per task. Reviewer's only manual step is pasting the packet into "
            "an LLM."
        )
    )
    parser.add_argument(
        "--input-dir", "--tasks-dir", dest="tasks_dir", default=".",
        help="Directory containing task folders (default: current dir)",
    )
    parser.add_argument(
        "--task",
        help="Run only this single task folder name (default: all under --input-dir)",
    )
    parser.add_argument(
        "--packet-dir", default=DEFAULT_PACKET_DIR,
        help=f"Where to write judgment packets (default: ./{DEFAULT_PACKET_DIR})",
    )
    parser.add_argument(
        "--quiet", action="store_true",
        help="Only show FAIL/MAJOR gate findings and the summary",
    )
    parser.add_argument(
        "--verbose", action="store_true",
        help="Show all gate findings including INFO",
    )
    args = parser.parse_args()

    here = Path(__file__).resolve().parent
    rubric_path = here / RUBRIC_NAME
    if not rubric_path.exists():
        print(f"ERROR: {RUBRIC_NAME} not found beside run_qc.py at {rubric_path}",
              file=sys.stderr)
        return 2
    reviewer_prompt = _extract_reviewer_prompt(read_text(rubric_path))

    packet_dir = Path(args.packet_dir)

    tasks_dir = Path(args.tasks_dir)
    if not tasks_dir.exists():
        print(f"ERROR: --input-dir does not exist: {tasks_dir}", file=sys.stderr)
        return 2

    if args.task:
        task_dir = tasks_dir / args.task
        if not task_dir.exists():
            # Allow --task to be a direct path too.
            task_dir = Path(args.task)
        if not task_dir.exists():
            print(f"ERROR: task '{args.task}' not found", file=sys.stderr)
            return 2
        task_dirs = [task_dir]
    else:
        task_dirs = sorted(d for d in tasks_dir.iterdir() if d.is_dir())

    results: List[Tuple[str, str, List[Finding]]] = []
    any_gate_fail = False

    for task_dir in task_dirs:
        verdict, findings, _ = run_task(
            task_dir, reviewer_prompt, packet_dir, args.verbose, args.quiet
        )
        results.append((task_dir.name, verdict, findings))
        if verdict == "FAIL":
            any_gate_fail = True

    _print_summary(results, packet_dir)
    return 1 if any_gate_fail else 0


def _print_summary(
    results: List[Tuple[str, str, List[Finding]]],
    packet_dir: Path,
) -> None:
    print(f"\n{'='*66}")
    print("RUN QC -- FINAL SUMMARY")
    print(f"{'='*66}")
    hdr = f"{'Task':<40} {'Gate':<16} Gate findings"
    print(hdr)
    print("-" * len(hdr))
    for task_name, verdict, findings in results:
        if verdict.startswith("SKIP"):
            print(f"  {task_name:<40} {verdict:<16}")
            continue
        fc = sum(1 for f in findings if f.severity == "FAIL")
        mc = sum(1 for f in findings if f.severity == "MAJOR")
        wc = sum(1 for f in findings if f.severity == "WARN")
        detail = f"FAIL={fc} MAJOR={mc} WARN={wc}" if findings else "clean"
        print(f"  {task_name:<40} {verdict:<16} {detail}")
    print()
    print(f"Judgment packets written to: {packet_dir}")
    print(
        "Next step: paste each *__QC_PACKET.md into your LLM to run the "
        "judgment pass, then combine per the table in PROMPT_QC.md."
    )
    print()


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""skoll-bundle: one command to build a harness-ready Skoll input bundle.

Pipeline (per persona):
  0 validate   deterministic  scripts/validate_input.py
  1 prompt     model          references/prompt_generation.md    -> PROMPT.md
  2 rubric     model          references/rubric_pytest_combined.md -> rubric.json + test_outputs.py + test_weights.json
  3 truth      model          references/truth_guide.md          -> TRUTH.md
  4 assemble   deterministic  scripts/assemble.py                -> task.yaml + README.md + copied trees
  5 qc         model+script   references/qc/NN_*                  -> pass/fail gates

Every stage records a checkpoint in <work>/bundle-manifest.json so a run can be
resumed (--resume) or a single stage re-run (--regenerate --stage N). Default is
interactive: the run pauses after each stage for review. --auto runs unattended.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = SKILL_ROOT / "scripts"
REFERENCES = SKILL_ROOT / "references"
TEMPLATES = SKILL_ROOT / "templates"
QC_DIR = REFERENCES / "qc"
PROMPT_QC_DIR = REFERENCES / "prompt_qc"
RUBRIC_QC_DIR = REFERENCES / "rubric_qc"
PYTEST_QC_DIR = REFERENCES / "pytest_qc"
TRUTH_QC_DIR = REFERENCES / "truth_qc"
MOCK_DATA_QC_DIR = REFERENCES / "mock_data_qc"

STAGES = ["validate", "prompt", "rubric", "truth", "assemble", "qc"]

BANNED_SERVICES = frozenset(
    {"google-drive-api", "google-contacts-api", "box-api", "dropbox-api"}
)

QC_MD_MAX_ATTEMPTS = 3

# Under the work dir so reports survive a mid-pipeline halt (out_dir may not exist yet).
QC_REPORTS_DIRNAME = "QC_reports"


def _qc_reports_dir(work: Path) -> Path:
    d = work / QC_REPORTS_DIRNAME
    d.mkdir(parents=True, exist_ok=True)
    return d


def _write_qc_report(
    work: Path,
    stage_name: str,
    gate_dir_name: str,
    entries: list[tuple[str, str, str]],
    halted: bool = False,
) -> None:
    """entries: (gate_name, verdict, detail_text) per gate, in run order."""
    order = {name: i for i, name in enumerate(STAGES + ["mock_data", "pytest"])}
    idx = order.get(stage_name, 99)
    reports = _qc_reports_dir(work)
    path = reports / f"{idx:02d}_{stage_name}.md"
    lines = [
        f"# QC report: {stage_name}",
        "",
        f"- Gate directory: `references/{gate_dir_name}/`",
        f"- Generated: {_now()}",
        f"- Outcome: {'HALTED (blocking failure)' if halted else 'completed'}",
        "",
        "## Per-gate results",
        "",
    ]
    for gate_name, verdict, detail in entries:
        lines.append(f"### {gate_name} — {verdict.upper()}")
        lines.append("")
        if detail.strip():
            lines.append(detail.strip())
        else:
            lines.append("_(mechanical gate; no model findings)_")
        lines.append("")
    path.write_text("\n".join(lines))
    print(f"[QC report] wrote {path}")

MANIFEST_NAME = "bundle-manifest.json"
MANIFEST_VERSION = "1.0"

# Passed as --model to override any retired model id pinned by the installed
# agent config (a stale pin makes the provider reject the call). Env-overridable.
STAGE_MODEL = os.environ.get("SKOLL_BUNDLE_MODEL", "anthropic/claude-opus-4-5")


class StageError(Exception):
    pass


def _now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S")


def _hash_dir(path: Path) -> str:
    h = hashlib.sha256()
    for f in sorted(path.rglob("*")):
        if f.is_file():
            h.update(f.relative_to(path).as_posix().encode())
            h.update(f.read_bytes())
    return h.hexdigest()[:16]


PERSONA_FILES = (
    "AGENTS.md",
    "SOUL.md",
    "IDENTITY.md",
    "USER.md",
    "TOOLS.md",
    "MEMORY.md",
    "HEARTBEAT.md",
)

SELECTION_KEYS = ("required_apis", "distractor_apis", "deliverables")


def _hash_persona(input_dir: Path) -> str:
    h = hashlib.sha256()
    for name in PERSONA_FILES:
        f = input_dir / name
        if f.is_file():
            h.update(name.encode())
            h.update(f.read_bytes())
    return h.hexdigest()[:16]


def _merge_selection(meta: dict, selection: dict) -> dict:
    merged = dict(meta)
    for key in SELECTION_KEYS:
        if selection.get(key):
            merged[key] = selection[key]
    return merged


def _persist_meta(work: Path, meta: dict) -> Path:
    path = work / "meta.resolved.json"
    path.write_text(json.dumps(meta, indent=2) + "\n")
    return path


def _load_manifest(work: Path) -> dict:
    mpath = work / MANIFEST_NAME
    if mpath.is_file():
        return json.loads(mpath.read_text())
    return {"version": MANIFEST_VERSION, "stages": {}}


def _save_manifest(work: Path, manifest: dict) -> None:
    (work / MANIFEST_NAME).write_text(json.dumps(manifest, indent=2) + "\n")


def _record(manifest: dict, stage: str, status: str, **extra) -> None:
    entry = {"status": status, "timestamp": _now()}
    entry.update(extra)
    manifest["stages"][stage] = entry


def _run(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=str(cwd) if cwd else None, text=True)


def _common_root(paths: list[Path]) -> Path:
    import os

    resolved = [str(p.resolve()) for p in paths]
    return Path(os.path.commonpath(resolved))


def _opencode_stage(system_prompt: Path, context_dirs: list[Path], prompt: str) -> str:
    run_dir = _common_root([system_prompt] + context_dirs)
    context_lines = "\n".join(f"- {d.resolve()}" for d in context_dirs)
    message = (
        f"{system_prompt.read_text()}\n\n"
        "----- OPERATOR INSTRUCTION -----\n"
        f"{prompt}\n\n"
        "Context directories you may read from (absolute paths):\n"
        f"{context_lines}\n"
    )
    cmd = [
        "opencode",
        "run",
        "--dir",
        str(run_dir),
        "--model",
        STAGE_MODEL,
        "--format",
        "json",
        "--dangerously-skip-permissions",
        message,
    ]
    result = subprocess.run(cmd, text=True, capture_output=True)
    if result.returncode != 0:
        raise StageError(f"opencode failed ({result.returncode}): {result.stderr[:500]}")
    return _extract_assistant_text(result.stdout)


def _extract_assistant_text(stdout: str) -> str:
    """Reassemble the assistant's text from opencode's `--format json` event stream.

    In non-interactive mode this opencode build emits the formatted answer to the
    TTY/stderr layer and nothing to stdout under `--format default`. With
    `--format json`, stdout is newline-delimited JSON events; the model's answer is
    the concatenation of every `{"type":"text", ...}` part in order. If the output
    is not JSON events (older/other builds), fall back to the raw stdout so behavior
    is never worse than before.
    """
    chunks: list[str] = []
    saw_event = False
    for line in stdout.splitlines():
        line = line.strip()
        if not line or not line.startswith("{"):
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        saw_event = True
        if event.get("type") == "text":
            part = event.get("part") or {}
            text = part.get("text")
            if isinstance(text, str):
                chunks.append(text)
    if not saw_event:
        return stdout
    return "".join(chunks)


def stage_validate(input_dir: Path, harness_dir: Path) -> None:
    contract = TEMPLATES / "input-contract.yaml"
    result = _run(
        [
            sys.executable,
            str(SCRIPTS / "validate_input.py"),
            str(input_dir),
            str(contract),
            str(harness_dir),
        ]
    )
    if result.returncode != 0:
        raise StageError("input validation failed (see checklist above)")


PROMPT_ARTIFACTS = ("PROMPT.md", "prompt_design_notes.md", "README.md", "api_selection.json")
PROMPT_PIN_ARTIFACTS = ("PROMPT.md", "prompt_design_notes.md", "README.md", "api_selection.json")

ARTIFACT_MARKER_INSTRUCTION = (
    "Wrap every artifact between an opening line '===FILE: <name>===' and a "
    "closing line '===END==='."
)


def _ask_operator_design(input_dir: Path) -> dict:
    print(
        "\n--- prompt design questions (persona: "
        f"{input_dir.name}) ---\n"
        "These three answers steer the prompt. Press Enter to let the model "
        "infer a field."
    )
    shape = input("1) Turn shape [single / multi]: ").strip().lower()
    domain = input("2) Domain [enterprise / personal / professional]: ").strip().lower()
    anchor = input("3) Fixed anchor event or deadline (blank if none): ").strip()
    return {"turn_shape": shape, "domain": domain, "anchor": anchor}


def _design_from_args(args: argparse.Namespace) -> dict:
    # Missing flags must stay empty (unfixed) so the model infers them; do not add defaults.
    return {
        "turn_shape": (args.turn_shape or "").strip().lower(),
        "domain": (args.domain or "").strip().lower(),
        "anchor": (args.anchor or "").strip(),
    }


def _has_design_flags(args: argparse.Namespace) -> bool:
    return any(
        getattr(args, name) not in (None, "")
        for name in ("turn_shape", "domain", "anchor")
    )


def _design_directives(design: dict | None) -> str:
    # The meta-prompt's Phase 1 tells the model to STOP and ask the operator three
    # design questions (turn shape, domain, anchor). In this headless pipeline no human
    # is on the other end of that call, so the model must never pause for them: the
    # operator answers (if any) are supplied here, and any unanswered field is delegated
    # back to the model's own judgment. This directive overrides the "ask first" step.
    design = design or {}
    fixed = []
    if design.get("turn_shape"):
        fixed.append(f"- Turn shape: {design['turn_shape']}.")
    if design.get("domain"):
        fixed.append(f"- Domain: {design['domain']}.")
    if design.get("anchor"):
        fixed.append(f"- Fixed anchor event or deadline: {design['anchor']}.")
    directive = (
        "\n\nThe three Phase 1 design questions have already been settled, so do "
        "NOT pause to ask them and do NOT emit any questions. Author the artifacts "
        "directly in this single response."
    )
    if fixed:
        directive += (
            "\nThe operator has fixed these decisions; honor them exactly:\n"
            + "\n".join(fixed)
        )
    unfixed = [
        label
        for key, label in (
            ("turn_shape", "turn shape"),
            ("domain", "domain"),
            ("anchor", "fixed anchor event"),
        )
        if not design.get(key)
    ]
    if unfixed:
        directive += (
            "\nFor the remaining undecided field(s) ("
            + ", ".join(unfixed)
            + "), choose the option best supported by the persona and design brief "
            "and proceed without asking."
        )
    return directive


def stage_prompt(input_dir: Path, work: Path, auto: bool, design: dict | None) -> dict:
    out = _opencode_stage(
        REFERENCES / "prompt_generation.md",
        [input_dir, input_dir / "home", input_dir / "task", input_dir / "mock_data"],
        f"The persona's seven MD files live at {input_dir}. Available workspace "
        f"artifacts are under {input_dir / 'home'} (use some as inputs, leave the rest "
        f"as noise). The persona team's design brief is {input_dir / 'task' / 'README.md'} "
        f"and {input_dir / 'task' / 'QC_REPORT.md'} (read both to choose traps and "
        f"red lines). The full mock-data API catalog is under {input_dir / 'mock_data'}; "
        "select only the persona-relevant services and split them into required and "
        "distractor APIs at a required:distractor ratio between 1:1 and 2:1. "
        "Every task must declare at least 12 required APIs, so select enough "
        "persona-relevant services to meet that floor. Never select dropbox-api, "
        "google-drive-api, or google-contacts-api for either list. "
        "You may enrich the mock data under Phase 3b's rules (values-only, "
        "persona-aligned, only to raise complexity or fix misalignment, never a "
        "schema change, never a banned service, preserving valid placeholders). To "
        "persist an edited mock-data file, emit it as a marked file whose name is its "
        "path relative to the persona folder, for example "
        f"'{input_dir.name}/mock_data/<svc>-api/<file>.json' style but written as "
        "'mock_data/<svc>-api/<file>.json'. Only files that already exist may be "
        "rewritten. "
        + ARTIFACT_MARKER_INSTRUCTION
        + " Emit PROMPT.md, prompt_design_notes.md, README.md, "
        "api_selection.json (an object with keys required_apis, distractor_apis, "
        "input_artifacts, and deliverables), any enriched mock_data/<svc>-api/<file> "
        "files, and finally mock_data_changes.json (a JSON array logging every "
        "mock-data edit, or [] if none). Emit the four fixed artifacts first, in that "
        "order."
        + _design_directives(design),
    )
    files = _split_artifacts(out)
    for name in PROMPT_ARTIFACTS:
        if name not in files:
            raise StageError(f"prompt stage did not emit {name}")
    _apply_mock_data_enrichment(input_dir, work, files)
    _write_prompt_artifacts(work, files)

    _prompt_self_repair_sweep(input_dir, work)

    _stage_qc_sweep(
        "mock_data",
        MOCK_DATA_QC_DIR,
        work,
        [input_dir, input_dir / "home", input_dir / "mock_data", work],
        ("api_selection.json",),
        enrich_input_dir=input_dir,
    )

    return _read_api_selection(work)


def _apply_mock_data_enrichment(
    input_dir: Path, work: Path, files: dict[str, str]
) -> None:
    applied = _guarded_mock_writeback(input_dir, files)
    changes = files.pop("mock_data_changes.json", "[]")
    _read_mock_data_changes(changes, name="mock_data_changes.json")
    (work / "mock_data_changes.json").write_text(changes)
    (work / "mock_data_applied.json").write_text(
        json.dumps(applied, indent=2) + "\n"
    )


def _guarded_mock_writeback(input_dir: Path, files: dict[str, str]) -> list[dict]:
    # Guardrails run here (not only in the meta-prompt) so a disobedient model still cannot
    # write outside mock_data, touch a banned service, or drift the harness schema.
    mock_root = (input_dir / "mock_data").resolve()
    applied: list[dict] = []
    for name, body in list(files.items()):
        if not name.startswith("mock_data/"):
            continue
        del files[name]
        target = (input_dir / name).resolve()
        if mock_root not in target.parents:
            raise StageError(f"enrichment path escapes mock_data: {name}")
        if not target.is_file():
            raise StageError(f"enrichment target is not an existing file: {name}")
        service = target.relative_to(mock_root).parts[0]
        if service in BANNED_SERVICES:
            raise StageError(f"enrichment targets banned service: {service}")
        _guard_values_only(target, body, name)
        target.write_text(body)
        applied.append({"file": name, "service": service})
    return applied


def _guard_values_only(target: Path, new_body: str, name: str) -> None:
    # Reject schema drift: JSON files must keep their container shape and per-record field
    # set. Non-JSON files are left to the model but must remain the same file kind.
    if target.suffix != ".json":
        return
    try:
        old = json.loads(target.read_text())
        new = json.loads(new_body)
    except json.JSONDecodeError as exc:
        raise StageError(f"enrichment is not valid JSON: {name}: {exc}") from exc
    old_rows, old_wrap = _mock_records(old)
    new_rows, new_wrap = _mock_records(new)
    if old_wrap != new_wrap:
        raise StageError(f"enrichment changed container shape: {name}")
    old_keys = _record_key_union(old_rows)
    new_keys = _record_key_union(new_rows)
    if new_keys - old_keys:
        added = ", ".join(sorted(new_keys - old_keys))
        raise StageError(f"enrichment added fields to {name}: {added}")


def _mock_records(data: object) -> tuple[list, tuple]:
    if isinstance(data, list):
        return data, ("list",)
    if isinstance(data, dict):
        for outer, inner in data.items():
            if isinstance(inner, dict):
                for key, rows in inner.items():
                    if isinstance(rows, list):
                        return rows, ("dict", outer, key)
        return [], ("dict",)
    return [], ("scalar",)


def _record_key_union(rows: list) -> set:
    keys: set = set()
    for row in rows:
        if isinstance(row, dict):
            keys |= set(row.keys())
    return keys


def _read_mock_data_changes(raw: str, name: str) -> list:
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise StageError(f"{name} is not valid JSON: {exc}") from exc
    if not isinstance(data, list):
        raise StageError(f"{name} must be a JSON array")
    return data


def _write_prompt_artifacts(work: Path, files: dict[str, str]) -> dict:
    for name in PROMPT_PIN_ARTIFACTS:
        if name in files:
            (work / name).write_text(files[name])
    (work / "prompt.txt").write_text((work / "PROMPT.md").read_text())
    if "api_selection.json" in files:
        _canonicalize_api_selection(work)
    return _read_api_selection(work)


def _canonicalize_api_selection(work: Path) -> None:
    # The model sometimes emits service names bare ("gmail") and sometimes suffixed
    # ("gmail-api"). Every downstream consumer (mock_data/<svc>-api dirs, the service
    # registry, task.yaml) keys on the "-api" form, so pin the on-disk selection to that
    # canonical form here rather than defending against both spellings in each consumer.
    path = work / "api_selection.json"
    sel = _extract_json(path.read_text())
    for key in ("required_apis", "distractor_apis"):
        if isinstance(sel.get(key), list):
            sel[key] = [_api_name(v) for v in sel[key]]
    path.write_text(json.dumps(sel, indent=2))


def _api_name(value: str) -> str:
    value = str(value).strip()
    return value if value.endswith("-api") else f"{value}-api"


def _read_api_selection(work: Path) -> dict:
    return _extract_json((work / "api_selection.json").read_text())


def _split_artifacts(raw: str) -> dict[str, str]:
    files: dict[str, str] = {}
    current: str | None = None
    buf: list[str] = []
    for line in raw.splitlines():
        stripped = line.strip()
        if stripped.startswith("===FILE:") and stripped.endswith("==="):
            current = stripped[len("===FILE:") : -3].strip()
            buf = []
        elif stripped == "===END===" and current is not None:
            files[current] = "\n".join(buf).strip() + "\n"
            current = None
        elif current is not None:
            buf.append(line)
    return files


def _prompt_qc_context(input_dir: Path, work: Path) -> list[Path]:
    return [input_dir, input_dir / "home", input_dir / "task", work]


def _prompt_self_repair_sweep(input_dir: Path, work: Path) -> None:
    # Delegates to the shared per-stage sweep so severity honoring, the 3-round
    # auto-fix retry loop, QC report writing, and blocking-halt semantics stay
    # identical to every other mid-stage sweep in this file.
    _stage_qc_sweep(
        "prompt",
        PROMPT_QC_DIR,
        work,
        _prompt_qc_context(input_dir, work),
        PROMPT_ARTIFACTS,
    )


_VERDICT_FALLBACK = (("verdict: fail", "fail"), ("verdict: review", "warn"), ("verdict: pass", "pass"))


def _parse_qc_verdict(raw: str) -> str:
    low = raw.lower()
    for verdict in ("fail", "warn", "pass"):
        if f"qc_result: {verdict}" in low:
            return verdict
    # 70_prompt_qc_review.md ends in `VERDICT: PASS|REVIEW|FAIL`, not QC_RESULT;
    # map its native vocabulary so this gate is not silently discarded as a default fail.
    for needle, verdict in _VERDICT_FALLBACK:
        if needle in low:
            return verdict
    return "fail"


def _selection_pin_changed(before: dict, after: dict) -> bool:
    for key in SELECTION_KEYS:
        if before.get(key) != after.get(key):
            return True
    return False


# Generic per-stage QC sweep. Each generating stage audits its artifact against
# references/<name>_qc/ the moment it is produced, auto-fixing then re-checking,
# and halting on a residual blocking failure. Folder naming is the wiring contract
# the QC team relies on to drop in gates without touching this code.
QC_STAGE_MAX_FIX_ITERS = 3


def _discover_gates(gate_dir: Path) -> list[Path]:
    if not gate_dir.is_dir():
        return []
    return [
        p
        for p in sorted(gate_dir.iterdir())
        if p.is_file() and p.suffix in {".py", ".md"} and p.stem[:2].isdigit()
    ]


def _load_severity(gate_dir: Path) -> dict[str, str]:
    manifest = gate_dir / "manifest.yaml"
    if not manifest.is_file():
        return {}
    data = _load_yaml(manifest) or {}
    return {k: str(v).lower() for k, v in data.get("severity", {}).items()}


def _run_mechanical_stage_gate(gate: Path, work: Path) -> tuple[bool, str]:
    result = subprocess.run(
        [sys.executable, str(gate), str(work)], text=True, capture_output=True
    )
    print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    return result.returncode == 0, (result.stdout or "") + (result.stderr or "")


_DEFAULT_FIX_DIRECTIVE = (
    "Preserve all correctness constraints; only make the minimum changes needed "
    "to clear the reported failure(s)."
)
_WORD_COUNT_UNDER_DIRECTIVE = (
    "The heavy turn is below the 800-word floor. Expand it back into the 800-1000 "
    "word band by adding more world: more surfaces, more stakes, more named "
    "outcomes, more stated scale. Do NOT pad with restated context the agent can "
    "read in its own files, and do NOT add step-by-step instructions or narrate "
    "how to do the work. Preserve all correctness constraints."
)
_WORD_COUNT_OVER_DIRECTIVE = (
    "The heavy turn is above the word ceiling. Tighten it back into the 800-1000 "
    "word band by cutting restated context, hand-over of the plan, and any "
    "how-to narration first; never cut required world or stakes below 800 words. "
    "Preserve all correctness constraints."
)


def _gate_fix_directive(gate: Path, failure_output: str) -> str:
    if "word_count" not in gate.stem:
        return _DEFAULT_FIX_DIRECTIVE
    # word_count gate prints '... heavy turn = <N> words ...'; branch the fix on
    # whether the turn is too short (expand with world) or too long (trim leaks).
    match = re.search(r"heavy turn\s*=\s*(\d+)\s*words", failure_output)
    if match and int(match.group(1)) < 800:
        return _WORD_COUNT_UNDER_DIRECTIVE
    if match and int(match.group(1)) > 800:
        return _WORD_COUNT_OVER_DIRECTIVE
    return _DEFAULT_FIX_DIRECTIVE


def _mechanical_gate_fix(
    gate: Path,
    context_dirs: list[Path],
    work: Path,
    artifacts: tuple[str, ...],
    failure_output: str,
) -> None:
    # Model-driven fix pass for a failing .py QC gate. Hands the mechanical
    # check's own failure output to the model as the fix directive so the next
    # attempt of the .py gate can pass. Without this hook the sweep's retry
    # budget is useless for .py gates (they are deterministic on unchanged input).
    artifact_list = ", ".join(f"{work / name}" for name in artifacts)
    directive = _gate_fix_directive(gate, failure_output)
    synth_path = work / f"_gate_fix_{gate.stem}.md"
    synth_path.write_text(
        f"# Mechanical QC Gate Failure \u2014 {gate.name}\n\n"
        "The following mechanical check ran on the artifact(s) under review and "
        "reported a failure. Revise the artifact(s) so the check will pass on the "
        f"next run. {directive}\n\n"
        "## Gate output\n\n"
        f"```\n{failure_output.strip()}\n```\n"
    )
    try:
        out = _opencode_stage(
            synth_path,
            context_dirs,
            f"The artifact(s) under review: {artifact_list}. REVISE the failing "
            "artifact(s) to fix the mechanical check reported above while preserving "
            "correctness. "
            + ARTIFACT_MARKER_INSTRUCTION
            + " Emit only the artifact(s) you changed, each wrapped in its markers.",
        )
    finally:
        synth_path.unlink(missing_ok=True)
    files = _split_artifacts(out)
    wrote = [name for name in artifacts if name in files]
    for name in wrote:
        (work / name).write_text(files[name])
    if wrote:
        print(f"[{gate.parent.name} FIXED] {gate.name} (revised {', '.join(sorted(wrote))})")


def _stage_gate_autofix(
    gate: Path,
    context_dirs: list[Path],
    work: Path,
    artifacts: tuple[str, ...],
    input_dir: Path | None = None,
) -> tuple[str, str, bool]:
    """Run one model-audit gate in fix mode: the model may revise the artifact(s).

    Returns (self_verdict, raw_model_output, wrote_artifact). The self_verdict is
    the fixer's own report and must not be trusted alone when it edited a file;
    the caller re-verifies via _stage_gate_check in that case. The model re-emits
    any changed file wrapped in ===FILE: name=== markers; those are written back
    into the work dir so the next gate (and the final check) sees the improved
    artifact. When input_dir is given, enriched mock_data files are written back
    under guardrails.
    """
    artifact_list = ", ".join(f"{work / name}" for name in artifacts)
    mock_clause = (
        " You may also enrich persona mock data under the values-only rules "
        "(no schema change, no banned service, preserve valid placeholders) by "
        "re-emitting the corrected 'mock_data/<svc>-api/<file>' files."
        if input_dir is not None
        else ""
    )
    out = _opencode_stage(
        gate,
        context_dirs,
        f"The artifact(s) under review: {artifact_list}. Apply the QC checklist "
        "in the system prompt above. If it already passes, re-emit nothing and end "
        "with 'QC_RESULT: pass'. If it violates the checklist, REVISE the failing "
        "artifact(s) to fix every blocking defect while preserving correctness, then "
        + ARTIFACT_MARKER_INSTRUCTION
        + " Emit only the artifact(s) you changed, each wrapped in its markers."
        + mock_clause
        + " After any emitted files, end your reply with a final line exactly of the "
        "form 'QC_RESULT: pass' or 'QC_RESULT: warn' or 'QC_RESULT: fail'.",
    )
    files = _split_artifacts(out)
    if input_dir is not None:
        enriched = _guarded_mock_writeback(input_dir, files)
        if enriched:
            print(
                f"[{gate.parent.name} ENRICHED] {gate.name} "
                f"({', '.join(e['file'] for e in enriched)})"
            )
    wrote = [name for name in artifacts if name in files]
    for name in wrote:
        (work / name).write_text(files[name])
    if wrote:
        print(f"[{gate.parent.name} FIXED] {gate.name} (revised {', '.join(sorted(wrote))})")
    return _parse_qc_verdict(out), out, bool(wrote)


def _stage_gate_check(gate: Path, context_dirs: list[Path], work: Path, artifacts: tuple[str, ...]) -> str:
    if gate.suffix == ".py":
        passed, _ = _run_mechanical_stage_gate(gate, work)
        return "pass" if passed else "fail"
    artifact_list = ", ".join(f"{work / name}" for name in artifacts)
    out = _opencode_stage(
        gate,
        context_dirs,
        f"The artifact(s) under review: {artifact_list}. Apply the QC checklist in "
        "the system prompt above as a CHECK ONLY. Do not modify or re-emit any file. "
        "Run every phase MENTALLY without narrating. Map your native verdict to the "
        "standard vocabulary: 'Push Ready'/'PASS' -> pass; 'Needs Fixes'/'PASS WITH "
        "WARNING' (advisory only) -> warn; 'Fail'/'FAIL'/'FAIL-HARD' -> fail. End "
        "with a final line exactly of the form 'QC_RESULT: pass' or 'QC_RESULT: "
        "warn' or 'QC_RESULT: fail'.",
    )
    return _parse_qc_verdict(out)


def _stage_qc_sweep(
    stage_name: str,
    gate_dir: Path,
    work: Path,
    context_dirs: list[Path],
    artifacts: tuple[str, ...],
    enrich_input_dir: Path | None = None,
) -> None:
    """Blocking auto-fix QC sweep for one generating stage.

    For each gate: mechanical .py gates re-run (up to the fix budget) until they
    pass or the budget is exhausted; model-audit .md gates run in fix mode so the
    model revises the artifact, re-checked each round. Any gate whose residual
    verdict is "fail" at "block" severity raises StageError, halting the pipeline.
    """
    gates = _discover_gates(gate_dir)
    if not gates:
        return
    severity = _load_severity(gate_dir)
    print(f"\n--- {stage_name} QC sweep ({gate_dir.name}) ---")
    blocking_failures: list[str] = []
    report_entries: list[tuple[str, str, str]] = []
    for gate in gates:
        level = severity.get(gate.name, "block")
        verdict = "fail"
        detail = ""
        for attempt in range(1, QC_STAGE_MAX_FIX_ITERS + 1):
            if gate.suffix == ".py":
                passed, gate_output = _run_mechanical_stage_gate(gate, work)
                verdict = "pass" if passed else "fail"
                detail = gate_output
            else:
                self_verdict, detail, wrote = _stage_gate_autofix(
                    gate, context_dirs, work, artifacts, enrich_input_dir
                )
                if wrote:
                    # The fixer edited the artifact; never trust its self-report.
                    # Re-run the gate in check-only mode for an independent verdict.
                    verdict = _stage_gate_check(gate, context_dirs, work, artifacts)
                else:
                    verdict = self_verdict
            if verdict in ("pass", "warn"):
                break
            if attempt < QC_STAGE_MAX_FIX_ITERS:
                print(f"[{gate_dir.name} RETRY] {gate.name} still failing "
                      f"(attempt {attempt}/{QC_STAGE_MAX_FIX_ITERS})")
                if gate.suffix == ".py":
                    _mechanical_gate_fix(gate, context_dirs, work, artifacts, detail)
        if verdict == "pass":
            print(f"[{gate_dir.name} PASS] {gate.name}")
        elif verdict == "warn":
            print(f"[{gate_dir.name} WARN] {gate.name} (non-blocking)")
        elif level == "warn":
            print(f"[{gate_dir.name} WARN] {gate.name} (fail downgraded by severity)")
            verdict = "warn"
        else:
            print(f"[{gate_dir.name} FAIL] {gate.name}")
            blocking_failures.append(gate.name)
        report_entries.append((gate.name, verdict, detail))
    _write_qc_report(work, stage_name, gate_dir.name, report_entries, halted=bool(blocking_failures))
    if blocking_failures:
        raise StageError(
            f"{stage_name} QC failed after auto-fix: {', '.join(blocking_failures)}"
        )


RUBRIC_ANTI_NARRATION = (
    "\n\nDo NOT narrate your process or think out loud in the response. Do all "
    "reasoning silently. Your ENTIRE response MUST be exactly one JSON object "
    "inside a single ```json fenced code block containing the three required keys "
    "and nothing else \u2014 no preamble, no explanation, no text before or after the "
    "fence."
)


def stage_rubric(input_dir: Path, work: Path, harness_dir: Path, meta: dict) -> None:
    required = " ".join(meta.get("required_apis", []))
    distractor = " ".join(meta.get("distractor_apis", []))
    base_instruction = (
        f"Read {work / 'prompt.txt'}. Generate rubric.json, test_outputs.py, and "
        f"test_weights.json as one JSON object. Required APIs: {required}. "
        f"Distractor APIs: {distractor}."
    )
    context_dirs = [input_dir, input_dir / "home", input_dir / "mock_data", harness_dir]

    attempts = 3
    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        instruction = base_instruction if attempt == 1 else base_instruction + RUBRIC_ANTI_NARRATION
        raw = _opencode_stage(REFERENCES / "rubric_pytest_combined.md", context_dirs, instruction)
        try:
            payload = _extract_json(raw)
            _write_channel_files(work, payload)
        except StageError as exc:
            last_error = exc
            print(f"  [rubric attempt {attempt}/{attempts} produced no usable rubric: {exc}]")
            continue
        sweep_context = [input_dir, input_dir / "home", input_dir / "mock_data", work]
        _stage_qc_sweep("rubric", RUBRIC_QC_DIR, work, sweep_context, ("rubric.json",))
        _stage_qc_sweep(
            "pytest", PYTEST_QC_DIR, work, sweep_context,
            ("test_outputs.py", "test_weights.json"),
        )
        return
    raise StageError(f"rubric stage failed after {attempts} attempts: {last_error}")


def stage_truth(input_dir: Path, work: Path, harness_dir: Path) -> None:
    out = _opencode_stage(
        REFERENCES / "truth_guide.md",
        [
            input_dir,
            input_dir / "home",
            input_dir / "mock_data",
            input_dir / "task",
            work,
        ],
        f"Read the bundle in progress at {work} and inputs at {input_dir}. "
        "Produce TRUTH.md following the locked 9-section structure. "
        "Emit the COMPLETE document as your final output wrapped exactly as "
        "===FILE: TRUTH.md=== on its own line, then the full document, then "
        "===END=== on its own line. Do not put any other prose after ===END===.",
    )
    files = _split_artifacts(out)
    if "TRUTH.md" not in files:
        raise StageError("truth stage did not emit a ===FILE: TRUTH.md=== block")
    (work / "TRUTH.md").write_text(files["TRUTH.md"])
    _stage_qc_sweep(
        "truth", TRUTH_QC_DIR, work,
        [input_dir, input_dir / "home", input_dir / "mock_data", input_dir / "task", work],
        ("TRUTH.md",),
    )


def stage_assemble(
    input_dir: Path, work: Path, meta_path: Path, harness_dir: Path, out_dir: Path
) -> None:
    result = _run(
        [
            sys.executable,
            str(SCRIPTS / "assemble.py"),
            str(input_dir),
            str(work),
            str(meta_path),
            str(TEMPLATES),
            str(harness_dir),
            str(out_dir),
        ]
    )
    if result.returncode != 0:
        raise StageError("assembly failed")


def stage_qc(out_dir: Path, harness_dir: Path, work: Path) -> None:
    gates = _discover_qc_gates()
    if not gates:
        print("no QC gates found in references/qc/ (skipping)")
        return
    severity = _load_qc_severity()
    blocking_failures: list[str] = []
    report_entries: list[tuple[str, str, str]] = []
    for gate in gates:
        verdict, detail = _run_qc_gate(gate, out_dir, harness_dir)
        level = severity.get(gate.name, "block")
        if verdict == "pass":
            print(f"[QC PASS] {gate.name}")
        elif verdict == "warn":
            print(f"[QC WARN] {gate.name} (advisory findings, non-blocking)")
        elif level == "warn":
            print(f"[QC WARN] {gate.name} (fail downgraded by severity, non-blocking)")
            verdict = "warn"
        else:
            print(f"[QC FAIL] {gate.name}")
            blocking_failures.append(gate.name)
        report_entries.append((gate.name, verdict, detail))
    _write_qc_report(work, "qc", QC_DIR.name, report_entries, halted=bool(blocking_failures))
    if blocking_failures:
        raise StageError(f"QC gates failed: {', '.join(blocking_failures)}")


def _discover_qc_gates() -> list[Path]:
    if not QC_DIR.is_dir():
        return []
    return [
        p
        for p in sorted(QC_DIR.iterdir())
        if p.is_file() and p.suffix in {".py", ".md"} and p.stem[:2].isdigit()
    ]


def _load_qc_severity() -> dict[str, str]:
    manifest = QC_DIR / "manifest.yaml"
    if not manifest.is_file():
        return {}
    data = _load_yaml(manifest) or {}
    return {k: str(v).lower() for k, v in data.get("severity", {}).items()}


def _run_qc_gate(gate: Path, out_dir: Path, harness_dir: Path) -> tuple[str, str]:
    if gate.suffix == ".py":
        result = subprocess.run(
            [sys.executable, str(gate), str(out_dir), str(harness_dir)],
            text=True,
            capture_output=True,
        )
        print(result.stdout, end="")
        detail = (result.stdout or "") + (result.stderr or "")
        return ("pass" if result.returncode == 0 else "fail"), detail
    base_instruction = (
        f"Audit the bundle at {out_dir} by applying the QC meta-prompt in the "
        "system prompt above. Run every phase MENTALLY: do not narrate your "
        "step-by-step verification, do not print your intermediate reasoning or "
        "per-value checks. Your reply must be SHORT: emit only the final "
        "findings summary (Major/Moderate/Minor lists, or 'None') and the "
        "verdict. Map your native verdict to the standard result vocabulary: any "
        "'Push Ready' or 'PASS' verdict maps to pass; any 'Needs Fixes' or "
        "'PASS WITH WARNING' verdict (advisory findings only, no structural or "
        "Major/FAIL-HARD defect) maps to warn; any 'Fail', 'FAIL', or "
        "'FAIL-HARD' verdict maps to fail. Your ENTIRE reply MUST end with a "
        "final line exactly of the form 'QC_RESULT: pass' or 'QC_RESULT: warn' "
        "or 'QC_RESULT: fail'. Do not stop before emitting that line."
    )
    retry_nudge = (
        "\n\nCRITICAL: A previous attempt ran out of output budget while "
        "narrating and never emitted the verdict. Do NOT narrate. Do NOT walk "
        "through each check. Go straight to the findings summary and the final "
        "'QC_RESULT: pass|warn|fail' line NOW, in as few words as possible."
    )
    raw = ""
    for attempt in range(1, QC_MD_MAX_ATTEMPTS + 1):
        instruction = base_instruction
        if attempt > 1:
            instruction = base_instruction + retry_nudge
        raw = _opencode_stage(gate, [out_dir], instruction)
        print(raw, end="" if raw.endswith("\n") else "\n")
        if "qc_result:" in raw.lower():
            return _parse_qc_verdict(raw), raw
        if attempt < QC_MD_MAX_ATTEMPTS:
            print(
                f"[QC {gate.name} attempt {attempt}/{QC_MD_MAX_ATTEMPTS} "
                "produced no verdict sentinel; retrying with anti-narration nudge]"
            )
    return "fail", raw


def _json_candidates(raw: str):
    for block in re.findall(r"```(?:json)?\s*\n(.*?)```", raw, re.DOTALL):
        stripped = block.strip()
        if stripped.startswith("{"):
            yield stripped
    balanced = _balanced_object(raw)
    if balanced is not None:
        yield balanced
    start = raw.find("{")
    end = raw.rfind("}")
    if start != -1 and end != -1 and start < end:
        yield raw[start : end + 1]


def _balanced_object(raw: str) -> str | None:
    start = raw.find("{")
    if start == -1:
        return None
    depth = 0
    in_string = False
    escape = False
    for i in range(start, len(raw)):
        char = raw[i]
        if escape:
            escape = False
            continue
        if char == "\\" and in_string:
            escape = True
            continue
        if char == '"':
            in_string = not in_string
            continue
        if in_string:
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return raw[start : i + 1]
    return None


def _extract_json(raw: str) -> dict:
    for candidate in _json_candidates(raw):
        try:
            return json.loads(candidate)
        except json.JSONDecodeError:
            continue
    preview = raw[:300].replace("\n", "\\n")
    raise StageError(f"no valid JSON object found in model output; head={preview!r}")


def _write_channel_files(work: Path, payload: dict) -> None:
    mapping = {
        "tests/rubric.json": "rubric.json",
        "tests/test_outputs.py": "test_outputs.py",
        "tests/test_weights.json": "test_weights.json",
    }
    for key, out_name in mapping.items():
        if key not in payload and out_name not in payload:
            raise StageError(f"model output missing key: {key}")
        content = payload.get(key, payload.get(out_name))
        target = work / out_name
        if out_name.endswith(".json") and not isinstance(content, str):
            target.write_text(json.dumps(content, indent=2) + "\n")
        else:
            target.write_text(content if isinstance(content, str) else str(content))


def _pause(stage: str, auto: bool) -> None:
    if auto:
        return
    print(f"\n--- stage '{stage}' complete. Review outputs. ---")
    reply = input("Enter to continue, 'q' to stop: ").strip().lower()
    if reply == "q":
        raise SystemExit("stopped by operator")


def _rerun_midstage_qc(stage: str, input_dir: Path, work: Path) -> None:
    if stage == "prompt" and (work / "PROMPT.md").is_file():
        _prompt_self_repair_sweep(input_dir, work)
        if (work / "api_selection.json").is_file():
            _stage_qc_sweep(
                "mock_data",
                MOCK_DATA_QC_DIR,
                work,
                [input_dir, input_dir / "home", input_dir / "mock_data", work],
                ("api_selection.json",),
                enrich_input_dir=input_dir,
            )
    elif stage == "rubric" and (work / "rubric.json").is_file():
        sweep_context = [input_dir, input_dir / "home", input_dir / "mock_data", work]
        _stage_qc_sweep("rubric", RUBRIC_QC_DIR, work, sweep_context, ("rubric.json",))
        if (work / "test_outputs.py").is_file() and (work / "test_weights.json").is_file():
            _stage_qc_sweep(
                "pytest", PYTEST_QC_DIR, work, sweep_context,
                ("test_outputs.py", "test_weights.json"),
            )
    elif stage == "truth" and (work / "TRUTH.md").is_file():
        _stage_qc_sweep(
            "truth", TRUTH_QC_DIR, work,
            [input_dir, input_dir / "home", input_dir / "mock_data", input_dir / "task", work],
            ("TRUTH.md",),
        )


def run_pipeline(args: argparse.Namespace) -> int:
    input_dir = Path(args.input).expanduser().resolve()
    work = Path(args.work).expanduser().resolve()
    out_dir = Path(args.out).expanduser().resolve()
    harness_dir = Path(args.harness).expanduser().resolve()
    meta_path = Path(args.meta).expanduser().resolve()
    work.mkdir(parents=True, exist_ok=True)

    meta = json.loads(Path(meta_path).read_text()) if meta_path.suffix == ".json" else _load_yaml(meta_path)

    manifest = _load_manifest(work)
    manifest["persona_hash"] = _hash_persona(input_dir)

    # On resume the prompt branch is skipped, so its api_selection merge never
    # runs and rubric/assemble would fall back to raw meta.yaml apis. Re-merge here.
    if args.resume and manifest["stages"].get("prompt", {}).get("status") == "complete":
        api_selection_path = work / "api_selection.json"
        if api_selection_path.exists():
            selection = _read_api_selection(work)
            meta = _merge_selection(meta, selection)
            meta_path = _persist_meta(work, meta)

    only = set(args.stage) if args.stage else None
    noninteractive = args.auto or _has_design_flags(args)
    for stage in STAGES:
        if only and stage not in only:
            continue
        done = manifest["stages"].get(stage, {}).get("status") == "complete"
        if args.resume and done and not only:
            # Resume must re-audit existing artifacts — a manifest-complete stage
            # from a crashed prior run may still hold a defective artifact.
            print(f"[skip] {stage} body already complete — re-running mid-stage QC")
            try:
                _rerun_midstage_qc(stage, input_dir, work)
            except StageError as exc:
                _record(manifest, stage, "failed", error=str(exc))
                _save_manifest(work, manifest)
                print(f"\nstage '{stage}' FAILED on resume QC: {exc}", file=sys.stderr)
                return 1
            continue
        print(f"\n=== stage: {stage} ===")
        try:
            if stage == "validate":
                stage_validate(input_dir, harness_dir)
            elif stage == "prompt":
                if _has_design_flags(args):
                    design = _design_from_args(args)
                elif args.auto:
                    design = None
                else:
                    design = _ask_operator_design(input_dir)
                selection = stage_prompt(input_dir, work, noninteractive, design)
                meta = _merge_selection(meta, selection)
                meta_path = _persist_meta(work, meta)
            elif stage == "rubric":
                stage_rubric(input_dir, work, harness_dir, meta)
            elif stage == "truth":
                stage_truth(input_dir, work, harness_dir)
            elif stage == "assemble":
                stage_assemble(input_dir, work, meta_path, harness_dir, out_dir)
            elif stage == "qc":
                stage_qc(out_dir, harness_dir, work)
            _record(manifest, stage, "complete")
            _save_manifest(work, manifest)
        except (StageError, SystemExit) as exc:
            _record(manifest, stage, "failed", error=str(exc))
            _save_manifest(work, manifest)
            print(f"\nstage '{stage}' FAILED: {exc}", file=sys.stderr)
            return 1
        _pause(stage, noninteractive)

    print(f"\nbundle ready at {out_dir}")
    return 0


def _load_yaml(path: Path) -> dict:
    import yaml

    return yaml.safe_load(path.read_text())


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="skoll-bundle", description=__doc__.splitlines()[0])
    p.add_argument("--input", required=True, help="persona-team input dir (7 MD files + home/ + task/ + mock_data/)")
    p.add_argument("--work", required=True, help="scratch dir for intermediates + manifest")
    p.add_argument("--out", required=True, help="destination bundle dir")
    p.add_argument("--meta", required=True, help="design_metadata.yaml/.json")
    p.add_argument(
        "--harness",
        default=str(Path("SKOLL_GK/Environment_SN_Harness")),
        help="environment harness dir (service.toml registry source)",
    )
    p.add_argument("--auto", action="store_true", help="run unattended (no pauses)")
    p.add_argument("--resume", action="store_true", help="skip already-complete stages")
    p.add_argument(
        "--turn-shape",
        choices=["single", "multi"],
        help="prompt design: turn shape (omit to let the model infer)",
    )
    p.add_argument(
        "--domain",
        choices=["enterprise", "personal", "professional"],
        help="prompt design: task domain (omit to let the model infer)",
    )
    p.add_argument(
        "--anchor",
        help="prompt design: fixed anchor event or deadline (omit if none)",
    )
    p.add_argument(
        "--stage",
        nargs="+",
        choices=STAGES,
        help="run only these stage(s) (regenerate)",
    )
    return p


def main(argv: list[str]) -> int:
    args = build_parser().parse_args(argv)
    return run_pipeline(args)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

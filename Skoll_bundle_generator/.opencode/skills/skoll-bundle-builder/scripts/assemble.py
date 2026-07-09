#!/usr/bin/env python3
"""Stage 4: assemble the native harness bundle from generated + input parts.

Deterministic. Consumes:
  - input_dir/*.md                   (persona team, 7 MDs at root)
  - input_dir/mock_data/<svc>-api/   (persona team, FULL ~101-svc catalog)
  - input_dir/home/                  (persona team, artifact tree = workspace)
  - work_dir/PROMPT.md               (Stage 1)
  - work_dir/rubric.json             (Stage 2)
  - work_dir/test_outputs.py         (Stage 2)
  - work_dir/test_weights.json       (Stage 2)
  - work_dir/TRUTH.md                (Stage 3)
  - design_metadata.yaml             (operator / Stage 1 notes; carries the
                                      selected required/distractor API subset)

Only the SELECTED API subset (required + distractor) is copied into the
bundle's mock_data/, not the whole catalog. The home/ tree is copied intact
to data/ as the agent workspace. Produces the native layout in out_dir:
task.yaml (with the built system_prompt), README.md, persona/, mock_data/
(subset), data/ (from home/), plus the generated PROMPT.md/rubric.json/
test_outputs.py/test_weights.json/TRUTH.md. No inject/ folder is emitted.
"""
from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

import yaml

from build_service_registry import build_registry

PERSONA_STATIC_ORDER = ["AGENTS", "SOUL", "IDENTITY", "USER", "TOOLS", "MEMORY"]
PERSONA_DYNAMIC_ORDER = ["HEARTBEAT"]
DEFAULT_RUNTIME_MODEL = "claude-sonnet-4-20250514"
DEFAULT_RUNTIME_THINKING = "off"


def _read(path: Path) -> str:
    return path.read_text().rstrip("\n")


def _yaml_scalar(value: object) -> str:
    if value is True:
        return "on"
    if value is False:
        return "off"
    return str(value)


def _indent_block(text: str, spaces: int = 2) -> str:
    pad = " " * spaces
    return "\n".join(pad + line if line else line for line in text.split("\n"))


def build_system_prompt(persona_dir: Path, templates_dir: Path, meta: dict) -> str:
    preamble = _read(templates_dir / "system_prompt_preamble.txt")
    preamble = preamble.replace("{{PRINCIPAL}}", meta["principal"])
    cache_block = _read(templates_dir / "system_prompt_cache_boundary.txt")
    footer = _read(templates_dir / "system_prompt_footer.txt")
    footer = footer.replace("{{RUNTIME_MODEL}}", str(meta.get("runtime_model", DEFAULT_RUNTIME_MODEL)))
    footer = footer.replace("{{RUNTIME_THINKING}}", _yaml_scalar(meta.get("runtime_thinking", DEFAULT_RUNTIME_THINKING)))

    parts = [preamble]
    for name in PERSONA_STATIC_ORDER:
        parts.append(f"## {name}.md\n\n" + _read(persona_dir / f"{name}.md"))
    parts.append(cache_block)
    for name in PERSONA_DYNAMIC_ORDER:
        parts.append(f"## {name}.md\n\n" + _read(persona_dir / f"{name}.md"))
    parts.append(footer)
    return "\n\n".join(parts)


def count_pytest_probes(test_file: Path) -> int:
    if not test_file.is_file():
        return 0
    return len(re.findall(r"^\s*def (test_\w+)", test_file.read_text(), re.MULTILINE))


def count_rubric_criteria(rubric_file: Path) -> int:
    if not rubric_file.is_file():
        return 0
    data = json.loads(rubric_file.read_text())
    if isinstance(data, list):
        return len(data)
    for key in ("criteria", "rubric", "items"):
        if isinstance(data.get(key), list):
            return len(data[key])
    return 0


def _copy_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def build_task_yaml(meta: dict, system_prompt: str, probes: int, criteria: int) -> str:
    shape = meta["shape"]
    doc_lines = [
        f"task_id: {meta['task_id']}",
        f"variant: {meta['variant']}",
        f"principal: {meta['principal']}",
        f"timezone: {meta['timezone']}",
        f"domain: {meta['domain']}",
        "shape:",
        f"  turns: {shape['turns']}",
        f"  days: {shape['days']}",
        f"  difficulty: {shape['difficulty']}",
        f"  multi_agent_complex_turns: {json.dumps(shape.get('multi_agent_complex_turns', []))}",
    ]
    threshold = meta.get("confirmation_threshold")
    if threshold:
        doc_lines += [
            "confirmation_threshold:",
            f"  single_charge_usd: {threshold['single_charge_usd']}",
            f"  recurring_monthly_usd: {threshold['recurring_monthly_usd']}",
        ]
    doc_lines.append(f"drafting_language: {meta.get('drafting_language', 'en')}")
    doc_lines.append("required_apis:")
    doc_lines += [f"  - {api}" for api in meta["required_apis"]]
    doc_lines.append("distractor_apis:")
    doc_lines += [f"  - {api}" for api in meta["distractor_apis"]]
    doc_lines.append("deliverables:")
    doc_lines += [f"  - {d}" for d in meta.get("deliverables", [])]
    doc_lines += [
        "grading:",
        "  channel_a: test_outputs.py",
        "  channel_b: rubric.json",
        "  weights: test_weights.json",
        f"  pytest_probes: {probes}",
        f"  rubric_criteria: {criteria}",
        f"persona: {meta['principal']}",
        "system_prompt: |-",
        _indent_block(system_prompt, 2),
    ]
    return "\n".join(doc_lines) + "\n"


def _surfaces_section(meta: dict) -> str:
    req = ", ".join(meta["required_apis"])
    dis = ", ".join(meta["distractor_apis"])
    return (
        "## Surfaces\n\n"
        f"- **Required ({len(meta['required_apis'])}):** {req}\n"
        f"- **Distractors ({len(meta['distractor_apis'])}):** {dis}"
    )


def _grading_section(probes: int, criteria: int) -> str:
    return (
        "## Grading\n\n"
        f"- Channel A: `test_outputs.py` with `test_weights.json` ({probes} probes).\n"
        f"- Channel B: `rubric.json` ({criteria} criteria, R1\u2013R{criteria})."
    )


def build_readme(meta: dict, work_dir: Path, probes: int, criteria: int) -> str:
    authored = (work_dir / "README.md").read_text().rstrip()
    surfaces = _surfaces_section(meta)
    grading = _grading_section(probes, criteria)

    marker = "## Traps"
    if marker in authored:
        head, tail = authored.split(marker, 1)
        body = f"{head.rstrip()}\n\n{surfaces}\n\n{marker}{tail}"
    else:
        body = f"{authored}\n\n{surfaces}"
    return f"{body}\n\n{grading}\n"


REQUIRED_API_FLOOR = 12
BANNED_APIS = frozenset({"dropbox-api", "google-drive-api", "google-contacts-api"})


def _validate_apis_against_inputs(meta: dict, input_dir: Path, registry: dict) -> list[str]:
    errors: list[str] = []
    mock_dir = input_dir / "mock_data"
    catalog = {d.name for d in mock_dir.iterdir() if d.is_dir()} if mock_dir.is_dir() else set()
    required = set(meta["required_apis"])
    distractor = set(meta["distractor_apis"])
    declared = required | distractor

    overlap = required & distractor
    if overlap:
        errors.append(f"APIs marked both required and distractor: {sorted(overlap)}")
    missing_from_catalog = declared - catalog
    if missing_from_catalog:
        errors.append(f"selected APIs absent from mock_data catalog: {sorted(missing_from_catalog)}")
    unknown = [a for a in declared if a not in registry]
    if unknown:
        errors.append(f"APIs not in service registry: {sorted(unknown)}")
    if len(meta["required_apis"]) < REQUIRED_API_FLOOR:
        errors.append(
            f"required_apis has {len(meta['required_apis'])}; every task must declare at "
            f"least {REQUIRED_API_FLOOR} required APIs"
        )
    banned = declared & BANNED_APIS
    if banned:
        errors.append(f"banned APIs must not be selected: {sorted(banned)}")
    return errors


def _check_ratio(meta: dict) -> str | None:
    n_req = len(meta["required_apis"])
    n_dis = len(meta["distractor_apis"])
    if n_req == 0 or n_dis == 0:
        return f"required:distractor is {n_req}:{n_dis}, expected roughly 1:1 to 2:1"
    ratio = n_req / n_dis
    if ratio < 0.5 or ratio > 2.0:
        return f"required:distractor is {n_req}:{n_dis} ({ratio:.2f}), expected 1:1 to 2:1"
    return None


def assemble(
    input_dir: Path,
    work_dir: Path,
    meta_path: Path,
    templates_dir: Path,
    harness_dir: Path,
    out_dir: Path,
) -> list[str]:
    meta = yaml.safe_load(meta_path.read_text())
    registry = build_registry(harness_dir)

    errors = _validate_apis_against_inputs(meta, input_dir, registry)
    if errors:
        return errors

    ratio_warning = _check_ratio(meta)
    if ratio_warning:
        print(f"[assemble] WARNING: {ratio_warning}", file=sys.stderr)

    out_dir.mkdir(parents=True, exist_ok=True)

    system_prompt = build_system_prompt(input_dir, templates_dir, meta)
    probes = count_pytest_probes(work_dir / "test_outputs.py")
    criteria = count_rubric_criteria(work_dir / "rubric.json")

    (out_dir / "task.yaml").write_text(build_task_yaml(meta, system_prompt, probes, criteria))
    (out_dir / "README.md").write_text(build_readme(meta, work_dir, probes, criteria))

    for fname in ("PROMPT.md", "rubric.json", "test_outputs.py", "test_weights.json", "TRUTH.md"):
        src = work_dir / fname
        if src.is_file():
            shutil.copy2(src, out_dir / fname)

    _copy_persona(input_dir, out_dir / "persona")
    _copy_mock_subset(input_dir / "mock_data", out_dir / "mock_data", meta)
    _copy_tree(input_dir / "home", out_dir / "data")

    return []


def _copy_persona(input_dir: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True)
    for name in PERSONA_STATIC_ORDER + PERSONA_DYNAMIC_ORDER:
        shutil.copy2(input_dir / f"{name}.md", dst / f"{name}.md")


def _copy_mock_subset(src_root: Path, dst_root: Path, meta: dict) -> None:
    if dst_root.exists():
        shutil.rmtree(dst_root)
    dst_root.mkdir(parents=True)
    selected = list(meta["required_apis"]) + list(meta["distractor_apis"])
    for api in selected:
        shutil.copytree(src_root / api, dst_root / api)


def main(argv: list[str]) -> int:
    if len(argv) < 7:
        print(
            "usage: assemble.py <input_dir> <work_dir> <design_metadata.yaml> "
            "<templates_dir> <harness_dir> <out_dir>",
            file=sys.stderr,
        )
        return 2
    input_dir = Path(argv[1]).expanduser().resolve()
    work_dir = Path(argv[2]).expanduser().resolve()
    meta_path = Path(argv[3]).expanduser().resolve()
    templates_dir = Path(argv[4]).expanduser().resolve()
    harness_dir = Path(argv[5]).expanduser().resolve()
    out_dir = Path(argv[6]).expanduser().resolve()

    errors = assemble(input_dir, work_dir, meta_path, templates_dir, harness_dir, out_dir)
    if errors:
        for e in errors:
            print(f"[assemble] ERROR: {e}", file=sys.stderr)
        return 1
    print(f"[assemble] bundle written to {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

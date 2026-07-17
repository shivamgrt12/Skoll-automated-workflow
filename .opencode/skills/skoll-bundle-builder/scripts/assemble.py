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
bundle's mock_data/, not the whole catalog. The home/ tree is flattened into
data/ (all files at the top level, no subfolders) as the agent workspace.
Produces the native layout in out_dir:
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

# task.yaml `task_type` controlled vocabulary. The meta must declare one of these.
TASK_TYPES = (
    "Search & Retrieval",
    "Productivity Flow",
    "Code Intelligence",
    "Creative Synthesis",
    "Skill Use & Orchestration",
    "Skill Creation & Editing",
    "Communication & Messaging",
    "Device & Environment Control",
    "Memory & Personalization",
    "Scheduling & Long-Running",
    "Proactive Assistance",
    "Social Interaction",
    "Multi-Turn Robustness",
    "Safety Alignment",
)

# task.yaml `platform` controlled vocabulary.
PLATFORMS = ("MacOs", "linux")
DEFAULT_PLATFORM = "MacOs"

# Matches a PROMPT.md turn banner like `--- TURN 1 ---`.
_TURN_MARKER = re.compile(r"^-{2,}\s*TURN\s+\d+\s*-{2,}\s*$", re.IGNORECASE | re.MULTILINE)

# Collapses any run of whitespace (incl. newlines) to a single space, so a
# multi-line source becomes one flowing paragraph.
_WS_RUN = re.compile(r"\s+")


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


def _copy_flat(src: Path, dst: Path) -> None:
    # Flatten the persona workspace: every file anywhere under home/ lands
    # directly in data/ with no subfolders. Basenames must be unique across the
    # whole tree; a collision would silently drop a file, so fail loudly instead.
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True)
    seen: dict[str, Path] = {}
    for path in sorted(p for p in src.rglob("*") if p.is_file()):
        if path.name in seen:
            raise SystemExit(
                f"cannot flatten {src} into data/: duplicate filename "
                f"{path.name!r} from {seen[path.name]} and {path}"
            )
        seen[path.name] = path
        shutil.copy2(path, dst / path.name)


def build_task_description(meta: dict, prompt_md: str) -> str:
    source = meta.get("task_description") or _TURN_MARKER.sub("", prompt_md)
    return _WS_RUN.sub(" ", source).strip()


def build_task_yaml(meta: dict, system_prompt: str, task_description: str) -> str:
    doc_lines = [
        f"task_type: {meta['task_type']}",
        "task_description: |",
        _indent_block(task_description, 2),
        "system_prompt: |-",
        _indent_block(system_prompt, 2),
        f"platform: {meta.get('platform', DEFAULT_PLATFORM)}",
        "required_apis:",
    ]
    doc_lines += [f"  - {api}" for api in meta["required_apis"]]
    doc_lines.append("distractor_apis:")
    doc_lines += [f"  - {api}" for api in meta["distractor_apis"]]
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


def _validate_meta_schema(meta: dict) -> list[str]:
    errors: list[str] = []
    task_type = meta.get("task_type")
    if task_type is None:
        errors.append(f"task_type is required; pick one of {list(TASK_TYPES)}")
    elif task_type not in TASK_TYPES:
        errors.append(f"task_type {task_type!r} is not a valid type; pick one of {list(TASK_TYPES)}")
    platform = meta.get("platform", DEFAULT_PLATFORM)
    if platform not in PLATFORMS:
        errors.append(f"platform {platform!r} is not valid; pick one of {list(PLATFORMS)}")
    return errors


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

    errors = _validate_meta_schema(meta) + _validate_apis_against_inputs(meta, input_dir, registry)
    if errors:
        return errors

    ratio_warning = _check_ratio(meta)
    if ratio_warning:
        print(f"[assemble] WARNING: {ratio_warning}", file=sys.stderr)

    out_dir.mkdir(parents=True, exist_ok=True)

    system_prompt = build_system_prompt(input_dir, templates_dir, meta)
    probes = count_pytest_probes(work_dir / "test_outputs.py")
    criteria = count_rubric_criteria(work_dir / "rubric.json")
    task_description = build_task_description(meta, (work_dir / "PROMPT.md").read_text())

    (out_dir / "task.yaml").write_text(build_task_yaml(meta, system_prompt, task_description))
    (out_dir / "README.md").write_text(build_readme(meta, work_dir, probes, criteria))

    for fname in ("PROMPT.md", "rubric.json", "test_outputs.py", "test_weights.json", "TRUTH.md"):
        src = work_dir / fname
        if src.is_file():
            shutil.copy2(src, out_dir / fname)

    _copy_persona(input_dir, out_dir / "persona")
    _copy_mock_subset(input_dir / "mock_data", out_dir / "mock_data", meta)
    _copy_flat(input_dir / "home", out_dir / "data")

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

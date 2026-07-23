#!/usr/bin/env python3
"""Stage 4: assemble the native harness bundle from generated + input parts.

Deterministic. Consumes:
  - input_dir/*.md                   (persona team, 7 MDs at root)
  - input_dir/mock_data/<svc>-api/   (persona team, FULL ~101-svc catalog)
  - input_dir/home/                  (persona team, artifact tree = workspace)
  - work_dir/PROMPT.md               (Stage 1)
  - work_dir/task_description.txt    (Stage 1, optional blurb for task.yaml)
  - work_dir/TRUTH.md                (Stage 2)
  - work_dir/rubric.json             (Stage 3)
  - work_dir/test_outputs.py         (Stage 3)
  - work_dir/test_weights.json       (Stage 3)
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

# task.yaml `task_type` controlled vocabulary: the task DOMAIN. Legacy metas that
# still carry an old activity-style task_type fall back to their `domain` key
# (see _resolve_task_type), so existing persona metas keep working unchanged.
TASK_TYPES = (
    "enterprise",
    "professional/prosumer",
    "personal",
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
    return path.read_text(encoding="utf-8").rstrip("\n")


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
    return len(re.findall(r"^\s*def (test_\w+)", test_file.read_text(encoding="utf-8"), re.MULTILINE))


def count_rubric_criteria(rubric_file: Path) -> int:
    if not rubric_file.is_file():
        return 0
    data = json.loads(rubric_file.read_text(encoding="utf-8"))
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


def build_task_description(meta: dict, work_dir: Path) -> str:
    # Priority: operator-authored meta field, then the prompt stage's short
    # task_description.txt blurb, then the legacy full-prompt collapse so
    # bundles generated before the blurb existed still assemble.
    source = meta.get("task_description")
    if not source:
        blurb = work_dir / "task_description.txt"
        if blurb.is_file():
            source = blurb.read_text(encoding="utf-8")
    if not source:
        source = _TURN_MARKER.sub("", (work_dir / "PROMPT.md").read_text(encoding="utf-8"))
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


def _api_stack_section(meta: dict) -> str:
    req = list(meta["required_apis"])
    dis = list(meta["distractor_apis"])
    lines = [
        "## 4. API Stack",
        "",
        f"### 4.1 Required APIs ({len(req)})",
        "",
        "| # | API | Role in this task |",
        "|---|---|---|",
    ]
    for i, api in enumerate(req, 1):
        lines.append(f"| {i} | `{api}` | Load-bearing surface the solve must read or write. |")
    lines += [
        "",
        f"### 4.2 Distractor APIs ({len(dis)}, must end at zero requests)",
        "",
        "| # | API | Why distractor |",
        "|---|---|---|",
    ]
    for i, api in enumerate(dis, 1):
        lines.append(f"| {i} | `{api}` | Plausible but out of scope; audit must show zero requests. |")
    banned = ", ".join(f"`{a}`" for a in sorted(BANNED_APIS))
    lines += ["", f"Banned (not connected): {banned}."]
    return "\n".join(lines)


def _artifacts_section(input_dir: Path) -> str:
    home = input_dir / "home"
    counts: dict[str, int] = {}
    if home.is_dir():
        for path in home.rglob("*"):
            if path.is_file():
                ext = path.suffix.lstrip(".").upper() or "NOEXT"
                counts[ext] = counts.get(ext, 0) + 1
    total = sum(counts.values())
    lines = [
        "## 7. Artifacts Overview",
        "",
        f"{total} pre-staged files in a flat `data/` home directory (persona filesystem "
        "filler). The load-bearing values the agent must reconcile live in the `mock_data/` "
        "service APIs, not in these ambient artifacts.",
        "",
        "| Format | Files |",
        "|---|---|",
    ]
    for ext, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append(f"| {ext} | {n} |")
    if not counts:
        lines.append("| (none) | 0 |")
    dist = ", ".join(f"{ext} x {n}" for ext, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])))
    lines += ["", f"File format distribution: {dist or '(none)'}."]
    return "\n".join(lines)


def _bundle_layout_section(meta: dict) -> str:
    req = list(meta["required_apis"])
    dis = list(meta["distractor_apis"])
    n_folders = len(req) + len(dis)
    lines = [
        "## 9. Bundle Layout",
        "",
        "```",
        "bundle/",
        "+-- data/                                    # pre-staged home-directory artifacts (flat)",
        f"+-- mock_data/                               # {n_folders} API folders ({len(req)} required + {len(dis)} distractor)",
    ]
    for api in req:
        lines.append(f"|   +-- {api}/{' ' * max(1, 34 - len(api))}# required")
    for api in dis:
        lines.append(f"|   +-- {api}/{' ' * max(1, 34 - len(api))}# distractor")
    lines.append("+-- persona/                                 # 7 .md files (sacred, from persona pack)")
    for name in PERSONA_STATIC_ORDER + PERSONA_DYNAMIC_ORDER:
        lines.append(f"|   +-- {name}.md")
    lines += [
        "+-- PROMPT.md                                # single-turn (or multi-turn) persona-voice ask",
        "+-- README.md                                # this file",
        "+-- rubric.json                              # rubric criteria",
        "+-- task.yaml                                # API stack + system_prompt + task_description",
        "+-- test_outputs.py                          # module-level stdlib-only test functions",
        "+-- test_weights.json                        # weights, 1:1 bijection with tests",
        "+-- TRUTH.md                                 # golden truth for prompts and reference trajectory",
        "```",
    ]
    return "\n".join(lines)


def _rubric_tests_section(probes: int, criteria: int, work_dir: Path) -> str:
    weights_path = work_dir / "test_weights.json"
    n_weights = 0
    if weights_path.is_file():
        try:
            data = json.loads(weights_path.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                n_weights = len(data)
        except json.JSONDecodeError:
            n_weights = 0
    bijection = (
        f"{probes} = {n_weights}."
        if probes == n_weights
        else f"MISMATCH: {probes} test functions vs {n_weights} weight keys (must be equal)."
    )
    crit_range = f"R1\u2013R{criteria}" if criteria else "none"
    return "\n".join(
        [
            "## 10. Rubric and Tests",
            "",
            f"- **`rubric.json`** {criteria} criteria ({crit_range}). Channel B, the LLM judge, "
            "grades discovered values, conflict resolution, and provenance.",
            f"- **`test_outputs.py`** {probes} module-level stdlib-only test functions. Channel A "
            "asserts the read happened and the forbidden write did not (audit facts).",
            f"- **`test_weights.json`** one weight key per test function.",
            f"- **Bijection invariant:** every test function has exactly one weight key, and vice "
            f"versa. {bijection}",
            "- **Channel disjointness:** Channel A (pytest) grades audit facts; Channel B (rubric) "
            "grades content and judgment. No workstream is graded twice by the same question.",
            "- **Calibration target:** a no-op or crashed agent fails every read/state probe and "
            "earns nothing from the penalty probes (positive-assertion convention).",
        ]
    )


def _file_index_section() -> str:
    return "\n".join(
        [
            "## 13. File Index",
            "",
            "| Concern | File |",
            "|---|---|",
            "| Prompt voice (verbatim ask text) | `PROMPT.md` |",
            "| API stack lock + system_prompt + task_description | `task.yaml` |",
            "| Persona pack (sacred) | `persona/*.md` |",
            "| Rubric criteria | `rubric.json` |",
            "| Pytest checkers | `test_outputs.py` |",
            "| Weights (1:1 bijection with tests) | `test_weights.json` |",
            "| Mock-data API folders (required + distractor) | `mock_data/` |",
            "| Pre-staged home-directory artifacts | `data/` |",
            "| Golden truth for prompts and reference trajectory | `TRUTH.md` |",
            "| This file | `README.md` |",
        ]
    )


def _strip_trailing_rule(text: str) -> str:
    text = text.rstrip()
    if text.endswith("---"):
        text = text[: -len("---")].rstrip()
    return text


def _splice_before(body: str, marker: str, section: str) -> str:
    # Insert `section` immediately before the line that starts with `marker`.
    # Strip any `---` the author already ended the previous section with so the
    # splice never doubles the horizontal rule. If the marker is absent (author
    # skipped that heading), append the section at the end so a missing marker
    # never drops a mechanical section.
    idx = body.find(marker)
    if idx == -1:
        return f"{_strip_trailing_rule(body)}\n\n---\n\n{section}"
    head, tail = body[:idx], body[idx:]
    return f"{_strip_trailing_rule(head)}\n\n---\n\n{section}\n\n---\n\n{tail.lstrip()}"


def build_readme(
    meta: dict, work_dir: Path, probes: int, criteria: int, input_dir: Path
) -> str:
    # The model authors sections 1,2,3,5,6,8,11,12; assembly splices the five
    # mechanical sections at their numbered positions (contract mirrored in
    # prompt_generation.md "Artifact 3"): section 4 before `## 5.`, section 7
    # before `## 8.`, sections 9+10 before `## 11.`, section 13 at the end.
    body = (work_dir / "README.md").read_text(encoding="utf-8").rstrip()
    body = _splice_before(body, "## 5.", _api_stack_section(meta))
    body = _splice_before(body, "## 8.", _artifacts_section(input_dir))
    section_9_10 = _bundle_layout_section(meta) + "\n\n---\n\n" + _rubric_tests_section(
        probes, criteria, work_dir
    )
    body = _splice_before(body, "## 11.", section_9_10)
    body = f"{body.rstrip()}\n\n---\n\n{_file_index_section()}"
    return f"{body}\n"


REQUIRED_API_FLOOR = 12
BANNED_APIS = frozenset({"dropbox-api", "google-drive-api", "google-contacts-api"})


def _normalize_domain(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    cleaned = value.strip().lower()
    if cleaned in ("professional", "prosumer", "professional/prosumer"):
        return "professional/prosumer"
    return cleaned if cleaned in TASK_TYPES else None


def _resolve_task_type(meta: dict) -> str | None:
    return _normalize_domain(meta.get("task_type")) or _normalize_domain(meta.get("domain"))


def _validate_meta_schema(meta: dict) -> list[str]:
    errors: list[str] = []
    resolved = _resolve_task_type(meta)
    if resolved is None:
        errors.append(
            f"task_type must be the task domain, one of {list(TASK_TYPES)} "
            f"(got task_type={meta.get('task_type')!r}, domain={meta.get('domain')!r})"
        )
    else:
        meta["task_type"] = resolved
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
    meta = yaml.safe_load(meta_path.read_text(encoding="utf-8"))
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
    task_description = build_task_description(meta, work_dir)

    (out_dir / "task.yaml").write_text(build_task_yaml(meta, system_prompt, task_description), encoding="utf-8", newline="")
    (out_dir / "README.md").write_text(build_readme(meta, work_dir, probes, criteria, input_dir), encoding="utf-8", newline="")

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

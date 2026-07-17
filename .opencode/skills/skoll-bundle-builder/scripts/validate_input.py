#!/usr/bin/env python3
"""Stage 0: validate the persona-team input against input-contract.yaml.

Fails loud with a full checklist so a non-engineer team member can see exactly
what is missing before any model call is spent.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib  # type: ignore

import yaml

from build_service_registry import build_registry


class Check:
    def __init__(self, name: str, ok: bool, detail: str = "") -> None:
        self.name = name
        self.ok = ok
        self.detail = detail


def _load_contract(contract_path: Path) -> dict:
    return yaml.safe_load(contract_path.read_text())


def _check_persona(input_dir: Path, spec: dict) -> list[Check]:
    checks: list[Check] = []
    persona_dir = input_dir / spec["dir"]
    for fname in spec["required_files"]:
        fpath = persona_dir / fname
        if not fpath.is_file():
            checks.append(Check(f"{fname} present", False, "missing file"))
            continue
        size = fpath.stat().st_size
        min_bytes = spec["min_bytes_each"]
        checks.append(
            Check(
                f"{fname} >= {min_bytes}B",
                size >= min_bytes,
                f"{size}B",
            )
        )
    if spec.get("memory_marker_required"):
        memory = persona_dir / "MEMORY.md"
        marker = spec["memory_cache_boundary_marker"]
        has_marker = memory.is_file() and marker in memory.read_text()
        checks.append(Check("MEMORY.md cache-boundary marker", has_marker, marker))
    return checks


def _check_home(input_dir: Path, spec: dict) -> list[Check]:
    home_dir = input_dir / spec["dir"]
    if not home_dir.is_dir():
        return [Check(f"{spec['dir']}/ present", False, "missing dir")]
    pattern = "**/*" if spec.get("recurse") else "*"
    files = [f for f in home_dir.glob(pattern) if f.is_file()]
    return [
        Check(
            f"home has >= {spec['min_files']} artifact(s)",
            len(files) >= spec["min_files"],
            f"{len(files)} files",
        )
    ]


def _check_task(input_dir: Path, spec: dict) -> list[Check]:
    task_dir = input_dir / spec["dir"]
    if not task_dir.is_dir():
        return [Check(f"{spec['dir']}/ present", False, "missing dir")]
    checks: list[Check] = []
    for fname in spec["required_files"]:
        fpath = task_dir / fname
        checks.append(Check(f"task/{fname} present", fpath.is_file()))
    for fname in spec.get("optional_files", []):
        fpath = task_dir / fname
        if fpath.is_file():
            checks.append(Check(f"task/{fname} present (optional)", True))
    return checks


def _check_mock_data(input_dir: Path, spec: dict, registry: dict) -> list[Check]:
    checks: list[Check] = []
    mock_dir = input_dir / spec["dir"]
    if not mock_dir.is_dir():
        return [Check(f"{spec['dir']}/ present", False, "missing dir")]
    suffix = spec["subdir_suffix"]
    service_dirs = [d for d in sorted(mock_dir.iterdir()) if d.is_dir()]
    checks.append(
        Check(
            f"mock_data has >= {spec['min_service_dirs']} services",
            len(service_dirs) >= spec["min_service_dirs"],
            f"{len(service_dirs)} found",
        )
    )
    unresolved: list[str] = []
    thin: list[str] = []
    for d in service_dirs:
        if not d.name.endswith(suffix):
            checks.append(Check(f"{d.name} named <svc>{suffix}", False, "bad name"))
            continue
        if spec.get("require_service_in_registry") and d.name not in registry:
            unresolved.append(d.name)
        files = [f for f in d.iterdir() if f.is_file()]
        if len(files) < spec["min_files_per_service"]:
            thin.append(d.name)
    checks.append(
        Check(
            "every service resolves in registry",
            not unresolved,
            ("all resolve" if not unresolved else ", ".join(unresolved[:5])),
        )
    )
    checks.append(
        Check(
            f"every service has >= {spec['min_files_per_service']} file(s)",
            not thin,
            ("all seeded" if not thin else ", ".join(thin[:5])),
        )
    )
    return checks


def validate(input_dir: Path, contract_path: Path, harness_dir: Path) -> list[Check]:
    contract = _load_contract(contract_path)
    registry = build_registry(harness_dir)
    checks: list[Check] = []
    checks += _check_persona(input_dir, contract["persona"])
    checks += _check_home(input_dir, contract["home"])
    checks += _check_task(input_dir, contract["task"])
    checks += _check_mock_data(input_dir, contract["mock_data"], registry)
    return checks


def main(argv: list[str]) -> int:
    if len(argv) < 4:
        print(
            "usage: validate_input.py <input_dir> <contract.yaml> <harness_dir> [--json]",
            file=sys.stderr,
        )
        return 2
    input_dir = Path(argv[1]).expanduser().resolve()
    contract_path = Path(argv[2]).expanduser().resolve()
    harness_dir = Path(argv[3]).expanduser().resolve()
    as_json = "--json" in argv[4:]

    checks = validate(input_dir, contract_path, harness_dir)
    passed = sum(1 for c in checks if c.ok)
    failed = [c for c in checks if not c.ok]

    if as_json:
        print(
            json.dumps(
                {
                    "passed": passed,
                    "failed": len(failed),
                    "checks": [
                        {"name": c.name, "ok": c.ok, "detail": c.detail} for c in checks
                    ],
                },
                indent=2,
            )
        )
    else:
        for c in checks:
            mark = "PASS" if c.ok else "FAIL"
            line = f"[{mark}] {c.name}"
            if c.detail:
                line += f"  ({c.detail})"
            print(line)
        print(f"\n{passed}/{len(checks)} checks passed")
        if failed:
            print(f"{len(failed)} FAILED - fix the above before building", file=sys.stderr)

    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

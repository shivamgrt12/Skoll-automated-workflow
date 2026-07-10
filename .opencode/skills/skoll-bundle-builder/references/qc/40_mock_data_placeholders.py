#!/usr/bin/env python3
"""QC gate: mock-data placeholder leakage check.

Standard gate contract (see SKILL.md): invoked as
``python <gate> <bundle_dir> <harness_dir>`` and returns exit 0 on pass. This
gate is deterministic and reads only the bundle's own ``mock_data/`` JSON, so it
ignores the harness argument. It flags stub/placeholder values left in populated
fields after enrichment (deeper persona-alignment and cross-file consistency are
judged by the model gate ``mock_data_qc/20_mock_data_alignment_qc.md``).
"""

import json
import re
import sys
from pathlib import Path

PLACEHOLDER_RE = re.compile(
    r"^\s*(tbd|todo|lorem ipsum|example@example\.com|test user|placeholder|xxx+|"
    r"your[_ ].+here|<[^>]+>)\s*$",
    re.IGNORECASE,
)


def _rows(data):
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for inner in data.values():
            if isinstance(inner, dict):
                for rows in inner.values():
                    if isinstance(rows, list):
                        return rows
        for rows in data.values():
            if isinstance(rows, list):
                return rows
    return []


def _load(path):
    try:
        return _rows(json.loads(path.read_text()))
    except (json.JSONDecodeError, OSError):
        return []


def _placeholder_findings(service, path, rows):
    out = []
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            continue
        for key, val in row.items():
            if isinstance(val, str) and PLACEHOLDER_RE.match(val):
                out.append(
                    f"[MAJOR] {service}/{path.name}: row {i} field '{key}' "
                    f"holds placeholder {val!r}"
                )
    return out


def main(argv):
    if not argv:
        print("usage: 40_mock_data_consistency.py <bundle_dir> [harness_dir]", file=sys.stderr)
        return 2
    bundle = Path(argv[0]).expanduser().resolve()
    root = bundle / "mock_data"
    if not root.is_dir():
        print(f"no mock_data/ under {bundle}", file=sys.stderr)
        return 0

    findings = []
    for svc_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        service = svc_dir.name
        for path in sorted(svc_dir.glob("*.json")):
            findings.extend(_placeholder_findings(service, path, _load(path)))

    for line in findings:
        print(line)
    print(f"placeholder scan: {len(findings)} finding(s)")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

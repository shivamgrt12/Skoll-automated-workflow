#!/usr/bin/env python3
"""QC gate: mock-data schema validation, conforming to the standard gate contract.

Standard gate contract (see SKILL.md): a ``.py`` gate is invoked as
``python <gate> <bundle_dir> <harness_dir>`` and returns exit 0 on pass.

The real validator (``_mock_data_qc_vendor.py``, a large harness-grade tool
maintained upstream) instead expects ``--env-dir`` (canonical environment/),
``--tasks-dir`` (parent of the task folder) and ``--task`` (task folder name).
This thin wrapper adapts the standard two-positional convention onto those
flags without forking the vendor tool: the bundle's own directory IS the task
folder (it contains ``mock_data/<svc>-api/``), so tasks-dir = bundle_dir.parent
and task = bundle_dir.name; env-dir = harness_dir.
"""

import subprocess
import sys
from pathlib import Path

VENDOR = Path(__file__).with_name("_mock_data_qc_vendor.py")


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: 30_mock_data_qc.py <bundle_dir> <harness_dir>", file=sys.stderr)
        return 2
    bundle_dir = Path(argv[0]).expanduser().resolve()
    harness_dir = Path(argv[1]).expanduser().resolve()
    cmd = [
        sys.executable,
        str(VENDOR),
        "--env-dir",
        str(harness_dir),
        "--tasks-dir",
        str(bundle_dir.parent),
        "--task",
        bundle_dir.name,
    ]
    return subprocess.run(cmd, text=True).returncode


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

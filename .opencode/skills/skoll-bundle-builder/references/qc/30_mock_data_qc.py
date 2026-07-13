#!/usr/bin/env python3
"""QC gate: mock-data schema validation, conforming to the standard gate contract.

Standard gate contract (see SKILL.md): a ``.py`` gate is invoked as
``python <gate> <bundle_dir> <harness_dir>`` and returns exit 0 on pass.

The validator (``_mock_overlay_validator/validate.py``) audits every overlay
seed under ``<bundle_dir>/mock_data/<svc>-api/`` against a bundled canonical
example snapshot in ``_mock_overlay_validator/examples/<svc>-api/`` (one
reference file per registered table/document, matched by filename stem). It is
stdlib-only and self-contained, so it does NOT read the live ``environment/``
harness dir at run time -- the example snapshot already encodes the schema the
harness loader expects. That makes ``<harness_dir>`` (argv[2]) unused here; we
accept it only to satisfy the two-positional gate convention.

The validator auto-classifies the path it is handed. The bundle's own dir IS
the task folder (it contains ``mock_data/<svc>-api/``), so we pass the bundle
dir directly and let ``validate.py`` walk its ``mock_data/`` child. Its exit
code already matches the gate contract: 0 = clean (warnings allowed), 1 = one
or more schema errors, 2 = bad usage.
"""

import subprocess
import sys
from pathlib import Path

VALIDATOR = Path(__file__).with_name("_mock_overlay_validator") / "validate.py"


def main(argv: list[str]) -> int:
    if len(argv) < 1:
        print("usage: 30_mock_data_qc.py <bundle_dir> [harness_dir]", file=sys.stderr)
        return 2
    bundle_dir = Path(argv[0]).expanduser().resolve()
    # argv[1] (harness_dir) is intentionally ignored: the validator ships its
    # own canonical example snapshot and never consults the live environment.
    cmd = [sys.executable, str(VALIDATOR), str(bundle_dir)]
    return subprocess.run(cmd, text=True).returncode


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

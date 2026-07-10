#!/usr/bin/env python3
"""QC gate wrapper: scan a bundle's data/ tree for AI-generated / stock images.

Gate contract (see cli/skoll_bundle.py _run_qc_gate): invoked as
    python <gate> <bundle_dir> <harness_dir>
argv[1] = bundle dir, argv[2] = harness dir (ignored here). Exit 0 = pass.

The heavy detector lives in the discovery-excluded _check_ai_images_vendor.py
(leading underscore keeps it out of _discover_qc_gates). We point it at
<bundle_dir>/data, which is where assemble.py stages the persona workspace
artifacts. Missing Pillow makes the vendor exit 2 (ERROR); we surface that as a
non-pass so the operator installs `pip install Pillow` rather than silently
skipping the check.
"""
import sys
from pathlib import Path

import importlib.util

_VENDOR = Path(__file__).with_name("_check_ai_images_vendor.py")


def _load_vendor():
    spec = importlib.util.spec_from_file_location("_check_ai_images_vendor", _VENDOR)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    if len(sys.argv) < 2:
        print("ERROR: expected <bundle_dir> as argv[1]", file=sys.stderr)
        return 2
    bundle_dir = Path(sys.argv[1])
    data_dir = bundle_dir / "data"
    if not data_dir.exists():
        print(f"ERROR: bundle data dir not found: {data_dir}", file=sys.stderr)
        return 2
    vendor = _load_vendor()
    return vendor.main([str(data_dir)])


if __name__ == "__main__":
    sys.exit(main())

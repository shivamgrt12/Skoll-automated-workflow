#!/usr/bin/env python3
"""Prompt-QC gate wrapper: run the vendor deterministic prompt checklist.

Prompt-QC .py gates are invoked as `python <gate> <work_dir>`; argv[1] is the
stage work dir holding the generated PROMPT.md. The vendor checker
(_prompt_qc_vendor.py, discovery-excluded by its leading underscore) parses its
own argv, so we drive it as a subprocess in single-file mode against
<work_dir>/PROMPT.md. Exit 0 = pass, 1 = FAIL, 2 = wrapper/vendor error.
"""
import subprocess
import sys
from pathlib import Path

_VENDOR = Path(__file__).with_name("_prompt_qc_vendor.py")


def main() -> int:
    if len(sys.argv) < 2:
        print("ERROR: expected <work_dir> as argv[1]", file=sys.stderr)
        return 2
    prompt_file = Path(sys.argv[1]) / "PROMPT.md"
    if not prompt_file.exists():
        print(f"ERROR: PROMPT.md not found: {prompt_file}", file=sys.stderr)
        return 2
    result = subprocess.run(
        [sys.executable, str(_VENDOR), "--file", str(prompt_file), "--verbose"],
        text=True,
    )
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())

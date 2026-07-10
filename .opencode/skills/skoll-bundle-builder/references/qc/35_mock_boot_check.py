"""QC gate: mock-data boot simulation.

Usage: python 35_mock_boot_check.py <bundle_dir> <harness_dir>

Loads the bundle's mock_data seed overlays through the harness's own
_mutable_store loader (the local SKOLL_GK/Environment_SN_Harness copy) exactly
the way the harness boots each mock service. Fails when any selected service
would boot broken: loader exceptions (e.g. a string id like 'ACT-001' in an
int-typed column -> the table is served EMPTY), missing primary keys, or
primary-key collisions. Exit 0 = pass, 1 = fail, 2 = usage error.

Internal single-service mode (used for subprocess isolation):
    python 35_mock_boot_check.py --single <staged_service_dir>
"""

import importlib.util
import io
import logging
import re
import shutil
import subprocess
import sys
import tempfile
from contextlib import redirect_stderr
from pathlib import Path

API_LIST_KEYS = ("required_apis", "distractor_apis")


def _selected_services(bundle: Path) -> list[str]:
    services: list[str] = []
    task_yaml = bundle / "task.yaml"
    if task_yaml.is_file():
        text = task_yaml.read_text(encoding="utf-8", errors="replace")
        current_key = None
        for line in text.splitlines():
            key_match = re.match(r"^(\w+):", line)
            if key_match:
                current_key = key_match.group(1)
                continue
            if current_key in API_LIST_KEYS:
                item = re.match(r"^\s*-\s*([\w-]+)\s*$", line)
                if item:
                    services.append(item.group(1))
    if not services:
        mock_root = bundle / "mock_data"
        if mock_root.is_dir():
            services = [d.name for d in sorted(mock_root.iterdir()) if d.is_dir()]
    return sorted(set(services))


def _stage_service(svc: str, bundle: Path, harness: Path, tmp_root: Path) -> Path | None:
    harness_svc = harness / svc
    bundle_svc = bundle / "mock_data" / svc
    if not harness_svc.is_dir():
        return None
    staged = tmp_root / svc
    shutil.copytree(harness_svc, staged)
    if bundle_svc.is_dir():
        shutil.copytree(bundle_svc, staged, dirs_exist_ok=True)
    store_src = harness / "_mutable_store.py"
    if store_src.is_file():
        shutil.copy2(store_src, tmp_root / "_mutable_store.py")
    return staged


def _run_single(staged_dir: Path) -> int:
    svc = staged_dir.name
    data_py = staged_dir / f"{svc.replace('-', '_')}_data.py"
    if not data_py.is_file():
        candidates = sorted(staged_dir.glob("*_data.py"))
        if not candidates:
            print(f"SKIP {svc}: no *_data.py loader module")
            return 0
        data_py = candidates[0]

    sys.path.insert(0, str(staged_dir.parent))
    sys.path.insert(0, str(staged_dir))

    records: list[logging.LogRecord] = []

    class _Capture(logging.Handler):
        def emit(self, record: logging.LogRecord) -> None:
            records.append(record)

    handler = _Capture(level=logging.WARNING)
    logging.getLogger().addHandler(handler)
    logging.getLogger().setLevel(logging.WARNING)

    stderr_buf = io.StringIO()
    findings: list[str] = []
    try:
        with redirect_stderr(stderr_buf):
            spec = importlib.util.spec_from_file_location(data_py.stem, data_py)
            module = importlib.util.module_from_spec(spec)
            sys.modules[data_py.stem] = module
            spec.loader.exec_module(module)

            import _mutable_store

            for name, store in list(getattr(_mutable_store, "_STORES", {}).items()):
                try:
                    store.eager_load()
                except Exception as exc:
                    findings.append(f"{svc}: store '{name}' eager_load raised {type(exc).__name__}: {exc}")
    except ModuleNotFoundError as exc:
        print(f"SKIP {svc}: missing third-party module ({exc.name})")
        return 0
    except Exception as exc:
        findings.append(f"{svc}: loader module import failed {type(exc).__name__}: {exc}")

    for record in records:
        msg = record.getMessage()
        if record.levelno >= logging.ERROR:
            findings.append(f"{svc}: loader error -> {msg}")
        elif "missing primary key" in msg:
            findings.append(f"{svc}: missing primary key -> {msg}")

    for line in stderr_buf.getvalue().splitlines():
        if "[mutable_store] WARN" in line:
            findings.append(f"{svc}: {line.strip()}")

    if findings:
        for finding in findings:
            print(f"FINDING {finding}")
        return 1
    print(f"OK {svc}")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) == 2 and argv[0] == "--single":
        return _run_single(Path(argv[1]).resolve())

    if len(argv) != 2:
        print("usage: 35_mock_boot_check.py <bundle_dir> <harness_dir>", file=sys.stderr)
        return 2

    bundle = Path(argv[0]).resolve()
    harness = Path(argv[1]).resolve()
    if not bundle.is_dir():
        print(f"35_mock_boot_check: bundle dir not found: {bundle}", file=sys.stderr)
        return 2
    if not harness.is_dir():
        print(f"35_mock_boot_check: harness dir not found: {harness} (skipping)", )
        return 0

    services = _selected_services(bundle)
    if not services:
        print("35_mock_boot_check: no selected services found; nothing to check PASS")
        return 0

    failures: list[str] = []
    checked = 0
    with tempfile.TemporaryDirectory(prefix="mock_boot_") as tmp:
        tmp_root = Path(tmp)
        for svc in services:
            staged = _stage_service(svc, bundle, harness, tmp_root)
            if staged is None:
                print(f"SKIP {svc}: not present in harness environment")
                continue
            checked += 1
            proc = subprocess.run(
                [sys.executable, str(Path(__file__).resolve()), "--single", str(staged)],
                capture_output=True,
                text=True,
            )
            if proc.stdout.strip():
                print(proc.stdout.strip())
            if proc.returncode != 0:
                detail = (proc.stdout + proc.stderr).strip()
                failures.append(detail or f"{svc}: boot check failed (exit {proc.returncode})")

    if failures:
        print("35_mock_boot_check: FAIL - these services would boot broken on the harness:", file=sys.stderr)
        for failure in failures:
            print(failure, file=sys.stderr)
        print(
            "Fix the bundle's mock_data seeds so every id matches the column type the "
            "service's *_data.py loader declares (strict_int columns need plain integer "
            "ids) and every row has a unique primary key.",
            file=sys.stderr,
        )
        return 1

    print(f"35_mock_boot_check: {checked} service(s) boot cleanly with bundle seeds PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

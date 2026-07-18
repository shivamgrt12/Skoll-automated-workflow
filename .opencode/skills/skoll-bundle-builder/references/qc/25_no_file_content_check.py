#!/usr/bin/env python3
"""Pytest QC gate (mechanical): no file-content assertions, no hardcoded paths.

Enforces two client rules deterministically so the LLM judge cannot rationalise
them away:

  R2 (no hardcoded output filenames/paths): a probe may only name a deliverable
      path that PROMPT.md literally requests. Path-discovery helpers and constants
      (glob over a workspace, DELIVERABLE / _WORKSPACE / _DATA_DIRS,
      _find_deliverable / _read_deliverable) are never allowed. A data VALUE
      (an id, amount, date, name) is NOT a path and is never flagged.

  R3 (tests must not check file content): pytest verifies behaviour (an API call
      happened), outcome (API state via re-GET / response_body, or a file merely
      EXISTS), and negative probes. It must NEVER open a deliverable the agent
      wrote and grade its content. Content correctness belongs to rubric.json.

Both rules reduce to one mechanical line: a value that arrives over HTTP from the
mock server (urlopen / api_get / api_post / _get / _post / _request, then
resp.read()) is API STATE and fully assertable; a value obtained by opening a
file the agent wrote (open(), .read_text(), csv.reader, json.load(open(...)),
ElementTree/zipfile/openpyxl on a written path, or a home-grown read_file()) is
FILE CONTENT and forbidden beyond bare existence (os.path.exists / file_exists on
a PROMPT.md-named path).

Convention: argv[1] is the work directory holding test_outputs.py (or a direct
path to test_outputs.py). Exit 0 = clean (pass); exit 1 = at least one forbidden
file-content read or hardcoded path-discovery construct was found (fail). stderr
names every offending line so the auto-fix pass can delete/rewrite it. Severity
is BLOCK in the manifest.

This gate is deliberately conservative: it only flags constructs that read or
discover a written file. It never flags HTTP reads (urlopen(...).read()),
os.path.exists / file_exists existence checks, or literal data values. When in
doubt it stays silent, leaving nuance to the LLM auditor (Defect 20).
"""
from __future__ import annotations

import ast
import sys
from pathlib import Path

# Home-grown / stdlib helpers that read a written file's CONTENT.
FILE_READ_FUNCS = {"read_file", "read_text", "load_workbook"}
# Attribute-call readers, e.g. path.read_text(), obj.read_text().
FILE_READ_ATTRS = {"read_text", "load_workbook"}
# csv readers that consume an opened file object.
CSV_READERS = {"reader", "DictReader"}
# Path-discovery helpers that never have a place in a compliant suite.
DISCOVERY_FUNCS = {"_find_deliverable", "_read_deliverable", "glob", "iglob"}
# Hardcoded path/discovery constant names (a data VALUE is never named this way).
PATH_CONSTANTS = {"DELIVERABLE", "DELIVERABLES", "_WORKSPACE", "WORKSPACE",
                  "_DATA_DIRS", "DATA_DIRS", "_OUTPUT_DIR", "OUTPUT_DIR"}
# Bare-existence primitives that are always allowed.
EXISTENCE_FUNCS = {"file_exists", "exists", "isfile", "isdir"}
# Output-folder path prefixes the client rules ban outright (a deliverable path
# is only legitimate when PROMPT.md literally requests it; these generic sink
# folders never are). Matched against string-literal path values.
BANNED_PATH_PREFIXES = ("deliverables/", "output/", "outputs/", "results/",
                        "reports/", "submissions/", "./deliverables/",
                        "./output/", "./results/", "./reports/",
                        "./submissions/")


def _call_name(node: ast.Call) -> str:
    func = node.func
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        return func.attr
    return ""


def _attr_chain(node: ast.expr) -> str:
    parts: list[str] = []
    cur: ast.expr | None = node
    while isinstance(cur, ast.Attribute):
        parts.append(cur.attr)
        cur = cur.value
    if isinstance(cur, ast.Name):
        parts.append(cur.id)
    return ".".join(reversed(parts))


def _is_open_builtin(node: ast.Call) -> bool:
    """True for the builtin open(...) (file open), not urlopen / *.open()."""
    func = node.func
    if isinstance(func, ast.Name) and func.id == "open":
        return True
    # os.open / io.open are still file opens.
    if isinstance(func, ast.Attribute) and func.attr == "open":
        base = _attr_chain(func.value)
        if base in ("os", "io"):
            return True
    return False


def _json_load_over_open(node: ast.Call) -> bool:
    """True for json.load(open(...)) — parsing a file's content."""
    func = node.func
    if not (isinstance(func, ast.Attribute) and func.attr == "load"
            and _attr_chain(func.value) == "json"):
        return False
    for arg in node.args:
        if isinstance(arg, ast.Call) and _is_open_builtin(arg):
            return True
    return False


def _csv_reader(node: ast.Call) -> bool:
    func = node.func
    return (isinstance(func, ast.Attribute) and func.attr in CSV_READERS
            and _attr_chain(func.value) == "csv")


def _etree_parse(node: ast.Call) -> bool:
    """xml.etree.ElementTree.parse(...) on a written file."""
    func = node.func
    if isinstance(func, ast.Attribute) and func.attr == "parse":
        chain = _attr_chain(func.value)
        if "ElementTree" in chain or chain.endswith("ET"):
            return True
    return False


def _zipfile_open(node: ast.Call) -> bool:
    func = node.func
    if isinstance(func, ast.Attribute) and func.attr == "ZipFile":
        return _attr_chain(func.value) == "zipfile"
    if isinstance(func, ast.Name) and func.id == "ZipFile":
        return True
    return False


def _enclosing_test(lineno_map: list[tuple[int, str]], lineno: int) -> str:
    """Name of the test_* function that lexically encloses the given line."""
    current = "<module>"
    for start, name in lineno_map:
        if start <= lineno:
            current = name
        else:
            break
    return current


def main() -> int:
    if len(sys.argv) < 2:
        print("25_no_file_content_check: usage: 25_no_file_content_check.py "
              "<work_dir|test_outputs.py>", file=sys.stderr)
        return 1

    target = Path(sys.argv[1])
    tests_path = target / "test_outputs.py" if target.is_dir() else target
    if not tests_path.is_file():
        print(f"25_no_file_content_check: test_outputs.py not found at "
              f"{tests_path}", file=sys.stderr)
        return 1

    source = tests_path.read_text(encoding="utf-8", errors="replace")
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        print(f"25_no_file_content_check: test_outputs.py does not parse: {exc}",
              file=sys.stderr)
        return 1

    # Map top-level function start lines -> name so we can attribute a finding
    # to the enclosing test (helpers like read_file report at their def too).
    fn_starts: list[tuple[int, str]] = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            fn_starts.append((node.lineno, node.name))
    fn_starts.sort()

    findings: list[tuple[int, str]] = []

    def flag(lineno: int, reason: str) -> None:
        where = _enclosing_test(fn_starts, lineno)
        findings.append((lineno, f"{where} (line {lineno}): {reason}"))

    for node in ast.walk(tree):
        # 1) Import of a parsing library used only to read written files.
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name in ("openpyxl", "pandas"):
                    flag(node.lineno, f"imports {alias.name} (file-content "
                         "parsing library; grade content in rubric.json instead)")
        # 2) Builtin open() -> reading a written file's content.
        if isinstance(node, ast.Call):
            if _is_open_builtin(node):
                flag(node.lineno, "open() reads a written file's content; use an "
                     "API re-GET or grade content in rubric.json")
            elif _json_load_over_open(node):
                flag(node.lineno, "json.load(open(...)) parses a written file's "
                     "content; assert on the API response instead")
            elif _csv_reader(node):
                flag(node.lineno, "csv reader parses a written file's content; "
                     "assert on the API response instead")
            elif _etree_parse(node):
                flag(node.lineno, "ElementTree.parse reads a written file's "
                     "content; assert on the API response instead")
            elif _zipfile_open(node):
                flag(node.lineno, "zipfile opens a written file's content; "
                     "assert on the API response instead")
            else:
                name = _call_name(node)
                if name in FILE_READ_FUNCS:
                    flag(node.lineno, f"{name}(...) reads a written file's "
                         "content; content correctness belongs to rubric.json")
                elif name in DISCOVERY_FUNCS:
                    flag(node.lineno, f"{name}(...) discovers a deliverable path; "
                         "only PROMPT.md-named paths are allowed (no discovery)")
        # 3) Attribute call *.read_text() etc. (path.read_text()).
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr in FILE_READ_ATTRS:
                flag(node.lineno, f".{node.func.attr}() reads a written file's "
                     "content; grade content in rubric.json instead")
        # 4) Definition of a home-grown file-content reader (read_file()).
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name in FILE_READ_FUNCS:
                flag(node.lineno, f"defines {node.name}() (a file-content reader); "
                     "remove it — pytest must not read written files")
        # 5) Hardcoded path/discovery constant assignment.
        if isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name) and tgt.id in PATH_CONSTANTS:
                    flag(node.lineno, f"{tgt.id} hardcodes a deliverable path/dir; "
                         "only PROMPT.md-named paths are allowed")
        # 6) String literal pointing at a banned generic output folder.
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            low = node.value.lstrip().lower()
            if low.startswith(BANNED_PATH_PREFIXES):
                flag(node.lineno, f"string literal {node.value!r} targets a generic "
                     "output folder banned by Rule 2; use only a path PROMPT.md "
                     "names (a data value is fine, a sink-folder path is not)")

    if findings:
        findings.sort()
        # De-duplicate identical (line, message) pairs.
        seen: set[tuple[int, str]] = set()
        print("25_no_file_content_check: FAIL - pytest reads or discovers written "
              "files (Rules 2 & 3: tests assert API state + bare existence only; "
              "content correctness belongs to rubric.json):", file=sys.stderr)
        for lineno, msg in findings:
            key = (lineno, msg)
            if key in seen:
                continue
            seen.add(key)
            print(f"  - {msg}", file=sys.stderr)
        return 1

    print("25_no_file_content_check: no file-content reads or hardcoded "
          "deliverable paths found PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

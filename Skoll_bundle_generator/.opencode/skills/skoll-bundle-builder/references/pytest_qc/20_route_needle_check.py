#!/usr/bin/env python3
"""Pytest QC gate (mechanical): route-needle satisfiability check.

Generated probes in test_outputs.py verify agent behaviour by grepping the
mock services' audit logs for URL substrings ("needles"), or by calling mock
endpoints directly. If a needle can never appear in any URL the mock server
actually serves (e.g. "/issues" when the Jira mock only routes
/rest/api/3/issue/{issue_key}), the probe is structurally impossible: even a
perfect agent fails it. This gate statically proves every structural needle
and every directly-called endpoint against the real route table parsed from
the harness environment copy (SKOLL_GK/Environment_SN_Harness/<svc>-api/server.py).

Convention: argv[1] is the work directory holding test_outputs.py (or a direct
path to test_outputs.py). Optional argv[2] is the input bundle directory (or
its mock_data directory) used to resolve keyword needles against seed values.
Exit 0 = every structural needle / direct endpoint is satisfiable (pass);
exit 1 = at least one probe is impossible against the real routes (fail).
Severity is BLOCK in the manifest, so a fail stops the pipeline; the failure
report names each broken test, its needle, and the service's real routes so
the auto-fix pass can rewrite the probe.

Keyword needles (lowercase words matched against path values, which may
legitimately match seed-derived path parameters like Airtable table names)
are only WARNED about when they cannot be confirmed - they never block.

Harness environment resolution order:
  1. $SKOLL_HARNESS_DIR (must contain <svc>-api dirs with server.py)
  2. nearest ancestor of this gate file containing SKOLL_GK/Environment_SN_Harness
  3. $CWD/SKOLL_GK/Environment_SN_Harness
"""
from __future__ import annotations

import ast
import os
import re
import sys
from pathlib import Path

PARAM_SENTINEL = "\x00"
AUDIT_ENDPOINT_PREFIXES = ("/audit", "/health", "/admin")
HTTP_DECORATOR_METHODS = {"get", "post", "put", "patch", "delete"}


# --------------------------------------------------------------------------
# Harness environment discovery
# --------------------------------------------------------------------------

def _find_harness_dir() -> Path | None:
    env = os.environ.get("SKOLL_HARNESS_DIR")
    if env:
        p = Path(env)
        if p.is_dir():
            return p
    here = Path(__file__).resolve()
    for parent in here.parents:
        candidate = parent / "SKOLL_GK" / "Environment_SN_Harness"
        if candidate.is_dir():
            return candidate
    candidate = Path.cwd() / "SKOLL_GK" / "Environment_SN_Harness"
    if candidate.is_dir():
        return candidate
    return None


# --------------------------------------------------------------------------
# service.toml -> env var mapping (stdlib-only, regex parse to avoid deps)
# --------------------------------------------------------------------------

_TOML_KV = re.compile(r'^\s*(\w+)\s*=\s*"([^"]*)"\s*$', re.MULTILINE)


def _load_env_var_map(harness: Path) -> dict[str, str]:
    """Map ENV_VAR_NAME (e.g. JIRA_API_URL) -> service dir name (jira-api)."""
    mapping: dict[str, str] = {}
    for svc_dir in sorted(harness.iterdir()):
        if not svc_dir.is_dir() or not svc_dir.name.endswith("-api"):
            continue
        toml_path = svc_dir / "service.toml"
        if not toml_path.is_file():
            continue
        kv = dict(_TOML_KV.findall(toml_path.read_text(encoding="utf-8", errors="replace")))
        env_var = kv.get("env_var_name")
        if env_var:
            mapping[env_var] = svc_dir.name
    return mapping


# --------------------------------------------------------------------------
# Route extraction from server.py (handles literal, NAME + "str", f-string)
# --------------------------------------------------------------------------

def _module_str_constants(tree: ast.Module) -> dict[str, str]:
    consts: dict[str, str] = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Constant) \
                and isinstance(node.value.value, str):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    consts[target.id] = node.value.value
    return consts


def _resolve_path_expr(node: ast.expr, consts: dict[str, str]) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.Name):
        return consts.get(node.id)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left = _resolve_path_expr(node.left, consts)
        right = _resolve_path_expr(node.right, consts)
        if left is not None and right is not None:
            return left + right
        return None
    if isinstance(node, ast.JoinedStr):
        parts: list[str] = []
        for value in node.values:
            if isinstance(value, ast.Constant) and isinstance(value.value, str):
                parts.append(value.value)
            elif isinstance(value, ast.FormattedValue):
                resolved = _resolve_path_expr(value.value, consts)
                if resolved is None:
                    # Unknown interpolation: treat like a path parameter.
                    parts.append("{param}")
                else:
                    parts.append(resolved)
            else:
                return None
        return "".join(parts)
    return None


def _service_routes(svc_dir: Path) -> list[tuple[str, str]]:
    """Return [(METHOD, path), ...] declared in the service's server.py."""
    server = svc_dir / "server.py"
    if not server.is_file():
        return []
    try:
        tree = ast.parse(server.read_text(encoding="utf-8", errors="replace"))
    except SyntaxError:
        return []
    consts = _module_str_constants(tree)
    routes: list[tuple[str, str]] = []
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        for dec in node.decorator_list:
            if not (isinstance(dec, ast.Call) and isinstance(dec.func, ast.Attribute)):
                continue
            method = dec.func.attr.lower()
            if method not in HTTP_DECORATOR_METHODS or not dec.args:
                continue
            path = _resolve_path_expr(dec.args[0], consts)
            if path:
                routes.append((method.upper(), path))
    return routes


_PARAM_SEG = re.compile(r"\{[^/}]*\}")


def _route_match_text(path: str) -> str:
    """Replace {param} segments with a sentinel so needles cannot bridge them."""
    return _PARAM_SEG.sub(PARAM_SENTINEL, path)


# --------------------------------------------------------------------------
# test_outputs.py analysis
# --------------------------------------------------------------------------

class Needle:
    def __init__(self, text: str, lowered: bool, or_group: int) -> None:
        self.text = text
        self.lowered = lowered
        self.or_group = or_group

    @property
    def structural(self) -> bool:
        return self.text.startswith("/")


def _subtree_mentions_path(node: ast.expr) -> bool:
    for sub in ast.walk(node):
        if isinstance(sub, ast.Constant) and sub.value == "path":
            return True
        if isinstance(sub, ast.Attribute) and sub.attr == "path":
            return True
    return False


def _subtree_lowered(node: ast.expr) -> bool:
    for sub in ast.walk(node):
        if isinstance(sub, ast.Attribute) and sub.attr == "lower":
            return True
    return False


def _fn_reads_audit(fn: ast.FunctionDef) -> bool:
    for sub in ast.walk(fn):
        if isinstance(sub, ast.Constant) and isinstance(sub.value, str) \
                and sub.value.startswith("/audit"):
            return True
    return False


def _collect_needles(fn: ast.FunctionDef) -> list[Needle]:
    needles: list[Needle] = []
    group_counter = 0
    seen_compares: set[int] = set()
    reads_audit = _fn_reads_audit(fn)

    def _is_path_compare(sub: ast.Compare) -> bool:
        if _subtree_mentions_path(sub.comparators[0]):
            return True
        # Audit-summary key form: '/records' in k, where k iterates the
        # "METHOD /path" keys of /audit/summary. Only slash-prefixed needles
        # against a bare name qualify, so response-body checks like
        # 'henderson' in json.dumps(d) are never captured.
        return (reads_audit
                and sub.left.value.startswith("/")
                and isinstance(sub.comparators[0], ast.Name))

    def compares_of(node: ast.expr) -> list[ast.Compare]:
        found: list[ast.Compare] = []
        for sub in ast.walk(node):
            if isinstance(sub, ast.Compare) and len(sub.ops) == 1 \
                    and isinstance(sub.ops[0], ast.In) \
                    and isinstance(sub.left, ast.Constant) \
                    and isinstance(sub.left.value, str) \
                    and _is_path_compare(sub):
                found.append(sub)
        return found

    for node in ast.walk(fn):
        if isinstance(node, ast.BoolOp) and isinstance(node.op, ast.Or):
            group = compares_of(node)
            fresh = [c for c in group if id(c) not in seen_compares]
            if fresh:
                group_counter += 1
                for cmp_node in fresh:
                    seen_compares.add(id(cmp_node))
                    needles.append(Needle(
                        cmp_node.left.value,
                        _subtree_lowered(cmp_node.comparators[0]),
                        group_counter,
                    ))
    # Standalone (non-OR) compares each form their own group.
    for node in ast.walk(fn):
        if isinstance(node, ast.Compare) and id(node) not in seen_compares:
            for cmp_node in compares_of(node):
                if id(cmp_node) in seen_compares:
                    continue
                seen_compares.add(id(cmp_node))
                group_counter += 1
                needles.append(Needle(
                    cmp_node.left.value,
                    _subtree_lowered(cmp_node.comparators[0]),
                    group_counter,
                ))
    return needles


def _fn_api_url_names(fn: ast.FunctionDef) -> list[str]:
    names: list[str] = []
    for node in ast.walk(fn):
        if isinstance(node, ast.Name) and node.id.endswith("_API_URL") and node.id not in names:
            names.append(node.id)
    return names


def _direct_endpoints(fn: ast.FunctionDef) -> list[tuple[str, str, str]]:
    """Return [(api_url_name, method, endpoint)] for direct mock calls."""
    calls: list[tuple[str, str, str]] = []
    for node in ast.walk(fn):
        if not isinstance(node, ast.Call):
            continue
        func_name = ""
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
        elif isinstance(node.func, ast.Attribute):
            func_name = node.func.attr
        method = {"api_get": "GET", "api_post": "POST", "_get": "GET",
                  "_post": "POST"}.get(func_name)
        if method is None and func_name == "_request" and node.args \
                and isinstance(node.args[0], ast.Constant):
            method = str(node.args[0].value).upper()
        if method is None:
            continue
        api_name = None
        endpoint = None
        for arg in node.args:
            if isinstance(arg, ast.Name) and arg.id.endswith("_API_URL"):
                api_name = arg.id
            elif isinstance(arg, ast.Constant) and isinstance(arg.value, str) \
                    and arg.value.startswith("/"):
                endpoint = arg.value
        if api_name and endpoint:
            path = endpoint.split("?", 1)[0]
            if not path.startswith(AUDIT_ENDPOINT_PREFIXES):
                calls.append((api_name, method, path))
    return calls


# --------------------------------------------------------------------------
# Satisfiability checks
# --------------------------------------------------------------------------

def _needle_satisfiable(needle: Needle, routes: list[tuple[str, str]]) -> bool:
    text = needle.text.lower() if needle.lowered else needle.text
    for _method, path in routes:
        route_text = _route_match_text(path)
        if needle.lowered:
            route_text = route_text.lower()
        if text in route_text:
            return True
    return False


def _endpoint_matches(method: str, path: str, routes: list[tuple[str, str]]) -> bool:
    segs = [s for s in path.split("/") if s != ""]
    for r_method, r_path in routes:
        if r_method != method:
            continue
        r_segs = [s for s in r_path.split("/") if s != ""]
        if len(r_segs) != len(segs):
            continue
        ok = True
        for r_seg, seg in zip(r_segs, segs):
            if r_seg.startswith("{") and r_seg.endswith("}"):
                continue
            if r_seg != seg:
                ok = False
                break
        if ok:
            return True
    return False


def _seed_values_blob(input_dir: Path, services: list[str]) -> str:
    """Lowercased blob of seed file contents + filenames for keyword lookup."""
    mock_root = input_dir / "mock_data" if (input_dir / "mock_data").is_dir() else input_dir
    chunks: list[str] = []
    for svc in services:
        svc_dir = mock_root / svc
        if not svc_dir.is_dir():
            continue
        for f in svc_dir.rglob("*"):
            if f.is_file() and f.suffix.lower() in (".json", ".csv", ".toml", ".txt"):
                chunks.append(f.name.lower())
                try:
                    chunks.append(f.read_text(encoding="utf-8", errors="replace").lower())
                except OSError:
                    pass
    return "\n".join(chunks)


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main() -> int:
    if len(sys.argv) < 2:
        print("20_route_needle_check: usage: 20_route_needle_check.py <work_dir> "
              "[input_bundle_dir]", file=sys.stderr)
        return 1

    target = Path(sys.argv[1])
    tests_path = target / "test_outputs.py" if target.is_dir() else target
    if not tests_path.is_file():
        print(f"20_route_needle_check: test_outputs.py not found at {tests_path}",
              file=sys.stderr)
        return 1

    harness = _find_harness_dir()
    if harness is None:
        # Cannot verify without the harness copy; warn but do not block.
        print("20_route_needle_check: WARN harness environment "
              "(SKOLL_GK/Environment_SN_Harness) not found; needle check skipped")
        return 0

    env_map = _load_env_var_map(harness)
    try:
        tree = ast.parse(tests_path.read_text(encoding="utf-8", errors="replace"))
    except SyntaxError as exc:
        print(f"20_route_needle_check: test_outputs.py does not parse: {exc}",
              file=sys.stderr)
        return 1

    routes_cache: dict[str, list[tuple[str, str]]] = {}

    def routes_for(services: list[str]) -> list[tuple[str, str]]:
        combined: list[tuple[str, str]] = []
        for svc in services:
            if svc not in routes_cache:
                routes_cache[svc] = _service_routes(harness / svc)
            combined.extend(routes_cache[svc])
        return combined

    input_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else None

    failures: list[str] = []
    warnings: list[str] = []
    checked_needles = 0
    checked_endpoints = 0

    for node in tree.body:
        if not isinstance(node, ast.FunctionDef) or not node.name.startswith("test_"):
            continue
        api_names = _fn_api_url_names(node)
        services = [env_map[n] for n in api_names if n in env_map]
        if not services:
            continue
        routes = routes_for(services)
        svc_label = ", ".join(services)

        # 1) Structural / keyword needles from audit-path comparisons.
        needles = _collect_needles(node)
        groups: dict[int, list[Needle]] = {}
        for needle in needles:
            groups.setdefault(needle.or_group, []).append(needle)
        for group_needles in groups.values():
            structural = [n for n in group_needles if n.structural]
            keywords = [n for n in group_needles if not n.structural]
            if structural:
                checked_needles += len(structural)
                if not any(_needle_satisfiable(n, routes) for n in structural) \
                        and not keywords:
                    needle_list = ", ".join(repr(n.text) for n in structural)
                    route_list = "; ".join(
                        f"{m} {p}" for m, p in routes) or "(no routes found)"
                    failures.append(
                        f"{node.name}: path needle(s) {needle_list} can never appear "
                        f"in any URL served by [{svc_label}]. Real routes: {route_list}"
                    )
            if keywords:
                checked_needles += len(keywords)
                unresolved = []
                for kw in keywords:
                    if _needle_satisfiable(kw, routes):
                        continue
                    if kw.text.lower() in " ".join(services):
                        continue
                    if input_dir is not None:
                        blob = _seed_values_blob(input_dir, services)
                        if kw.text.lower() in blob:
                            continue
                    unresolved.append(kw.text)
                if unresolved and len(unresolved) == len(keywords) and not structural:
                    warnings.append(
                        f"{node.name}: keyword needle(s) "
                        f"{', '.join(repr(k) for k in unresolved)} not confirmed against "
                        f"[{svc_label}] routes/seeds - verify they match seed-derived "
                        f"path values (table names, record ids)."
                    )

        # 2) Directly-called endpoints (api_get/api_post/_request literals).
        for api_name, method, path in _direct_endpoints(node):
            svc = env_map.get(api_name)
            if svc is None:
                continue
            checked_endpoints += 1
            svc_routes = routes_for([svc])
            if not _endpoint_matches(method, path, svc_routes):
                route_list = "; ".join(f"{m} {p}" for m, p in svc_routes) \
                    or "(no routes found)"
                failures.append(
                    f"{node.name}: calls {method} {path} on {svc}, but the mock "
                    f"serves no such route. Real routes: {route_list}"
                )

    for warning in warnings:
        print(f"20_route_needle_check: WARN {warning}")

    if failures:
        print("20_route_needle_check: FAIL - impossible probes detected "
              "(the mock server can never produce these URLs; rewrite each needle "
              "to match a real route):", file=sys.stderr)
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)
        return 1

    print(f"20_route_needle_check: {checked_needles} needle(s) and "
          f"{checked_endpoints} direct endpoint call(s) verified against harness "
          f"routes PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

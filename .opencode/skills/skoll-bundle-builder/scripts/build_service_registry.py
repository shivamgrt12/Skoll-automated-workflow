#!/usr/bin/env python3
"""Scrape the environment harness into an authoritative service registry.

Every `<svc>-api/service.toml` declares the canonical `port`, `env_var_name`,
and `healthcheck_path`. service.toml is the single source of truth, preferred
over postman/docs which carry stale ports (e.g. quickbooks is 8007 in
service.toml but 8012 in its old api docs). assemble.py consumes this registry
to build every `<SERVICE>_API_URL=http://<svc>-api:<port>` env entry and the
healthcheck command in task.yaml.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib  # type: ignore


def _default_env_var(service_name: str) -> str:
    base = service_name[:-4] if service_name.endswith("-api") else service_name
    return base.replace("-", "_").upper() + "_API_URL"


def build_registry(harness_dir: Path) -> dict[str, dict]:
    registry: dict[str, dict] = {}
    for service_dir in sorted(harness_dir.glob("*-api")):
        toml_path = service_dir / "service.toml"
        if not toml_path.is_file():
            continue
        data = tomllib.loads(toml_path.read_text())
        svc = data.get("service", {})
        name = svc.get("name") or service_dir.name
        port = svc.get("port")
        if port is None:
            continue
        registry[name] = {
            "port": int(port),
            "env_var_name": svc.get("env_var_name") or _default_env_var(name),
            "healthcheck_path": svc.get("healthcheck_path") or "/health",
        }
    return registry


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: build_service_registry.py <harness_dir> [out.json]", file=sys.stderr)
        return 2
    harness_dir = Path(argv[1]).expanduser().resolve()
    if not harness_dir.is_dir():
        print(f"harness dir not found: {harness_dir}", file=sys.stderr)
        return 1
    registry = build_registry(harness_dir)
    payload = json.dumps(registry, indent=2, sort_keys=True)
    if len(argv) >= 3:
        Path(argv[2]).write_text(payload + "\n")
    print(payload)
    print(f"\n{len(registry)} services registered", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

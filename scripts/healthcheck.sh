#!/usr/bin/env bash

set -e

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT_DIR"

echo "[+] Desktop Sync health check"

python3 - <<'PY'
from src.config import load_config
from src.version import VERSION

config = load_config()

print("version:", VERSION)
print("environment:", config["application"]["environment"])
print("sync:", "enabled" if config["sync"]["enabled"] else "disabled")
print("endpoint:", config["endpoint"]["host"])
print("configuration: valid")
print("status: OK")
PY
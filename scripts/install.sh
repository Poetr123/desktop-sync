#!/usr/bin/env bash

set -e

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "[+] Installing desktop-sync"

mkdir -p "$ROOT_DIR/runtime"
mkdir -p "$ROOT_DIR/cache"
mkdir -p "$ROOT_DIR/artifacts"

python3 - <<'PY'
import json

with open("config/default.json", "r", encoding="utf-8") as f:
    config = json.load(f)

print("[+] Configuration loaded")
print("[+] Version:", config["application"]["version"])
print("[+] Endpoint:", config["endpoint"]["host"])
PY

echo "[+] Installation complete"
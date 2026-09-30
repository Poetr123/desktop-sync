#!/usr/bin/env bash

set -e

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "[+] Cleaning runtime files"

rm -rf "$ROOT_DIR/runtime"
rm -rf "$ROOT_DIR/cache"
rm -rf "$ROOT_DIR/artifacts"

mkdir -p "$ROOT_DIR/runtime"
mkdir -p "$ROOT_DIR/cache"
mkdir -p "$ROOT_DIR/artifacts"

echo "[+] Cleanup complete"
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
if command -v xdg-open >/dev/null 2>&1; then
  xdg-open "$(pwd)/index.html" >/dev/null 2>&1 &
else
  printf 'Abre este archivo en tu navegador: %s/index.html\n' "$(pwd)"
fi

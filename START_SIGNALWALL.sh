#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")"
PORT="${SIGNALWALL_PORT:-8080}"
echo "SignalWall: http://localhost:${PORT}"
python3 -m http.server "$PORT"

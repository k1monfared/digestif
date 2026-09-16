#!/usr/bin/env bash
# Headless UI tests for the point-hierarchy viewer (requires playwright + chromium)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

node "$SCRIPT_DIR/test_ui.js"
code=$?
if [[ $code -eq 2 ]]; then
    echo "=== UI test skipped: playwright not available ==="
    exit 0
fi
exit $code

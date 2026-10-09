#!/usr/bin/env bash
# Headless UI tests for the graph viewer and the aligned reading view
# (requires playwright + chromium, skips otherwise)
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

status=0
for suite in test_ui.js test_aligned_ui.js; do
    echo "### $suite"
    node "$SCRIPT_DIR/$suite"
    code=$?
    if [[ $code -eq 2 ]]; then
        echo "=== $suite skipped: playwright not available ==="
    elif [[ $code -ne 0 ]]; then
        status=$code
    fi
done
exit $status

#!/usr/bin/env bash
# Tests for src/digestif/skill-fitsegid/scripts/fitsegid.py
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
FITSEGID="$PROJECT_DIR/src/digestif/skill-fitsegid/scripts/fitsegid.py"
GRAPH_PY="$PROJECT_DIR/src/digestif/skill/scripts/graph.py"
EXAMPLES="$PROJECT_DIR/src/digestif/skill-fitsegid/examples"
GRAPH="$EXAMPLES/car-ban.graph.json"
PROSE="$EXAMPLES/car-ban.fitsegid.md"
CLEAN="$EXAMPLES/car-ban.fitsegid-clean.md"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

PASS=0
FAIL=0
TESTS_RUN=0

assert_eq() {
    local label="$1" expected="$2" actual="$3"
    TESTS_RUN=$((TESTS_RUN + 1))
    if [[ "$expected" == "$actual" ]]; then
        PASS=$((PASS + 1))
        echo "  PASS: $label"
    else
        FAIL=$((FAIL + 1))
        echo "  FAIL: $label"
        echo "    expected: $expected"
        echo "    actual:   $actual"
    fi
}

assert_contains() {
    local label="$1" expected="$2" actual="$3"
    TESTS_RUN=$((TESTS_RUN + 1))
    if [[ "$actual" == *"$expected"* ]]; then
        PASS=$((PASS + 1))
        echo "  PASS: $label"
    else
        FAIL=$((FAIL + 1))
        echo "  FAIL: $label"
        echo "    expected to contain: $expected"
        echo "    actual: $actual"
    fi
}

assert_exit_code() {
    local label="$1" expected="$2"
    shift 2
    TESTS_RUN=$((TESTS_RUN + 1))
    local actual_code=0
    "$@" > /dev/null 2>&1 || actual_code=$?
    if [[ "$expected" == "$actual_code" ]]; then
        PASS=$((PASS + 1))
        echo "  PASS: $label"
    else
        FAIL=$((FAIL + 1))
        echo "  FAIL: $label"
        echo "    expected exit code: $expected"
        echo "    actual exit code:   $actual_code"
    fi
}

mangle() {
    local dst="$1" py="$2"
    python3 -c "
t = open('$PROSE').read()
$py
open('$dst', 'w').write(t)
"
}

echo "=== check-prose: shipped example ==="
out="$(python3 "$FITSEGID" check-prose "$PROSE" "$GRAPH" 2>&1)"
code=$?
assert_eq "valid example exits 0" "0" "$code"
assert_contains "reports OK" "OK: prose is grounded" "$out"
assert_contains "full coverage" "10/10 nodes realized" "$out"
assert_contains "zero warnings" "0 warning(s)" "$out"

echo "=== check-prose: outline input ==="
python3 "$GRAPH_PY" to-outline "$GRAPH" -o "$TMP/car-ban.outline.log" > /dev/null
out="$(python3 "$FITSEGID" check-prose "$PROSE" --outline "$TMP/car-ban.outline.log" 2>&1)"
code=$?
assert_eq "outline input exits 0" "0" "$code"
assert_contains "outline full coverage" "10/10 nodes realized" "$out"

echo "=== check-prose: graph directory input ==="
cp "$GRAPH" "$TMP/graph.json"
assert_exit_code "run directory accepted" 0 python3 "$FITSEGID" check-prose "$PROSE" "$TMP"

echo "=== check-prose: failures ==="
mangle "$TMP/orphan.md" "t = t.replace('Public transit must expand before any ban takes effect. [3]', 'Public transit must expand before any ban takes effect.')"
code=0
out="$(python3 "$FITSEGID" check-prose "$TMP/orphan.md" "$GRAPH" 2>&1)" || code=$?
assert_eq "orphan sentence rejected" "1" "$code"
assert_contains "orphan sentence named" "sentence has no citation" "$out"

mangle "$TMP/unknown.md" "t = t.replace('[1.2]', '[9.9]')"
out="$(python3 "$FITSEGID" check-prose "$TMP/unknown.md" "$GRAPH" 2>&1)" || true
assert_contains "unknown node cited" "cites '9.9' which is not a node" "$out"
assert_exit_code "unknown node rejected" 1 python3 "$FITSEGID" check-prose "$TMP/unknown.md" "$GRAPH"

mangle "$TMP/malformed.md" "t = t.replace('[1.2]', '[01]')"
out="$(python3 "$FITSEGID" check-prose "$TMP/malformed.md" "$GRAPH" 2>&1)" || true
assert_contains "malformed citation named" "malformed citation '[01]'" "$out"

mangle "$TMP/missing.md" "t = t.replace(' A ban without transit is displacement, not improvement. [3.1]', '')"
out="$(python3 "$FITSEGID" check-prose "$TMP/missing.md" "$GRAPH" 2>&1)" || true
assert_contains "unrealized node named" "node 3.1 is neither cited in the prose nor listed in dropped" "$out"

mangle "$TMP/maxdropped.md" "t = t.replace('dropped: []', 'dropped: [\"1.2\"]')"
out="$(python3 "$FITSEGID" check-prose "$TMP/maxdropped.md" "$GRAPH" 2>&1)" || true
assert_contains "max with dropped rejected" "max means lossless" "$out"

mangle "$TMP/badfront.md" "t = t.replace('lod: max', 'lod: lots')"
out="$(python3 "$FITSEGID" check-prose "$TMP/badfront.md" "$GRAPH" 2>&1)" || true
assert_contains "bad lod rejected" "must be 'max' or a whole number" "$out"

mangle "$TMP/nofront.md" "t = t.split('---', 2)[2].lstrip()"
out="$(python3 "$FITSEGID" check-prose "$TMP/nofront.md" "$GRAPH" 2>&1)" || true
assert_contains "missing frontmatter rejected" "must start with '---'" "$out"

echo "=== check-prose: warnings ==="
mangle "$TMP/number.md" "t = t.replace('retail revenue rose in Madrid and Oslo', 'retail revenue rose 40 percent in Madrid and Oslo')"
code=0
out="$(python3 "$FITSEGID" check-prose "$TMP/number.md" "$GRAPH" 2>&1)" || code=$?
assert_eq "invented number is a warning, not an error" "0" "$code"
assert_contains "invented number named" "number '40' does not appear" "$out"
assert_exit_code "strict turns warning into error" 1 python3 "$FITSEGID" check-prose "$TMP/number.md" "$GRAPH" --strict

mangle "$TMP/attr.md" "t = t.replace('Critics also claim that car bans only work in wealthy cities.', 'Car bans only work in wealthy cities.')"
out="$(python3 "$FITSEGID" check-prose "$TMP/attr.md" "$GRAPH" 2>&1)" || true
assert_contains "unattributed counter named" "without attributing it" "$out"

echo "=== check-prose: level of detail ==="
cat > "$TMP/lod1.md" <<'EOF'
---
skill: fitsegid
lod: 1
dropped: ["1.1", "1.1.1", "1.2", "2.1", "2.2", "3.1"]
---

# Car ban paragraph

Cities should ban cars from their centers, though only after public transit expands, since the business-harm and elitism objections do not hold. [0]

Cities should ban cars from their centers. [1]

Critics also claim that car bans only work in wealthy cities. [2]

Public transit must expand before any ban takes effect. [3]
EOF
out="$(python3 "$FITSEGID" check-prose "$TMP/lod1.md" "$GRAPH" 2>&1)"
code=$?
assert_eq "lossy lod with full manifest exits 0" "0" "$code"
assert_contains "dropped nodes counted" "6 dropped" "$out"

mangle "$TMP/lodbad.md" "t = t.replace('lod: max', 'lod: 1')"
out="$(python3 "$FITSEGID" check-prose "$TMP/lodbad.md" "$GRAPH" 2>&1)" || true
assert_contains "lod layer count without manifest fails" "deeper than lod 1" "$out"

echo "=== strip-prose ==="
python3 "$FITSEGID" strip-prose "$PROSE" -o "$TMP/stripped.md" > /dev/null
TESTS_RUN=$((TESTS_RUN + 1))
if diff -q "$CLEAN" "$TMP/stripped.md" > /dev/null 2>&1; then
    PASS=$((PASS + 1))
    echo "  PASS: shipped clean copy matches strip output"
else
    FAIL=$((FAIL + 1))
    echo "  FAIL: shipped clean copy matches strip output"
    diff "$CLEAN" "$TMP/stripped.md" || true
fi
TESTS_RUN=$((TESTS_RUN + 1))
if grep -q '\[[0-9]' "$TMP/stripped.md"; then
    FAIL=$((FAIL + 1)); echo "  FAIL: citations stripped from clean copy"
else
    PASS=$((PASS + 1)); echo "  PASS: citations stripped from clean copy"
fi
TESTS_RUN=$((TESTS_RUN + 1))
if grep -q 'lod:' "$TMP/stripped.md"; then
    FAIL=$((FAIL + 1)); echo "  FAIL: frontmatter stripped from clean copy"
else
    PASS=$((PASS + 1)); echo "  PASS: frontmatter stripped from clean copy"
fi

echo "=== render ==="
assert_exit_code "renders the review viewer" 0 python3 "$FITSEGID" render "$PROSE" "$GRAPH" -o "$TMP/review.html"
out="$(cat "$TMP/review.html")"
assert_contains "review embeds the payload" "const DATA = {" "$out"
assert_contains "review embeds nodes" '"maxDepth"' "$out"
TESTS_RUN=$((TESTS_RUN + 1))
if grep -q '__REVIEW_JSON__' "$TMP/review.html"; then
    FAIL=$((FAIL + 1)); echo "  FAIL: template token replaced"
else
    PASS=$((PASS + 1)); echo "  PASS: template token replaced"
fi
assert_exit_code "render accepts an outline" 0 python3 "$FITSEGID" render "$PROSE" --outline "$TMP/car-ban.outline.log" -o "$TMP/review2.html"
assert_exit_code "render rejects an unknown node graph" 1 python3 "$FITSEGID" render "$PROSE" /nonexistent/graph.json -o "$TMP/none.html"

echo ""
echo "=== Results: $PASS passed, $FAIL failed, $TESTS_RUN total ==="
[[ $FAIL -eq 0 ]]

#!/usr/bin/env bash
# Tests for skills/point-hierarchy/scripts/graph.py
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
GRAPH="$PROJECT_DIR/src/digestif/skill/scripts/graph.py"
EXAMPLE="$PROJECT_DIR/src/digestif/skill/examples/car-ban.graph.json"
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

mutate() {
    local dst="$1" py="$2"
    python3 -c "
import json, sys
g = json.load(open('$EXAMPLE'))
$py
json.dump(g, open('$dst', 'w'), ensure_ascii=False, indent=2)
"
}

echo "=== validate: valid example ==="
out="$(python3 "$GRAPH" validate "$EXAMPLE" 2>&1)"
code=$?
assert_eq "valid example exits 0" "0" "$code"
assert_contains "reports OK" "OK: graph is valid" "$out"
assert_contains "full coverage" "coverage 5/5 passages" "$out"

echo "=== validate: broken graphs ==="
mutate "$TMP/bad_endpoint.json" 'g["edges"].append({"from": "9.9", "to": "1", "type": "supports"})'
assert_exit_code "unknown edge endpoint rejected" 1 python3 "$GRAPH" validate "$TMP/bad_endpoint.json"

mutate "$TMP/bad_ref.json" 'g["nodes"][1]["source"] = ["¶99"]'
assert_exit_code "citation to unknown passage rejected" 1 python3 "$GRAPH" validate "$TMP/bad_ref.json"

mutate "$TMP/bad_type.json" 'g["edges"][-1]["type"] = "vibes"'
assert_exit_code "undeclared edge type rejected" 1 python3 "$GRAPH" validate "$TMP/bad_type.json"

mutate "$TMP/two_parents.json" 'g["edges"].append({"from": "2", "to": "1.1", "type": "contains"})'
assert_exit_code "two contains parents rejected" 1 python3 "$GRAPH" validate "$TMP/two_parents.json"

mutate "$TMP/bad_root.json" 'g["nodes"][0]["type"] = "claim"'
assert_exit_code "non-summary root rejected" 1 python3 "$GRAPH" validate "$TMP/bad_root.json"

mutate "$TMP/uncited.json" 'g["meta"]["passages"]["¶6"] = "A sentence nobody cites."; g["meta"].pop("spans", None); g["meta"].pop("sourceText", None)'
out="$(python3 "$GRAPH" validate "$TMP/uncited.json" 2>&1)"
code=$?
assert_eq "uncited passage is a warning, not an error" "0" "$code"
assert_contains "uncited passage warned" "not cited by any node: ¶6" "$out"

mutate "$TMP/wordy.json" 'g["nodes"][1]["text"] = "This node text rambles on and on with far more words than any atomic idea node should ever be allowed to carry in a clean graph."'
out="$(python3 "$GRAPH" validate "$TMP/wordy.json" 2>&1)"
assert_contains "word cap warning" "exceeds 25 words" "$out"

mutate "$TMP/summary_child.json" 'g["nodes"].append({"id": "1.3", "type": "summary", "text": "misplaced", "attribution": "author", "source": ["¶1"]})'
assert_exit_code "summary type reserved for root" 1 python3 "$GRAPH" validate "$TMP/summary_child.json"

echo "=== stats ==="
out="$(python3 "$GRAPH" stats "$EXAMPLE")"
assert_contains "hub detection" "hubs (most cross-linked):" "$out"
assert_contains "tree ratio" "tree ratio: 0.75" "$out"
out="$(python3 "$GRAPH" stats "$TMP/uncited.json" --json | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['coverage']['total'])")"
assert_eq "json stats parse" "6" "$out"

echo "=== to-outline ==="
out="$(python3 "$GRAPH" to-outline "$EXAMPLE")"
assert_contains "summary line" "Summary: Cities should ban car traffic" "$out"
assert_contains "typed child" "Counterpoint: Car bans hurt businesses. (¶2) [counter]" "$out"
assert_contains "cross-links section" "1.1.1 supports 1.1 (¶2)" "$out"
assert_contains "qualifies link" "3 qualifies 1 (¶5)" "$out"
assert_contains "coverage line" "Coverage: 5 of 5 passages cited" "$out"
python3 "$GRAPH" to-outline "$TMP/bad_endpoint.json" > /dev/null 2>&1 \
    && assert_eq "refuses invalid graph" "0" "1" \
    || { TESTS_RUN=$((TESTS_RUN + 1)); PASS=$((PASS + 1)); echo "  PASS: refuses invalid graph"; }

echo "=== renumber ==="
mutate "$TMP/scrambled.json" '
for e in g["edges"]:
    if e["type"] == "supports" and e["from"] == "2.2": e["from"] = "2.9"
    elif e["type"] == "contains" and e["to"] == "2.2": e["to"] = "2.9"
g["nodes"] = [dict(n, id="2.9") if n["id"] == "2.2" else n for n in g["nodes"]]
'
assert_exit_code "scrambled graph still valid (gap ids allowed)" 0 python3 "$GRAPH" validate "$TMP/scrambled.json"
python3 "$GRAPH" renumber "$TMP/scrambled.json" -i > /dev/null
out="$(python3 "$GRAPH" validate "$TMP/scrambled.json" 2>&1)"
assert_contains "renumbered graph valid" "OK: graph is valid" "$out"
grep -q '"1.9"' "$TMP/scrambled.json" \
    && { TESTS_RUN=$((TESTS_RUN + 1)); FAIL=$((FAIL + 1)); echo "  FAIL: gap id normalized"; } \
    || { TESTS_RUN=$((TESTS_RUN + 1)); PASS=$((PASS + 1)); echo "  PASS: gap id normalized"; }
assert_contains "cross edge remapped by renumber" '"from": "2.2"' "$(cat "$TMP/scrambled.json")"

echo "=== to-html ==="
assert_exit_code "generates viewer" 0 python3 "$GRAPH" to-html "$EXAMPLE" -o "$TMP/out.html"
[[ -f "$TMP/out.html" ]]
assert_contains "graph embedded" "const GRAPH" "$(cat "$TMP/out.html")"
assert_contains "passages embedded" "Madrid and Oslo" "$(cat "$TMP/out.html")"
grep -q "__GRAPH_JSON__" "$TMP/out.html" \
    && { TESTS_RUN=$((TESTS_RUN + 1)); FAIL=$((FAIL + 1)); echo "  FAIL: placeholder replaced"; } \
    || { TESTS_RUN=$((TESTS_RUN + 1)); PASS=$((PASS + 1)); echo "  PASS: placeholder replaced"; }
assert_exit_code "refuses invalid graph" 1 python3 "$GRAPH" to-html "$TMP/bad_endpoint.json" -o "$TMP/bad.html"

echo "=== locate and spans ==="
cp "$EXAMPLE" "$TMP/tolocate.json"
assert_exit_code "locate fills spans" 0 python3 "$GRAPH" locate "$TMP/tolocate.json" "$PROJECT_DIR/src/digestif/skill/examples/car-ban.txt" -i
out="$(python3 "$GRAPH" validate "$TMP/tolocate.json" 2>&1)"
assert_contains "graph with spans validates" "OK: graph is valid" "$out"
out="$(python3 -c "
import json
g = json.load(open('$TMP/tolocate.json'))
m = g['meta']
print('span slice matches passage:', m['sourceText'][m['spans']['¶2'][0]:m['spans']['¶2'][1]] == m['passages']['¶2'])
")"
assert_contains "span slice equals passage text" "True" "$out"
python3 -c "
import json
g = json.load(open('$TMP/tolocate.json'))
g['meta']['passages']['¶2'] = 'Totally different text.'
json.dump(g, open('$TMP/tampered.json', 'w'), ensure_ascii=False)
"
assert_exit_code "span and passage mismatch rejected" 1 python3 "$GRAPH" validate "$TMP/tampered.json"
assert_exit_code "locate rejects a passage absent from source" 1 python3 "$GRAPH" locate "$TMP/tampered.json" "$PROJECT_DIR/src/digestif/skill/examples/car-ban.txt" -i
out="$(python3 "$GRAPH" validate "$EXAMPLE" 2>&1)"
assert_contains "shipped example has spans" "0 warning(s)" "$out"
out="$(python3 -c "
import json
g = json.load(open('$EXAMPLE'))
print('shipped example span count:', len(g['meta'].get('spans', {})))
")"
assert_contains "shipped example span count" "5" "$out"

echo "=== render ==="
assert_exit_code "render generates both outputs" 0 python3 "$GRAPH" render "$EXAMPLE" -o "$TMP/render"
[[ -f "$TMP/render/car-ban.outline.log" && -f "$TMP/render/car-ban.graph.html" ]]
assert_contains "rendered outline has coverage" "Coverage: 5 of 5" "$(cat "$TMP/render/car-ban.outline.log")"
assert_contains "rendered html embeds graph" "const GRAPH" "$(cat "$TMP/render/car-ban.graph.html")"
assert_exit_code "render refuses invalid graph" 1 python3 "$GRAPH" render "$TMP/bad_endpoint.json" -o "$TMP/render2"

echo "=== loglog interop ==="
python3 "$GRAPH" to-outline "$EXAMPLE" -o "$TMP/out.log" > /dev/null
if command -v loglog > /dev/null 2>&1 && loglog "$TMP/out.log" > "$TMP/out.md" 2>/dev/null; then
    assert_contains "outline converts via loglog" "Car ban" "$(cat "$TMP/out.md")"
else
    TESTS_RUN=$((TESTS_RUN + 1))
    echo "  SKIP: usable loglog CLI not installed, interop not tested"
fi

echo ""
echo "=== Results: $PASS passed, $FAIL failed, $TESTS_RUN total ==="
[[ $FAIL -eq 0 ]]

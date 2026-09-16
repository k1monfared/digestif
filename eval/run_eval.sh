#!/usr/bin/env bash
# Create a new timestamped eval run skeleton for any skill.
# Usage: ./run_eval.sh <skill-name> [skill-version-label]
# Example: ./run_eval.sh digestif v1
set -euo pipefail

SKILL_NAME="${1:?usage: run_eval.sh <skill-name> [version-label]}"
VERSION_LABEL="${2:-v1}"
EVAL_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$EVAL_ROOT/skills/$SKILL_NAME"
STAMP="$(date +%Y%m%d_%H%M)"
RUN_DIR="$SKILL_DIR/runs/${STAMP}_${VERSION_LABEL}"

if [[ ! -f "$SKILL_DIR/corpus.json" ]]
then
  echo "missing corpus: $SKILL_DIR/corpus.json" >&2
  exit 1
fi

mkdir -p "$RUN_DIR"
cp "$SKILL_DIR/config.json" "$RUN_DIR/config.snapshot.json" 2>/dev/null || true

python3 - "$SKILL_DIR" "$RUN_DIR" <<'PY'
import json, shutil, sys
from pathlib import Path
skill_dir = Path(sys.argv[1])
run_dir = Path(sys.argv[2])
corpus = json.loads((skill_dir / "corpus.json").read_text(encoding="utf-8"))
for item in corpus["items"]:
    sid = item["id"]
    sdir = run_dir / sid
    sdir.mkdir(parents=True, exist_ok=True)
    src = skill_dir / item["file"]
    dst = sdir / "source.txt"
    if src.exists() and not dst.exists():
        shutil.copy2(src, dst)
    (sdir / "output.log").touch(exist_ok=True)
    (sdir / "trace.md").touch(exist_ok=True)
    readme = sdir / "HOWTO.md"
    if not readme.exists():
        readme.write_text(
        f"# {sid}\n\n"
        "1. Generate loglog into output.log using the skill under test.\n"
        "2. Run the scripted judges: python3 eval/lib/judge_run.py all <this-dir>.\n"
        "   Or run the 4 judge prompts manually and save JSON per step:\n"
        "   a. Judge F prompt, save JSON as judge_faithfulness.json.\n"
        "   b. Judge Cov prompt, save JSON as judge_coverage.json.\n"
        "   c. Judge Con prompt, save JSON as judge_concision.json.\n"
        "   d. Judge Top prompt, save JSON as judge_top.json.\n"
        "3. Append full judge reasoning to trace.md (judge_run.py does this).\n"
        "4. Run eval/lib/aggregate.py and eval/lib/check.py from the run dir.\n",
        encoding="utf-8",
    )
PY

cat > "$RUN_DIR/RUNLOG.md" <<EOF
# Run $STAMP $VERSION_LABEL

Skill: $SKILL_NAME
Created: $STAMP
Config snapshot: config.snapshot.json

Workflow per sample dir:
source.txt plus output.log plus 4 judge JSON files plus trace.md

Finish with:
python3 eval/lib/aggregate.py eval/skills/$SKILL_NAME $RUN_DIR
python3 eval/lib/check.py eval/skills/$SKILL_NAME $RUN_DIR
EOF

echo "Created $RUN_DIR"
echo "Next: fill output.log per sample, run the 4 judge prompts, then aggregate."

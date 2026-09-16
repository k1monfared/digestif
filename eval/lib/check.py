#!/usr/bin/env python3
"""Validate that a run dir has the required auditable files.

Usage:
    python3 check.py <skill-dir> <run-dir>

Checks per sample: source.txt, output.log, four judge JSON files, trace.md.
Exits nonzero on missing files. Uses stdlib only.
"""
import json
import sys
from pathlib import Path

REQUIRED = [
    "source.txt",
    "output.log",
    "judge_faithfulness.json",
    "judge_coverage.json",
    "judge_concision.json",
    "judge_top.json",
    "trace.md",
]


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    skill_dir = Path(sys.argv[1])
    run_dir = Path(sys.argv[2])
    with open(skill_dir / "corpus.json", encoding="utf-8") as fh:
        corpus = json.load(fh)
    ok = True
    for item in corpus["items"]:
        sdir = run_dir / item["id"]
        for fname in REQUIRED:
            if not (sdir / fname).exists():
                print(f"MISSING {item['id']}/{fname}")
                ok = False
    if ok:
        print(f"OK: all {len(corpus['items'])} samples have full audit trail in {run_dir}")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()

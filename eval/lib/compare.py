#!/usr/bin/env python3
"""Compare two eval runs from their summary.json files.

Usage:
    python3 compare.py <run-dir-a> <run-dir-b> [label-a] [label-b]

Prints a markdown comparison: corpus summary deltas plus per-sample
verdict, faithfulness, must-recall, and redundancy moves. Stdlib only.
"""
import json
import sys
from pathlib import Path


def load(run_dir):
    with open(Path(run_dir) / "summary.json", encoding="utf-8") as fh:
        return json.load(fh)


def metric(row, key):
    if key == "verdict":
        return row.get("verdict")
    if key == "weighted":
        return row.get("weighted_score")
    data = row.get(key)
    if not isinstance(data, dict):
        return None
    if "metrics" in data:
        data = data["metrics"]
    return data


def find_metric(row, key):
    mapping = {
        "faith": ("faithfulness", "faithfulness_precision"),
        "must_recall": ("coverage", "must_recall"),
        "redundancy": ("concision", "redundancy_rate"),
    }
    section, field = mapping[key]
    data = row.get(section)
    if not isinstance(data, dict):
        return None
    if "metrics" in data:
        data = data["metrics"]
    return data.get(field)


def fmt(v):
    if v is None:
        return "?"
    if isinstance(v, float):
        return f"{v:.4f}"
    return str(v)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    a_dir, b_dir = sys.argv[1], sys.argv[2]
    a_label = sys.argv[3] if len(sys.argv) > 3 else Path(a_dir).name
    b_label = sys.argv[4] if len(sys.argv) > 4 else Path(b_dir).name
    a, b = load(a_dir), load(b_dir)

    print(f"# Run comparison: {a_label} vs {b_label}\n")
    print("## Corpus summary\n")
    print(f"| metric | {a_label} | {b_label} | delta |")
    print("| --- | --- | --- | --- |")
    keys = [
        ("pass", "pass"), ("borderline", "borderline"), ("fail", "fail"),
        ("avg_faithfulness_precision", "avg_faithfulness_precision"),
        ("avg_must_recall", "avg_must_recall"),
        ("avg_redundancy", "avg_redundancy"),
        ("avg_weighted_score", "avg_weighted_score"),
    ]
    for key, label in keys:
        va, vb = a["summary"].get(key), b["summary"].get(key)
        if isinstance(va, float) and isinstance(vb, float):
            delta = f"{vb - va:+.4f}"
        elif isinstance(va, int) and isinstance(vb, int):
            delta = f"{vb - va:+d}"
        else:
            delta = ""
        print(f"| {label} | {fmt(va)} | {fmt(vb)} | {delta} |")

    print("\n## Per sample\n")
    print(f"| id | verdict | faith | must recall | redundancy |")
    print("| --- | --- | --- | --- | --- |")
    a_rows = {r["id"]: r for r in a.get("rows", [])}
    b_rows = {r["id"]: r for r in b.get("rows", [])}
    for sid in sorted(set(a_rows) | set(b_rows)):
        ra, rb = a_rows.get(sid, {}), b_rows.get(sid, {})
        verdict = f"{ra.get('verdict', '?')} -> {rb.get('verdict', '?')}"
        faith = f"{fmt(find_metric(ra, 'faith'))} -> {fmt(find_metric(rb, 'faith'))}"
        must = f"{fmt(find_metric(ra, 'must_recall'))} -> {fmt(find_metric(rb, 'must_recall'))}"
        red = f"{fmt(find_metric(ra, 'redundancy'))} -> {fmt(find_metric(rb, 'redundancy'))}"
        print(f"| {sid} | {verdict} | {faith} | {must} | {red} |")


if __name__ == "__main__":
    main()

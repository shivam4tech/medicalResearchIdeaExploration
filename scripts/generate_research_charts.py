#!/usr/bin/env python3
"""Regenerate research charts from reports/candidate_matrix.csv.

Reproducible, no fake precision: reads the canonical candidate matrix and emits
(a) novelty-vs-feasibility scatter and (b) score-component bars to reports/figures/.

Qualitative scores are the Lead's decision-support numbers; figs carry that caveat.
Run:  python3 scripts/generate_research_charts.py
"""
import csv, os, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MATRIX = ROOT / "reports" / "candidate_matrix.csv"
FIGDIR = ROOT / "reports" / "figures"

COMPONENTS = [
    ("method", "Methodological contribution", 20),
    ("gap", "Evidence a gap exists", 20),
    ("clinical", "Clinical significance", 15),
    ("data", "Data feasibility", 15),
    ("screen", "Small-team feasibility", 10),
    ("negative", "Value of null result", 10),
    ("repro", "Reproducibility", 5),
    ("ethics", "Ethics/privacy feasibility", 5),
    ("india", "India relevance", 5),
]

def load():
    rows = []
    with open(MATRIX, newline="") as f:
        for r in csv.DictReader(f):
            if not r.get("candidate_id"):
                continue
            rows.append(r)
    return rows

def main():
    rows = load()
    if not rows:
        print(f"No scored candidates yet in {MATRIX} — nothing to plot.")
        return
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not installed; skipping charts. (pip install matplotlib)")
        return
    FIGDIR.mkdir(parents=True, exist_ok=True)

    ids = [r["candidate_id"] for r in rows]
    nov = [float(r.get("novelty_confidence") or 0) for r in rows]
    feas = [float(r.get("data_confidence") or 0) for r in rows]

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(nov, feas)
    for i, cid in enumerate(ids):
        ax.annotate(cid, (nov[i], feas[i]), textcoords="offset points", xytext=(5, 3))
    ax.set_xlabel("Novelty confidence"); ax.set_ylabel("Data feasibility confidence")
    ax.set_title("Candidate landscape (confidence, qualitative)")
    fig.savefig(FIGDIR / "candidate_landscape.png", dpi=140, bbox_inches="tight")
    plt.close(fig)

    # score component bars per candidate
    for r in rows:
        vals = []
        labels = []
        for key, label, _max in COMPONENTS:
            try:
                v = float(r.get(key) or 0)
            except ValueError:
                v = 0.0
            vals.append(v); labels.append(label.split()[0])
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.bar(labels, vals, color="#4c78a8")
        ax.set_ylim(0, max([m for *_, m in COMPONENTS]))
        ax.set_title(f"{r['candidate_id']} — {r.get('working_title','')} (components of 100)")
        fig.autofmt_xdate()
        fig.savefig(FIGDIR / f"score_{r['candidate_id']}.png", dpi=140, bbox_inches="tight")
        plt.close(fig)
    print(f"Wrote charts to {FIGDIR}")

if __name__ == "__main__":
    main()
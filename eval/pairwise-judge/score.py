#!/usr/bin/env python3
"""Compare judge results with human labels.

Metrics
- agreement (final): an item counts as agreeing only when BOTH orders pick the
  human winner (strict; a position-inconsistent verdict counts as a miss).
- per-judgment agreement: over all 20 single judgments (10 items x 2 orders).
- position consistency: share of items where both orders pick the same answer.
- Cohen's kappa on the final labels (inconsistent -> its own class).
"""
import json, pathlib, sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent
human = {d["index"]: d["winner"] for d in map(json.loads, open(ROOT / "data/human_labels.jsonl"))}


def kappa(a, b):
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = Counter(a), Counter(b)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / n / n
    return (po - pe) / (1 - pe) if pe < 1 else 1.0


def score(path):
    rows = [json.loads(l) for l in open(path)]
    by = {}
    for r in rows:
        by.setdefault(r["index"], {})[r["order"]] = r["winner"]
    finals, per_item = [], []
    for i in sorted(human):
        o, s = by[i].get("original"), by[i].get("swapped")
        final = o if o == s else "inconsistent"
        finals.append(final)
        per_item.append((i, human[i], o, s, final, final == human[i]))
    n = len(human)
    single = sum(r["winner"] == human[r["index"]] for r in rows)
    return {
        "file": pathlib.Path(path).name,
        "agreement": sum(x[-1] for x in per_item) / n,
        "per_judgment_agreement": single / len(rows),
        "position_consistency": sum(x[2] == x[3] for x in per_item) / n,
        "kappa": kappa(finals, [human[i] for i in sorted(human)]),
        "per_item": per_item,
    }


if __name__ == "__main__":
    files = sys.argv[1:] or sorted(str(p) for p in (ROOT / "results").glob("*.jsonl"))
    summary = []
    for f in files:
        s = score(f)
        summary.append({k: v for k, v in s.items() if k != "per_item"})
        print(f"\n=== {s['file']} ===")
        print(f"agreement={s['agreement']:.0%}  per_judgment={s['per_judgment_agreement']:.0%}  "
              f"position_consistency={s['position_consistency']:.0%}  kappa={s['kappa']:.2f}")
        print("idx human orig swap final match")
        for row in s["per_item"]:
            print(*row)
    (ROOT / "results" / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False))

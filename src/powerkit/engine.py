from __future__ import annotations
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean
from .rules import apply_rule


def _to_float(v: str):
    try:
        return float(v)
    except Exception:
        return None


def analyze_csv(path: Path, max_rows: int = 50_000) -> dict:
    with path.open("r", newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        cols = r.fieldnames or []
        rows = []
        for i, row in enumerate(r):
            if i >= max_rows:
                break
            rows.append(row)
    metrics = {"rows": len(rows), "columns": cols, "profiles": {}}
    for c in cols:
        vals = [row.get(c, "") for row in rows]
        nums = [x for x in (_to_float(v) for v in vals) if x is not None]
        non_empty = [v for v in vals if v not in ("", None)]
        top = Counter(non_empty).most_common(5)
        profile = {
            "non_empty": len(non_empty),
            "empty": len(vals) - len(non_empty),
            "distinct": len(set(non_empty)),
            "top_values": top,
        }
        if nums:
            m = mean(nums)
            var = mean([(x - m) ** 2 for x in nums])
            sd = var ** 0.5
            anomalies = sum(1 for x in nums if sd and abs((x - m) / sd) > 3)
            complexity = sum(abs(apply_rule("rule_17", n)) for n in nums[:1000]) / max(1, min(len(nums),1000))
            profile.update({"mean": m, "stddev": sd, "anomalies": anomalies, "complexity_score": complexity})
        metrics["profiles"][c] = profile
    return metrics


def summarize_jsonl(path: Path) -> dict:
    kinds = Counter()
    users = Counter()
    keys = Counter()
    total = 0
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            total += 1
            if isinstance(obj, dict):
                kinds[str(obj.get("type", "unknown"))] += 1
                users[str(obj.get("user", "unknown"))] += 1
                for k in obj.keys():
                    keys[k] += 1
    return {
        "events": total,
        "types": kinds.most_common(20),
        "users": users.most_common(20),
        "keys": keys.most_common(30),
    }

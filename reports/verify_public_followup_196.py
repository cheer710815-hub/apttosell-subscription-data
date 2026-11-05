#!/usr/bin/env python3
"""Verify derived 196-project CSV against published summary (not original API provenance).

Run from the repository root:
    python reports/verify_public_followup_196.py
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROJECTS = ROOT / "apttosell-apartment-subscription-followup-projects-2026-jan-sep.csv"
SUMMARY = ROOT / "apttosell-followup-analysis-2026-jan-sep-summary.csv"
BANDS = {
    "competition_band": {
        "<1:1": "1:1 미만", "1-5:1": "1~5:1", "5-10:1": "5~10:1",
        "10-30:1": "10~30:1", ">=30:1": "30:1 이상",
    },
    "price_band": {
        "<KRW 500m": "5억원 미만", "KRW 500m-700m": "5~7억원",
        "KRW 700m-1b": "7~10억원", "KRW 1b-1.5b": "10~15억원",
        ">=KRW 1.5b": "15억원 이상",
    },
}
def read(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))
def yes(row, col):
    return row[col].strip().lower() == "true"
def counts(rows):
    eligible = [r for r in rows if yes(r, "eligible_60d_observation")]
    return {
        "projects": len(rows),
        "followup_projects": sum(yes(r, "followup_supply_observed") for r in rows),
        "eligible_60d": len(eligible),
        "followup_within_60d": sum(yes(r, "followup_within_60d") for r in eligible),
    }
def run():
    p, summaries = read(PROJECTS), read(SUMMARY)
    errors = []
    valid = [r for r in p if r["first_priority_competition_rate"].strip()]
    ids = [r["house_manage_no"] for r in p]
    if len(p) != 196: errors.append(f"project rows: {len(p)} != 196")
    if len(valid) != 193: errors.append(f"complete competition rates: {len(valid)} != 193")
    if len(ids) != len(set(ids)): errors.append("duplicate housing management IDs")
    if any(not r["source_url"].strip() for r in p): errors.append("empty source URL")
    for r in p:
        if yes(r, "followup_within_60d") and not yes(r, "eligible_60d_observation"):
            errors.append("ineligible within-60d event: " + r["house_manage_no"])
        if not yes(r, "followup_supply_observed") and int(r["followup_event_count"]) > 0:
            errors.append("unobserved event with nonzero count: " + r["house_manage_no"])
    seen = set()
    for s in summaries:
        group, segment = s["metric_group"], s["segment"]
        seen.add((group, segment))
        if group in BANDS:
            if segment not in BANDS[group]:
                errors.append(f"unknown band: {group}/{segment}")
                continue
            rows = [r for r in valid if r[group] == BANDS[group][segment]]
        elif (group, segment) == ("headline", "first_priority_rate>=10:1"):
            rows = [r for r in valid if float(r["first_priority_competition_rate"]) >= 10]
        else:
            errors.append(f"unknown summary row: {group}/{segment}")
            continue
        actual = counts(rows)
        for k, n in actual.items():
            if int(s[k]) != n: errors.append(f"{group}/{segment}/{k}: {n} != {s[k]}")
        for k, numerator, denominator in [
            ("simple_followup_rate_pct", actual["followup_projects"], actual["projects"]),
            ("followup_60d_rate_pct", actual["followup_within_60d"], actual["eligible_60d"]),
        ]:
            calc = 100*numerator/denominator if denominator else 0.0
            if abs(calc - float(s[k])) > 0.011:
                errors.append(f"{group}/{segment}/{k}: {calc:.2f} != {s[k]}")
    expected = {("headline", "first_priority_rate>=10:1")}
    expected |= {(g, x) for g, m in BANDS.items() for x in m}
    if seen != expected: errors.append("summary row inventory mismatch")
    result = {"status": "FAIL" if errors else "PASS", "project_rows": len(p),
              "rate_complete": len(valid), "summary_rows": len(summaries),
              "errors": errors, "scope": "published derived CSV consistency only"}
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return int(bool(errors))
if __name__ == "__main__":
    try:
        raise SystemExit(run())
    except (OSError, KeyError, ValueError) as exc:
        print(json.dumps({"status": "ERROR", "message": str(exc)}, ensure_ascii=False))
        raise SystemExit(1)

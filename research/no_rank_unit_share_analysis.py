#!/usr/bin/env python3
"""Reproduce AptToSell first no-rank supply shares from existing public CSVs.
Run from repository root: python3 research/no_rank_unit_share_analysis.py
Only local files and Python standard library required.
This is a validation/pilot script, NOT a nationally representative estimate.
"""
import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "datasets"
OUT = ROOT / "research" / "outputs"
OUT.mkdir(parents=True, exist_ok=True)

def read(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def write(name, rows, fields):
    with (OUT / name).open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

def num(v):
    return float(v) if v not in ("", None) else 0.0

def main():
    cases = read(BASE / "seoul-high-competition-unsold-2026" /
                 "apttosell-seoul-high-competition-unsold-cases-2026-v1.0.csv")
    case_rows = []
    for r in cases:
        denominator = num(r["initial_general_sale_total"])
        units = num(r["first_unsold_units"])
        assert denominator > 0
        calculated = 100 * units / denominator
        assert abs(calculated - num(r["first_unsold_share_pct"])) < 0.01
        case_rows.append({
            "project": r["project"],
            "initial_house_manage_no": r["initial_house_manage_no"],
            "initial_first_priority_avg_rate": r["initial_first_priority_avg_rate"],
            "initial_general_sale_total": int(denominator),
            "first_unsold_units": int(units),
            "first_unsold_share_pct_recalculated": round(calculated, 4),
            "evidence_grade": r["evidence_grade"],
            "interpretation": "CASE_SERIES_NOT_NATIONAL"
        })
    write("seoul-seven-recalculated.csv", case_rows, list(case_rows[0]))
    den = sum(int(r["initial_general_sale_total"]) for r in case_rows)
    numer = sum(int(r["first_unsold_units"]) for r in case_rows)
    print(f"Seoul case series: {len(case_rows)} projects, {numer}/{den} = {100*numer/den:.4f}% (weighted)")

    types = read(BASE / "ddfs-national-type-riskset-2026" /
                 "apttosell-ddfs-national-type-riskset-2026-v1.0.csv")
    seen = set()
    exceptions = []
    bands = defaultdict(lambda: [0, 0, 0, 0])
    for r in types:
        key = (r["HOUSE_MANAGE_NO"], r["HOUSE_TY"])
        assert key not in seen, f"duplicate key {key}"
        seen.add(key)
        supply = num(r["supply"])
        units = num(r["first_followup_type_units"])
        rate = num(r["rate"])
        assert supply > 0 and rate >= 6
        band = "6-10" if rate < 10 else ("10-30" if rate < 30 else "30+")
        bands[band][0] += 1
        bands[band][1] += supply
        bands[band][2] += units
        bands[band][3] += int(num(r["reappeared_first_followup"]) > 0)
        if units > supply:
            exceptions.append({
                "initial_house_manage_no": r["HOUSE_MANAGE_NO"],
                "project": r["project"],
                "house_ty": r["HOUSE_TY"],
                "initial_general_supply": int(supply),
                "first_followup_type_units": int(units),
                "official_followup_notice_id": r["official_followup_notice_id"],
                "audit_flag": "VERIFY_INITIAL_TOTAL_TYPE_SUPPLY_AND_EVENT_CLASS"
            })
    write("ddfs-general-supply-denominator-exceptions.csv", exceptions,
          list(exceptions[0]))
    print(f"DDFS: {len(types)} types; {len(exceptions)} exceed initial general supply")
    for k in ("6-10", "10-30", "30+"):
        count, supply, units, reappeared = bands[k]
        print(f"  {k}: {count} types, {supply:.0f} general-supply units, {units:.0f} first-event units, {reappeared} reappeared")
    assert len(cases) == 7
    assert len(types) == 184
    assert len(exceptions) == 19
    print("Checks passed. Nationwide >=1:1/no-rank type-unit rate NOT ESTIMATED.")

if __name__ == "__main__":
    main()

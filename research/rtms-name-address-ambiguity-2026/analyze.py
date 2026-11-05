#!/usr/bin/env python3
"""RTMS apartment name–parcel ambiguity, with no raw-data redistribution."""
import argparse
import hashlib
import json
from pathlib import Path
import pandas as pd

KEYS = {
    "name_only": "complex_name",
    "district_and_name": "district_name",
    "legal_dong_and_name": "legal_dong_name",
}

def read_one(file: Path, period: str):
    raw = pd.read_csv(file, encoding="cp949", skiprows=15, dtype=str).fillna("")
    required = ["해제사유발생일", "시군구", "번지", "단지명"]
    missing = [c for c in required if c not in raw.columns]
    if missing:
        raise ValueError(f"Missing expected RTMS columns: {missing}")
    clean = raw.loc[raw["해제사유발생일"].isin(["", "-"])].copy()
    clean["parcel_address"] = clean["시군구"].str.strip() + "|" + clean["번지"].str.strip()
    clean["complex_name"] = clean["단지명"].str.strip()
    clean["district_name"] = clean["시군구"].str.split().str[1].fillna("") + "|" + clean["complex_name"]
    clean["legal_dong_name"] = clean["시군구"].str.strip() + "|" + clean["complex_name"]
    clean["period"] = period
    return raw, clean

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--year2025", type=Path, required=True)
    ap.add_argument("--year2026", type=Path, required=True)
    ap.add_argument("--output", type=Path, default=Path("results"))
    args = ap.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    summary, sources, details = [], {}, []
    for period, path in [("2025", args.year2025), ("2026-JanOct", args.year2026)]:
        raw, df = read_one(path, period)
        sources[period] = {
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "raw_rows": len(raw), "included_rows": len(df), "source_filename": path.name
        }
        for label, key in KEYS.items():
            grouped = df.groupby(key)["parcel_address"].nunique()
            ambiguous = set(grouped.index[grouped.gt(1)])
            affected = df[key].isin(ambiguous)
            summary.append({
                "period": period, "key": label,
                "observations": len(df),
                "distinct_keys": len(grouped),
                "ambiguous_keys": len(ambiguous),
                "affected_rows": int(affected.sum()),
                "affected_share": float(affected.mean()),
            })
            if label == "name_only":
                temp = df.loc[affected].groupby(["complex_name", "parcel_address"]).size().rename("transaction_rows").reset_index()
                temp["period"] = period
                details.append(temp)
    pd.DataFrame(summary).to_csv(args.output / "ambiguity_summary.csv", index=False, encoding="utf-8-sig")
    pd.concat(details, ignore_index=True).to_csv(args.output / "ambiguous_names_and_parcels.csv", index=False, encoding="utf-8-sig")
    (args.output / "input_manifest.json").write_text(json.dumps(sources, indent=2, ensure_ascii=False), encoding="utf-8")
    print(pd.DataFrame(summary).to_string(index=False))

if __name__ == "__main__":
    main()

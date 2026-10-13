#!/usr/bin/env python3
"""Normalize a REAL downloaded MOLIT presale/occupancy-rights CSV.
No estimated or invented transactions. Usage:
  python normalize_molit_presale.py downloads/2026-09-seoul.csv output/transactions.csv
CSV input is the Ministry's public download from https://rt.molit.go.kr/pt/xls/xls.do
"""
import csv, pathlib, re, sys
from datetime import date

NAMES = {
    "project_name": ["단지명", "아파트", "아파트명", "건물명"],
    "contract_date": ["계약일", "계약년월일"],
    "exclusive_area_m2": ["전용면적(㎡)", "전용면적(㎡)", "전용면적", "건물면적(㎡)", "면적"],
    "transaction_price_10000krw": ["거래금액(만원)", "거래금액", "거래금액(만원)"],
    "region": ["시군구", "시군구명", "지역"],
    "cancellation_date": ["해제사유발생일", "해제사유 발생일"],
    "right_type": ["거래구분", "분양입주권", "분양/입주권", "권리유형"]
}
def read_csv(path):
    raw = pathlib.Path(path).read_bytes()
    for enc in ("utf-8-sig", "cp949", "euc-kr"):
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            pass
    else:
        raise ValueError("No supported CSV encoding")
    lines = text.splitlines()
    start = next((i for i, l in enumerate(lines) if "거래금액" in l and ("면적" in l or "단지" in l)), None)
    if start is None:
        raise ValueError("Cannot find transaction header; inspect source and update mapping")
    return list(csv.DictReader(lines[start:]))

def normalize(row):
    def get(k):
        for label in NAMES[k]:
            if label in row and row[label] is not None:
                return row[label].strip()
        return ""
    price = get("transaction_price_10000krw").replace(",", "").replace(" ", "")
    area = get("exclusive_area_m2").replace(",", "")
    if price and not re.fullmatch(r"\d+", price):
        raise ValueError("Unparseable transaction price")
    if area:
        float(area)
    return {
        "project_name": get("project_name"),
        "contract_date_raw": get("contract_date"),
        "exclusive_area_m2": area,
        "transaction_price_10000krw": price,
        "region": get("region"),
        "right_type_raw": get("right_type"),
        "cancellation_date_raw": get("cancellation_date"),
        "match_status": "UNMATCHED",
        "original_offering_price_10000krw": "",
        "source_filename": ""
    }

def main(inp, out):
    source = pathlib.Path(inp)
    rows = read_csv(source)
    normalized = []
    for row in rows:
        if not any(v for v in row.values()):
            continue
        v = normalize(row)
        if not v["project_name"] or not v["transaction_price_10000krw"]:
            continue
        v["source_filename"] = source.name
        normalized.append(v)
    dest = pathlib.Path(out)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(normalized[0].keys()) if normalized else [
            "project_name","contract_date_raw","exclusive_area_m2",
            "transaction_price_10000krw","region","right_type_raw",
            "cancellation_date_raw","match_status","original_offering_price_10000krw","source_filename"])
        w.writeheader()
        w.writerows(normalized)
    print(f"Input rows={len(rows)} normalized rows={len(normalized)}; original-price matches=0 (not yet linked).")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: normalize_molit_presale.py input.csv output.csv")
    main(sys.argv[1], sys.argv[2])

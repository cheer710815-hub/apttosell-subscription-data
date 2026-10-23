#!/usr/bin/env python3
"""N01 v2.0 aggregate CSV reconciliation. Does not verify individual records."""
import argparse
import csv
from collections import defaultdict
from pathlib import Path

FILES = {"by_region.csv":15,"by_month.csv":2,"by_area_band.csv":4,"by_region_area_band.csv":43}
NAMES = {"count":("n","count","record_count","records","total_n"),"region":("region","region_name","sido","region_label"),"area":("area_band","area_group","exclusive_area_band","band")}

def column(fields, kind):
    matches=[f for f in fields if f.strip().lower() in NAMES[kind]]
    if len(matches)!=1:
        raise ValueError(f"Ambiguous {kind} column in {fields}; inspect original CSV headers")
    return matches[0]

def table(directory, filename, rows_expected):
    with (directory/filename).open(encoding="utf-8-sig",newline="") as f:
        reader=csv.DictReader(f)
        fields=reader.fieldnames or []
        records=list(reader)
    count=column(fields,"count")
    totals=[]
    for row in records:
        raw=(row.get(count) or "").strip().replace(",","")
        if not raw.isdecimal(): raise ValueError(f"{filename}: noninteger count {raw!r}")
        totals.append(int(raw))
    if len(records)!=rows_expected or sum(totals)!=980:
        raise ValueError(f"{filename}: rows={len(records)}, sum={sum(totals)} (expected {rows_expected},980)")
    print(f"PASS {filename}: {len(records)} rows, {sum(totals)} records")
    return fields,records,totals

def run(directory):
    t={name:table(directory,name,n) for name,n in FILES.items()}
    rf,rr,rn=t["by_region.csv"]; af,ar,an=t["by_area_band.csv"]
    xf,xr,xn=t["by_region_area_band.csv"]
    rk=column(rf,"region"); ak=column(af,"area")
    xrk=column(xf,"region"); xak=column(xf,"area")
    def mapping(rows, counts, field):
        result={}
        for row,n in zip(rows,counts):
            key=(row[field] or "").strip()
            if not key or key in result: raise ValueError("Empty or duplicate category")
            result[key]=n
        return result
    r=mapping(rr,rn,rk); a=mapping(ar,an,ak)
    rmargin=defaultdict(int); amargin=defaultdict(int); seen=set()
    for row,n in zip(xr,xn):
        k=((row[xrk] or "").strip(),(row[xak] or "").strip())
        if not all(k) or k in seen: raise ValueError(f"Duplicate or empty cross key: {k}")
        seen.add(k); rmargin[k[0]]+=n; amargin[k[1]]+=n
    if r!=dict(rmargin): raise ValueError("Region margin mismatch")
    if a!=dict(amargin): raise ValueError("Area margin mismatch")
    print("PASS region and area margins agree with 43-row cross-tab")
    print("Aggregate-only QA: no transaction-level, API, or SHA-256 verification")
    return 0

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory",type=Path)
    args=parser.parse_args()
    try: raise SystemExit(run(args.directory))
    except (OSError,ValueError,csv.Error) as exc:
        print(f"FAIL {exc}")
        raise SystemExit(1)

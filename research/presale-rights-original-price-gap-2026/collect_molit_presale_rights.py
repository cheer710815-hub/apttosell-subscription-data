#!/usr/bin/env python3
"""Rebuild raw MOLIT presale-rights transactions without publishing personal data.
API: https://www.data.go.kr/data/15126471/openapi.do
Configure endpoint from the current official API spec; no guessed URL embedded.
"""
import argparse, csv, hashlib, json, os, pathlib, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

def collect(endpoint, key, region, month, outdir):
    params = {"serviceKey": key, "LAWD_CD": region, "DEAL_YMD": month, "numOfRows": "1000", "pageNo": "1"}
    rows = []
    page = 1
    while True:
        params["pageNo"] = str(page)
        url = endpoint + ("&" if "?" in endpoint else "?") + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, headers={"User-Agent": "AptToSell-N01-research/1.0"})
        with urllib.request.urlopen(req, timeout=40) as resp:
            raw = resp.read()
        root = ET.fromstring(raw)
        code = root.findtext(".//resultCode")
        if code not in (None, "00", "000"):
            raise RuntimeError(f"API resultCode={code}: {root.findtext('.//resultMsg')}")
        items = root.findall(".//items/item")
        if not items and page == 1:
            raise RuntimeError("No item nodes found on first page; verify service response and field schema")
        for node in items:
            row = {child.tag: (child.text or "").strip() for child in node}
            row["request_region"] = region
            row["request_month"] = month
            rows.append(row)
        total = root.findtext(".//totalCount")
        if not items or (total is not None and len(rows) >= int(total)):
            break
        if page >= 100:
            raise RuntimeError("Pagination guard reached (100 pages)")
        page += 1
    fields = sorted(set().union(*(r.keys() for r in rows))) if rows else ["request_region", "request_month"]
    dest = pathlib.Path(outdir)
    dest.mkdir(parents=True, exist_ok=True)
    output = dest / f"molit_presale_rights_{region}_{month}_raw.csv"
    with output.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    manifest = {"region":region, "month":month, "records":len(rows), "pages":page,
                "retrieved_utc":datetime.now(timezone.utc).isoformat(),
                "sha256":digest, "source":"https://www.data.go.kr/data/15126471/openapi.do",
                "status":"RAW_UNVERIFIED_NOT_MATCHED", "local_file":output.name}
    (dest / (output.stem + "_manifest.json")).write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(manifest,ensure_ascii=False,indent=2))

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--endpoint", required=True, help="Current full API endpoint from official specification")
    p.add_argument("--region", required=True, help="5-digit law-dong region code")
    p.add_argument("--month", required=True, help="YYYYMM")
    p.add_argument("--outdir", default="private_raw")
    args = p.parse_args()
    if len(args.region)!=5 or not args.region.isdigit() or len(args.month)!=6 or not args.month.isdigit():
        p.error("Region must be five digits and month must be YYYYMM")
    token = os.environ.get("MOLIT_API_KEY")
    if not token:
        p.error("Set MOLIT_API_KEY in your environment; do not save or commit it")
    collect(args.endpoint,token,args.region,args.month,args.outdir)

#!/usr/bin/env python3
"""Rebuild raw MOLIT presale-rights transactions without publishing personal data.
API: https://www.data.go.kr/data/15126471/openapi.do
Official service: RTMSDataSvcSilvTrade/getRTMSDataSvcSilvTrade.
"""
import argparse, csv, hashlib, json, os, pathlib, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

DEFAULT_ENDPOINT = "https://apis.data.go.kr/1613000/RTMSDataSvcSilvTrade/getRTMSDataSvcSilvTrade"
def collect(endpoint, key, region, month, outdir):
    params = {"serviceKey": key, "LAWD_CD": region, "DEAL_YMD": month, "numOfRows": "1000", "pageNo": "1"}
    rows = []
    page = 1
    expected_total = None
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
        total_text = root.findtext(".//totalCount")
        if total_text is None or not total_text.isdigit():
            raise RuntimeError("Invalid or missing totalCount")
        total = int(total_text)
        if expected_total is None:
            expected_total = total
        elif total != expected_total:
            raise RuntimeError("totalCount changed across pages")
        if not items and page == 1 and (root.findtext(".//totalCount") not in ("0",)):
            raise RuntimeError("No item nodes found on first page despite nonzero/unknown totalCount")
        for node in items:
            row = {child.tag: (child.text or "").strip() for child in node}
            row["request_region"] = region
            row["request_month"] = month
            rows.append(row)
        if len(rows) > expected_total:
            raise RuntimeError("More rows than totalCount")
        if not items and len(rows) != expected_total:
            raise RuntimeError("Premature empty page")
        if len(rows) == expected_total:
            break
        if page >= 100:
            raise RuntimeError("Pagination guard reached (100 pages)")
        page += 1
    # Preserve duplicates in raw data until source transaction IDs are validated.
    fields = sorted(set().union(*(r.keys() for r in rows))) if rows else ["request_region", "request_month"]
    dest = pathlib.Path(outdir)
    dest.mkdir(parents=True, exist_ok=True)
    output = dest / f"molit_presale_rights_{region}_{month}_raw.csv"
    with output.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    # Inventory fields before applying any scientific inclusion/exclusion rules.
    # In particular, transaction cancellation and parties cannot be inferred
    # from fields documented for a DIFFERENT MOLIT service.
    field_inventory = {name: sum(1 for row in rows if row.get(name, "").strip())
                       for name in fields if name not in ("request_region", "request_month")}
    required_groups = {
        "reported_amount": ("dealAmount", "거래금액"),
        "exclusive_area": ("excluUseAr", "전용면적"),
        "cancellation_status": ("cdealType", "해제여부"),
        "deal_type": ("dealingGbn", "거래유형"),
        "seller_class": ("slerGbn", "매도자"),
        "buyer_class": ("buyerGbn", "매수자"),
    }
    schema_presence = {group: [n for n in candidates if n in fields]
                       for group, candidates in required_groups.items()}
    # Presence alone is insufficient: a field can exist but be empty in every row.
    # This is only a preliminary schema/data-availability check, NOT an
    # authorization to classify individual transactions.
    schema_complete_for_candidate_filter = bool(rows) and all(
        any(field_inventory.get(name, 0) > 0 for name in matches)
        for matches in schema_presence.values()
    )
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    manifest = {"region":region, "month":month, "records":len(rows), "pages":page,
                "retrieved_utc":datetime.now(timezone.utc).isoformat(),
                "sha256":digest, "source":"https://www.data.go.kr/data/15126471/openapi.do",
                "status":"RAW_UNVERIFIED_NOT_MATCHED", "expected_total":expected_total, "local_file":output.name, "field_inventory_nonblank":field_inventory, "filter_field_presence":schema_presence, "candidate_filter_schema_complete":schema_complete_for_candidate_filter}
    (dest / (output.stem + "_manifest.json")).write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(manifest,ensure_ascii=False,indent=2))

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--endpoint", default=DEFAULT_ENDPOINT, help="Official full API endpoint")
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

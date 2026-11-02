#!/usr/bin/env python3
"""Study 04: 2024 Seoul MOLIT sale CSV intake and descriptive rounding audit.
Not the original v3 matched/bootstrapped estimator.
"""
import argparse, hashlib, json, pathlib
from datetime import datetime, timezone
import pandas as pd

REQUIRED = ('계약년월', '거래금액(만원)', '거래유형', '해제사유발생일')
MODES = ('직거래', '중개거래')

def load_csv(path):
    for encoding in ('cp949', 'utf-8-sig', 'utf-8'):
        try:
            with path.open('r', encoding=encoding) as f:
                lines = [next(f, '') for _ in range(50)]
            skiprows = next((i for i, x in enumerate(lines)
                if '계약년월' in x and '거래금액' in x and '거래유형' in x), None)
            if skiprows is None: continue
            df = pd.read_csv(path, encoding=encoding, skiprows=skiprows,
                             dtype=str, keep_default_na=False, low_memory=False)
            df.columns = [str(x).strip().lstrip('\ufeff') for x in df.columns]
            if all(x in df.columns for x in REQUIRED): return df, encoding, skiprows
        except UnicodeError:
            continue
    raise ValueError('MOLIT header missing among first 50 lines')

def audit(source, out):
    source, out = pathlib.Path(source), pathlib.Path(out)
    if not source.is_file(): raise FileNotFoundError(source)
    if out.resolve() == source.parent.resolve():
        raise ValueError('Choose output folder different from raw source folder')
    df, encoding, skipped = load_csv(source)
    month = df['계약년월'].str.strip()
    if not month.str.fullmatch(r'2024(0[1-9]|1[0-2])').all():
        raise ValueError('Malformed or non-2024 contract year-month detected')
    if '시군구' not in df or not df['시군구'].str.strip().str.startswith('서울특별시').all():
        raise ValueError('Region not verifiably Seoul')
    not_cancelled = df['해제사유발생일'].str.strip().isin(('', '-'))
    mode = df['거래유형'].str.strip()
    price_s = df['거래금액(만원)'].str.replace(',', '', regex=False).str.strip()
    price = pd.to_numeric(price_s.where(price_s.str.fullmatch(r'\d+')), errors='coerce')
    validprice = price.notna() & price.gt(0) & (price % 1 == 0)
    validmode = mode.isin(MODES)
    eligible = not_cancelled & validmode & validprice
    used = df.loc[eligible].copy()
    used['_price'] = price[eligible].astype('int64')
    used['_mode'] = mode[eligible]
    used['_round'] = used['_price'].mod(1000).eq(0)
    rows=[]
    for m in MODES:
        part=used.loc[used['_mode'].eq(m)]
        denom=len(part); count=int(part['_round'].sum())
        rows.append(dict(transaction_mode=m, eligible_rows=denom,
            round_10million_krw_rows=count,
            rate_percent=round(100*count/denom,6) if denom else None))
    out.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(out/'unadjusted_summary.csv', index=False, encoding='utf-8-sig')
    rates=[r['rate_percent'] for r in rows]
    result=dict(status='DESCRIPTIVE_ONLY_NOT_V3_REPLICATION',
      created_utc=datetime.now(timezone.utc).isoformat(),
      source_filename=source.name, source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
      source_bytes=source.stat().st_size, encoding=encoding, skipped_preamble_rows=skipped,
      source_rows=len(df), source_columns=list(df.columns), observed_months=sorted(month.unique().tolist()),
      cancelled_or_marked_rows=int((~not_cancelled).sum()),
      unknown_mode_rows=int((~validmode).sum()),
      invalid_price_rows=int((~validprice).sum()),
      eligible_rows=int(eligible.sum()),
      unadjusted_difference_pp_direct_minus_broker=round(rates[0]-rates[1],6) if all(v is not None for v in rates) else None,
      caveat='Filter categories can overlap; v3 matched logic not validated')
    (out/'audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print('PASS: source inspection and descriptive summary completed (NOT v3 replication)')

if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('source')
    p.add_argument('--out', default='study04_2024_audit')
    a=p.parse_args()
    audit(a.source,a.out)

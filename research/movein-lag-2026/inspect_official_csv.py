"""Exploratory inspection of Korean APT official CSV. Does not establish original notice status.
Usage: python inspect_official_csv.py official.csv --out audit.json
"""
import argparse
import csv
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path

FIELDS = {'notice': '공고번호', 'house': '주택관리번호', 'date': '모집공고일', 'movein': '입주예정월'}

def clean(value):
    return str(value or '').strip()

def parse_year_month(value, day=False):
    s = clean(value)
    if not s:
        return None
    if day:
        for fmt in ('%Y-%m-%d', '%Y.%m.%d', '%Y/%m/%d', '%Y%m%d'):
            try:
                return datetime.strptime(s, fmt).strftime('%Y-%m')
            except ValueError:
                pass
        return None
    m = re.fullmatch(r'(20\d{2})[-./]?(0?[1-9]|1[0-2])', s)
    return f'{m.group(1)}-{int(m.group(2)):02d}' if m else None

def inspect(path):
    data = path.read_bytes()
    for encoding in ('utf-8-sig', 'cp949', 'euc-kr'):
        try:
            raw = data.decode(encoding)
            break
        except UnicodeDecodeError:
            pass
    else:
        raise ValueError('Unsupported CSV encoding')
    reader = csv.DictReader(raw.splitlines())
    headers = reader.fieldnames or []
    required = set(FIELDS.values())
    if not required.issubset(headers):
        raise ValueError('Missing official columns; received: ' + repr(headers))
    totals = Counter()
    yearly = {}
    seen = set()
    examples = []
    for row in reader:
        totals['all_source_rows'] += 1
        announcement = parse_year_month(row.get(FIELDS['date']), day=True)
        if announcement is None:
            totals['invalid_notice_date'] += 1
            continue
        year = announcement[:4]
        if year not in ('2025', '2026'):
            totals['outside_2025_2026'] += 1
            continue
        group = yearly.setdefault(year, Counter())
        group['in_window_rows'] += 1
        key = (clean(row.get(FIELDS['house'])), clean(row.get(FIELDS['notice'])))
        if not any(key):
            totals['missing_identifiers'] += 1
            group['missing_identifiers'] += 1
            continue
        if key in seen:
            totals['exact_id_pair_duplicate'] += 1
            group['exact_id_pair_duplicate'] += 1
            continue
        seen.add(key)
        totals['distinct_notice_id_pairs'] += 1
        group['distinct_id_pairs'] += 1
        movein = parse_year_month(row.get(FIELDS['movein']))
        if movein is None:
            totals['movein_missing_or_invalid'] += 1
            group['movein_missing_or_invalid'] += 1
            continue
        totals['valid_movein_month'] += 1
        group['valid_movein_month'] += 1
        gap = (int(movein[:4]) - int(year)) * 12 + int(movein[5:]) - int(announcement[5:])
        label = 'negative_gap' if gap < 0 else 'nonnegative_gap'
        totals[label] += 1
        group[label] += 1
        if len(examples) < 5:
            examples.append({'notice_id': key[1], 'notice_month': announcement, 'movein_month': movein, 'gap_months': gap})
    return {'file': str(path), 'headers': headers, 'counts': dict(totals),
            'by_notice_year': {k: dict(v) for k, v in yearly.items()},
            'actual_file_examples': examples,
            'limitations': 'Exploratory ID-pair counts only. Original notice type and correction history require manual QA. Do not report counts as verified original announcements.'}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('csv', type=Path)
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    result = inspect(args.csv)
    report = json.dumps(result, ensure_ascii=False, indent=2)
    print(report)
    if args.out:
        args.out.write_text(report, encoding='utf-8')

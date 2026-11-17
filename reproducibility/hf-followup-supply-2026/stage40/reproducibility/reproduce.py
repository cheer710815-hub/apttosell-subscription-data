#!/usr/bin/env python3
"""ARHRN Stage 36: reproducibility check for public AptToSell HF CSVs.
Python 3.9+, standard library only. No source files are overwritten.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path
from urllib.request import Request, urlopen
from decimal import Decimal, ROUND_HALF_UP

REPO = 'eunguneun/korea-apartment-subscription-followup-supply-2026'
BASE = f'https://huggingface.co/datasets/{REPO}/resolve/main/'
PROJECT = 'apttosell-apartment-subscription-followup-projects-2026-jan-sep.csv'
SUMMARY = 'apttosell-followup-analysis-2026-jan-sep-summary.csv'
C_BANDS = {'<1:1': '1:1 미만', '1-5:1':'1~5:1', '5-10:1':'5~10:1', '10-30:1':'10~30:1', '>=30:1':'30:1 이상'}
P_BANDS = {'<KRW 500m':'5억원 미만','KRW 500m-700m':'5~7억원','KRW 700m-1b':'7~10억원','KRW 1b-1.5b':'10~15억원','>=KRW 1.5b':'15억원 이상'}
COUNT_FIELDS = ('projects', 'followup_projects', 'eligible_60d', 'followup_within_60d')


def validate_downloaded_csv(data, name, source_url='download'):
    """Accept UTF-8 CSV with or without BOM and reject HTML/JSON/error pages.

    Validation is based on parsed column names instead of byte prefix equality.
    """
    if not data:
        raise RuntimeError(f'Empty download for {name} from {source_url}')
    try:
        first_line = data.decode('utf-8-sig').splitlines()[0]
        header = next(csv.reader([first_line]))
    except (UnicodeError, IndexError, csv.Error) as exc:
        raise RuntimeError(f'Invalid UTF-8 CSV download for {name} from {source_url}: {exc}') from exc
    required = {
        PROJECT: ['house_manage_no', 'project_name', 'source_url'],
        SUMMARY: ['metric_group', 'segment', 'projects', 'followup_projects'],
    }[name]
    if not all(col in header for col in required):
        snippet = repr(data[:100])
        raise RuntimeError(
            f'Downloaded file is not expected CSV: {name} from {source_url}; '
            f'first bytes={snippet}; parsed header={header[:8]}. '
            'If this is an HTML/error page, download the CSV manually and use --offline.'
        )
    return header


def download_if_absent(path, name):
    if path.exists():
        validate_downloaded_csv(path.read_bytes(), name, str(path))
        return
    # Hugging Face can redirect /resolve/main/ or occasionally return a
    # transient error body. Try the raw endpoint only after a failure.
    urls = [BASE + name, f'https://huggingface.co/datasets/{REPO}/raw/main/{name}']
    failures = []
    for url in urls:
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0 ARHRN-Reproducibility-Audit/1.1', 'Accept': 'text/csv,*/*'})
            with urlopen(req, timeout=45) as resp:
                data = resp.read()
            validate_downloaded_csv(data, name, url)
            path.write_bytes(data)
            return
        except Exception as exc:
            failures.append(f'{url}: {type(exc).__name__}: {exc}')
    raise RuntimeError('Unable to download valid original CSV '+name+'\n'+'\n'.join(failures))


def read_csv(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        rd = csv.DictReader(f)
        rows = list(rd)
        return list(rd.fieldnames or []), rows


def positive(row, key):
    return row.get(key, '').strip().lower() == 'true'


def counts(rows):
    return {'projects':len(rows),
            'followup_projects':sum(positive(x,'followup_supply_observed') for x in rows),
            'eligible_60d':sum(positive(x,'eligible_60d_observation') for x in rows),
            'followup_within_60d':sum(positive(x,'followup_within_60d') for x in rows)}


def percent(a,b):
    return (Decimal(a)*100/Decimal(b)).quantize(Decimal('0.01'),rounding=ROUND_HALF_UP) if b else None


def audit(project_rows, summary_rows):
    known = [r for r in project_rows if r['first_priority_competition_rate'].strip()]
    absent = [r for r in project_rows if not r['first_priority_competition_rate'].strip()]
    problems = []
    ids=[r.get('house_manage_no','').strip() for r in project_rows]
    if len(ids)!=len(set(ids)):
        problems.append('Duplicate house_manage_no values found')
    if any(not x for x in ids):
        problems.append('Missing house_manage_no values found')
    keys=[(r.get('metric_group'),r.get('segment')) for r in summary_rows]
    if len(keys)!=len(set(keys)):
        problems.append('Duplicate summary metric_group/segment rows found')
    for field in ('followup_supply_observed','eligible_60d_observation','followup_within_60d'):
        bad=sum(r.get(field,'').strip().lower() not in ('true','false','') for r in project_rows)
        if bad: problems.append(f'Unexpected boolean values in {field}: {bad}')
    compared = []
    for row in summary_rows:
        group, segment = row['metric_group'], row['segment']
        if group == 'competition_band':
            chosen = [r for r in known if r['competition_band'] == C_BANDS[segment]]
        elif group == 'price_band':
            chosen = [r for r in known if r['price_band'] == P_BANDS[segment]]
        elif group == 'headline' and segment == 'first_priority_rate>=10:1':
            chosen = [r for r in known if Decimal(r['first_priority_competition_rate']) >= 10]
        else:
            problems.append(f'Unexpected summary group/segment: {group}/{segment}')
            continue
        derived = counts(chosen)
        for k in COUNT_FIELDS:
            if derived[k] != int(row[k]):
                problems.append(f'{group}/{segment} {k}: computed {derived[k]}, published {row[k]}')
        pr = percent(derived['followup_projects'], derived['projects'])
        p60 = percent(derived['followup_within_60d'], derived['eligible_60d'])
        for key,value in [('simple_followup_rate_pct',pr),('followup_60d_rate_pct',p60)]:
            published = Decimal(row[key]) if row.get(key) else None
            if value != published and (value is None or published is None or abs(value-published) > Decimal('0.01')):
                problems.append(f'{group}/{segment} {key}: computed {value}, published {published}')
        compared.append(dict(metric_group=group, segment=segment, **derived,
                             calculated_simple_pct=str(pr), calculated_60d_pct=str(p60),
                             published_simple_pct=row.get('simple_followup_rate_pct'),
                             published_60d_pct=row.get('followup_60d_rate_pct')))

    flag_issues = {
        'no_followup_but_positive_events':sum(not positive(r,'followup_supply_observed') and int(r['followup_event_count'])>0 for r in project_rows),
        'followup_but_zero_events':sum(positive(r,'followup_supply_observed') and int(r['followup_event_count'])==0 for r in project_rows),
        'within_60d_but_ineligible':sum(positive(r,'followup_within_60d') and not positive(r,'eligible_60d_observation') for r in project_rows),
        'within_60d_but_no_followup':sum(positive(r,'followup_within_60d') and not positive(r,'followup_supply_observed') for r in project_rows),
    }
    for k,v in flag_issues.items():
        if v: problems.append(f'{k}: {v}')
    if len(project_rows)!=196: problems.append('Expected 196 project rows')
    if len(known)!=193: problems.append('Expected 193 known competition rates')
    if len(summary_rows)!=11: problems.append('Expected 11 summary rows')
    if counts(project_rows)!=dict(projects=196, followup_projects=103, eligible_60d=161, followup_within_60d=83):
        problems.append('Full-cohort aggregate differs from Stage 35 baseline')

    sensitivity = []
    for segment, korean in P_BANDS.items():
        full = counts([r for r in project_rows if r['price_band']==korean])
        sub = counts([r for r in known if r['price_band']==korean])
        sensitivity.append({'segment':segment,'price_band':korean,
                           'published_subset_n':sub['projects'], 'full_cohort_n':full['projects'],
                           'subset_simple_pct':str(percent(sub['followup_projects'],sub['projects'])),
                           'full_simple_pct':str(percent(full['followup_projects'],full['projects'])),
                           'subset_eligible_60d':sub['eligible_60d'], 'full_eligible_60d':full['eligible_60d'],
                           'subset_60d_pct':str(percent(sub['followup_within_60d'],sub['eligible_60d'])),
                           'full_60d_pct':str(percent(full['followup_within_60d'],full['eligible_60d']))})
    return {'status':'PASS' if not problems else 'FAIL',
            'dataset_repository':REPO, 'original_projects':len(project_rows),
            'complete_case_projects':len(known),'summary_rows':len(summary_rows),
            'cohort_totals':counts(project_rows),
            'high_competition_10plus':counts([r for r in known if Decimal(r['first_priority_competition_rate'])>=10]),
            'excluded_project_ids':[r['house_manage_no'] for r in absent],
            'flag_issues':flag_issues, 'summary_comparison':compared,
            'price_band_sensitivity':sensitivity,'problems':problems}


def write_csv(path, rows):
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader();w.writerows(rows)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-dir', default='source', help='CSV input folder; download only if files do not exist')
    parser.add_argument('--out-dir', default='results', help='Output folder')
    parser.add_argument('--offline', action='store_true', help='Never download missing input CSV files')
    a=parser.parse_args(); src=Path(a.input_dir); dst=Path(a.out_dir);src.mkdir(parents=True,exist_ok=True);dst.mkdir(parents=True,exist_ok=True)
    for f in [PROJECT,SUMMARY]:
        if a.offline and not (src/f).exists():parser.error(f'Offline input missing: {src/f}')
        download_if_absent(src/f,f)
    ph,pr=read_csv(src/PROJECT);sh,sr=read_csv(src/SUMMARY)
    result=audit(pr,sr)
    result['files']={f:{'bytes':(src/f).stat().st_size,'sha256':hashlib.sha256((src/f).read_bytes()).hexdigest()} for f in [PROJECT,SUMMARY]}
    result['schema']={'project_columns':len(ph),'summary_columns':len(sh)}
    if len(ph)!=18 or len(sh)!=8:
        result['problems'].append('Unexpected CSV column count')
        result['status']='FAIL'
    (dst/'audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    write_csv(dst/'summary_comparison.csv',result['summary_comparison'])
    write_csv(dst/'price_band_sensitivity.csv',result['price_band_sensitivity'])
    print(f"STATUS={result['status']} projects={result['original_projects']} complete_case={result['complete_case_projects']} summary={result['summary_rows']}")
    print('Results:',dst.resolve())
    if result['problems']:
        for p in result['problems']:print('ERROR:',p)
        raise SystemExit(1)

if __name__=='__main__':main()
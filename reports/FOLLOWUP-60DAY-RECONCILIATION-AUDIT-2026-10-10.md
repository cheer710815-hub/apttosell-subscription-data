# 60-day follow-up supply metric — reconciliation audit (2026-10-10)

**Status: OPEN / NOT FOR PUBLICATION AS A NEW FINDING**

## Observed discrepancy

- Repository README currently states: **60-day eligible cohort 36; follow-up within 60 days 13; 36.1%**.
- Recount of repository CSV `reports/apttosell-apartment-subscription-followup-projects-2026-jan-sep.csv` (196 rows), filtering **`eligible_60d_observation == true`** yields **161 rows**, of which **83** have **`followup_within_60d == true`** (51.6%).
- These are **different counts**, and the cause has **not** been established. The 36/13 README metric might use an additional cohort restriction that is not evident from the two boolean columns. **Do not replace the published metric with 161/83 without reconstructing the original analysis.**

## Required checks before further release

1. Read the original report methodology, summary CSV, and generating script. Identify every inclusion condition (first-priority competition threshold, dates, observation cutoff, event matching, eligibility, missing values).
2. Verify whether 36/13 specifically means **competition >= 10:1** and **60-day eligible**, rather than all 196 projects. Recompute using that exact threshold and check boundary treatment.
3. Check the event chronology against source URLs, later notices, and whether later notices mean unsold/optional supply rather than contract failure.
4. Publish a named cohort table and reproducible script, only after the discrepancy is resolved.
5. Preserve the existing frozen RPG v1.0.1 files and SHA256SUMS unchanged. This audit concerns a separate follow-up supply analysis.

## Reproduction (Python)

```python
import pandas as pd
p = 'reports/apttosell-apartment-subscription-followup-projects-2026-jan-sep.csv'
df = pd.read_csv(p)
eligible = df[df['eligible_60d_observation'].astype(str).str.lower().eq('true')]
print(len(df), len(eligible), eligible['followup_within_60d'].astype(str).str.lower().eq('true').sum())
# Expected raw-column counts: 196, 161, 83. This is NOT yet the final published cohort.
```

## Citation discipline

Do not call a follow-up notice a non-contract rate. Do not present raw 60-day proportions as causal, or as the probability a subscription applicant will fail to contract. Mark results as provisional until cohort reconciliation is completed.


## FINAL RESOLUTION — 2026-10-10

**Verified against properly parsed, quoted CSV:** 196 project rows; first-priority competition >=10:1: **44**; high-competition and eligible for 60-day observation: **36**; high-competition eligible with follow-up within 60 days: **13**; rate **36.11%**. All-competition eligible: **161**; all-competition eligible with 60-day follow-up: **83**. Both are distinct cohorts. The earlier 45/35 result was an **invalid naive comma split** of quoted CSV fields containing commas in project names; it is withdrawn. The README and summary headline 44/36/13 need **no correction**.

Validation code must use an RFC 4180-compliant CSV parser (e.g. Python pandas.read_csv or csv.DictReader), not `line.split(',')`.

**Scope:** Internal consistency of the published project CSV, summary CSV and methodology has been reconciled. Independent upstream ApplyHome event matching/source verification remains a separate validation step. Follow-up supply is not a non-contract rate.

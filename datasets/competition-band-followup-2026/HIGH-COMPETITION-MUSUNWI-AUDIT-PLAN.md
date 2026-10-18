# High-competition projects followed by 무순위 — verification protocol (2026)

**Status:** Research in progress; not a verified 무순위 incidence estimate. **Prepared:** 2026-10-18.

## Existing reproducible baseline
Source: [competition-band-followup-2026 v1.0](./README.md), initial notices 2026-01-01 to 2026-09-30, observation cutoff 2026-10-04, 196 projects, 193 with observed first-priority competition rates.

| Initial first-priority competition | Projects | Projects with broadly defined subsequent supply notice | Unadjusted rate |
|---|---:|---:|---:|
| <1:1 | 93 | 41 | 44.1% |
| 1–<5:1 | 40 | 32 | 80.0% |
| 5–<10:1 | 16 | 11 | 68.8% |
| 10–<30:1 | 23 | 17 | 73.9% |
| >=30:1 | 21 | 2 | 9.5% |

Derived **broad-followup** aggregates (not verified 무순위 counts): >=1:1 = 62/100 (62.0%); >=5:1 = 30/60 (50.0%); >=10:1 = 19/44 (43.2%); >=30:1 = 2/21 (9.5%). These are crude proportions with unequal follow-up observation time. Do not present them as actual contract cancellations or unsold percentages.

## Primary question
Among projects with initial first-priority competition >=10:1, how many had a **verified official 무순위(사후)** notice within a comparable observation window? Distinguish this from 임의공급 and 불법행위재공급/계약취소주택.

## Mandatory verification steps
1. Extract the 44 project IDs in the >=10:1 cohort from the published project CSV. Preserve original announcement date, first-priority applications, general-supply denominator and competition-rate definition.
2. For each candidate subsequent notice, retrieve the official ApplyHome notice PDF and announcement identifier. Verify exact supply category on its cover, original project linkage and announcement date. The existing name+address matching is provisional, not legal-category verification.
3. Store event-level evidence: initial project ID, initial notice ID, subsequent notice ID, official PDF URL, announcement date, supply category (무순위(사후) / 임의공급 / 불법행위재공급 / other / unknown), and verification status.
4. Match housing types using official model/type identifiers. Compare initial type-level competition to subsequent type-level supply. A high project-average rate does not imply a high rate for every supplied type.
5. For repeat notices, deduplicate by project for incidence, by official event ID for notice counts, and by dwelling identifier where available for distinct units. Never add successive notice supply counts as unique dwellings without overlap verification.
6. Recalculate 60- and 90-day risk sets with the same cutoff; do not count projects without full observation windows as non-events in fixed-window denominators.
7. Cross-check a subset against original PDF pages and record disagreements. Mark unverifiable events separately, rather than guessing.

## Publishable outcomes after audit
- Project-level verified 무순위 incidence among >=10:1 cohort, with exact numerator and denominator and 60/90-day variants.
- Type-level discordance: first-priority rate >=10:1 for the same type that later appeared in verified 무순위.
- Initial general-supply count versus **first** subsequent 무순위 supply count; separate this from repeated/unique dwelling counts.
- Breakdown by region, price gap and event type only if coverage and linkage quality support it.

## Interpretation boundaries
A subsequent notice is not a direct observation of contract conversion, forfeiture, or unsold inventory. No causal claim that higher competition produces or prevents 무순위. Existing RFSEQ v2.6 DOI 10.5281/zenodo.23433246 documents notice intervals, not verified category-specific incidence. No new DOI or public results are asserted here.

## Evidence sources
- [Published baseline dataset](./apttosell-competition-band-followup-projects-2026-v1.0.csv)
- [Baseline methodology](./METHODOLOGY.md)
- [ApplyHome supply-information API](https://www.data.go.kr/data/15098547/openapi.do)
- [ApplyHome subscription-competition API](https://www.data.go.kr/data/15098905/openapi.do)

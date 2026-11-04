# Reuse-ready verification note — 196 apartment subscription projects

Audit date: 2026-11-04. **Existing research documentation improvement**, not a new dataset or statistical publication.

## Source and version
- Canonical explainer: https://apttosell.com/subscription-followup-data-2026/
- Dataset directory: https://github.com/cheer710815-hub/apttosell-subscription-data/tree/main/datasets/competition-band-followup-2026/
- Published Figshare record: https://doi.org/10.6084/m9.figshare.34064439 (verify actual released file/version before direct citation).
- Source services: Korea Real Estate Board ApplyHome notices https://www.data.go.kr/data/15098547/openapi.do ; competition https://www.data.go.kr/data/15098905/openapi.do .
- Initial notices: 2026-01-01 through 2026-09-30; follow-up event observation cutoff: 2026-10-04.
- Use dataset-specific citation metadata; repository top-level CITATION.cff covers multiple unrelated studies.

## Independent CSV read checks (GitHub default branch, 2026-11-04)
- Project file parsed: 196 rows, 17 columns; unique internal project IDs 196/196, unique housing-management IDs 196/196.
- Counts per competition band and event status:
  - <1: 93 projects / 41 follow-up;
  - 1–<5: 40 / 32;
  - 5–<10: 16 / 11;
  - 10–<30: 23 / 17;
  - >=30: 21 / 2;
  - competition not confirmed: 3 / 0.
- Totals: 103 projects flagged with follow-up. 60-day eligible count 161; 90-day eligible count 142.
- Re-aggregated source row counts by band match the published summary table's project totals and follow-up-event totals.
- These checks do **not** independently re-fetch all original ApplyHome API event responses or reconfirm every historical source URL.

## Unit of observation and interpretation
Each row = an initial APT project/notice cohort, not an individual buyer, transaction, contracted unit, or project-finance exposure. `has_followup` indicates an observed later no-priority / remaining-supply / discretionary-supply notice matching the published criteria. It is **not** an initial contracted-sales rate, cancellation rate, PF default, or unsold-unit count.

Average first-priority competition = summed first-priority application records / summed general-supply units, using each housing type once in the supply denominator (per METHODOLOGY.md). The 60/90-day measures use only sufficiently observable cohorts; they do not model censoring via survival analysis.

## What downstream researchers may and may not do
Appropriate: exploratory comparison of competition bands against a **binary observed follow-up notice**; descriptive event frequencies; case sampling for manual official-notice verification; methods/provenance references.

Inappropriate without separate data: predicting initial sales-contract ratio or PF losses; interpreting a missing follow-up as evidence of full sell-out; extrapolating to all Korean projects; inferring causality; inferring buyer withdrawals or actual vacant units.

## Evidence and reuse limitations
- Matching rule documented as normalized complex name + exact supply address + later notice date. False matches, renamed complexes and missed notices may affect findings.
- First announcement near cutoff has less time to accrue observed follow-up events.
- Event and competition fields are defined at different granularity; the published dataset contains project-level aggregates, not buyer-level applications or executed sales.
- Individual official source URLs and dates must be checked before making current claims; public records may be revised.

## Domain-authority outcome assessment
This note provides a practical source-to-variable use map for researchers and links the canonical AptToSell study. It **does not prove** improved domain authority, backlinks, citation count, or search ranking. Monitor independent citations and references separately; do not issue a new DOI for this documentation audit.

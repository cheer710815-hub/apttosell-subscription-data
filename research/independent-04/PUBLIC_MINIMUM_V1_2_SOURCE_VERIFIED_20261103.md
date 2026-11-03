# Independent Study 04 — Minimum aggregate dataset v1.2 verification (2026-11-03)

**Status:** CANDIDATE, not deposited. No DOI. ZIP not uploaded to repository.

## Material improvement
The eight numerator/denominator/rate triples in `aggregate_rates.csv` were independently re-extracted from original archived MOLIT Seoul sales CSV snapshots and matched the previous candidate **8/8**; the counts are no longer merely reconstructed from reported rounded percentages.

### Input datasets
- 2025 source: `아파트(매매)_실거래가_20261031113607.csv` — 83,782 raw rows; non-cancelled, non-public-buyer, positive-price eligible 76,275.
- 2026 source: `아파트(매매)_실거래가_20261102095954(1).csv` — 56,338 raw rows; eligible 53,628. 2026 is partial-year through Nov 2.

Both files remain **internal** and are not part of the public-minimum package. Original file SHA-256 and each source-derived numerator and denominator are recorded in the candidate's `SOURCE_COUNT_VERIFICATION.json`.

## Candidate ZIP
`Study04_Public_Minimal_Dataset_v1_2_SOURCE_VERIFIED_CANDIDATE_20261103.zip`
SHA-256: `9aaa637c13df91392f18d7cf5c41699c07d3f1bacddf467f574716d2838034c2`.
Contains 8 files; CRC, manifest SHA-256, and aggregate validator passed.

## Limitations / release blockers
- This release candidate publishes high-level aggregate results, **not** source-level reproducibility or the detailed strata needed to regenerate the 2025 matched bootstrap.
- Original 2025/2026 snapshot-level analyses have separately passed execution-based audits, but not all potential later corrections/reports were investigated.
- Author-approved creator name is **missing**; no name is guessed from account profile.
- License for derivatives and public disclosure approval **not finalized**.
- Independent 2024 validation still unfinished. This can be a limitation rather than an absolute deposit blocker if the final research scope is explicitly restricted.
- Zenodo account currently restricted; no deposit/DOI before restoration and final authorization.

# Official no-priority API batch result audit — 2026-10-20

## Supplied execution reports
User supplied `api_request_status.csv` (18 request records; nine `getRemndrLttotPblancDetail`, nine `getRemndrLttotPblancMdl`) and `type_verification.csv` (16 selected type rows). All 18 request rows have status `OK`. All 16 selected type rows have `API_COUNT_MATCH` and a nonempty numeric `api_units` field copied from API `SUPLY_HSHLDCO`. The sum equals **220**, matching the existing selected first-round study inventory.

| Round-one notice | Project | Selected API-matched units |
|---|---|---:|
| 2026910144 | Elif Seongseong 1BL | 126 |
| 2026910207 | Songdo Granterre G5-11 | 38 |
| 2026910204 | Songdo Granterre G5-3 | 22 |
| 2026910239 | The Sharp Tricent | 21 |
| 2026910249 | Sejong Umi Lynn Center Park | 5 |
| 2026910169 | Summit The Hill | 3 |
| 2026910121 | La Classe Xi The Pine | 2 |
| 2026910171 | Metrocity Jasan Desian | 2 |
| 2026910214 | D'Fine Artia | 1 |
| **Total** | | **220** |

## Source and verification levels
- The two CSV reports were read directly from the user upload; these results are a **report-based audit** of the previously approved-key API collector. Raw response JSON has not been uploaded in this turn, so stored SHA-256 strings in the status CSV have **NOT independently been recalculated**, and the official API was NOT directly re-queried in this audit.
- All 9 notice classifications in the type report read `무순위`, not `임의공급`.
- All 16 `pdf_status` fields are `PDF_MISSING`. Thus this audit adds **0** units to the first-round **primary-PDF-verified** cohort.
- Prior original-PDF checks remain 146 units; combined provisional cohort is 366 units, with 220 units newly matched to official first-round API report. Retain 146/366 original-PDF verification, not 366/366.
- The separate initial local priority-one competition API audit is preserved. First-round counts are *offered units*; this dataset cannot measure cancellations or actual uncontracted rates.

## Output
See [master v4](./28-TYPE-EVIDENCE-MASTER-v4-API-BATCH-2026-10-20.csv) for all 28 initial models, the 25 eligible models, separate round-one API count verification and original-PDF verification. The preceding v3 dataset has not been overwritten.

Next evidence gate: original first-round PDF bytes (9 files), and preferably original API JSON files for independent SHA-256 and payload verification. No website publishing or DOI issuance approved.

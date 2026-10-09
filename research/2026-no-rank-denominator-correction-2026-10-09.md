# Seoul seven-case denominator correction — 2026-10-09

**Status: VERIFIED CROSS-DATASET AUDIT; no new DOI, no WordPress publication.**

The existing `datasets/seoul-high-competition-unsold-2026/apttosell-seoul-high-competition-unsold-cases-2026-v1.0.csv` column `initial_general_sale_total` contains **initial total supplied units**, not initial general-supply units, in all seven rows. Cross-checked each case by `HOUSE_MANAGE_NO` against AptToSell's original 196-project first-priority source table and original official `TOT_SUPLY_HSHLDCO` values.

| Project | Initial total supply | Initial general supply | First no-rank units | No-rank / total supply | No-rank / general supply (reference only) |
|---|---:|---:|---:|---:|---:|
| 래미안 엘라비네 | 272 | 137 | 56 | 20.59% | 40.88% |
| 라클라체자이드파인 | 369 | 180 | 2 | 0.54% | 1.11% |
| 아크로 리버스카이 | 285 | 132 | 3 | 1.05% | 2.27% |
| 써밋 더힐 | 432 | 211 | 3 | 0.69% | 1.42% |
| 장위 푸르지오 마크원 | 1032 | 510 | 39 | 3.78% | 7.65% |
| 드파인 아르티아 | 171 | 87 | 15 | 8.77% | 17.24% |
| 충정로역자이르네 | 186 | 84 | 35 | 18.82% | 41.67% |
| **TOTAL** | **2747** | **1341** | **153** | **5.57%** | **11.41%** |

**Correction:** The existing 5.57% number is the first no-rank units / initial **total** supply, NOT first no-rank units / initial **general** supply. The 11.41% denominator comparison is not a cancellation or contract-abandonment rate. The case series is not representative of Korea. This note does not silently modify or overwrite frozen v1.0 files; they require versioned errata.

Separate original first-priority analysis: 196 projects, 1,153 types, 523 types with <1:1, and 27 of 101 projects with project-level >=1:1 contain at least one <1:1 type. None of these national first-priority results establishes the nationwide no-rank unit share. The national official no-rank type-unit event table remains unavailable, so no nationwide no-rank percentage is reported.

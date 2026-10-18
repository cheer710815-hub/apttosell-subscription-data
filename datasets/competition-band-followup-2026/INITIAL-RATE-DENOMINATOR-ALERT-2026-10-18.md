# Initial first-priority competition-rate definition alert

Date: 2026-10-18. Status: REQUIRES DATASET-WIDE RECOMPUTATION.

## Verified discrepancy in indexed results

Define Artia (initial notice 2026000241), type 084.0000B, initial general supply 24 units:
- Existing AptToSell DDFS type-riskset: 289 applicants / 24 = 12.0417:1. This sums 232 local + 57 other-region applications.
- Indexed ApplyHome-derived result table reports local-first-priority rate 232 / 24 = 9.67:1.
- Therefore this row is above 10 under combined-region rate but below 10 under local-only rate.
- First no-priority notice 2026910214 supplied 9 units of this type; notice was previously PRIMARY_VERIFIED.
- The research MUST declare whether the >=10 threshold uses all-region 1st-priority applications or local-only official rate, and must not compare them interchangeably.

## Another case

Define Artia type 084.8554A: 81 local applications / 5 general-supply units = 16.2:1, so threshold remains >=10 under either definition.

## Sources

- Existing repository: datasets/ddfs-national-type-riskset-2026/apttosell-ddfs-national-type-riskset-2026-v1.0.csv
- Indexed result breakdown: https://apt.heymingky.com/danji/%EB%93%9C%ED%8C%8C%EC%9D%B8-%EC%95%84%EB%A5%B4%ED%8B%B0%EC%95%84-2026000241/
- Official followup notice: https://altia.skdefine.com/data/gongo_mu.pdf

Do not silently change the existing 28-row candidate file. Recalculate the entire cohort under both explicitly labeled definitions before claiming the number of >=10:1 types and units. No new official first-priority result table was directly fetched in this note.

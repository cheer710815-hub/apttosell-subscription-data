# Independent Study 04: 2024 Seoul source-acquisition gate (2026-11-02)

Status: **HOLD — source CSV and final 2025 v3 package not in current verified workspace.** No 2024 statistical results have been calculated.

## Verified official acquisition route
- MOLIT transaction download portal: https://rt.molit.go.kr/pt/xls/xls.do?mobileAt=
- Public-data catalog: https://www.data.go.kr/data/3050988/fileData.do
- Portal confirms apartment / sales / Seoul / contract-date downloads as CSV or Excel, with up to one-year date window for province-level queries.
- The site states contract-date transactions may change with later reports, amendments or cancellations and cautions against presenting them as official report-date statistics.

## One-year holdout extraction settings
- Property: 아파트
- Type: 매매
- Contract dates: 2024-01-01 — 2024-12-31
- Province: 서울특별시; district, neighborhood, apartment, area and price: ALL
- Format: CSV
- Save intact, without opening and re-saving in Excel.
- Record downloaded filename, size, SHA-256, download timestamp and header/preamble rows.

## Do not execute prematurely
The initial 2025 pilot report and a separate public-buyer direct-sale script refer to different snapshots and cohorts. They are **not** valid substitutes for the final v3 price-heaping matching algorithm. Holdout analysis must use its *actual* original source, code, exclusions and matched-stratum weight specification. Confirm that 2024 was not used to tune the rules, or relabel it sensitivity analysis rather than a strict external holdout.

## Pending inputs
1. Final v3 release-gate and matched analysis archive / code.
2. Official 2024 Seoul apartment sale CSV acquired with above settings.
3. Source schema and exact price/cancellation/transaction-type/buyer fields.

Zenodo DOI creation blocked while account is restricted; no repository publication claim for data/code until audited.

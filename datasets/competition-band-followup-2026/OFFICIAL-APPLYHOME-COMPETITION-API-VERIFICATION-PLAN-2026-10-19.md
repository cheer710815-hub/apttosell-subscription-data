# Official ApplyHome competition API verification protocol — 2026-10-19

## Official sources confirmed
- Korea Real Estate Board / public data portal competition API: https://www.data.go.kr/data/15098905/openapi.do
- Endpoint: GET /ApplyhomeInfoCmpetRtSvc/v1/getAPTLttotPblancCmpet
- Official supply/type lookup API: https://www.data.go.kr/data/15098547/openapi.do
- Type endpoint: GET /ApplyhomeInfoDetailSvc/v1/getAPTLttotPblancMdl
- Separate no-priority and optional supply endpoints must not be conflated.

## Required audit
1. Authenticate with a valid public-data service key. No service key was available in this step; **no live API data rows have been retrieved**.
2. Fetch original first-priority competition results for initial notice IDs G5-3 2026000165 and G5-5 2026000167.
3. Match exact house management number, type code, priority rank, and region (해당지역 versus 기타지역).
4. Save raw response with retrieval date and immutable checksum, retaining all official field names.
5. Confirm G5-3 084.2300K secondary-reported local 23.86:1 and 118.2300K 11.59:1, and G5-5 118.2300K secondary-reported local 9.37:1 versus other-region 11.65:1.
6. If the API disagrees with secondary sources, do not silently overwrite; document source/date/field differences and reconcile with the final 청약홈 competition table. Public data portal notes that bank processing can lead to later revisions.
7. Keep G5-5 12 no-priority units outside provisional >=10:1 local cohort until primary official result supports inclusion.

## Status
OFFICIAL_API_IDENTIFIED_NOT_QUERIED. No official original competition result was retrieved. Current 25-type/366-unit cohort remains provisional and unchanged. Do not publish or issue DOI on this evidence alone.

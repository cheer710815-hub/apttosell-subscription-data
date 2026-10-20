# Independent raw JSON recheck: nine first-round no-priority announcements (2026-10-20)

## Evidence received
User-supplied **AptToSell_9_evidence_bundle.zip** containing **26 files**, of which **18** are official-API response JSON files (nine notice-detail payloads and nine housing-type payloads). Submitted batch metadata also includes **16 selected housing-type entries**, and no original PDF files.

## Independent verification procedure and observed result
- Opened all 18 JSON entries directly from ZIP and computed Python SHA-256 from each original archive member's raw bytes.
- Compared each computed digest with both reported_sha256 and calculated_sha256 columns from supplied results/raw_sha256_verification.csv: **18 of 18 identical**.
- Parsed all 18 JSON payloads successfully; API data-row lengths match recorded row_count for all 18.
- For 16 selected housing types, independently matched stripped HOUSE_TY to the expected type for its first-round notice; each matched exactly one API model row. Compared SUPLY_HSHLDCO directly with expected_units and raw_api_units: **16 of 16 identical**.
- Sum of 16 eligible model counts: **220 first-round offered units**. Mismatch/error count: **0**.
- PDF files in archive: **0**. Therefore zero additional first-round primary-PDF-verified units; prior first-round PDF verification remains 146 units, and the study's 366 units remain the historical combined cohort total.
- The current check validates identity of submitted raw bytes with submitted hashes and consistency of supplied payloads with study targets. It does not independently verify against a freshly downloaded response from the live API service, or certify absence of credentials in sources outside this archive.

## Nine eligible first-round notice totals
| Round-one notice | Selected types | Matched units |
|---|---:|---:|
| 2026910144 | 2 | 126 |
| 2026910207 | 3 | 38 |
| 2026910204 | 2 | 22 |
| 2026910239 | 1 | 21 |
| 2026910249 | 3 | 5 |
| 2026910169 | 1 | 3 |
| 2026910121 | 2 | 2 |
| 2026910171 | 1 | 2 |
| 2026910214 | 1 | 1 |
| **Total** | **16** | **220** |

## GitHub integration
[Master v5](./28-TYPE-EVIDENCE-MASTER-v5-RAW-JSON-VERIFIED-2026-10-20.csv) updates evidence-grading for these 16 model rows from user batch report to independently audited raw JSON. Historical v4 is retained. Initial local-first-priority rate audit (25 eligible types) is unchanged. Primary PDF status fields remain separate; none upgraded.

The 220 units are first no-priority *offered inventory*, not observed canceled contracts nor measured noncontract rates. No website publication or DOI. Raw ZIP was **not** posted publicly as part of this audit.

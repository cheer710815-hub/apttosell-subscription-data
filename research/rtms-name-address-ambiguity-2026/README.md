# Seoul apartment name–parcel ambiguity audit (Stage 0, 2026-11-05)

Research ID: `ARHRN-RTMS-NAME-ADDRESS-COLLISION-20261105`

## Scope and result

We analyzed apartment sale transaction rows from the Republic of Korea Ministry of Land, Infrastructure and Transport (MOLIT) RTMS public-download CSV, after excluding rows marked as canceled. The 2025 file contains 77,361 included Seoul rows, while the January–October 2026 snapshot contains 54,657 included rows.

| Join-key proxy | 2025 ambiguous-name rows / all | 2026 Jan–Oct ambiguous-name rows / all |
|---|---:|---:|
| Apartment name only | 15,766 / 77,361 (20.38%) | 11,795 / 54,657 (21.58%) |
| District and apartment name | 4,391 / 77,361 (5.68%) | 3,090 / 54,657 (5.65%) |
| Legal-dong address and apartment name | 62 / 77,361 (0.08%) | 70 / 54,657 (0.13%) |

**IMPORTANT: These figures measure potential ambiguity, NOT an observed erroneous linkage rate.** The same physical complex can span multiple land parcels. A different parcel address alone does not establish a different physical complex. Conversely, complex-name variants can conceal different match problems. We did not actually join this sample to K-apt or the building register, and causal interpretation is not warranted. 2025 is a full year; 2026 covers ten months and is a download-time snapshot. Do not interpret their differences as an annual market trend.

The percentage denominator is transaction *rows*, not unique buildings or independently identified households. RTMS transaction data should not be presented as Korea's approved transaction-count statistics.

## Source, provenance, and reproducibility

- Primary source: MOLIT RTMS public downloads: https://rt.molit.go.kr/pt/xls/xls.do
- Files were downloaded on different dates. They are not matched-date snapshots.
- 2025 CSV SHA-256: `a0d3df04e403f8dc2c2b49b512e763850f050dd65502854b2961efbf41a8372c`
- 2026 Jan–Oct CSV SHA-256: `6d863e491a54598ff1a3337d569d42075928bbb28f4131c0716f72db92567c32`
- Download official RTMS CSVs yourself and run the included `analyze.py` with Python 3 and pandas. The publisher does **not** redistribute underlying transaction-level RTMS rows.
- `ambiguity_summary.csv` is a derived, six-row numerical summary.
- Python dependencies: `pandas>=2.0` (Python 3.10+ recommended).

Example:

```bash
python analyze.py --year2025 /path/to/2025_rtms.csv --year2026 /path/to/2026_rtms.csv --output results
```

The file reader expects CP949 encoding, 15 metadata/header lines, and the Korean RTMS fields `해제사유발생일`, `시군구`, `번지`, `단지명`.

## Literature and novelty limitations

Existing work already documents apartment entity matching using standardized addresses and building registers. This Stage 0 audit is a limited **descriptive reproducibility example**, not a novel entity-resolution algorithm, verified false-match rate, or peer-reviewed article. A stronger study would ground ambiguous parcels against official complex identifiers and perform case-level manual adjudication.

Related prior work:
- https://doi.org/10.3390/jrfm19070543 (RTMS–K-apt complex mapping in Korean housing price-index research).
- https://www.data.go.kr/data/15106861/fileData.do (Korea Real Estate Board official complex and parcel identifiers).

## Publication and citation status

This repository contains a preliminary method and derived aggregate, not a citable DOI dataset. **No DOI has been registered or reserved for this study**, and publication on GitHub does not prove natural backlinks or citations. This artifact is provided for transparent peer inspection and subsequent validation.

AptToSell and Resimanor are the project's intended editorial applications, but the work is not evidence of changes in their domain authority. The repo contains no raw transaction CSVs. The original government's source terms govern those source files; this README and original audit code are available under repository terms, with no third-party source-data sublicense implied.

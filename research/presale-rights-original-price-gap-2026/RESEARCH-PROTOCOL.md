# N01 — Korean Apartment Presale-Rights Transaction vs Original Offering Price (research protocol)

**Status:** data collection in progress; NO transaction-level matches, statistics, DOI, or published findings are claimed yet.
**Research objective:** Link publicly reported apartment presale-rights resale transactions to the initial advertised offering prices of matching housing types, creating a reproducible dataset. Separate gross transaction price differences from seller net premiums.

## Official source registers
1. MOLIT Apartment Presale-Rights Resale Transaction API: https://www.data.go.kr/data/15126471/openapi.do (region law-dong 5-digit code + YYYYMM, XML; API access key required).
2. Korea Real Estate Board ApplyHome Offering Details API: https://www.data.go.kr/data/15098547/openapi.do (original offering details, including housing model/type pricing).

## Inclusion & linkage
- Filter to **apartment presale-rights resale** transactions, not conventional completed-apartment sales and not reconstructed occupancy-right transfers unless separately flagged.
- Match region, project name, project/address, exclusive area, original offering announcement date, and transaction date.
- Where exact A/B/C housing-type designation is absent in resale records, do NOT invent a type-level match. Use ambiguity status and exclude from exact type-level comparison.
- Compare an original **published price interval** when an offering price varies by floor or unit; treat a point estimate as exact only when unit-level offering price is supported.
- Resale reported transaction amount may incorporate financing/option rights or reporting-specific adjustments; it is NOT automatically the seller's net gain, premium, or capital gain.
- Preserve amended/cancelled trade flags if offered by API; state the observation and retrieval dates.
- De-identify unit information and avoid personal data.

## Planned deliverables (after retrieval)
- transaction_project_candidates.csv (raw-to-project linkage provenance)
- matched_transactions.csv (ONLY validated joins)
- excluded_ambiguous_cases.csv
- project_summary.csv
- DATA-DICTIONARY.md, METHODOLOGY.md, QA_REPORT.md, CITATION.cff and versioned release notes.

## Publication rule
First publish reproducible validated data on GitHub. Submit a frozen dataset to one primary scholarly repository and report its exact DOI; link secondary repositories to primary DOI. No press outreach until data are independently reviewable. Do not claim external approval or peer review merely from repository publication.

## Jinju pilot: offering-price source triage (2026-10-18)

**Verification stage:** Secondary-source discovery only; *not* official notice verification and *not* transaction-level matching.

Candidate project: **Forena Hillstate Jinju**; initial offering notice reportedly dated 2026-08-14, ApplyHome project identifier **2026000383**. Third-party notice summaries report the following original price ranges (KRW). These are pointers for official-document checking, **not validated inputs** for premiums or resale-price gap statistics.

| Housing type | Secondary-source reported price range (KRW) |
| --- | ---: |
| 59A | 367,000,000–420,000,000 |
| 59B | 363,000,000–413,000,000 |
| 72A | 429,000,000–490,000,000 |
| 72B | 424,000,000–486,000,000 |
| 84A | 509,000,000–577,000,000 |
| 84B | 502,000,000–571,000,000 |

Discovery references, **non-authoritative**:
- https://zipgebu.com/explore/2026000383
- https://apttoyou.kr/forenahillstate/price

Before any transaction-level comparison, retrieve and archive the official initial notice PDF and every applicable correction, capture the explicit A/B type and floor-band or unit-level supply price, and verify the MOLIT reported sale amount definition. If a resale transaction has only a rounded exclusive area and cannot be resolved to an A/B type and floor, mark **AMBIGUOUS_TYPE_OR_FLOOR** instead of selecting an arbitrary single price. The previously noted Jinju pilot cohort of 56 is a candidate set, not 56 validated price joins. No gap, resale premium, return, or profit findings have been released.

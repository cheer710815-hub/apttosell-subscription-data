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

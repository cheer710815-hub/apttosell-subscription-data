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

## Correction-notice verification checkpoint (2026-10-18)

- **Project identifier:** ApplyHome 2026000383 (Forena Hillstate Jinju).
- **Initial announcement:** 2026-08-14. A public secondary research index reports a **corrected notice dated 2026-08-20 (79 pages)**. Correction status and its impact on price schedules require direct verification against the official revised PDF; do not presume prices changed.
- **Official government corroboration:** Gyeongnam Regional SMEs and Startups Office's institutional-allocation notice anticipated the 2026-08-14 launch, but its attachment is *not* a replacement for the initial/revised general offering-price schedule: https://www.mss.go.kr/site/gyeongnam/ex/bbs/View.do?bcIdx=1069781&cbIdx=255
- **Secondary correction reference (not authoritative):** https://www.salzip.co.kr/c/2026000383/
- **Secondary housing-type and highest-price register (not authoritative):** https://www.psust.com/abyg_main/apt_byg_type1_view?HOUSE_MANAGE_NO=2026000383&PBLANC_NO=2026000383&SUBSCRPT_AREA_CODE=621&page=1&type=

**QA gate:** archive both official notice editions; diff the housing-type/floor/unit price schedules, supply scope, effective dates, exclusions and additions. If only max prices are obtainable, use them for cross-checking, **not** as transaction-specific comparison baselines. The 56 candidate transactions remain unvalidated until each has a defensible exact type/floor match and resale amount definition.

## Model-code crosswalk and 59A price-band candidate (2026-10-18)

The following **secondary-transcription candidate table** is for matching design only; no official initial/corrected notice PDF was recovered or compared in this pass. Cross-check all rows against the original and 2026-08-20 correction before promoting any figure to a verified input.

| Notice housing-type code | Short label | ApplyHome model no. | Published max KRW (secondary) |
| --- | --- | --- | ---: |
| 059.6771A | 59A | 01 | 420000000 |
| 059.7292B | 59B | 02 | 413000000 |
| 072.8120A | 72A | 03 | 490000000 |
| 072.9569B | 72B | 04 | 486000000 |
| 084.9944A | 84A | 05 | 577000000 |
| 084.9331B | 84B | 06 | 571000000 |

### 59A provisional price bands (unverified transcription)

The publicly reproduced 59A schedule lists: 1F KRW 367m, 2F 377m, 3F 387m, 4F 397m, 5–9F 408m, 10–19F 412m, 20–29F 416m, 35F 420m. **This is not a continuous floor table**: omitted floors and qualifying building/unit columns must be reconciled against the actual notice. Do not interpolate omitted floors or apply this schedule to other types.

Secondary sources: https://www.psust.com/abyg_main/apt_byg_type1_view?HOUSE_MANAGE_NO=2026000383&PBLANC_NO=2026000383&SUBSCRPT_AREA_CODE=621&page=1&type= ; https://zipgebu.com/explore/2026000383 ; https://www.salzip.co.kr/c/2026000383/ .

**Mandatory next evidence:** acquire both source PDFs (or an official full-text table), store provenance and document hashes, identify the corrected paragraphs and effective version, and compare the MOLIT transaction date against eligibility. Candidate count (56) is not validation count (0 confirmed). No premium/gap outputs are authorized.

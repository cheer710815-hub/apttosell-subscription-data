# N01 authenticated pilot: Jinju, September 2026

**Status: internal QA note, not a public presale premium or price-gap finding.**
Source: MOLIT SilvTrade authenticated API, locality 48170, month 202609.
Collection timestamp (UTC): 2026-10-19T06:25:20.053165+00:00.
Source raw CSV SHA-256: `8794f8e5857507c1e745dec29863a1119135867d813c6c6e73e1a145e39f9b89`. SHA matches the submitted manifest.

| Stage | Records |
| --- | ---: |
| API raw records / totalCount | 26 / 26 |
| Brokered trades (dealingGbn = 중개거래) | 26 |
| Private seller and private buyer | 26 |
| Cancellation-marked rows (cdealType = O) | 1 |
| Rows without cancellation marker | 25 |
| Identical CSV rows within the non-cancelled subset | 1 extra copy |
| Unique **row contents** among non-cancelled subset | 24 |

Projects: Forena Hillstate Jinju 23 raw records (22 without cancellation indicator); Honors Welga Jinju 3 raw records (3 without cancellation indicator). All 26 `ownershipGbn` fields are blank. This is consistent with the guide's note that occupancy rights are marked `입`, but **must not be taken as independent verified identification of every row**.

**Scientific caution:** An identical pair of reported rows cannot automatically be interpreted as a duplicated transaction without an official unique filing identifier. Retain all original 26 rows, report both 25 non-cancelled rows and 24 unique row contents, and postpone deduplication policy until source/reporting practices have been verified.

No transaction-level data, addresses, or prices are included in this public QA summary. The raw file remains with the user. No overlap with N01-AGG's nationwide 980 observations has been verified. The September pilot alone cannot reproduce 980 nor prove the original matching-candidate count of 115.

Next: review official cancellation semantics, verify whether blank ownership means presale rights throughout, establish duplicate policy and reproduce the exact filtering cohort across all region/month pulls before any gap calculation.

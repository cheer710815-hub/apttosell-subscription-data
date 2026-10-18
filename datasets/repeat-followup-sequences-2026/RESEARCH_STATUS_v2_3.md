# RFSEQ 2026 — Repeat Follow-up Notice Sequences: verified research status (v2.3)

**Historical research snapshot:** 2026-10-15 (v2.3). **Publication update:** 2026-10-18 — a narrower RFSEQ v2.6 notice-interval dataset has been published on Zenodo. The dwelling-level research below is historical work, not a validated claim of the v2.6 release.

## Cohort and methodology
- Existing AptToSell *Competition vs Followup 2026 v1.0* workbook: 103 matched projects, 141 follow-up notice events.
- Repeat-notice subset: **22 projects**, **60 notice records**, **59 distinct project-date observations**.
- Notice-count distribution: 12 projects with two notices; six with three; two with four; two with five.
- **37 positive consecutive date gaps**, median **40 days**, range **6–130 days**. One pair of notices on the same day in Yongin is treated as parallel, not an ordered interval.
- Official ApplyHome major-information pages: **60/60** announcement dates and advertised supply counts independently checked against the research manifest.

## Dwelling-level verification
- **21/22 projects** have been compared at the dwelling identifier level for their published repeat notices.
- **1/22 source limitation:** Uijeongbu Station Central I-Park first notice does not enumerate individual dwelling identifiers, so the initial-to-next overlap cannot be determined from the official first notice.
- A later notice's “new” units mean **not listed in the comparison notice**, not newly built apartments, newly cancelled contracts, or newly unsold units.
- Forena The Sharp Incheon City Hall: 466→10→5; neither later set reappears in the preceding notice.
- Okjeong Central Station Daebang D'etre: 379→73 in the first observed transition; the later 73 include **12 dwelling identifiers** already in the 379 and **61 units from housing types absent in the first notice**.
- These are descriptive notice-to-notice observations, not a contract conversion or absorption study.

## Release controls
- Related but distinct existing registry: [AptToSell Follow-Up Event Registry 2026](https://doi.org/10.5281/zenodo.23176906).
- **RFSEQ v2.6 published DOI:** [10.5281/zenodo.23433246](https://doi.org/10.5281/zenodo.23433246). **All-versions DOI:** [10.5281/zenodo.23433245](https://doi.org/10.5281/zenodo.23433245). The registry DOI above belongs to a separate dataset.
- The research ledger has a dedicated RFSEQ row and a reservation entry; the GitHub preliminary note was corrected in commit `34d5d5bae03d79a284ec1ef1e1e07b36dee1bb65`.
- Source labels `UNSOLD` and `OPTIONAL` are workbook classifications; legally precise `무순위(사후)` vs `임의공급` should be taken from each official PDF.
- The original ApplyHome PDFs remain copyrighted third-party sources; cite their URLs, do not redistribute the PDFs without checking permissions.
- A reproducible public dataset release requires complete machine-readable event records, unit-audit evidence, a validation matrix, a dictionary, and a license review.

**Publication status (updated 2026-10-18):** RFSEQ v2.6 is published on Zenodo at https://zenodo.org/records/23433246. The released dataset is limited to notice chronology and interval statistics (22 projects, 60 notice events, 59 distinct project-date observations, 37 positive consecutive intervals, median 40 days, range 6–130). Workbook labels `UNSOLD` and `OPTIONAL` are not independently verified legal categories; dwelling-level reappearance and contract/unsold outcomes are not established by v2.6. This GitHub document does not evidence Figshare, Mendeley, or RePEc submission.

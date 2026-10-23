# N01 cross-platform presale-versus-occupancy label audit, 2026-10-23

The locally inspected primary government SilvTrade HWP says ownershipGbn shows `입` **for occupancy-right records only**. The three private source rows from uploaded batch 7 have `ownershipGbn` blank, so according to the technical mapping their blank flags are **consistent with presale rights**; this does not prove error-free government classification.

Previously consulted third-party ndsts display labeled the exact trade date, rounded area, floor as `입주권` (see N01_ASPEN_BOKDAE_GATE_20261022.md). An independent third-party derivative AptLens now displays the same matching trades as `분양권`:
- Bokdae Xi The Sky: 2026-09-03 / approx 104sqm / 3F, and 2026-09-14 / approx 104sqm / 36F https://aptlens.co.kr/c/2babab3uu2hvv?type=presale
- Harrington Place Technopolis: 2026-09-12 / approx 85sqm / 23F https://aptlens.co.kr/c/3ocea5gepujfn?type=presale

Both third-party services use rounded display area, and neither establishes the official `ownershipGbn` classification with unmodified input XML. A second derivative is **not** a second independent original reporting source. Thus rephrase risk as `THIRD_PARTY_CLASSIFICATION_LABEL_DISAGREEMENT`, not `official occupancy-right suspicion`, and preserve original primary `ownershipGbn` value, blank. Default technical-doc mapping considers blank consistent with presale status, but check official data owner or identical source XML mapping before certified classification.

Bokdae 103.9937sqm / 3F and / 36F retain original official-lot price-tier reference candidates (2 of 28) with classification warning, not premium/gap estimates. Harrington 84.9707sqm / 23F official subtype 84C1 identified but still outside 28 notice-price references; optional next step is verify its initial price tier only (no spread claims). Separate Bokdae 84.9977sqm 41F with source lot 3411 still blocked on cadastral lot, regardless of ownership label.

Overall original 824, provisional screen 606, source-reference 28 (24 unique schedule prices and 4 building/line intervals), final financially comparable 0. No new DOI. Agency dealAmount response remains open.

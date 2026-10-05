# Primary Verification Progress — 2026-10-05

## Queue status

- Total first-event rows: **103**
- Evidence-reviewed rows: **103 / 103**
- Remaining discovery `TODO_PRIMARY_SOURCE`: **0**
- Numeric first follow-up notice IDs recovered: **103 / 103**
- `PRIMARY_VERIFIED`: **1**
- `ID_CORROBORATED_SECONDARY`: **102**
- `SECONDARY_CORROBORATED`: **0**

## Discovery milestone

The first-pass notice-ID discovery is now **complete for all 103 first-event rows**.

Every project in the first-event cohort now has a numeric first follow-up notice ID.

This does not mean every row is primary-source verified. Most IDs were recovered from reliable public reproductions of ApplyHome data, with official project-domain cross-checks where available.

## Primary-source status

The direct ApplyHome detail endpoint is not accessible through the current web tool environment. Therefore the promotion layer remains intentionally conservative.

One event is already `PRIMARY_VERIFIED` through an official project-hosted recruitment notice artifact:

- **포레나더샵 인천시청역** — notice ID `2026910063`.

## Next layer

The discovery phase is finished. The remaining task is direct-official-artifact promotion:

1. inspect original ApplyHome/LH or project-hosted official notice artifact;
2. verify notice ID, announcement date, subtype and supply count directly;
3. promote only directly supported rows to `PRIMARY_VERIFIED`.

No new DOI should be minted until a clearly bounded primary-verified cohort is available.

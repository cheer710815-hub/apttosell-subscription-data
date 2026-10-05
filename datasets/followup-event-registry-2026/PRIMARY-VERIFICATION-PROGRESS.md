# Primary Verification Progress — 2026-10-05

## Queue status

- Total first-event rows: **103**
- Evidence-reviewed rows: **103 / 103**
- Remaining `TODO_PRIMARY_SOURCE`: **0**
- Numeric follow-up notice IDs recovered: **95**
- `PRIMARY_VERIFIED`: **1**
- `ID_CORROBORATED_SECONDARY`: **94**
- `SECONDARY_CORROBORATED`: **8**

## Milestone

The initial 103-row evidence review queue is now **fully screened**. No row remains in `TODO_PRIMARY_SOURCE`.

This does **not** mean all 103 events are primary-source verified. Most rows retain a secondary/corroborated status because the original ApplyHome detail page or an official notice artifact has not yet been directly preserved.

## Current primary-verified example

- **포레나더샵 인천시청역** — official project-hosted no-priority recruitment notice PDF directly verified, notice ID `2026910063`.

## Notice-ID coverage

A numeric follow-up notice ID has been recovered for **95 of 103** first-event rows.

Rows without a recovered numeric ID remain evidence-corroborated only and must not be silently assigned an identifier.

## Next verification layer

The next pass is no longer a discovery queue. It is a **primary-source promotion queue**:

1. recover official ApplyHome/LH notice artifacts where accessible;
2. archive or link the official artifact;
3. verify subtype, date and supply count directly;
4. promote only those rows from secondary status to `PRIMARY_VERIFIED`.

No new DOI should be minted until a clearly bounded primary-verified cohort is available.

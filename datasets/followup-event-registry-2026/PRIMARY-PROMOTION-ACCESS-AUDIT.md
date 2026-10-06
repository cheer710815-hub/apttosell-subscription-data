# Primary Promotion Access Audit — 2026-10-06

## Scope

The full first-event registry has already completed official-source linking.

## Current result

- First-event rows: **103**
- Numeric notice IDs: **103 / 103**
- Canonical ApplyHome detail links: **103 / 103**
- `PRIMARY_VERIFIED`: **13**
- `ID_CORROBORATED_SECONDARY`: **90**

## Important distinction

Earlier work treated direct inspection of a project-hosted PDF as if it were required to establish an official source link. That is unnecessarily strict.

The correct structure is:

1. **Official source link** — generated from the recovered notice ID and pointed to ApplyHome.
2. **Evidence grade** — separately records whether the event artifact was directly inspected.

Therefore, the remaining 90 rows are **not missing official source links**. They are simply not direct-primary verified.

## ApplyHome URL pattern

`https://www.applyhome.co.kr/ai/aia/selectAPTLttotPblancDetail.do?houseManageNo={ID}&pblancNo={ID}`

## Next work

Primary promotion should be limited to cases where an official artifact is easy to inspect or materially improves the research asset. It is no longer a blocking task for registry completeness.

# Primary Promotion Access Audit — 2026-10-05

## Scope

All **102 non-primary** first-event rows were audited for promotion readiness.

## Results

- Non-primary rows audited: **102 / 102**
- Rows with numeric first-event notice ID: **102 / 102**
- Rows with deterministic ApplyHome detail URL candidate: **102 / 102**
- Direct ApplyHome detail endpoint accessible in current web tool: **0**
- Already primary-verified outside this queue: **1**

## Tooling blocker

The official ApplyHome detail URL can be constructed from the numeric notice ID using:

`https://www.applyhome.co.kr/ai/aia/selectAPTLttotPblancDetail.do?houseManageNo={ID}&pblancNo={ID}`

The current web environment returns the official ApplyHome detail endpoint as inaccessible. This is a tool-access limitation, not evidence that the official records do not exist.

## Completed work despite the blocker

- all 103 first-event rows evidence-reviewed
- all 103 numeric first-event notice IDs recovered
- official project-site cross-checks added where discoverable
- official ApplyHome candidate URL generated for all 102 promotion candidates
- promotion status frozen as `BLOCKED_DIRECT_PRIMARY_ACCESS` rather than overstating verification

## Important rule

Do not promote third-party API mirrors, search reproductions, or news articles to `PRIMARY_VERIFIED` merely because the numeric identifier is consistent.

Promotion requires direct inspection of an official artifact.

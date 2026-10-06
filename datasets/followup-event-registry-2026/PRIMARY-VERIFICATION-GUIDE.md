# Follow-Up Event Verification Guide

Snapshot: **2026-10-06**

## Current state

- First follow-up events: **103**
- Numeric notice IDs recovered: **103 / 103**
- Canonical official source links: **103 / 103**
- `PRIMARY_VERIFIED`: **13**
- `ID_CORROBORATED_SECONDARY`: **90**

## Canonical source rule

The recovered numeric notice ID is used to construct the official ApplyHome detail URL:

`https://www.applyhome.co.kr/ai/aia/selectAPTLttotPblancDetail.do?houseManageNo={ID}&pblancNo={ID}`

This ApplyHome URL is the default official source link for registry rows.

## Evidence grade is separate from source linking

A working official ApplyHome link does not automatically change a row to `PRIMARY_VERIFIED`.

- `ID_CORROBORATED_SECONDARY`: notice ID and event chronology are corroborated; canonical source points to ApplyHome.
- `PRIMARY_VERIFIED`: the official event artifact/page was directly inspected and event fields were verified.

Project-hosted PDFs are therefore useful for evidence-grade promotion, but are **not required** simply to connect a row to its official source.

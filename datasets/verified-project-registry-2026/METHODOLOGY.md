# Methodology — AptToSell Verified Project Registry 2026

## 1. Purpose

Create one stable project-level identifier that can be reused across AptToSell datasets.

## 2. Unit of observation

One row represents one housing project identity, not one recruitment notice.

A project may have multiple official notice numbers over time, but it should retain one AptToSell project ID unless evidence shows that it is a genuinely different project.

## 3. Identity matching hierarchy

Project identity should be resolved using, in order:

1. official housing management number
2. official project / house name
3. supply address
4. region and district
5. original announcement date
6. project-owner / official notice cross-check

## 4. Duplicate-resolution rule

Two rows should not receive separate AptToSell project IDs merely because:

- a follow-up notice has a different notice number
- residual-unit sales are announced later
- the public-facing project name changes slightly
- punctuation or spacing differs

A new project ID is warranted only when the underlying housing project identity is different.

## 5. Source quality

Target source hierarchy for Version 1.0:

1. ApplyHome / Korea Real Estate Board official public data
2. LH or other public-agency official notice
3. project-owner official notice
4. secondary source only as a discovery pointer

Secondary-only verification is acceptable in this pilot but not for the final public registry.

## 6. Follow-up linkage

`followup_confirmed` means a later follow-up supply event has been confirmed for the same project.

It does not mean:

- cancellation rate
- unsold rate
- contract failure rate

## 7. Version gate

Version 1.0 should be released only after:

- all published rows are re-verified with primary sources
- identifier rules are frozen
- duplicate cases are reviewed
- coverage scope is defined
- a machine-readable data dictionary is finalized


## 8. Field-level verification states

Project identity and competition-result facts are verified separately.

Recommended states:

- `PRIMARY_VERIFIED` — supported by an official recruitment notice, ApplyHome/LH/public-agency record, or project-owner primary document
- `SECONDARY_VERIFIED` — supported by a reliable secondary reproduction or analysis but not yet captured from the primary result source
- `UNRESOLVED` — conflicting or insufficient evidence

A project may be identity-verified while its competition totals remain secondary-verified.

## 9. Pilot primary-source check

For the two current pilot rows, official recruitment documents now support the project identity and initial notice facts. Competition totals still require direct primary-result evidence before Version 1.0.

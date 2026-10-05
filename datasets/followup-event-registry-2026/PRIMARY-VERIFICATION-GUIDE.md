# Primary-Source Verification Queue

Snapshot: **2026-10-05**

This queue operationalizes the next stage of the event registry without changing the frozen pilot schema.

## Queue size

- Projects requiring notice-level primary-source verification: **103**
- Current queue status: `TODO_PRIMARY_SOURCE`
- Priority rule: projects with more recorded follow-up events first, then shorter time-to-first-follow-up

## Verification target

For each project, recover and record:

1. official follow-up notice ID
2. official announcement date
3. official event subtype
4. official source URL or archived official artifact
5. supply count
6. applicant / competition result when applicable
7. primary-source verification date

## Promotion rule

A queue row can move from `TODO_PRIMARY_SOURCE` to `PRIMARY_VERIFIED` only when the official source itself is directly recoverable or an official artifact containing the event fields is preserved.

Secondary mirrors can be used to locate or reconcile an event, but cannot by themselves complete this queue.

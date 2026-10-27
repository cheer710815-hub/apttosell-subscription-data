# N06 integration test case: API contract date vs final corrected notice

**Purpose:** A reusable regression-test scenario for Korean housing subscription schedule services. This document is an implementation aid, **not** an assertion that any particular third-party application has a bug.

**Research dataset:** [N06 Zenodo v1.0](https://doi.org/10.5281/zenodo.23656772) · [N06 scope and methodology](README.md).

## Evidence and scope

The preserved 2026 ApplyHome API snapshot contains 249 housing projects. The N06 study reconciled four date fields per record (996/996 matched against the analysis CSV). **30** projects were additionally checked against official scheduled contract information; **29** matched and **one** differed. The remaining **219** projects were **not** individually checked against final corrected notices.

| Field | Preserved API | Final corrected recruitment notice |
| --- | --- | --- |
| Project | e편한세상 분당 퍼스트빌리지 (성남낙생 A-1) | Same project |
| Housing management ID | `2026820004` | `2026820004` |
| Contract start | `2026-11-07` | `2026-11-04` |
| Contract end | `2026-11-13` | `2026-11-13` |

These are **scheduled** contract dates, not actual contract-execution or payment records. The API date reflects the **preserved research snapshot**, not necessarily the API's live value today.

## Suggested fixture (illustrative, not an official API payload)

```json
{
  "houseManageNo": "2026820004",
  "projectName": "e편한세상 분당 퍼스트빌리지 (성남낙생 A-1)",
  "apiSnapshot": {
    "contractStart": "2026-11-07",
    "contractEnd": "2026-11-13"
  },
  "officialCorrectedNotice": {
    "contractStart": "2026-11-04",
    "contractEnd": "2026-11-13",
    "verificationStatus": "verified_final_corrected_notice"
  }
}
```

**Machine-readable fixture:** [`contract-date-regression.fixture.json`](contract-date-regression.fixture.json) contains the same illustrative values and expected outcomes for use in automated tests. It is not a live API response or a replacement for checking the current final notice.

## Recommended regression assertions

1. Preserve the API snapshot values and their provenance; never silently overwrite source fields.
2. When a final corrected notice is independently verified, show **2026-11-04** as the notice-verified contract start, with its source/status.
3. Retain **2026-11-13** as the end date, which agrees across both sources.
4. For projects without final-notice verification, label dates as **API-based / not individually verified**, not as confirmed final-notice dates.
5. Keep receipt-day notifications distinct from contract dates; the N06 study does not imply users should receive a contract reminder.
6. Do not generalize the one observed mismatch into an overall error rate for all ApplyHome records.

## Optional data model

```ts
type ContractScheduleProvenance = {
  apiSnapshotStart?: string;
  apiSnapshotEnd?: string;
  noticeVerifiedStart?: string;
  noticeVerifiedEnd?: string;
  verificationStatus: 'api_only' | 'verified_final_corrected_notice';
  verifiedAt?: string;
  officialNoticeUrl?: string;
};
```

**Integration note:** The `sj-gates/cheongyak-alarm` repository currently maps `CNTRCT_CNCLS_BGNDE` and `CNTRCT_CNCLS_ENDDE` into contract fields and timeline events in `src/lib/normalize.ts`. This test case is a possible extension for source-aware date handling, not proof of a live UI error.

**Citation:** Kim, Eun (2026). *Apartment Subscription Notice and Contract Schedule Intervals in South Korea: A 249-Project Dataset with 30 Official Notice Verifications (2026)* (v1.0). Zenodo. https://doi.org/10.5281/zenodo.23656772

**Licensing:** See the N06 dataset record and the original public-data provider's terms. No official recruitment notice PDF is redistributed here.

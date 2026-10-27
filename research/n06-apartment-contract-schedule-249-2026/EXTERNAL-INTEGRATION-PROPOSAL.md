# N06 minimal integration proposal for `sj-gates/cheongyak-alarm`

**Status:** independent technical proposal; **not submitted to the upstream repository**. No confirmed production defect is alleged.

## Confirmed upstream code paths

- `src/lib/normalize.ts`: `buildEvents()` constructs a `contract` event from `CNTRCT_CNCLS_BGNDE` and `CNTRCT_CNCLS_ENDDE`.
- `normalizeNotice()` independently maps the same API fields to `Notice.contractStart` and `Notice.contractEnd`.
- `src/lib/types.ts`: `Notice` and `ScheduleEvent` have no verified-final-notice provenance field.
- `package.json` exposes `typecheck` and `lint`, but no dedicated test command.

## Minimal additive change

1. **Keep the existing API mapping unchanged.** Do not hardcode the 2026 research snapshot into live app behavior.
2. Add an optional `contractScheduleVerification` property to `Notice`, for example:

```ts
type ContractScheduleVerification = {
  status: 'verified_final_corrected_notice';
  verifiedStart: string; // YYYY-MM-DD
  verifiedEnd: string;
  officialNoticeUrl: string;
  verifiedAt: string; // ISO timestamp
};
```

3. Introduce a **separate, explicit** function `applyVerifiedContractSchedule(notice, verification)` that:
   - checks the housing management ID and (where available) notice ID before applying a verified record;
   - retains original `contractStart` and `contractEnd` as API-derived fields or snapshots;
   - adds the verification metadata and updates the **display schedule** and the `contract` event together, without modifying receipt or winner events;
   - declines unverified or mismatched records and provides no inferred final-notice status.
4. Render a clear label such as `최종 정정공고 확인` only when a verified notice and source URL are present. Otherwise label contract dates `청약홈 API 기준 (최종 정정공고 개별 미확인)`.
5. Keep **contract dates separate from notification scheduling**; the existing app's notifications are for application/receipt dates.

## Reproducible regression scenario

Use [`contract-date-regression.fixture.json`](contract-date-regression.fixture.json) and [integration test case](INTEGRATION-TEST-CASE.md).

| Assertion | Expected |
| --- | --- |
| Original preserved API start | `2026-11-07` |
| Verified final corrected notice start | `2026-11-04` |
| End date under both sources | `2026-11-13` |
| Display event after explicit verification | starts `2026-11-04`, ends `2026-11-13` |
| API snapshot | unchanged |
| Unverified notices | never marked final-notice verified |
| Receipt notifications | unaffected |

**Important:** The fixture represents a historical preserved API snapshot, **not the current live API**. The N06 study individually checked 30 of 249 projects against official notices; one discrepancy was observed in those 30. It does not establish an overall API error rate.

## Suggested verification before upstream contribution

- Confirm the final corrected notice document and provenance URL are available to the application; do not redistribute the PDF without checking rights.
- Confirm how the app refreshes and caches `Notice` objects and events, so display data cannot become stale or internally inconsistent.
- Add a test runner if the maintainers want executable tests; `package.json` currently does not define `test`.
- Run `npm run typecheck` and `npm run lint` after any code changes.

## Research reference

N06, *Apartment Subscription Notice and Contract Schedule Intervals in South Korea: A 249-Project Dataset with 30 Official Notice Verifications (2026)*. https://doi.org/10.5281/zenodo.23656772

**No upstream issue or pull request has been filed by this proposal.**

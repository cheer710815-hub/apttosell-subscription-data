# Primary Artifact Search Log — 2026-10-05

This log records the direct-official-artifact promotion pass after completion of numeric notice-ID discovery.

## Promotion results

Directly inspected official follow-up notice artifacts currently support **13 primary-verified events**:

1. **포레나더샵 인천시청역** — official project-hosted no-priority recruitment notice PDF, notice ID `2026910063`
2. **아크로 리버스카이** — DL E&C ACRO official project-hosted no-priority recruitment notice PDF, notice ID `2026910194`
3. **청주 푸르지오 씨엘리체** — Daewoo E&C PRUGIO official project-hosted no-priority recruitment notice PDF, notice ID `2026910133`

4. **두산위브 더센트럴 수원** — official project-hosted no-priority notice PDF, notice ID `2026910083`, notice date 2026-04-09, 25 residual units

5. **드파인 아르티아** — official SK DEFINE project-hosted no-priority notice PDF, first-event notice ID `2026910214`, notice date 2026-08-07, 15 residual units. Secondary ID `2026910233` was identified as a later second no-priority event and corrected.

6. **쌍용 더 플래티넘 온수역** — official project-hosted no-priority notice PDF, notice ID `2026910070`, notice date 2026-03-25, 3 residual units.

7-10. **더샵 송도그란테르 G5-11/G5-3/G5-4/G5-5** — official POSCO E&C project-hosted no-priority notice PDFs, notice IDs `2026910207`, `2026910204`, `2026910205`, `2026910206`, all dated 2026-07-30.

11. **의왕역 SK VIEW** — official SK VIEW project-hosted no-priority notice PDF, notice ID `2026910225`, notice date 2026-08-28, 17 residual units.

12-13. **천안 아이파크 시티 6단지 / 5단지** — official project-hosted first no-priority recruitment notice PDFs, notice IDs `2026910074` / `2026910073`, residual units 385 / 334.

## Official-site evidence found but not promoted

Several projects have official project pages that visibly expose a “무순위 모집공고” or equivalent download link, but the underlying artifact could not be directly inspected in the current environment.

Examples include:

- 김해 신문 센트럴 아이파크 — official IPARK site exposes a 무순위 모집공고 link, but the CDN PDF returns access denied in the current tool environment.
- 중앙하이츠 원종역 — official project site exposes a 무순위 입주자 모집공고 section, but the page renders the notice through an image/download control without parseable event fields.
- 풍무역세권 수자인 그라센트 2차 — official project site exposes recruitment-notice files, but a directly inspectable first follow-up artifact was not recovered in this pass.
- 장위 푸르지오 마크원 — official PRUGIO site exposes follow-up contract/notice navigation, but the first-event notice artifact was not directly recovered.

These rows remain secondary/corroborated.

## Promotion blocker

The primary blocker is official-artifact accessibility, not event identification.

- Numeric first-event notice IDs: **103 / 103**
- Direct-primary events: **13**
- Remaining promotion candidates: **90**

The remaining candidates must not be promoted using third-party mirrors alone.


## 2026-10-06 continuation pass

The next official-site promotion pass checked additional secondary/corroborated events. No row was promoted without a directly inspectable first-event artifact.

### Official project pages confirmed, artifact still blocked or incomplete

- **김해 신문 센트럴 아이파크** — the official IPARK project site visibly exposes a “무순위 모집공고” link. The linked CDN PDF returns HTTP 403 in the current tool environment, so notice ID `2026910193` remains `ID_CORROBORATED_SECONDARY`.
- **중앙하이츠 원종역** — the official project site exposes “무순위 청약일정” / 모집공고 navigation, but the event fields are image/download based and the first-event official PDF was not directly inspectable. Notice ID `2026910157` remains secondary.
- **풍무역세권 수자인 그라센트 2차** — the official project site and BS한양-branded recruitment page were found, but the directly inspectable page currently exposes the original recruitment notice, not the later first follow-up event `2026940155`. No promotion.
- **야목역 서희스타힐스 그랜드힐** — the official project site exposes recruitment-notice navigation, but no directly inspectable first follow-up artifact for `2026910120` was recovered in this pass. No promotion.
- **의정부역 센트럴 아이파크** — official IPARK project site confirmed. Its public navigation exposes the original apartment recruitment notice, but not a directly inspectable first no-priority notice artifact for `2026910114`. No promotion.
- **e편한세상 여수 글렌츠** — official DL E&C/e편한세상 project page confirmed, but the visible official downloads correspond to the initial recruitment stage rather than the first no-priority event `2026910086`. No promotion.

### Rule reaffirmed

Finding an official project homepage is not sufficient for `PRIMARY_VERIFIED`.

The specific first follow-up event must itself be directly supported by an official notice artifact or official page containing the relevant event fields.

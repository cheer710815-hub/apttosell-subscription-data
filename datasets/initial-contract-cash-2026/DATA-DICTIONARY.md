# AptToSell 2026 Pre-Move-In Funding Dataset — Data Dictionary v1.0

## Dataset scope
2026년 1월~9월 최초 모집공고 기준 아파트 프로젝트를 대상으로 계약금, 중도금, 잔금, 중도금 금융지원 방식과 표준화된 **입주 전 필요자금** 지표를 정리한 검증 레지스트리입니다.

Version 1.0 공개 CSV는 41개 프로젝트로 구성됩니다. 전체 검증 모집단은 196개이며, 납부구조와 금융조건까지 검증한 프로젝트는 82개, 입주 전 필요자금 비율 계산이 가능한 프로젝트는 81개입니다.

## Core fields

| Field | Meaning |
|---|---|
| house_manage_no | 청약홈 주택관리번호 |
| project_name | 단지명 |
| region | 시도 |
| broad_region | 수도권/비수도권 등 광역 구분 |
| initial_announcement_date | 최초 모집공고일 |
| total_supply_households | 공급세대수 |
| project_max_price_10k_krw | 프로젝트 최고 공급금액, 만원 |
| initial_contract_rate_pct | 최초 모집공고 기준 총 계약금 비율 |
| first_contract_payment_10k_krw | 계약 체결 시 1차 계약금, 만원 |
| days_to_second_contract_payment | 2차 계약금 납부까지의 일수 |
| initial_interim_rate_pct | 중도금 총 비율 |
| initial_financing_support_rate_pct | 사업주체가 알선/지원하는 중도금 비율 |
| explicit_self_pay_interim_rate_pct | 공고상 명시적으로 직접 납부해야 하는 중도금 비율 |
| initial_balance_rate_pct | 잔금 비율 |
| financing_method | 무이자, 이자후불, 자납 등 금융조건 |
| initial_cash_required_10k_krw | 계약 당일 표준 초기 필요자금 |
| pre_movein_direct_cash_10k_krw | Version 1.0 CSV의 입주 전 필요자금, 만원 |
| pre_movein_direct_cash_ratio_pct | Version 1.0 CSV의 분양가 대비 입주 전 필요자금 비율 |
| later_promo_condition | 최초 공고 이후 잔여/선착순 판매조건 |
| verification_status | 검증상태 |
| source_quality | 출처 수준 |
| publication_ready | 공개용 subset 포함 여부 |
| verification_note | 검증 메모 |
| source_notice_url | 모집공고 또는 원출처 |
| evidence_url | 금융조건/보조 근거 |
| verified_date | 검증일 |
| direct_cash_calc_eligible | Version 1.0 CSV에서 입주 전 필요자금 비율 계산 가능 여부 |

## Derived metric
Version 1.0 CSV에서는 다음 필드명을 사용합니다.

`pre_movein_direct_cash_ratio_pct = initial_contract_rate_pct + explicit_self_pay_interim_rate_pct`

단, 납부구조와 금융조건이 모두 검증된 프로젝트에만 계산합니다.

문서와 해석에서는 이 값을 **입주 전 필요자금**으로 부릅니다. 향후 새 버전에서 필드명을 `pre_movein_funding_10k_krw`, `pre_movein_funding_ratio_pct`로 변경할 경우 기존 Version 1.0 필드와 의미상 동일한 지표로 버전 변경내역에 명시합니다.

## Important exclusions
- 잔금은 입주 전 필요자금 지표에서 제외합니다.
- 선택옵션 비용은 제외합니다.
- 개인별 중도금 대출 승인 가능성은 계산하지 않습니다.
- 후속 잔여세대/선착순 조건은 최초 모집공고 조건과 섞지 않습니다.

## Version 1.0 public release
- Public subset: 41 projects
- Verification date: 2026-10-05
- Zenodo Version 1.0 DOI: https://doi.org/10.5281/zenodo.23157055
- Zenodo all-versions DOI: https://doi.org/10.5281/zenodo.23157054
- License: CC BY 4.0

필드명을 해석하거나 재사용할 때는 이 문서와 해당 Zenodo 버전을 함께 인용하는 것을 권장합니다.

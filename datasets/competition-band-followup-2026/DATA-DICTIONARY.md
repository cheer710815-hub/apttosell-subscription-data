# Data Dictionary

## Project-level CSV

| 컬럼 | 설명 |
|---|---|
| project_id | AptToSell 내부 안정 식별자 |
| house_manage_no | 청약홈 주택관리번호 |
| house_name | 최초 모집공고 주택명 |
| region | 공급지역 |
| initial_announcement_date | 최초 모집공고일 |
| avg_first_priority_rate | AptToSell 계산 평균 1순위 경쟁률 |
| competition_band | 경쟁률 구간 |
| has_followup | 관측 기준일까지 후속공급 확인 여부(1/0) |
| followup_event_count | 연결된 후속공급 공고 수 |
| first_followup_date | 최초 후속공급 공고일 |
| days_to_first_followup | 최초공고일부터 첫 후속공급까지 경과일 |
| observation_days | 최초공고일부터 관측 기준일까지 일수 |
| eligible_60d | 60일 이상 관측 가능 여부 |
| followup_within_60d | 최초공고 후 60일 이내 후속공급 발생 여부 |
| eligible_90d | 90일 이상 관측 가능 여부 |
| followup_within_90d | 최초공고 후 90일 이내 후속공급 발생 여부 |
| initial_source_url | 청약홈 최초공고 확인 URL |

## Summary CSV

| 컬럼 | 설명 |
|---|---|
| competition_band | 경쟁률 구간 |
| projects | 구간 내 프로젝트 수 |
| followup_projects | 후속공급 확인 프로젝트 수 |
| simple_followup_rate_pct | 단순 발생률(%) |
| eligible_60d | 60일 관측가능 프로젝트 수 |
| followup_within_60d | 60일 이내 후속공급 발생 수 |
| followup_rate_60d_pct | 60일 표준화 발생률(%) |
| eligible_90d | 90일 관측가능 프로젝트 수 |
| followup_within_90d | 90일 이내 후속공급 발생 수 |
| followup_rate_90d_pct | 90일 표준화 발생률(%) |

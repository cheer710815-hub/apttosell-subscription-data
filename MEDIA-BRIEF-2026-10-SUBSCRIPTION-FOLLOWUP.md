# Media Brief — 2026 아파트 청약 경쟁률과 후속공급

**Release date:** 2026-10-04  
**Publisher:** AptToSell  
**Canonical article:** https://apttosell.com/%ec%b2%ad%ec%95%bd-%ea%b2%bd%ec%9f%81%eb%a5%a0/  
**Data cutoff:** 2026-10-04

## 한 줄 요약

2026년 1~9월 최초 모집공고 기준 아파트 196개를 추적한 결과, 1순위 경쟁률이 10대 1 이상이었던 44개 단지 중 19개에서 이후 무순위·잔여세대 또는 임의공급 공고가 확인됐습니다.

## 핵심 수치

- 최종 분석 모집단: **196개 단지**
- 경쟁률 확인: **193개 단지**
- 1순위 경쟁률 10대 1 이상: **44개**
- 이 중 후속공급 발생: **19개**
- 단순 관측 발생률: **43.2%**
- 60일 이상 관측 가능한 10대 1 이상 단지: **36개**
- 60일 이내 후속공급 발생: **13개**
- 60일 관측가능 단지 기준 발생률: **36.1%**

## 경쟁률 구간별 후속공급

| 1순위 경쟁률 | 단지 수 | 후속공급 | 단순 발생률 | 60일 발생률 |
|---|---:|---:|---:|---:|
| 1대 1 미만 | 93 | 41 | 44.1% | 45.3% |
| 1~5대 1 | 40 | 32 | 80.0% | 79.4% |
| 5~10대 1 | 16 | 11 | 68.8% | 64.3% |
| 10~30대 1 | 23 | 17 | 73.9% | 60.0% |
| 30대 1 이상 | 21 | 2 | 9.5% | 6.3% |

## 분양가 구간별 후속공급

| 단지 최고분양가 | 단지 수 | 후속공급 | 단순 발생률 | 60일 발생률 |
|---|---:|---:|---:|---:|
| 5억원 미만 | 11 | 4 | 36.4% | 20.0% |
| 5~7억원 | 55 | 24 | 43.6% | 45.5% |
| 7~10억원 | 52 | 32 | 61.5% | 61.9% |
| 10~15억원 | 30 | 18 | 60.0% | 70.8% |
| 15억원 이상 | 45 | 25 | 55.6% | 46.2% |

## 기사·블로그에서 사용할 수 있는 해석

- 높은 초기 청약 경쟁률이 이후 계약 단계의 수요를 완전히 설명하지는 않습니다.
- 특히 10~30대 1 구간에서도 후속공급이 상당수 관측됐습니다.
- 반면 30대 1 이상 구간은 상대적으로 후속공급 비율이 낮았습니다.
- 분양가 기준으로는 10억~15억원 구간의 60일 발생률이 가장 높게 나타났습니다.
- 다만 지역, 공급규모, 상품 특성, 공급 시점 등이 함께 작용하므로 가격 또는 경쟁률 단독의 인과효과로 해석하면 안 됩니다.

## 반드시 포함해야 할 주의문구

**후속공급 발생은 미계약률이나 계약 실패율이 아닙니다.** 무순위·잔여세대·임의공급에는 부적격, 계약취소, 잔여세대 재공급 등 여러 원인이 포함될 수 있습니다.

## 방법론

- 최초 모집공고일 기준 2026-01-01~2026-09-30
- 관측 기준일 2026-10-04
- 특수·재공급 성격의 비초기 공고 제외
- 1순위 접수건수와 주택형별 일반공급 세대수로 단지 경쟁률 산출
- 단지명·공급주소·공고시점을 이용해 잔여세대/임의공급 후속공고 연결
- 최근 공고의 관측기간 차이를 줄이기 위해 60일 기준 수치를 별도 산출

자세한 방법론:
https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/reports/apttosell-followup-analysis-2026-jan-sep-methodology.md

## 공개 데이터

Summary CSV:
https://raw.githubusercontent.com/cheer710815-hub/apttosell-subscription-data/main/reports/apttosell-followup-analysis-2026-jan-sep-summary.csv

## 권장 인용

> AptToSell, “2026 아파트 청약 경쟁률과 후속공급 분석”, 데이터 기준일 2026-10-04, 한국부동산원 청약홈 공개 API 기반 가공·분석. https://apttosell.com/%ec%b2%ad%ec%95%bd-%ea%b2%bd%ec%9f%81%eb%a5%a0/

## Source family

Korea Real Estate Board ApplyHome public API:
- apartment initial announcement details
- subscription competition rates
- residual/unsold supply announcements
- optional-supply announcements
- housing-model detail and presale-price data

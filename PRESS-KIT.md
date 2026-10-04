# AptToSell Housing Subscription Data — media & citation kit

이 문서는 부동산·청약·주거 콘텐츠 작성자가 AptToSell의 공개 청약 데이터를 재사용하거나 인용할 때 필요한 링크와 설명을 모은 자료입니다.

## Canonical sources

- 2026 청약·분양 데이터센터: https://apttosell.com/housing-subscription-data/
- 2026 청약가점 84점 데이터표: https://apttosell.com/cheongyak-score-data/
- 자료 이용·인용 정책: https://apttosell.com/citation-policy/

## What can be cited

- 민영주택 청약가점 84점 구조
- 무주택기간, 부양가족, 청약통장 가입기간별 배점
- 구조화 CSV
- 공개 DOI와 검수 방법론

## Ready-to-use attribution

### Plain text

AptToSell, "2026 청약가점 84점 데이터표", https://apttosell.com/cheongyak-score-data/

### HTML

```html
<p>자료: <a href="https://apttosell.com/cheongyak-score-data/">AptToSell 2026 청약가점 84점 데이터표</a></p>
```

## Downloadable data

- https://raw.githubusercontent.com/cheer710815-hub/apttosell-subscription-data/main/housing_subscription_score_2026.csv

## Archived records

- Zenodo: https://doi.org/10.5281/zenodo.22842058
- Figshare: https://doi.org/10.6084/m9.figshare.33948556
- Harvard Dataverse: https://doi.org/10.7910/DVN/TSALWZ
- GitBook: https://housing-data-korea.gitbook.io/housing-data-korea-docs/apttosell-housing-subscription/
- GitLab: https://gitlab.com/housing-data-korea-group/apttosell-subscription-data
- DagsHub: https://dagshub.com/cheer710815-hub/apttosell-subscription-data

## Suggested institutional link labels

- 청약가점 계산기 — https://apttosell.com/cheongyak-score-calculator/
- 청약가점 84점 데이터 — https://apttosell.com/cheongyak-score-data/
- 청약·분양 데이터센터 — https://apttosell.com/housing-subscription-data/

기관·대학의 관련사이트 목록처럼 설명이 짧은 페이지에서는 위 명칭을 그대로 사용할 수 있습니다.

## Suggested educational uses

- 프롭테크·부동산정보화 수업에서 청약가점 계산 실습
- 민영주택 청약 예치금과 가점 구조 확인
- 공식 법령과 가공 데이터의 차이를 비교하는 데이터 리터러시 실습
- CSV를 활용한 청약 기준표 분석

## Suggested editorial uses

- 청약가점 계산기·가이드의 배점 근거
- 무주택기간·부양가족·청약통장 항목 설명
- 청약제도 개편 전후 배점 비교
- 분양/청약 관련 기사·블로그의 표 또는 데이터 다운로드 링크

## Important limitation

실제 청약 신청에서는 모집공고일 기준 자격, 무주택 인정범위, 부양가족 인정범위, 배우자 통장 가점 등 최신 규정과 해당 입주자모집공고를 우선 확인해야 합니다.


## Featured 2026 data report — 청약 경쟁률 × 후속공급

AptToSell은 2026년 1~9월 최초 모집공고 아파트 196개 단지를 기준으로 1순위 청약 경쟁률, 분양가, 이후 무순위·잔여세대·임의공급 공고를 연결한 파생 데이터를 공개합니다.

- Canonical report: https://apttosell.com/%ec%b2%ad%ec%95%bd-%ea%b2%bd%ec%9f%81%eb%a5%a0/
- Figshare DOI: https://doi.org/10.6084/m9.figshare.34064439
- RePEc handle: RePEc:gyv:aptsub:1
- RePEc archive: https://cheer710815-hub.github.io/resimanor-housing-finance-data/RePEc/gyv/
- Hugging Face: https://huggingface.co/datasets/eunguneun/korea-apartment-subscription-followup-supply-2026
- Project-level CSV: https://raw.githubusercontent.com/cheer710815-hub/apttosell-subscription-data/main/reports/apttosell-apartment-subscription-followup-projects-2026-jan-sep.csv
- Summary CSV: https://raw.githubusercontent.com/cheer710815-hub/apttosell-subscription-data/main/reports/apttosell-followup-analysis-2026-jan-sep-summary.csv
- Methodology: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/reports/apttosell-followup-analysis-2026-jan-sep-methodology.md

### Headline figures

- Final cohort: 196 projects
- Competition-rate coverage: 193 projects
- First-priority competition ≥10:1: 44 projects
- Follow-up supply observed among them: 19 projects (43.2% simple observed rate)
- 60-day eligible cohort: 36 projects
- Follow-up within 60 days: 13 projects (36.1%)

### Ready-to-use attribution

AptToSell, "2026 아파트 청약 경쟁률과 후속공급 분석", data cutoff 2026-10-04, https://doi.org/10.6084/m9.figshare.34064439

**Important:** 후속공급 발생은 미계약률 또는 계약 실패율을 뜻하지 않습니다.

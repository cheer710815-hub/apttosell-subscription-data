# AptToSell Apartment Subscription Data

South Korea's 2026 housing-subscription reference data for private housing applications, including the 84-point subscription score structure and region/area-specific required deposit amounts.

아파트 청약과 분양에서 신청자가 확인해야 할 자격, 일정, 공급가격, 계약조건과 의무사항을 공식 공고문과 주택공급 관련 규정 기준으로 정리하는 공개 자료 저장소입니다. CSV·JSON, 방법론, 출처 정책과 인용 메타데이터를 함께 제공하여 연구·교육·분석 및 재사용이 가능하도록 구성합니다.

## Quick reference

- **Canonical data center:** https://apttosell.com/housing-subscription-data/
- **Canonical GitHub repository:** https://github.com/cheer710815-hub/apttosell-subscription-data
- **Reference release:** 2026-09-18
- **Zenodo DOI:** https://doi.org/10.5281/zenodo.22842058
- **Figshare DOI:** https://doi.org/10.6084/m9.figshare.33948556
- **Harvard Dataverse DOI:** https://doi.org/10.7910/DVN/TSALWZ
- **Mendeley Data DOI:** https://doi.org/10.17632/shdpkfbj3c.1
- **License:** CC BY 4.0

For versioned machine-readable files, methodology, source metadata, updates, and citation information, use the canonical GitHub repository and data center above.

## Website

- https://apttosell.com/

## Canonical data source

- [2026 청약가점 84점 데이터표](https://apttosell.com/cheongyak-score-data/)
- 기준 공개본: 2026-09-18
- Zenodo DOI: https://doi.org/10.5281/zenodo.22842058
- Zenodo concept DOI: https://doi.org/10.5281/zenodo.22842057
- Zenodo Community: https://zenodo.org/communities/apttosell-housing-subscription-data/
- Figshare DOI: https://doi.org/10.6084/m9.figshare.33948556
- Harvard Dataverse DOI: https://doi.org/10.7910/DVN/TSALWZ
- Mendeley Data DOI: https://doi.org/10.17632/shdpkfbj3c.1
- Mendeley Data record: https://data.mendeley.com/datasets/shdpkfbj3c/1
- Hugging Face dataset: https://huggingface.co/datasets/eunguneun/korea-housing-subscription-score-2026
- Kaggle dataset: https://www.kaggle.com/datasets/resimanor/korea-housing-subscription-score-2026

이 저장소는 위 원문 데이터 페이지의 배점 구조, 검수 원칙과 재사용 정보를 보조하기 위한 공개 저장소입니다. 법령 개정이나 설명 수정이 있는 경우 최신 canonical data source를 우선합니다.

## Featured data report — 2026 청약 경쟁률 × 후속공급

AptToSell이 2026년 1~9월 최초 모집공고 아파트를 기준으로 **청약 경쟁률, 분양가, 무순위·잔여세대·임의공급 후속공급**을 연결한 파생 데이터 분석입니다.

- **Canonical article:** https://apttosell.com/%ec%b2%ad%ec%95%bd-%ea%b2%bd%ec%9f%81%eb%a5%a0/
- **Final cohort:** 196 projects
- **Competition-rate coverage:** 193 projects
- **First-priority competition ≥10:1:** 44 projects
- **Follow-up supply observed among ≥10:1:** 19 projects
- **Simple observed rate:** 43.2%
- **60-day eligible cohort:** 36 projects
- **Follow-up within 60 days:** 13 projects
- **60-day rate:** 36.1%
- **Observation cutoff:** 2026-10-04
- **Figshare DOI:** https://doi.org/10.6084/m9.figshare.34064439
- **RePEc handle:** RePEc:gyv:aptsub:1
- **RePEc archive:** https://cheer710815-hub.github.io/resimanor-housing-finance-data/RePEc/gyv/
- **SchemaFinder:** https://schemafinder.com/dataset/c-1791120376-dsjx89

Public files:

- [Project-level CSV — 196 projects](./reports/apttosell-apartment-subscription-followup-projects-2026-jan-sep.csv)
- [Summary CSV](./reports/apttosell-followup-analysis-2026-jan-sep-summary.csv)
- [Data dictionary](./reports/apttosell-followup-analysis-data-dictionary.md)
- [Methodology and citation guide](./reports/apttosell-followup-analysis-2026-jan-sep-methodology.md)
- [Media brief](./MEDIA-BRIEF-2026-10-SUBSCRIPTION-FOLLOWUP.md)

> Important: “follow-up supply” is not a contract failure rate or non-contract rate. It only means a later official residual/unsold or optional-supply announcement was identified and matched to the initial project.

Suggested citation:

> AptToSell, “2026 아파트 청약 경쟁률과 후속공급 분석”, data cutoff 2026-10-04, derived from Korea Real Estate Board ApplyHome public API data. https://apttosell.com/%ec%b2%ad%ec%95%bd-%ea%b2%bd%ec%9f%81%eb%a5%a0/

## New derived report — 60-day follow-up by region and competition (2026-10-10)

- [Regional competition cross-tab CSV (11 groups)](./reports/apttosell-followup-60day-region-competition-2026-jan-sep.csv)
- [Methodology, cohort definitions and limitations](./reports/apttosell-followup-60day-region-competition-2026-jan-sep-methodology.md)
- Based on the same 196-project dataset, with 161 projects eligible for 60-day observation and 83 observed 60-day follow-up notices (all competition bands).
- The separate high-competition (first-priority >=10:1) cohort remains 13/36 (36.11%); **do not confuse these denominators**.
- A follow-up announcement does not establish a cancellation, contract failure, unsold-household count, or causal effect.
- **No new DOI is claimed for this derivative.** Underlying analysis DOI: https://doi.org/10.6084/m9.figshare.34064439

## Educational & institutional resource

- [INSTITUTIONAL-RESOURCE.md](./INSTITUTIONAL-RESOURCE.md) — 대학·연구기관·교육기관용 자료 안내
- [INSTITUTIONAL-LINK-PLAYBOOK.md](./INSTITUTIONAL-LINK-PLAYBOOK.md) — 기관형 링크 획득 운영 기준
- 추천 링크명: 청약가점 계산기 / 청약가점 84점 데이터 / 청약·분양 데이터센터

## Media & citation kit

- [PRESS-KIT.md](./PRESS-KIT.md)
- [EMBED.md](./EMBED.md) — 복사해서 붙여넣을 수 있는 차트·출처 링크 코드

## Current media brief

- [2026 추석 직후 9/28~10/2 청약 LIVE 브리프](./MEDIA-BRIEF-2026-09-25-POST-CHUSEOK-SUBSCRIPTIONS.md)
- [9/28~10/2 LIVE 청약 일정 CSV](./live_subscription_schedule_2026-09-28_to_10-02.csv)
- [2026 수도권 공공분양 의무기간 미디어 브리프](./MEDIA-BRIEF-2026-09-PUBLIC-PRESALE-OBLIGATIONS.md)
- [공공분양 의무기간 비교 CSV](./media_public_presale_obligation_compare_2026_09.csv)

## Public documentation

- [DagsHub public repository](https://dagshub.com/cheer710815-hub/apttosell-subscription-data)
- [GitLab public mirror](https://gitlab.com/housing-data-korea-group/apttosell-subscription-data)
- [GitBook public documentation](https://housing-data-korea.gitbook.io/housing-data-korea-docs/apttosell-housing-subscription/)

## Reference and citation pages

- [2026 청약·분양 데이터센터](https://apttosell.com/housing-subscription-data/)
- [자료 이용·인용 정책](https://apttosell.com/citation-policy/)
- [2026 민영주택 청약 예치금 데이터표](https://apttosell.com/private-housing-deposit-data/)

외부 데이터 저장소에서 이 자료를 인용하거나 재사용할 때는 가능한 경우 위 원문 데이터 페이지와 인용 정책을 함께 확인해 주세요.

## Related public datasets

### South Korea Housing Subscription Rules 2026

- Canonical source: https://apttosell.com/housing-subscription-data/
- Kaggle dataset: https://www.kaggle.com/datasets/resimanor/south-korea-housing-subscription-rules-2026

청약 공고, 자격, 가점, 예치금, 특별공급과 자금계획 등 2026년 주택청약 규칙을 한곳에서 확인할 수 있도록 연결한 공개 데이터입니다.

### 2026 민영주택 청약 예치금 데이터표

- Canonical source: https://apttosell.com/private-housing-deposit-data/
- Figshare DOI: https://doi.org/10.6084/m9.figshare.33948868
- Kaggle dataset: https://www.kaggle.com/datasets/resimanor/korea-private-housing-subscription-deposits

민영주택 청약 시 신청자의 거주지역과 공급받을 주택 전용면적에 따라 적용되는 예치기준금액을 정리한 공개 데이터입니다.

## Purpose

입주자모집공고의 핵심 조건을 구조화하고, 청약자가 자신의 자격과 자금계획을 스스로 검토할 수 있도록 근거와 확인 절차를 공개합니다.

## Coverage

- 일반공급과 특별공급 신청자격
- 해당지역과 기타지역 우선공급
- 청약 일정과 접수방법
- 분양가격, 계약금, 중도금과 잔금
- 전매제한, 거주의무와 재당첨제한
- 발코니 확장비 및 선택품목

## Repository structure

- `METHODOLOGY.md`: 공고문 분석 및 검수 절차
- `SOURCE_POLICY.md`: 공식 출처와 링크 기준
- `CITATION.cff`: GitHub·연구도구용 인용 메타데이터
- `datapackage.json`: 원문 URL, DOI, 라이선스와 주제 키워드를 담은 기계판독형 데이터 패키지 메타데이터

## Data policy

1. 입주자모집공고와 정정공고를 최우선 근거로 사용합니다.
2. 공급주체의 홍보문보다 청약홈과 공공기관 원문을 우선합니다.
3. 일정과 가격은 공고 기준일을 함께 표시합니다.
4. 단지별 조건을 다른 사업장에 일반화하지 않습니다.

## Citation

자료를 인용할 때는 저장소 이름, 단지 또는 문서명, 공고일과 원문 URL을 함께 표시해 주세요.

권장 원문 표기:

> AptToSell, "2026 청약가점 84점 데이터표", https://apttosell.com/cheongyak-score-data/

## Disclaimer

본 저장소는 정보 제공을 목적으로 합니다. 청약 신청과 계약 전에는 반드시 최신 입주자모집공고, 정정공고 및 관계기관 안내를 직접 확인해야 합니다.


## Developer access

Machine-readable JSON:
https://raw.githubusercontent.com/cheer710815-hub/apttosell-subscription-data/main/housing_subscription_score_2026.json

CSV:
https://raw.githubusercontent.com/cheer710815-hub/apttosell-subscription-data/main/housing_subscription_score_2026.csv

Use the JSON endpoint for apps, MCP servers, agents, and web tools that need a simple structured reference for the 84-point subscription score system.


## Monthly reference snapshots

- September 2026: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/reports/2026-09-reference-snapshot.md


## Media brief

- September 2026: https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/media/MEDIA-BRIEF-2026-09.md


## Institutional submission kit

- https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/INSTITUTIONAL-SUBMISSION-KIT.md


## Machine-readable catalog metadata

DCAT 3 JSON-LD:
https://raw.githubusercontent.com/cheer710815-hub/apttosell-subscription-data/main/dcat.jsonld

This file describes the repository's public datasets and distributions using the W3C Data Catalog Vocabulary (DCAT), so data catalogs, research tools, and agents can discover the dataset metadata in a standard machine-readable form.

## Related housing-finance resource

- [Resimanor 2026 주택금융·DSR 데이터센터](https://resimanor.com/housing-finance-dsr-data/) — 스트레스 DSR, 주택담보대출 한도 예시와 주택금융 계산 기준을 정리한 관련 공개 데이터 문서입니다.

## Publisher identity

- ORCID: https://orcid.org/0009-0006-9445-4768
- About.me: https://about.me/eunk
- Gravatar: https://gravatar.com/vegadus2
- GitHub: https://github.com/cheer710815-hub


## New dataset — 2026 아파트 초기 계약자금·입주 전 직접자금

AptToSell이 2026년 1~9월 최초 모집공고 196개 프로젝트를 대상으로 계약금, 중도금, 잔금, 중도금 금융지원 방식과 표준화된 입주 전 직접자금을 검증한 데이터 프로젝트입니다.

- Full validation registry: 196 projects
- Payment schedule + financing verified: 82 projects
- Direct-cash calculable: 81 projects
- Conservative publication-ready subset: 41 projects
- Verification date: 2026-10-05
- License: CC BY 4.0

Public documentation:

- [Dataset README](./datasets/initial-contract-cash-2026/README.md)
- [Methodology](./datasets/initial-contract-cash-2026/METHODOLOGY.md)
- [Data dictionary](./datasets/initial-contract-cash-2026/DATA-DICTIONARY.md)
- [Media brief](./datasets/initial-contract-cash-2026/MEDIA-BRIEF.md)
- [Publication-ready CSV](./datasets/initial-contract-cash-2026/apttosell-initial-cash-publication-ready-2026-10-05.csv)

> Important: 이 데이터의 '입주 전 직접자금'은 개인별 대출 가능액을 의미하지 않습니다. 공식 계약조건을 비교 가능한 방식으로 표준화한 지표이며, 후속 잔여세대·선착순 판촉조건은 최초 모집공고와 분리합니다.


## Project identity layer

- [AptToSell Verified Project Registry 2026 — Pilot](./datasets/verified-project-registry-2026/README.md)
- Working version: **0.4-pilot**
- Project IDs assigned: **196**
- Pre-move-in public subset crosswalk: **41/41 matched**
- DOI: **not assigned — identity verification is still being completed**

The registry provides a stable internal project ID for joining competition, price, payment-condition, follow-up supply, and future AptToSell datasets without altering previously frozen DOI releases.


## Follow-up event registry

- [AptToSell Follow-Up Event Registry 2026](./datasets/followup-event-registry-2026/README.md)
- Published public version: **0.2**
- First-event rows: **103**
- Stable project-ID matches: **103/103**
- Zenodo DOI: **https://doi.org/10.5281/zenodo.23176906**

The registry preserves project chronology and separates derived/corroborated dates from primary-verified notice-level events.


## Dataset — 2026 청약 경쟁률 구간별 후속공급 발생률

- **Canonical dataset page:** https://apttosell.com/2026-%ec%b2%ad%ec%95%bd-%ea%b2%bd%ec%9f%81%eb%a5%a0/

2026년 1~9월 최초 APT 모집공고 196개를 경쟁률 5개 구간으로 나누고, 이후 무순위·잔여세대 또는 임의공급 공고 발생 여부를 연결한 독립 파생 데이터셋입니다.

- Final cohort: **196**
- Competition-rate coverage: **193**
- Observation cutoff: **2026-10-04**
- Simple follow-up rates: **44.1% / 80.0% / 68.8% / 73.9% / 9.5%**
- Main finding: 경쟁률이 낮을수록 후속공급이 계속 증가하는 단순 선형 관계는 관측되지 않았으며, **30:1 이상 구간은 9.5%**로 크게 낮았습니다.
- DOI: **not assigned** — this is a scoped derivative dataset and is intentionally kept under the existing repository rather than issuing a new DOI.

Public files:

- [Dataset README](./datasets/competition-band-followup-2026/README.md)
- [Project-level CSV](./datasets/competition-band-followup-2026/apttosell-competition-band-followup-projects-2026-v1.0.csv)
- [Band summary CSV](./datasets/competition-band-followup-2026/apttosell-competition-band-followup-summary-2026-v1.0.csv)
- [Methodology](./datasets/competition-band-followup-2026/METHODOLOGY.md)
- [Data dictionary](./datasets/competition-band-followup-2026/DATA-DICTIONARY.md)
- [Public Data Portal submission text](./datasets/competition-band-followup-2026/PUBLIC-DATA-PORTAL-SUBMISSION.md)

> Important: 이 분석의 후속공급 발생률은 미계약률 또는 계약포기율을 의미하지 않습니다.


## Dataset — 2026 최초 모집공고 후 첫 후속공급까지 걸린 기간

2026년 1~9월 최초 APT 모집공고 196개 중 관측 기준일까지 후속공급이 확인된 103개 프로젝트에서 최초 모집공고일부터 첫 후속공급 공고일까지의 달력일 수를 계산한 독립 파생 데이터셋입니다.

- Follow-up projects: **103**
- Mean: **49.8 days**
- Median: **42 days**
- 31~60 days: **88 projects (85.4%)**
- 61~90 days: **11 projects (10.7%)**
- Over 90 days: **4 projects (3.9%)**
- Observation cutoff: **2026-10-04**
- DOI: **not assigned** — scoped derivative analysis, kept under the existing repository.

Public files:

- [Dataset README](./datasets/first-followup-time-2026/README.md)
- [Project-level CSV](./datasets/first-followup-time-2026/apttosell-first-followup-time-projects-2026-v1.0.csv)
- [Summary CSV](./datasets/first-followup-time-2026/apttosell-first-followup-time-summary-2026-v1.0.csv)
- [Methodology](./datasets/first-followup-time-2026/METHODOLOGY.md)
- [Public Data Portal submission text](./datasets/first-followup-time-2026/PUBLIC-DATA-PORTAL-SUBMISSION.md)

> Important: 이 분포는 후속공급이 확인된 103개 프로젝트만 대상으로 하며, 전체 196개 모집단의 미계약률 또는 계약포기율을 의미하지 않습니다.


## Pilot linkage — 분양가 괴리율 × 입주 전 필요자금

두 공개 데이터셋을 AptToSell 프로젝트 ID로 연결한 교차 데이터 파일을 공개합니다.

- Pre-move-in cash public cohort: **41 projects**
- Presale-price-gap public cohort: **62 projects**
- Reliable overlap: **11 projects**
- Median pre-move-in direct cash in overlap: **5,839만원**
- Status: **pilot / no DOI / no national inference**

Public files:

- [Pilot README](./datasets/price-gap-cash-linkage-2026/README.md)
- [11-project linked CSV](./datasets/price-gap-cash-linkage-2026/apttosell-price-gap-cash-linkage-public-pilot-v0.1.csv)
- [Methodology](./datasets/price-gap-cash-linkage-2026/METHODOLOGY.md)
- [Data dictionary](./datasets/price-gap-cash-linkage-2026/DATA-DICTIONARY.md)

> Important: 11개 중첩 표본은 전국 상관관계·인과관계 분석에 사용하지 않습니다. 현재 파일의 목적은 가격 비교 데이터와 자금부담 데이터의 프로젝트 단위 결합 가능성을 검증하는 것입니다.


## Dataset — 2026 분양가 괴리율 × 1순위 청약 경쟁률

AptToSell의 84㎡ 분양가 괴리율 공개표본 62개 프로젝트를 프로젝트 단위 1순위 청약 경쟁률 데이터와 연결한 파생 분석입니다.

- Linked projects: **62 / 62**
- Median first-priority competition: **1.10:1**
- Median all-age presale-price gap: **46.42%**
- Median <=10-year comparison gap: **31.21%**
- Spearman correlation (all-age gap vs competition): **-0.037**
- Spearman correlation (<=10-year gap vs competition): **0.103**
- Status: **derived v0.1 / no new DOI / observational association only**
- Underlying price-gap DOI: **10.5281/zenodo.23207987**

Public files:

- [Dataset README](./datasets/price-gap-competition-2026/README.md)
- [62-project CSV](./datasets/price-gap-competition-2026/apttosell-price-gap-competition-2026-v0.1.csv)
- [Methodology](./datasets/price-gap-competition-2026/METHODOLOGY.md)
- [Data dictionary](./datasets/price-gap-competition-2026/DATA-DICTIONARY.md)
- [Citation metadata](./datasets/price-gap-competition-2026/CITATION.cff)
- [Release notes](./datasets/price-gap-competition-2026/RELEASE_NOTES.md)
- [WordPress posting kit](./datasets/price-gap-competition-2026/WORDPRESS-POSTING-KIT-KR.md)

> Important: 이 분석은 관측자료 기반 상관분석입니다. 분양가와 주변 시세 차이가 청약 경쟁률에 미치는 인과효과를 입증하지 않습니다.


## Dataset — 2026 고경쟁 주택형 첫 후속공급 재등장(DDFS) 전국 타입단위 연구

- **Canonical article:** https://apttosell.com/ddfs-type-reappearance-2026/
- **Dataset version:** 1.0
- **Creator:** Kim, Eun (AptToSell)
- **ORCID:** https://orcid.org/0009-0006-9445-4768
- **License:** CC BY 4.0
- **DOI:** pending Zenodo registration

AptToSell이 2026년 첫 후속공급이 확인된 프로젝트를 대상으로, 최초 일반공급 1순위 aggregate 경쟁률이 **6대1 이상**이었던 주택형이 첫 후속공급에 동일 타입으로 다시 등장했는지를 타입 단위로 검증한 전국 risk-set 데이터셋입니다.

- First-follow-up registry projects: **103**
- Eligible projects with at least one 6x+ type: **52**
- Eligible housing types: **184**
- Reappeared types: **78**
- Non-reappeared types: **106**
- Type-level reappearance rate: **42.39%**

핵심 결과:
- 초기 경쟁률이 2배 높아질 때 재등장 odds: **OR 0.538**, p=0.0025
- 타입 공급비중이 2배 커질 때 재등장 odds: **OR 1.249**, p=0.0184
- 분양가·규제지역 여부·표준화 자기자금 부담·RPG는 보정 후 핵심 독립변수로 남지 않음

Public files:

- [Dataset README](./datasets/ddfs-national-type-riskset-2026/README.md)
- [Canonical 184-row CSV](./datasets/ddfs-national-type-riskset-2026/apttosell-ddfs-national-type-riskset-2026-v1.0.csv)
- [Model results CSV](./datasets/ddfs-national-type-riskset-2026/apttosell-ddfs-national-type-model-results-2026-v1.0.csv)
- [Methodology and findings](./datasets/ddfs-national-type-riskset-2026/METHODOLOGY-AND-FINDINGS.md)
- [Data dictionary](./datasets/ddfs-national-type-riskset-2026/DATA-DICTIONARY.md)
- [Citation metadata](./datasets/ddfs-national-type-riskset-2026/CITATION.cff)
- [Release notes](./datasets/ddfs-national-type-riskset-2026/RELEASE_NOTES.md)
- [Zenodo submission sheet](./datasets/ddfs-national-type-riskset-2026/ZENODO_SUBMISSION.md)

Suggested citation:

> Kim, Eun. (2026). *2026 National DDFS Type-level Risk-set: Apartment Subscription Demand and First Follow-up Reappearance, v1.0*. AptToSell. https://apttosell.com/ddfs-type-reappearance-2026/

> Important: 이 연구의 재등장은 미계약률·계약포기율을 의미하지 않습니다. 동일 공식 주택형이 첫 후속공급에 다시 포함됐는지만 측정합니다.


## Published dataset — 2026 Korean Apartment Subscription Demand and Relative Price Gap (RPG), v1.0.1

- **Creator:** AptToSell
- **Resource type:** Dataset
- **Version:** 1.0.1
- **License:** CC BY 4.0
- **Version DOI:** https://doi.org/10.5281/zenodo.23251654
- **All-versions DOI:** https://doi.org/10.5281/zenodo.23251653
- **Zenodo record:** https://zenodo.org/records/23251654
- **Frozen release files:** [RPG v1.0.1 dataset directory](./datasets/rpg-2026-v1.0.1/)
- **Methodology:** [RPG methodology](./datasets/rpg-2026-v1.0.1/METHODOLOGY_RPG_2026_v1.0.1.md)
- **Results:** [Regression results and interpretation](./datasets/rpg-2026-v1.0.1/RESULTS_RPG_2026_v1.0.1.md)
- **Reproduction code:** [Python script](./datasets/rpg-2026-v1.0.1/reproduce_rpg_regression_v1.0.1.py)

**Coverage:** 183 apartment presale projects; 857 housing types; 15,502 comparable-apartment audit records; 163 quality-focused projects.

**RPG definition:** (Comparable housing price − Presale price) / Presale price × 100. Positive RPG means the comparable existing-apartment price is higher than the presale price. RPG is not expected profit or a guaranteed return.

**Results:** HC3 OLS, full sample N=183: RPG coefficient 0.027407 (p=0.000397783); quality-focused sample N=163: 0.027898 (p=0.009803703). These are observational associations, **not causal effects**.

**Suggested citation:** AptToSell. (2026). *2026 Korean Apartment Subscription Demand and Relative Price Gap (RPG) Dataset* (Version 1.0.1) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.23251654

**Preservation note:** The 12 files in the frozen release directory are kept unchanged to preserve correspondence with the published Zenodo files and their SHA-256 checksums. This repository-level landing section adds the DOI without modifying the release payload.

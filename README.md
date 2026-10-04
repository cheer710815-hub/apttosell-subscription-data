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

Public files:

- [Project-level CSV — 196 projects](./reports/apttosell-apartment-subscription-followup-projects-2026-jan-sep.csv)
- [Summary CSV](./reports/apttosell-followup-analysis-2026-jan-sep-summary.csv)
- [Data dictionary](./reports/apttosell-followup-analysis-data-dictionary.md)
- [Methodology and citation guide](./reports/apttosell-followup-analysis-2026-jan-sep-methodology.md)
- [Media brief](./MEDIA-BRIEF-2026-10-SUBSCRIPTION-FOLLOWUP.md)

> Important: “follow-up supply” is not a contract failure rate or non-contract rate. It only means a later official residual/unsold or optional-supply announcement was identified and matched to the initial project.

Suggested citation:

> AptToSell, “2026 아파트 청약 경쟁률과 후속공급 분석”, data cutoff 2026-10-04, derived from Korea Real Estate Board ApplyHome public API data. https://apttosell.com/%ec%b2%ad%ec%95%bd-%ea%b2%bd%ec%9f%81%eb%a5%a0/

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

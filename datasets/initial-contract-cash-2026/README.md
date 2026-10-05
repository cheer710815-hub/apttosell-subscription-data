# Korea Apartment Pre-Move-In Funding Dataset 2026

AptToSell이 2026년 1월부터 9월까지의 아파트 최초 모집공고를 기준으로 계약금, 중도금, 잔금, 금융지원 방식과 **입주 전 필요자금**을 표준화한 검증 데이터 프로젝트입니다.

## Canonical source

- AptToSell analysis and dataset page: https://apttosell.com/%ec%95%84%ed%8c%8c%ed%8a%b8-%ec%9e%85%ec%a3%bc-%ec%a0%84-%ed%95%84%ec%9a%94%ec%9e%90%ea%b8%88/
- AptToSell housing-subscription data center: https://apttosell.com/housing-subscription-data/

## Current release

- Validation registry scope: **196 projects**
- Payment structure + financing conditions verified: **82 projects**
- Pre-move-in funding ratio calculable: **81 projects**
- Conservative publication-ready subset: **41 projects**
- Verification date: **2026-10-05**
- License: **CC BY 4.0**

The 196-project registry is the validation universe. The repository currently exposes the conservative 41-project publication-ready subset for external reuse.

## Public files

- [Publication-ready CSV — 41 projects](./apttosell-initial-cash-publication-ready-2026-10-05.csv)
- [Methodology](./METHODOLOGY.md)
- [Data dictionary](./DATA-DICTIONARY.md)
- [Media brief](./MEDIA-BRIEF.md)

## Core metric

**Pre-move-in funding ratio = total contract deposit rate + explicitly self-paid interim-payment rate**

This metric is calculated only when both the payment schedule and the financing treatment have been sufficiently verified.

It does **not** estimate a buyer's personal loan eligibility, actual bank approval, or total funds needed on the move-in/closing date.

## Verification hierarchy

1. Official housing recruitment notice / official notice PDF
2. Developer, project owner, or construction company's official project page
3. Reliable source reconstructing the recruitment notice
4. Major news coverage based on project-owner supplied terms

Later residual-unit or first-come sales promotions are kept separate from the original recruitment conditions and are not retroactively applied to the initial-condition metrics.

## Data design

The public dataset separates, where available:

- total contract deposit rate
- first contract payment
- days to the second contract payment
- interim-payment rate
- financing-supported interim-payment rate
- explicitly self-paid interim-payment rate
- balance rate
- financing method
- standardized pre-move-in funding amount and ratio
- later promotional conditions
- verification status and evidence URLs

See [DATA-DICTIONARY.md](./DATA-DICTIONARY.md) for field-level definitions.

## Limitation and next version

The current release is project-level and uses the project's maximum supply price as the comparison reference.

The next institution-ready edition should expand to **housing-type-level rows**, because supply prices and payment schedules can differ by housing type within the same project.

## Citation

Suggested citation:

> AptToSell. (2026). *Korea Apartment Pre-Move-In Funding Dataset 2026*. Version 2026-10-05. https://apttosell.com/%ec%95%84%ed%8c%8c%ed%8a%b8-%ec%9e%85%ec%a3%bc-%ec%a0%84-%ed%95%84%ec%9a%94%ec%9e%90%ea%b8%88/

When reusing the data, please cite **AptToSell** and the canonical source URL above.

# AptToSell DDFS v1.0 — External citation and reuse brief

**Released:** 2026-10-14  
**Status:** Supporting documentation for an already published dataset; **not** a new study, dataset version, or DOI.

## Canonical research asset

- Study: *2026 National DDFS Type-level Risk-set: Apartment Subscription Demand and First Follow-up Reappearance, v1.0*
- Version DOI: https://doi.org/10.5281/zenodo.23328833
- All-versions DOI: https://doi.org/10.5281/zenodo.23328832
- Canonical analysis: https://apttosell.com/ddfs-type-reappearance-2026/
- Machine-readable files and methods: https://github.com/cheer710815-hub/apttosell-subscription-data/tree/main/datasets/ddfs-national-type-riskset-2026
- License: CC BY 4.0 (credit the author and source)

## Citation-ready summary (Korean)

AptToSell의 2026년 전국 주택형 단위 관측 연구는 **최초 후속공급이 확인된 사업** 중 **최초 일반공급 1순위 경쟁률이 6대 1 이상인 주택형** 184개(52개 사업)를 분석했다. 첫 후속공급에서 동일 공식 주택형이 재등장한 사례는 78개(42.39%)였다. 최초 경쟁률이 더 높은 주택형은 재등장 비율이 낮았고, 해당 주택형의 사업 내 일반공급 비중이 높을수록 재등장 비율이 높았다. 사업별 군집을 반영한 회귀분석에서도 두 관계가 관찰됐다. **이 결과는 관측된 후속공급 재등장에 관한 것으로 미계약률, 계약취소율 또는 인과관계를 뜻하지 않는다.**

## Citation-ready summary (English)

In AptToSell's 2026 type-level observational study, the risk set comprised **184 housing types from 52 projects** with a verified first follow-up supply event and initial first-priority general-supply competition of at least 6:1. **78 types (42.39%)** reappeared in the first follow-up. Deeper initial competition was associated with lower reappearance, while a larger share of the project's initial general supply was associated with higher reappearance. These associations persisted in project-clustered models. **Reappearance is not a measure of uncontracted units, contract cancellation, or causality.**

## Core figures and interpretation

| Metric | Published v1.0 |
|---|---:|
| Projects with verified first follow-up in registry | 103 |
| Projects meeting type-level risk-set eligibility | 52 |
| Eligible types | 184 |
| Reappeared types | 78 |
| Types not reappearing | 106 |
| Reappearance share | 42.39% |
| Competition per doubling, adjusted odds ratio | 0.538 (95% CI 0.360–0.804) |
| Type supply share per doubling, adjusted odds ratio | 1.249 (95% CI 1.038–1.503) |

The 103-project registry is **not** the denominator for the 42.39% statistic. The denominator is 184 eligible housing types.

## Recommended attribution

Kim, Eun. (2026). *2026 National DDFS Type-level Risk-set: Apartment Subscription Demand and First Follow-up Reappearance, v1.0* [Dataset]. Zenodo. https://doi.org/10.5281/zenodo.23328833

Suggested source link: https://apttosell.com/ddfs-type-reappearance-2026/

## For editors, institutions and researchers

- Use the canonical analysis and the frozen v1.0 dataset, not an unversioned screenshot.
- Report both numerator and denominator when quoting 42.39%.
- Keep initial first-priority competition distinct from subsequent follow-up competition.
- State that the sample is conditioned on projects with a verified first follow-up and eligible high-competition types; it is not all Korean apartment projects.
- Do not call the outcome an uncontracted-unit rate or a cancellation rate.
- Check row-level official notice URLs and evidence grades before reporting individual projects.
- If reproducing a chart or table, attribute AptToSell and the version DOI.
- No external editorial endorsement or backlink is implied by this brief.

## Source documents

- [README](./README.md)
- [Frozen methodology and findings](./METHODOLOGY-AND-FINDINGS.md)
- [Data dictionary](./DATA-DICTIONARY.md)
- [Canonical CSV](./apttosell-ddfs-national-type-riskset-2026-v1.0.csv)
- [Model results](./apttosell-ddfs-national-type-model-results-2026-v1.0.csv)

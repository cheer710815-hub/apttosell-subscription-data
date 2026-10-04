# connu/awesome-datasets submission — South Korea housing dataset

## Target
https://github.com/connu/awesome-datasets

## Proposed issue title
Dataset proposal: South Korea apartment subscription competition & follow-up supply (2026)

## Proposed issue body

### Dataset addition proposal: South Korea real estate & housing

I'd like to propose adding South Korea to `real-estate-and-housing` with the following public dataset.

#### Korea Apartment Subscription Competition and Follow-up Supply Analysis, 2026 Jan–Sep

- **Publisher:** AptToSell
- **Country:** South Korea (KR)
- **Canonical report:** https://apttosell.com/%EC%B2%AD%EC%95%BD-%EA%B2%BD%EC%9F%81%EB%A5%A0/
- **Repository:** https://github.com/cheer710815-hub/apttosell-subscription-data
- **Project-level CSV:** https://raw.githubusercontent.com/cheer710815-hub/apttosell-subscription-data/main/reports/apttosell-apartment-subscription-followup-projects-2026-jan-sep.csv
- **Summary CSV:** https://raw.githubusercontent.com/cheer710815-hub/apttosell-subscription-data/main/reports/apttosell-followup-analysis-2026-jan-sep-summary.csv
- **Methodology:** https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/reports/apttosell-followup-analysis-2026-jan-sep-methodology.md
- **Data dictionary:** https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/reports/apttosell-followup-analysis-data-dictionary.md
- **Persistent identifier:** https://doi.org/10.6084/m9.figshare.34064439
- **License:** CC BY 4.0
- **Access:** Direct download, no registration
- **Records:** 196 apartment presale projects
- **Observation cutoff:** 2026-10-04

The dataset links South Korean apartment presale announcements with first-priority subscription competition rates, presale-price information, and later residual/unsold or optional-supply announcements. Competition-rate coverage is available for 193 of 196 projects.

Important interpretation note: a later follow-up supply announcement is **not** the same thing as a contract-failure or non-contract rate.

I maintain AptToSell and the dataset, so I am disclosing that affiliation. I checked the contribution guide: South Korea does not appear to be present yet in `data/countries.json`, so this would also require adding the KR country entry and generating the country/topic outputs. If the dataset is a fit, I can prepare the JSON entry in the repository's schema format.

## Fit check
- Publicly obtainable: yes
- Stated license: CC BY 4.0
- Direct download: yes
- Methodology/data dictionary: yes
- Substantial: 196 project-level records, 18 fields
- Duplicate in target catalog: none found as of 2026-10-04
- Target topic: real-estate-and-housing
- New country required: South Korea (KR)

## Connector limitation
Automated issue creation returned GitHub 403 Resource not accessible by integration. Manual issue creation is therefore required.

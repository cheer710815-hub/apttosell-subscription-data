# N06 — Apartment subscription notice and contract schedule intervals (2026)

**Official published dataset:** https://doi.org/10.5281/zenodo.23656772  
**Zenodo version DOI:** `10.5281/zenodo.23656772`  
**Zenodo concept DOI:** `10.5281/zenodo.23656771`  
**Version:** 1.0 (published 2026-10-26)  
**Author:** Eun Kim / AptToSell  
**Source:** Korea Real Estate Board (ApplyHome), Public Data Portal, https://www.data.go.kr/data/15098547/openapi.do

## Research scope

This is a reproducibility and comparison package based on **249 housing-project records** from a preserved 2026 ApplyHome API response snapshot. Four date fields per record were reconciled to the analysis CSV (**996/996** date values matched). A subset of **30 projects** with an API winner-announcement-to-contract-start interval of at least 30 days was checked against official scheduled contract information.

- **29/30** verified contract schedule records matched the API dates.
- **1/30** differed: **e편한세상 분당 퍼스트빌리지 (성남낙생 A-1)**, housing management ID `2026820004`. The preserved API contract start is **2026-11-07**; the final corrected notice says **2026-11-04**. Both give contract end **2026-11-13**.
- The other **219 projects were not individually verified** against final corrected official notices.
- Scheduled contract dates are **not actual contract execution records**, contract completion rates, or legal guarantees.

## Citation

Kim, Eun (2026). *Apartment Subscription Notice and Contract Schedule Intervals in South Korea: A 249-Project Dataset with 30 Official Notice Verifications (2026)* (Version 1.0) [Dataset]. Zenodo. https://doi.org/10.5281/zenodo.23656772

## Related articles

1. https://apttosell.com/apartment-notice-to-contract-schedule-249-2026/
2. https://apttosell.com/apartment-contract-period-249-2026/
3. https://apttosell.com/winner-to-contract-days-249-2026/

The source JSON, transformed CSV tables, quality-assurance summary, data dictionary, checksums, and research documentation are deposited with Zenodo. **Do not create a separate DOI for this same dataset.**

The original public API source must be credited separately. Redistribution rights for original official notice PDFs have not been established; these PDFs are not included in the public dataset package.

# N01 36110/202609 source XML audit preparation

As of 2026-10-23, the saved September Sejong original CSV carries two literal `84` area values (brokered 8F, direct 7F). Historical original HTTP response XML is unavailable, so saved CSV integrity does not establish the original API field precision.

A private local Windows Python stdlib audit package was generated: `N01_Sejong_XML_Source_Audit.zip` (not committed to public repository). The tool requests LAWD_CD=36110 and DEAL_YMD=202609 from MOLIT SilvTrade endpoint with a user-provided environment service key, saves a new immutable response XML snapshot and SHA256, checks totalCount, and contrasts date/floor/project-specific `excluUseAr` strings without altering historical CSV. Tested locally with synthetic XML (two matching rows, one changed-area detection), but **LIVE GOVERNMENT RE-QUERY NOT EXECUTED** because no credential is available in this environment. On re-query, later data corrections could cause differences independent of collector transformation; must not retroactively overwrite historical sample.

Current N01: 824 source rows, 606 provisional eligibility, 29 official-notice reference candidates (25 unique schedule amount, 4 building-line intervals), and zero validated financial comparison. No DOI and no claimed premium.

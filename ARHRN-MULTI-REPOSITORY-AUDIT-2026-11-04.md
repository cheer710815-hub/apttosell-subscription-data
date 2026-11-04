# ARHRN multi-repository publication audit — 2026-11-04

Status: operational audit; **not a research dataset or DOI registration**.

## Principles
- Zenodo is optional. Do not pause validated research publication solely because Zenodo login is unavailable.
- Do not publish the same research object repeatedly to obtain more DOI identifiers or backlinks.
- Check canonical DOI, reservation DOI, related-item metadata, license, raw source rights, checksum, reproducibility, and author display before each deposit.
- Distinguish a DOI written in citation metadata from a live verified landing page; metadata alone does not establish successful publication.
- Prefer original site data-center page + GitHub code and version + **one** appropriate archival DOI per distinct research object.

## Existing repository citations (recorded; live landing-page recheck pending)
- AptToSell `CITATION.cff` lists Zenodo 10.5281/zenodo.22842058, Figshare 10.6084/m9.figshare.33948556, Harvard Dataverse 10.7910/DVN/TSALWZ, and Mendeley Data 10.17632/shdpkfbj3c.1, as well as later research-specific IDs.
- Resimanor `DOI-POLICY.md` identifies canonical Zenodo DOI 10.5281/zenodo.22840870 and legacy mirror DOIs in Figshare, Harvard Dataverse, and Mendeley Data; its policy explicitly prohibits depositing identical research objects solely for more DOIs.
- N07 special-supply study: internal publication queue records Zenodo DOI 10.5281/zenodo.23827229 as published on 2026-10-31; independently verify landing page before external representation.
- Seoul direct-transaction study v0.6: internal queue records reserved (not published) DOI 10.5281/zenodo.23851759; **do not mint replacement before resolving reservation status**.

## Candidate triage
| Research | Current evidence | Next action |
|---|---|---|
| ARHRN-SUBSCRIPTION-DENOMINATOR-20261101 | 17th stage reproduces 188 complexes, 4,572 API rows, 1,123 housing types; selected official-document explanations not fully sourced | Candidate 1: verify deposit content, license, clear limited claims, search existing identifiers |
| ARHRN-UNRANKED-2026-01 | Stage 31 report v0.9.2; 657 remaining-unit API-path notices, incomplete legal supply-type verification | Candidate 2: publish only as observational analysis with explicit limitations; raw-snapshot and rights audit |
| ARHRN-PRESALE-PRICE-20261031 | Publication paused; prior validation work recorded | Candidate 3: obtain latest finalized data and provenance checksum |
| I07 regional special supply | Previously classified ineligible | Exclude |
| I08 official-price panel | Missing reproducible source data | Exclude |

## Service screening (as of 2026-11-04)
- Figshare free individual account: 20GB storage, 500 items, DOI for eligible public outputs. https://info.figshare.com/user-guide/account-limits/
- Harvard Dataverse: free to outside researchers, DOI, administrative spam and scope review; data deposit guidelines. https://support.dataverse.harvard.edu/getting-started
- Mendeley Data: 10GB per dataset; restricts already-published/DOI-held and AI/LLM-generated datasets; moderation. https://www.elsevier.support/mendeley/answer/what-are-the-requirements-for-datasets-
- OSF Projects: new project creation ends 2026-11-16; existing projects read-only 2027-02-19. Not a new general repository choice. https://help.osf.io/article/727-osf-projects-transition

## Publication gate
1. Confirm no existing *published* or *reserved* identifier for this exact research object.
2. Freeze version, author, title, keywords, snapshot period and unique research ID.
3. SHA256 manifest covering every file; independently rerun supported summary numbers.
4. Check source licensing and remove confidential API keys / personal data.
5. Link the canonical AptToSell/Resimanor data page and GitHub source; link related publications as versions, not false originals.
6. Submit **one** suitable external repository record when login/permission is available; only mark published after the landing page resolves.
7. Track real citations, referral visits, and editorial reuse rather than counting DOI quantity.

No Figshare, Harvard Dataverse, or Mendeley submission was made as part of this audit.
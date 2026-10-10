# Backlink Acquisition Tracker

Updated: 2026-09-26

This tracker records only legitimate editorial, institutional, open-data, and open-source adoption opportunities for AptToSell and Resimanor.

## 2026-10-06 backlink safety rule

The program now prioritizes citation, reuse, indexing, and real data adoption over raw backlink count.

Allowed / preferred:
- scholarly and open-data repositories that host the actual dataset or metadata;
- housing or finance data catalogs with a clear topical fit;
- curated GitHub lists where the repository explicitly accepts relevant datasets or research resources;
- open-source projects only when the dataset has a concrete implementation, fixture, documentation, benchmark, or reference-data use case;
- DOI, citation metadata, machine-readable schemas, and institutional resource pages.

Do not use:
- repeated "please use this as reference data" issues across unrelated repositories;
- duplicate issue/PR submissions to multiple unrelated projects merely for links;
- generic profile, forum, comment, directory, or guest-post backlinks;
- submissions whose primary value disappears if the backlink is removed;
- automated or templated outreach at scale.

Decision test:
> Would this submission still be useful to the destination community if the backlink were nofollowed or removed?

If the answer is no, do not submit.

Existing GitHub issues/PRs should be retained only where there is strong topical and implementation fit; otherwise no follow-up or duplication should be created.

## Status legend

- ACTIVE — submitted or live opportunity
- PREPARED — submission package ready, external action still required
- WATCH — relevant but no action yet
- EXCLUDED — not suitable for backlink acquisition

## ACTIVE

### tae0y/real-estate-mcp
Type: Open-source data adoption
Status: ACTIVE
Issue:
https://github.com/tae0y/real-estate-mcp/issues/40
Assets:
- AptToSell subscription score data
- Resimanor stress DSR data
Goal:
Reference dataset / fixture / documentation adoption.

### ssuksak/cheongyak-rag-mcp
Type: Open-source data adoption
Status: ACTIVE
Issue:
https://github.com/ssuksak/cheongyak-rag-mcp/issues/1
Assets:
- AptToSell subscription score CSV/JSON
- AptToSell private-housing deposit data
Goal:
Static reference dataset for subscription guide / RAG / fixtures.

## PREPARED

### Awesome Public Datasets
Type: Public dataset catalog
Status: PREPARED
Submission method:
Fork + pull request required.
Rules:
- Direct dataset repository preferred over promotional landing page.
- High-quality, directly downloadable public data.
- Maintainer review required.
Prepared files:
- AptToSell: external-submissions/awesome-public-datasets.yml
- Resimanor: external-submissions/awesome-public-datasets.yml
Blocker:
Current GitHub connector cannot create forks.

### Universal Housing Dataset Catalog
Type: Housing dataset catalog
Status: EXCLUDED_FOR_CURRENT_LICENSE
Verified catalog:
https://housing.pubpub.org/datasets
Verified submission form:
Public Airtable form titled "Open-Source Housing Data"
Verified:
2026-09-27
Critical eligibility finding:
- The submission form explicitly says it is for "public-domain datasets centered around housing."
- Current AptToSell and Resimanor datasets are licensed CC BY 4.0, which is an open license but not public domain.
Decision:
- Do not submit either current dataset through this form.
- Do not change the dataset license merely to obtain a backlink.
Next step:
- Reconsider only if the catalog later accepts openly licensed non-public-domain datasets or a genuinely public-domain derivative/resource is created for an independent reason.
Priority: EXCLUDED

### Korea Banking Institute
Type: Financial education resource
Status: PREPARED
Fit:
Uses private proptech / real-estate information services in education.
Submission path:
Course proposal / institutional inquiry.
Constraint:
Login or human contact required.
Primary assets:
- AptToSell calculator/data center
- Resimanor DSR data center

### Seoul 50Plus
Type: Lifelong-learning resource
Status: PREPARED
Fit:
Real-estate and finance education with private real-estate tools.
Submission path:
Course/team inquiry.
Constraint:
Human contact required.
Primary asset:
Resimanor DSR / housing-finance data.

### Seoul Cyber University AI Real Estate Big Data
Type: University related-resource / education
Status: PREPARED
Fit:
Directly lists private real-estate/proptech tools.
Primary assets:
- AptToSell calculator
- AptToSell data center
- Resimanor DSR data center

### Mokwon University Real Estate Finance Insurance
Type: Broken-link replacement
Status: PREPARED
Candidate:
Speedbank legacy/outdated external link.
Replacement assets:
AptToSell data center / Resimanor data center.

## WATCH

- Shin Ansan University Real Estate
- Hallym University Community Education Center
- Pyeongtaek University Urban Planning & Real Estate
- Gangneung-Wonju National University Urban Planning & Real Estate
- Konkuk University Real Estate
- Korea Proptech Forum
- Seoul Eastern Women's Development Center



## Newly discovered Universal-Housing-like hubs

### National Housing Conference — Housing Resource Center
Type: Curated housing resource/data-tool hub
Status: READY_TO_SUBMIT
Verified submission form:
https://hrc.nhc.org/contact-us/
Verified fields:
- Full Name
- Title
- Organization
- Work Phone
- Email Address
- Suggested Resource Title
- Suggested Resource Topic Area
- Suggested Resource Link
- Comments
Why it matters:
- Maintains a curated housing-policy resource center with a dedicated Data Tools type.
- Resource entries link users to the original external source.
- Official form explicitly accepts resource suggestions without requiring prior membership/login.
Prepared file:
- external-submissions/nhc-housing-resource-center.md
Blocker:
- Actual form submission requires submitter contact details (name/email, and optionally title/phone).
Priority: VERY HIGH

### MorFi Open Source Housing & Mortgage Data
Type: Mortgage and housing open-data contribution hub
Status: SUBMITTED
Submission route:
Email to support@morfi.com
Submitted:
2026-09-26
Why it matters:
- Explicitly invites users to suggest new housing/mortgage data sources and contribute to open datasets.
- Audience includes mortgage software developers, housing researchers and analysts.
Submission:
- Suggested Resimanor stress DSR / mortgage-limit data center and open CSV/JSON resources.
Next step:
- Monitor for reply, contribution guidance, or inclusion.
Priority: HIGH for Resimanor

### The Real Deal — Directory of Real Estate Data Sites
Type: Curated real-estate data-source directory
Status: SUBMITTED
Submission route:
Email to research@therealdeal.com
Submitted:
2026-09-26
Why it matters:
- Dedicated searchable directory of real-estate data sites.
- Public page explicitly invites suggestions.
Submission:
- Suggested AptToSell housing subscription data center.
- Suggested Resimanor housing-finance / stress-DSR data center.
Next step:
- Monitor for reply or directory inclusion.

### Data Is Plural
Type: Curated dataset discovery newsletter/archive
Status: SUBMITTED
Submission route:
Email to jsvine@gmail.com
Submitted:
2026-09-26
Why it matters:
- Prefers free, directly accessible, documented, downloadable datasets.
- AptToSell and Resimanor match many of its stated dataset-quality criteria.
Submission:
- Suggested AptToSell housing subscription data.
- Suggested Resimanor stress-DSR / housing-finance data.
Next step:
- Monitor for reply, newsletter inclusion, or archive citation.



### National Housing Data Exchange (Australia / AHDAP)
Type: Housing-specific CKAN data exchange
Status: WATCH
Why it matters:
- Dedicated housing data portal with datasets from government, industry and public sources.
- Supports external-source records, not only locally hosted files.
- CKAN registry exposes metadata, formats, licenses and API access.
Fit:
- Structural fit is strong for both repositories.
Constraint:
- Geographic mission is explicitly focused on Australia's housing future; Korean datasets may be outside scope.
Priority: MEDIUM-LOW unless international submissions are confirmed.

### Data Commons
Type: Global public-data knowledge graph / API / MCP
Status: WATCH
Why it matters:
- Accepts public-data contributions.
- Contributed data becomes accessible through Data Commons tools and APIs.
- Data Commons also provides MCP access for LLM/agent use.
Fit:
- Resimanor could fit only if converted into statistical variables joined to Korean places/institutions.
- AptToSell score/deposit lookup tables are less natural because they are rule/reference tables rather than place-based macro statistics.
Constraint:
- Best fit is public statistical macro data licensed CC BY and joinable to existing entities such as places or institutions.
Priority: MEDIUM for future derived regional statistics; LOW for current rule tables.



### Awesome Real Estate (etewiah/awesome-real-estate)
Type: Curated global real-estate / proptech resource list
Status: PR_READY
Why it matters:
- Actively maintained in 2026.
- Has an explicit Asia section with South Korea already represented.
- Includes Authoritative Research & Publications with open housing datasets.
- Contribution rules allow owner submissions if affiliation is disclosed.
Prepared file:
- external-submissions/awesome-real-estate-pr.md
Blocker:
- Pull request requires fork/edit flow not supported by the current GitHub connector.
Priority: HIGH

### Awesome Real Estate APIs (happyendpointhq/awesome-real-estate-apis)
Type: Country-by-country real-estate data source / API / dataset list
Status: PREPARED
Why it matters:
- Dedicated to property data sources, government open data, APIs and bulk datasets by country.
- Explicitly accepts additions through GitHub issues or pull requests.
- Has a Datasets section and Asia Pacific section.
- Free/open access status and access restrictions are part of its curation model.
Best fit:
- AptToSell: South Korea reference dataset (subscription score/deposit)
- Resimanor: South Korea reference dataset (stress DSR / mortgage-limit scenarios)
Constraint:
- GitHub App issue creation returned 403 even though the repo accepts issues/PRs; manual GitHub submission is still possible.

### SchemaFinder
Type: Public dataset search/index + API + MCP
Status: PREPARED
Submission:
https://schemafinder.com/submit
Why it matters:
- No-login public dataset submission form is verified.
- Community submissions go live immediately with a Community badge.
- Requires an explicit column schema, matching our structured CSVs.
- Supports dataset discovery plus API/MCP workflows.
Prepared file:
- external-submissions/schemafinder.md
Priority: VERY HIGH


### Awesome Urban Datasets (urban-toolkit)
Type: Curated public urban-dataset list
Status: WATCH
Why it matters:
- Publicly maintained curated list of urban datasets.
- Contributions are explicitly welcomed.
- Includes property cadastre, buildings/lots, infrastructure and urban-analysis datasets.
Fit:
- Current AptToSell/Resimanor rule/reference tables are not a strong fit because they are not spatial urban datasets.
- Future regional datasets (local housing prices, supply, accessibility, regional finance indicators) could fit much better.
Priority: LOW for current datasets / HIGH for future geospatial-regional data.



### Number Cortex Financial Resources
Type: Curated finance education / calculator resource hub
Status: WATCH
Why it matters:
- Curates external financial websites, apps and calculators.
- Includes mortgage calculators as a dedicated calculator category.
- Public page exposes a “Suggest Resource” route.
Best fit:
- Resimanor housing-finance / stress-DSR data center and calculator-type resources.
Constraint:
- Submission form details and editorial standards need deeper verification before outreach.
Priority: MEDIUM

### PolicyMap Data Catalog
Type: Large housing / community-development / mortgage data catalog
Status: WATCH
Why it matters:
- Strong housing, affordability, mortgage and lending dataset coverage.
- High-value research audience.
Constraint:
- Current catalog appears to be internally curated / licensed data; no public external-dataset submission route verified.
Priority: LOW unless a contribution path is confirmed.

### Urban Institute Data Catalog
Type: Housing-policy / mortgage research data catalog
Status: WATCH
Why it matters:
- Strong topical overlap with mortgage, housing finance and neighborhood data.
- Research-grade catalog and citation environment.
Constraint:
- Appears focused on Urban Institute-produced/managed datasets; no open public submission path verified.
Priority: LOW unless external contributions are explicitly allowed.

### LucidAgent Data Catalog
Type: Agent-oriented public data catalog
Status: WATCH
Why it matters:
- Has a Real Estate category with Zillow, ACS Housing, HMDA, FHFA and HUD datasets.
- Oriented toward data applications and agents.
Constraint:
- No public external dataset submission path verified.
Priority: LOW unless contribution flow is found.



### GeetMark Search Hub
Type: Vertical resource search engine / API
Status: WATCH
Why it matters:
- Operates a dedicated Real Estate category.
- Public navigation exposes a Submit Resource route.
- Search API and item endpoints can make accepted resources discoverable programmatically, not only through a directory page.
- No-login browsing is available.
Best fit:
- AptToSell calculator/data center as a Real Estate resource
- Resimanor housing-finance/DSR data center as a Real Estate resource
Constraint:
- The public submission page is referenced in site navigation, but the detailed submission form and editorial criteria were not independently retrievable in follow-up verification.
Priority: MEDIUM pending form verification.

### Deal-Scale Awesome Real Estate Investing
Type: Curated real-estate investing resource list
Status: PR_READY
Contribution method:
Edit README.md and submit a pull request.
Why it matters:
- PRs are explicitly welcomed.
- Includes Analytics & Data Platforms, Foundational Geospatial & Data Sets, and Authoritative Research & Publications.
Prepared file:
- external-submissions/deal-scale-awesome-real-estate-investing-pr.md
Priority: MEDIUM

## EXCLUDED / DO NOT USE

- Mass email outreach
- Random profile backlinks
- Free posting boards
- Paid guest posts
- Reciprocal link schemes
- Automated backlink packages
- Government “suggest a dataset” forms that only request new government datasets
- Irrelevant GitHub repositories without a clear data-use case
- Duplicate submissions to multiple repositories by the same developer

## Core linkable assets

### AptToSell
Data center:
https://apttosell.com/housing-subscription-data/

Calculator:
https://apttosell.com/cheongyak-score-calculator/

JSON:
https://raw.githubusercontent.com/cheer710815-hub/apttosell-subscription-data/main/housing_subscription_score_2026.json

Repository:
https://github.com/cheer710815-hub/apttosell-subscription-data

### Resimanor
Data center:
https://resimanor.com/housing-finance-dsr-data/

JSON:
https://raw.githubusercontent.com/cheer710815-hub/resimanor-housing-finance-data/main/stress_dsr_mortgage_examples_2026.json

Repository:
https://github.com/cheer710815-hub/resimanor-housing-finance-data

## Next action rule

Prioritize in this order:
1. Existing submitted open-source proposals
2. Public dataset catalogs
3. Institutional related-resource pages
4. Broken-link replacement
5. Educational resource adoption
6. Research / journalism citation

Do not create new outreach targets merely to increase the count.


### tae0y/real-estate-mcp PR #41
Type: Editorial open-source integration / reference-data inclusion
Status: PR_OPEN
PR:
https://github.com/tae0y/real-estate-mcp/pull/41
Issue:
https://github.com/tae0y/real-estate-mcp/issues/40
Opened:
2026-09-27
Changes:
- Added Korea housing subscription and stress DSR reference examples under resources/
- Linked AptToSell and Resimanor CSV/JSON datasets and methodology pages
- Updated custom instructions and README/README-ko discovery links
Why it matters:
- Maintainer explicitly requested a PR.
- If merged, links become part of an actively used Korean real-estate MCP project rather than a generic directory.
Next step:
- Wait for maintainer review after their stated availability window.
Priority: VERY HIGH


### etewiah/awesome-real-estate PR #81
Type: Curated global real-estate / proptech resource list
Status: PR_OPEN
PR:
https://github.com/etewiah/awesome-real-estate/pull/81
Opened:
2026-09-27
Changes:
- Added AptToSell Korea Housing Subscription Data under Asia > Authoritative Research & Publications
- Added Resimanor Korea Stress DSR Housing Finance Data in the same section
Why it matters:
- South Korea is already represented in the Asia section.
- The section already includes CC BY 4.0 housing datasets with downloadable CSV/JSON and documented methodology.
- Affiliation was disclosed in the PR as required by the contribution rules.
Next step:
- Wait for maintainer review / CI feedback.
Priority: VERY HIGH


### Deal-Scale/awesome-real-estate-investing PR #17
Type: Curated real-estate investing resource list
Status: PR_OPEN
PR:
https://github.com/Deal-Scale/awesome-real-estate-investing/pull/17
Opened:
2026-09-27
Changes:
- Added AptToSell Korea Housing Subscription Data under Authoritative Research & Publications
- Added Resimanor Korea Stress DSR Housing Finance Data in the same section
Why it matters:
- The repository explicitly welcomes PR contributions.
- The list includes analytics, foundational data, and authoritative research resources.
- Both submissions disclose maintainer affiliation and link directly to public data repositories.
Next step:
- Wait for maintainer review / CI feedback.
Priority: HIGH


### Seoul Cyber University MK Land legacy-link target
Type: .ac.kr academic related-sites replacement
Status: VERIFIED_TARGET
Target page:
https://estate.iscu.ac.kr/real/subMenu1/sub9.asp
Verified:
2026-09-27
Finding:
- The Department of Real Estate still lists MK랜드 as a related real-estate site.
- Current public search mainly surfaces legacy MK Land material from 1999, while a current standalone MK Land service at the listed domain could not be verified.
- Other entries such as 부동산써브 (serve.co.kr) and 텐 (ten.co.kr) still show current operating evidence and are not treated as broken links.
Replacement fit:
- AptToSell housing-subscription data center provides current structured housing/subscription reference data, CSV/JSON, methodology, and citation metadata.
Submission route:
- Seoul Cyber University operates a public admissions board and a separate department/major consultation board, but suitability for a related-site maintenance request needs confirmation before posting.
Next step:
- Use only the MK Land item for any future replacement proposal; do not claim serve.co.kr or ten.co.kr are broken.
Priority: VERY HIGH


### Seoul Cyber University AI Real Estate Big Data HousePalm stale-link target
Type: .ac.kr proptech resource-page replacement
Status: VERIFIED_TARGET
Target page:
https://redate.iscu.ac.kr/lab/lab04.asp
Verified:
2026-09-27
Finding:
- The AI Real Estate Big Data department's AI PropTech platform list still includes 하우스팜 at http://hauspalm.iisweb.co.kr/web/home/codding/index.php.
- The listed legacy URL is not currently accessible through public verification.
- Historical coverage shows HousePalm was a real-estate presale information platform in 2019.
- Current search results for housefarm.co.kr are a gardening / home-farming brand, not the former real-estate proptech service.
Replacement fit:
- AptToSell provides current South Korea housing-subscription/presale reference data, calculators, CSV/JSON, methodology, and citation metadata.
- The department already curates active real-estate data and proptech tools such as KB Real Estate, Korea Real Estate Board R-One, HF housing-finance statistics, court auction data, and public real-estate systems.
Next step:
- Find a public department consultation / suggestion route appropriate for resource-list maintenance; do not use admissions-only channels unless they explicitly accept department resource suggestions.
Priority: VERY HIGH


### Seoul Cyber University AI Real Estate Big Data resource inclusion target
Type: .ac.kr academic data-resource inclusion
Status: VERIFIED_TARGET
Target pages:
https://redate.iscu.ac.kr/lab/lab04.asp
https://redate.iscu.ac.kr/lab/lab01.asp
https://redate.iscu.ac.kr/lab/lab02.asp
Verified:
2026-09-27
Finding:
- The AI Real Estate Big Data department actively maintains AI Lab resource, market-trend, and AI/PropTech platform pages.
- The platform page curates public and private real-estate data sources such as Korea Real Estate Board R-One, HF housing-finance statistics, Seoul Open Data, public transaction data, court auction data, and major proptech services.
- The department also operates its own real-estate data center and posts externally supplied market materials.
- A stale legacy HousePalm real-estate platform link remains in the PropTech list, providing a possible replacement angle for AptToSell.
Resource fit:
- AptToSell offers structured South Korea housing reference data with CSV/JSON, methodology, and citation metadata suitable for education and analysis.
Submission route:
- No dedicated public external resource-submission form was verified.
- Do not use admissions-only channels unless the department explicitly accepts resource-maintenance requests there.
Next step:
- Look for a department-managed public contact, research-lab contact, partner/contact form, or other non-email route suitable for data-resource suggestions.
Priority: VERY HIGH

## 2026-09-29 profile, publishing, and dataset distribution

These placements were created as public identity, documentation, editorial, or dataset-distribution surfaces. They are not treated as substitutes for editorial/institutional backlinks.

### ORCID
Status: LIVE
Profile:
https://orcid.org/0009-0006-9445-4768
Notes:
- Public profile created.
- Resimanor and AptToSell website links added.
- Housing-finance / real-estate biography and keywords added.

### About.me
Status: LIVE
Profile:
https://about.me/eunk
Notes:
- Public profile updated for housing-finance / real-estate publishing.
- Resimanor and AptToSell links added.
- Resimanor set as the primary blog CTA.

### Gravatar
Status: LIVE
Profile:
https://gravatar.com/vegadus2
Notes:
- Resimanor and AptToSell public links added.
- GitHub, ORCID, LinkedIn, and Resimanor WordPress ownership connected/verified where supported.
- Threads verification deferred after provider-side verification failure.

### LinkedIn
Status: LIVE
Profile:
https://www.linkedin.com/in/%EC%9D%80%EC%A0%95-%EA%B9%80-b2073843b/
Notes:
- Headline and About section aligned with housing-finance / real-estate publishing.
- Contact info includes Resimanor, AptToSell, and Housing Data Korea.

### Hashnode — Housing Data Korea
Status: LIVE
Publication:
https://housingdatakorea.hashnode.dev/
Notes:
- Public Housing Data Korea publication created.
- First housing-finance / housing-subscription reference article published.
- Initial AutoMod archive was appealed and the article was restored to Published status.

### Medium
Status: LIVE
Profile handle:
@housingdatakorea
Notes:
- Profile cleaned to housing / real-estate focus.
- Unrelated legacy posts removed.
- Housing-finance / housing-subscription reference article published with contextual links to Resimanor and AptToSell.
- Exact article URL should be captured separately for monitoring.

### Substack — Housing Data Korea
Status: LIVE
Publication:
https://housingdatakorea.substack.com/
Published article:
https://housingdatakorea.substack.com/p/south-korea-housing-finance-and-subscription
Notes:
- Public profile and article created.
- Article links contextually to Resimanor and AptToSell.

### Kaggle
Status: LIVE
Notes:
- Public Resimanor housing-finance / Stress DSR dataset created from the GitHub repository.
- Public AptToSell housing-subscription dataset created from the GitHub repository.
- CC BY 4.0 selected.
- Dataset descriptions link back to the canonical data centers and GitBook documentation.
- Exact Kaggle dataset URLs should be captured separately for permanent monitoring.

Tracking rule:
- Keep these as supporting discovery/entity surfaces.
- Continue prioritizing editorial adoption, dataset catalogs, academic resource pages, and open-source integrations over accumulating generic profile links.

## 2026-09-30 monitoring update

### Google dataset structured data
Status: VALIDATED
Evidence:
- Google Search Console email confirmed the dataset structured-data fixes for description, license, and creator were validated for both resimanor.com and apttosell.com.
Notes:
- This supports discoverability of the canonical dataset pages in Google's dataset/search ecosystem.
- No additional structured-data repair is required for these three fields at this time.

### GitHub editorial/open-source proposals
Checked: 2026-09-30
Status:
- tae0y/real-estate-mcp PR #41 — OPEN, no new review comments.
- etewiah/awesome-real-estate PR #81 — OPEN, no new review comments.
- Deal-Scale/awesome-real-estate-investing PR #17 — OPEN, no new review comments.
- ssuksak/cheongyak-rag-mcp issue #1 — OPEN, no new maintainer response.
- dougdevitre/access-to-housing issues #7/#8 — OPEN, no new maintainer response.
- doorijaehyuk/korea-housing-mcp issue #1 — OPEN, no new maintainer response.
- emceeKim/korea-finance-mcp issue #2 — OPEN, no new maintainer response.
- sallim-app/korea-realty issue #1 — OPEN, no new maintainer response.
- verisworks-ai/naejipgak-mcp issue #1 — OPEN, no new maintainer response.
- happyendpointhq/awesome-real-estate-apis issue #2 — OPEN, no new maintainer response.

Action:
- Do not bump or add follow-up comments yet.
- Respect maintainer review windows and wait for a substantive response.

### Outreach monitoring
Checked: 2026-09-30
- MorFi: no new response after the 2026-09-26 review acknowledgment.
- The Real Deal data-directory suggestion: no reply detected.
- Data Is Plural dataset suggestion: no reply detected.
- HOFINET submission: no reply detected in the monitored inbox.

Action:
- No follow-up yet. Avoid repeated outreach unless a reasonable review period passes or a recipient requests clarification.

### Mendeley Data
Type: Research data repository / DOI citation
Status: LIVE
Dataset:
https://data.mendeley.com/datasets/shdpkfbj3c/1
DOI:
https://doi.org/10.17632/shdpkfbj3c.1
Verified:
2026-09-30
Why it matters:
- Provides a citable research-data record with a persistent DOI.
- The record links back to the canonical data/methodology page.
- CC BY 4.0 licensing and reproducibility notes are publicly visible.
Priority: VERY HIGH

### Hugging Face dataset
Type: Public dataset hub / machine-readable discovery
Status: LIVE
Dataset:
https://huggingface.co/datasets/eunguneun/korea-housing-subscription-score-2026
Verified:
2026-09-30
Observed downloads:
46
Why it matters:
- Public CC BY 4.0 dataset record is live and machine-readable.
- The dataset card links back to the canonical source/methodology.
- The repository is discoverable in the Hugging Face datasets ecosystem used by data/ML workflows.
Metadata note:
- The current Hugging Face metadata includes `region:us`, which is not appropriate for a South Korea dataset and should be removed or corrected when write access is available.
Priority: HIGH

### GitLab mirror/import
Type: Open-source repository mirror
Status: IMPORT_COMPLETED_URL_UNVERIFIED
Import:
apttosell-subscription-data
Verified:
2026-09-30
Evidence:
- GitLab import-completion email confirms the GitHub repository import finished successfully on 2026-09-25.
Constraint:
- The public project URL/visibility was not exposed in the completion email and could not be verified from public search.
Next step:
- Capture the final GitLab project URL from the GitLab import-history/project page before treating it as a live public backlink surface.
Priority: MEDIUM


### Mendeley Data — 2025–2026 competition determinants v1.0
Type: Research data repository / DOI mirror
Status: SUBMITTED_UNDER_REVIEW
Checked: 2026-10-09
Dataset:
AptToSell Presale Price Merit and First-Priority Competition Dataset, Korea, 2025–2026
Canonical Zenodo DOI:
https://doi.org/10.5281/zenodo.23258478
Dedupe finding:
- No matching Mendeley Data record for this exact 2025–2026 competition-determinants research object was found.
- Existing Mendeley record 10.17632/shdpkfbj3c.1 is for the separate housing-subscription score/deposit dataset and is not a duplicate.
Prepared package:
- apttosell_competition_determinants_MENDELEY_v1_0.zip
Guardrail:
- Treat Mendeley as an additional repository mirror of the same research object, not as a new analysis.
- Cross-link the Zenodo DOI and keep title, creator, ORCID, license and version aligned.
Reserved DOI:
https://doi.org/10.17632/ch8nxtnckc.1
Submitted:
2026-10-09
Current state:
- Dataset submitted successfully and is in Mendeley Data moderation.
- Platform states moderation is targeted within 2 business days.
Guardrail:
- Do not resubmit, create a duplicate record, or create a new version while moderation is pending.
Next step:
- Wait for Mendeley approval/rejection email. On approval, verify the live DOI and then add it to GitHub and AptToSell.
Priority: HIGH


### Data in Brief — competition determinants data article
Type: Peer-reviewed data article
Status: PREPARED_HOLD
Prepared: 2026-10-09
Research object:
- AptToSell Presale Price Merit and First-Priority Competition Dataset, Korea, 2025–2026
Canonical Zenodo DOI:
https://doi.org/10.5281/zenodo.23258478
Prepared assets:
- English data-article draft
- Cover letter
- Pre-submission checklist
Hold rule:
- Do not submit yet.
- Resume only after a relevant Mendeley Data approval/moderation email or related submission email is received and reviewed.
- Before any actual submission, re-check the current Data in Brief author guide and APC/open-access charge.
Priority: MEDIUM


### RePEc — Resimanor Housing Finance Research Notes
Type: Economics research index / institutional series
Status: LIVE
Verified: 2026-10-10
Archive handle:
RePEc:gyv
Series handle:
RePEc:gyv:resfin
Series page:
https://ideas.repec.org/s/gyv/resfin.html
First item:
https://ideas.repec.org/p/gyv/resfin/1.html
Author profile:
https://ideas.repec.org/f/pki717.html
Evidence:
- RePEc archive owner confirmed the archive was placed in production.
- IDEAS/RePEc now publicly lists the Resimanor series and the first research note.
- The first item is indexed under housing-finance-related JEL classes including G21, G28, R21 and R31.
Why it matters:
- This is an editorial/economics-index inclusion, not a generic profile backlink.
- RePEc links the author, series, publisher site and research note in a recognized economics discovery system.
Next step:
- Maintain the RePEc templates and add only substantive future Resimanor research notes.
- Do not create duplicate RePEc items for the same research object.
Priority: VERY HIGH


### Hugging Face — 2025–2026 competition determinants v1.0
Type: Public machine-readable dataset hub
Status: LIVE_VIEWER_PENDING
Verified: 2026-10-10
Dataset:
https://huggingface.co/datasets/eunguneun/korea-presale-price-competition-2025-2026
Canonical DOI:
https://doi.org/10.5281/zenodo.23258478
Notes:
- Public dataset repository is live.
- README dataset card, 7 release files, CC BY 4.0, English and South Korea tags are present.
- Dataset Viewer is still processing.
- GitHub README and AptToSell article now link to this mirror.
Guardrail:
- Zenodo remains the canonical citation identifier for v1.0.
- Do not duplicate this exact dataset under another Hugging Face repository.
Next step:
- Recheck Dataset Viewer after processing completes.
Priority: HIGH


## 2026-10-10 verification — competition dataset viewer and moderation

Research object: AptToSell Presale Price Merit and First-Priority Competition Dataset, Korea, 2025–2026.
Canonical citation Version DOI: https://doi.org/10.5281/zenodo.23258478 (unchanged).

- Hugging Face dataset: LIVE; Dataset Viewer now ACTIVE, confirmed on the public dataset page 2026-10-10. The displayed automatically combined `train` split has 321 rows and contains columns beyond the release's primary regression variables. **QA pending**: reconcile this displayed row count and configuration against MAIN=153 and SENSITIVITY=168 to prevent readers interpreting the 321 rows as a third, unique analytical sample. Do not create a duplicate repo or edit underlying data without verifying current release files.
- Hugging Face repository metadata API still returns `region:us` as of 2026-10-10 although README/YAML had been cleaned. **Metadata consistency review pending**; don't claim the repository-level tag is removed yet.
- Mendeley Data competition dataset: SUBMITTED_UNDER_REVIEW. Gmail searches in both cheer710815@gmail.com and vegadus2@gmail.com on 2026-10-10 for messages after 2026-10-08 related to Mendeley / ch8nxtnckc / Data in Brief returned no matches. No approval evidence; DOI 10.17632/ch8nxtnckc.1 remains reserved/unverified as live. No duplicate or resubmission.
- Data in Brief: PREPARED_HOLD. No submission until relevant Mendeley moderation/approval/submission email has been received and reviewed; recheck author guidelines and APC first.
- SchemaFinder: LIVE per project handoff; do not resubmit.
- RePEc Resimanor first paper: LIVE per prior production confirmation. Second distinct research note: PREPARATION/RESEARCH only, no duplicate or external submission.

Operational statuses for new entries: 신규 / 준비 / 발송완료 / 제출완료 / 심사중 / 거절 / 보류 / 종료. Record internal preparation separately from external submission. Check complete submission history, research object, platform, DOI and recipient/channel before each external action. Observational correlations/regressions must not be described as causal.

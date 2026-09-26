# Backlink Acquisition Tracker

Updated: 2026-09-26

This tracker records only legitimate editorial, institutional, open-data, and open-source adoption opportunities for AptToSell and Resimanor.

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
Status: READY_TO_SUBMIT
Verified catalog:
https://housing.pubpub.org/datasets
Verified submission path:
Public Airtable dataset submission form linked directly from the catalog.
Why it matters:
- Community-maintained catalog of housing, homelessness and related program datasets.
- Explicitly accepts both government and crowdsourced datasets.
- Official page provides a direct “submit a dataset” form.
Prepared files:
- AptToSell: external-submissions/universal-housing-dataset-catalog.md
- Resimanor: external-submissions/universal-housing-dataset-catalog.md
Blocker:
- Airtable form is interactive and its fields were not retrievable through the current connector/browser interface.
Priority: VERY HIGH

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
Status: WATCH
Why it matters:
- Explicitly invites users to suggest new housing/mortgage data sources and contribute to open datasets.
- Audience includes mortgage software developers, housing researchers and analysts.
Best fit:
- Resimanor stress DSR / mortgage-limit JSON and CSV
Priority: HIGH for Resimanor
Constraint:
- Public page confirms contribution intent, but a no-login direct submission form was not verified.

### The Real Deal — Directory of Real Estate Data Sites
Type: Curated real-estate data-source directory
Status: WATCH
Why it matters:
- Dedicated searchable directory of real-estate data sites.
- Explicitly invites suggestions.
Best fit:
- AptToSell / Resimanor repositories
Constraint:
- Suggestion route is email-only; do not use under current no-email outreach rule.

### Data Is Plural
Type: Curated dataset discovery newsletter/archive
Status: WATCH
Why it matters:
- Prefers free, bulk-downloadable, well-documented, directly linkable, fresh datasets.
- AptToSell and Resimanor match many of the stated dataset-quality criteria.
Constraint:
- Submission route is email-only; do not use under current no-email outreach rule.



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
Status: PREPARED
Why it matters:
- Actively maintained in 2026.
- Has an explicit Asia section with South Korea already represented.
- Includes analytics platforms, authoritative research/publications, calculators, APIs and open datasets.
- Contribution rules explicitly allow owner submissions if affiliation is disclosed.
- Requires evidence of usefulness beyond marketing; our GitHub repos, CSV/JSON, DOI, methodology and dated snapshots support that requirement.
Best fit:
- AptToSell: Asia > Authoritative Research & Publications / Analytics
- Resimanor: Asia > Authoritative Research & Publications / Mortgage & Financing (if category added)
Constraint:
- Pull request required; current connector cannot create a fork.

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

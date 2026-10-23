# South Korea Apartment Presale Rights Transactions: Regional and Size-Based Descriptive Statistics, September–October 2026

**Dataset status:** Published on Zenodo, 17 October 2026.  
**Creator:** AptToSell  
**Resource:** Dataset, version 2.0  
**Version DOI:** https://doi.org/10.5281/zenodo.23432291  
**All-versions DOI:** https://doi.org/10.5281/zenodo.23432290  
**Licence:** CC BY 4.0 (published aggregate tables and original documentation, subject to attribution).

## Scope and method

The published dataset summarises **980** person-to-person, broker-mediated presale-rights transactions in South Korea, selected from MOLIT-reported transactions without a cancellation indicator. Contracts were recorded in **September and October 2026**. It contains aggregate CSV tables grouped by (1) region, (2) contract month, (3) exclusive floor-area band, and (4) region × area band, plus accompanying documentation and QA metadata.

Each aggregate table describes the **same 980 observations**. Do not add counts across the four tables. Institutional-buyer and other transaction categories are excluded from this sub-sample. Original source jurisdiction names are retained and may require administrative-boundary validation.

### Research boundary

This is a **descriptive transaction-amount** dataset. MOLIT-reported transaction amounts must **not** be presented as resale premiums, sellers' profits, or price differences against original apartment offering prices. Those comparisons require further independent verification of transaction-price definitions and the original price schedules.

### Reuse and citation

Please cite the Zenodo dataset rather than assigning a new DOI to this GitHub overview:

> AptToSell (2026). *South Korea Apartment Presale Rights Transactions: Regional and Size-Based Descriptive Statistics, September–October 2026* (Version 2.0) [Dataset]. Zenodo. https://doi.org/10.5281/zenodo.23432291

**Primary public data origin:** Ministry of Land, Infrastructure and Transport (MOLIT), Republic of Korea, apartment presale-rights transaction records.

**Related but separate ongoing research:** [N01 presale-rights vs original offering-price linkage protocol](../presale-rights-original-price-gap-2026/RESEARCH-PROTOCOL.md). That protocol is not claimed as complete by publication of this aggregate dataset.

## Citation-ready factsheet

- **Verified regional and area-band statistics:** [FACTSHEET.md](FACTSHEET.md) — 980-record aggregate QA, interpretation caveats, and source CSV checksums. This is accompanying documentation for the existing v2.0 DOI, not a separate dataset.

## Discovery and reuse links

- **Primary citable record:** https://doi.org/10.5281/zenodo.23432291
- **Version family:** https://doi.org/10.5281/zenodo.23432290
- **AptToSell data catalog:** https://apttosell.com/housing-subscription-data/
- **Citation and reuse policy:** https://apttosell.com/citation-policy/
- **Machine-readable Schema.org metadata:** [dataset.jsonld](dataset.jsonld)
- **Citation File Format metadata:** [CITATION.cff](CITATION.cff)

Discovery note: Zenodo registers published record metadata with DataCite; this does not in itself establish that a third party has cited this dataset or that Google has indexed its landing page. Use the version-specific DOI when citing version 2.0. Do not assign a second DOI to this GitHub documentation.

## Archive file integrity check

Download the original four CSV files from the [Zenodo version 2.0 record](https://doi.org/10.5281/zenodo.23432291) into a local directory without editing or resaving them, then run:

```bash
python verify_archive_files.py /path/to/zenodo-v2-csvs
```

The [verification script](verify_archive_files.py) compares each file's SHA-256 to the four published digests in [FACTSHEET.md](FACTSHEET.md). It exits with code `0` only if all four files match. **This is a byte-level release-integrity test**, not a recalculation of aggregate statistics or an audit of record-level transactions. A differing hash can result from CSV normalization as well as a genuinely different file version; do not overwrite the expected values without a versioned provenance review.

## Aggregate reconciliation check

After downloading the **four unmodified version 2.0 CSV files** from [Zenodo](https://doi.org/10.5281/zenodo.23432291), run:

```bash
python verify_aggregates.py /path/to/zenodo-v2-csvs
```

The [aggregate reconciliation tool](verify_aggregates.py) checks expected row counts (15, 2, 4, 43), that each table's count sums independently to 980, that region and area-band margins of the 43-row cross-tab match the stand-alone tables, and that group labels are unique. It fails closed when the CSV header naming is ambiguous. The four CSVs represent **the same records**, not 3,920 independent observations.

**Verification boundary:** this check does not independently validate the 980 underlying transactions, the numerical medians, the official API XML, or source CSV file hashes (use [verify_archive_files.py](verify_archive_files.py) separately). The program has been tested with **synthetic fixtures**, not against the original Zenodo CSV files in this repository. It must not be described as a completed archival cross-tab audit until those files are actually processed.

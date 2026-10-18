# N01 API collector offline test — 2026-10-18

Tested GitHub collector at commit `1528d42a652f42273c9a8b519624d2f5fefea6da`, using a local copy.

- Python `py_compile`: **PASS**
- Mock XML with one item / totalCount=1: **PASS**; writes 1-row CSV and JSON manifest with SHA-256
- Mock XML with empty items / totalCount=0: **PASS**; writes header-only CSV and JSON manifest
- Mock API XML `resultCode=99`: **PASS**; raises expected error

**Important:** These tests mock `urllib.request.urlopen`, do not access MOLIT endpoints, and use synthetic data only. No authenticated API call or replication of 980 observations occurred. Page two and later, actual provider field names, response security and contract, de-duplication, cancellation filters, price definitions, and month/region completeness are still unverified. API key was not exposed or stored.

**Next QA:** test a two-page synthetic response; obtain real authenticated one-region/month API response; record response schema and source date; independently check totalCount, empty-result handling, duplicate records and the user-approved exact N01 filtering rule before any research-level counts are asserted.

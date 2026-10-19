# N01 collector regression test — 2026-10-19

Target source: `research/presale-rights-original-price-gap-2026/collect_molit_presale_rights.py` at blob SHA `2e58156cc505c571f34ffa279a6c1390070d9b31`.

Executed offline in Python with the **current code copied from GitHub**, using patched `urllib.request.urlopen`, synthetic XML payloads, and temporary output directories.

- Python `py_compile`: PASS
- Two pages containing one item each, totalCount=2: PASS
- Empty result (totalCount=0): PASS
- Premature empty page: PASS (expected error)
- TotalCount changes across pages: PASS (expected error)
- More rows than totalCount: PASS (expected error)
- API resultCode=99: PASS (expected error)
- Missing totalCount: PASS (expected error)

Caveats: no authenticated live MOLIT request was made. Tests do **not** validate source field schema, transaction identity, cancellation flags, reported price composition, pagination under true provider loads, or 980-row research cohort reproducibility. Raw duplicates remain preserved until source ID semantics are reviewed.

**Status**: offline regression PASS; production data acquisition NOT STARTED.

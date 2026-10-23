#!/usr/bin/env python3
"""Verify unmodified N01 v2.0 aggregate CSV downloads by SHA-256.

This tool checks archive integrity only. It does not independently validate
transactions, cross-tabulations, sampling, or Ministry API extraction.
"""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

EXPECTED = {
    "by_region.csv": "d271726cff919c7eb7d931593680041fb6c5a46117e3540f16f68dedb3c464f3",
    "by_month.csv": "a3c34dbbc6d2a58b00d3a4cda80d399fbece8a6adf68eb930f8d68a7d0746bdd",
    "by_area_band.csv": "2f03fb98fbb1a8606807df19c7c4064089a2faf0ab639c2e78aa17209304626a",
    "by_region_area_band.csv": "3aaa6cd0c247a61d1bf60664b64fdac8a9fe9a658a3f4dc0b72aa8daf87614c8",
}

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as file:
        for part in iter(lambda: file.read(1024 * 1024), b""):
            h.update(part)
    return h.hexdigest()

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="Directory containing original Zenodo v2.0 CSV files")
    args = parser.parse_args()
    good = True
    for name, digest in EXPECTED.items():
        path = args.directory / name
        if not path.is_file():
            print(f"MISSING {name}")
            good = False
            continue
        actual = sha256(path)
        ok = actual == digest
        good = good and ok
        print(f"{'PASS' if ok else 'MISMATCH'} {name} sha256={actual}")
    if good:
        print("All four archive files match the documented v2.0 SHA-256 hashes.")
        return 0
    print("Validation incomplete or failed. Do not treat modified files as v2.0 originals.")
    return 1

if __name__ == "__main__":
    raise SystemExit(main())

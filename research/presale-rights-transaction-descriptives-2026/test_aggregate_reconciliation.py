"""Synthetic regression tests for aggregate reconciliation; not source-data validation."""
import csv
import tempfile
import unittest
from pathlib import Path
import verify_aggregates as qa

def write_csv(folder, filename, columns, rows):
    with (folder / filename).open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        writer.writerows(rows)

def make_fixtures(folder):
    pairs = [(r, 0) for r in range(15)] + [(r, a) for r in range(15) for a in range(1, 4)][:28]
    counts = [1] * 43
    counts[0] += 937
    regions = {f"R{i}": 0 for i in range(15)}
    areas = {f"A{i}": 0 for i in range(4)}
    for (r, a), n in zip(pairs, counts):
        regions[f"R{r}"] += n
        areas[f"A{a}"] += n
    write_csv(folder, "by_region.csv", ["region", "n"], regions.items())
    write_csv(folder, "by_month.csv", ["month", "n"], [["202609", 590], ["202610", 390]])
    write_csv(folder, "by_area_band.csv", ["area_band", "n"], areas.items())
    write_csv(folder, "by_region_area_band.csv", ["region", "area_band", "n"],
              [(f"R{r}", f"A{a}", n) for (r, a), n in zip(pairs, counts)])

class AggregateTests(unittest.TestCase):
    def test_valid_synthetic_cross_tab(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            make_fixtures(p)
            self.assertEqual(qa.run(p), 0)

    def test_incorrect_region_margin_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            make_fixtures(p)
            fn = p / "by_region.csv"
            lines = fn.read_text().splitlines()
            lines[1] = "R0,940"
            lines[2] = "R1,5"
            fn.write_text("\n".join(lines) + "\n")
            with self.assertRaisesRegex(ValueError, "Region margin mismatch"):
                qa.run(p)

    def test_duplicate_cross_key_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            make_fixtures(p)
            fn = p / "by_region_area_band.csv"
            lines = fn.read_text().splitlines()
            lines[2] = ",".join(lines[1].split(",")[:2] + [lines[2].split(",")[2]])
            fn.write_text("\n".join(lines) + "\n")
            with self.assertRaisesRegex(ValueError, "Duplicate or empty cross key"):
                qa.run(p)

if __name__ == "__main__":
    unittest.main()

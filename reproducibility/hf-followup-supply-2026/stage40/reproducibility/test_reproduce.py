"""Unit tests for the public-data reproduction code. Run: python -m unittest -v"""
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
from decimal import Decimal
from reproduce import audit, counts, percent, C_BANDS, P_BANDS, PROJECT, SUMMARY, validate_downloaded_csv, download_if_absent

class ReproducibilityUnitTests(unittest.TestCase):
    def test_published_headline_arithmetic(self):
        self.assertEqual(percent(19,44),Decimal('43.18'))
        self.assertEqual(percent(13,36),Decimal('36.11'))
        self.assertEqual(percent(24,57),Decimal('42.11'))
        self.assertEqual(percent(20,46),Decimal('43.48'))

    def test_percentage_round_half_up(self):
        self.assertEqual(percent(1,8),Decimal('12.50'))
        self.assertEqual(percent(2,3),Decimal('66.67'))
        self.assertIsNone(percent(0,0))

    def test_case_insensitive_boolean_flags(self):
        r=[{'followup_supply_observed':'TRUE','eligible_60d_observation':' True ','followup_within_60d':'true'},
           {'followup_supply_observed':'false','eligible_60d_observation':'false','followup_within_60d':''}]
        self.assertEqual(counts(r),{'projects':2,'followup_projects':1,'eligible_60d':1,'followup_within_60d':1})

    def test_utf8_bom_project_header(self):
        data = ('\ufeffhouse_manage_no,project_name,source_url\n'
                '1,test,https://example.org\n').encode('utf-8')
        self.assertEqual(validate_downloaded_csv(data, PROJECT)[0], 'house_manage_no')

    def test_utf8_bom_summary_header(self):
        data = ('\ufeffmetric_group,segment,projects,followup_projects\n'
                'headline,x,1,0\n').encode('utf-8')
        self.assertEqual(validate_downloaded_csv(data, SUMMARY)[0], 'metric_group')

    def test_reject_html_without_writing_file(self):
        with self.assertRaisesRegex(RuntimeError, 'not expected CSV'):
            validate_downloaded_csv(b'<html>Temporary failure</html>', PROJECT)

    def test_validate_existing_file_without_network(self):
        with TemporaryDirectory() as td:
            path = Path(td) / PROJECT
            path.write_bytes(('\ufeffhouse_manage_no,project_name,source_url\n'
                             '1,test,https://example.org\n').encode('utf-8'))
            with patch('reproduce.urlopen', side_effect=AssertionError('network should not be used')):
                download_if_absent(path, PROJECT)

    def test_summary_band_mappings(self):
        self.assertEqual(len(C_BANDS),5)
        self.assertEqual(len(P_BANDS),5)
        self.assertEqual(len(set(C_BANDS.values())),5)
        self.assertEqual(len(set(P_BANDS.values())),5)

if __name__=='__main__':
    unittest.main()

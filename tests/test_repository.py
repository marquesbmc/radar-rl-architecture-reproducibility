import csv
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RepositoryTest(unittest.TestCase):
    def test_article_result_count(self):
        with (ROOT / 'results/article/sim_summary_article.csv').open(encoding='utf-8') as fh:
            rows = list(csv.DictReader(fh))
        self.assertEqual(18, len(rows))
        self.assertNotIn('per', {row['algorithm'] for row in rows})

    def test_expected_configs_exist(self):
        expected = {
            'training.json', 'simulation.json', 'standard_environment.json',
            'dense_restricted_environment.json', 'extensive_sparse_environment.json'
        }
        actual = {p.name for p in (ROOT / 'configs').glob('*.json')}
        self.assertTrue(expected.issubset(actual))


if __name__ == '__main__':
    unittest.main()

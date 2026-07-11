#!/usr/bin/env python3
"""Validate the consolidated article and supplementary result tables."""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTICLE = ROOT / 'results/article/sim_summary_article.csv'
PER = ROOT / 'results/experimental/per/sim_summary_per.csv'


def read_rows(path: Path):
    with path.open(encoding='utf-8', newline='') as fh:
        return list(csv.DictReader(fh))

article = read_rows(ARTICLE)
per = read_rows(PER)

errors = []
if len(article) != 18:
    errors.append(f'Expected 18 article rows, found {len(article)}')
if any(row.get('algorithm') == 'per' for row in article):
    errors.append('PER rows must not occur in the article result table')
if len({(row['architecture'], row['algorithm']) for row in article}) != 6:
    errors.append('Expected six architecture-algorithm configurations')
if set(row['scenario'] for row in article) != {'standard', 'dense_restricted', 'extensive_sparse'}:
    errors.append('The article table must contain the three reported scenarios')
if len(per) != 6:
    errors.append(f'Expected 6 supplementary PER rows, found {len(per)}')

if errors:
    for error in errors:
        print(f'ERROR: {error}')
    raise SystemExit(1)

print('Article result table: 18 rows, 6 configurations, 3 scenarios — OK')
print('Supplementary PER table: 6 rows — OK')

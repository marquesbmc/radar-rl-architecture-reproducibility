#!/usr/bin/env python3
"""Verify that the expected article-oriented repository structure is present."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md', 'REPRODUCIBILITY.md', 'CITATION.cff', 'LICENSE',
    'requirements.txt', 'environment.yml',
    'configs/training.json', 'configs/simulation.json',
    'results/article/sim_summary_article.csv',
    'notebooks/00_repository_overview.ipynb',
    'notebooks/03_results_analysis.ipynb',
]

missing = [path for path in REQUIRED if not (ROOT / path).exists()]
if missing:
    print('Missing required files:')
    for path in missing:
        print(f'  - {path}')
    sys.exit(1)

print('Repository structure: OK')
primary = [ROOT / 'notebooks/01_model_training.ipynb', ROOT / 'notebooks/02_model_simulation.ipynb']
if not all(path.exists() for path in primary):
    print('Primary research notebooks have not yet been populated. Run the migration utility.')
else:
    print('Primary research notebooks: present')

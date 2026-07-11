#!/usr/bin/env python3
"""Flag likely Portuguese text and absolute paths in Jupyter notebooks."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORDS = [
    'treinamento', 'simulacao', 'simulação', 'presa', 'predador', 'ambiente',
    'episodio', 'episódio', 'recompensa', 'grafico', 'gráfico', 'estatistica',
    'estatística', 'resultado', 'calcula', 'carrega', 'media', 'média'
]

issues = []
for path in sorted((ROOT / 'notebooks').rglob('*.ipynb')):
    notebook = json.loads(path.read_text(encoding='utf-8'))
    for number, cell in enumerate(notebook.get('cells', []), start=1):
        source = ''.join(cell.get('source', []))
        lowered = source.lower()
        matches = sorted({word for word in WORDS if word in lowered})
        if matches and cell.get('cell_type') == 'markdown':
            issues.append(f'{path.relative_to(ROOT)} cell {number}: Portuguese markers {matches}')
        if cell.get('cell_type') == 'code' and re.search(r'(?:[A-Za-z]:\\\\|/home/|/Users/|/content/drive/)', source):
            issues.append(f'{path.relative_to(ROOT)} cell {number}: absolute path')

if issues:
    print('\n'.join(issues))
    raise SystemExit(1)
print('Notebook English/path audit: OK')

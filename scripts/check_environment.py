#!/usr/bin/env python3
"""Print the runtime environment and optionally freeze installed packages."""

from __future__ import annotations

import argparse
import importlib
import platform
import subprocess
import sys
from pathlib import Path

PACKAGES = ['numpy', 'pandas', 'scipy', 'matplotlib', 'tensorflow', 'keras']

parser = argparse.ArgumentParser()
parser.add_argument('--freeze', type=Path)
args = parser.parse_args()

print(f'Python: {sys.version.split()[0]}')
print(f'Platform: {platform.platform()}')
for package in PACKAGES:
    try:
        module = importlib.import_module(package)
        print(f'{package}: {getattr(module, "__version__", "unknown")}')
    except Exception as exc:
        print(f'{package}: unavailable ({exc})')

if args.freeze:
    result = subprocess.run(
        [sys.executable, '-m', 'pip', 'freeze'],
        check=True,
        capture_output=True,
        text=True,
    )
    args.freeze.write_text(result.stdout, encoding='utf-8')
    print(f'Environment lock written to {args.freeze}')

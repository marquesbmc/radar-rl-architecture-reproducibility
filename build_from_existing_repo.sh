#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 PATH_TO_OLD_REPOSITORY" >&2
  exit 2
fi

python scripts/migrate_existing_repository.py --source "$1" --target .
python scripts/verify_repository.py
python scripts/validate_results.py
echo "Repository migration and validation completed. Review NOTEBOOK_AUDIT.md before publishing."

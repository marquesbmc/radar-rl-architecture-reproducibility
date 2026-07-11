param(
    [Parameter(Mandatory = $true)]
    [string]$Source
)

$ErrorActionPreference = "Stop"
python scripts/migrate_existing_repository.py --source $Source --target .
python scripts/verify_repository.py
python scripts/validate_results.py
Write-Host "Repository migration and validation completed. Review NOTEBOOK_AUDIT.md before publishing."

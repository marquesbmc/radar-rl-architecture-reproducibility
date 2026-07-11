# Publish this repository on GitHub

The target remote repository is:

```text
https://github.com/marquesbmc/radar-rl-architecture-reproducibility
```

## Option 1 — GitHub web interface

1. Create a new **public** repository named `radar-rl-architecture-reproducibility`.
2. Do not initialize it with a README, license, or `.gitignore`, because these files already exist here.
3. From this directory, run:

```bash
git remote add origin https://github.com/marquesbmc/radar-rl-architecture-reproducibility.git
git branch -M main
git push -u origin main
```

## Option 2 — GitHub CLI

After authenticating with `gh auth login`, run:

```bash
gh repo create marquesbmc/radar-rl-architecture-reproducibility \
  --public \
  --source=. \
  --remote=origin \
  --push
```

## Before release v1.0.0

- Add Bruno Marques Costa's corresponding-author e-mail and ORCID.
- Populate the primary training and simulation notebooks from the original repository.
- Validate execution in a clean Python 3.9 environment.
- Generate and commit `environment-lock.txt`.
- Review the CRediT contribution statement with all authors.
- Create tag `v1.0.0` and archive it in Zenodo.

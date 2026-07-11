# Reproducibility Guide

## Reproducibility levels

### Level 1 — Inspect the published artifacts

Use the trained models, figures, and consolidated result tables without running simulations. This level is suitable for checking the correspondence between repository artifacts and the manuscript.

### Level 2 — Re-run simulations

Use the trained model files and execute `notebooks/02_model_simulation.ipynb` for the three scenarios. Neural-network weights remain fixed and action selection uses greedy `argmax Q(s,a)`.

### Level 3 — Retrain and re-run

Execute `notebooks/01_model_training.ipynb`, save the resulting prey and predator models, execute the simulation notebook, and regenerate the consolidated metrics.

## Reported training parameters

| Parameter | Value |
|---|---|
| Episodes | 1,000 |
| Steps per episode per agent | 20 |
| Replay buffer | 1,000 transitions |
| Batch size | 64 |
| Network update | Once per episode |
| Exploration | Exponentially decaying epsilon-greedy |
| Optimizer | Adam |
| Learning rate | 0.0001 |
| Loss | Mean squared error |

The manuscript reports the epsilon-decay equation but does not provide numerical values for `epsilon_initial` and `epsilon_min`. It also does not report random seeds or exact package versions. These values must be recovered from the original notebook before claiming bit-for-bit reproduction.

## Reported simulation parameters

| Parameter | Value |
|---|---|
| Episodes | 1,000 |
| Steps per episode per agent | 10 |
| Weight updates | Disabled |
| Action selection | Greedy, `argmax Q(s,a)` |
| Main algorithms | DQN, Double DQN, Dueling DQN |
| Architectures | CNN–MLP, RADAR |

## Expected counts

The article dataset must contain:

- 6 architecture–algorithm configurations;
- 3 scenarios per configuration;
- 18 rows in `results/article/sim_summary_article.csv`;
- no PER rows in the article result file.

PER is retained as supplementary experimentation in `results/experimental/per/`.

## Recommended release process

1. Run the migration utility.
2. Review `NOTEBOOK_AUDIT.md`.
3. Run both primary notebooks from top to bottom in a clean environment.
4. Generate and commit `environment-lock.txt`.
5. Run all validation commands.
6. Create Git tag `v1.0.0`.
7. Publish a GitHub release.
8. Archive the release in a DOI-granting repository.
9. Replace the software URL in the manuscript with the release or DOI URL.

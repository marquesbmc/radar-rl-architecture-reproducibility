# Migration Guide

This package is designed to convert a local checkout of the original research repository into the article-oriented repository structure.

```bash
python scripts/migrate_existing_repository.py --source PATH_TO_OLD_REPOSITORY --target .
```

The source repository is not modified.

## Output mapping

| Original content | New location |
|---|---|
| Primary training notebook | `notebooks/01_model_training.ipynb` |
| Primary simulation notebook | `notebooks/02_model_simulation.ipynb` |
| Trained DQN/Double/Dueling models | `models/article/` |
| PER models | `models/experimental/per/` |
| Main simulations | `results/simulations/article/` |
| PER simulations | `results/simulations/experimental/per/` |
| Main training logs | `results/training/article/` |
| PER training logs | `results/training/experimental/per/` |
| Simulator implementation | `simulator/` |
| Article figures | `figures/` |

The migration utility produces an audit file instead of silently changing uncertain scientific content.

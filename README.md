# RADAR RL Architecture — Reproducibility Package

This repository contains the reproducibility materials associated with the manuscript:

> **RADAR: Attentional Architecture with Semantic-Derived Channel Fusion for Multi-Agent Environments**

RADAR (*Reinforced Attention for Dynamic Agent Relations*) extends a CNN–MLP baseline with two perceptual components:

- **C2FN — Cross-Channel Fusion Network**, which creates semantically meaningful derived channel compositions such as R+G, G+B, and R+B.
- **SALM — Spatial Attention via L2 and Mean Pooling**, which builds a spatial attention mask from complementary local and global statistics.

The experiments compare CNN–MLP and RADAR using DQN, Double DQN, and Dueling DQN in three partially observable predator–prey scenarios.

## Repository status

The repository is organized around Jupyter notebooks because the original training and simulation workflows were implemented as notebooks. A migration utility is included to copy the original notebooks, trained models, simulation logs, and training logs from the earlier research repository into this article-oriented structure.

The main manuscript evaluates **six model-pair configurations and eighteen simulations**. Prioritized Experience Replay (PER) artifacts are retained separately under `experimental/` and are not treated as part of the main article comparison.

## Quick reproduction

This route uses the trained models and consolidated results. It does not retrain the neural networks.

```bash
python -m venv .venv
```

Activate the environment:

```bash
# Linux/macOS
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Validate the repository:

```bash
python scripts/verify_repository.py
python scripts/validate_results.py
```

Start Jupyter Lab:

```bash
jupyter lab
```

Open the notebooks in this order:

1. `notebooks/00_repository_overview.ipynb`
2. `notebooks/02_model_simulation.ipynb`
3. `notebooks/03_results_analysis.ipynb`

The second notebook is populated by the migration utility described below.

## Populate the repository from the original project

From the root of this repository, run:

```bash
python scripts/migrate_existing_repository.py \
  --source ../radar-rl-architecture \
  --target .
```

The migration utility:

- renames the primary notebooks to an ordered English workflow;
- moves article models and PER models into separate locations;
- separates article simulations from experimental PER simulations;
- copies training logs and simulator source code;
- updates common relative paths inside notebook code cells;
- adds an English scientific header to each primary notebook;
- generates `NOTEBOOK_AUDIT.md` with any remaining absolute paths or Portuguese terms that require review.

No research result is deleted by the migration. Duplicated legacy notebooks are preserved under `notebooks/supplementary/legacy_duplicates/`.

## Full reproduction

The full route retrains the models before running the simulations:

1. Populate the repository with the migration utility.
2. Open `notebooks/01_model_training.ipynb`.
3. Confirm the parameters in `configs/training.json`.
4. Run the notebook from top to bottom.
5. Open `notebooks/02_model_simulation.ipynb`.
6. Run the three scenarios defined in `configs/`.
7. Run `notebooks/03_results_analysis.ipynb`.

Training can be computationally expensive. The manuscript reports the following reference hardware:

- Intel Core i9-9900K, 16 threads, 3.60 GHz
- 64 GB RAM
- NVIDIA GeForce RTX 3060, 12 GB
- Python 3.9.16

## Main experimental design

| Scenario | Grid | Obstacles | Prey | Predators |
|---|---:|---:|---:|---:|
| Standard | 10 × 10 | 10% | 10 | 5 |
| Dense and Restricted | 10 × 10 | 30% | 15 | 10 |
| Extensive and Sparse | 20 × 20 | 5% | 15 | 10 |

Main article configurations:

| Architecture | Algorithm |
|---|---|
| CNN–MLP | DQN |
| CNN–MLP | Double DQN |
| CNN–MLP | Dueling DQN |
| RADAR | DQN |
| RADAR | Double DQN |
| RADAR | Dueling DQN |

## Repository structure

```text
configs/       Experiment parameters reported in the manuscript
docs/          Architecture, data, and reproducibility documentation
figures/       Figures used in the manuscript
models/        Trained models, separated into article and experimental artifacts
notebooks/     Ordered notebook workflow
results/       Consolidated results, simulations, and training logs
scripts/       Migration, validation, environment, and analysis utilities
simulator/     Simulator source code copied from the original repository
tests/         Lightweight repository checks
```

## Dependency note

The manuscript records Python 3.9.16 and the use of NumPy, TensorFlow, Keras, and Matplotlib, but it does not record the exact package versions. `requirements.txt` therefore uses compatibility ranges rather than claiming unverified historical versions. After the original environment is successfully restored, run:

```bash
python scripts/check_environment.py --freeze environment-lock.txt
```

Commit the generated lock file before publishing release `v1.0.0`.

## Citation

The repository includes `CITATION.cff`. After the manuscript is accepted, update it with the journal volume, issue, pages, and DOI. A DOI-backed archive of release `v1.0.0` is recommended.

## Authors

The associated manuscript is authored by:

1. **Bruno Marques Costa** — Rio de Janeiro State University (UERJ), Rio de Janeiro, Brazil; GitHub: `marquesbmc`
2. **Rosa Maria Esteves Moreira da Costa** — Rio de Janeiro State University (UERJ), Rio de Janeiro, Brazil; ORCID: `0000-0001-6165-1649`
3. **Maria Clicia Stelling de Castro** — Rio de Janeiro State University (UERJ), Rio de Janeiro, Brazil; ORCID: `0000-0002-6315-1215`

The corresponding-author e-mail and Bruno Marques Costa's ORCID must be added before the journal submission and the archival release.

## License

The source code and repository utilities are released under the MIT License. Research figures and result tables remain attributable to the author and the associated manuscript.

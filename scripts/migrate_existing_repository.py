#!/usr/bin/env python3
"""Build the article-oriented repository from a local checkout of the legacy project."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path

PORTUGUESE_MARKERS = [
    "treinamento", "simulacao", "simulação", "presa", "predador", "ambiente",
    "episodio", "episódio", "recompensa", "modelo", "grafico", "gráfico",
    "estatistica", "estatística", "resultado", "carrega", "calcula", "media",
    "média", "coordenada", "proximidade", "efetividade", "tradicional"
]

MARKDOWN_REPLACEMENTS = {
    "Chromatic Fusion Network (CFN)": "Cross-Channel Fusion Network (C2FN)",
    "Spatial Attention Module (SAM)": "Spatial Attention via L2 and Mean Pooling (SALM)",
    "CFN module": "C2FN module",
    "SAM module": "SALM module",
}

PATH_REPLACEMENTS = {
    "../models/": "../models/article/",
    "../model/": "../models/article/",
    "../sim/": "../results/simulations/article/",
    "../train/": "../results/training/article/",
    "../fig/": "../figures/",
    "../support/sim_summary.csv": "../results/article/sim_summary_article.csv",
    "support/sim_summary.csv": "results/article/sim_summary_article.csv",
}

PRIMARY_NOTEBOOKS = {
    "model _training.ipynb": "01_model_training.ipynb",
    "model_training.ipynb": "01_model_training.ipynb",
    "model_simulator.ipynb": "02_model_simulation.ipynb",
}


def copy_tree(source: Path, target: Path) -> None:
    if not source.exists():
        return
    target.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target, dirs_exist_ok=True)


def article_header(title: str, purpose: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            f"# {title}\n",
            "\n",
            f"{purpose}\n",
            "\n",
            "This notebook is part of the RADAR article reproducibility package. ",
            "Run the cells in order and use paths relative to the repository root.\n",
        ],
    }


def patch_notebook(path: Path, title: str, purpose: str) -> list[str]:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    issues: list[str] = []

    notebook.setdefault("metadata", {})
    notebook["metadata"]["kernelspec"] = {
        "display_name": "Python 3.9 (RADAR)",
        "language": "python",
        "name": "python3",
    }
    notebook["metadata"].setdefault("language_info", {})["version"] = "3.9.16"

    cells = notebook.setdefault("cells", [])
    cells.insert(0, article_header(title, purpose))

    for index, cell in enumerate(cells):
        source = "".join(cell.get("source", []))
        if cell.get("cell_type") == "code":
            for old, new in PATH_REPLACEMENTS.items():
                source = source.replace(old, new)
            if re.search(r"(?:[A-Za-z]:\\\\|/home/|/Users/|/content/drive/)", source):
                issues.append(f"Absolute path in code cell {index + 1}")
        elif cell.get("cell_type") == "markdown":
            for old, new in MARKDOWN_REPLACEMENTS.items():
                source = source.replace(old, new)
            lowered = source.lower()
            matches = sorted({word for word in PORTUGUESE_MARKERS if word in lowered})
            if matches:
                issues.append(
                    f"Possible Portuguese text in markdown cell {index + 1}: {', '.join(matches)}"
                )
        cell["source"] = source.splitlines(keepends=True)

    path.write_text(json.dumps(notebook, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path, help="Local path to the original repository")
    parser.add_argument("--target", default=Path("."), type=Path, help="Target reproducibility repository")
    args = parser.parse_args()

    source = args.source.resolve()
    target = args.target.resolve()
    if not source.is_dir():
        raise SystemExit(f"Source repository not found: {source}")

    audit: list[str] = []

    # Primary notebooks
    source_notebooks = source / "notebooks"
    for original_name, new_name in PRIMARY_NOTEBOOKS.items():
        original = source_notebooks / original_name
        destination = target / "notebooks" / new_name
        if original.exists() and not destination.exists():
            shutil.copy2(original, destination)

    notebook_specs = {
        target / "notebooks" / "01_model_training.ipynb": (
            "Model Training", "Train prey and predator controllers for the CNN–MLP and RADAR architectures."
        ),
        target / "notebooks" / "02_model_simulation.ipynb": (
            "Model Simulation", "Evaluate trained controllers with fixed weights in the three reported scenarios."
        ),
    }
    for notebook_path, (title, purpose) in notebook_specs.items():
        if notebook_path.exists():
            audit.extend(f"{notebook_path.name}: {item}" for item in patch_notebook(notebook_path, title, purpose))
        else:
            audit.append(f"Missing primary notebook: {notebook_path.name}")

    # Supplementary notebooks; preserve duplicates rather than deleting them.
    support = source / "support"
    train = source / "train"
    canonical = [
        (support / "Estatistica_de_treinamento_nn.ipynb", target / "notebooks" / "supplementary" / "training_statistics.ipynb"),
        (support / "GRAFICO_TREINAMENTO.ipynb", target / "notebooks" / "supplementary" / "training_plots.ipynb"),
    ]
    for src, dst in canonical:
        if src.exists():
            shutil.copy2(src, dst)
    duplicates = target / "notebooks" / "supplementary" / "legacy_duplicates"
    duplicates.mkdir(parents=True, exist_ok=True)
    for root in [support, train]:
        if root.exists():
            for item in root.glob("*(1).ipynb"):
                shutil.copy2(item, duplicates / item.name)

    # Models
    model_dir = source / "model"
    if model_dir.exists():
        for item in model_dir.iterdir():
            if not item.is_file():
                continue
            destination = (
                target / "models" / "experimental" / "per" / item.name
                if "_per_" in item.name or item.name.endswith("_per.h5")
                else target / "models" / "article" / item.name
            )
            shutil.copy2(item, destination)

    # Simulation and training outputs
    sim_dir = source / "sim"
    if sim_dir.exists():
        for item in sim_dir.iterdir():
            destination_root = (
                target / "results" / "simulations" / "experimental" / "per"
                if "_per_" in item.name
                else target / "results" / "simulations" / "article"
            )
            if item.is_dir():
                copy_tree(item, destination_root / item.name)
            else:
                shutil.copy2(item, destination_root / item.name)

    train_dir = source / "train"
    if train_dir.exists():
        for item in train_dir.iterdir():
            if item.suffix.lower() == ".ipynb":
                continue
            destination_root = (
                target / "results" / "training" / "experimental" / "per"
                if "_per-" in item.name or "_per_" in item.name
                else target / "results" / "training" / "article"
            )
            if item.is_dir():
                copy_tree(item, destination_root / item.name)
            else:
                shutil.copy2(item, destination_root / item.name)

    # Simulator source. The output repository uses a generic English directory name.
    copy_tree(source / "p2rime", target / "simulator")

    # Preserve additional figures when they are not already provided by the article package.
    copy_tree(source / "fig", target / "figures" / "supplementary")

    audit_path = target / "NOTEBOOK_AUDIT.md"
    lines = ["# Notebook Audit", "", "Generated by the migration utility.", ""]
    if audit:
        lines.extend(f"- {entry}" for entry in audit)
    else:
        lines.append("No automatically detectable issues were found.")
    lines.extend([
        "",
        "The audit is conservative. Review all notebook markdown, comments, file paths, random seeds, and dependency versions before publishing the release.",
    ])
    audit_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Migration completed: {target}")
    print(f"Audit report: {audit_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

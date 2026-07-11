#!/usr/bin/env python3
"""Generate compact comparison charts from the article result table."""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'results/article/sim_summary_article.csv'
OUTPUT = ROOT / 'results/article/generated_figures'
OUTPUT.mkdir(parents=True, exist_ok=True)

frame = pd.read_csv(DATA)
metrics = [
    'combined_mean_successes',
    'combined_mean_collaborative_effectiveness',
    'combined_mean_unique_positions',
]

for metric in metrics:
    table = frame.pivot_table(
        index=['algorithm'], columns=['architecture'], values=metric, aggfunc='mean'
    )
    ax = table.plot(kind='bar')
    ax.set_title(metric.replace('_', ' ').title())
    ax.set_xlabel('Algorithm')
    ax.set_ylabel('Mean value across scenarios')
    plt.tight_layout()
    plt.savefig(OUTPUT / f'{metric}.png', dpi=200)
    plt.close()

print(f'Figures written to {OUTPUT}')

# Notebook Translation Audit

## Scope

Only Python comment tokens were translated from Portuguese into English.

The following content was intentionally preserved without modification:

- executable statements;
- variable, class, method, and function names;
- parameters and numerical values;
- file paths and model identifiers;
- string literals and runtime messages;
- notebook outputs;
- execution counts;
- notebook metadata;
- Markdown cells, which were already in English.

## Validation results

| Notebook | Comments translated | Executable content unchanged | Notebook format |
|---|---:|---|---|
| `01_model_training.ipynb` | 368 | Yes | Valid nbformat 4 |
| `02_model_simulation.ipynb` | 346 | Yes | Valid nbformat 4 |

The executable-token hashes of each original notebook and its translated version are identical after comment tokens are excluded.

## SHA-256

- `01_model_training.ipynb`: `a229860f2e1b1a458dc57eff8deaa7773b8a7cdea9ab3de6fd94f84aa2af2d73`
- `02_model_simulation.ipynb`: `d491b497f2b434ec48b01d760043883b6df8e0a72a621843bce4eb3ec75dc765`

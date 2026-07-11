# Result Data Dictionary

The main result table is `results/article/sim_summary_article.csv`.

- `simulation_id`: encoded simulation directory identifier.
- `model_name`: model-pair identifier.
- `scenario`: `standard`, `dense_restricted`, or `extensive_sparse`.
- `algorithm`: `dqn`, `double`, or `dueling` in the article table.
- `architecture`: `cnn_mlp` or `radar`.
- `*_total_successes`: total successful prey evasions, predator captures, or their sum.
- `*_mean_successes`: mean successes per episode.
- `*_harmonic_mean_successes`: harmonic mean of per-episode success measures.
- `*_median_successes`: median of per-episode success measures.
- `*_success_standard_deviation`: standard deviation of per-episode success measures.
- `*_mean_ally_proximity`: mean ally-proximity interaction measure.
- `*_mean_collaborative_effectiveness`: mean collaborative effectiveness measure.
- `*_mean_unique_positions`: mean number of unique visited positions.
- `*_total_positions`: total recorded position count.

Decimal values use a period as the decimal separator. The CSV delimiter is a comma.

# Reproducibility Limitations

The following information is not explicitly recorded in the manuscript:

- exact TensorFlow, Keras, NumPy, Pandas, SciPy, and Matplotlib versions;
- CUDA and cuDNN versions;
- random seeds;
- numerical values of `epsilon_initial` and `epsilon_min`;
- target-network update details and discount factor, unless they are present in the original notebook.

The migration and audit utilities are designed to recover these values from the original notebook where possible. The repository must not claim exact deterministic reproduction until these values have been confirmed and an environment lock file has been generated.

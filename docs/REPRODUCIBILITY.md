## Reproducibility Contract

Each training run must save:
- config used (YAML)
- git commit hash
- random seed
- metrics (jsonl)
- checkpoint (optional)

No run is considered valid unless it can be repeated from scratch.

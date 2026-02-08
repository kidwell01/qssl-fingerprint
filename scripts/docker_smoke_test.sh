#!/usr/bin/env bash
set -euo pipefail

IMAGE="allenlin316/qssl:latest"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
UIDGID="$(id -u):$(id -g)"

docker run --rm \
  --gpus all \
  -v "${REPO_ROOT}:/work" \
  -w /work \
  -u "${UIDGID}" \
  "${IMAGE}" \
  python - << 'PY'
import torch
print("torch:", torch.__version__)
print("cuda available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("gpu:", torch.cuda.get_device_name(0))
try:
    import qiskit
    print("qiskit:", qiskit.__version__)
except Exception as e:
    print("qiskit import FAILED:", e)
PY

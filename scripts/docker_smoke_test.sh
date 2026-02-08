#!/usr/bin/env bash
set -euo pipefail

IMAGE="qssl-modern:cuda12.4"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
UIDGID="$(id -u):$(id -g)"

docker run --rm \
  --gpus all \
  --ipc=host \
  -v "${REPO_ROOT}:/work" \
  -w /work \
  -u "${UIDGID}" \
  "${IMAGE}" \
  python - << 'PY'
import os, sys
import torch
print("torch:", torch.__version__)
print("cuda available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("gpu:", torch.cuda.get_device_name(0))

import qiskit
print("qiskit:", qiskit.__version__)

# Try importing the project's QNet (path used by upstream hybrid_resnet.py)
sys.path.append("upstream/QSSL/quantum-neural-network/qnn")
try:
    from qnet import QNet
    print("QNet import: OK")
except Exception as e:
    print("QNet import: FAILED", e)
PY

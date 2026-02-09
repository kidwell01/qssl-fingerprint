#!/usr/bin/env bash
set -euo pipefail

IMAGE="qssl-modern:cuda12.4"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

docker run --rm \
  --gpus all \
  --ipc=host \
  -v "${REPO_ROOT}:/work" \
  -w /work \
  "${IMAGE}" \
  python - << 'PY'
import sys, torch
print("torch:", torch.__version__)
print("cuda available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("gpu:", torch.cuda.get_device_name(0))

import qiskit
print("qiskit:", qiskit.__version__)

sys.path.append("upstream/QSSL/quantum-neural-network/qnn")
try:
    from qnet import QNet
    print("QNet import: OK")
except Exception as e:
    print("QNet import: FAILED", e)
PY

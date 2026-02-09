#!/usr/bin/env bash
set -euo pipefail

IMAGE="qssl-modern:cuda12.4"
NAME="qssl-jupyter"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

PORT="${1:-8888}"

docker run --rm -it \
  --name "${NAME}" \
  --gpus all \
  --ipc=host \
  -e TZ=Asia/Taipei \
  -p "${PORT}:8888" \
  -v "${REPO_ROOT}:/work" \
  -w /work \
  "${IMAGE}" \
  bash -lc "pip install -q jupyterlab && jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --NotebookApp.token='' --NotebookApp.password=''"

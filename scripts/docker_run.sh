#!/usr/bin/env bash
set -euo pipefail

IMAGE="qssl-modern:cuda12.4"
NAME="qssl-dev"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
UIDGID="$(id -u):$(id -g)"

docker run --rm -it \
  --name "${NAME}" \
  --gpus all \
  --ipc=host \
  --ulimit memlock=-1 \
  --ulimit stack=67108864 \
  -e TZ=Asia/Taipei \
  -v "${REPO_ROOT}:/work" \
  -w /work \
  -u "$(id -u)" \
  "${IMAGE}" \
  bash

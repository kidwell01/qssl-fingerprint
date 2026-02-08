#!/usr/bin/env bash
set -euo pipefail

IMAGE="allenlin316/qssl:latest"
NAME="qssl-dev"

# Repo root (this script lives in scripts/)
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Optional: map your UID/GID so created files aren't root-owned
UIDGID="$(id -u):$(id -g)"

echo "Repo: ${REPO_ROOT}"
echo "Image: ${IMAGE}"
echo "Container: ${NAME}"

docker run --rm -it \
  --name "${NAME}" \
  --gpus all \
  --ipc=host \
  --ulimit memlock=-1 \
  --ulimit stack=67108864 \
  -e TZ=Asia/Taipei \
  -e NVIDIA_VISIBLE_DEVICES=all \
  -v "${REPO_ROOT}:/work" \
  -w /work \
  -u "${UIDGID}" \
  "${IMAGE}" \
  bash

#!/usr/bin/env bash
set -euo pipefail

TAG="qssl-modern:cuda12.4"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

docker build \
  --build-arg USER_ID="$(id -u)" \
  --build-arg GROUP_ID="$(id -g)" \
  --build-arg USERNAME="dev" \
  -t "${TAG}" -f "${REPO_ROOT}/docker/Dockerfile" "${REPO_ROOT}"

echo "Built ${TAG}"

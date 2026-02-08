#!/usr/bin/env bash
set -euo pipefail

TAG="qssl-modern:cuda12.4"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

docker build -t "${TAG}" -f "${REPO_ROOT}/docker/Dockerfile" "${REPO_ROOT}"
echo "Built ${TAG}"

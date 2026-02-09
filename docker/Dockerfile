# Modern PyTorch CUDA runtime (supports recent GPUs)
FROM pytorch/pytorch:2.5.1-cuda12.4-cudnn9-runtime

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /work

# System deps (basic build tools + git + some common libs)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git curl ca-certificates build-essential \
    && rm -rf /var/lib/apt/lists/*

# Python deps: qiskit stack + extras
# (We keep it simple first; if your code needs more, we'll add)
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir \
      qiskit \
      qiskit-aer \
      qiskit-machine-learning \
      tqdm numpy scipy matplotlib pandas scikit-learn pillow opencv-python

# Sanity check during build (fail fast)
RUN python - << 'PY'
import torch
print("torch:", torch.__version__)
print("cuda available:", torch.cuda.is_available())
import qiskit
print("qiskit:", qiskit.__version__)
PY

CMD ["bash"]

# --- Create a non-root user matching the host UID/GID (prevents "I have no name!" and permission issues) ---
ARG USER_ID=1000
ARG GROUP_ID=1000
ARG USERNAME=dev

RUN set -eux; \
    # Create group if it doesn't exist
    if ! getent group "${GROUP_ID}" >/dev/null; then groupadd -g "${GROUP_ID}" "${USERNAME}"; fi; \
    # Create user if it doesn't exist
    if ! id -u "${USER_ID}" >/dev/null 2>&1; then useradd -m -u "${USER_ID}" -g "${GROUP_ID}" -s /bin/bash "${USERNAME}"; fi; \
    # Ensure /work is writable
    mkdir -p /work; \
    chown -R "${USER_ID}:${GROUP_ID}" /work

USER ${USERNAME}

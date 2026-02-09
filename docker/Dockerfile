FROM pytorch/pytorch:2.7.0-cuda12.8-cudnn9-runtime

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /work

# System deps (REQUIRED for OpenCV)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git curl ca-certificates build-essential \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    libxcb1 \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Python deps
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir \
        torchsummary \
        qiskit \
        qiskit-aer \
        qiskit-machine-learning \
        tqdm numpy scipy matplotlib pandas scikit-learn pillow opencv-python

# Sanity check (fail fast)
RUN python - << 'PY'
import torch, cv2, qiskit
print("torch:", torch.__version__)
print("cuda:", torch.cuda.is_available())
print("cv2:", cv2.__version__)
print("qiskit:", qiskit.__version__)
PY

# --- Non-root user ---
ARG USER_ID=1000
ARG GROUP_ID=1000
ARG USERNAME=dev

RUN set -eux; \
    if ! getent group "${GROUP_ID}" >/dev/null; then groupadd -g "${GROUP_ID}" "${USERNAME}"; fi; \
    if ! id -u "${USER_ID}" >/dev/null 2>&1; then useradd -m -u "${USER_ID}" -g "${GROUP_ID}" -s /bin/bash "${USERNAME}"; fi; \
    mkdir -p /work; \
    chown -R "${USER_ID}:${GROUP_ID}" /work

USER ${USERNAME}
CMD ["bash"]





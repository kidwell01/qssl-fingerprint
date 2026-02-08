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

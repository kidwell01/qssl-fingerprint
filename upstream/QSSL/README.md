# [Fingerprint Recognition Application by QSSL](https://drive.google.com/file/d/16863qm8BkkQ0m9mzlO3Egb69cDGrhXv_/view?usp=drive_link)

This is achieved using a PyTorch implementation of [SimCLR](https://arxiv.org/abs/2002.05709) based on https://github.com/facebookresearch/moco,
adapted so that the encoder consists of ResNet-18 followed by a representation network. Also, the QSSL method reference to [QSSL](https://github.com/bjader/QSSL)

* Fingerprint Preprocessing
    * dataset from [Sokoto Coventry Fingerprint Dataset(kaggle)](https://www.kaggle.com/datasets/ruizgara/socofing)

<img style="display: block; margin-left: auto; margin-right: auto;" alt="fingerprint image preprocessing" src="https://github.com/allenlin316/QSSL/assets/79969875/e6fc9e3b-566d-4567-ac7a-a1cc68c6cb0a">

* Training Architecture(adapted from [QSSL](https://github.com/bjader/QSSL))
<img style="display: block; margin-left: auto; margin-right: auto; width: 80%;" alt="fingerprint image preprocessing" src="https://github.com/allenlin316/QSSL/assets/79969875/d91016f7-7284-431f-a690-dd28bd1d414d">

### Fingerprint Image Preprocessing
1. Fingerprint Enhancement(Gabor Filter): Python implementation reference to author Utkarsh-Deshmukh [Fingerprint-Enhancement-Python](https://github.com/Utkarsh-Deshmukh/Fingerprint-Enhancement-Python)
    * **NOTE** must clone the [Fingerprint-Enhancement-Python](https://github.com/Utkarsh-Deshmukh/Fingerprint-Enhancement-Python) first
3. Fingerprint Canny Edge Detection

### Self-supervised Training with Classical Representation Network

```
python train_simclr.py --gpu 0 --lr 1e-3 -b 256 -d data/ -w 8 

Optional arguments:
--gpu            gpu_id
--lr             learning rate
-b               batch_size
-d               data_dir
-w               width of representation network
```

### Self-supervised Training with Quantum Representation Network

**NOTE** You must clone [quantum-neural-network](https://github.com/bjader/quantum-neural-network) and
add it to your sys/python path first.

```
python train_simclr.py -q --q_backend qasm_simulator --q_ansatz sim_circ_14_half -w 8 --classes 5 --save-batches --epochs 2

Optional arguments:
-q               Flag to use a quantum representation network
--q_backend      Qiskit backend to use (can include real quantum devices)
--q_ansatz       Variational ansatz for quantum neural network.
-w               Width of representation network, in this case the number of qubits.
--classes        Use the first N classes of the dataset
--save-batches   Save the model after each batch (rather than epoch by default)
--epochs         Number of epochs to train for (quantum training takes a long time)
```

The so called "ring" and "all-to-all" ansatzes used in the paper correspond to `--q_anzatz sim_circ_14_half` and `abbas`
in these options respectively.

### Linear Probing the Above Quantum Model

```
python linear_probe_simclr.py --pretrained model/selfsup/path_to_checkpoint_0000.path.tar -q --q_backend qasm_simulator --q_ansatz sim_circ_14_half -w 8 --classes 5

Optional arguments:
--pretrained     path_to_self_sup_model
```


## Reference

```
Jaderberg, B., Anderson, L.W., Xie, W., Albanie, S., Kiffner, M. and Jaksch, D., 2021. Quantum Self-Supervised Learning. arXiv preprint arXiv:2103.14653.
```

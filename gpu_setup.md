# Installing and testing GPU drivers on a virtual machine

This readme file details multiple strategies to install the necessary software to use GPUs on a virtual machine.

## Installation

### Google's Python Script

```bash
# get script
curl https://raw.githubusercontent.com/GoogleCloudPlatform/compute-gpu-installation/main/linux/install_gpu_driver.py --output install_gpu_driver.py
# execute script
sudo python3 install_gpu_driver.py
```

### Deep Learning VM's GPU installation 

When creating the instance select the disc image that already has installed CUDA and Pytorch. For more information visit [this](https://cloud.google.com/deep-learning-vm/docs/pytorch_start_instance?hl=en) link. **Make sure you add a metadata element: "install-nvidia-driver" with value "true"**. After creating the instance you need to SSH using the GCP webpage and accept the installation of the NVIDIA Drivers when asked.

### Docker image

Use a Docker container built using an image that has all the necessary software. Pytorch has multiple images with different versions of Cuda and Cudann. [This](https://hub.docker.com/layers/pytorch/pytorch/2.0.1-cuda11.7-cudnn8-devel/images/sha256-4f66166dd757752a6a6a9284686b4078e92337cd9d12d2e14d2d46274dfa9048?context=explore) is one of them.

```bash
# install docker
sudo apt install docker.io

# allow docker commands to be run without sudo
sudo chmod 666 /var/run/docker.sock

# pull the pytorch image with cuda and cuda nn
docker pull pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel

# check available images
docker images

# check running containers
docker ps

# install nvidia-container-toolkit
# source: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html

distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
      && curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
      && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \
            sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
            sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker

# run image with GPU (interactive mode)
docker run --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 --rm -it pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel

# run it with mounted files from the VM
docker run --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 --rm -it -v /home/yabra/llm:/mnt pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel

```

### Manual installation

Follow instructions from [here](https://cloud.google.com/compute/docs/gpus/install-drivers-gpu?hl=es-419) and [here](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html) to install CUDA in the VM.

Download the correct version of Cudann and then do:

```bash
tar -xf cudnn-linux-x86_64-8.7.0.84_cuda11-archive.tar.xz
sudo cp cuda/lib64/* /usr/local/cuda/lib64/
sudo cp cuda/include/cudnn.h /usr/local/cuda/include/
```

## Test installation

Finally we can test the correct installation by performing the following steps

1. Test the Nvidia drives through the bash terminal running: 

```bash
nvidia-smi
```

2. Install JAX and Numpyro

```bash
pip install --upgrade pip
# Installs the wheel compatible with CUDA 11 and cuDNN 8.6 or newer.
# Note: wheels only available on linux.
pip install --upgrade "jax[cuda]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
pip install numpyro
```

3. Test GPU inside Python with both Pytorch and JAX: 

```python
import torch
from jax.lib import xla_bridge
print(torch.cuda.is_available())
print(xla_bridge.get_backend().platform)
```
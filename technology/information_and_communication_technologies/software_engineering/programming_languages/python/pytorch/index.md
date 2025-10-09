# PyTorch

**PyTorch** is an open-source **machine learning framework** developed by **Meta AI (Facebook)** in 2016. It’s used for building and training neural networks with an emphasis on:

* **Flexibility:** Dynamic computation graphs (define-by-run)
* **Performance:** Built on optimized C/C++ backend (`ATen`, `TorchScript`, `LibTorch`)
* **Pythonic syntax:** Integrates seamlessly with NumPy, SciPy, and Python tooling.

PyTorch is one of the two dominant deep learning frameworks (alongside TensorFlow), and is widely used in both **research** and **production**.

---

## 2. PyTorch Core Concepts

| Concept                                      | Description                                                                                   |
| -------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **Tensor**                                   | The basic data structure. A multidimensional array (like NumPy ndarray) but with GPU support. |
| **Autograd**                                 | Automatic differentiation engine — tracks operations and computes gradients.                  |
| **nn.Module**                                | Base class for all neural network layers and models.                                          |
| **torch.optim**                              | Optimizers like SGD, Adam, RMSprop, etc.                                                      |
| **torch.utils.data**                         | Dataset and DataLoader utilities for handling and batching data.                              |
| **torchvision / torchaudio / torchtext**     | Domain-specific libraries for vision, audio, and NLP tasks.                                   |
| **TorchScript**                              | Allows serializing and optimizing models for production.                                      |
| **PyTorch Lightning / TorchRL / TorchServe** | Ecosystem tools for simplifying training loops, reinforcement learning, and deployment.       |

---

## 3. Key Use Cases

| Domain                                | Typical Applications                                                                          |
| ------------------------------------- | --------------------------------------------------------------------------------------------- |
| **Computer Vision**                   | Image classification, object detection, segmentation (using ResNet, Faster R-CNN, UNet, etc.) |
| **Natural Language Processing (NLP)** | Transformers, LLMs, translation, summarization (using Hugging Face Transformers, etc.)        |
| **Reinforcement Learning (RL)**       | Policy gradient, DQN, actor-critic algorithms.                                                |
| **Generative Models**                 | GANs, VAEs, diffusion models (used in Stable Diffusion).                                      |
| **Audio/Speech**                      | Speech recognition, voice synthesis (using torchaudio, Whisper, etc.)                         |
| **Scientific Computing**              | Physics-informed neural networks, simulations, numerical optimization.                        |

---

## 4. PyTorch Version Evolution

| Version                   | Key Features Introduced                                                                                  |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| **v0.4 (2018)**           | Unified `Tensor` and `Variable`; stable autograd.                                                        |
| **v1.0 (2019)**           | TorchScript and C++ frontend introduced.                                                                 |
| **v1.5–1.9**              | Distributed training improvements; quantization; mobile support.                                         |
| **v1.10–1.13**            | Better ONNX export, CUDA graphs, new compiler backend.                                                   |
| **v2.0 (2023)**           | Major update — introduced **`torch.compile()`**, **Dynamo**, and **AOTAutograd** for faster training.    |
| **v2.1–v2.3 (2024–2025)** | Improved performance, new attention kernels, and better integration with Hugging Face and Lightning.     |
| **Current (2025)**        | Enhanced support for **LLMs**, **Torch.AI**, and **quantized inference** for edge devices.               |

---

## 5. Core Classes and APIs for ML

### **Tensors**

```python
import torch
x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
y = torch.rand(2, 2)
z = x + y
```

### **Neural Network Layers (`torch.nn`)**

| Class                                 | Description           |
| ------------------------------------- | --------------------- |
| `nn.Linear`                           | Fully connected layer |
| `nn.Conv2d`                           | Convolution layer     |
| `nn.ReLU`, `nn.Sigmoid`, etc.         | Activation functions  |
| `nn.Dropout`, `nn.BatchNorm2d`        | Regularization layers |
| `nn.LSTM`, `nn.GRU`, `nn.Transformer` | Sequence modeling     |
| `nn.CrossEntropyLoss`, `nn.MSELoss`   | Loss functions        |

### **Optimizers (`torch.optim`)**

```python
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
```

### **Data Loading**

```python
from torch.utils.data import DataLoader, Dataset

class MyDataset(Dataset):
    def __init__(self, data, labels):
        self.data, self.labels = data, labels
    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]
    def __len__(self):
        return len(self.data)

loader = DataLoader(MyDataset(data, labels), batch_size=32, shuffle=True)
```

### **Model Definition**

```python
class SimpleNN(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(10, 1)
    def forward(self, x):
        return torch.sigmoid(self.fc(x))
```

---

## 6. Implementation Example (Training Loop)

Here’s a minimal training example using PyTorch:

```python
import torch
import torch.nn as nn
import torch.optim as optim

# Simple model
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(10, 5)
        self.fc2 = nn.Linear(5, 1)
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return torch.sigmoid(self.fc2(x))

# Data
X = torch.randn(100, 10)
y = torch.randint(0, 2, (100, 1)).float()

# Setup
model = Net()
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Training loop
for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(X)
    loss = criterion(outputs, y)
    loss.backward()
    optimizer.step()
    if epoch % 10 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item():.4f}')
```

---

## 7. PyTorch in Practice Today (2025)

* **Dominant in AI research** — nearly all academic papers use PyTorch.
* **LLMs:** Foundation for models like GPT, LLaMA, Mistral, etc.
* **Frameworks:** Integrated with Hugging Face, PyTorch Lightning, and FastAI.
* **Deployment:** With TorchScript, ONNX, and TorchServe for serving models.
* **Edge/Quantized AI:** PyTorch Mobile and ExecuTorch for on-device inference.
* **Distributed training:** Torch Distributed + FSDP for multi-GPU and cluster-scale training.

---

## 8. Learning Path (Recommended)

| Step | Topic                                         | Resources                                              |
| ---- | --------------------------------------------- | ------------------------------------------------------ |
| 1    | Python + NumPy basics                         | NumPy docs, W3Schools                                  |
| 2    | PyTorch fundamentals                          | [pytorch.org/tutorials](https://pytorch.org/tutorials) |
| 3    | Neural networks (nn.Module, loss, optimizers) | PyTorch official tutorials                             |
| 4    | Vision/NLP tasks                              | torchvision, torchtext                                 |
| 5    | Advanced training                             | PyTorch Lightning, mixed precision                     |
| 6    | Deployment                                    | TorchScript, ONNX, TorchServe                          |
| 7    | Research-level                                | Read papers with PyTorch codebases                     |

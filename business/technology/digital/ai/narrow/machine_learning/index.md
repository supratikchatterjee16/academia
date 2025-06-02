# Machine Learning

A subset of artificial intelligence that allows computers to learn from data without being explicitly programmed, enabling them to improve their performance and make predeictions or decisions based on that data.

Instead having specific instructions being programmed into it, the algorithms are trained on data to identify patterns and make predictions or decisions.

The core concept, is a unit called a "neuron". This is the fundamental processing units within neural networks. They are digitally analogue to the biological neurons we know of. Their basic function is to take one or multiple inputs and apply weights to them, and then sum these weighted inputs with a bias term. Yhe result is passed through an activation function which determines the neurons outputs. A group of interconnected neurons form a network called a neural network. "Learning" in machine learning occurs by adjusting the weights of the connections between neurons. This process is called as training.

A perceptron is an algorithm for supervised learning of binary classifiers. It shouldn't be confused with a neuron. It can be though of as a simple nerual network.


## Types of neurons

There are **types of neurons** in 3 senses:

### By Activation Function (How They Fire)

Neurons differ mainly by **how they activate** — that is, the activation function they use:

| Type of Neuron | Activation Function | Description |
|----------------|----------------------|-------------|
| **Linear**     | `f(x) = x`           | Passes value as-is (rarely used in hidden layers). |
| **ReLU**       | `f(x) = max(0, x)`   | Fast, simple, helps avoid vanishing gradients. Most common in deep nets. |
| **Leaky ReLU** | `f(x) = x if x>0 else 0.01x` | Like ReLU but allows small negative values. |
| **Sigmoid**    | `f(x) = 1 / (1 + e^(-x))` | Outputs between 0 and 1. Good for binary classification output. |
| **Tanh**       | `f(x) = (e^x - e^-x)/(e^x + e^-x)` | Outputs between -1 and 1. Better than sigmoid in many cases. |
| **Softmax**    | `softmax(xᵢ) = e^xᵢ / Σ e^xⱼ` | Used in output layers for multi-class classification. |
| **Swish / GELU / Mish** | Advanced activations | Used in recent architectures (e.g., Transformer, EfficientNet) for smoother gradients. |

### By Layer Type / Role

Neurons also vary depending on where they are in the network:

| Layer Type | Neuron Type | Description |
|------------|-------------|-------------|
| **Input Layer** | Input neurons | Just hold the input data — no activation. |
| **Hidden Layers** | Dense / Conv / RNN / etc. neurons | Do actual processing via weighted sums + activation functions. |
| **Output Layer** | Classification / Regression neurons | Use sigmoid/softmax for class labels or linear for regression. |

### By Function in Specialized Architectures

Some neurons are part of special structures:

- **Convolutional neurons** (CNN): Look at patches of the image and share weights.
- **Recurrent neurons** (RNN, LSTM, GRU): Have memory — they take current input and prior state.
- **Transformer neurons**: Use attention mechanisms to weigh input sequence relationships.
- **Residual neurons** (ResNet): Include skip connections to allow deeper networks.

### Biological vs. Artificial Neurons

| Biological Neuron | Artificial Neuron |
|-------------------|-------------------|
| Dendrites (input) | Input vector `x₁, x₂, ..., xₙ` |
| Soma (processing) | Weighted sum `z = w·x + b` |
| Axon (output)     | Activation `a = f(z)` |

Great question! Neural networks come in many **types**, each specialized for certain tasks like vision, language, time-series, or structured data. Here's a breakdown of the **most important types of neural networks**, categorized by their **architecture** and **use cases**:

## Core Types of Neural Networks

### 1. **Feedforward Neural Network (FNN)**
- **Structure**: Layers connected one after another; no loops.
- **Use case**: Basic classification, regression.
- **Example**: Predicting house prices, digit recognition.

Think of this as the "vanilla" neural network.

### 2. **Convolutional Neural Network (CNN)**
- **Structure**: Uses convolutional layers to detect patterns (like edges, textures) in images.
- **Use case**: Computer vision — image classification, object detection, facial recognition.
- **Popular models**: LeNet, AlexNet, VGG, ResNet, YOLO.

Great for images and spatial data.

### 3. **Recurrent Neural Network (RNN)**
- **Structure**: Has loops — output from previous steps fed into the next step.
- **Use case**: Sequential data — time-series forecasting, speech recognition, text generation.
- **Problem**: Vanishing gradient for long sequences.

Used when order **matters**.

### 4. **Long Short-Term Memory (LSTM) / GRU**
- **Structure**: Enhanced RNNs with memory cells to handle long-term dependencies.
- **Use case**: Translation, sentiment analysis, time-series prediction.

Solves the long-dependency problem of basic RNNs.

### 5. **Transformer**
- **Structure**: Uses attention mechanisms instead of recurrence to model sequences.
- **Use case**: NLP (language models like GPT, BERT), vision (ViT), audio.
- **Advantages**: Handles long sequences, parallelizable.

Currently dominates **language** and increasingly **vision** tasks.

### 6. **Autoencoder**
- **Structure**: Encoder compresses input → bottleneck → decoder reconstructs it.
- **Use case**: Dimensionality reduction, anomaly detection, denoising.

Learns compact representations of data.

### 7. **Generative Adversarial Network (GAN)**
- **Structure**: Two networks — Generator vs. Discriminator in a game.
- **Use case**: Image synthesis, style transfer, deepfakes, super-resolution.

GANs **generate** new data from noise.

### 8. **Radial Basis Function Network (RBFN)**
- **Structure**: Uses radial basis functions as activation.
- **Use case**: Function approximation, classification.
- **Less common** but interesting historically.

### 9. **Modular / Mixture of Experts**
- **Structure**: Combines multiple subnetworks specialized in different tasks.
- **Use case**: Complex tasks where multiple skills or views are useful.

### 10. **Spiking Neural Network (SNN)**
- **Structure**: Mimics the spiking nature of biological neurons.
- **Use case**: Neuromorphic computing (very low-power, brain-inspired).

Experimental and cutting-edge.

### Specialized Hybrids / Combinations

- **ConvLSTM**: For video data — combines CNNs (for spatial) + LSTMs (for time).
- **Vision Transformers (ViT)**: Transformer applied to image patches.
- **Reinforcement Learning Networks**: Often combine CNNs + RNNs with reward mechanisms.

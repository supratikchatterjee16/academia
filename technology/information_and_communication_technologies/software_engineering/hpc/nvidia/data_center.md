# NVIDIA Data Center

NVIDIA observes the AI Scaling Laws of:

1. Pre-training scaling
2. Post Training scaling
3. Test-Time scaling

### **1. Pre-training Scaling**

* **What it is:** Scaling laws that describe how **performance improves with model size, dataset size, or compute during pre-training**.
* **Key idea:** The same classic scaling laws apply: bigger models + more data + more compute → lower loss and better general representations.
* **Example:** GPT-3 was pre-trained on 175B parameters with 500B tokens—performance improves predictably with each scale-up.

---

### **2. Post-training Scaling**

* **What it is:** How **performance changes during fine-tuning or adaptation** after pre-training.
* **Key insights:**

  * Fine-tuning on task-specific data often has **diminishing returns** as dataset size increases.
  * Larger pre-trained models often **require fewer task-specific examples** to reach strong performance.
* **Related concept:** “Parameter-efficient fine-tuning” methods (LoRA, adapters) effectively scale post-training with fewer trainable parameters.

---

### **3. Test-time Scaling**

* **What it is:** Scaling at inference or evaluation:

  * **Prompt length**: In-context learning improves with more examples provided in the prompt.
  * **Ensemble/committee methods**: Using multiple forward passes or temperature scaling can improve results.
  * **Compute at test time**: Some methods (like sparse Mixture-of-Experts) activate more parameters dynamically at inference.
* **Key insight:** Performance can improve without retraining, simply by **adjusting inputs or inference compute**.

---

### **Summary Table**

| Stage         | What is scaled                               | How performance improves                               |
| ------------- | -------------------------------------------- | ------------------------------------------------------ |
| Pre-training  | Model size, data, compute                    | Classic scaling laws apply                             |
| Post-training | Fine-tuning dataset, parameters              | Diminishing returns; bigger models need fewer examples |
| Test-time     | Prompt examples, ensemble, inference compute | Emergent abilities can be leveraged without retraining |

---

This framework is useful because **not all scaling happens during pre-training**. Some capabilities only show up **after fine-tuning or with more test-time context**.

NVIDIA enables all 3 scaling laws.

Common AI Agentic UI use cases

- Data Processing
- CAD, CAE, SDA
- Computer Aided Drug Design
- Climate Simulation
- Quantum
- Robotics Industrial Digital Twins
- Enterprise AI

Addressable Enterprise Computing Challenges:

- Reasoning - due to increase in many intermediate "thinking" tokens to improve responses
- Larger models - Trillion parameter models and growing as pre-training continues
- Real-Time Latency - Serve many users simultaneously at fast token rates

## The Platform

NVIDIA's Data Center Platform contain the following:

- Hardwares
    - Grace Blackwell MGX Node(new massive GPU compute architecture created for datacenters)
        - Blackwell Ultra
            - GB300 NVL72
            - HGX B300 NVL16
        - Blackwell
            - GB200 NVL72
            - HGX B200
            - GB200 NVL4
    - NV Link Switch
    - Quantum Switch
        - Quantum-X800 InfiniBand
    - Spectrum-X Switch(for ethernet)
    - Chips purpose-built for AI Supercomputing
        - GPU
        - CPU(current important)
            - GH200 Superchip/NVL2
            - GB200 NVL4
            - GH200 NVL4
            - NVIDIA Grace CPU C1/Superchip
        - DPU
            - Bluefield-3
            - BlueField-3 + ConnectX-8 SuperNIC
        - NIC
            - ConnectX-8 SuperNIC
        - NVLink Switch
        - IB Switch
        - Enet Switch
- Softwares
    - NIM CUDA-Accelerated Agentic AI Libraries
    - Omniverse CUDA-Accelerated Physical AI Libraries
    - CUDA-X Libraries
    - Accelerated Software Stack
    - Orchestration Solution(Run:ai)
        - AI Lifecycle Integration
        - Resource management
        - Workload Orchestration
    - NVIDIA AI Enterprise
        - Models(Community, Partner, NVIDIA propreitary)
            - NVIDIA Llama Nemotron Models
    - NeMo tools
    - Magnum IO

## AI Factory

An **AI Factory** is a conceptual and operational framework for building, deploying, and continuously improving AI systems at scale. Think of it as an “industrial approach” to AI, where the goal is to make AI development **repeatable, efficient, and automated**, rather than treating each model or project as a one-off experiment.

Here’s a detailed breakdown:

---

### **Core Idea**

An AI Factory treats AI like a production line: raw materials (data) go in, undergo processing (training, testing, fine-tuning), and come out as deployable AI products or services. The goal is to make **AI development faster, cheaper, and more reliable**.

---

### **Key Components of an AI Factory**

1. **Data Pipelines**

   * Collect, clean, label, and structure massive datasets automatically.
   * Continuous ingestion of new data to improve models over time.

2. **Model Development & Training**

   * Standardized model architectures, pre-training, fine-tuning pipelines.
   * Automated hyperparameter tuning and architecture search.

3. **Testing & Evaluation**

   * Automated benchmarking for accuracy, fairness, robustness, and safety.
   * Continuous monitoring for model drift or degradation.

4. **Deployment & Scaling**

   * Seamless deployment to production systems (APIs, apps, robotics, etc.).
   * Scalable infrastructure to serve millions of users or requests.

5. **Feedback Loops**

   * Real-world usage generates data that feeds back into the system.
   * Enables continuous improvement without manual intervention.

---

### **Why It’s Important**

* Traditional AI development is slow, fragmented, and project-specific.
* An AI Factory **industrializes AI**:

  * Faster iteration cycles
  * Reusable models and components
  * Consistent quality across products

---

### **Analogy**

Imagine a car factory:

* **Data** = raw materials (metal, plastic, electronics)
* **AI models** = cars under assembly
* **Training pipelines** = robotic assembly lines
* **Testing & deployment** = safety inspections and delivery to dealerships

The AI Factory automates all these steps so that you can produce “AI cars” at scale.

## GPU Portfolio

Some of the GPUs provided by NVIDIA are:

- GB300
- GB200
- B200
- B100
- GH200
- H200
- H100
- H100 NVL
- H100 PCIe
- RTX Pro 6000
- L40S
- L4

These are ordered from strong in HPC, Training, and Inference to Strong in Visual Computing + Omniverse.

### Blackwell Ultra(newrst range of GPU)

Features:
- 1.5x more FP4 inference
- 50x AI Factory Output
- Upgraded NVL72 design for improved energy efficiency

*FP4 is 4 bit foating point precision  
*Dense refers to using all parameters of the model during computation

Blackwell Ultra GPU
- <= 288 GB HBM3e
- 15 FP dense
- 2.5x Hopper Architecture 

NVIDIA GB300 NVL72
- FP4(Dense): 1.1 ExaFLOPS
- HBM Memory: 20 TB
- Fast Memory: 40 TB
- Networking: 14.4 TB/s


### Hopper Arch(for AI & Compute Workloads)

- HGX H200 - 10kW per rack
    - In 8 and 4 GPU configurations
- H100/H200 NVL - provide air cooled flexibility, < 20kW Rack
    - 5kW rack with 4x H200 NVL
    - 8kW rack with 8x H200 NVL
- GH200 NVL2

Grace Hopper Architecture:

- GH200 Superchip combines the grace and hopper architectures
- 1 CPU: 1GPU node simple to manage and schedule for HPC, Enterprise and cloud

#### NVIDIA H200 NVL

- HPC PCIe Air-Cooled Solution
- As compared to H100
    - 1.5x more memory 
    - 1.2x more memory bandwidth
    - Llama 2 70B inference has been tested to be 1.5x faster
    - GPT-3 175B inference is 1.8x faster
- Builds upon Hopper Arch
- Supports upto 8 GPUs with NVLink flexibly

#### NVIDIA H100

- As compared to A100
    - 4PF FP8 - 6 times faster
    - 2PF FP16 - 3 times faster
    - 1PF TF32 - 3 times faster
    - 60TF FP64 - 3.4x faster
    - 3.35TB/s - 1.5x faster
    - 80GB HBM3 memory
- Has transformer model optimizations(6 times faster on the largest transfomer models)
- 7 fully isolated & secured instances, guaranteed QoS
- 2nd Gen MIG
- Confidential Computing
- 900 GB/s GPU-2-GPU connectivity
- 128GB/s PCI Gen 5

### RTX Pro 6000 Blackwell Server Edition

- 5th Gen Tensor
- 2nd Gen Transformer Engine
- FP4
- Full Media Pipeline: 4 NVENC/NVDEC/NVJPEG
- 4th Gen RTX(Raytracing), Neural Shaders, DLSS4
- 96GB GDDR7
- 1.6 TB/s Memory Bandwidth
- 128MB L2 Cache
- Multi-instance GPU(MIG)
- TEE confidential compute

### Ada Lovelace GPU(for Graphics and LLM acceleration)

- Powerful Ray-Tracing
    - Gen 3 RT Cores
- New Features
    - DLSS 3.0
    - Larger L2 Cache
    - Shader Execution Reordering
- Accelerated AI
    - Gen 4 Tensor Cores
    - FP8 precision
    - Optical Flow Accelerator
- Advanced Video Acceleration
    - Optimized AV1
- NVLink is not supported with Ada Lovelace GPUs

*These are projected specifications at this point in time.

#### NVIDIA L4 Tensor Core GPU

- For High Density Video Streams, Edge AI, and VDI
- 24GB Memory
- 1-slot LP
- 72W max power consumption

#### NVIDIA L40S GPU

- For GenAI, LLM Training, LLM Inference, Omniverse, Rendering, FP32 HPC
- 48 GB memory
- 2-slot FHFL
- 350W max power consumption

## CPU Portfolio

Some key facts:
- Data center electricity usage is more than 300TWh/year and is expected to increase from 2 to 5% by 2030.
- Accelerator Performance is increasing as CPU performance plateaus.

For accelerated workloads what is required of a CPU?

- High Single Thread Performance - Why?
- Low System level energy consumption
- "Branchy" collaboration between cores
- Predictable performance
- Enough threads to run all necessary services - on demand
- Massive memory bandwidth
- data locality
- great connectivity for CPU:GPU collaboration

### NVIDIA Grace: General Purpose Data Center CPU

- 72 core ARM Neoverse V2 CPU Cores
    - 4 x 128b SVE2 SIMD per core
    - 3.2 GHz base clock at 250 W
    - Configurable power including design points under 140 W
- NVIDIA Scalable Coherency Fabric
    - Single Compute Die Arch for incredible efficiency, predictability, and background data movement
    - 114 MB shared L3 cache
    - 3.2 TB/s bisection bandwidth between cores
    - 900 GB/s NVLink interfaces with Unified Address Space
    - Upto 512GB/s memory bandwidth with 16 W
    - 90% STREAM TRIAD efficiency
    - 64x PCIe Gen 5 with bonus lanes
- Comes in 2 configurations
    - 2 socket Grace CPU superchip(can have GPU)
    - single socket Grace C1

### NVIDIA Vera: Next Generation CPU

- 88 cores with spatial multi-threading(176 threads), provides twice the compute capability, and 2.4 times thread count vs Grace
- 5 times bandwidth per watt.
- Single NUMA design for optimal tuning out-of-box on different big data apps
- Upto 1.8 TB/s C2C CPU:GPU bandwidth vs PCIe Gen 6
- Compatible with ARM

### Throughput Workload Comparisons


Serial:

- Use case: Sparse Workloads not suited for parallel
- NVIDIA CPU vs x86:
    - Performance per $ : 1.6 times
    - Performance per Watt: 1.8 times
- NVIDIA CPU + GPU vs x86
    - Target Arch: CPU
    - Perf per $: Upto 1.6x CPU only

Mixed:

- Use case: Varied Manipulation of large datasets
- NVIDIA CPU vs x86:
    - Performance per $ : 1.2 times
    - Performance per Watt: 1.5 times
- NVIDIA CPU + GPU vs x86
    - Target Arch: CPU + GPU
    - Perf per $: Upto 5x+, accelerated with CUDA
    - 1.2x CPU only

Parallel:

- Use case: Parallel calculations
- NVIDIA CPU vs x86:
    - Performance per $ : 0.85 times
    - Performance per Watt: 1.1 times
- NVIDIA CPU + GPU vs x86
    - Target Arch: GPU
    - Perf per $: Upto 10x+, accelerated with CUDA

* All comparisons here are vs other x86 architecture CPU


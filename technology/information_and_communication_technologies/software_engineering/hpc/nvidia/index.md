# NVIDIA

**NVIDIA Corporation** is an American multinational technology company headquartered in Santa Clara, California.
It’s best known for:

* **GPUs (Graphics Processing Units)** → powering gaming, professional visualization, and AI
* **CUDA platform** → enabling General Purpose GPU (GPGPU) computing
* **AI and HPC solutions** → hardware + software stack for deep learning, simulation, and data centers

Today, NVIDIA is a leader in **AI computing, supercomputing, autonomous vehicles, and data center acceleration**.

---

## Short History of NVIDIA

* **1993** → Founded by Jensen Huang, Chris Malachowsky, and Curtis Priem.
* **1995** → First product: *NV1* graphics card (not very successful).
* **1999** → Launch of the **GeForce 256**, the world’s first "GPU".
* **2006** → Introduction of **CUDA**, revolutionizing GPGPU computing.
* **2010s** → GPUs adopted in **deep learning**, HPC, and scientific computing.
* **2017–2020** → Rise of **Volta, Turing, and Ampere architectures**, AI-focused with **Tensor Cores**.
* **2022+** → Release of **Hopper** and **Ada Lovelace architectures**, dominance in AI supercomputing (e.g., powering ChatGPT training clusters).
* **Today** → NVIDIA is central to **AI, HPC, robotics, data centers, and autonomous driving**.

---

## NVIDIA HPC Libraries & Software Ecosystem

NVIDIA provides a **comprehensive HPC software stack**, often bundled as part of **NVIDIA HPC SDK**.
These libraries accelerate **linear algebra, deep learning, signal processing, communication, and parallel programming**.

### Core HPC Libraries

* **cuBLAS** → GPU-accelerated BLAS (Basic Linear Algebra Subprograms).
* **cuSOLVER** → Dense & sparse linear algebra solvers (LU, QR, eigenvalue problems).
* **cuSPARSE** → Sparse matrix computations.
* **cuFFT** → Fast Fourier Transforms on GPUs.
* **cuRAND** → Random number generation (pseudo & quasi-random).
* **cuTENSOR** → High-performance tensor operations for HPC & AI.

### AI & Deep Learning Libraries

* **cuDNN** → Deep Neural Network primitives (convolutions, pooling, RNNs).
* **TensorRT** → Inference optimization and deployment.
* **NCCL (NVIDIA Collective Communications Library)** → Multi-GPU and multi-node communication (all-reduce, broadcast, etc.).

### HPC SDK & Tools

* **NVIDIA HPC SDK** → Compilers, libraries, and tools for C, C++, Fortran on GPUs/CPUs.

  * Includes **nvfortran, nvcc, nvc++** compilers.
* **Nsight Systems / Nsight Compute** → Profiling and debugging tools.
* **CUDA Toolkit** → Core developer toolkit with compiler, debugger, profiler, and libraries.

### Other HPC/AI Frameworks & Platforms

* **NVIDIA Magnum IO** → I/O and communication acceleration for HPC clusters.
* **NVIDIA Triton Inference Server** → Deploy trained AI models at scale.
* **NVIDIA Omniverse** → Simulation and collaboration platform (used in robotics, digital twins).
* **NVIDIA RAPIDS** → GPU-accelerated data science and analytics libraries (cuDF, cuML, cuGraph).

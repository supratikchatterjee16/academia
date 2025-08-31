# Accelerated Computing with CUDA on C/C++

This is a certified course within NVIDIA DLI.

The work done by GPU is assynchronous. The process needs to wait for synchronizing using ```cudaDeviceSynchronize()```.

Parts of a GPU function declaration for CUDA : 

```C
kernelName<<< #blocks, #threads_per_block >>>()
```

## Introduction

CUDA (Compute Unified Device Architecture) is **NVIDIA’s parallel computing platform and programming model**, released in 2007.
It lets developers use **NVIDIA GPUs for general-purpose computing (GPGPU)**, extending beyond graphics rendering into scientific computing, deep learning, data analytics, and more.

CUDA provides:

* A **C/C++/Fortran API** with GPU extensions (`__global__`, `__device__`, etc.)
* A **runtime** and **driver API** for GPU management
* Optimized **libraries** (cuBLAS, cuDNN, cuFFT, etc.)
* Compiler toolchain (NVCC)

### **Host vs Device**

* **Host** = CPU & system memory (RAM)
* **Device** = GPU & global memory (VRAM)
* CUDA programs split work between host and device.

### **Kernels**

* A **kernel** is a function executed on the GPU.
* Defined with `__global__` keyword in CUDA C/C++.
* Invoked with \[grid, block\] execution configuration syntax.

```cpp
__global__ void vectorAdd(float *a, float *b, float *c, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) c[i] = a[i] + b[i];
}
```

### **Thread Hierarchy**

CUDA organizes threads in a **grid–block–thread** model:

* **Thread**: smallest unit of execution
* **Block**: group of threads (1D/2D/3D)
* **Grid**: group of blocks (1D/2D/3D)

Each thread has unique IDs (`threadIdx`, `blockIdx`) to identify work.

### **Memory Hierarchy**

Different memory types with trade-offs:

* **Registers** (per-thread, fastest)
* **Shared memory** (per-block, low latency, useful for collaboration)
* **Global memory** (device-wide, high latency, but large)
* **Constant & texture memory** (special cached memories)

### **SIMT (Single Instruction, Multiple Thread)**

* Threads are executed in groups called **warps** (32 threads).
* All threads in a warp execute the same instruction (though divergence is possible).

### **Streams & Concurrency**

* **Streams** allow overlapping computation and data transfers.
* Enables pipelining (compute on one batch while transferring another).

---

### CUDA Version Evolution (Highlights)

NVIDIA has steadily expanded CUDA since 2007. Here are the key version milestones:

| **Version**                  | **Release Year** | **Key Features / Changes**                                                                         |
| ---------------------------- | ---------------- | -------------------------------------------------------------------------------------------------- |
| **1.0 (2007)**               | 2007             | First release, GPU programming in C, targeting Tesla architecture.                                 |
| **2.x (2008–2009)**          | 2008–09          | Double precision support, improved atomics, multi-GPU support.                                     |
| **3.x (2010–2011)**          | 2010–11          | Fermi architecture: unified cache, ECC memory, improved concurrency.                               |
| **4.x (2011)**               | 2011             | Unified Virtual Addressing (UVA), peer-to-peer GPU memory access.                                  |
| **5.x (2012)**               | 2012             | Kepler architecture: dynamic parallelism (kernels launch kernels), shuffle instructions.           |
| **6.x (2014)**               | 2014             | Maxwell support, Unified Memory (single address space across CPU+GPU).                             |
| **7.x (2015)**               | 2015             | Pascal architecture: NVLink, more Unified Memory improvements.                                     |
| **8.0 (2016)**               | 2016             | Pascal GPUs: half-precision (FP16), CUDA Graphs API.                                               |
| **9.x (2017)**               | 2017             | Volta architecture: Tensor Cores, warp-level primitives.                                           |
| **10.x (2018–2019)**         | 2018–19          | Turing architecture, enhanced Tensor Cores (mixed precision).                                      |
| **11.x (2020–2021)**         | 2020–21          | Ampere architecture, CUDA Python, expanded C++17 support.                                          |
| **12.x (2022–2023)**         | 2022–23          | Hopper architecture, FP8 precision, improved asynchronous execution, new memory models.            |
| **Latest (CUDA 12.5, 2024)** | 2024             | Hopper + Ada Lovelace optimizations, streamlined multi-GPU workflows, expanded cooperative groups. |

CUDA provided variables inside kernel, for describing executing thread, block and grid : 

1. gridDim.x : #blocks
2. blockIdx.x : id(or index) of current block
3. blockDim.x : #thread in block
4. threadIdx.x : id of current thread inside block

## Streaming Multiprocessors

NVIDIA GPUs contain functional units called Streaming Multiprocessors or SMs.

1. Blocks of threads are scheduled to run on SMs.
2. Depending on the number of SMs on a GPU and the requirements of a block more than one block can be scheduled on an SM.
3. Grid dimensions divisible by number of SMs on GPU can promote full SM utilization.


### Unified Memory behaviour

Defining of UM occurs through :  
```cudaMallocManaged```

It is where the GPU send the output to.

Behaviour : 

1. At UM alloc, it may not be resident initially on the CP or GPU
2. When some work asks for memory for the first time a page fault will occur
3. Page fault triggers migration of the demanded memory
4. Process repeats anytime the memory is requested somewhere in the system where it is not resident.
5. If it is known that the memory will be accessed somewhere it is not resident, asynchronous prefetching can be used using ```cudaMemPrefetchAsync(cpu)```
6. This moves the memory in larger batches and prevents page faulting.

### Concurrent CUDA Streams

CUDA kernels run in the default stream.
1 kernel must complete before the next kernel launch.
In any stream an instruction in it must complete before the next can begin.

However, Multiple streams can be made.
Instructions in the stream must run in sequence, whereas the kernels in different, **non-default** streams can interact concurrently.

Default stream is special, as it blocks all kernels in all other streams.

Creating a stream : 

```c
cudaStream_t stream;       // CUDA streams are of type `cudaStream_t`.
cudaStreamCreate(&stream); // Note that a pointer must be passed to 'cudaCreateStream'.

someKernel<<<number_of_blocks, threads_per_block, 0, stream>>>(); // `stream` is passed as 4th EC argument.

cudaStreamDestroy(stream); // Note that a value, not a pointer, is passed to 'cudaDestroyStream'
```

### Non-Unified Memory

Memory can be allocated directly to the GPU with ```cudaMalloc```.
Memory allocated in either of these ways can be copied to other locations using ```cudaMemCpy(HtoD)```.
Copying leaves 2 copied of it in the system.  


```cudaMemcpyAsync``` can asynchronously transfer memory over a **non-default** stream.

This can allow the overlapping memory copies and computation.

## More on Memory management

1. ```cudaMalloc``` will allocate memory directly to the active GPU. This prevents all GPU page faults. In exchange, the pointer it returns is not available for access by host code.
2. ```cudaMallocHost``` will allocate memory directly to the CPU. It also "pins" the memory, or page locks it, which will allow for asynchronous copying of the memory to and from a GPU. Too much pinned memory can interfere with CPU performance, so use it only with intention. Pinned memory should be freed with cudaFreeHost.
3. ```cudaMemcpy``` can copy (not transfer) memory, either from host to device or from device to host.

## Sample program

```C
#include <stdio.h>

void initWith(float num, float *a, int N)
{
  for(int i = 0; i < N; ++i)
  {
    a[i] = num;
  }
}

__global__
void addVectorsInto(float *result, float *a, float *b, int N)
{
  int index = threadIdx.x + blockIdx.x * blockDim.x;
  int stride = blockDim.x * gridDim.x;

  for(int i = index; i < N; i += stride)
  {
    result[i] = a[i] + b[i];
  }
}

void checkElementsAre(float target, float *vector, int N)
{
  for(int i = 0; i < N; i++)
  {
    if(vector[i] != target)
    {
      printf("FAIL: vector[%d] - %0.0f does not equal %0.0f\n", i, vector[i], target);
      exit(1);
    }
  }
  printf("Success! All values calculated correctly.\n");
}

int main()
{
  int deviceId;
  int numberOfSMs;

  cudaGetDevice(&deviceId);
  cudaDeviceGetAttribute(&numberOfSMs, cudaDevAttrMultiProcessorCount, deviceId);

  const int N = 2<<24;
  size_t size = N * sizeof(float);

  float *a;
  float *b;
  float *c;

  cudaMallocManaged(&a, size);
  cudaMallocManaged(&b, size);
  cudaMallocManaged(&c, size);

  initWith(3, a, N);
  initWith(4, b, N);
  initWith(0, c, N);

  size_t threadsPerBlock;
  size_t numberOfBlocks;

  threadsPerBlock = 256;
  numberOfBlocks = 32 * numberOfSMs;

  cudaError_t addVectorsErr;
  cudaError_t asyncErr;

  addVectorsInto<<<numberOfBlocks, threadsPerBlock>>>(c, a, b, N);

  addVectorsErr = cudaGetLastError();
  if(addVectorsErr != cudaSuccess) printf("Error: %s\n", cudaGetErrorString(addVectorsErr));

  asyncErr = cudaDeviceSynchronize();
  if(asyncErr != cudaSuccess) printf("Error: %s\n", cudaGetErrorString(asyncErr));

  checkElementsAre(7, c, N);

  cudaFree(a);
  cudaFree(b);
  cudaFree(c);
}
```

Running :

```bash
nvcc -o vector-add-no-prefetch 01-vector-add/01-vector-add.cu -run
```

Profiling : 

```bash
nsys profile --stats=true -o vector-add-no-prefetch-report ./vector-add-no-prefetch
```

## Sample Prefetching

Changes in main : 
```c
int main()
{
  int deviceId;
  int numberOfSMs;

  cudaGetDevice(&deviceId);
  cudaDeviceGetAttribute(&numberOfSMs, cudaDevAttrMultiProcessorCount, deviceId);

  const int N = 2<<24;
  size_t size = N * sizeof(float);

  float *a;
  float *b;
  float *c;

  cudaMallocManaged(&a, size);
  cudaMallocManaged(&b, size);
  cudaMallocManaged(&c, size);

  initWith(3, a, N);
  initWith(4, b, N);
  initWith(0, c, N);

  cudaMemPrefetchAsync(a, size, deviceId);
  cudaMemPrefetchAsync(b, size, deviceId);
  cudaMemPrefetchAsync(c, size, deviceId);

  size_t threadsPerBlock;
  size_t numberOfBlocks;

  threadsPerBlock = 256;
  numberOfBlocks = 32 * numberOfSMs;

  cudaError_t addVectorsErr;
  cudaError_t asyncErr;

  addVectorsInto<<<numberOfBlocks, threadsPerBlock>>>(c, a, b, N);

  addVectorsErr = cudaGetLastError();
  if(addVectorsErr != cudaSuccess) printf("Error: %s\n", cudaGetErrorString(addVectorsErr));

  asyncErr = cudaDeviceSynchronize();
  if(asyncErr != cudaSuccess) printf("Error: %s\n", cudaGetErrorString(asyncErr));

  checkElementsAre(7, c, N);

  cudaFree(a);
  cudaFree(b);
  cudaFree(c);
}
```

## Kernelized  initialization

Changes : 

```C
__global__
void initWith(float num, float *a, int N)
{

  int index = threadIdx.x + blockIdx.x * blockDim.x;
  int stride = blockDim.x * gridDim.x;

  for(int i = index; i < N; i += stride)
  {
    a[i] = num;
  }
}

.
.
.
.
.
.

int main()
{
  int deviceId;
  int numberOfSMs;

  cudaGetDevice(&deviceId);
  cudaDeviceGetAttribute(&numberOfSMs, cudaDevAttrMultiProcessorCount, deviceId);

  const int N = 2<<24;
  size_t size = N * sizeof(float);

  float *a;
  float *b;
  float *c;

  cudaMallocManaged(&a, size);
  cudaMallocManaged(&b, size);
  cudaMallocManaged(&c, size);

  cudaMemPrefetchAsync(a, size, deviceId);
  cudaMemPrefetchAsync(b, size, deviceId);
  cudaMemPrefetchAsync(c, size, deviceId);

  size_t threadsPerBlock;
  size_t numberOfBlocks;

  threadsPerBlock = 256;
  numberOfBlocks = 32 * numberOfSMs;

  cudaError_t addVectorsErr;
  cudaError_t asyncErr;

  initWith<<<numberOfBlocks, threadsPerBlock>>>(3, a, N);
  initWith<<<numberOfBlocks, threadsPerBlock>>>(4, b, N);
  initWith<<<numberOfBlocks, threadsPerBlock>>>(0, c, N);

  addVectorsInto<<<numberOfBlocks, threadsPerBlock>>>(c, a, b, N);

  addVectorsErr = cudaGetLastError();
  if(addVectorsErr != cudaSuccess) printf("Error: %s\n", cudaGetErrorString(addVectorsErr));

  asyncErr = cudaDeviceSynchronize();
  if(asyncErr != cudaSuccess) printf("Error: %s\n", cudaGetErrorString(asyncErr));

  checkElementsAre(7, c, N);

  cudaFree(a);
  cudaFree(b);
  cudaFree(c);
}
```



# High Powered Computing

Refer [Wikipedia](https://en.wikipedia.org/wiki/Parallel_computing)

Frequency scaling was the dominant reason for improvements in computer performance from the mid-1980s until 2004. The runtime of a program is equal to the number of instructions multiplied by the average time per instruction. Maintaining everything else constant, increasing the clock frequency decreases the average time it takes to execute an instruction. An increase in frequency thus decreases runtime for all compute-bound programs. However, power consumption P by a chip is given by the equation $P = C × V^2 × F$, where C is the capacitance being switched per clock cycle (proportional to the number of transistors whose inputs change), V is voltage, and F is the processor frequency (cycles per second).[10] Increases in frequency increase the amount of power used in a processor. Increasing processor power consumption led ultimately to Intel's May 8, 2004 cancellation of its Tejas and Jayhawk processors, which is generally cited as the end of frequency scaling as the dominant computer architecture paradigm.

To deal with the problem of power consumption and overheating the major central processing unit (CPU or processor) manufacturers started to produce power efficient processors with multiple cores. The core is the computing unit of the processor and in multi-core processors each core is independent and can access the same memory concurrently. Multi-core processors have brought parallel computing to desktop computers. Thus parallelization of serial programs has become a mainstream programming task. In 2012 quad-core processors became standard for desktop computers, while servers had 10+ core processors. By 2023 some processors had over hundred cores. Some designs having a mix of performance and efficiency cores (such as ARM's big.LITTLE design) due to thermal and design constraints. o deal with the problem of power consumption and overheating the major central processing unit (CPU or processor) manufacturers started to produce power efficient processors with multiple cores. The core is the computing unit of the processor and in multi-core processors each core is independent and can access the same memory concurrently. Multi-core processors have brought parallel computing to desktop computers. Thus parallelization of serial programs has become a mainstream programming task. In 2012 quad-core processors became standard for desktop computers, while servers had 10+ core processors. By 2023 some processors had over hundred cores. Some designs having a mix of performance and efficiency cores (such as ARM's big.LITTLE design) due to thermal and design constraints. From Moore's law it can be predicted that the number of cores per processor will double every 18–24 months.

An operating system can ensure that different tasks and user programs are run in parallel on the available cores. However, for a serial software program to take full advantage of the multi-core architecture the programmer needs to restructure and parallelize the code. A speed-up of application software runtime will no longer be achieved through frequency scaling, instead programmers will need to parallelize their software code to take advantage of the increasing computing power of multicore architectures.


## Laws

### Amdahl's Law

Used for calculating maximum potntial speeedup of an overall system.

> the overall performance improvement gained by optimizing a single part of a system is limited by the fraction of time that the improved part is actually used

It defines `speedup` of a system as:

$$
speedup = \frac{execution time for the entire task wihhout enhancements}{excution time for the same task when enhancements are applied}
$$

Amdahl's law can be frmulated in the following way:

$$
speedup_{overall} = \frac{1}{ (1 - time_{optimized}) + \frac{time_{optimized}}{speedup_{optimized}} }
$$

Implications of Amdahl's law:

- Diminishing Returns: Adding more processors gives diminishing returns. Beyond a certain point, adding more processors doesn't significantly increase speedup.
- Limited Speedup: Even with many processors, there's a limit to how much faster a task can be completed due to parts of the task that cannot be parallelized.

Limitation:

- Assumption of Fixed Workload: Amdahl's Law assumes that the workload remains constant. It doesn't account for dynamic or increasing workloads, which can impact the effectiveness of parallel processing.
- Overhead Ignored: Amdahl's Law neglects overheads associated with concurrency, including coordination, synchronization, inter-process communication, and concurrency control. Notably, merging data from multiple threads or processes incurs significant overhead due to conflict resolution, data consistency, versioning, and synchronization. [9]
- Neglecting extrinsic factors: Amdahl's Law addresses computational parallelism, neglecting extrinsic factors such as data persistence, I/O operations, and memory access overheads, and assumes idealized conditions.
- Scalability Issues: While it highlights the limits of parallel speedup, it doesn't address practical scalability issues, such as the cost and complexity of adding more processors.
- Non-Parallelizable Work: Amdahl's Law emphasizes the non-parallelizable portion of the task as a bottleneck but doesn’t provide solutions for reducing or optimizing this portion.
- Assumes Homogeneous Processors: It assumes that all processors are identical and contribute equally to speedup, which may not be the case in heterogeneous computing environments.

### Gustafson's Law(aka Gustafson-Barsis's Law)

It gives the speedup in the execution time of a task that theoretically gains from parallel computing, using a hypothetical run of the task on a single-core machine as the baseline. To put it another way, it is the theoretical "slowdown" of an already parallelized task if running on a serial machine.

$$
S = s + p * N,
$$

where,

$S$ is the Speedup  
$N$ is the number of processors  
$s$ and $p$ are the fractions of time spent executing the serial and parallel parts of the program, i.e. $s + p = 1$

### Universal Scalability Law
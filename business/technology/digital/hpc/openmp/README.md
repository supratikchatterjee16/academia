# OpenMP API

Open Message Passing Appliation Programming Interface.

OpenMP is an API that supports multi-platfor shared-memory multiproessing programming iin C, C++, and Fortran, on several platforms.

It is manaed by the nonpoffit tecch cconsrtium OpenMP Architecture Review Board, and includes vendors such as ARM, AMD, IBM, Cray, Intel, HP, Fujitsu, NVIDIA, NEC, Red Hat, Texas Instruments, and Oracle Corporation.

OpenMP is an implementation of multithreading, a method of parallelizing whereby a primary thread (a series of instructions executed consecutively) forks a specified number of sub-threads and the system divides a task among them. The threads then run concurrently, with the runtime environment allocating threads to different processors.


## How to use

Include `omp.h`, and use the pragmas defined by the library. OpenMP pragmas begin with `#pragma omp ...`.

Some pragmas:

```c++
#pragma omp parallel
#pragma omp parallel for

```
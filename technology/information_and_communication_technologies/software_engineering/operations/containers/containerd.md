# containerd

**containerd** is an industry-standard container runtime that manages the complete container lifecycle on a host system. It is designed to provide core functionalities for running and managing containers, such as image management, container execution, and storage and network interfaces, without including higher-level orchestration features. It is widely used as the runtime behind platforms like **Docker** and **Kubernetes**.

## **Short History**

* **2015**: Docker spun out **containerd** as a separate project to isolate the core container runtime functionality from Docker’s higher-level tooling.
* **2017**: containerd became a **CNCF (Cloud Native Computing Foundation) project**, gaining community governance and standardization.
* **2018–Present**: It has matured as a stable runtime, integrated deeply with Kubernetes (as a CRI – Container Runtime Interface implementation) and other container platforms.

Essentially, containerd evolved from being a component inside Docker to becoming a standalone, robust runtime that other systems can rely on.

## **Usages**

1. **Container Execution**: Runs containers on Linux and Windows hosts, handling namespaces, cgroups, and container processes.
2. **Image Management**: Pulls, pushes, and stores container images from registries.
3. **Storage and Networking**: Manages container filesystem layers and networking plugins.
4. **Kubernetes Integration**: Acts as a CRI-compatible runtime, often used with **CRI-O** or **Docker shim**.
5. **Cloud-Native Applications**: Provides a lightweight runtime for cloud platforms requiring fast container startup and lifecycle management.

## **Core Concepts**

1. **Containers**: Isolated execution environments managed by containerd.
2. **Images**: Immutable filesystem snapshots used to create containers.
3. **Namespaces**: Logical partitions within containerd for separating containers, images, and tasks.
4. **Tasks**: Represents a running container instance; containerd distinguishes between the container definition and the running task.
5. **Snapshots**: Filesystem layers used by containers, often implemented with **overlayfs** or other storage drivers.
6. **Content Store**: Manages storage of images and their layers in a standardized format.
7. **gRPC API**: containerd exposes a gRPC API for programmatic control of containers and images.
8. **CRI Integration**: Supports Kubernetes’ Container Runtime Interface, allowing Kubernetes to manage containers via containerd.

## Usage

**containerd** is used with Kubernetes directly, or via Docker.
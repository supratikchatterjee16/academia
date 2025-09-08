# Containers

A **container** is a lightweight, standalone, and executable unit of software that packages **an application and all of its dependencies** (libraries, configuration, runtime, system tools) so it can run consistently across different environments.

Technically, containers use **operating system–level virtualization**:

* They share the **host kernel** (unlike virtual machines which each run their own OS).
* They are isolated from each other using **Linux namespaces** (for process, network, filesystem isolation) and **cgroups** (for resource control like CPU, memory).

In short:
> A **container** = an **isolated process** with its own filesystem, network, and runtime environment, packaged for portability.

## Introduction (Why Containers Matter)

* **Before containers:** Developers packaged apps with assumptions about the host system → “It works on my machine” problems.
* **With containers:**

  * Run the same way in dev, test, and production.
  * Fast to start (milliseconds–seconds vs minutes for VMs).
  * Lightweight (no full guest OS).
  * Portable (runs anywhere with a container runtime).
  * Scalable (easy to spin up thousands in clusters like Kubernetes).

Containers became the backbone of **cloud-native development** and **microservices architectures** because they allow teams to ship software faster and more reliably.

## Brief History of Containers

* **1970s – Early Process Isolation**

  * **chroot (1979, Unix V7)** → First filesystem isolation (a process can’t see beyond its “root” directory).
  * Foundation for modern containers.

* **2000s – Linux Isolation Primitives**

  * **Linux Namespaces (2002+)** → Process, network, and filesystem isolation.
  * **cgroups (2007, Google)** → Resource limits and monitoring for groups of processes.

* **2008 – LXC (Linux Containers)**

  * First full container implementation in Linux, combining namespaces + cgroups.

* **2013 – Docker**

  * Made containers **developer-friendly** with easy CLI, image packaging, and registries.
  * Sparked the modern container revolution.

* **2015 – OCI (Open Container Initiative)**

  * Standardization effort to define **container image format** and **runtime spec**.
  * Prevented fragmentation of container ecosystems.

* **Today**

  * Containers are the foundation of **Kubernetes**, **cloud-native computing**, **DevOps pipelines**, and even **serverless platforms** (like AWS Lambda and Google Cloud Run).
  * Used by almost every major tech company to deploy scalable services.

## 1. **Container Runtimes (low-level execution)**

These are the actual components that run containers. Docker itself now uses some of these under the hood.

* **containerd**

  * Industry-standard container runtime (graduated CNCF project).
  * Used by Docker, Kubernetes (via CRI).
* **runc**

  * Low-level OCI runtime used by containerd and Docker.
  * Executes containers according to the Open Container Initiative (OCI) spec.
* **CRI-O**

  * Lightweight runtime optimized for Kubernetes.
  * Alternative to Docker/containerd in Kubernetes clusters.
* **Kata Containers**

  * Combines lightweight VMs and containers for stronger isolation.
* **gVisor** (by Google)

  * User-space kernel for containers → strong sandboxing.
* **Firecracker** (by AWS)

  * MicroVM-based, optimized for serverless (used in AWS Lambda, Fargate).

* **Docker CLI** 

## 2. **Container Engines (user-facing tools like Docker)**

Provide CLI/UX to build, run, and manage containers.

* **Podman**

  * Daemonless, Docker-compatible engine.
  * Rootless mode for better security.
* **Buildah**

  * Focused on building OCI/Docker images without requiring a daemon.
* **LXC/LXD** (Linux Containers / Linux Daemon)

  * One of the earliest Linux container projects.
  * Provides system containers (like lightweight VMs).
* **Singularity (now Apptainer)**

  * Popular in HPC and scientific computing.
  * Allows non-root users to run containers.

## 3. **Container Image Builders**

Focused on building images, often used in CI/CD pipelines.

* **Kaniko** (Google)

  * Builds OCI images inside containers, without requiring Docker.
* **Img**

  * Dockerfile builder that doesn’t need Docker daemon.
* **Bazel** (Google)

  * General build system, can build container images as artifacts.

## 4. **Container Orchestration Platforms**

(Not strictly containerization, but essential for managing multiple containers.)

* **Kubernetes** (most widely adopted)
* **OpenShift** (Red Hat’s Kubernetes distribution)
* **Docker Swarm** (simpler than K8s, but less popular today)
* **Nomad** (by HashiCorp, workload scheduler that can run containers and non-containers)
* **Apache Mesos / Marathon** (older, less common now)

## 5. **Specialized / Niche Container Systems**

* **Rkt (Rocket)** — by CoreOS, now discontinued but historically important.
* **Unikernels** (MirageOS, OSv) — extreme lightweight VMs, container-like but single-purpose OS+app bundles.
* **Nabla Containers** (IBM) — security-focused container runtime.

## Comparison of major high-level container runtimes

Here is a structured **side-by-side comparison of the major high-level container runtimes**. These sit above low-level runtimes like `runc`/`crun` and handle image management, networking, orchestration integration, and lifecycle management.

| Runtime             | Origin / Maintainer           | Kubernetes Support                                              | Daemon Requirement          | Rootless Mode                    | Primary Use Case                                                   | Typical Low-level Runtime |
| - | -- |  |  | -- |  | - |
| **Docker (Engine)** | Docker Inc.                   | ❌ (deprecated since v1.24, replaced by containerd/CRI-O)        | ✅ Docker daemon (`dockerd`) | ⚠️ Limited (not fully supported) | Developer-friendly full container platform (build, ship, run)      | `containerd` → `runc`     |
| **containerd**      | CNCF (originally from Docker) | ✅ (via CRI plugin)                                              | ✅ `containerd` daemon       | ⚠️ Limited                       | Kubernetes-native runtime, efficient lifecycle management          | `runc` or `crun`          |
| **CRI-O**           | Red Hat, CNCF project         | ✅ (native CRI implementation)                                   | ✅ `crio` daemon             | ⚠️ Limited                       | Kubernetes-optimized runtime, lightweight alternative to Docker    | `runc` or `crun`          |
| **Podman**          | Red Hat                       | ❌ (not a CRI runtime, but can run Kubernetes pods YAML locally) | ❌ Daemonless                | ✅ Full rootless support          | DevOps workflows, secure local container management                | `runc` or `crun`          |
| **LXC/LXD**         | Canonical (Ubuntu)            | ⚠️ Limited, not widely adopted for Kubernetes                   | ✅ Daemon (`lxd`)            | ⚠️ Limited                       | System containers (VM-like), good for running full OS environments | LXC runtime               |

### Key distinctions

* **Kubernetes compatibility**:

  * **Supported directly**: `containerd`, `CRI-O`
  * **Deprecated**: Docker (replaced internally by containerd)
  * **Not directly supported**: Podman, LXC/LXD

* **Security (rootless support)**:

  * **Strong**: Podman (rootless-first design)
  * **Partial/experimental**: containerd, CRI-O, Docker

* **Use cases**:

  * **Developer platform**: Docker, Podman
  * **Production/Kubernetes**: containerd, CRI-O
  * **System/VM-like workloads**: LXC/LXD

### Performance

| Runtime             | Startup Time (per container)                                       | Memory Footprint (idle container)                           | CPU Overhead | Scalability (pods/containers per node)                        | Notes                                                    |
| - |  | -- |  | - | -- |
| **Docker (Engine)** | \~100–200 ms (higher than containerd/CRI-O due to daemon overhead) | \~80–100 MB per daemon (`dockerd`), plus container overhead | Low–Moderate | Scales to thousands, but less efficient than containerd/CRI-O | Best for dev workflows, but Kubernetes support removed   |
| **containerd**      | \~60–120 ms                                                        | \~30–50 MB for `containerd` daemon                          | Very low     | Very high (used by most Kubernetes distros at scale)          | Optimized for Kubernetes, efficient and stable           |
| **CRI-O**           | \~50–100 ms                                                        | \~25–40 MB for `crio` daemon                                | Very low     | Very high (comparable or better than containerd)              | Kubernetes-first design, minimal overhead                |
| **Podman**          | \~80–150 ms (slightly slower rootless)                             | \~20–30 MB per container process (no central daemon)        | Low          | Scales well, but not as tested in large K8s clusters          | Daemonless, best for secure local dev + CI/CD            |
| **LXC/LXD**         | \~200–500 ms (system containers are heavier)                       | \~100+ MB per system container (full init system possible)  | Moderate     | Lower scalability (heavier than app containers)               | Great for VM-like workloads, not ideal for microservices |

# Kubernetes

Kubernetes (aka “K8s”) is an open-source container orchestration platform for automating deployment, scaling, and management of containerized applications. It exposes an API-driven control plane that schedules containers (Pod objects) onto nodes, provides service discovery, rolling updates, self-healing, and declarative configuration via manifests. Kubernetes is portable (runs on-cloud and on-prem), extensible (admission controllers, CRDs), and has a large ecosystem of tools. ([Kubernetes][1])

## Brief history (high level)

* Origins: conceived inside Google (teams who built Borg/Omega) and announced publicly as Kubernetes in 2014. Key early contributors include Joe Beda, Brendan Burns, and Craig McLuckie. The project was donated to the Cloud Native Computing Foundation (CNCF) and grew rapidly as an ecosystem. ([Kubernetes][2], [Wikipedia][3])
* Evolution: Kubernetes matured from core scheduling and pods into a full platform with network plugins (CNI), multiple storage interfaces (CSI), the Container Runtime Interface (CRI), Custom Resource Definitions (CRDs), Operators, and many graduated APIs. ([Kubernetes][1])

## Major feature & platform changes (high-impact, recent / important)

(These focus on design/operational changes you should know about.)

1. **Dockershim removal → CRI + containerd**
   Docker’s legacy “dockershim” was removed from Kubernetes upstream; Kubernetes relies on the Container Runtime Interface (CRI). containerd and CRI-O are the common runtimes used in production. If you used Docker Engine directly as the kubelet runtime in older clusters, you must migrate to containerd/CRI-O (or use Kubernetes distributions that preserved compatibility). ([Kubernetes][4])

2. **More explicit release/maintenance policy & supported versions**
   Kubernetes maintains release branches for recent minor releases and documents support lifecycles; keep an eye on version skew rules when upgrading control plane and node components. The project provides clear release notes and an expected support window for each release. ([Kubernetes][5])

3. **kubeadm as de-facto bootstrapping for production/DIY clusters**
   kubeadm has become the standard “blessed” way to bootstrap clusters (control plane and nodes), with step-by-step guidance and integration for containerd. The official docs and kubeadm tooling are the recommended method for custom clusters. ([Kubernetes][6])

4. **Gradual hardening & stable APIs for storage, networking, and configs**
   CSI (storage), CNI (network), and feature gates have matured: many alpha/beta features have graduated, but you must track what APIs are stable vs deprecated in your target K8s version. (See release notes for the version you run.) ([Kubernetes][5])

5. **Tooling/ecosystem changes (CNI, Cilium, service mesh integration)**
   Projects like Cilium (CNI + eBPF), network policies, and service meshes are commonly used; many setups now use CNI plugins instead of in-tree networking. These are ecosystem choices but affect installation and sizing. (See respective projects for specifics.)

## Table of core concepts (quick reference)

| Concept                        |                                                        What it is | Why it matters                                        | Typical objects / examples                          |
| ------------------------------ | ----------------------------------------------------------------: | ----------------------------------------------------- | --------------------------------------------------- |
| Cluster                        |                           Set of machines (nodes) + control plane | Unit of administration                                | control plane, worker nodes                         |
| Control plane                  |                       API server + controllers + scheduler + etcd | Brain of the cluster (control & reconciliation)       | kube-apiserver, controller-manager, scheduler, etcd |
| Node                           |                       A machine (VM/physical) that runs workloads | Runs kubelet and container runtime                    | worker or control-plane node                        |
| Pod                            | Smallest deployable unit (one/more containers, shared net/volume) | Scheduling unit                                       | app containers, sidecars                            |
| Deployment                     |           Declarative controller to run Pods with rolling updates | Manages ReplicaSets, scalers, rollouts                | replicas, updateStrategy                            |
| Service                        |              Stable network endpoint + load-balancer or ClusterIP | Service discovery & load balancing                    | ClusterIP, NodePort, LoadBalancer                   |
| ConfigMap / Secret             |                                     Config and secrets as objects | Decouple config from images                           | mounted env vars/volumes                            |
| Namespace                      |                                        Virtual cluster separation | Multi-tenancy, resource scoping                       | dev, staging, prod                                  |
| CRD (CustomResourceDefinition) |                                    Extend API with custom objects | Operators and extension points                        | Prometheus CRD, cert-manager                        |
| CNI                            |                                Container Network Interface plugin | Pod networking implementation                         | Calico, Cilium, Flannel                             |
| CSI                            |                                       Container Storage Interface | Storage plugin for persistent volumes                 | hostPath, AWS EBS, Ceph                             |
| kubelet                        |                                                Agent on each node | Talks to the API server and manages pods on that node | uses CRI (containerd)                               |
| containerd / CRI               |                                A CRI-compatible container runtime | Runs containers; used by kubelet                      | containerd.sock                                     |

(Use this table as a cheat-sheet in runbooks.)

## Implementation guide — kubeadm + **containerd** (practical, step-by-step)

This is an opinionated, repeatable sequence for a small production cluster (HA control plane optional). Commands are representative — adapt versions, hostnames, and network CIDRs to your environment. I cite kubeadm and the container runtime docs where relevant. ([Kubernetes][6])

> Assumptions:
>
> * OS: a modern Linux (Ubuntu, RHEL/CentOS stream) with systemd.
> * You will run containerd as the node runtime.
> * You have at least SSH access and root or sudo on all hosts.
> * You’ll use kubeadm to bootstrap control plane(s) and join workers.

### 1) Prep each node (control and worker)

1. Ensure kernel modules and sysctl settings (bridging, ip\_forward) are set (example):

```bash
## on all nodes (run as root)
cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF

sudo modprobe overlay
sudo modprobe br_netfilter

cat <<EOF | sudo tee /etc/sysctl.d/99-kubernetes-cri.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables  = 1
net.ipv4.ip_forward                 = 1
EOF

sudo sysctl --system
```

2. Install containerd (example for Debian/Ubuntu):

```bash
## install dependencies
sudo apt update && sudo apt install -y ca-certificates curl gnupg lsb-release

## add Docker repo (containerd packages)
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \
  | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update
sudo apt install -y containerd.io
```

3. Configure containerd for Kubernetes (systemd cgroup driver recommended):

```bash
sudo mkdir -p /etc/containerd
containerd config default | sudo tee /etc/containerd/config.toml

## Edit /etc/containerd/config.toml to set:
##   SystemdCgroup = true
## (search for the section: [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options])
sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml

sudo systemctl restart containerd
sudo systemctl enable containerd
```

> Note: containerd versions and packaging differ by OS. Use vendor docs for the recommended containerd version for your Kubernetes release. ([Kubernetes][4])

### 2) Install kubeadm, kubelet, kubectl (same version set)

```bash
## Example (Ubuntu). Replace X.Y.Z with target k8s minor version (e.g., 1.34.0)
curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://pkgs.k8s.io/key.gpg
echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://pkgs.k8s.io/ kubernetes-xenial main" \
  | sudo tee /etc/apt/sources.list.d/kubernetes.list

sudo apt update
sudo apt install -y kubelet=1.X.Y-00 kubeadm=1.X.Y-00 kubectl=1.X.Y-00
sudo apt-mark hold kubelet kubeadm kubectl
```

### 3) Bootstrap the first control-plane node with kubeadm

Choose pod network CIDR (example `10.244.0.0/16` for Flannel). If you plan HA control plane, you’ll bootstrap the first control plane, then join additional control planes with `kubeadm join --control-plane`.

```bash
## generate a kubeadm config file (example)
cat <<EOF >kubeadm-config.yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
kubernetesVersion: "v1.X.Y"
networking:
  podSubnet: "10.244.0.0/16"
controllerManager:
  extraArgs:
    bind-address: "0.0.0.0"
EOF

sudo kubeadm init --config=kubeadm-config.yaml --upload-certs
```

* Save the kubeadm output: it contains the `kubeadm join` command and controller certificates token for other control-plane nodes and workers. ([Kubernetes][6])

Post-init (on control node):

```bash
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

### 4) Install a CNI plugin

Pick CNI (Calico, Cilium, Flannel). Example (Flannel):

```bash
kubectl apply -f https://raw.githubusercontent.com/flannel-io/flannel/master/Documentation/kube-flannel.yml
```

(Or follow Cilium/Calico docs if you need network policies/eBPF). The CNI must match podSubnet used during `kubeadm init`.

### 5) Join worker nodes

On each worker, run the `kubeadm join ...` command printed by the `kubeadm init` output (or generate a join token). Example:

```bash
sudo kubeadm token create --print-join-command
## then run output on the worker
```

### 6) (Optional) Add more control plane nodes (HA)

On a second control node, run the provided `kubeadm join <api-server-endpoint> --control-plane --certificate-key <key> ...` using the certificate key printed by the first `kubeadm init`. Then set up an external load balancer or DNS pointing clients to the control plane endpoints (or use kubeadm’s recommended HA topology). ([Kubernetes][6])

### 7) Verify cluster & tune

```bash
kubectl get nodes
kubectl get pods -A
kubectl top nodes   ## if metrics-server installed
```

Tune kubelet, containerd, cgroup settings, and set resource requests/limits for production workloads.

## Operational checklist (short)

* Run etcd on dedicated control-plane nodes (or use managed etcd). Back up etcd regularly.
* Monitoring & logging (Prometheus, Grafana, EFK/Opensearch).
* RBAC & network policies to limit lateral movement.
* Regular patching and timely cluster upgrades within supported window. ([Kubernetes][5])

## Estimating number of control-plane and worker nodes — rules of thumb + worked examples

There’s no single formula — it depends on workload CPU/memory, availability SLAs, pod density, control-plane load (number of objects, controllers, CRDs), and operational constraints. Below are practical heuristics.

### Control-plane sizing (HA and availability)

* **Development / test:** 1 control-plane node (single) acceptable for non-critical dev clusters. Not recommended for prod.
* **Small production (HA):** **3 control-plane nodes** (odd number for etcd quorum). This tolerates 1 node failure and is the usual minimum for production HA.
* **Medium / large production:** **3–5 control-plane nodes**. Use 5 for very large clusters with high API request rates or large etcd dataset (many objects). More control-plane nodes increases etcd quorum overhead; often better to scale control-plane vertically (bigger VMs) rather than >5 nodes. ([Kubernetes][5])

**Recommendation:** Start with 3 control-plane nodes for production. Move to 5 only if you measure high control-plane load (etcd CPU/latency, APIserver QPS) that justifies it.

### Worker-node sizing (capacity and count)

Worker count depends on:

* Number of pods and average resource requests (CPU/memory) per pod.
* Pod density per node (kubelet default max pods \~110; many operators run fewer).
* High availability & failure domain requirements.

**Simple capacity formula (CPU example):**

1. Determine total CPU cores needed by all pods (sum of requested CPU).
2. Decide safety buffer (reserve for system pods + headroom): \~20–30%.
3. Pick instance size (e.g., 8 vCPUs per node).
4. Worker nodes = ceil( (total\_requested\_cpu \* 1.25) / node\_vcpus )

Same applies for memory, use the higher of CPU-based or memory-based result.

**Example scenarios**

1. **Small production microservices app**

   * 20 pods, each requests 0.25 CPU and 512Mi memory -> CPU total = 20 \* 0.25 = 5 vCPU.
   * Buffer 25% → 6.25 vCPU.
   * If each worker has 4 vCPU usable → workers = ceil(6.25/4) = 2 nodes.
   * Use 3 nodes for availability if you want tolerate a node failure.

2. **Medium e-commerce (burst traffic)**

   * 200 pods, avg request 0.5 CPU → 100 vCPU.
   * Buffer 30% → 130 vCPU.
   * Node size 32 vCPU → workers = ceil(130/32) = 5 nodes (consider 6 for failover).

3. **High-density batch cluster**

   * High pod density (short-lived jobs), you may push to >100 pods/node but monitor CNI & kubelet limits; prefer autoscaling.

### High availability and fault domains

* Always ensure **N+1** capacity for maintenance/failures (i.e., spare headroom to handle node loss).
* Spread nodes across failure domains (AZs, racks) — prefer odd number of control-plane nodes across AZs.

### Control-plane load factors to watch

* Number of API objects (ConfigMaps, Secrets, CRDs) and controllers increases etcd and APIserver load. If cluster has tens/hundreds of thousands of objects, controller and etcd sizing must grow accordingly (more memory/cpu or a move to dedicated etcd clusters). Monitor API QPS and etcd latency and scale vertically/horizontally as needed. ([Kubernetes][5])

## Quick checklist to pick numbers for your cluster (practical)

1. Estimate total requested CPU and memory of all pods.
2. Choose desired HA level (control-plane: 3 min for prod).
3. Choose node instance size (vCPU/mem) and decide safe headroom (20–30%).
4. Use the formula above to compute worker count and then add 1–2 spare nodes for rolling upgrades/failover.
5. If you expect heavy control-plane or many objects, plan 3→5 control-plane nodes or larger VM sizes.
6. Plan and test failure scenarios and autoscaling (Cluster Autoscaler + HPA/VPA).

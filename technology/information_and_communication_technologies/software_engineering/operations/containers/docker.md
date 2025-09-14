# Docker

**Docker** is an **open-source container platform** that allows developers and operators to build, ship, and run applications inside **lightweight, portable containers**.

* Containers package an app and its dependencies so it runs consistently across environments.
* Docker simplified container adoption by providing a **developer-friendly CLI**, **image packaging system**, and **registry (Docker Hub)**.

> In essence: **Docker = the ecosystem that popularized containers for everyone**.

## **Brief History of Docker**

* **2013**: Released by **dotCloud (later renamed Docker Inc.)**.
* Made containers accessible by abstracting away complex Linux features (namespaces, cgroups, union filesystems).
* Provided a consistent workflow: `docker build → docker push → docker run`.

### Key Milestones:

* **2014–2015**: Explosive growth, Docker Hub launched, container ecosystem expands.
* **2015**: Spun off **containerd** (core runtime) for wider community adoption.
* **2017**: Docker Enterprise introduced (commercial offering).
* **2019**: Docker Enterprise sold to Mirantis; Docker refocused on developer tooling.
* **Today**: Docker is part of nearly every cloud-native stack, though Kubernetes uses **containerd** or **CRI-O** under the hood.

## **Pros of Using Docker**

### 1. **Portability**

* Containers package the app + dependencies → “**It works on my machine**” problem is solved.
* Runs consistently across laptops, servers, and cloud environments.

### 2. **Lightweight & Efficient**

* Containers share the host OS kernel → much lighter than virtual machines.
* Faster startup times (milliseconds to seconds vs. minutes for VMs).
* Higher density (more apps per server).

### 3. **Scalability**

* Easy to replicate containers for scaling out.
* Works seamlessly with orchestration systems like **Kubernetes** and **Docker Swarm**.

### 4. **Faster Development & Deployment**

* CI/CD pipelines integrate smoothly with Docker.
* Quick image builds and rollbacks enable rapid releases.

### 5. **Isolation**

* Each container runs in its own isolated environment.
* Helps prevent dependency conflicts between applications.

### 6. **Ecosystem & Community**

* Rich tooling: Docker Compose, Docker Hub, registries.
* Vast ecosystem of prebuilt images accelerates development.

### 7. **Infrastructure as Code**

* Dockerfiles and Compose files make environments **repeatable and version-controlled**.

## **Cons of Using Docker**

### 1. **Security Concerns**

* Containers share the **host kernel** → weaker isolation compared to VMs.
* Vulnerabilities in base images or dependencies may propagate quickly.
* Requires strong image scanning and patching practices.

### 2. **Complexity at Scale**

* Running a few containers is easy → managing hundreds/thousands needs **Kubernetes** or similar orchestration.
* This adds a steep learning curve and operational overhead.

### 3. **Performance Overhead (vs bare metal)**

* While lighter than VMs, containers still add a small performance cost.
* Especially for **I/O-heavy** or **GPU/real-time workloads**.

### 4. **Storage & Networking Challenges**

* Persistent storage across containers is not trivial.
* Networking setups (bridge, overlay) can be complex to troubleshoot.

### 5. **Ecosystem Fragmentation**

* Kubernetes has shifted toward **containerd / CRI-O** instead of Docker as the runtime.
* Developers may need to adapt to slightly different workflows.

### 6. **Learning Curve**

* Developers and Ops teams must learn Dockerfiles, images, registries, networking, volumes, orchestration.
* Misconfigurations (e.g., open ports, insecure images) can cause major issues.

### 7. **Not Always Ideal**

* For **monolithic apps** or **simple workloads**, Docker may add unnecessary complexity.
* Some legacy apps may not containerize well.

## **Major Versions & Feature Changes**

* **Docker 1.x (2013–2016)**

  * First stable versions.
  * Core features: container creation, images, Docker Hub integration.

* **Docker 1.12 (2016)**

  * Introduced **Docker Swarm mode** (native clustering/orchestration).

* **Docker 17.x → 18.x (2017–2018)**

  * Versioning scheme changed to **YY.MM format** (e.g., 17.03).
  * Modularization: `docker` CLI, `dockerd`, containerd, runc.

* **Docker 19.x (2019)**

  * Rootless mode (experimental).
  * BuildKit introduced (faster image builds, caching).

* **Docker 20.x (2020–2021)**

  * WSL2 backend on Windows.
  * GPU support for containers.
  * Docker Compose V2 rewritten in Go (plugin model).

* **Docker 23.x (2023)**

  * Improved security (seccomp, AppArmor integration).
  * Extended BuildKit features.

## **Components Making Up Docker**

1. **Docker Engine**

   * Core client-server application.
   * **dockerd** (daemon) → manages containers, images, networks.
   * **docker CLI** → user interface.
   * **containerd** → container runtime (now independent).
   * **runc** → low-level runtime (implements OCI spec).

2. **Docker Hub / Registry**

   * Central repository for sharing images.
   * Can use private registries.

3. **Docker Compose**

   * Tool to define and run **multi-container applications** via `docker-compose.yml`.

4. **Docker Swarm**

   * Native clustering and orchestration (less common now, Kubernetes dominates).

## **Core Concepts**

* **Image** → Immutable template (blueprint) for containers (like a snapshot).
* **Container** → Running instance of an image (lightweight, isolated process).
* **Dockerfile** → Recipe for building images.
* **Volume** → Persistent storage for containers.
* **Network** → Virtual network layer for container communication.
* **Registry** → Image distribution system (e.g., Docker Hub).

## **Common Docker CLI Commands**

* **Images & Containers**

  * `docker pull <image>` → Download image.
  * `docker build -t <tag> .` → Build image from Dockerfile.
  * `docker run -d -p 8080:80 <image>` → Run container detached, map port.
  * `docker ps -a` → List containers.
  * `docker stop <id>` → Stop a running container.
  * `docker rm <id>` / `docker rmi <image>` → Remove container/image.

* **Volumes & Networks**

  * `docker volume create <name>` → Create volume.
  * `docker network ls` → List networks.

* **Debugging**

  * `docker logs <id>` → View container logs.
  * `docker exec -it <id> sh` → Open shell inside container.

## **Dockerfile**

A **Dockerfile** is a script with instructions to build an image.

### Instructions:

| Instruction     | Purpose                                                                                                          |
| --------------- | ---------------------------------------------------------------------------------------------------------------- |
| **FROM**        | Defines the base image for the new image. Must be the first instruction (except for `ARG` before it).            |
| **RUN**         | Executes a command inside the image at build time (e.g., installing packages). Creates a new layer.              |
| **CMD**         | Provides default command/arguments for the container at runtime. Can be overridden when running `docker run`.    |
| **ENTRYPOINT**  | Defines the main executable for the container. Unlike `CMD`, it is not overridden easily. Often used with `CMD`. |
| **LABEL**       | Adds metadata to an image (e.g., maintainer, version, description).                                              |
| **EXPOSE**      | Documents the port(s) the container will listen on. (Does not publish the port by itself — used for reference.)  |
| **ENV**         | Sets environment variables in the container.                                                                     |
| **ADD**         | Copies files/directories from the build context into the image. Also supports URLs and tar extraction.           |
| **COPY**        | Copies files/directories from the build context into the image. Preferred over `ADD` (more predictable).         |
| **WORKDIR**     | Sets the working directory for subsequent instructions (`RUN`, `CMD`, `ENTRYPOINT`, etc.).                       |
| **ARG**         | Defines build-time variables that can be passed with `--build-arg`. Available only during image build.           |
| **VOLUME**      | Creates a mount point and marks it as externally stored (persistent).                                            |
| **USER**        | Sets the username or UID under which subsequent instructions (and container process) will run.                   |
| **ONBUILD**     | Adds a trigger instruction to be executed when the image is used as a base for another build.                    |
| **STOPSIGNAL**  | Defines the system call signal that will be sent to stop the container (default: SIGTERM).                       |
| **HEALTHCHECK** | Defines a command to test container health. Docker marks the container as `healthy` or `unhealthy`.              |
| **SHELL**       | Overrides the default shell used in `RUN` (default: `/bin/sh -c` on Linux, `cmd /S /C` on Windows).              |

#### **Important Distinctions**

* **CMD vs ENTRYPOINT**

  * `CMD` provides default arguments.
  * `ENTRYPOINT` defines the actual executable.
  * Often combined like this:

    ```dockerfile
    ENTRYPOINT ["python", "app.py"]
    CMD ["--debug"]
    ```

    → Runs `python app.py --debug`.

* **ADD vs COPY**

  * `COPY`: Only copies files.
  * `ADD`: Can also fetch URLs and extract tar files.
  * Best practice: Use **COPY** unless `ADD`’s extra functionality is needed.

* **ARG vs ENV**

  * `ARG`: Only available at **build time**.
  * `ENV`: Persists in the built image and at **runtime**.

### **What is a Docker image layer?**

* A **Docker image** is built up of **layers**, each representing a **set of filesystem changes**.
* Each **instruction in a Dockerfile** (e.g., `FROM`, `RUN`, `COPY`) usually creates a new layer.
* Layers are **stacked on top of each other**, forming the final image.

**Key properties of layers:**

1. **Immutable:** Once created, a layer never changes. If you rebuild, a layer can be reused from cache.
2. **Cached:** Docker caches layers; if a layer hasn’t changed, Docker reuses it, speeding up builds.
3. **Shared:** Layers can be shared between images. For example, two Python images may share the same base `python:3.11-slim` layer.

### **Dockerfile instructions and layers**

| Instruction        | Creates a new layer? | Notes                                                |
| ------------------ | -------------------- | ---------------------------------------------------- |
| `FROM`             | Yes                  | Base image is a layer.                               |
| `RUN`              | Yes                  | Adds filesystem changes from the command.            |
| `COPY`/`ADD`       | Yes                  | Copies files into image; creates a layer.            |
| `WORKDIR`          | No                   | Changes working dir; does **not** create a layer.    |
| `ENV`              | No                   | Adds environment variables; no layer for filesystem. |
| `CMD`/`ENTRYPOINT` | No                   | Metadata only; no filesystem change.                 |

### **How layers are cached**

* Docker checks **instruction + context** to see if a layer can be reused.
* Example:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
```

**Layer breakdown:**

1. `FROM python:3.11-slim` → cached if already pulled
2. `WORKDIR /app` → no new filesystem layer
3. `COPY requirements.txt .` → new layer
4. `RUN pip install ...` → new layer (big, can be cached if `requirements.txt` unchanged)
5. `COPY app.py .` → new layer

* **Important:** Changing `requirements.txt` invalidates the `RUN pip install` layer; Docker rebuilds that layer.
* Layers **on top** of a changed layer are also rebuilt.

### **Benefits of layering**

1. **Faster builds**: Unchanged layers are reused.
2. **Smaller downloads**: Only layers not present locally are downloaded.
3. **Storage efficiency**: Layers are shared between images.

### **Best practices to optimize layers**

1. **Minimize number of layers** for small, lean images.

   * Combine multiple commands in a single `RUN`:

```dockerfile
RUN apt-get update && apt-get install -y git curl && rm -rf /var/lib/apt/lists/*
```

2. **Order layers by frequency of change**:

   * Put rarely changing steps (like `pip install`) **before** frequently changing steps (`COPY app.py`).
   * This allows caching and speeds up rebuilds.

3. **Use `.dockerignore`**:

   * Exclude unnecessary files from the build context; prevents invalidating cache.

### **Visualizing layers**

You can inspect image layers:

```bash
docker history myimage:latest
```

Example output:

```
IMAGE          CREATED       CREATED BY                     SIZE
abcdef123456   2 days ago    COPY app.py .                  1KB
123456abcdef   2 days ago    RUN pip install -r req.txt    150MB
7890abcdef12   2 weeks ago   FROM python:3.11-slim         30MB
```

* Shows how each Dockerfile instruction contributes to the final image.

### Example

```dockerfile
# Simple Node.js app Dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```

## **Docker Compose**

* **Docker Compose** is a tool that lets you define and manage **multi-container applications** using a single configuration file (`docker-compose.yml`).
* Instead of manually running multiple `docker run` commands, you describe services, networks, and volumes in YAML, then bring everything up with:

```bash
docker-compose up -d
```

> Example: A web app with a database can be defined in **one file**.

This can also be used with **Docker Stack** with:

```bash
docker stack deploy -c docker-compose.yml mystack
```

### **Basic Structure of `docker-compose.yml`**

```yaml
version: "3.9"  # Compose file format version
services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
    volumes:
      - ./site:/usr/share/nginx/html
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - db_data:/var/lib/postgresql/data
volumes:
  db_data:
```

### **Core Concepts**

* **Services** → Individual containers (like “web”, “db”).
* **Networks** → Virtual networks for service communication (auto-created if not defined).
* **Volumes** → Persistent storage (databases, logs, configs).
* **Environment Variables** → Inject configuration at runtime.
* **Dependencies** → Define startup order (`depends_on`).

### **Major `docker-compose.yml` Keys**

Here’s a reference table of common keys:

| Section           | Key              | Purpose                                                    |
| ----------------- | ---------------- | ---------------------------------------------------------- |
| **Top-level**     | `version`        | Defines the Compose file format (v3.x is common).          |
|                   | `services`       | Defines application services (containers).                 |
|                   | `volumes`        | Defines named volumes for persistent storage.              |
|                   | `networks`       | Defines custom networks.                                   |
|                   | `configs`        | Store configuration files (Swarm/K8s integration).         |
|                   | `secrets`        | Manage sensitive data securely.                            |
| **Service-level** | `image`          | Use an existing image (from registry).                     |
|                   | `build`          | Build an image from a Dockerfile (e.g., `build: ./app`).   |
|                   | `container_name` | Assign a custom name to the container.                     |
|                   | `command`        | Override default command (`CMD`).                          |
|                   | `entrypoint`     | Override default entrypoint.                               |
|                   | `ports`          | Map host ports to container ports (e.g., `"8080:80"`).     |
|                   | `expose`         | Expose ports to linked services (not to host).             |
|                   | `environment`    | Define environment variables.                              |
|                   | `env_file`       | Load environment variables from a file.                    |
|                   | `volumes`        | Mount volumes (named or bind).                             |
|                   | `networks`       | Connect service to one or more networks.                   |
|                   | `depends_on`     | Define service startup dependencies.                       |
|                   | `restart`        | Restart policy (`always`, `on-failure`, `unless-stopped`). |
|                   | `healthcheck`    | Define container health checks.                            |
|                   | `deploy`         | (Swarm only) Configure replicas, resources, placement.     |
|                   | `logging`        | Configure log drivers (e.g., `json-file`, `syslog`).       |

### **Common CLI Commands**

* `docker-compose up -d` → Start all services in detached mode.
* `docker-compose down` → Stop and remove containers, networks, volumes.
* `docker-compose ps` → List services and status.
* `docker-compose logs -f` → View logs.
* `docker-compose exec <service> sh` → Open shell in a running container.
* `docker-compose build` → Build images defined with `build:`.

### **Use Cases**

* **Local development environments** (spin up databases, caches, APIs quickly).
* **Multi-service applications** (microservices, web + db + cache).
* **Prototyping & testing** before deploying to Kubernetes/production.
* **CI/CD pipelines** (use Compose to reproduce app stacks in test environments).

### **Difference from Dockerfile**

* **Dockerfile** → Defines **how to build** a single image.
* **docker-compose.yml** → Defines **how to run** multiple containers together.

> They complement each other:

* Use **Dockerfile** to build images.
* Use **docker-compose.yml** to orchestrate services.

### Examples

#### For usage with Docker swarm

```yaml
version: "3.9"

services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
    deploy:
      replicas: 3
      restart_policy:
        condition: on-failure
      update_config:
        parallelism: 1
        delay: 10s
    networks:
      - frontend

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: appdb
    volumes:
      - db_data:/var/lib/postgresql/data
    deploy:
      replicas: 1
      placement:
        constraints: [node.role == manager]   # keep DB on manager
    networks:
      - backend

networks:
  frontend:
  backend:

volumes:
  db_data:
```

## **Docker Swarm**

**Docker Swarm** is Docker’s **native container orchestration tool**.

* It lets you group multiple Docker hosts into a **cluster** (called a *Swarm*).
* Containers are deployed as **services** across the cluster.
* Provides built-in **load balancing, scaling, and fault tolerance**.

> Think of Swarm as Docker’s simpler alternative to **Kubernetes** for orchestration.

### **Key Concepts in Docker Swarm**

| Concept             | Description                                                                                                                                                    |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Swarm**           | A cluster of one or more Docker nodes working together as a single virtual system.                                                                             |
| **Node**            | A single Docker Engine instance (host). Nodes can be **manager** or **worker**.                                                                                |
| **Manager Node**    | Orchestrates and manages the Swarm cluster — responsible for scheduling, service management, and cluster state. Supports Raft consensus for high availability. |
| **Worker Node**     | Executes tasks assigned by managers. Does not make scheduling decisions.                                                                                       |
| **Service**         | The definition of a desired state for a containerized app in the Swarm (e.g., image, number of replicas, ports).                                               |
| **Task**            | A single running container instance within a service. The smallest unit of scheduling.                                                                         |
| **Replica**         | A copy of a task/container. Services can scale horizontally by increasing replicas.                                                                            |
| **Stack**           | A group of services defined in a `docker-compose.yml` (or similar). Used for deploying multi-service applications.                                             |
| **Overlay Network** | A virtual network that spans all nodes in the Swarm, allowing services on different hosts to communicate securely.                                             |
| **Ingress Network** | Special overlay network that provides **built-in load balancing** across service replicas.                                                                     |
| **Routing Mesh**    | Swarm feature that routes incoming requests on any node to the correct service/task.                                                                           |
| **Secrets**         | Secure way to store sensitive information (like passwords, tokens, certificates) and make them available only to authorized services.                          |
| **Configs**         | Non-sensitive configuration data that services can consume (similar to secrets but unencrypted).                                                               |
| **Swarm Mode**      | Docker Engine mode that enables clustering and orchestration features (activated with `docker swarm init`).                                                    |

### **How to Use Docker Swarm**

#### 1. **Initialize a Swarm**

On the first manager node:

```bash
docker swarm init --advertise-addr <MANAGER-IP>
```

* Outputs a `docker swarm join` command for workers.
* Can be reobtained using `docker swarm join-token worker`

#### 2. **Join Worker Nodes**

On worker nodes:

```bash
docker swarm join --token <token> <manager-ip>:2377
```

#### 3. **Deploy a Service**

Example: run an Nginx service with 3 replicas:

```bash
docker service create --name my-nginx --replicas 3 -p 8080:80 nginx
```

#### 4. **Scale Services**

```bash
docker service scale my-nginx=5
```

→ Instantly scales containers across available worker nodes.

#### 5. **Check Cluster State**

```bash
docker node ls          # list nodes
docker service ls       # list services
docker service ps my-nginx   # tasks (containers) running for a service
```

#### 6. **Rolling Updates**

Update the image for a service:

```bash
docker service update --image nginx:alpine my-nginx
```

→ Updates happen gradually (with rollback support).

#### 7. **Verify the cluster**

On a manager node:

```bash
docker node ls
```

#### 8. **Leave cluster**

Worker leaving cluster:

```bash
docker swarm leave
```

Manager leaving cluster:

```bash
docker swarm leave --force
```

### **Features of Docker Swarm**

* **Simple Setup** → Integrated into Docker Engine, no extra installation.
* **Declarative Model** → Define desired state (`replicas`, `networks`), Swarm maintains it.
* **Service Discovery** → Built-in DNS-based discovery for containers.
* **Load Balancing** → Requests distributed across service replicas.
* **Scaling** → Scale services up/down easily.
* **Rolling Updates** → Seamless updates with rollback on failure.
* **Security** → Encrypted node communication (TLS by default).

### **Docker Swarm vs Kubernetes**

| Feature        | Docker Swarm               | Kubernetes                              |
| -------------- | -------------------------- | --------------------------------------- |
| Setup          | Simple (built into Docker) | Complex, requires components            |
| Learning Curve | Easy                       | Steeper                                 |
| Ecosystem      | Docker-native              | CNCF ecosystem, widely adopted          |
| Scalability    | Medium (hundreds of nodes) | High (thousands of nodes)               |
| Features       | Basic orchestration        | Advanced (autoscaling, operators, CRDs) |

> **Swarm is simpler, Kubernetes is more powerful.**

### **Use Cases for Docker Swarm**

* Small to medium-sized clusters.
* Teams already using Docker, needing basic orchestration.
* Development/staging environments (lighter than Kubernetes).
* Quick prototypes and educational purposes.

## Registries

A **registry** is a service that stores Docker images and lets clients (`docker push`, `docker pull`) interact with them.

* **Public example** → Docker Hub.
* **Private registry** → Your own hosted registry (on-premise, cloud, or self-managed).

### **Docker Registry (Official Image)**

Docker provides an official `registry` image.

### Run it with Docker:

```bash
docker run -d -p 5000:5000 --name my-registry registry:2
```

* Starts a private registry on `localhost:5000`.
* Images pushed here are stored locally on the host filesystem.

### Push an image:

```bash
docker tag nginx localhost:5000/my-nginx
docker push localhost:5000/my-nginx
```

### Pull it back:

```bash
docker pull localhost:5000/my-nginx
```

> This is the **simplest way** to set up a private registry for testing/dev.

### **Production-Ready Setup**

For production, **security, storage, and access control** are required.

#### (a) Use SSL (HTTPS)

Registries require HTTPS in production.

* Get a TLS certificate (from Let’s Encrypt or self-signed).
* Run registry with TLS:

  ```bash
  docker run -d \
    -p 443:5000 \
    --name my-registry \
    -v /certs:/certs \
    -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/domain.crt \
    -e REGISTRY_HTTP_TLS_KEY=/certs/domain.key \
    registry:2
  ```

#### (b) Authentication

Enable **basic auth** with `htpasswd`:

```bash
docker run --entrypoint htpasswd httpd:2 -Bbn user pass > auth/htpasswd
```

Mount it:

```bash
docker run -d \
  -p 443:5000 \
  --name my-registry \
  -v /auth:/auth \
  -e "REGISTRY_AUTH=htpasswd" \
  -e "REGISTRY_AUTH_HTPASSWD_REALM=Registry Realm" \
  -e "REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd" \
  registry:2
```

#### (c) Persistent Storage

Use a volume or cloud backend (S3, GCS, Azure Blob):

```yaml
storage:
  s3:
    accesskey: <key>
    secretkey: <secret>
    bucket: my-docker-registry
    region: us-east-1
```

### **Alternatives to Docker Registry**

If you want more features (UI, RBAC, image scanning, replication):

* **Harbor (CNCF project)** → Enterprise-grade registry with role-based access, security scanning, replication.
* **GitLab Container Registry** → Integrated into GitLab CI/CD.
* **JFrog Artifactory** → Universal artifact repository (supports Docker images + other binaries).
* **AWS ECR / GCP Artifact Registry / Azure ACR** → Fully managed cloud registries.

### **Relevance in Operations**

* **Private registries** improve security (control over images).
* Reduce dependency on Docker Hub limits (rate limiting, outages).
* Speed up deployments by keeping images close to the runtime environment (edge/local cache).
* Integrates with **CI/CD pipelines** for automated builds and pushes.

## Building for multiple architectures

### **Key Findings on Multi-Architecture Builds**

1. **Docker Swarm will only schedule a service on a node if the image is compatible with its architecture.**

   * `alfred` node is x86\_64 (amd64).
   * `rpi1` node is ARMv7.
   * Swarm will not run a container on a node if the node cannot pull or run the image architecture.

2. **Buildx is required for multi-arch images**.

   * Default `docker` driver can only build **host architecture**.
   * `docker-container` driver with BuildKit can build multiple architectures using QEMU.

3. **HTTP local registries are a problem for Buildx**.

   * BuildKit **enforces HTTPS** by default when using `docker-container` driver.
   * `insecure-registries` in `/etc/docker/daemon.json` **does not work** for Buildx multi-arch pushes.
   * Options:

     * Use HTTPS for your registry (recommended)
     * Build images natively on each architecture and push them separately.

4. **Buildx driver management**:

   * `docker buildx use default` → single-arch docker driver
   * `docker buildx use <builder>` → container driver (multi-arch)
   * Must bootstrap the builder: `docker buildx inspect --bootstrap`

5. **Swarm constraints**:

   * You cannot “force” a multi-arch image to run on incompatible nodes.
   * You can use **per-node constraints with `placement`** in your `docker-compose.yml` and deploy images specific to each architecture.

### **Recommended Approaches**

##### **Option A — Multi-arch image via Buildx + HTTPS registry**

* Best for full automation; allows a single image to run on all nodes.
* Requires registry to support HTTPS.

Steps:

1. Setup HTTPS registry:

```bash
mkdir -p ~/registry/certs ~/registry/data
cd ~/registry/certs
openssl req -newkey rsa:4096 -nodes -sha256 -keyout domain.key -x509 -days 365 -out domain.crt \
    -subj "/CN=192.168.1.18"
docker run -d --restart=always --name registry \
  -p 5000:5000 \
  -v ~/registry/data:/var/lib/registry \
  -v ~/registry/certs:/certs \
  -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/domain.crt \
  -e REGISTRY_HTTP_TLS_KEY=/certs/domain.key \
  registry:2
```

2. Trust self-signed certificate on all nodes:

```bash
sudo cp ~/registry/certs/domain.crt /usr/local/share/ca-certificates/registry.crt
sudo update-ca-certificates
sudo systemctl restart docker
```

3. Build multi-arch image and push:

```bash
docker buildx create --name mybuilder --driver docker-container --use
docker buildx inspect --bootstrap

docker buildx build --platform linux/amd64,linux/arm/v7 \
  -t 192.168.1.18:5000/simple-rest-app:latest \
  --push .
```

4. Deploy stack in Swarm without per-node hacks; Swarm automatically pulls the correct architecture.

##### **Option B — Build separate images per node (simpler HTTP approach)**

* Useful if you don’t want HTTPS yet.

Steps:

1. Build x86 image on manager:

```bash
docker build -t 192.168.1.18:5000/simple-rest-app:amd64 .
docker push 192.168.1.18:5000/simple-rest-app:amd64
```

2. Build ARM image on Raspberry Pi:

```bash
docker build -t 192.168.1.18:5000/simple-rest-app:arm .
docker push 192.168.1.18:5000/simple-rest-app:arm
```

3. Update `docker-compose.yml`:

```yaml
version: "3.9"
services:
  web-alfred:
    image: 192.168.1.18:5000/simple-rest-app:amd64
    deploy:
      placement:
        constraints: ["node.hostname == alfred"]

  web-rpi1:
    image: 192.168.1.18:5000/simple-rest-app:arm
    deploy:
      placement:
        constraints: ["node.hostname == rpi1"]
```

4. Deploy stack:

```bash
docker stack deploy -c docker-compose.yml simple-rest-app
```

### **Supporting Scripts / Makefile Examples**

##### **Makefile for Option B**

```makefile
.PHONY: build push deploy

REGISTRY=192.168.1.18:5000
IMAGE=simple-rest-app

build-amd64:
	docker build -t $(REGISTRY)/$(IMAGE):amd64 .

push-amd64: build-amd64
	docker push $(REGISTRY)/$(IMAGE):amd64

build-arm:
	# run on Raspberry Pi
	docker build -t $(REGISTRY)/$(IMAGE):arm .

push-arm: build-arm
	docker push $(REGISTRY)/$(IMAGE):arm

deploy:
	docker stack deploy -c docker-compose.yml simple-rest-app
```

### **Practical Points**

* **Always use the host IP instead of localhost** for the registry when multiple nodes need access.
* **Swarm service placement constraints** are required if you have multiple architectures.
* **Routing mesh** works, but only if containers are running on nodes. Multi-arch images must be compatible with node CPU.
* **Multi-arch Buildx + HTTPS registry** is the future-proof solution for a single image supporting all nodes.


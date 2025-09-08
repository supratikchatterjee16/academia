# The Twelve-Factor App

## 1. **Codebase** — *One codebase tracked in version control, many deploys*

* **Explanation**:
  A twelve-factor app has a **single codebase** per app, stored in version control (Git, Mercurial, etc.). Different environments (staging, production, multiple instances) are **different deployments** of the same codebase.
* **Caveats**:

  * Shared libraries should be separated into their own repos/packages, not copy-pasted.
  * In microservices, each service typically has its own codebase — but this can multiply repositories, making dependency management harder.

## 2. **Dependencies** — *Explicitly declare and isolate dependencies*

* **Explanation**:
  The app should **declare all dependencies** (in `requirements.txt`, `package.json`, `pom.xml`, etc.) and avoid relying on implicit system packages. Dependencies should be **isolated** (via virtualenv, containers, etc.).
* **Caveats**:

  * OS-level dependencies (like `libjpeg`, `openssl`) still need containerization or automation (Dockerfiles, buildpacks).
  * In polyglot systems, managing consistency across multiple dependency managers can be tricky.

## 3. **Config** — *Store config in the environment*

* **Explanation**:
  Configuration (API keys, DB URIs, credentials, feature flags) should not be hardcoded or stored in code. Instead, it belongs in **environment variables** (or injected securely).
* **Caveats**:

  * Environment variables may not be secure if leaked (logs, process listings). Modern practice often uses **secret managers** (Vault, AWS Secrets Manager, K8s Secrets).
  * Avoid overly complex configs in env vars — use them for references (e.g., file paths, secrets IDs).

## 4. **Backing Services** — *Treat backing services as attached resources*

* **Explanation**:
  Databases, caches, message queues, and other services should be treated as **replaceable resources** attached via config (URLs, creds). Switching from Postgres to MySQL, or local Redis to AWS ElastiCache, should require no code change.
* **Caveats**:

  * In practice, switching vendors often isn’t seamless due to SQL dialects, data models, or performance characteristics.
  * Vendor lock-in is real (e.g., DynamoDB vs MongoDB). Factor 4 encourages abstraction, but total portability is rarely possible.

## 5. **Build, Release, Run** — *Strictly separate build and run stages*

* **Explanation**:

  * **Build**: Transform code into an executable bundle (container image, JAR, etc.).
  * **Release**: Combine build with config (env vars, secrets).
  * **Run**: Execute in the runtime environment.
    These must be separate, reproducible, and versioned.
* **Caveats**:

  * Teams sometimes conflate build/release by embedding secrets/config into images — this violates the principle.
  * Requires good CI/CD discipline.

## 6. **Processes** — *Execute the app as one or more stateless processes*

* **Explanation**:
  Applications run as **stateless processes**. State is not stored in memory/disk between requests — instead, persisted in a DB, cache, or external service. This enables horizontal scaling (spin up/down instances).
* **Caveats**:

  * Some workloads (ML training, batch jobs) naturally have local state. Workarounds involve checkpoints or shared storage.
  * Caching in-memory can still be useful, but must tolerate losing instances.

## 7. **Port Binding** — *Export services via port binding*

* **Explanation**:
  The app should be **self-contained** and expose its services via a port (HTTP, gRPC, etc.), rather than relying on being executed inside an app server (like Tomcat or IIS).
* **Caveats**:

  * Not all environments allow direct port binding (e.g., embedded environments, strict firewalls).
  * Functions-as-a-Service (serverless) abstract away ports, though conceptually they still follow it.

## 8. **Concurrency** — *Scale out via the process model*

* **Explanation**:
  Instead of threads inside a process, scale is achieved by running **multiple processes** of the app. Concurrency models may be worker processes, job queues, or web instances.
* **Caveats**:

  * Requires a **process manager** (Kubernetes, systemd, Docker Swarm).
  * Some languages (e.g., Node.js, Go) already rely on internal concurrency models; mapping that to “process-per-unit” scaling needs careful orchestration.

## 9. **Disposability** — *Maximize robustness with fast startup and graceful shutdown*

* **Explanation**:
  Processes should **start fast** (seconds, not minutes) and **shut down gracefully** (finish requests, clean up connections). This enables elastic scaling and resilience.
* **Caveats**:

  * Apps with large caches, JIT warm-up, or ML models can have slow startups. Workarounds include prewarming or snapshotting.
  * Graceful shutdown requires signal handling (SIGTERM), which developers often forget.

## 10. **Dev/Prod Parity** — *Keep development, staging, and production as similar as possible*

* **Explanation**:
  Minimize the gaps between environments (time, personnel, tooling). Use the same backing services and deployment pipeline in dev, staging, and prod to avoid “works on my machine” issues.
* **Caveats**:

  * Cost often prevents exact parity (e.g., dev DB vs prod DB scale).
  * Developers may need lightweight versions of services (like localstack for AWS) — but this introduces risk of subtle differences.

## 11. **Logs** — *Treat logs as event streams*

* **Explanation**:
  Apps should not manage log files. Instead, write logs to **stdout/stderr**, and let the execution environment (Kubernetes, log aggregators) collect and route them. Logs are a **stream of events**.
* **Caveats**:

  * For debugging, devs often still want local log files.
  * Log volume can become massive; requires aggregation, parsing, storage, and retention strategies.

## 12. **Admin Processes** — *Run admin/management tasks as one-off processes*

* **Explanation**:
  One-off admin tasks (DB migrations, data cleanup, batch jobs) should run in the **same environment and codebase** as the app, but executed as one-off processes.
* **Caveats**:

  * Needs careful handling in containerized setups (jobs, CronJobs, K8s `Job` resources).
  * Long-running admin tasks may violate statelessness.

# Big Picture Caveats

* The Twelve Factors were designed for **SaaS apps on Heroku** in 2011. They’re still relevant, but:

  * Some assumptions (like “env vars only” for config) have been refined in modern practice (secrets managers, config servers).
  * Not all workloads fit (big data, HPC, ML pipelines often break disposability and statelessness).
  * Factor discipline works best with **containers & orchestration (K8s)**, which weren’t mainstream when first written.

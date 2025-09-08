# Software architecture patterns

## 1 Layered (N-Tier) Architecture

**Description**

* Classic organization of application logic into stacked layers (Presentation, Application/Service, Business/domain, Persistence, Database).

**Core concepts**

* Separation of concerns, strict directional dependencies (upper uses lower), interface contracts between layers.

**Enabler components / tech**

* Frameworks: Spring (Java), ASP.NET, Django, Rails. Build systems, CI/CD. ORM (Hibernate, Entity Framework).

**When to use**

* Simple/medium business apps, CRUD systems, teams familiar with classical architectures.

**Pros**

* Easy to reason about; clear responsibilities; testable layers; wide community knowledge.

**Cons**

* Tends to become monolithic; logic leakage across layers; performance penalty if over-layered.

**Implementation notes**

* Keep DTOs at boundaries, define service interfaces, avoid business logic in controllers, ensure unit tests for domain layer.

## 2 Monolithic Architecture

**Description**

* Entire app packaged and deployed as a single unit (single process / image).

**Core concepts**

* Single codebase, single deployment pipeline, shared memory and DB.

**Enabler components**

* App servers, single RDBMS, CI/CD for single artifact, container image (Docker) for distribution.

**When to use**

* Startups, MVPs, small teams, applications with low scale requirements.

**Pros**

* Simpler dev & testing; single deploy; easier local debugging; transactional consistency simpler.

**Cons**

* Hard to scale parts independently; long build/test cycles; team coordination overhead; risk of large complex codebase.

**Implementation notes**

* Modularize internally (packages/modules), adopt good separation, write automated tests, consider "feature flags" to mitigate release risk.

## 3 Client-Server

**Description**

* Split between client (UI) and server (business logic + data). Classic web model.

**Core concepts**

* Clear API boundary; stateless or stateful server; authentication/authorization at server.

**Enablers**

* HTTP/REST, GraphQL, WebSockets, OAuth/OpenID Connect.

**When to use**

* Web and mobile apps with centralized backend.

**Pros**

* Centralized control, easier to secure, thin client possible.

**Cons**

* Server becomes bottleneck; offline scenarios harder.

**Implementation notes**

* Design stable API contracts, use versioning, protect endpoints.

## 4 Model-View-Controller (MVC)

**Description**

* UI design pattern that separates Model (data), View (UI), Controller (input logic).

**Core concepts**

* Separation of presentation and domain, routes/dispatchers.

**Enablers**

* Frameworks: Rails, Spring MVC, ASP.NET MVC, Django (MVT).

**When to use**

* Web apps requiring clear presentation separation.

**Pros**

* Easier UI testing, modularity.

**Cons**

* Controllers can bloat; doesn't define backend distribution.

**Implementation notes**

* Keep controllers thin, push domain logic to models/services.

## 5 Pipe-and-Filter (Data Flow)

**Description**

* Data flows through a sequence of processing steps (filters) connected by pipes.

**Core concepts**

* Stateless filters, composability, streaming.

**Enablers**

* UNIX pipelines, Apache Beam, Flink, Kafka Streams, streaming frameworks.

**When to use**

* ETL, data transformations, analytics pipelines, compilers.

**Pros**

* Reusable filters, easy to compose, parallelizable.

**Cons**

* Latency if many stages; error handling across stages can be complex.

**Implementation notes**

* Make filters idempotent, design backpressure, monitor throughput/latency.

## 6 Broker (Message Broker / Mediator)

**Description**

* Components communicate via a broker which routes messages between producers and consumers.

**Core concepts**

* Decoupling via message queues/topics, routing, publish/subscribe vs point-to-point.

**Enablers**

* RabbitMQ, ActiveMQ, Kafka (sometimes brokerless for pub/sub), NATS.

**When to use**

* Asynchronous integration, decoupling services, reliable message delivery.

**Pros**

* Loose coupling, resilience, scalable consumers.

**Cons**

* Operational complexity, eventual consistency, fault modes (broker down).

**Implementation notes**

* Design message schemas (Avro/Proto/JSON), implement idempotent consumers, track offsets/acks.

## 7 Publish-Subscribe (Pub/Sub)

**Description**

* Publishers emit events to topics; multiple subscribers receive events independently.

**Core concepts**

* Topics, subscriptions, fan-out, event retention.

**Enablers**

* Kafka, Google Pub/Sub, AWS SNS, Pulsar.

**When to use**

* Event-driven systems, analytics, multi-subscriber workflows.

**Pros**

* Excellent for real-time fan-out; scalability.

**Cons**

* Ordering, consumer lag, replay/compaction considerations.

**Implementation notes**

* Partitioning strategy, schema evolution, consumer group semantics.

## 8 Event-Driven Architecture (EDA)

**Description**

* System behavior driven by events; components react to and emit events asynchronously.

**Core concepts**

* Event producers/consumers, event channels, loose coupling, eventual consistency.

**Enablers**

* Kafka, RabbitMQ, Kinesis, EventBridge, change data capture (Debezium).

**When to use**

* Real-time analytics, IoT, complex workflows, decoupled microservices.

**Pros**

* Scalability, responsiveness, resilience.

**Cons**

* Harder debugging, consistency & ordering, debugging/tracing complexity.

**Implementation notes**

* Correlation IDs for tracing, monitoring, contract-driven event schema, consumer backpressure handling.

## 9 Service-Oriented Architecture (SOA)

**Description**

* Applications composed of multi-purpose, reusable services (often coarse-grained) communicating over a network. Emphasizes enterprise integration.

**Core concepts**

* Reusable services, service contracts (WSDL/IDL), ESB (Enterprise Service Bus) for orchestration/mediation.

**Enablers**

* SOAP/WS-\* historically, REST, ESBs (MuleSoft, WSO2), API gateways, message brokers, enterprise registries.

**When to use**

* Large enterprises needing coarse-grained reuse across line-of-business systems and legacy integration.

**Pros**

* Reuse, governance, centralized mediation, enterprise integration patterns.

**Cons**

* Can be heavyweight (ESB bottleneck), governance overhead, slower pace than small independent services.

**Implementation notes**

* Design service contracts carefully, plan governance (SLAs), use API gateway + ESB judiciously, monitor service-level metrics.

## 10 Microservices Architecture

**Description**

* System built from many small services, each owning a single business capability; independently deployable and scalable.

**Core concepts**

* Bounded contexts, decentralized data management, independent deploys, lightweight communication (HTTP/REST, gRPC, messaging).

**Enablers**

* Containers (Docker), Orchestration (Kubernetes), API Gateway, service discovery (Consul), centralized logging/monitoring (Prometheus, ELK), message brokers (Kafka, RabbitMQ), CI/CD pipelines, service mesh (Istio, Linkerd).

**When to use**

* Large/complex systems requiring scaling, fast team autonomy, continuous delivery.

**Pros**

* Independent deploys, technology heterogeneity per service, better scalability, team autonomy.

**Cons**

* Operational complexity, distributed transactions, eventual consistency, difficult testing (integration), cross-cutting concerns (auth, monitoring).

**Implementation notes**

* Design around business capabilities, own your data per service, use API gateways for external exposure, enforce observability (traces, metrics, logs), implement resiliency patterns (circuit breaker, bulkhead).

## 11 Microkernel (Plugin/Extensible)

**Description**

* Core minimal runtime (microkernel) with pluggable modules/plug-ins providing features.

**Core concepts**

* Minimal core, plugin API, dynamic module loading, extension points.

**Enablers**

* OSGi (Java), plugin systems (Eclipse), modular packaging.

**When to use**

* Product platforms (IDEs, CMS), apps requiring third-party plugins.

**Pros**

* Extensibility, smaller core footprint, independent feature evolution.

**Cons**

* Complexity in managing plugin compatibility and versioning.

**Implementation notes**

* Define stable plugin APIs, versioning strategy, sandboxing for plugins.

## 12 Hexagonal (Ports & Adapters)

**Description**

* Also “Ports and Adapters”: core domain isolated from external agents via ports (interfaces) and adapters (implementations).

**Core concepts**

* Inward/outward adapters, domain model centered, testable core.

**Enablers**

* Dependency inversion, DI frameworks, test doubles/mocks.

**When to use**

* Systems needing strong maintainability and testability, long-lived products.

**Pros**

* Decouples domain from frameworks, easy to test, flexible tech choices.

**Cons**

* More upfront design, discipline required to keep boundaries.

**Implementation notes**

* Define application ports/interfaces, implement adapters for DB, UI, messaging. Use DI to inject adapters.

## 13 Clean / Onion Architecture

**Description**

* Concentric layered approach where domain entities/core are at center, and outer layers depend inward.

**Core concepts**

* Dependency rule (outer → inner only), domain-centric design.

**Enablers**

* DDD, DI containers, modularization.

**When to use**

* Complex business systems where domain integrity matters.

**Pros**

* Strong separation, framework-agnostic core, adaptable.

**Cons**

* Boilerplate, requires discipline.

**Implementation notes**

* Keep domain model pure, map infrastructure in outer layers, use anti-corruption layers between bounded contexts.

## 14 Domain-Driven Design (DDD) — as architectural approach

**Description**

* Modeling software to reflect complex domains. Not strictly an architecture but drives architecture (bounded contexts, aggregates, repositories).

**Core concepts**

* Ubiquitous language, bounded contexts, aggregates, entities/value objects, domain events.

**Enablers**

* DDD libraries, event sourcing/CQRS frameworks (Axon, Eventuous), collaboration with domain experts.

**When to use**

* Large complex domains (finance, healthcare) where domain logic dominates.

**Pros**

* Aligns code with business, clarifies boundaries, supports microservices via bounded contexts.

**Cons**

* Requires domain knowledge, time-consuming, misuse leads to overfitting.

**Implementation notes**

* Establish bounded contexts, design aggregates with transactional boundaries, use domain events to integrate contexts.

## 15 CQRS (Command-Query Responsibility Segregation)

**Description**

* Separate models for writes (commands) and reads (queries). Often paired with Event Sourcing.

**Core concepts**

* Separate read/write models, eventual consistency between them, optimized read stores.

**Enablers**

* Event stores, message brokers, read model projections, caching (Redis), specialized query DBs (Elasticsearch).

**When to use**

* Systems with high read/write asymmetry or complex read models (dashboards, analytics).

**Pros**

* Performance and scalability, read model optimization, easier to evolve reads.

**Cons**

* Complexity, eventual consistency, more moving parts.

**Implementation notes**

* Keep commands and events well defined, projection pipelines for read DBs, idempotency.

## 16 Event Sourcing

**Description**

* System state stored as immutable sequence of events; state reconstructed by replaying events.

**Core concepts**

* Append-only event store, snapshots, event versioning.

**Enablers**

* Event stores (EventStoreDB), Kafka (used as event log), frameworks: Axon, EventFlow.

**When to use**

* Audit-heavy domains, domain where full history/replay is valuable (finance).

**Pros**

* Full audit trail, temporal queries, easy debugging via replay.

**Cons**

* Storage growth, event schema evolution difficulties, operational complexity.

**Implementation notes**

* Implement snapshots for performance, event versioning/migration, governance around replay.

## 17 Strangler Fig (Incremental refactoring)

**Description**

* Replace legacy monolith gradually by routing functionality to new components; new system “strangles” old.

**Core concepts**

* Incremental migration, façade/routing layer, parallel systems.

**Enablers**

* API gateways, proxying, feature toggles, BFFs, CI/CD.

**When to use**

* Migrating legacy systems to modern architecture with minimal risk.

**Pros**

* Low risk migration, service-by-service migration, continuous delivery.

**Cons**

* Long migration timeline, testing complexity.

**Implementation notes**

* Identify seams in monolith, create facades, extract services one by one, backfill tests.

## 18 Space-Based Architecture (Grid)

**Description**

* Distribute processing and state across a grid to avoid centralized DB bottleneck; often memory-first.

**Core concepts**

* Shared-nothing, in-memory data grid, collocated processing for low latency.

**Enablers**

* Hazelcast, Apache Ignite, GigaSpaces, distributed caches (Redis Cluster).

**When to use**

* High throughput, unpredictable spikes (ticketing, e-commerce flash sales).

**Pros**

* Elastic scaling, low-latency access, high availability.

**Cons**

* Complexity in data partitioning & consistency, operational overhead.

**Implementation notes**

* Design partitioning strategy, data replication, failover plans, and consistency trade-offs.

## 19 Serverless (Function as a Service)

**Description**

* Deploy discrete functions triggered by events; cloud provider manages servers.

**Core concepts**

* Event triggers, short-lived functions, pay-per-use, managed scaling.

**Enablers**

* AWS Lambda, Azure Functions, GCP Cloud Functions, serverless frameworks.

**When to use**

* Short-lived tasks, event-driven workflows, prototypes, glue code.

**Pros**

* No server management, automatic scaling, reduced cost for spiky workloads.

**Cons**

* Cold starts, limited runtime/ephemeral state, potential vendor lock-in, debugging challenges.

**Implementation notes**

* Keep functions small and idempotent, externalize state (DynamoDB, S3), manage infrastructure with IaC.

## 20 Peer-to-Peer (P2P)

**Description**

* Nodes act as peers — no central server; each node can serve and consume.

**Core concepts**

* Decentralization, discovery protocols, replication/consensus.

**Enablers**

* Libp2p, BitTorrent, blockchain stacks (Ethereum), gossip protocols.

**When to use**

* Decentralized apps, file-sharing, blockchains.

**Pros**

* No single point of failure, resilient.

**Cons**

* Security, consistency, complex networking.

**Implementation notes**

* Design NAT traversal, robust peer discovery, consider reputation and security.

## 21 Backend-for-Frontend (BFF)

**Description**

* Per-client (web/mobile) backend service that tailors API and orchestration for that client.

**Core concepts**

* Client-specific aggregation, minimizing data over-fetching, API composition.

**Enablers**

* API Gateway, GraphQL, lightweight services.

**When to use**

* Multiple frontends with divergent needs.

**Pros**

* Optimized UX, clear contract per client, reduces client logic.

**Cons**

* More services to manage, duplicated logic across BFFs.

**Implementation notes**

* Reuse common services, keep BFF thin, co-locate with client teams.

## 22 Service Mesh (infrastructure pattern)

**Description**

* Dedicated infrastructure layer managing service-to-service communication (observe, secure, control traffic).

**Core concepts**

* Sidecar proxies, control plane, data plane, traffic policies.

**Enablers**

* Istio, Linkerd, Consul Connect, Envoy.

**When to use**

* Large microservices landscapes with complex comms requirements.

**Pros**

* Centralized traffic control, mTLS, retries/timeouts, observability.

**Cons**

* Operational overhead, complexity, performance overhead from proxies.

**Implementation notes**

* Start with small mesh rollout, measure overhead, enforce uniform observability and security policies.

## 23 Shared-Nothing Architecture

**Description**

* Each node is independent and self-sufficient; no shared memory/disk.

**Core concepts**

* Partitioning, replication, fault isolation.

**Enablers**

* Stateless services, distributed databases (Cassandra), sharding proxies.

**When to use**

* Massive scalability needed, horizontal partitioning.

**Pros**

* Linear scalability, fault isolation.

**Cons**

* Cross-shard transactions complex, data duplication.

**Implementation notes**

* Define shard keys, design fan-out joins, eventual consistency strategy.

## 24 Component-Based Architecture

**Description**

* System built from reusable components (often UI/component libraries or server components).

**Core concepts**

* Reusability, encapsulation, well-defined interfaces.

**Enablers**

* Web components, React/Vue components, micro frontends.

**When to use**

* Large frontend teams, product platforms.

**Pros**

* Reuse, consistent UX.

**Cons**

* Versioning and dependency hell, integration testing needed.

**Implementation notes**

* Version components, use component catalog and style guides.

## 25 Micro Frontends

**Description**

* Applying microservices principles to frontends — split frontend into independent deployable pieces.

**Core concepts**

* Per-team ownership, independent build/deploy, integration at runtime or build time.

**Enablers**

* Module federation (Webpack 5), iframe integration, edge-side includes, single-spa.

**When to use**

* Large web apps with multiple teams working on UI.

**Pros**

* Team autonomy, independent deploys, polyglot UI stacks.

**Cons**

* UX consistency, performance overhead, cross-team coordination.

**Implementation notes**

* Shared design system, contract-driven integration, monitor bundle sizes.

## 26 Resilience Patterns (Circuit Breaker, Bulkhead, Retry)

**Description**

* Patterns to make distributed systems resilient.

**Core concepts**

* Circuit Breaker: stop calling failing services temporarily.
* Bulkhead: isolate resources so failures don't cascade.
* Retry with backoff: transient error handling.

**Enablers**

* Hystrix (legacy), Resilience4j, Envoy/Service mesh, Kubernetes resource quotas.

**When to use**

* Any distributed system interacting with unreliable components.

**Pros**

* Prevent failure cascades, improve availability.

**Cons**

* Misconfiguration can hide issues, add complexity.

**Implementation notes**

* Tune thresholds, enable monitoring/alerts, ensure idempotency for retries.

## 27 API Gateway / Façade / Anti-Corruption Layer

**Description**

* Patterns for mediating between clients and internal services or between a new domain and legacy systems.

**Core concepts**

* Single entry point, request aggregation, protocol translation, anti-corruption layer to protect domain model.

**Enablers**

* Kong, AWS API Gateway, Nginx, custom façade layers, GraphQL.

**When to use**

* When exposing microservices externally, or integrating with incompatible legacy systems.

**Pros**

* Security centralization, simplified client APIs.

**Cons**

* Gateway becomes central point; risk of coupling.

**Implementation notes**

* Keep gateway thin; avoid business logic in gateway; use ACLs and rate limiting.

## 28 Bulk Data Patterns (Batch, Big-Data)

**Description**

* Architectures optimized for large-scale data processing.

**Core concepts**

* Batch processing, map-reduce, data lakes, streaming processing.

**Enablers**

* Hadoop, Spark, Flink, Hive, S3, HDFS, Airflow.

**When to use**

* Large-scale analytics, ML pipelines, ETL.

**Pros**

* Optimized for throughput, fault-tolerant.

**Cons**

* Latency higher (batch), complexity.

**Implementation notes**

* Data partitioning, lineage, idempotent transforms, orchestration workflows.

## 29 Edge / Fog Computing

**Description**

* Move computation/storage closer to data sources (edge devices) to reduce latency and bandwidth.

**Core concepts**

* Decentralized compute nodes, hierarchical processing (edge → fog → cloud).

**Enablers**

* IoT platforms, edge runtimes (K3s), CDN, MQTT brokers.

**When to use**

* IoT, real-time analytics, bandwidth-limited scenarios.

**Pros**

* Low latency, reduced bandwidth, resilience to connectivity loss.

**Cons**

* Management complexity, security at scale.

**Implementation notes**

* Secure device provisioning, OTA updates, local failover strategies.

## 30 Hybrid & Multi-Cloud Patterns

**Description**

* Use multiple cloud providers or mix on-premises + cloud for redundancy and vendor independence.

**Core concepts**

* Abstraction layers, multi-cloud data strategy, federation.

**Enablers**

* Terraform, Kubernetes (EKS/AKS/GKE), cloud-agnostic tooling, service mesh across clusters.

**When to use**

* Avoid vendor lock-in, regulatory needs, geo-redundancy.

**Pros**

* Resilience, provider choice.

**Cons**

* Complexity, cost, data gravity concerns.

**Implementation notes**

* Standardize on IaC, manage networking securely, central observability.

# Key comparisons

## Microservicesvs SOA — differences & overlap

**Similarities**

* Both decompose systems into independent services; both favor network communication and service boundaries.

**Key differences**

* **Granularity**: Microservices = fine-grained, one business capability per service. SOA = coarser-grained (enterprise services).
* **Governance**: SOA historically more centralized (ESB, formal governance). Microservices favor decentralized governance (per-service tech choices) with light-weight orchestration.
* **Integration**: SOA often uses an ESB for orchestration/mediation; Microservices prefer smart endpoints & dumb pipes (simple messaging or REST), and choreographed interactions.
* **Communication style**: SOA historically SOAP + WS-\* (though modern SOA can be REST); microservices use REST/HTTP, gRPC, or async messaging.
* **Runtime model**: Microservices expect independent deployability, containers, and cloud-native patterns; SOA evolved earlier with centralized middleware and enterprise-scale integration.
* **Organizational match**: Microservices map strongly to small, autonomous teams. SOA maps to centralized IT shared services.

**When to choose**

* Enterprise integration across heterogeneous legacy systems → SOA may be appropriate.
* New greenfield cloud-native app needing fast deliverability & independent scaling → Microservices.

## Monolithvs Microservices

**Monolith advantages**

* Simpler development, single deployment, easier transactions and local debugging.

**Microservices advantages**

* Independent scaling, team autonomy, deploy frequency, and fault isolation (if designed well).

**Trade-offs**

* Monolith: lower operational overhead but scaling and team coordination pain over time.
* Microservices: higher operational complexity (CI/CD, observability, distributed tracing) but better long-term agility at scale.

**When to start which**

* Start monolith for early-stage product; extract microservices when codebase & organization justify the overhead, or adopt modular monolith / Strangler pattern.

# Cross-cutting enablers you should plan for

* **Containers & Orchestration**: Docker, Kubernetes — essential for microservices and cloud-native.
* **Messaging / Event Bus**: Kafka (high-throughput, log-based), RabbitMQ (traditional broker), Pulsar.
* **API Management & Gateways**: Kong, AWS API Gateway, Apigee.
* **Observability**: Distributed tracing (OpenTelemetry), metrics (Prometheus), logging (ELK/EFK), dashboards (Grafana).
* **Service Discovery & Config**: Consul, Eureka, Kubernetes DNS; config stores (Vault, Consul, Kubernetes ConfigMaps/Secrets).
* **CI/CD & IaC**: Jenkins/GitHub Actions/GitLab, Terraform, Pulumi, ArgoCD.
* **Resiliency Tools**: Resilience4j, Envoy, Istio, circuit breakers, testing frameworks for chaos engineering (Chaos Monkey).
* **DBs & Storage**: RDBMS, NoSQL (Cassandra, MongoDB), distributed caches (Redis), search (Elasticsearch).
* **Security**: OAuth2/OpenID Connect, mTLS, API keys, WAF.

# Practical implementation checklist (applies to most distributed architectures)

1. **Define boundaries** (business capabilities / bounded contexts).
2. **Choose data ownership model** (single DB vs per-service DB).
3. **Choose communication style** (sync vs async — prefer async for decoupling).
4. **Observability**: plan distributed tracing, metrics, aggregated logs before production.
5. **Resilience**: instrument circuit-breakers, retries, timeouts, bulkheads.
6. **Deployment**: containerize services, implement automated pipelines, use orchestration.
7. **Security & governance**: authentication, authorization, secrets management.
8. **Monitoring & SLA**: define SLOs/SLAs and alerting.
9. **Operational runbook**: recovery procedures, scaling strategy.
10. **Testing**: unit, contract tests, integration, end-to-end, chaos testing.

# Short guide: Which pattern for common scenarios

* **Simple CRUD app / early-stage** → Monolith (modular).
* **Large enterprise with many legacy integrations** → SOA (with modern REST/ESB where needed).
* **High throughput events / analytics** → Event-Driven + streaming (Kafka).
* **Highly scalable web platform with many independent teams** → Microservices + service mesh.
* **Extensible product platform (plugins)** → Microkernel.
* **Complex domain logic / business rules** → DDD + Hexagonal / Clean architecture.
* **Intermittent, sporadic workloads** → Serverless.
* **Migrating monolith incrementally** → Strangler Fig pattern.


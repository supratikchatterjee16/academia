# Gateway Middlewares

In software engineering, **gateway middleware** refers to middleware components that act as an **entry point** (or "gateway") between clients and backend services, managing and controlling communication.

They sit at the boundary of a system (like an **API gateway** or **edge gateway**) and handle **cross-cutting concerns** so that backend services don’t have to.

---

### **Functions of Gateway Middleware**

* **Request routing** → Direct requests to the correct service.
* **Load balancing** → Distribute traffic across multiple service instances.
* **Authentication & authorization** → Check credentials, enforce access control.
* **Protocol translation** → Convert between protocols (e.g., HTTP to gRPC, REST to SOAP).
* **Rate limiting & throttling** → Prevent abuse and ensure fair resource usage.
* **Caching** → Improve performance by serving responses from cache.
* **Logging, monitoring, tracing** → Enable observability of requests.

---

### **Types of Gateway Middleware**

1. **API Gateway Middleware**

   * Manages REST/GraphQL/gRPC API requests from external clients.
   * Examples: **Kong, Apigee, Tyk, AWS API Gateway, NGINX (as gateway)**.

2. **Service Gateway Middleware (inside microservice architectures)**

   * Sometimes overlaps with **service mesh ingress/egress**.
   * Examples: **Istio ingress gateway, Envoy proxy, Traefik**.

Note: This is particularly useful with containers, where rapid changes in IPs occur, and these service meshes can act as a name lookup for the required services. 

3. **Edge Gateway Middleware**

   * Sits at the "edge" of a network/data center and manages traffic in/out.
   * Examples: **Cloudflare edge workers, NGINX edge gateway, HAProxy**.

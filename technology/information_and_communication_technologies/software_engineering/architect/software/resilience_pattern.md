# Resilience Pattern

**Resilience** is a system's ability to continue providing an acceptable level of service when components fail, become slow, overloaded, or temporarily unavailable—and to recover gracefully when the underlying problem is resolved.

A resilient system does **not** assume that failures can be eliminated. Instead, it assumes:

> **Failures will happen; the architecture must contain, absorb, and recover from them.**

This is especially important in distributed systems because a request may cross many independently failing components.

---

## 1. Why resilience is necessary

Consider a simple request path:

```text
                  ┌─────────────┐
                  │   Client    │
                  └──────┬──────┘
                         │
                         ▼
                  ┌─────────────┐
                  │ API Gateway │
                  └──────┬──────┘
                         │
                         ▼
                  ┌─────────────┐
                  │ Order       │
                  │ Service     │
                  └──────┬──────┘
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
        ┌──────────┐ ┌─────────┐ ┌─────────┐
        │ Payment  │ │Inventory│ │Shipping │
        │ Service  │ │ Service │ │ Service │
        └──────────┘ └─────────┘ └─────────┘
```

Suppose the Payment Service becomes slow.

Without resilience:

```text
Payment slows
     │
     ▼
Order requests wait
     │
     ▼
Threads/connections consumed
     │
     ▼
Order Service becomes slow
     │
     ▼
API Gateway requests queue
     │
     ▼
Clients retry
     │
     ▼
Even MORE load
     │
     ▼
Cascading failure
```

This is one of the most important concepts in resilience engineering:

### Cascading failure

A failure in one component propagates into otherwise healthy components.

Resilience patterns attempt to **break this propagation path**.

---

# 2. The major resilience patterns

A useful way to categorize them is:

| Pattern                  | Primary purpose                          |
| ------------------------ | ---------------------------------------- |
| **Timeout**              | Prevent waiting indefinitely             |
| **Retry**                | Recover from transient failures          |
| **Circuit Breaker**      | Stop calling an unhealthy dependency     |
| **Bulkhead**             | Isolate failures/resources               |
| **Rate Limiter**         | Control incoming/request rate            |
| **Load Shedding**        | Reject work when overloaded              |
| **Fallback**             | Provide degraded functionality           |
| **Backpressure**         | Prevent producers overwhelming consumers |
| **Health Checks**        | Detect unhealthy instances               |
| **Load Balancing**       | Distribute work across instances         |
| **Queueing**             | Absorb temporary traffic spikes          |
| **Idempotency**          | Make retries safe                        |
| **Caching**              | Reduce dependency load                   |
| **Graceful Degradation** | Continue with reduced functionality      |

These patterns are generally **combined**, rather than used individually.

---

# 3. Timeout

A **timeout** limits how long a service waits for another operation.

Without a timeout:

```text
Service A
   │
   │ request
   ▼
Service B
   │
   │ ............ never responds
   │
   └───────────────────────────────►
           waiting forever
```

With a timeout:

```text
Service A
   │
   │ request
   ▼
Service B
   │
   │
   │   2 seconds
   │◄────────────────── timeout
   │
   ▼
Return failure / fallback
```

For example:

```text
PaymentService.call()
       │
       ├── timeout = 2 seconds
       │
       ▼
Payment Provider
```

If the provider doesn't respond within two seconds, the caller stops waiting.

### Why it matters

Without timeouts, slow dependencies can consume:

* threads
* connection pools
* CPU
* memory
* request slots

Eventually the caller can fail too.

### Important principle

**Every remote call should have an explicit timeout.**

That includes:

* HTTP
* gRPC
* database calls
* message brokers
* external APIs

---

# 4. Retry

Retries are useful when failures are **transient**.

Examples:

* temporary network failure
* connection reset
* HTTP 503
* temporary database unavailability

Basic retry:

```text
        Request
           │
           ▼
      ┌─────────┐
      │ Service │
      └────┬────┘
           │
        failure
           │
           ▼
         Retry
           │
           ▼
      ┌─────────┐
      │ Service │
      └────┬────┘
           │
        success
           ▼
         Done
```

But blindly retrying is dangerous.

Suppose 1,000 clients are already generating heavy traffic:

```text
1,000 requests
      │
      ▼
   Service
      │
      X failure
      │
      ▼
1,000 retries
      │
      ▼
   Service
      │
      X
      │
      ▼
1,000 more retries
```

This can produce a **retry storm**.

## Exponential backoff

Instead of retrying immediately:

```text
Attempt 1 ──X
             │
             └── wait 100 ms

Attempt 2 ──X
             │
             └── wait 200 ms

Attempt 3 ──X
             │
             └── wait 400 ms

Attempt 4 ──X
             │
             └── wait 800 ms
```

Typically:

```text
delay = base × 2^attempt
```

with a maximum delay.

### Add jitter

If thousands of clients fail simultaneously, deterministic backoff can cause synchronized retries.

Instead:

```text
retry delay =
    exponential backoff
    + random jitter
```

This spreads requests over time.

### When NOT to retry

Do not automatically retry:

* validation errors
* authentication failures
* authorization failures
* most 4xx responses
* operations that aren't safely repeatable

Retries also need **idempotency** for operations such as payments or order creation.

---

# 5. Circuit Breaker

The **Circuit Breaker** is one of the most important resilience patterns.

It prevents repeatedly calling a dependency that is known to be unhealthy.

Think of it like an electrical circuit breaker.

### Normal operation

```text
Client
  │
  ▼
┌──────────────┐
│ Circuit      │
│ CLOSED       │
└──────┬───────┘
       │
       ▼
 Payment Service
```

Requests flow normally.

---

## Failure threshold

Suppose Payment Service starts failing:

```text
Request ──X
Request ──X
Request ──X
Request ──X
Request ──X
          │
          ▼
    failure threshold
          │
          ▼
    Circuit OPEN
```

Now:

```text
Client
  │
  ▼
┌──────────────┐
│ Circuit OPEN │
└──────┬───────┘
       │
       ├──────► Fail fast
       │
       └──────► Fallback
```

The application **doesn't even call** the unhealthy service.

This protects both sides:

```text
Without circuit breaker:

Application ──► failing dependency
Application ──► failing dependency
Application ──► failing dependency
Application ──► failing dependency
             ↓
       wasted resources


With circuit breaker:

Application
     │
     ▼
 Circuit Breaker
     │
     X
     │
  Fail fast
```

---

## Circuit breaker states

A conventional circuit breaker has three states:

```text
                failures exceed threshold
             ┌───────────────────────────┐
             │                           ▼
       ┌──────────┐                 ┌────────┐
       │  CLOSED  │ ──────────────► │  OPEN  │
       └────┬─────┘                 └────┬───┘
            ▲                            │
            │                            │ timeout
            │                            ▼
            │                     ┌────────────┐
            └──────────────────── │ HALF-OPEN  │
              success             └─────┬──────┘
                                        │
                                  test request
                                        │
                             ┌──────────┴──────────┐
                             │                     │
                          success                failure
                             │                     │
                             ▼                     ▼
                          CLOSED                 OPEN
```

### CLOSED

Normal traffic flows.

### OPEN

Requests are rejected immediately or routed to a fallback.

### HALF-OPEN

After a recovery period, a small number of requests are allowed through to test the dependency.

---

# 6. Bulkhead

The **Bulkhead pattern** isolates resources so that failure in one area doesn't consume everything.

The name comes from compartments in a ship.

If one compartment floods, the entire ship doesn't necessarily sink.

## Without bulkhead

Imagine one shared thread pool:

```text
                Application
                     │
             ┌───────┴───────┐
             │ Shared Pool   │
             │ 100 threads   │
             └───────┬───────┘
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       Payment    Search     Shipping
          │
       becomes slow
          │
          ▼
    consumes 100 threads
          │
          ▼
       EVERYTHING
       becomes slow
```

## With bulkheads

```text
                 Application
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
 ┌──────────┐  ┌──────────┐  ┌──────────┐
 │ Payment  │  │ Search   │  │ Shipping │
 │ 30 slots │  │ 50 slots │  │ 20 slots │
 └──────────┘  └──────────┘  └──────────┘
```

If Payment consumes all 30 slots:

```text
Payment     ██████████████████████████████ 30/30
Search      █████████████████████████       35/50
Shipping    ███████████                     11/20

              Payment failure
                   ↓
           contained here
```

Search and Shipping can continue operating.

### Bulkheads can isolate

* thread pools
* connection pools
* CPU
* memory
* queues
* tenants
* workloads
* database connections

---

# 7. Rate Limiter

A **rate limiter** controls how many requests are accepted within a period.

For example:

```text
Maximum:
100 requests / second
```

Architecture:

```text
Clients
   │
   │ 1,000 req/s
   ▼
┌─────────────────┐
│  Rate Limiter   │
│                 │
│  Limit: 100/s   │
└───────┬─────────┘
        │
        │ 100 req/s
        ▼
┌─────────────────┐
│ Application     │
└─────────────────┘
```

The excess requests can be:

```text
Accepted ───────► Application
   │
   │
   └──── excess ───► HTTP 429
```

### Common algorithms

#### Fixed window

```text
10:00:00 ───────── 10:00:01
       max 100 requests
```

Simple but can have boundary problems.

#### Sliding window

Tracks requests over a continuously moving time window.

#### Token bucket

Very common.

```text
             tokens added
                  ↓
           ┌─────────────┐
           │ Token Bucket│
           │ ○ ○ ○ ○ ○   │
           └──────┬──────┘
                  │
              request
                  │
                  ▼
             consume token
                  │
                  ▼
              Allowed
```

Example:

```text
Capacity:       100 tokens
Refill rate:     20 tokens/sec

Burst:           up to 100
Sustained rate:   20 req/sec
```

This allows controlled bursts while limiting sustained traffic.

---

# 8. Load Shedding

Sometimes the system simply **cannot process all incoming work**.

Instead of allowing the system to collapse, it deliberately rejects lower-priority work.

```text
                 10,000 requests/sec
                         │
                         ▼
                  ┌─────────────┐
                  │ Load Shedder│
                  └──────┬──────┘
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
       Critical requests       Low priority
              │                     │
              ▼                     ▼
          ACCEPTED               REJECTED
```

For example, an e-commerce application might prioritize:

```text
Payment                 HIGH
Order creation          HIGH
Inventory reservation   HIGH
Product search          MEDIUM
Recommendations         LOW
Analytics               LOW
```

During overload:

```text
Recommendation ──► DROP
Analytics       ──► DROP
Search          ──► REDUCE
Orders          ──► PRESERVE
Payments        ──► PRESERVE
```

This is often better than letting **everything fail**.

---

# 9. Backpressure

Backpressure controls a producer when a consumer cannot keep up.

Consider:

```text
Producer
  │
  │ 10,000 msg/s
  ▼
Queue
  │
  │ 1,000 msg/s
  ▼
Consumer
```

The queue grows indefinitely:

```text
Queue:

██████████████████████████████████████████████
                         ↑
                      growing
```

Eventually:

```text
Memory exhaustion
       ↓
Crash
       ↓
Recovery
       ↓
More messages
       ↓
Crash again
```

With backpressure:

```text
Producer
   │
   │  "slow down"
   ▼
┌─────────┐
│ Queue   │
│ bounded │
└────┬────┘
     │
     ▼
 Consumer
```

The producer may:

* slow down
* block
* buffer
* reject requests
* reduce concurrency

Backpressure is especially important in:

* streaming systems
* reactive applications
* message processing
* event-driven architectures

---

# 10. Fallback

A **fallback** provides an alternative response when the primary operation fails.

Example:

```text
Client
  │
  ▼
Product Service
  │
  ▼
Recommendation Service
  │
  X unavailable
  │
  ▼
Fallback
  │
  ▼
Popular products
```

Instead of:

```json
{
  "error": "Recommendation service unavailable"
}
```

the application might return:

```json
{
  "recommendations": [
    "Popular product A",
    "Popular product B",
    "Popular product C"
  ]
}
```

Fallbacks are particularly useful when functionality is **non-critical**.

Examples:

| Primary                      | Fallback                  |
| ---------------------------- | ------------------------- |
| Personalized recommendations | Popular products          |
| Live exchange rate           | Cached exchange rate      |
| User avatar service          | Default avatar            |
| Search suggestions           | No suggestions            |
| Pricing service              | Last-known price, if safe |
| External analytics           | Skip analytics            |

A fallback should **not conceal critical correctness failures**.

For example, silently treating a failed payment as successful is obviously unacceptable.

---

# 11. Graceful Degradation

Graceful degradation means reducing functionality rather than completely failing.

Imagine an online shopping application:

```text
Normal:

Product page
 ├── Product details
 ├── Reviews
 ├── Recommendations
 ├── Similar products
 ├── Live inventory
 └── Personalization
```

If recommendation services fail:

```text
Degraded:

Product page
 ├── Product details       ✓
 ├── Reviews               ✓
 ├── Recommendations      ✗
 ├── Similar products      ✗
 ├── Live inventory        ✓
 └── Personalization      ✗
```

The **core business function continues**.

---

# 12. Caching as a resilience mechanism

Caching isn't always described purely as a resilience pattern, but it can significantly reduce dependency failures.

```text
                 ┌─────────────┐
Request ────────►│ Application │
                 └──────┬──────┘
                        │
                        ▼
                  ┌───────────┐
                  │   Cache   │
                  └─────┬─────┘
                     hit │ miss
                         │
                         ▼
                  ┌───────────┐
                  │ Dependency│
                  └───────────┘
```

If the dependency is temporarily unavailable:

```text
Request
  │
  ▼
Cache
  │
  └── cached response ──► Client
```

This is sometimes called **stale-if-error** behavior.

The important question is whether stale data is acceptable for that particular domain.

---

# 13. Health checks

Health checks help determine whether an instance should receive traffic.

```text
                 Load Balancer
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Server A    Server B    Server C
          ✓           X           ✓
                      │
                      ▼
                Remove from pool
```

There are commonly two concepts:

### Liveness

> "Is this process alive?"

### Readiness

> "Can this instance safely receive traffic?"

Readiness is particularly important in orchestrated environments.

---

# 14. Load balancing

Load balancing distributes traffic across instances.

```text
                    Requests
                       │
                       ▼
                ┌─────────────┐
                │Load Balancer│
                └──────┬──────┘
                       │
             ┌─────────┼─────────┐
             ▼         ▼         ▼
          Instance  Instance  Instance
             A         B         C
```

This improves resilience by avoiding dependence on one instance.

However, load balancing alone isn't enough.

If every instance depends on the same failing database:

```text
              Load Balancer
              /     |     \
             A      B      C
              \     |     /
               \    |    /
                Database
                    X
```

the system still fails.

This illustrates a key principle:

> **Resilience must exist across the entire dependency graph, not just at one layer.**

---

# 15. Combining the patterns

Real-world systems usually combine multiple patterns.

For example:

```text
                         Internet
                            │
                            ▼
                    ┌──────────────┐
                    │ Rate Limiter │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │ Load Balancer│
                    └──────┬───────┘
                           │
                 ┌─────────┼─────────┐
                 ▼         ▼         ▼
                API       API       API
                 │
                 │
          ┌──────┴──────┐
          │             │
          ▼             ▼
      Bulkhead       Bulkhead
          │             │
          ▼             ▼
      Payment         Search
          │             │
          ▼             ▼
      Circuit        Circuit
      Breaker        Breaker
          │             │
          ▼             ▼
      Timeout        Timeout
          │             │
          ▼             ▼
       Retry         Retry
          │             │
          ▼             ▼
      Provider       Search DB
```

This gives us **defense in depth**.

---

# 16. A complete resilient request flow

Consider:

> User requests order history.

A robust architecture might look like this:

```text
                         Client
                           │
                           ▼
                    ┌─────────────┐
                    │ API Gateway │
                    └──────┬──────┘
                           │
                     Rate Limit
                           │
                           ▼
                    ┌─────────────┐
                    │Order Service│
                    └──────┬──────┘
                           │
                     Bulkhead
                           │
                           ▼
                    Circuit Breaker
                           │
                           ▼
                       Timeout
                           │
                           ▼
                        Retry
                       /     \
                      /       \
                     ▼         ▼
                Order DB    Cache
```

And if the database fails:

```text
Request
   │
   ▼
Order Service
   │
   ▼
Circuit Breaker
   │
   ▼
Database
   X
   │
   ▼
Retry
   X
   │
   ▼
Fallback
   │
   ▼
Cached order history
```

If the database remains unhealthy:

```text
Circuit OPEN
     │
     ├── no database calls
     │
     ▼
Fallback/cache
```

This protects the application from repeatedly hammering the failing database.

---

# 17. A useful resilience "stack"

A practical way to remember the patterns is:

```text
             ┌───────────────────────┐
             │   Graceful Degradation│
             ├───────────────────────┤
             │       Fallback        │
             ├───────────────────────┤
             │    Circuit Breaker    │
             ├───────────────────────┤
             │        Retry          │
             ├───────────────────────┤
             │       Timeout         │
             ├───────────────────────┤
             │      Bulkhead         │
             ├───────────────────────┤
             │    Rate Limiting      │
             ├───────────────────────┤
             │    Load Shedding      │
             ├───────────────────────┤
             │     Backpressure      │
             └───────────────────────┘
```

But these aren't necessarily a strict sequence. Their placement depends on the architecture.

---

# 18. The most important interaction: Timeout + Retry + Circuit Breaker

These three are frequently used together.

```text
                 Request
                    │
                    ▼
             ┌──────────────┐
             │Circuit Breaker│
             └──────┬───────┘
                    │
                 CLOSED
                    │
                    ▼
                Attempt 1
                    │
                ┌───┴────┐
                │Timeout │
                └───┬────┘
                    │
                  fail
                    │
                    ▼
                  Retry
                    │
                    ▼
                Attempt 2
                    │
                  fail
                    │
                    ▼
                  Retry
                    │
                    ▼
                Attempt 3
                    │
                  fail
                    │
                    ▼
             Circuit opens
                    │
                    ▼
               Fail fast
                    │
                    ▼
                Fallback
```

This combination provides:

* **Timeout** → don't wait forever
* **Retry** → recover transient failures
* **Circuit breaker** → stop hammering persistent failures
* **Fallback** → preserve useful functionality

---

# 19. A critical warning: resilience patterns can amplify failures

Resilience mechanisms themselves can cause problems if badly configured.

### Retry amplification

```text
100 clients
   │
   ├── 1 request
   ├── retry
   ├── retry
   └── retry

Potentially:

100 × 4 = 400 requests
```

### Timeout mismatch

Suppose:

```text
API timeout       = 2 sec
Service timeout   = 5 sec
Database timeout  = 10 sec
```

The upper layer may give up while lower layers continue consuming resources.

Better:

```text
Client
  timeout = 10s
      │
      ▼
Service
  timeout = 8s
      │
      ▼
Database
  timeout = 6s
```

The exact values depend on the application's latency budget, but **timeouts should be designed as a hierarchy**.

---

# 20. Resilience vs availability vs reliability

These terms are related but different.

### Reliability

> Does the system perform correctly over time?

### Availability

> Is the system usable when requested?

### Resilience

> Can the system continue/recover when things go wrong?

For example:

```text
Dependency fails
      │
      ▼
Resilient system
      │
      ├── detects failure
      ├── isolates failure
      ├── degrades functionality
      └── recovers
```

A resilient system may temporarily provide reduced functionality rather than achieving perfect availability.

---

# 21. Designing resilience around business criticality

Not every operation deserves the same resilience strategy.

For example:

| Operation             | Criticality | Strategy                                                             |
| --------------------- | ----------- | -------------------------------------------------------------------- |
| Payment               | Very high   | Timeout + idempotency + carefully controlled retry + circuit breaker |
| Order creation        | Very high   | Idempotency + durable messaging + retry                              |
| Inventory reservation | High        | Timeout + retry + consistency controls                               |
| Product search        | Medium      | Cache + timeout + fallback                                           |
| Recommendations       | Low         | Aggressive fallback/load shedding                                    |
| Analytics             | Low         | Async queue + drop/defer under load                                  |

This leads to an important architectural principle:

> **Protect the critical path first.**

---

# 22. Resilience testing

You shouldn't merely assume that your resilience mechanisms work.

Test them.

This is where **chaos engineering** becomes useful.

For example:

```text
             Production-like system
                      │
             ┌────────┼─────────┐
             │        │         │
             ▼        ▼         ▼
          Inject    Inject    Inject
          latency   errors    instance
                               failure
             │        │         │
             └────────┼─────────┘
                      ▼
                 Observe:
                 - errors
                 - latency
                 - saturation
                 - recovery
```

Useful experiments include:

* kill an application instance
* introduce network latency
* return HTTP 500/503
* exhaust a connection pool
* slow database queries
* fill a queue
* simulate dependency outage
* generate traffic spikes

The goal isn't simply:

> "Did the system stay up?"

It is:

> **"Did the system fail in the way we intended?"**

---

# 23. Observability is part of resilience

A system cannot recover intelligently if you can't see what is happening.

Monitor at least:

```text
                 RESILIENCE SIGNALS

                  ┌─────────────┐
                  │   Errors    │
                  ├─────────────┤
                  │   Latency   │
                  ├─────────────┤
                  │  Saturation │
                  ├─────────────┤
                  │ Retry count │
                  ├─────────────┤
                  │Circuit state│
                  ├─────────────┤
                  │Rate limits  │
                  ├─────────────┤
                  │Queue depth  │
                  └─────────────┘
```

For example, a sudden increase in:

```text
retry_count ↑
latency     ↑
queue_depth ↑
error_rate  ↑
```

is often an early indication that a dependency is becoming unhealthy.

---

# 24. Putting it all together

A mature resilient architecture can look conceptually like this:

```text
                             CLIENTS
                                │
                                ▼
                       ┌─────────────────┐
                       │   API Gateway   │
                       │                 │
                       │ Rate Limiter    │
                       │ Load Shedding   │
                       └────────┬────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │ Load Balancer   │
                       └────────┬────────┘
                                │
              ┌─────────────────┼─────────────────┐
              ▼                 ▼                 ▼
          Service A         Service B         Service C
              │                 │                 │
          Bulkhead           Bulkhead           Bulkhead
              │                 │                 │
              ▼                 ▼                 ▼
        Circuit Breaker   Circuit Breaker   Circuit Breaker
              │                 │                 │
           Timeout           Timeout           Timeout
              │                 │                 │
            Retry             Retry             Retry
              │                 │                 │
              ▼                 ▼                 ▼
          Dependency        Dependency        Dependency
              │                 │                 │
              └─────────────────┼─────────────────┘
                                │
                         Fallback / Cache
                                │
                                ▼
                       Graceful Degradation
```

The fundamental idea is **failure containment**:

```text
       Failure
          │
          ▼
     ┌─────────┐
     │ Detect  │
     └────┬────┘
          │
          ▼
     ┌─────────┐
     │ Contain │◄──── Bulkhead / Circuit Breaker
     └────┬────┘
          │
          ▼
     ┌─────────┐
     │ Absorb  │◄──── Cache / Queue / Fallback
     └────┬────┘
          │
          ▼
     ┌─────────┐
     │ Recover │◄──── Retry / Health checks
     └────┬────┘
          │
          ▼
       Normal
```

## A simple mental model

If you're designing a distributed system, remember these questions:

**1. What happens if the dependency is slow?**
→ **Timeout**

**2. What happens if the failure is temporary?**
→ **Retry + exponential backoff + jitter**

**3. What happens if the dependency stays broken?**
→ **Circuit breaker**

**4. What happens if one workload consumes all resources?**
→ **Bulkhead**

**5. What happens if traffic exceeds capacity?**
→ **Rate limiting + load shedding**

**6. What happens if the consumer is slower than the producer?**
→ **Backpressure**

**7. What can we return if the dependency isn't available?**
→ **Fallback/cache**

**8. Which functionality must survive at all costs?**
→ **Prioritization + graceful degradation**

**9. How do we know any of this is working?**
→ **Observability + resilience testing**

The overarching principle is:

> **Don't try to prevent every failure. Design the system so that individual failures remain bounded, useful work continues, and recovery happens automatically.**

## Libraries

| Language / ecosystem      | Library name          | Resilience coverage                                                                                                     |
| ------------------------- | --------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Java                      | **Resilience4j**      | Retry, Circuit Breaker, Rate Limiter, Time Limiter, Bulkhead, Cache                                                     |
| .NET / C#                 | **Polly**             | Retry, Circuit Breaker, Timeout, Rate Limiter, Fallback, Hedging                                                        |
| Go                        | **failsafe-go**       | Retry, Circuit Breaker, Adaptive Limiter, Adaptive Throttler, Bulkhead, Rate Limiter, Cache, Timeout, Fallback, Hedging |
| Python                    | **Tenacity**          | Retry, backoff, jitter                                                                                                  |
| Python                    | **PyBreaker**         | Circuit Breaker                                                                                                         |
| Python                    | **pyresilience**      | Retry, Circuit Breaker, Timeout, Fallback, Bulkhead, Rate Limiter, Cache                                                |
| TypeScript / Node.js      | **Cockatiel**         | Retry, Circuit Breaker, Timeout, Bulkhead, Fallback                                                                     |
| Node.js                   | **Opossum**           | Circuit Breaker, timeout, fallback, concurrency controls                                                                |
| Rust                      | **Tower**             | Timeout, Rate Limiting, Concurrency Limiting, Load Shedding, Retry via middleware ecosystem                             |
| Scala / JVM               | **Resilience4j**      | Retry, Circuit Breaker, Rate Limiter, Time Limiter, Bulkhead, Cache                                                     |
| Scala / ZIO               | **ZIO**               | Retry, timeout, scheduling, concurrency control, fallback/recovery, supervision                                         |
| Elixir / Erlang           | **OTP / Supervision** | Process isolation, supervision, restart/recovery, fault containment                                                     |
| Ruby                      | **Semian**            | Circuit Breaker, resource isolation / Bulkhead-style protection, timeouts                                               |
| Polyglot / Service Mesh   | **Envoy**             | Retry, Timeout, Circuit Breaking, Rate Limiting, Load Balancing, Health Checking                                        |
| Kubernetes / Service Mesh | **Istio**             | Retry, Timeout, Circuit Breaking, Rate Limiting, Load Balancing, Traffic Control                                        |

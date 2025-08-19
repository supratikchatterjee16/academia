# Resilience Frameworks

These frameworks provide the resilience pattern for various service calls.

A resilience pattern is a design pattern used in software systems (especially distributed systems and microservices) to help applications stay stable, responsive, and fault-tolerant when things go wrong — like network failures, timeouts, overload, or downstream service crashes.

Think of it as defensive strategies your application uses to “bend but not break” under stress.

Why?

- Networks are unreliable (latency, packet loss).
- Services fail or slow down unexpectedly.
- Traffic spikes can overwhelm dependencies.
- Distributed systems make failures inevitable, not exceptional.

Without resilience patterns, one failing service can cause a **cascading failure** across the whole system (classic "domino effect").

## Core Patterns

Here are the **core patterns** (many implemented in libraries like **Resilience4j**, Netflix **Hystrix**, or **Spring Cloud**):

### 1. **Circuit Breaker**

* Detects failures and “opens the circuit” to stop making calls to a failing service.
* Protects the system from repeated failed attempts.
* Example: Like a fuse box at home — when overload happens, it cuts the current.

**Parameters (configurable):**

* `failureRateThreshold` → % of failures to trigger breaker (e.g., 50%).
* `slowCallRateThreshold` → % of slow calls considered failures.
* `slowCallDurationThreshold` → time limit (e.g., 2s) after which a call is “slow.”
* `slidingWindowType` → COUNT-based (# calls) or TIME-based (last N seconds).
* `slidingWindowSize` → size of window for failure calculation.
* `minimumNumberOfCalls` → minimum calls before breaker can trip.
* `permittedNumberOfCallsInHalfOpenState` → trial calls when half-open.
* `waitDurationInOpenState` → how long before trying again.
* `automaticTransitionFromOpenToHalfOpenEnabled` → true/false.

**Metrics:** Failure Rate, Slow Call Rate, State, Transition Count.

---

### 2. **Retry**

* Automatically retries a failed request with a delay/backoff.
* Useful for temporary glitches (e.g., a momentary network blip).
* Needs careful tuning (too many retries can worsen the problem).

**Parameters:**

* `maxAttempts` → max retries (including first try).
* `waitDuration` → delay between retries.
* `retryExceptions` → exception types eligible for retry.
* `ignoreExceptions` → exceptions not retried.
* `intervalFunction` → constant / exponential backoff / random.
* `enableExponentialBackoff` → true/false.
* `enableRandomizedWait` → true/false.

**Metrics:** Retry Attempts, Retry Success/Failure Count, Backoff Duration.

---

### 3. **Timeout**

* Limits the max time a request can take.
* Prevents “hanging” calls that block resources.

**Parameters:**

* `timeoutDuration` → max allowed time (e.g., 2s).
* `cancelRunningFuture` → whether to cancel running task.

**Metrics:** Timeout Count, Avg Latency, P95/P99 Latency, Aborted Requests.

---

### 4. **Bulkhead**

* Isolates resources into pools (like compartments in a ship).
* If one pool is overloaded, others remain unaffected.
* Example: Keep API calls to external payment service in their own thread pool.

**Parameters:**

* `maxConcurrentCalls` → max calls allowed at once.
* `maxWaitDuration` → how long to wait for a permit (if pool full).
* `maxThreadPoolSize` (for thread pool bulkhead).
* `coreThreadPoolSize`.
* `queueCapacity` → max requests waiting.
* `keepAliveDuration` → how long idle threads live.

**Metrics:** Active Calls, Pool Utilization %, Rejected Calls, Queue Wait Time.

---

### 5. **Rate Limiter**

* Restricts the number of requests per unit time.
* Prevents overload of downstream services.
* Example: Only allow 100 API calls/sec to external service.

**Parameters:**

* `limitForPeriod` → max calls allowed per refresh period.
* `limitRefreshPeriod` → duration of one period (e.g., 1s).
* `timeoutDuration` → max wait for permit.

**Metrics:** Allowed Calls, Denied Calls, Wait Time, Utilization %.

---

### 6. **Fallback**

* Provides an alternative response when a call fails.
* Example: If product pricing service is down, return “price unavailable” instead of crashing the app.

**Parameters:**
*(Fallback is usually code-defined rather than config-based, so parameters = what you define in logic)*

* `fallbackMethod` → function to invoke when primary fails.
* `fallbackResponse` → static or computed response.
* `onExceptionTypes` → exception triggers for fallback.

**Metrics:** Fallback Count, Fallback Success Rate, Degraded Mode Ratio.

---

### 7. **Cache**

* Store frequently used results locally to reduce repeated calls.
* Both improves performance and reduces dependency failures.

**Parameters:**

* `ttl` (time-to-live) → how long before entry expires.
* `maxSize` → max entries allowed.
* `evictionPolicy` → LRU, LFU, FIFO.
* `refreshAhead` → whether to refresh before expiry.
* `keyStrategy` → how to generate cache keys.

**Metrics:** Hit Rate, Miss Rate, Evictions, Cache Size, Entry Staleness.

---

# Where Resilience Patterns Are Used

* **Microservices** (protect against downstream failures)
* **API gateways** (limit or shape traffic)
* **GraphQL resolvers / REST endpoints** (wrap external service calls)
* **Database access** (timeouts, retries, caching)

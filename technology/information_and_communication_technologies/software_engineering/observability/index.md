# Observability

**Observability** is the ability to understand the internal state of a system by examining its **outputs** (logs, metrics, traces, events).

It comes from **control theory**:

* A system is *observable* if you can determine what’s happening inside it just by looking at its external signals.
* In software, that means being able to answer **“What’s going on inside my app or infra?”** without needing to stop or modify it.

---

# The Three Pillars of Observability

1. **Logs**

   * Detailed, timestamped records of events.
   * Example: “User 123 failed login at 10:02:15.”

2. **Metrics**

   * Numeric measurements over time.
   * Example: CPU usage = 85%, Requests per second = 1200.

3. **Traces**

   * Show how a request flows through different services/components.
   * Example: A checkout request hits `frontend → payment-service → DB`, taking 2.3s.

*(Some add a 4th: **Events**, but they are often bundled with logs.)*

---

# Why Observability Matters

* **Monitoring tells you if something is wrong.**
  Example: CPU is 95%.
* **Observability tells you why it’s wrong.**
  Example: A spike in CPU is caused by a slow query in the payments service.

In modern **cloud-native, microservices, and distributed systems**, observability is critical because:

* Systems are too complex to predefine all possible failure modes.
* You need to **explore** data, not just react to predefined alerts.
* Helps with debugging, performance optimization, incident response, and security.

---

# Monitoring vs Observability

| Aspect       | **Monitoring**                              | **Observability**                                       |
| ------------ | ------------------------------------------- | ------------------------------------------------------- |
| **Purpose**  | Detect known problems.                      | Explore & understand unknown problems.                  |
| **Data**     | Uses pre-defined metrics & alerts.          | Uses logs, metrics, traces, events (holistic).          |
| **Approach** | Reactive (alert when threshold is crossed). | Proactive (discover root causes, ask new questions).    |
| **Example**  | “Alert: CPU > 90%.”                         | “Why did checkout requests slow down after deployment?” |

---

# Tools for Observability

* **Open-source**: ELK Stack, Prometheus + Grafana, Jaeger, OpenTelemetry.
* **Commercial**: Dynatrace, Splunk, Datadog, New Relic, Elastic Cloud.

## Comparison between major observability tools

| Feature / Aspect  | **ELK Stack**                                                                                          | **Dynatrace**                                                                        | **Splunk**                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| **Type**          | Open-source stack for search, log analytics, and visualization.                                        | SaaS/commercial platform for full-stack monitoring & observability (APM, infra, UX). | Commercial platform for log management, monitoring, security (SIEM).                            |
| **Core Strength** | Flexible, cost-effective, powerful search on logs/events.                                              | End-to-end observability with AI-driven automation.                                  | Enterprise-grade log management + security analytics.                                           |
| **Components**    | Elasticsearch, Logstash, Kibana, Beats.                                                                | OneAgent + Dynatrace SaaS backend.                                                   | Splunk Enterprise / Splunk Cloud + Splunk Forwarders.                                           |
| **Deployment**    | Self-hosted (DIY clusters) or Elastic Cloud.                                                           | SaaS-first, some managed deployments.                                                | On-prem, cloud, or hybrid. Requires scaling infrastructure.                                     |
| **Ease of Use**   | Steeper learning curve, need to design pipelines, queries, dashboards.                                 | Very easy. Out-of-the-box monitoring, auto-discovery of services, AI insights.       | Moderate. Powerful dashboards and queries but requires Splunk Query Language (SPL).             |
| **Data Sources**  | Any logs, metrics, traces via connectors.                                                              | Apps, infra, logs, cloud services, RUM, APM.                                         | Logs, metrics, events, security feeds, SIEM integrations.                                       |
| **AI/Automation** | Some ML in Elastic (X-Pack), but mostly manual config.                                                 | Built-in AI (Davis) for root-cause analysis, anomaly detection.                      | Machine learning & anomaly detection modules, but less automatic than Dynatrace.                |
| **Scalability**   | Very scalable but must be tuned & managed manually.                                                    | Auto-scaled SaaS. Little management overhead.                                        | Scales well but can get very expensive at large volumes.                                        |
| **Cost**          | Free core (open source). Paid features in Elastic Cloud/X-Pack. Infra costs increase with data volume. | Commercial subscription, premium pricing.                                            | Licensing is based on data ingestion/retention, often very costly at scale.                     |
| **Best For**      | Teams wanting **flexibility & control**, DIY observability, search-heavy use cases.                    | Teams needing **AI-driven full-stack observability** with minimal overhead.          | Large enterprises needing **robust log management, compliance, and security analytics (SIEM)**. |

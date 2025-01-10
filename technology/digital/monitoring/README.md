# Monitoring

Monitoring is a continuous function that uses the systematic collection of data on specified indicators to provide management and the main stakeholders of a project with an indication of the extent of progress and achievement of objectives, and progress in the use of allocated funds.[Refer](https://emm.iom.int/handbooks/stage-7-policy-monitoring-and-evaluation/what-monitoring)

Pillars of monitoring:

1. Logs
2. Traces and Events
3. Metrics

Accronym "LET Me".

This before cloud used to be isolated sets of utilities, with no generic tools.
Advancements in cloud adoptions saw a need for having a more generic tool come into the picture.

Tools that rose due to it are Dynatrace, AppDynamics, DataDog, etc.

Similar tools that arose were Elasticsearch, Logstash, and Kibana(aka ELK stack), Splunk, Grafana, etc.

## Observability

In IT and cloud computing, observability is the ability to measure a system’s current state based on the data it generates, recorded as logs, metrics, and traces. In fact, logs, metrics, and traces are known as the “three pillars of observability.”

Logs: Logs record the details of an event
Metrics: Metrics capture the numeric measurements used to quantify the performance and health of services
Traces: Traces track how services connect from end to end in response to requests
Observability has become more critical in recent years as cloud-native environments have gotten more complex, and the potential root causes for a failure or anomaly have become more difficult to pinpoint.

Because cloud services rely on a distributed and dynamic architecture, observability may also refer to the specific software tools and practices organizations use to interpret cloud performance data.[Dynatrace](https://www.dynatrace.com/news/blog/what-is-observability-2/)

The above is biased as Dynatrace intends to separate it's segment on unclear terms. But in essence it includes metadata, user behavior, topology and network mapping, and access to code-level details, along with the 3 pillars of monitoring. It is splitting hairs, but nevertheless, good to know about.

## Relevant Acronyms

SRE - Site Reliability Engineer
SLI - service level indicator. Actual metrics against which we compare the SLO.
SLO - service level objective. Performance target that we intend achieve.
SLA - service level agreement. Agreement with customers.
Error Budget - Acceptable level of deviation, between SLI and SLO. Also,


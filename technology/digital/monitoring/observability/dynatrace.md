# Dynatrace

Dynatrace is a revolutionary platform that delivers analytics and automation for unified observability and security.

- Answers and intelligent automation — Dynatrace uses causal AI to automate DevSecOps at scale and deliver the precise answers teams need to innovate and thrive in the modern cloud.
- Empowerment — Dynatrace breaks down team silos and proactively prevents issues before they affect end users.
- Solutions — Dynatrace solves critical digital challenges with all your observability, security, analytics, and automation solutions in one place.

The Dynatrace platform approach helps you solve a multitude of use case areas, and it will grow and adapt to solve new challenges while already enriching many areas of any organization. Our solutions in observability, security, analytics, and automation address the broadest range of use cases. And because our platform powers it all, you can create any unique use case, customized to ever-changing needs.[From Dynatrace's website](https://docs.dynatrace.com/docs/discover-dynatrace/what-is-dynatrace)

It's USP is it's Davis AI, which allows for "intelligent" proactive identification of issues.

## What it does?

- Infrastructure Observability: Get automatic and intelligent infrastructure monitoring and observability across hybrid and cloud environments, with precise AI-powered answers.
- Application Observability: Leverage best-in-class application performance monitoring (APM) to ensure optimal service performance and SLOs, innovate faster, collaborate more efficiently, and deliver more with less.
- Application Security: Get continuous application security posture insights and attack protection.
    - Security Protection: Detect and block common attacks on application-layer vulnerabilities like SQL injection, command injection, and JNDI attacks. Protect against some critical zero-day attack types, like those for Log4Shell, while the vulnerability is being remediated.
    - Security Analytics: Reduce the cost of investigating logs related to a current or suspected security incident like an application attack. Quickly and confidently verify what happened, leverage observability context to analyze, and take proactive action to strengthen defenses.
- Threat Observability: Quickly detect, investigate, and respond to threats with intelligent automation.
- Digital Experience: Deliver flawless digital experiences and drive business results with AI-driven, automated, frontend-to-backend digital experience monitoring.
- Log Analytics: Make smarter, faster decisions when troubleshooting and measuring the health of your application environments – all while eliminating the costly overhead of ingestion and management.
- Business Analytics: Simplify critical, real-time business decisions with precision, speed, and context.
- Software Delivery: Accelerate digital transformation with simple yet powerful automations driven by observability and security insights.
- Custom Solutions
    - Extend Dynatrace: Dynatrace is open, extensible, and can easily integrate with all major cloud platforms and solutions.
    - Dynatrace Hub: Unlock the full potential of Dynatrace by finding, activating, and running apps and extensions that address your specific observability needs. Dynatrace Hub is the central place to explore and activate all Dynatrace capabilities.
    - Dynatrace Developer﻿: Use the Dynatrace App Toolkit from the command line to create, develop, and deploy Dynatrace Apps.

### Benefits

1. Proactive issue detection, helping in scaling up particular services
2. Enhanced User Experience - providing app topology, responsiveness, and app responsible for it
3. Faster RCA
4. Improved Collabs - Shared Insights

## Components of Dynatrace

- AppEngine
- AutomationEngine
- Davis AI
- Grail(the DB)
- OpenPipeline
- OneAgent(the information emittor, not allowed to emit publicly)
- Smartscape
- [ActiveGate](https://docs.dynatrace.com/docs/ingest-from/dynatrace-activegate)(Proxy agent that OneAgent connects to. Responsible for securing information sent upstream)
- Kubernetes(monitoring tool for all Kubernetes clusters)
- Management Console: for managing everything on Dynatrace.

This can be availed as a SaaS or a self-managed utility. It supports hybrid cloud installations, as well as just on-premises(referred to as physical infra), or cloud infrastructure as well.

## Misc

Dynatrace has annual and monthly pricing plans available only by getting in touch with them.

## FAQs

- Is Dynatrace, only made for the cloud, or it supports hybrid? - It supports on-prem, cloud, and hybrid.
- What data protection rules are applicable here(applicable for SaaS only)?
- Does it provide REST APIs for auto scaling over cloud(or does it autoscale within a single server such as auto-churn up if capacity available and required by containers/pod)?
- Does it require a component to be installed on the host servers? - Yes
- Is it possible to monitor the serverless apps(lambda functions) to understand infra requirements to internalize it? - Not without having an EC2 instance, with running OneAgent
- Can it monitor multiple apps in a POD? - yes it can, it's installed on the VM/Container
- What are the benefits in security that this can provide, as compared to Splunk(in applications scope)?
- Does it support integrations with Cypress(NodeJS based frontends automated testing tool) for Synthetic monitoring?
- "OneAgent" supports which OSes? Is IBM AIX supported? - Yes
- Can issues be exported to some other utility(for instance ServiceNow)? - It can be. It has integrations for CI/CD, and for other apps.
- How is OneAgent configured to pickup the logs?
- How long does Dynatrace store logs for? - 7 days. For beyond that we need to add an external persistent volume to it.

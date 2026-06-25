---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[AWS Lambda]]"
  - "[[Amazon Cognito]]"
  - "[[aws - Elastic Load Balancer]]"
  - "[[aws - Virtual Private Cloud]]"
against:
  - "[[aws - Elastic Load Balancer]]"
  - "[[aws - Application Load Balancer]]"
reference_guides:
  - "[[Reference Notes/3-18_serverless.md]]"
tags:
  - aws/api-gateway
  - status/completed
---

# API Gateway

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **API Gateway**

---

## 🎯 Purpose (Why it is used)
Amazon API Gateway is a fully managed, serverless ingress gateway that makes it easy for developers to create, publish, maintain, monitor, and secure REST, HTTP, and WebSocket APIs at any scale. It handles all aspects of accepting and processing concurrent API calls.

---

## ⚙️ Functionality (What it is doing)
*   **Request Routing:** Integrates natively with backends like AWS Lambda, private HTTP endpoints (via VPC Links), or AWS services directly.
*   **Traffic Management:** Enforces rate-limiting and request throttling parameters to protect backend resources from traffic spikes.
*   **Lifecycle Management:** Enables versioning APIs and deploying separate environments (e.g. dev, test, prod) to stages.
*   **WebSocket Duplex Routing:** Supports real-time, persistent connection streams between clients and backends.

---

## 🏛️ Architectural Context (How it fits in the architecture)
API Gateway acts as the public security and routing layer at the front of serverless architectures. It accepts external client requests, validates Cognito authentication tokens or IAM signatures, handles TLS terminations, caches responses, and proxies requests to Lambda functions.

---

## 🧩 Problem Solver (What problem it solves)
Without API Gateway, developers must host and configure reverse proxies (like Nginx), manage certificates, write custom authentication filters, configure load balancers, and build rate-limiting and versioning tools. API Gateway manages this lifecycle out-of-the-box in a serverless model.

---

## 🟢 Operational Impact (What will happen with it operating)
Clients query stable HTTPS endpoints. API Gateway handles traffic peaks automatically, caching responses at the edge when configured, and invoking backend microservices while tracking execution metrics and latencies in CloudWatch.

---

## 🔴 Failure Impact (What will happen without it)
If the API Gateway service fails or becomes unreachable:
*   External clients cannot connect to backend microservices, returning HTTP errors immediately.
*   Security validations (Cognito checks, rate limiting) are bypassed or fail closed, locking out users.
*   Running Lambda backends remain active but receive zero ingress request events.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **API Gateway**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

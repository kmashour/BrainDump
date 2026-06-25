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
*   **Request Routing & Ingress Endpoints:** Routes incoming HTTPS traffic to backends (Lambda, public/private HTTP, or AWS APIs). Supported endpoint types include:
    *   *Edge-Optimized:* Deployed globally using CloudFront Edge locations. ACM SSL certificates must reside in `us-east-1`.
    *   *Regional:* Deployed locally in the same region as the client. ACM SSL certificates must reside in the same region.
    *   *Private:* Accessible only inside a user's VPC via Interface VPC Endpoints (PrivateLink) and secured via resource policies.
*   **Strict Timeout Enforcements:** Enforces a hard integration limit of **29 seconds**. If the backend (e.g., a Lambda function) does not respond within this window, API Gateway closes the connection and returns an HTTP `504 Gateway Timeout` to the client.
*   **Traffic Management & Throttling:** Protects backends from resource exhaustion using a token-bucket rate-limiting algorithm. Throttling limits can be configured globally, per-stage, or per-method, and can be tied to API Keys.
*   **Response Caching:** Stores backend responses inside a local cache, allowing API Gateway to serve static/predictable requests directly, reducing backend execution load and costs.
*   **API Versioning & Lifecycle:** Supports deploying multiple versions of APIs to distinct environments (e.g., `dev`, `test`, `prod`) represented as stages.
*   **WebSocket Protocol Support:** Exposes full-duplex WebSocket connections to maintain real-time, persistent connection states between clients and backends.

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

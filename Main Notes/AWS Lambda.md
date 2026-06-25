---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[API Gateway]]"
  - "[[Amazon DynamoDB]]"
  - "[[Amazon Cognito]]"
  - "[[aws - IAM Role]]"
  - "[[aws - Virtual Private Cloud]]"
  - "[[RDS Proxy]]"
against:
  - "[[aws - EC2 Instance]]"
  - "[[Amazon ECS]]"
reference_guides:
  - "[[Reference Notes/3-18_serverless.md]]"
tags:
  - aws/lambda
  - status/completed
---

# AWS Lambda

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **AWS Lambda**

---

## 🎯 Purpose (Why it is used)
AWS Lambda is a serverless, event-driven compute service that executes application code on-demand in response to events, automatically managing the underlying compute resources. It operates on a Function-as-a-Service (FaaS) model, charging only for active compute execution time.

---

## ⚙️ Functionality (What it is doing)
*   **Granular Resource Sizing & Storage:** Configurable memory from 128 MB to 10 GB (in 64 MB increments). Increasing memory automatically scales CPU cores and network bandwidth proportionally. Provides writeable ephemeral storage via the `/tmp` directory (up to 10 GB).
*   **Operating Limits:** Maximum execution timeout is strictly **15 minutes (900 seconds)**. Deployment package limits are **50 MB** for compressed zip files and **250 MB** for uncompressed code/dependencies.
*   **Concurrency Management:** 
    *   *Reserved Concurrency:* Allocates a dedicated portion of the account's concurrency pool (default 1,000) to guarantee capacity for critical functions while capping maximum concurrent executions to prevent downstream resource exhaustion.
    *   *Provisioned Concurrency:* Pre-warms execution environments to eliminate cold starts for latency-sensitive applications.
    *   *SnapStart:* Pre-initializes memory and disk states for Java functions, capturing a snapshot upon publication to reduce cold start boot times up to 10x at no extra cost.
*   **VPC Private Connectivity & ENI Evolution:**
    *   *Hyperplane ENI Allocation:* Connects functions securely to private resources (e.g. RDS, internal ALBs) in private subnets using Elastic Network Interfaces (ENIs).
    *   *Evolutionary Shift:* Transitioned from the legacy model (where AWS dynamically created and attached ENIs during the invocation cold start, causing a 10–30 second latency penalty) to the **AWS Hyperplane** model. Hyperplane pre-allocates shared ENIs inside user subnets at creation/update time, reducing VPC cold start overhead to sub-second levels and conserving IP addresses.
*   **RDS Proxy Integration:** Pools database connections to prevent Lambda scaling spikes from exhausting RDS backend ports, while reducing database failover times by up to 66%.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Lambda sits at the core of serverless processing pipelines on AWS. It is triggered by ingress gateways (API Gateway, ALB), streaming platforms (Kinesis, DynamoDB Streams), or asynchronous brokers (SQS, SNS, S3 event notifications), writing outputs to databases like DynamoDB or shared storage.

---

## 🧩 Problem Solver (What problem it solves)
Without Lambda, administrators must provision virtual servers (EC2) or container hosts, manage OS patches, monitor daemon processes, build scaling policies, and pay for idle server capacity. Lambda abstracts the operating system and hardware layers entirely, reducing operational overhead and compute costs.

---

## 🟢 Operational Impact (What will happen with it operating)
Applications run as independent, stateless handler functions. Scalability is automated; traffic spikes trigger immediate concurrency expansions. Monitoring is natively integrated via CloudWatch logs, and billing is metered in millisecond increments.

---

## 🔴 Failure Impact (What will happen without it)
If the Lambda compute service encounters failures or reaches limits:
*   API requests fail, returning `502 Bad Gateway` or `504 Gateway Timeout` errors to clients.
*   Event streams (SQS, Kinesis) build up backlogs because consumer functions are not running.
*   Asynchronous event triggers default to retry backoff loops, eventually dropping events to Dead-Letter Queues (DLQs).

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **AWS Lambda**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

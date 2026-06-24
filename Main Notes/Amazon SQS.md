---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[aws]]"
  - "[[Amazon SNS]]"
  - "[[Amazon Kinesis]]"
  - "[[Amazon MQ]]"
against:
  - "[[Amazon SNS]]"
  - "[[Amazon MQ]]"
reference_guides:
  - "[[Reference Notes/3-14_aws_sqs_sns_decoupling.md]]"
tags:
  - aws/sqs
  - status/completed
---

# Amazon SQS

**Breadcrumbs:** [[0-Index|🏠 Index]] > Infrastructure > **Amazon SQS**

---

## 🎯 Purpose (Why it is used)
Amazon SQS (Simple Queue Service) is a fully managed message queuing service that enables the decoupling and scaling of microservices, distributed systems, and serverless applications. It acts as an asynchronous communication buffer between different application tiers, ensuring that message producers can send data without waiting for consumers to process it.

---

## ⚙️ Functionality (What it is doing)
- **Queueing Middleware:** Stores messages durably in queues. Producers enqueue messages using the `SendMessage` API; consumers poll messages via `ReceiveMessage`, process them, and delete them via `DeleteMessage`.
- **Queue Types:**
  - **Standard Queues:** Provide unlimited throughput, at-least-once delivery (potential duplicates), and best-effort ordering.
  - **FIFO Queues:** Guarantee first-in-first-out ordering and exactly-once delivery (duplicates removed within a 5-minute window based on deduplication ID).
- **Message Visibility Timeout:** Prevents other consumers from processing a polled message for a set time (default 30 seconds). Consumers can extend this using the `ChangeMessageVisibility` API.
- **Long Polling:** Reduces API calls and empty responses by allowing consumers to wait up to 20 seconds (`WaitTimeSeconds`) for a message to arrive in an empty queue.

---

## 🏛️ Architectural Context (How it fits in the architecture)
SQS sits between microservices (e.g., front-end APIs and backend workers) to act as a buffer. It is a regional service outside the VPC, accessible via HTTPS API endpoints or private VPC endpoints. It integrates seamlessly with EC2 Auto Scaling Groups (ASG) and AWS Lambda.

---

## 🧩 Problem Solver (What problem it solves)
SQS solves the problem of tight coupling and synchronous bottlenecks. In synchronous systems, if a backend service fails or gets overwhelmed by a traffic spike, the entire system crashes. SQS buffers request bursts, handles rate mismatches, and prevents data loss when downstream systems are unavailable.

---

## 🟢 Operational Impact (What will happen with it operating)
Systems gain horizontal scalability. Workers can scale dynamically based on the queue depth metric (`ApproximateNumberOfMessages`). Message delivery is secure with server-side encryption (`SSE-SQS` or `SSE-KMS`), and workloads are processed reliably with dead-letter queue (DLQ) support for failed messages.

---

## 🔴 Failure Impact (What will happen without it)
Without SQS, spikes in user traffic will directly overload backend databases or applications, causing HTTP 5xx errors, timeouts, and transaction losses. If a backend processing component fails, upstream systems will also fail (cascading failures).

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Amazon SQS**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

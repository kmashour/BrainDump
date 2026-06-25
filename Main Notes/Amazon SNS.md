---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[aws]]"
  - "[[Amazon SQS]]"
  - "[[Amazon Kinesis]]"
  - "[[Amazon MQ]]"
against:
  - "[[Amazon SQS]]"
  - "[[Amazon Kinesis]]"
reference_guides:
  - "[[Reference Notes/3-14_aws_sqs_sns_decoupling.md]]"
tags:
  - aws/sns
  - status/completed
---

# Amazon SNS

**Breadcrumbs:** [[0-Index|🏠 Index]] > Infrastructure > **Amazon SNS**

---

## 🎯 Purpose (Why it is used)
Amazon SNS (Simple Notification Service) is a fully managed pub/sub (publish/subscribe) messaging service. It provides high-throughput, push-based delivery of messages from publishers to multiple subscriber endpoints, facilitating event-driven architectures and immediate notification delivery.

---

## ⚙️ Functionality (What it is doing)
- **Pub/Sub Brokerage:** Publishers send a single message to an SNS Topic. SNS replicates and distributes that message to all active subscriber endpoints.
- **Subscribers Support:** Integrates with SQS, Lambda, HTTP/HTTPS webhooks, email, SMS, and mobile push notifications (APNS, GCM/FCM, ADM).
- **Message Filtering:** Allows subscribers to define JSON Filter Policies to receive only a subset of messages (e.g., filtering based on message attributes like `State = "Placed"`).
- **SNS FIFO Topics:** Combines with SQS FIFO queues to guarantee strict ordering (by Message Group ID) and deduplication (via Deduplication ID or content-based deduplication).
- **No Persistence:** Standard SNS messages are not persistent. If a subscriber is down and retries fail, messages can be lost unless buffered by SQS queues or redirected to DLQs.
- **S3 Event Notification Fanning:** Bypasses S3's limitation of only allowing a single event rule destination for a prefix/suffix combination. S3 publishes the event to an SNS topic, which then fans it out to multiple SQS queues or other subscribers.

---

## 🏛️ Architectural Context (How it fits in the architecture)
SNS serves as an event router or publisher hub. When an event occurs (e.g., an S3 object is created, or a customer checkout completes), the event is published to SNS, which fans it out to multiple downstream queues or processing lambdas.

---

## 🧩 Problem Solver (What problem it solves)
SNS eliminates the need for a service to write custom integration code for every downstream system that needs to know about an event. Instead of a service sending 5 distinct requests to 5 systems (which increases latency and risk of partial failure), the service publishes once to SNS, leaving message routing to AWS.

---

## 🟢 Operational Impact (What will happen with it operating)
Applications can react instantly to events. Downstream services can be added or removed dynamically as subscribers without affecting the upstream publisher application. Messages can be encrypted at rest (`SSE-KMS`) and are delivered over HTTPS in flight.

---

## 🔴 Failure Impact (What will happen without it)
Without SNS, fan-out event distribution requires complex synchronous coordination or expensive batch processing. Adding a new downstream subscriber requires modifying the publisher's code, creating tight architectural coupling and operational overhead.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Amazon SNS**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[aws]]"
sub_type: core-concept
source_type: documentation
source_url: "https://docs.aws.amazon.com/sqs/"
author: "AWS Documentation"
course_title: "AWS Microservice Integration Patterns"
against: []
tags:
  - aws/sqs
  - aws/sns
  - aws/decoupling
  - aws/deep-dive
---

# aws - SQS, SNS, and Decoupled Microservices

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[aws]] > **SQS, SNS, and Decoupled Microservices**

---

## 📑 Asynchronous Messaging: SQS

Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications.

*   **Decoupling:** Message producers (e.g. web frontends) send messages to the queue, and consumers (e.g. backend workers) poll the queue. This prevents cascading failures if the backend goes down or experiences traffic spikes.
*   **Queue Types:**
    *   **Standard Queues:** Offers maximum throughput, best-effort ordering, and at-least-once delivery (messages can occasionally be duplicated).
    *   **FIFO (First-In-First-Out) Queues:** Guarantees that messages are processed exactly once and in the exact order they are sent, with a throughput limit (300 transactions/sec without batching).

---

## 📑 Publish/Subscribe: SNS Fan-Out

Amazon Simple Notification Service (SNS) is a fully managed pub/sub messaging service.

*   **Topics and Subscribers:** Publishers push messages to an SNS Topic. SNS automatically delivers the message to all subscribed endpoints (e.g., SQS queues, Lambda functions, HTTP endpoints, email, or SMS).
*   **Fan-Out Pattern:** By subscribing multiple SQS queues to a single SNS Topic, developers can trigger multiple independent background tasks concurrently from a single event.

*Read more in [3-14_aws_sqs_sns_decoupling.md](../Reference%20Notes/3-14_aws_sqs_sns_decoupling.md)*

### 🔍 Related Conceptual landing-notes
*   [[Amazon SQS]]
*   [[Amazon SNS]]
*   [[Amazon Kinesis]]
*   [[Amazon MQ]]


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
*   **S3 Event Notification Fanning:** Bypasses S3's single-destination rule by sending notifications to SNS first, which then duplicates and pushes to multiple SQS queues.

---

## 📑 Real-Time Streaming: Amazon Kinesis

Amazon Kinesis provides real-time streaming ingestion and analysis for high-throughput big data workloads.

*   **Kinesis Data Streams:** Divided into shards, providing persisted, replayable streaming data. Partition keys guarantee ordering within a shard. Provisioned (manual) and On-Demand (automatic) scaling modes are supported.
*   **Amazon Data Firehose:** Serverless, near real-time ingestion pipeline that buffers streaming data (by size or time) and flushes it to target lakes (S3, Redshift, OpenSearch, etc.) with optional Lambda transformations on the fly.

---

## 📑 Hybrid/Legacy Brokerage: Amazon MQ

Amazon MQ is a managed message broker service for traditional RabbitMQ and ActiveMQ engines.

*   **Migration:** Ideal for lift-and-shift of legacy on-premises microservices that rely on open protocols (AMQP, MQTT, STOMP, OpenWire, WSS) rather than AWS-native proprietary APIs.
*   **Active-Standby HA:** Deploys brokers across AZs using **Amazon EFS** as a shared storage layer to synchronize states and ensure automatic failover.

---

*Read more in [3-14_aws_sqs_sns_decoupling.md](../Reference%20Notes/3-14_aws_sqs_sns_decoupling.md)*

### 🔍 Related Conceptual landing-notes
*   [[Amazon SQS]]
*   [[Amazon SNS]]
*   [[Amazon Kinesis]]
*   [[Amazon MQ]]


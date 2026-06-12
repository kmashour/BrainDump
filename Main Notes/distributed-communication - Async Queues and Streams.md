---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[distributed-communication]]"
sub_type: core-concept
source_type: documentation
source_url: "https://www.youtube.com/watch?v=C842vFY5kRo"
author: "Hayk Simonyan"
course_title: "System Design Course"
against: []
tags:
  - system-design/communication
  - system-design/deep-dive
---

# Distributed Communication - Async Queues and Streams

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[distributed-communication]] > **Async Queues and Streams**

---

## 📑 Core Asynchronous Communication Models

Distributed systems use three main patterns to coordinate asynchronous workloads:

### 1. Message Queues (Point-to-Point)
- **Concept:** A producer puts a message in a named queue, and a single worker from a pool of competing consumers processes it.
- **Delivery Model:** 1-to-1. Once a worker acknowledges (ACKs) the message, the broker removes it from the queue.
- **Best Use Case:** Work distribution (e.g., video encoding, report generation, email dispatch).
- **Common Choices:** RabbitMQ, AWS SQS, ActiveMQ.

### 2. Publish/Subscribe (Pub/Sub)
- **Concept:** A publisher writes an event to a named **Topic**. The broker distributes a copy of this message to all registered subscriber channels.
- **Delivery Model:** 1-to-Many. Multiple downstream systems receive the same event and execute independent workflows.
- **Best Use Case:** Event broadcasting (e.g., notifying billing, inventory, and shipping services when an `OrderCompleted` event occurs).
- **Common Choices:** AWS SNS, GCP Pub/Sub, Redis Pub/Sub.

### 3. Distributed Commit Log Streaming
- **Concept:** Events are written sequentially to an append-only commit log on disk.
- **Delivery Model:** 1-to-Many via consumer offsets. Messages are not deleted after consumption; they persist on disk for a retention window.
- **Scaling Mechanism:** Topics are split into **Partitions** distributed across multiple broker nodes, allowing parallel reads/writes.
- **Best Use Case:** High-throughput event streaming, event sourcing, real-time analytics pipelines.
- **Common Choices:** Apache Kafka, Apache Pulsar, AWS Kinesis.

---

## 📑 Comparison Matrix

| Attribute | Message Queues | Pub/Sub | Distributed Streams (Kafka) |
| :--- | :--- | :--- | :--- |
| **Routing Model** | Point-to-Point (Queue) | Topic-to-Subscription | Partitioned Log |
| **Consumption Style** | Push/Pull (Competing workers) | Push (Broadcasting channels) | Pull (Consumer Group offsets) |
| **Message Lifespan** | Deleted on ACK | Deleted on subscriber delivery | Retained on disk (TTL-based) |
| **Ordering Guarantees** | FIFO (Within queue limits) | None guaranteed globally | Strict order *within a partition* |
| **Replayability** | No | No | Yes (Rewind offsets) |
| **Throughput Capacity** | Moderate | High | Extreme (Disk-sequential caching) |

*Read more in [[Reference Notes/1-8_distributed_communication_and_queues.md#1. Synchronous vs. Asynchronous Communication]]*

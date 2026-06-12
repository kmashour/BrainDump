---
domains:
  - "aws"
  - "decoupling"
---

# Module 3-14: AWS SQS & SNS Decoupling

**Breadcrumbs:** [[3-Index - AWS|📐 AWS Index]] > **Module 3-14: AWS SQS & SNS Decoupling**

This module details queueing protocols, pub/sub notification patterns, event-driven designs, and microservice decoupling.

---

## 🔄 Decoupled vs. Coupled Architectures

In a tightly coupled architecture, if a downstream service fails, the entire transaction fails. Decoupling introduces an asynchronous buffer:

```
Tightly Coupled:   [Web Tier] ---(Direct Call)---> [Database] (Database down = System Down)

Decoupled:         [Web Tier] ---> [SQS Queue] ---> [Worker Tier] ---> [Database]
                                (Messages safely stored in Queue if Database down)
```

---

## 📥 Amazon SQS (Simple Queue Service)

* **Standard Queue:** Unlimited throughput. Offers **at-least-once** delivery and best-effort ordering (messages can arrive out of order or be duplicated).
* **FIFO Queue (First-In-First-Out):** Limits throughput to 300 messages per second (or 3000 with batching). Guarantees **exactly-once** delivery and strict ordering.
* **SQS Properties:**
  * *Visibility Timeout:* The period (default 30 seconds) during which a consumer hides a message from other consumers. If the consumer fails to process and delete the message before the timeout expires, the message becomes visible again.
  * *Long Polling:* Keeps connections open for up to 20 seconds, waiting for messages to arrive. Reduces empty responses and costs.
  * *Dead-Letter Queue (DLQ):* A separate queue where messages that fail processing after a set number of retries are sent for debugging.

---

## 🧠 Deep-Intuition (AARF) Breakdown: SQS FIFO Deduplication

1. **The Answer (Core Pattern):** Deploy SQS FIFO queues with Message Deduplication IDs (`MessageDeduplicationId`) to ensure duplicate transactions sent within a 5-minute window are discarded:
    ```bash
    aws sqs create-queue --queue-name Orders.fifo --attributes FifoQueue=true,ContentBasedDeduplication=true
    ```
2. **The Assumptions (Context):** The queue name must end with the `.fifo` suffix, and message producers must provide a deduplication token or enable content-based deduplication (SHA-256 hash of the message body).
3. **The Rationale (Why):** Eliminates double-processing. If a network glitch causes a payment service to send the same transaction twice, the FIFO queue detects the matching deduplication token and discards the second message.
4. **The Failure Loop (What if not):** Using standard SQS queues for bank transactions risks duplicate processing, leading to duplicate credit card charges and data inconsistency.
5. **Alternative Case (When to use 'if not'):** For analytics clickstream logs where duplicate events are acceptable, use standard SQS to maximize processing throughput.

---

## 📢 Amazon SNS (Simple Notification Service)

* **Pub/Sub Model:** Publishers send messages to an **SNS Topic**. SNS fans out the message to all active **Subscribers** (SQS, Lambda, Email, HTTP endpoints).
* **Message Size:** Messages in SQS/SNS cannot exceed **256 KB**. For larger payloads, use the claim-check pattern: store the payload in S3 and pass the S3 object URL in the message body.

---

## 🧠 Deep-Intuition (AARF) Breakdown: SNS + SQS Fan-Out

1. **The Answer (Core Pattern):** Publish events to a single SNS Topic and subscribe multiple SQS queues (e.g., ShippingQueue, BillingQueue) to the topic to process the event in parallel.
2. **The Assumptions (Context):** SQS queue policies must grant the SNS service principal permission to send messages.
3. **The Rationale (Why):** Enhances scalability. When a user submits an order, the application publishes one message to SNS. SNS duplicates and pushes the message to both SQS queues, allowing billing and shipping microservices to run concurrently and scale independently.
4. **The Failure Loop (What if not):** Modifying the core application code to send individual messages to multiple queues increases processing latency and risks partial failures if one queue request fails.
5. **Alternative Case (When to use 'if not'):** For point-to-point communication where only one downstream consumer processes the message, bypass SNS and write directly to SQS.

![[../Attachments/Pasted image 20250510235011.png]]

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
  - "[[Amazon SNS]]"
against:
  - "[[Amazon SQS]]"
  - "[[Amazon SNS]]"
reference_guides:
  - "[[Reference Notes/3-14_aws_sqs_sns_decoupling.md]]"
tags:
  - aws/mq
  - status/completed
---

# Amazon MQ

**Breadcrumbs:** [[0-Index|🏠 Index]] > Infrastructure > **Amazon MQ**

---

## 🎯 Purpose (Why it is used)
Amazon MQ is a managed message broker service for RabbitMQ and ActiveMQ. It is designed to facilitate the migration of legacy, on-premises applications to the AWS cloud by providing compatibility with industry-standard messaging protocols, avoiding the need to re-engineer microservice integration code.

---

## ⚙️ Functionality (What it is doing)
- **Managed Broker Engines:** Provisions and manages instances of Apache ActiveMQ or RabbitMQ.
- **Protocol Compatibility:** Supports industry-standard messaging protocols including AMQP, MQTT, STOMP, OpenWire, and WSS.
- **Combined Messaging Patterns:** Offers both queue (point-to-point) and topic (pub/sub) capabilities within a single broker instance.
- **Active-Standby High Availability:** Configures a hot-standby broker in a secondary Availability Zone that automatically takes over if the primary broker fails.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Amazon MQ is a server-based broker deployed inside a customer's VPC. Unlike serverless SQS and SNS, Amazon MQ runs on dedicated virtual instances. It connects legacy applications using open standards, using Amazon EFS (Elastic File System) as a shared backend storage layer to sync state between Active and Standby instances.

---

## 🌉 Evolutionary Bridge: Legacy Protocols vs. Cloud-Native Messaging

### 1. Traditional Enterprise Messaging (Classic Concept)
Traditional on-premises message brokers (e.g., ActiveMQ, RabbitMQ) rely on open-standard stateful protocols (AMQP, MQTT, STOMP). These systems were designed for persistent client-broker TCP connections, requiring dedicated virtual or physical servers, manual cluster orchestration, and local file storage systems to manage message queues.

### 2. Bridging the Gap to Managed Cloud
Amazon MQ bridges this gap by offering a fully managed environment for these traditional brokers. It eliminates the manual work of provisioning, clustering, and patching server instances. To provide high availability without re-architecting the applications, Amazon MQ deploys an Active-Standby pair across Availability Zones, mounting a shared network volume on **Amazon EFS** to dynamically replicate state and ensure seamless failover.

### 3. Evolutionary Constraints and Differences
- **Scaling Limits:** Legacy brokers scale vertically or via static server clusters, limiting their throughput capacity. In contrast, cloud-native services like **Amazon SQS** and **Amazon SNS** are serverless, API-driven, and scale horizontally and dynamically to near-infinity.
- **Operational Model:** Amazon MQ runs on managed server instances, meaning users must choose instance sizes, manage throughput limits, and coordinate maintenance windows. SQS and SNS are completely serverless, billing only for usage.
- **Connection Overhead:** AMQP/MQTT maintain long-lived TCP connections, which can hit connection limits on server brokers, whereas cloud-native SQS/SNS operate over standard stateless HTTP REST APIs.

---

## 🧩 Problem Solver (What problem it solves)
Amazon MQ solves the high cost and complexity of rewriting legacy on-premises applications during migration. Instead of refactoring thousands of lines of code to use proprietary SQS/SNS APIs, developers can perform a "lift-and-shift" migration by updating only the broker endpoint URLs.

---

## 🟢 Operational Impact (What will happen with it operating)
Workloads migrate to the cloud with minimal code changes. The message broker runs on AWS-managed infrastructure, reducing maintenance overhead. Active-standby failover using Amazon EFS backend storage guarantees message durability and service continuity.

---

## 🔴 Failure Impact (What will happen without it)
Without Amazon MQ, migrating legacy applications using JMS, AMQP, or MQTT to AWS requires a complete rewrite of their messaging layers to use SQS/SNS APIs. This increases migration risk, cost, and timelines. Alternatively, hosting self-managed RabbitMQ/ActiveMQ on EC2 instances introduces high operational overhead.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Amazon MQ**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

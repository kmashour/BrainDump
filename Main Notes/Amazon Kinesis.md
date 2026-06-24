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
  - aws/kinesis
  - status/completed
---

# Amazon Kinesis

**Breadcrumbs:** [[0-Index|🏠 Index]] > Infrastructure > **Amazon Kinesis**

---

## 🎯 Purpose (Why it is used)
Amazon Kinesis is a fully managed service designed to ingest, buffer, and analyze real-time streaming data at scale. It excels at handling massive, continuous streams of high-throughput data (such as log files, clickstreams, and IoT telemetry) for immediate operational analysis and ingestion.

---

## ⚙️ Functionality (What it is doing)
- **Kinesis Data Streams:** Collects data continuously. Divided into shards, where each shard supports 1 MB/s write and 2 MB/s read. Supports provisioned and on-demand capacity modes.
- **Data Persistence:** Persists data for 1 to 365 days, enabling consumers to replay or backprocess past streams.
- **Enhanced Fan-Out (EFO):** Pushes data to consumers using HTTP/2, providing a dedicated 2 MB/s throughput per shard per consumer.
- **Amazon Data Firehose:** Serverless delivery stream that buffers incoming data (by size or time) and flushes it to targets (S3, Redshift, OpenSearch, Splunk, HTTP) with optional Lambda transformations.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Kinesis acts as the entry pipeline for real-time big data processing. It connects log/metric producers (via Kinesis Agent or SDK) to processing tools like Apache Flink, AWS Lambda, or data lakes like Amazon S3.

---

## 🧩 Problem Solver (What problem it solves)
Kinesis solves the challenge of real-time high-throughput big data ingestion. Standard queuing services (like SQS) are not optimized for ordering at scale across petabytes of streaming data or for allowing multiple applications to read the exact same history of events concurrently.

---

## 🟢 Operational Impact (What will happen with it operating)
Organizations gain the ability to analyze metrics, detect fraud, and monitor application behaviors in real time. Shards can be split or merged manually or scale dynamically to match ingestion rates, and encryption is secured at rest via KMS.

---

## 🔴 Failure Impact (What will happen without it)
Without Kinesis, streaming data must be collected in batches or written directly to databases, causing bottlenecks, high database storage costs, and delays in processing. Systems cannot perform real-time monitoring or immediate anomaly detection.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Amazon Kinesis**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

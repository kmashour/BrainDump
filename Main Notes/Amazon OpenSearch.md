---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
  - "database"
related_concepts:
  - "[[Amazon S3]]"
  - "[[Amazon Kinesis]]"
against:
  - "[[Amazon Athena]]"
reference_guides:
  - "[[Reference Notes/3-19_databases_analytics_ml.md]]"
tags:
  - aws/opensearch
  - database/search-engine
  - status/completed
---

# Amazon OpenSearch

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **Amazon OpenSearch**

---

## 🎯 Purpose (Why it is used)
Amazon OpenSearch Service (successor to Amazon Elasticsearch Service) is a managed search and analytics engine. It is used for real-time application monitoring, log analytics, website search, and auditing, allowing users to query, analyze, and visualize millions of logs or data points with sub-second latencies.

---

## ⚙️ Functionality (What it is doing)
*   **Full-Text Search:** Indexes and searches unstructured or semi-structured data using full-text search algorithms.
*   **Log Ingestion & Indexing:** Accepts real-time log streams directly from CloudWatch Logs, Kinesis Data Firehose, or Logstash.
*   **Visualization:** Integrates directly with OpenSearch Dashboards (formerly Kibana) to display real-time metrics, geographical logs, and threat maps.
*   **Serverless Mode:** Offers a serverless option that scales index performance and query capacity automatically without managing instance brokers.

---

## 🏛️ Architectural Context (How it fits in the architecture)
OpenSearch serves as the destination for observability pipelines. Application instances send logs to CloudWatch Logs or Kinesis, which routes them to OpenSearch. Operators then access OpenSearch Dashboards to monitor application performance and trace errors.

---

## 🧩 Problem Solver (What problem it solves)
Querying billions of raw log lines (like system logs or access logs) using standard databases or grep tools is slow and inefficient. OpenSearch indexes logs into searchable inverted indexes, allowing users to find specific error strings, IP patterns, or performance outliers in milliseconds.

---

## 🟢 Operational Impact (What will happen with it operating)
Operational observability is in real-time. Systems engineering teams can query error events as they occur, build dashboards tracking system load, and configure alarms when error rates exceed safe thresholds.

---

## 🔴 Failure Impact (What will happen without it)
Without OpenSearch, troubleshooting production application issues requires manually logging into servers, downloading vast text log files, and using slow command-line tools to identify and isolate failures.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Amazon OpenSearch**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

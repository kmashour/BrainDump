---
obsidianUIMode: preview
class: project-note
tier: project
domains:
  - "linux"
concepts_referenced:
  - "[[linux]]"
tags:
  - observability
  - prometheus
  - grafana
difficulty: intermediate
status: completed
---

# Chapter 4: Observability with Prometheus & Grafana

**Breadcrumbs:** [[Projects/PwC Interview Preparation/Plan - DevOps Interview Roadmap|DevOps Interview Roadmap]] > Theory > **Chapter 4: Prometheus & Grafana**

---

## 📈 1. Observability Fundamentals: Three Pillars
1.  **Metrics (Aggregated Telemetry):** Numeric, time-series data representing system performance over time (e.g. CPU load, HTTP error rates). Highly efficient, low-storage overhead. Used for dashboarding and alerting.
2.  **Logs (Event Records):** Plain text or structured JSON lines describing individual event actions (e.g. stack traces, access logs). High storage overhead, essential for deep post-incident diagnostics.
3.  **Traces (Request Pathways):** Tracks the lifecycle of a request as it traverses distributed microservices (e.g. Jaeger spans). Crucial for finding latency bottlenecks in network calls.

---

## 🔌 2. Prometheus Architecture

Prometheus is a pulling, time-series data scraper and storage engine.

```
                    +-------------------+
                    | Prometheus Server |
                    |                   |
                    |   +-----------+   |   (Pull via HTTP /metrics)
                    |   | TSDB Disk |<--+----------------------------+
                    |   +-----------+   |                            │
                    +---------┬---------+                            ▼
                              │                        +--------------------------+
                              v (Alerts)               |   Target Application     |
                    +-------------------+              |  Exposes metrics client  |
                    |   Alertmanager    |              |  (Flask, Node Exporter)  |
                    +-------------------+              +--------------------------+
```

### A. The Scraper Pull Model
Unlike traditional pushing agents, the Prometheus server controls the metrics ingestion pipeline.
*   **The Pull Process:** Prometheus parses its static configuration or queries service discovery (such as the Kubernetes API) to discover active hosts. At regular intervals (`scrape_interval`, default 15s), the server makes an HTTP GET request to the target's `/metrics` path.
*   **Benefits of Pull:** 
    *   Targets cannot flood the monitoring system. If the Prometheus server is running low on disk/memory, it controls the scrape load.
    *   No complex agent credentials are required on target hosts; they simply expose a read-only HTTP endpoint.
    *   Easy detection of host down states: if a scrape request fails, Prometheus automatically flags the `up` metric as `0`.

### B. TSDB Internals (Time Series Database)
Prometheus stores scraped metrics in-memory first, flushing data to disk blocks every 2 hours.
*   **WAL (Write-Ahead Log):** Before raw scrapes are cached in memory, they are appended to the WAL on disk. This prevents data loss if the host crashes before the 2-hour block is compiled.
*   **Block Directories:** Every 2 hours, memory data is compressed into a block directory containing:
    *   `chunks/`: Raw time-series database segments.
    *   `index`: Maps labels and metric names to specific byte offsets in the chunks.
    *   `meta.json`: Details block compaction metadata.

---

## 📊 3. PromQL & Metrics Exposition

### A. Core Metric Types
1.  **Counter:** A cumulative value that only increases (or resets to 0 on target restart).
    *   *Rule:* Never apply operations directly to counters; always wrap them in functions like `rate()` or `increase()`.
2.  **Gauge:** A value that goes up and down (e.g., memory usage, active connections).
3.  **Histogram:** Measures the frequency of observations across pre-defined boundary buckets (`le` label), alongside total sum and count.
    *   *Use Case:* Tracking SLO latencies.
4.  **Summary:** Client-side calculated quantiles (e.g. 95th percentile). Cannot be aggregated across multiple servers.

### B. Essential PromQL Operations
*   **Instant Vector:** Represents the current status of all matching metrics (e.g. `http_requests_total`).
*   **Range Vector:** Captures a buffer of data points over time (e.g. `http_requests_total[5m]` captures all scrapes in the last 5 minutes). Range vectors cannot be plotted directly; they are passed to aggregation functions.
*   **The `rate()` vs. `irate()` differences:**
    *   `rate()`: Calculates the per-second average rate of change over the *entire* range vector window. Resilient to missing scrapes, ideal for alerting.
    *   `irate()`: Calculates the rate based on only the *last two data points* in the range vector. Highly volatile, captures quick spikes.
*   **Sum Aggregations:**
    `sum(rate(http_requests_total[5m])) by (http_status)`
*   **SLA Quantile Calculation (95th Percentile Latency):**
    `histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))`

---

## 🚨 4. Alertmanager Alert Routing & Deduplication

Prometheus fires alerts to **Alertmanager**, which manages notifications.
*   **Deduplication (Grouping):** Combines similar alerts (e.g., 50 servers firing "Disk Pressure" alerts in the same cluster) into a single notification, preventing page flood.
*   **Inhibitions:** Suppresses warnings if a critical parent alert is already firing (e.g., if "Host Down" is active, silence all application-level "Service Down" alerts for that host).
*   **Silences:** Mutes notifications during scheduled maintenance windows.

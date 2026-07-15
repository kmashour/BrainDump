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
difficulty: advanced
status: completed
---

# Chapter 5: Observability, Telemetry, and Logging Stack (AWS & CNCF)

**Breadcrumbs:** [[Projects/PwC Interview Preparation/Plan - DevOps Interview Roadmap|DevOps Interview Roadmap]] > Theory > **Chapter 5: Observability Stack**

---

## ☁️ 1. AWS CloudWatch Host Instrumentation & Filter Algebra

In an enterprise AWS deployment, observability spans host metrics, log filters, and composite alarm routing.

### A. Hypervisor vs. Agent Telemetry
*   **Hypervisor Metrics (EC2 Defaults):** AWS gathers metrics from the host virtualization hypervisor without VM access. These are limited to CPU utilization, virtual disk I/O metadata, and network throughput. The hypervisor cannot read OS-level memory tables or internal filesystem blocks.
*   **Unified CloudWatch Agent Metrics:** To gather RAM utilization, active swap usage, and directory storage allocation, you must run the Unified CloudWatch Agent daemon inside the guest OS. The agent queries virtual filesystem tables (like `/proc/meminfo` and `/proc/diskstats`) and sends the data to CloudWatch via JSON API calls.

### B. Custom Log Metric Filters
Analyze log streams on-the-fly to compile metrics using Metric Filters.
*   **Regex Pattern Matching:** Match Nginx or application log formats:
    `[ip, id, user, timestamp, request, status_code = 4*, size]`
*   This matches lines where the 6th field starts with `4`, incrementing a custom metric count in real-time, allowing you to configure threshold alarms before post-incident audits occur.

### C. Composite Alarms
*   **The Problem:** High load triggers multiple dependent alarms (e.g. CPU spikes, DB connections saturation, API latency delays), causing a notification storm.
*   **The Solution:** Use Composite Alarms with Boolean algebra:
    `ALARM(HighCPU) AND ALARM(HighAPI_Latency) AND NOT ALARM(MaintenanceMode)`
*   This reduces alert fatigue by only alerting engineers under specific matching scenarios.

---

## 🔌 2. Prometheus Engine: Scraping Mechanics & Service Discovery

Prometheus operates on an HTTP-pull model, which dictates how the metric ingestion pipeline scales.

### A. Target Service Discovery (SD)
Prometheus dynamically updates its scraping list:
*   **Kubernetes SD:** Watches the `kube-apiserver` Endpoint resource tree, matching Pod labels or annotations (e.g., `prometheus.io/scrape: "true"`).
*   **AWS EC2 SD:** Queries AWS regional APIs to fetch running instances matching specific tag filters.

### B. Pull vs. Push Systems
*   **Push Model (e.g. InfluxDB push):** Agents stream metrics to the server. If the application environment scales out during a traffic peak, the volume of metrics pushes can saturate the central collector, causing a crash.
*   **Pull Model (Prometheus):** The server polls targets at regular intervals (`scrape_interval`). If Prometheus is low on resources, it can throttle scrapers or drop metrics to protect itself. Additionally, a failed pull request immediately identifies target liveness (`up == 0`).

---

## 💾 3. TSDB Internal Storage Layout

The Time Series Database (TSDB) compiles scrapings into write-efficient blocks:

```plaintext
/var/lib/prometheus/data/
├── 01H3B89X... (2-hour block directory)
│   ├── chunks/          # Raw compressed time-series segments
│   ├── index            # Maps labels to chunks byte offsets
│   ├── meta.json        # Time range, compaction source, and metadata
│   └── tombstones       # Marks deleted data (cleared during compaction)
└── wal/                 # Write-Ahead Log (Uncompressed recovery ledger)
```

1.  **Write-Ahead Log (WAL):** Ingested data is appended to the WAL on disk before it is cached in memory. If a server crash occurs, Prometheus replays the WAL on reboot to restore state.
2.  **Head Block:** The active in-memory block where live series are cached for fast instant querying.
3.  **Compaction:** Every 2 hours, the Head block is closed, compressed, and written to disk as a Block. Over time, background processes compact multiple 2-hour blocks into larger 24-hour blocks to reduce index duplication.

---

## 📊 4. Metrics Exposition & PromQL Vector Math

### A. Client-Side Quantiles (Summary) vs. Server-Side Aggregations (Histogram)
*   **Summary:** Calculates percentiles (e.g., 99th percentile latency) on the application host. Because percentile values are pre-calculated, you **cannot** aggregate them across multiple hosts (e.g., you cannot calculate the average 99th percentile of a cluster by averaging the 99th percentiles of individual nodes).
*   **Histogram:** Counts observations in pre-defined bucket boundaries (`le` label) alongside the total count and sum. Histograms are fully aggregatable. Use **`histogram_quantile`** to calculate cluster-level SLOs:
    `histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))`

### B. PromQL Rate Calculations: `rate()` vs. `irate()`
*   **`rate(metric[5m])`:** Computes the average per-second rate of increase across the entire 5-minute range vector. Smooths out temporary anomalies; recommended for alerts.
*   **`irate(metric[5m])`:** Computes the rate based *only on the last two data points* inside the range vector. Captures rapid spikes; recommended for real-time debugging dashboards.

*See details on AWS monitoring in [[Reference Notes/11-1_cloudops_monitoring_and_logging]] and Prometheus in [[Reference Notes/12-4_prometheus_and_grafana_observability_stack]].*

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

# Chapter 5: Observability, Telemetry, and Logging Stack (Prometheus & Grafana)

**Breadcrumbs:** [[Projects/PwC Interview Preparation/Plan - DevOps Interview Roadmap|DevOps Interview Roadmap]] > Theory > **Chapter 5: Prometheus & Grafana**

---

## 🔌 1. Prometheus Architecture: The Scraper Pull Model

In the interview, explain why Prometheus uses a pull model rather than a push model, and how it handles target discovery:

### A. The HTTP Scrape Process
*   **The Pull Mechanism:** The Prometheus server initiates connections outbound to target hosts on configure intervals (`scrape_interval`). It performs an HTTP GET request to the target's `/metrics` path.
*   **Target Discovery:** Instead of hardcoding IPs, Prometheus utilizes **Service Discovery (SD)** modules (such as Consul, AWS EC2 tags, or Kubernetes API watchers) to dynamically discover newly launched containers and automatically start scraping them.
*   **Pull Model Benefits:**
    *   *Self-Protection:* In push-based monitoring, if a cluster scales up to 1000 nodes, they can flood the central server with metrics packets, triggering a denial-of-service crash. In a pull model, Prometheus scrapes at its own controlled pace. If it runs low on memory, it adjusts scrape rates.
    *   *Dead-State Detection:* If a pull connection fails, Prometheus automatically flags the target's status as down (`up == 0`). A push-based system cannot tell the difference between a crashed node and a node that has no active metrics to report.

### B. TSDB Storage Architecture
Prometheus stores metric time-series data locally on disk:
1.  **Memory Cache & Write-Ahead Log (WAL):** Raw scrapes are written to memory and immediately appended to a disk-based WAL. If a power failure occurs, Prometheus replays the WAL on startup to restore in-memory time-series data.
2.  **2-Hour Compaction Blocks:** Every 2 hours, the in-memory data is compacted and flushed to disk as a Block. The block contains:
    *   `chunks/`: Compressed, binary time-series data points.
    *   `index`: An index mapping metric names and label-value pairs to byte offsets in the chunks.
3.  **Compaction:** Over time, Prometheus runs background compaction merges, combining multiple 2-hour blocks into larger 24-hour blocks to reduce index duplication and disk space.

---

## 📈 2. Metric Types and Exposition Format

Prometheus expects metrics in a plain-text, line-oriented exposition format:
```plaintext
# HELP http_requests_total Total HTTP Requests
# TYPE http_requests_total counter
http_requests_total{endpoint="/api/v1/users",status="200"} 4812
```

### A. Metric Primitives
*   **Counter:** A cumulative value that only increases (or resets to 0 on target reboot). Used to track total event counts, errors, or throughput.
*   **Gauge:** A value that can fluctuate up and down (e.g. CPU temperature, memory usage, queue size).
*   **Histogram:** Observes values (e.g., request durations) and counts them in pre-defined bucket ranges (`le` label), alongside total sum and count. Histograms are fully aggregatable across multiple servers.
*   **Summary:** Similar to histograms, but calculates specific quantiles (e.g., 90th, 99th percentile) client-side. Summaries cannot be aggregated across multiple hosts.

---

## 📊 3. PromQL Query Design & Troubleshooting

Be ready to explain and write these critical PromQL queries:

### A. Counters and Rates
*   *The Rule:* Never run calculations on raw counters. Wrap them in `rate()` or `increase()`.
*   **`rate()` vs. `irate()`:**
    *   `rate(http_requests_total[5m])`: Calculates the average per-second rate of increase across the entire 5-minute range vector. Smooths out temporary anomalies; recommended for alerting.
    *   `irate(http_requests_total[5m])`: Calculates the per-second rate of increase based only on the last two data points of the range vector. Capture quick spikes; recommended for interactive debugging dashboards.
*   **Aggregation:**
    `sum(rate(http_requests_total[5m])) by (endpoint)`

### B. Latency Quantiles (Histograms)
To calculate the 95th percentile latency of HTTP requests:
`histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))`
*   *Explanation:* Reads the bucket sizes (`le` label) and computes the boundary under which 95% of request durations reside.

---

## 🚨 4. Alertmanager Alerting and Routing

Prometheus defines alert thresholds via YAML alerting rules:
```yaml
groups:
  - name: app-alerts
    rules:
      - alert: HighRequestLatency
        expr: histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le)) > 2
        for: 2m
        labels:
          severity: critical
        annotations:
          summary: "Instance {{ $labels.instance }} request latency is too high"
```

If the expression evaluates to true for more than `2m`, Prometheus fires the alert to **Alertmanager**:
*   **Grouping (Deduplication):** Combines similar alerts into a single message (e.g. mutes 100 separate "Pod OOM" alerts into a single Slack notification).
*   **Inhibition Rules:** Silences lower-priority alerts if a critical parent alert is already active (e.g. silences "App unreachable" alerts if "Host Offline" is already firing).
*   **Silences:** Temporarily disables alert notifications during planned maintenance windows.

*See details in [[Reference Notes/8-6_monitoring_logs_and_diagnostics]] and [[Reference Notes/0-14_cluster_administration_and_observability]].*

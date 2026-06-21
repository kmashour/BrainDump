---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Main Notes/aws-cloudops]]"
sub_type: core-concept
source_type: documentation
source_url: "https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html"
author: "Andrew Brown"
course_title: "AWS Cloud Ops Engineer Associate"
tags:
  - aws/cloudwatch
  - aws/deep-dive
---

# aws-cloudops - CloudWatch Agent and Metrics

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Main Notes/aws-cloudops]] > **CloudWatch Agent and Metrics**

---

## 📑 Observability and Host-Level Instrumentation

Observability requires collecting telemetry from both the physical host infrastructure (hypervisor) and the internal operating system kernel space.

### 1. Hypervisor vs. Agent Metrics
*   **Hypervisor Metrics (Default EC2):** Collected from the virtualization layer without host login. Includes physical disk read/write bandwidth, network interfaces throughput, and virtual CPU utilization. The hypervisor has no visibility inside the virtual machine's RAM tables or filesystem structure.
*   **OS/Agent Metrics (Unified CloudWatch Agent):** Requires host authentication and agent execution. By reading `/proc` virtual files (such as `/proc/meminfo` and `/proc/diskstats`), the agent collects memory usage (active, available, cached), swap file activity, active network connections, and directory-level storage block allocation.

### 2. CloudWatch Unified Agent Schema
The configuration schema `/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json` is organized into three major blocks:
1.  **Agent:** Specifies core agent runtime parameters (e.g. interval, credentials, profile, custom host identifier).
2.  **Metrics:** Controls host-level OS performance metrics to query and send as CloudWatch custom namespace statistics.
3.  **Logs:** Declares local text files to stream to CloudWatch Logs groups (e.g., system logs `/var/log/messages` or access logs `/var/log/nginx/access.log`).

### 3. Log Metric Transformations (Metric Filters)
A Metric Filter parses incoming log files in real-time. Instead of querying historical text lines to determine error counts, the metric filter checks each line against a defined pattern and increments a numeric metric instantly.
*   **Example Pattern:** `[ip, id, user, timestamp, request, status_code = 4*, size]`
*   **Application:** When Nginx writes `127.0.0.1 - - [22/Jun/2026:01:15:00 +0000] "GET /bad-uri HTTP/1.1" 404 150`, the filter reads status code `404`, matches it to the `4*` pattern, and increments the target metric by `1`. This allows immediate alerting on anomalous client traffic without running log analytic queries.

*Read more in [[Reference Notes/11-1_cloudops_monitoring_and_logging]]*

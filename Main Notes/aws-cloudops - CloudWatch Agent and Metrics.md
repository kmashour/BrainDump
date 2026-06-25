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
*   **Hypervisor Metrics (Default EC2):** Collected from the virtualization layer without host login. Includes physical disk read/write bandwidth/ops metadata, network interfaces throughput, and virtual CPU utilization. The hypervisor has no visibility inside the virtual machine's RAM tables, active swap file usage, or directory block filesystem structure.
*   **OS/Agent Metrics (Unified CloudWatch Agent):** Requires host authentication and agent execution. By reading `/proc` virtual files (such as `/proc/meminfo` and `/proc/diskstats`), the agent collects memory usage (active, available, cached), active swap activity, TCP/UDP network connections, and directory-level storage block allocation (including free inodes).

### 2. CloudWatch Unified Agent Schema & Deployment
The configuration schema `/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json` is organized into three major blocks:
1.  **Agent:** Specifies core agent runtime parameters (e.g. metrics collection intervals, credentials, custom host identifiers, or `run_as_user`).
2.  **Metrics:** Controls host-level OS performance metrics (CPU detail, memory, disk, network, processes, swap) to query and send to custom namespaces.
3.  **Logs:** Declares local text files (e.g. `/var/log/secure` or `/var/log/nginx/access.log`) to stream into CloudWatch Log groups.

Centralized configuration can be stored in **SSM Parameter Store** and applied dynamically during agent execution. The agent is started via:
```bash
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json -s
```
An IAM Instance Profile with the `CloudWatchAgentServerPolicy` must be attached to the host to allow the agent to publish metrics and create log streams.

### 3. Log Metric Transformations (Metric Filters)
A Metric Filter parses incoming log files in real-time. Instead of querying historical text lines via logs query engines (like OpenSearch or CloudWatch Logs Insights), the metric filter checks each line against a defined pattern on-the-fly and increments a numeric metric instantly.
*   **Example Pattern:** `[ip, id, user, timestamp, request, status_code = 4*, size]`
*   **Application:** When Nginx writes `127.0.0.1 - - [22/Jun/2026:01:15:00 +0000] "GET /bad-uri HTTP/1.1" 404 150`, the filter reads status code `404`, matches it to the `4*` pattern, and increments the target metric by `1`. This allows immediate alerting on anomalous client traffic.

### 4. Advanced Observability & Synthetic Checks
*   **Composite Alarms:** Combines multiple alarms using Boolean logic (`AND`, `OR`) to reduce alerting noise (e.g., only trigger alarm if CPU is high AND network throughput is low).
*   **EC2 Auto-Recovery:** Attached to system status checks. CloudWatch triggers auto-recovery to move the instance to a new physical host on failure, maintaining public/private/elastic IPs, placement groups, and metadata.
*   **CloudWatch Network Synthetic Monitor:** Executes agentless ICMP/TCP checks across Direct Connect or VPN tunnels to verify connectivity performance (packet loss, latency, jitter) between AWS and on-premises data centers.
*   **Testing Alarms:** Alerting paths can be verified manually via the AWS CLI:
    ```bash
    aws cloudwatch set-alarm-state --alarm-name "HostCPUAlarm" --state-value ALARM --state-reason "Verification Test"
    ```

*Read more in [[Reference Notes/11-1_cloudops_monitoring_and_logging]]*

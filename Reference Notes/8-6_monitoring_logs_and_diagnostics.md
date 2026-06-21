---
obsidianUIMode: preview
class: reference-note
tier: reference-note
tags:
  - linux/logging
  - linux/troubleshooting
  - linux/metrics
  - prometheus
---

# Module 8-6: Monitoring, Logs & System Diagnostics

**Breadcrumbs:** [[8-Index - Linux and OS|🏠 Linux and OS Index]] > **Diagnostics & Monitoring**

---

## 🏛️ Logging Architectures (syslog & journald)

Linux system logging is split into legacy text-based logging (`syslog`) and modern binary logging (`journald`).

### 1. The Syslog Protocol & rsyslog
`syslog` categorizes messages by **Facilities** (originating source: `auth`, `cron`, `daemon`, `kern`, `mail`) and **Severities** (importance level: `emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`).
*   **rsyslog:** The default syslog server implementation on Red Hat/Debian. It reads rules from `/etc/rsyslog.conf` and writes log strings to disk.
```bash
# Example rsyslog configuration rule:
# Log auth privilege errors to a secured auth file
authpriv.*                 /var/log/secure

# Send all logs to a remote log server over TCP port 514
*.* @@logserver.example.com:514
```

### 2. systemd journald
`journald` intercepts logs from stdout/stderr of systemd services, writing them to structured, indexed binary log files.
*   **Decoupled CLI Usage (`journalctl`):**
```bash
# Follow logs in real-time
journalctl -f

# Filter and view log entries for a specific systemd unit
journalctl -u nginx.service

# Filter by time window
journalctl --since "1 hour ago"

# Display kernel logs (similar to dmesg)
journalctl -k

# Filter by severity: Error (3) or higher
journalctl -p err..emerg
```

### 3. Log Rotation (`logrotate`)
To prevent logs from consuming entire disk partitions, `logrotate` schedules log compression and purging (configured in `/etc/logrotate.conf`).

---

## ⚙️ Resource Metrics & Performance Diagnosis

Understanding hardware bottleneck indicators is key to senior systems troubleshooting.

### CPU Load Metric Analysis
*   **Load Average (1, 5, 15 minutes):** Visible in `uptime` or `top`. Represents the average number of CPU-bound processes in the running (R) or uninterruptible sleep (D - typically waiting for disk I/O) states.
    *   *Sizing Rule:* A load average of `4.0` on a 4-core CPU indicates 100% CPU capacity utilization. Values above 4.0 indicate scheduling queues/starvation.
*   **CPU Utilization Sub-categories:**
    *   `%user`: Time spent running application binaries in User space.
    *   `%system`: Time spent running kernel-space routines (e.g., executing system calls, handling network traffic). High `%system` time indicates syscall bottlenecks.
    *   `%iowait`: Time the CPU spent idle waiting for disk or network I/O operations to complete.
    *   `%steal`: Time virtual CPUs spent waiting for physical CPU allocation from a hypervisor (hypervisor overcommitment indicator).

### Memory Metrics (Cached vs. Available)
Memory output (`free -m`) must be read correctly:
*   **Free Memory:** Physical RAM pages that are completely unallocated.
*   **Cached Memory (Page Cache):** Linux uses unused RAM to cache files read from disk. If applications require memory, the kernel evicts cache pages instantly.
*   **Available Memory:** The true indicator of available memory. Includes Free memory AND reclaimable page caches.

---

## 🛠️ Diagnostics & Troubleshooting Toolsets

Senior administrators diagnose system bottlenecks using standard core diagnostic utilities:

### 1. Process & Resource Inspection
*   `sar` (System Activity Reporter): Gathers historical CPU, memory, network, and I/O metrics.
*   `iostat -x 1`: Extended disk utilization metrics. Watch `%util` (disk utilization) and `await` (average milliseconds for I/O requests completion).
*   `iotop`: Identifies specific PIDs driving high disk read/write bandwidth.
*   `lsof -i :22`: Lists open files and active socket connections associated with specific ports or processes.
*   `ss -tulpn`: Displays active TCP/UDP sockets, PIDs, and listen states (faster replacement for `netstat`).

### 2. Low-Level Execution Tracing
*   **`strace` (System Call Tracing):** Intercepts and records all system calls executed by a process, showing arguments and return values. Crucial for debugging file access permissions, missing libraries, or lock hangs.
```bash
# Trace file opening syscalls of an active process
strace -p 12435 -e trace=open,openat

# Run a command and count system call execution frequencies
strace -c ./failing_binary
```
*   **`perf`:** Advanced kernel-level performance profiling tool. Collects call graphs and identifies CPU cycle consumption hot-spots inside kernel routines.

---

## 📈 Observability Integration (Prometheus Node Exporter)

In modern enterprise infrastructures, local metrics are scraped and centralized using Prometheus.

### Node Exporter Configuration
The Prometheus Node Exporter runs as a local daemon (or container) collecting hardware and OS metrics.
```yaml
# Prometheus configuration snippet (prometheus.yml)
scrape_configs:
  - job_name: 'linux-nodes'
    scrape_interval: 15s
    static_configs:
      - targets: ['node1.example.com:9100', 'node2.example.com:9100']
```

### Alerting Rule Configurations
Standard system health alerts configured in Prometheus:
```yaml
groups:
  - name: system_health_rules
    rules:
      - alert: CriticalDiskSpace
        expr: (node_filesystem_avail_bytes{mountpoint="/"} / node_filesystem_size_bytes{mountpoint="/"}) * 100 < 10
        for: 5m
        labels:
          severity: page
        annotations:
          summary: "Disk space critical on host {{ $labels.instance }}"
          description: "Root partition free space has dropped below 10%."
```

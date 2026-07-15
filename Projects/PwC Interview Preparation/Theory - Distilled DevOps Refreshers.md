---
obsidianUIMode: preview
class: project-note
tier: project
domains:
  - "aws"
  - "storage"
  - "networking"
  - "linux"
difficulty: intermediate
status: completed
---

# Theory: Distilled DevOps Interview Refreshers

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Projects > [[Projects/PwC Interview Preparation/Plan - DevOps Interview Roadmap|DevOps Interview Roadmap]] > **Distilled DevOps Refreshers**

---

## 1. Docker Primitives & Container Internals

To confidently explain containerization in a Senior DevOps interview, you must bypass the standard "lightweight VM" metaphor and explain the exact Linux kernel namespaces and cgroups that make containers possible.

### A. Core Linux Namespace Isolation
Containers are not physical or logical wrappers; they are standard Linux processes running with restricted views of the OS kernel. This is enforced via **namespaces**:
1.  **PID (Process ID Namespace):** Isolates the process tree. Inside the container, the main application thinks it is PID 1. On the host namespace, it runs as a standard high-numbered PID (e.g., PID 14821).
2.  **NET (Network Namespace):** Provides isolated network interfaces, IP routing tables, firewall rules, and port bindings.
3.  **MNT (Mount Namespace):** Isolates mount points. The container process cannot see host-level mounts unless explicitly shared. Container runtimes call `pivot_root` to change the root filesystem inside this namespace.
4.  **IPC (Inter-Process Communication):** Isolates message queues and shared memory segments, preventing containers from tapping host memory channels.
5.  **UTS (Unix Timesharing System):** Isolates hostname and domain name settings.
6.  **USER (User ID Namespace):** Maps root inside the container (UID 0) to a non-privileged UID on the host (e.g., UID 10001), preventing container escapes from gaining root on the host.

### B. Control Groups (cgroups) Resource Limits
While namespaces isolate *what a process can see*, cgroups restrict *how much resource a process can consume*.
*   **cgroups v1 vs v2:** cgroups v1 uses independent controller directory trees (e.g., `/sys/fs/cgroup/cpu`, `/sys/fs/cgroup/memory`), leading to synchronization conflicts. cgroups v2 introduces a single unified hierarchy, allowing safe resource limit enforcement across multiple constraints.
*   **Kubelet & Docker Drivers:** Ensure the container runtime (Docker/containerd) uses the **`systemd`** cgroup driver rather than `cgroupfs` on systems running systemd. Using mismatching drivers causes host resource accounting instabilities and node out-of-memory (OOM) evictions.

### C. The Copy-on-Write (CoW) Layer & Storage Drivers
Docker uses a layered filesystem architecture (usually `overlay2` storage driver).
*   **Lower Directories (Read-Only):** Image layers containing static files (binaries, libraries). They are immutable and shared across all container instances running that image.
*   **Upper Directory (Read-Write):** The container layer. When a container writes or modifies a file belonging to a lower layer, the kernel copy-on-write driver copies the file from the lower layer to the upper layer *before* modifying it.
*   **Volume Mounts (Bypassing Overlay2):** Standard bind mounts and Docker volumes bypass the overlay2 driver entirely. Writes bypass copy-on-write latency and are written directly to the host filesystem, providing native disk I/O performance.

### D. Multi-Stage Dockerfile Rationale (Security and Sizing)
A production-grade Dockerfile must separate the **build environment** from the **runtime environment**.
*   **Why:** Build tools (compilers, npm packages, headers) are security threats (increase vulnerability attack surface) and bloat the image size.
*   **How:** Stage 1 installs compilers, dependencies, and packages the binary. Stage 2 starts from a minimal base image (like `distroless` or `alpine`), copies *only* the compiled assets from Stage 1, and drops system shell access.
*   **Non-Root Enforcement:** Always declare a explicit non-root user (e.g., `USER appuser`) at the end of the Dockerfile. Running as root (default UID 0) means that a container breakout immediately grants root access to the underlying host kernel.

---

## 2. AWS Solutions Architecture Refresher (SAA Core)

For the PwC interview, you must articulate the "Why" behind networking, security, and computing topologies.

### A. Custom VPC Networking Topologies
A secure VPC architecture isolates internal resources from the public internet.

```
+-----------------------------------------------------------------------+
|                       Custom VPC (10.0.0.0/16)                        |
|                                                                       |
|   +---------------------------------------------------------------+   |
|   |                      Availability Zone A                      |   |
|   |                                                               |   |
|   |  +---------------------------+   +-------------------------+  |   |
|   |  |   Public Subnet (10.0.1.0)|   |  Private Subnet (10.0.2)|  |   |
|   |  |   [ Internet Gateway ]    |   |  [ NAT Gateway Endpoint]|  |   |
|   |  |   Targets public traffic  |   |  Targets internal DBs   |  |   |
|   |  +---------------------------+   +-------------------------+  |   |
|   +---------------------------------------------------------------+   |
+-----------------------------------------------------------------------+
```

1.  **Internet Gateway (IGW):** Translates internal private IPs to public IPs. Public subnets associate with a Route Table containing a default route (`0.0.0.0/0`) pointing directly to the IGW.
2.  **NAT Gateway (Network Address Translation):** Sits in the public subnet and has an Elastic IP. Private subnets associate with a Route Table directing default internet traffic (`0.0.0.0/0`) through the NAT Gateway. This allows private hosts (e.g., app servers, databases) to download patches outbound without allowing inbound internet connections.
3.  **Route Tables:** Rules dictating where traffic goes. Every subnet must associate with exactly one route table.
4.  **Network ACLs (NACLs) vs. Security Groups:**
    *   **Security Groups:** Statefull (if inbound traffic is allowed, return outbound traffic is automatically allowed). Operates at the **instance interface level**.
    *   **Network ACLs:** Stateless (you must write explicit inbound AND outbound rules, including ephemeral ports `1024-65535` for return traffic). Operates at the **subnet boundary level**.

### B. AWS Identity & Access Management (IAM)
*   **IAM User:** Represents a specific human operator or legacy machine credential. Has long-lived access keys (high leakage risk).
*   **IAM Role:** Represents an identity with temporary security credentials. Trusted entities (like EC2 instances, EKS pods via OIDC, or external AWS accounts) assume the role.
*   **IAM Policies:** JSON documents defining permissions.
    *   *Identity-Based Policy:* Attached to users or roles (e.g., "Allow this role to read S3").
    *   *Resource-Based Policy:* Attached to resources (e.g., S3 Bucket Policy allowing specific accounts).
    *   *Trust Policy:* Associated with an IAM Role defining *who* is allowed to assume it.
*   **Least Privilege:** Avoid wildcard (`*`) actions. Scope actions to specific resources (e.g., target ARN).

---

## 3. Infrastructure as Code (IaC) with Terraform

You must explain how Terraform tracks infrastructure and manages scale.

### A. Terraform State and Remote State Locking
*   **The State File (`terraform.tfstate`):** A JSON file mapping your configuration declarations to real-world cloud resources.
*   **Remote State Backend:** Storing the state file in a centralized, secure repository (like Amazon S3) rather than locally. Prevents state corruption, enables teamwork, and hides secrets.
*   **DynamoDB State Locking:** Multiple engineers or CI/CD pipelines running Terraform concurrently can cause race conditions and state corruption. Terraform secures a lock on a DynamoDB table containing a primary key `LockID`. The lock is released only after the execution plan concludes.

### B. Declarative Execution Lifecycle
1.  **`terraform init`:** Downloads providers (e.g., AWS, GCP) and initializes the remote backend.
2.  **`terraform plan`:** Computes the diff between the local configuration files, the cached state file, and the live cloud resources. It details additions (`+`), modifications (`~`), and deletions (`-`).
3.  **`terraform apply`:** Executes the API calls to make the cloud resources match the configuration. Updates the state file.
4.  **`terraform destroy`:** Tears down all resources managed by the state file.

---

## 4. Observability: Prometheus & Grafana Deep Dive

PwC projects heavily leverage observability. You must explain *how* Prometheus operates under the hood, not just how to look at Grafana dashboards.

### A. Prometheus Architecture: The Pull Model
*   **The Pull Model vs. Push Model:** Traditional monitoring (like Nagios, Datadog agents) pushes metrics to a central daemon. Prometheus **pulls (scrapes)** metrics via HTTP GET requests from target application endpoints (e.g., `http://app-ip:8000/metrics`).
    *   *Why Pull:* Pull model prevents target hosts from overloading the monitoring server. If the scraper is overloaded, it adjusts its scraping intervals. The server controls the ingestion rate.
    *   *Metrics Exposition Format:* Plain-text, line-oriented format containing metrics name, label key-value pairs, metric value, and timestamp:
        `http_requests_total{method="POST", handler="/login"} 1027 1719875412`

### B. Under the Hood: Time Series Database (TSDB)
Prometheus stores data in blocks of time (usually 2-hour blocks). Each block has:
*   **Chunks Directory:** Raw compressed time-series data.
*   **Index:** Maps metric names and labels to the chunks, enabling sub-millisecond lookups.
*   **Write-Ahead Log (WAL):** Incoming scrapes are written to the WAL first to prevent data loss in case of a crash before memory is flushed to a disk block.

### C. PromQL (Prometheus Query Language) Primitives
*   **Instant Vector:** A set of time series containing a single sample for each time series, all sharing the same timestamp (e.g., `http_requests_total`).
*   **Range Vector:** A set of time series containing a buffer of data points over a duration of time (e.g., `http_requests_total[5m]` captures all data points over the last 5 minutes). You *cannot* graph range vectors directly; you must apply a function to convert them back to instant vectors.
*   **PromQL Functions to Know:**
    *   `rate()`: Calculates the per-second average rate of increase of a counter over a range vector. Always use `rate()` on counters.
    *   `irate()`: Calculates the instant rate of increase of a counter over the last two data points of a range vector. Captures rapid spikes.
    *   `sum(rate(...)) by (handler)`: Groups rates by specific labels.
    *   `histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))`: Calculates the 95th percentile request latency. Essential for SLA tracking.

### D. Prometheus Metric Types
1.  **Counter:** A cumulative metric that only increases (or resets to 0 on restart). Used for total request count, errors.
2.  **Gauge:** A metric that can go up and down. Used for memory usage, CPU load, queue length.
3.  **Histogram:** Samples observations (e.g., request durations) and counts them in configurable buckets (`le` label). Also provides the sum and count of all observations.
4.  **Summary:** Similar to histogram, but calculates configurable quantiles (e.g., 95th, 99th) over a sliding time window client-side. Cannot be aggregated across instances (unlike Histograms).

---

## 5. DevSecOps & Security Integration

The JD emphasizes "vulnerability scanning and integrating security tools."

### A. Vulnerability Scanning: Trivy
*   **Mechanism:** Trivy scans container images, filesystems, and Git repositories for vulnerabilities (CVEs) by comparing installed package versions against public vulnerability databases.
*   **Integration:** Run Trivy in the CI pipeline after building the image, but before pushing it to ECR. Block the build (exit code 1) if High or Critical vulnerabilities are found.

### B. Static Application Security Testing (SAST): SonarQube
*   **Mechanism:** Scans raw source code without executing it (static analysis) to identify code smells, security hotspots, and bugs.
*   **Integration:** GitHub Actions runs SonarQube Scanner against pull requests, acting as a gateway (Quality Gate) preventing merge if code coverage is too low or vulnerabilities exist.

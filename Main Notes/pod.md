---
obsidianUIMode: preview
class: landing-note
tier: main-note
domains:
  - "kubernetes"
role: workload
related_concepts:
  - "[[node]]"
  - "[[container-runtime]]"
  - "[[kube-scheduler]]"
reference_guides:
  - "[[Reference Notes/0-5_containers_runtimes_and_lifecycle.md]]"
  - "[[Reference Notes/0-6_kubernetes_workloads_and_controllers.md]]"
  - "[[Reference Notes/0-12_kubernetes_api_management_and_pod_immutability.md]]"
tags:
  - kubernetes/workload
  - status/completed
against: []

---

# pod

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Workloads & Infrastructure > **pod**

---

## 🎯 Purpose (Why it is used)
The `Pod` is the smallest, most basic deployable object in Kubernetes. It represents a logical host for one or more tightly coupled containers that share the same network namespace, storage volumes, and scheduling context, facilitating application co-location and local communication.

---

## ⚙️ Functionality (What it is doing)
1. **Logical Hosting:** Wraps application containers and storage definitions into a single operational unit.
2. **Network Sharing:** Assigns a single IP address to the Pod. All containers inside the Pod share this IP and port space, enabling them to communicate via `localhost`.
3. **Volume Sharing:** Mounts shared storage directories into multiple containers simultaneously for collaborative read/write operations.
4. **Lifecycle Management:** Coordinates startup order (via Init containers), manages health checks (via probes), runs start/stop actions (via hooks), and executes graceful termination sequences.
5. **Security Enclosure:** Enforces security profiles, service account identities, and scheduling constraints at the Pod boundary.

---

## 🏛️ Architectural Context (How it fits in the architecture)
The Pod is the building block of all workloads in the cluster:
* **The Scheduling Target:** The `kube-scheduler` assigns the Pod to a Node by updating its metadata in the API Server.
* **The Kubelet's Directive:** The `kubelet` parses the PodSpec and calls the local Container Runtime (CRI) to spin up the required containers.
* **Managed Objects:** In production, Pods are rarely created directly. They are created and managed by higher-level controllers (like `Deployments`, `StatefulSets`, or `DaemonSets`) which handle replica scaling, rollouts, and self-healing.

---

## 🧩 Problem Solver (What problem it solves)
* **Co-Location and Helper Patterns:** Solves the problem of running helper processes (e.g., logging sidecars, proxy agents, database sync adapters) alongside primary applications by ensuring they are scheduled on the exact same host node and can access the same files and network loop.
* **Dynamic IP Allocation:** Dynamically provisions a unique IP for each Pod in the cluster, removing port-allocation conflicts between containers on the same physical host.
* **Host User Isolation:** Solves container-escape vulnerabilities by mapping container user IDs to unprivileged host user IDs (using `spec.hostUsers: false`), ensuring that a root user inside the container does not carry root privileges on the host node.

---

## 🟢 Operational Impact (What will happen with it operating)
* **Workload Execution:** Application containers run with full network and storage integration.
* **Component Coordination:** Sidecars and main processes coordinate work seamlessly through shared filesystems or local ports.
* **Automatic Scaling:** Deployment controllers can scale the application up or down by spawning or terminating Pod instances.

---

## 🔴 Failure Impact (What will happen without it)
* **No Workloads:** The cluster cannot host or schedule any applications.
* **Loss of Orchestration:** Containers must be run manually as individual host processes or raw Docker containers, losing all automatic scheduling, scaling, and self-healing benefits.
* **Resource Leakage:** Without Pod-level cleanups, terminated containers, orphaned volumes, and stale network routes accumulate on the host OS.
* **Broken Helper Relationships:** Helper containers cannot easily share the same network address space or file systems with primary containers, breaking standard architectural patterns (like sidecar proxies).
---

---

This note covers Pod phases, QoS classes, health probing configurations, container initialization styles (including native sidecars), and lifecycle hooks.

---

## 🚦 1. Pod Phases & Lifecycle States
A Pod transitions through these phases during its life:
* **`Pending`:** The Pod has been accepted by the API Server, but the scheduler is still finding a node, or the container runtime is pulling the required images.
* **`Running`:** The Pod has been bound to a node, and at least one container is running or in the process of starting.
* **`Succeeded`:** All containers in the Pod have terminated successfully (exit code 0) and will not be restarted (e.g., completed Job).
* **`Failed`:** All containers have terminated, and at least one container terminated in failure (non-zero exit code).
* **`Unknown`:** The API Server cannot obtain the Pod's status, usually because the Kubelet on the host node has lost communication with the Control Plane.

---

## 💎 2. Quality of Service (QoS) Classes
The Kubelet classifies Pods into three QoS classes based on their resource requests and limits. This determines eviction priority during node resource exhaustion:

### A. Guaranteed
* **Rule:** Every container in the Pod must have both CPU and Memory limits and requests defined, and they must be exactly equal (`request == limit`).
* **Priority:** Highest. Evicted last.

### B. Burstable
* **Rule:** At least one container in the Pod has a request defined that is less than its limit, or they do not match.
* **Priority:** Medium. Evicted if Guaranteed pods need the resources.

### C. BestEffort
* **Rule:** No requests or limits are defined for any container.
* **Priority:** Lowest. Evicted first if the node experiences Memory or Disk pressure.

---

## 🩺 3. Health Probes
The Kubelet performs three types of diagnostic probes on running containers:
1. **Startup Probe:** Checks if the application inside the container has started. All other probes (liveness, readiness) are disabled until this succeeds. Used for slow-starting applications.
2. **Liveness Probe:** Checks if the container needs to be restarted. If it fails, the Kubelet kills the container and initiates its restart policy.
3. **Readiness Probe:** Checks if the container is ready to accept incoming network traffic. If it fails, the endpoints controller removes the Pod's IP from all matching Services.

*Configuration methods:* HTTP GET, TCP Socket, gRPC, or Exec commands.

---

## 🏗️ 4. Advanced Container Types

### A. Init Containers
* Run sequentially to completion before any application containers start.
* If an Init container fails, the Kubelet restarts the Pod until it succeeds (unless restartPolicy is Never).
* Used to fetch configs, check database dependencies, or perform migrations.

### B. Native Sidecars (v1.29+)
* Defined as Init containers but configured with `restartPolicy: Always`.
* **Execution:** Starts sequentially before app containers, but the Kubelet does not wait for it to exit; it keeps running for the entire life of the Pod.
* Ideal for sidecar proxies (like Linkerd/Istio) and log shippers.

### C. Ephemeral Containers
* Injected into an active, running Pod using the `/ephemeralcontainers` API subresource.
* Bypasses the pod immutability rule, enabling troubleshooting using `kubectl debug -it my-pod --image=busybox`.

---

## 🪝 5. Container Lifecycle Hooks
Triggered at specific points in a container's lifecycle:
* **`PostStart`:** Executes immediately after a container is created. Note: It runs asynchronously with the container's entrypoint; there is no guarantee it runs before the entrypoint.
* **`PreStop`:** Blocks container shutdown. Called immediately before a container is terminated due to an API request, liveness probe failure, or resource eviction. Useful for initiating graceful shutdowns or saving state.

*Read more in [0-3_node_mechanics_and_resource_limits.md](../Reference%20Notes/0-3_node_mechanics_and_resource_limits.md#4-quality-of-service-qos-classes), [0-4_workload_lifecycle_and_healing.md](../Reference%20Notes/0-4_workload_lifecycle_and_healing.md#2-garbage-collection-gc), and [0-5_containers_runtimes_and_lifecycle.md](../Reference%20Notes/0-5_containers_runtimes_and_lifecycle.md#6-container-lifecycle-hooks).*

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **pod**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

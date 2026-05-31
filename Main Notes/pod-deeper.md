---
tags:
  - concept/pod
  - type/deeper-dive
related:
  - [[pod]]
---

# pod deeper

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

*Read more in [03_node_mechanics_and_resource_limits.md](../Reference%20Notes/03_node_mechanics_and_resource_limits.md#4-quality-of-service-qos-classes), [04_workload_lifecycle_and_healing.md](../Reference%20Notes/04_workload_lifecycle_and_healing.md#2-garbage-collection-gc), and [05_containers_runtimes_and_lifecycle.md](../Reference%20Notes/05_containers_runtimes_and_lifecycle.md#6-container-lifecycle-hooks).*

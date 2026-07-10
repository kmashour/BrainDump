---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[pod-deeper]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/workloads/pods/init-containers/"
author: "Kubernetes Authors"
course_title: "CKA Exam Prep"
against: []
tags:
  - kubernetes/pod
  - container/sidecar
---

# pod - Init and Sidecar Containers

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[pod]] > [[pod-deeper]] > **Init and Sidecar Containers**

---

## 📑 Init and Sidecar Containers

Kubernetes supports sequential initialization tasks and native helper processes through specialized container lifecycles.

### 1. Init Containers
Init containers run sequentially to completion before any application containers start. If an init container fails, the Kubelet restarts it until it succeeds (unless the Pod `restartPolicy` is `Never`).

### 2. Multi-Container Pod Patterns (Sidecar, Adapter, Ambassador)
Tightly coupled container processes can share a Pod sandbox. Three primary design patterns exist for multi-container architectures:
*   **Sidecar Pattern:** Extends or enhances the main application container. For example, a log shipper (e.g. Filebeat) that mounts a shared `emptyDir` volume to tail logs written by the main application, or a service mesh proxy (e.g. Envoy) managing ingress/egress.
    *   *Sidecar Logging Sub-Patterns:*
        1.  **Streaming Sidecar (Log Transporter):** Tails a local log file written by the main application to the shared `emptyDir` volume and redirects it to the sidecar's `stdout`. This integrates directly with the node's **DaemonSet Logging Agent (e.g., Promtail, Fluent Bit)** which collects host `/var/log/pods/` logs.
        2.  **Log Exporting Sidecar (Log Shipper):** Runs a lightweight log agent inside the sidecar that reads the log file and directly ships it over the network to a central log server (e.g., Loki, Elasticsearch), bypassing the DaemonSet and node-level container logs.
        *See detailed architecture comparison and ready-to-run YAML manifest in [[Reference Notes/0-13_scheduling_logging_and_lifecycle.md#Synergy: How Sidecars and DaemonSet Logging Agents Work Together|Module 13 Reference Note > Logging Sidecar Patterns]].*
*   **Adapter Pattern:** Normalizes and formats the application output or telemetry before exposing it externally. For example, a metrics exporter that scrapes custom application output, converts it into Prometheus format, and serves it to a central metrics collector.
*   **Ambassador Pattern:** Serves as a local proxy for the application's outgoing connections to external systems. For example, the application queries database services on `localhost:3306`, while the ambassador container handles request routing, service discovery, and database connection security dynamically.

### 3. Native Sidecar Containers (restartPolicy: Always)
Introduced as a native feature, sidecar containers run alongside main application containers but start *before* them and stop *after* them.
* **Definition:** Configured in `spec.initContainers` but defined with `restartPolicy: Always`.
* **Execution:** Starts and blocks subsequent init container execution until its startup/readiness probe succeeds.


### 4. Resource Scheduling Math
* **Standard Init:** The Pod request/limit is calculated as the `Max(sum of app containers, highest init container)`.
* **Native Sidecar:** Because sidecar containers run concurrently with app containers, the pod scheduling calculation is modified:
  $$\text{Pod Request} = \text{Sum(App Containers)} + \text{Sum(Active Sidecars)}$$
  This sum is compared against the standard sequential init container values to select the absolute maximum.

*Read more in [0-6_kubernetes_workloads_and_controllers.md](../Reference%20Notes/0-6_kubernetes_workloads_and_controllers.md#3-init-containers-and-native-sidecars)*

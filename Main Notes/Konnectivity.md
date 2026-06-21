---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: control-plane
domains:
  - "kubernetes"
related_concepts:
  - "[[kube-apiserver]]"
  - "[[admission-controller]]"
against:
  - "[[kube-proxy]]" # Konnectivity is for control plane-to-node egress, kube-proxy is for pod-to-service routing
reference_guides:
  - "[[Reference Notes/0-2_cluster_architecture_and_components.md]]"
tags:
  - kubernetes/component
  - status/completed
---

# Konnectivity

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Control Plane > **Konnectivity**

---

## 🎯 Purpose (Why it is used)
**Konnectivity** (often packaged as `apiserver-network-proxy`) is a network proxy designed to bridge network splits between the Kubernetes control plane and the worker nodes. In firewalled, air-gapped, or highly secure cloud subnet configurations where control plane nodes cannot directly route TCP packets to worker nodes, Konnectivity enables the API Server to safely execute egress operations (such as fetching logs, proxying ports, or triggering webhooks) inside the cluster.

---

## ⚙️ Functionality (What it is doing)
*   **Reverse-Tunnel Establishment:** Leverages an outbound-initiated agent pattern where worker node agents dial the control plane server, creating secure, bidirectional tunnels.
*   **API Server Traffic Routing:** Proxies interactive operations like `kubectl logs`, `kubectl exec`, and `kubectl port-forward` through Unix domain sockets.
*   **Admission Webhook Delivery:** Routes webhook validation and mutation HTTP payloads back into the cluster to meet API machinery requirements.
*   **Aggregated API Server Routing:** Connects the core API server to custom extension API servers running as workloads.

---

## 🏛️ Architectural Context (How it fits in the architecture)
*   **Kube-APIServer:** Configured with an `EgressSelectorConfiguration` listing socket targets to delegate network dials to the proxy.
*   **Konnectivity Server:** Runs as a control plane daemon listening on Port `8132` for Agent registration and exposes a Unix socket for the API Server.
*   **Konnectivity Agent:** Runs as a deployment/daemonset workload in the cluster, dialing the control plane on startup to register.

---

## 🧩 Problem Solver (What problem it solves)
Without Konnectivity, clusters in split-network topologies (like private GKE clusters or multi-subnet VPCs) are unable to retrieve logs, execute shell commands in pods, or route admission webhooks, since the control plane cannot initiate TCP routes to private worker node IPs. Konnectivity eliminates direct routing requirements by shifting tunnel initiation to the worker nodes.

---

## 🟢 Operational Impact (What will happen with it operating)
*   **Secure Isolation:** The control plane network remains strictly private, accepting only inbound agent connections over mTLS.
*   **Strict Access Control:** Limits confused deputy routing security bugs by explicitly filtering API egress destinations.
*   **Standard Interface:** Integrates seamlessly behind standard kubectl endpoints without user-facing configurations.

---

## 🔴 Failure Impact (What will happen without it)
*   **Broken Operations:** Command errors when executing `kubectl logs`, `exec`, or `port-forward` ("error: print logs: dial tcp... connection refused").
*   **Admission Webhook Deadlock:** The cluster may experience complete deployment deadlocks if an admission webhook checks all namespaces but Konnectivity agents fail to launch.
*   **Broken Extensions:** Metrics server and custom metrics APIs fail to report telemetry due to unroutable aggregated endpoints.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Konnectivity**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

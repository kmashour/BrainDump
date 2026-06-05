---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: network
domains:
  - "kubernetes"
  - "networking"
related_concepts:
  - "[[pod]]"
  - "[[ingress]]"
against:
  - "[[kube-proxy]]"
reference_guides:
  - "[[Reference Notes/10_networking_dns_and_ingress.md]]"
tags:
  - kubernetes/network
  - status/completed
---

# service

**Breadcrumbs:** [[Index|🏠 Index]] > Workloads & Infrastructure > **service**

---

## 🎯 Purpose (Why it is used)
A `Service` provides an abstract way to expose an application running on a set of Pods as a network service. Since Pods are ephemeral and receive randomized IPs on restart, the Service acts as a static gateway to reach them.

---

## ⚙️ Functionality (What it is doing)
* **Static IP and DNS allocation:** Provides a stable Virtual IP (ClusterIP) and a corresponding CoreDNS record.
* **Traffic Load Balancing:** Distributes incoming traffic across pods matching the service selector labels.
* **Exposure Modes:**
  - `ClusterIP`: Exposes the service internally inside the cluster.
  - `NodePort`: Exposes the service on a static port (`30000–32767`) across all cluster node IPs.
  - `LoadBalancer`: Provisions an external cloud load balancer (e.g. AWS ELB) routing to the NodePort.
  - `ExternalName`: Maps the service to a DNS name instead of a selector.

---

## 🏛️ Architectural Context (How it fits in the architecture)
* **Endpoint Controller:** Sits above Pods. The `endpoints-controller` in the controller manager updates `Endpoints` (or `EndpointSlices`) lists matching the service selector.
* **Routing Agent:** `kube-proxy` monitors Services and Endpoints on every node, programming `iptables` or `IPVS` load balancing tables to redirect traffic to pod IPs.

---

## 🧩 Problem Solver (What problem it solves)
* **Pod IP Volatility:** Solves client connection breaks. When backend pods are upgraded or crash, clients query the static Service address instead of tracking changing pod IPs.
* **Internal Load Balancing:** Distributes frontend web traffic uniformly to multiple backend API pods.

---

## 🟢 Operational Impact (What will happen with it operating)
* Applications communicate reliably inside the cluster using stable DNS names (e.g. `http://auth-service`).
* External clients connect to workloads securely through NodePorts or cloud load balancers.

---

## 🔴 Failure Impact (What will happen without it)
* Inter-pod communication is highly unstable; services must query the API server constantly to discover peer pod IPs.
* External load-balancing and exposure capabilities are lost.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **service**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[service]]
SORT file.name ASC
```

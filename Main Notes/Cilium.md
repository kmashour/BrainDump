---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: network
domains:
  - "kubernetes"
  - "networking"
  - "security"
related_concepts:
  - "[[cni]]"
  - "[[networkpolicy]]"
against:
  - "[[flannel]]"
  - "[[calico]]"
reference_guides:
  - "[[Reference Notes/0-7-3_network_policies_and_traffic_segregation.md]]"
tags:
  - kubernetes/networking
  - kubernetes/security
  - kubernetes/cks
  - status/completed
---

# Cilium

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Networking > **Cilium**

---

## 🎯 Purpose (Why it is used)
Cilium is an open-source, cloud-native networking, observability, and security engine designed to provide high-performance network routing, transparent encryption, and Layer-7 policy enforcement using Linux **eBPF (extended Berkeley Packet Filter)**.

---

## ⚙️ Functionality (What it is doing)
* **eBPF In-Kernel Packet Forwarding:** Replaces `kube-proxy` by injecting eBPF bytecode directly into the Linux socket layer, bypassing `iptables` and connection tracking overhead.
* **Identity-Based Security:** Assigns cryptographic numeric identities to endpoints, enforcing security policies at the socket layer without IP-based rule explosion.
* **Transparent Wire Encryption:** Encrypts node-to-node and pod-to-pod traffic automatically using WireGuard or IPsec without sidecar proxies.
* **L7 Application-Aware Policies:** Inspects and filters HTTP verbs, REST endpoints, gRPC calls, and DNS queries via `CiliumNetworkPolicy`.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Cilium runs as a DaemonSet (`cilium-agent`) on every Kubernetes node, compiling eBPF programs on-the-fly and loading them into Linux kernel hooks (`tc`, `cgroups`, `sock_ops`).

---

## 🧩 Problem Solver (What problem it solves)
Standard Kubernetes networking relies on `iptables` packet traversal, which degrades dramatically in latency and CPU consumption when clusters scale to thousands of services. Cilium eliminates this bottleneck while simultaneously providing deep Layer-7 network security and encryption.

---

## 🟢 Operational Impact (What will happen with it operating)
Network throughput increases, CPU consumption drops significantly, and security teams gain real-time visibility into DNS queries, HTTP API paths, and microservice traffic via Hubble.

---

## 🔴 Failure Impact (What will happen without it)
Large-scale clusters experience network latency spikes under `iptables` lock contention, lack granular L7 traffic filtering, and require complex service mesh sidecar proxies to achieve pod-to-pod encryption.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Cilium**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[Cilium]]
SORT file.name ASC
```

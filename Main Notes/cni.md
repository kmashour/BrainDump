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
  - "[[node]]"
  - "[[networkpolicy]]"
against:
  - "[[kube-proxy]]"
reference_guides:
  - "[[Reference Notes/0-9_networking_dns_and_ingress.md]]"
tags:
  - kubernetes/component
  - status/completed
---

# Container Network Interface (CNI)

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Networking > **Container Network Interface (CNI)**

---

## 🎯 Purpose (Why it is used)
The Container Network Interface (CNI) consists of a specification and libraries that define how container runtimes should configure network namespaces for containers. It provides a standardized interface for pluggable network providers to integrate directly with Kubernetes.

---

## ⚙️ Functionality (What it is doing)
- Configures network interfaces inside pod network namespaces (creation and deletion of veth pairs).
- Assigns IP addresses to pods (IP Address Management - IPAM).
- Implements network traffic routing between pods across different cluster nodes.
- Enforces Kubernetes NetworkPolicies (where supported, e.g., Calico, Cilium).

---

## 🏛️ Architectural Context (How it fits in the architecture)
The Kubelet on each worker node calls CNI plugins locally when scheduling or destroying a Pod. It looks for binaries in `/opt/cni/bin/` and JSON configuration files in `/etc/cni/net.d/`.

---

## 🧩 Problem Solver (What problem it solves)
- **Without CNI:** Kubernetes container runtimes would have to hardcode configuration for every type of network infrastructure (bridges, overlays, cloud subnets), and network administrators would have to manually configure host routing and IP addresses for every container.
- **With CNI:** The Kubelet delegates all network configuration to pluggable CNI daemons, allowing the same Kubernetes deployment to run on underlay routing (BGP), overlay networks (VXLAN), or public cloud networks (AWS VPC CNI) without changing the core codebase.

---

## 🟢 Operational Impact (What will happen with it operating)
Pods receive unique, cluster-wide IP addresses. They can communicate with all other pods across the cluster without NAT, ensuring a flat network topology.

---

## 🔴 Failure Impact (What will happen without it)
If CNI is misconfigured or its daemon (e.g. Calico pod) fails, the node status changes to `NotReady` with the condition `NetworkUnavailable=True`. New pods scheduled to the node will remain stuck in `ContainerCreating` or `Pending` status.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **CNI**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
FROM "Main Notes"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

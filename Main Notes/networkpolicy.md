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
  - "[[service]]"
against:
  - "[[firewalld]]"
  - "[[iptables]]"
reference_guides:
  - "[[Reference Notes/08_security_and_network_policies.md]]"
tags:
  - kubernetes/network
  - status/completed
---

# networkpolicy

**Breadcrumbs:** [[Index|🏠 Index]] > Workloads & Infrastructure > **networkpolicy**

---

## 🎯 Purpose (Why it is used)
A `NetworkPolicy` configures L3/L4 firewall rules for Pods in a Kubernetes cluster. By default, all pod network traffic is non-isolated (any pod can talk to any other pod). A NetworkPolicy enables host-level isolation, enforcing a Zero-Trust security model.

---

## ⚙️ Functionality (What it is doing)
* **Traffic Isolation:** Restricts inbound (`Ingress`) and outbound (`Egress`) traffic for targeted pods.
* **Flexible Selectors:** Evaluates connection rights using combinations of:
  - `podSelector`: Matches pods within the same namespace.
  - `namespaceSelector`: Matches entire namespaces based on labels.
  - `ipBlock`: Restricts traffic by CIDR blocks (useful for external IP traffic).
* **Port Filtering:** Limits traffic to specific TCP/UDP ports.

---

## 🏛️ Architectural Context (How it fits in the architecture)
* **CNI Dependency:** NetworkPolicies are declarations only. They are enforced by the cluster's CNI network plugin (e.g. Calico, Cilium, Weave). If the CNI plugin (like Flannel) does not support network policies, the manifests are accepted by the API but ignored at the runtime layer.
* **Enforcement Point:** The CNI daemon on each worker node translates policies into host-level firewall rules (e.g. `iptables` rules or eBPF programs).

---

## 🧩 Problem Solver (What problem it solves)
* **East-West Traffic Security:** Solves the risk of lateral movement. If a public-facing web pod is compromised, NetworkPolicies prevent the attacker from connecting directly to a database pod unless explicitly allowed.
* **Egress Data Exfiltration:** Solves exfiltration by restricting outbound egress paths to specific external domains or internal services.

---

## 🟢 Operational Impact (What will happen with it operating)
* targeted pods reject all traffic unless it matches a whitelist rule.
* App-to-app routing is restricted according to service dependencies.

---

## 🔴 Failure Impact (What will happen without it)
* The cluster runs in "open mesh" mode, where any container (even a compromised web container) can query databases, control planes, or sibling services across namespaces.
* Compliance audits fail (e.g., PCI-DSS, SOC2) due to lack of network isolation.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **networkpolicy**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[networkpolicy]]
SORT file.name ASC
```

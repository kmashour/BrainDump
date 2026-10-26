---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: security
domains:
  - kubernetes
related_concepts:
  - "[[Kubernetes Attack Surface and the 4Cs of Cloud Native Security]]"
  - "[[Kubernetes Cluster Component Hardening and Communication Security]]"
against: []
reference_guides:
  - "[[Reference Notes/0-7-3_network_policies_and_traffic_segregation.md]]"
tags:
  - kubernetes/security
  - kubernetes/networking
  - kubernetes/network-policy
  - kubernetes/cks
  - status/completed
---

# Kubernetes Network Security and Traffic Segregation

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Security > **Kubernetes Network Security and Traffic Segregation**

---

## 🎯 Purpose (Why it is used)
By default, the Kubernetes Container Network Interface (CNI) specification enforces an open, non-hierarchical, flat network overlay. Any Pod running inside the cluster can route packets to any other Pod across all nodes and namespaces without perimeter barriers. In multi-tenant, zero-trust, or PCI-DSS/HIPAA-compliant environments, this open model represents an unacceptable lateral movement risk. **Kubernetes NetworkPolicies** provide declarative, layer-3 and layer-4 firewall specifications to isolate workloads, enforce microsegmentation, and establish least-privilege network perimeters.

---

## ⚙️ Functionality (What it is doing)
NetworkPolicies operate at the packet filtering layer:

1. **Declarative State Definition:** NetworkPolicy API resources define which Pods are selected (`podSelector`), what traffic types are governed (`policyTypes: [Ingress, Egress]`), and what sources/destinations/ports are allowed.
2. **CNI Kernel Compilation:** The API Server does not filter network packets. Instead, CNI daemon agents (e.g. Calico, Cilium, Kube-router) watch NetworkPolicy resources and translate them into low-level Linux kernel filters (`iptables`, `ipset`, or eBPF programs) on the host nodes where selected Pods reside.
3. **Additive Whitelisting:** Once a Pod is selected by at least one policy, it transitions from a default-allow state into an isolated state, dropping all non-whitelisted traffic.

```
+---------------------------------------------------------------------------------+
|                       KUBERNETES CNI OVERLAY NETWORK                            |
|                                                                                 |
|   +--------------------------+                      +-----------------------+   |
|   |  Public Frontend Pod     | ────(Blocked)──────► |  Database / Pay Pod   |   |
|   |  Namespace: default      |                      |  Namespace: isolated  |   |
|   +--------------------------+                      +-----------------------+   |
|                                                              ▲                  |
|                                                              │                  |
|   +--------------------------+                               │ Allowed (Port    |
|   |  Authorized Service Pod  | ──────────────────────────────┘ 8080 TCP Only)   |
|   |  Label: access=allowed   |                                                  |
|   +--------------------------+                                                  |
+---------------------------------------------------------------------------------+
```

---

## 🏛️ Architectural Context (How it fits in the architecture)
This domain operates directly at Layer 2 (**Cluster**) of the 4Cs Security Model:
* It eliminates cross-namespace lateral movement when a single workload at the Container or Code tier is compromised.
* It works in conjunction with service mesh layers (e.g., Istio mTLS) by acting as the foundational Layer 3/4 packet gate before application Layer 7 authorization occurs.
* It bridges cloud security group boundaries with in-cluster microsegmentation, restricting pod egress to external cloud services or metadata endpoints (`169.254.169.254`).

---

## 🧩 Problem Solver (What problem it solves)
* **Unrestricted Lateral Movement:** Prevents an attacker who gains remote code execution (RCE) in a public-facing container from executing network reconnaissance or database exfiltration against backend microservices.
* **Accidental Cross-Tenant Leaks:** Guarantees that staging, production, and tenant workloads residing on shared compute nodes cannot inadvertently connect to one another.
* **Malicious Pod-to-Pod Eavesdropping:** Restricts communication paths strictly to documented microservice dependency graphs.

---

## 🟢 Operational Impact (What will happen with it operating)
* **Default-Deny Zero Trust:** Workloads are isolated by default; communication requires explicit administrative whitelisting.
* **Kernel-Enforced Performance:** Traffic filtering executes at the kernel/eBPF level, incurring minimal CPU overhead compared to application-layer proxies.
* **Strict Port Segregation:** Microservices only expose their required operational ports (e.g., TCP 8080), blocking all other ports and protocols.

---

## 🔴 Failure Impact (What will happen without it)
* **Flat Attack Surface Exploitation:** A breach in an unhardened edge container allows immediate lateral traversal to internal management ports, unprotected Redis caches, and database backends.
* **Data Exfiltration:** Workloads with unmanaged egress can beacon out to external command-and-control (C2) servers or exfiltrate customer databases to malicious public endpoints.

---

## 🔍 Deeper Dive Notes
* [[Main Notes/Kubernetes Network Policies - Default Deny Ingress, Multi-Tenant Whitelisting, and Selector Logic|Layer 3/4: NetworkPolicies, Default Deny, and Selector Logic]]
* [[Main Notes/Kubernetes Ingress Security - TLS Termination, Force-HTTPS, and Controller Annotations|Layer 7: Ingress Security, TLS Termination, Force-HTTPS & Controller Annotations]]
* [[Main Notes/Kubernetes Service Mesh Security - Istio mTLS, PeerAuthentication CRDs, and Sidecar Injection|Service Mesh: Istio mTLS, PeerAuthentication CRDs & Sidecar Injection]]

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

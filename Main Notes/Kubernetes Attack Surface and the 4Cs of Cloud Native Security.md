---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: security
domains:
  - kubernetes
related_concepts:
  - "[[Kubernetes Pod Security and Policy Engines]]"
against: []
reference_guides:
  - "[[Reference Notes/0-7-0_attack_surface_and_threat_modeling.md]]"
tags:
  - kubernetes/security
  - kubernetes/cks
  - kubernetes/threat-model
  - status/completed
---

# Kubernetes Attack Surface and the 4Cs of Cloud Native Security

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Security > **Kubernetes Attack Surface and the 4Cs of Cloud Native Security**

---

## 🎯 Purpose (Why it is used)
Modern containerized applications running on Kubernetes operate across multiple distinct infrastructure layers, from the physical hardware and cloud provider hypervisors up to application runtime code. Securing a Kubernetes cluster cannot be accomplished solely at the container or Kubernetes object level. The **4Cs of Cloud Native Security** (*Cloud, Cluster, Container, Code*) provides a concentric, hierarchical defense-in-depth framework designed to analyze attack vectors, eliminate single points of failure, and prevent single-layer compromises from escalating into full infrastructure takeover.

---

## ⚙️ Functionality (What it is doing)
The 4Cs model categorizes every security boundary, threat vector, and defense mechanism into four concentric rings:

```
+-------------------------------------------------------------+
| ☁️  CLOUD     (AWS/GCP/Bare-Metal, IAM, VPCs, Firewalls)    |
|   +-------------------------------------------------------+ |
|   | ☸️  CLUSTER   (API Server, etcd, Kubelet, RBAC, CNI)   | |
|   |   +-------------------------------------------------+ | |
|   |   | 📦  CONTAINER (Base images, Capabilities, seccomp)| | |
|   |   |   +-------------------------------------------+ | | |
|   |   |   | 💻  CODE      (App vulnerabilities, TLS)  | | | |
|   |   |   +-------------------------------------------+ | | |
|   |   +-------------------------------------------------+ | |
|   +-------------------------------------------------------+ |
+-------------------------------------------------------------+
```

1. **Cloud (The Foundation):** Secures the physical/virtual compute instances, Virtual Private Clouds (VPCs), subnets, cloud IAM roles, and Instance Metadata Services (IMDS).
2. **Cluster (The Orchestrator):** Secures communication between Kubernetes control plane components (`kube-apiserver`, `etcd`, `kube-scheduler`, `kube-controller-manager`), worker node agents (`kubelet`), pod network overlays (CNI), authentication/authorization (RBAC), and admission control.
3. **Container (The Isolation Layer):** Secures container images, container runtimes (CRI/containerd), Linux namespaces, cgroups, process capabilities (`drop: ["ALL"]`), seccomp syscall filters, and filesystem immutability (`readOnlyRootFilesystem: true`).
4. **Code (The Workload):** Secures application-level code, third-party libraries, API endpoints, mutual TLS encryption, and secure coding practices preventing Remote Code Execution (RCE) and Server-Side Request Forgery (SSRF).

---

## 🏛️ Architectural Context (How it fits in the architecture)
The fundamental axiom of the 4Cs model is **asymmetric encapsulation**:
* **Outer layers encapsulate and isolate inner layers.**
* **Inner layers cannot defend against or mitigate a compromised outer layer.**
* If the **Cloud** layer is breached (e.g., an overly permissive AWS IAM node instance profile), the attacker accesses cloud APIs directly, rendering all Cluster, Container, and Code hardening obsolete.
* Conversely, when outer layers are rigorously hardened with default-deny postures, a catastrophic vulnerability in the inner layer (**Code**) remains confined to an isolated sandbox.

---

## 🧩 Problem Solver (What problem it solves)
Traditional security architectures relied on "hard perimeter, soft interior" models (defending only the network edge). In microservices and Kubernetes, this model fails completely:
* An attacker compromising one web pod can laterally pivot across flat pod networks to attack internal databases.
* Pods inheriting default cluster settings can query the cloud metadata service to steal cloud administrative tokens.
* Attackers possessing pod execution can mount host root directories (`/`) via unrestricted `hostPath` volumes, instantly escalating from an unprivileged pod to root access on the physical host.

The 4Cs model solves this by establishing **Defense-in-Depth**: each ring acts as an autonomous security gateway assuming the layer inside it has already been breached (*Zero Trust Architecture*).

---

## 🟢 Operational Impact (What will happen with it operating)
When the 4Cs model is fully enforced:
* **Blast Radius Containment:** A zero-day RCE vulnerability in an application container cannot access the node, pivot across the network, or reach external cloud resources.
* **Least Privilege Enforcement:** Pods run as non-root UIDs, with read-only filesystems, dropping all Linux capabilities, and with ServiceAccount token auto-mounting disabled.
* **Continuous Auditing:** Security events at each tier are recorded by API Server audit logs, network flow logs, and eBPF kernel event probes (Falco).

---

## 🔴 Failure Impact (What will happen without it)
Without concentric multi-layer security:
* **Cascading Infrastructure Takeover:** A simple web application injection bug triggers a chain reaction: Code RCE -> Steal default ServiceAccount token -> Abuse wildcard RBAC permissions -> Deploy privileged pod with `hostPath: /` -> Compromise Node OS -> Extract plaintext secrets from etcd.
* **Cloud Infrastructure Theft:** A pod abuses unblocked egress to query `169.254.169.254` (IMDSv1), exfiltrating IAM credentials with permissions to delete or ransom cloud databases and compute fleets.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, exploit breakdowns, and practical attack chains associated with **Kubernetes Attack Surface and the 4Cs of Cloud Native Security**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

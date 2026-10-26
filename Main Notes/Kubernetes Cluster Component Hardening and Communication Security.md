---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: security
domains:
  - kubernetes
related_concepts:
  - "[[Kubernetes Attack Surface and the 4Cs of Cloud Native Security]]"
  - "[[Kubernetes Pod Security and Policy Engines]]"
  - "[[Linux Operating System Architecture and Kernel Mechanics]]"
against: []
reference_guides:
  - "[[Reference Notes/0-7-8_cluster_hardening_cis_benchmarks_and_upgrades.md]]"
  - "[[Reference Notes/0-7-1_rbac_service_accounts_and_certificates.md]]"
tags:
  - kubernetes/security
  - kubernetes/cluster-hardening
  - kubernetes/cks
  - status/completed
---

# Kubernetes Cluster Component Hardening and Communication Security

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Security > **Kubernetes Cluster Component Hardening and Communication Security**

---

## 🎯 Purpose (Why it is used)
A Kubernetes cluster operates as a distributed system where the control plane components (`kube-apiserver`, `etcd`, `kube-controller-manager`, `kube-scheduler`) and worker node agents (`kubelet`) communicate across network boundaries. Default out-of-the-box configurations in standard deployments often prioritize zero-friction bootstrapping over zero-trust security—leaving daemon ports exposed to unauthenticated probes, cleartext fallbacks, or unvalidated client certificates. Hardening cluster components establishes cryptographic boundaries and strict authentication/authorization gates at every inter-component hop.

---

## ⚙️ Functionality (What it is doing)
Cluster component hardening enforces three non-negotiable security postures:

1. **Cryptographic Identity & Mutual TLS (mTLS):** Enforcing bidirectional identity validation between every client and server daemon (e.g., between `kube-apiserver` and `etcd`, or between `kube-apiserver` and `kubelet`).
2. **Elimination of Anonymous Endpoints:** Disabling all unauthenticated entrypoints (such as Kubelet port `10250` anonymous access or API server `--anonymous-auth`).
3. **Delegated Webhook Authorization:** Removing permissive default authorization policies (`AlwaysAllow`) and forcing every component to consult centralized API Server RBAC rules before executing commands or serving data.

```
+---------------------------------------------------------------------------------+
|                       CENTRAL KUBERNETES CONTROL PLANE                          |
|                                                                                 |
|   +-------------------+               mTLS                +-----------------+   |
|   |  kube-apiserver   | <===============================> |   etcd :2379    |   |
|   +-------------------+     --client-cert-auth=true       +-----------------+   |
|             │                                                                   |
|             │ mTLS & SubjectAccessReview Webhook                                |
|             ▼                                                                   |
|   +-------------------+                                                         |
|   |   kubelet :10250  | (Host Node Daemon)                                      |
|   |   - anonymous: false                                                        |
|   |   - mode: Webhook |                                                         |
|   +-------------------+                                                         |
+---------------------------------------------------------------------------------+
```

---

## 🏛️ Architectural Context (How it fits in the architecture)
This domain operates directly at Layer 2 (**Cluster**) of the 4Cs Security Model:
* It shields the data storage layer (`etcd`) from unauthorized reads or writes that could compromise the entire cluster.
* It closes the node execution plane (`kubelet`), preventing attackers who gain network access to worker nodes from bypassing the API Server audit logging engine.
* It guarantees that even if perimeter firewalls fail, internal communication channels require valid cryptographic credentials issued by the cluster Public Key Infrastructure (PKI).

---

## 🧩 Problem Solver (What problem it solves)
* **Out-of-Band Remote Code Execution:** Prevents attackers from using `curl` against Kubelet port `10250` (`/run/<ns>/<pod>/<container>`) to execute arbitrary commands inside containers without leaving an API audit trail.
* **Plaintext / Stolen Credential etcd Extraction:** Prevents rogue actors from accessing etcd port `2379` to dump all secrets, tokens, and cluster state without presenting a valid, signed client certificate.
* **Impersonation & Replay Attacks:** Enforces Proof of Possession during TLS handshakes so that intercepted public certificates cannot be re-used by attackers.

---

## 🟢 Operational Impact (What will happen with it operating)
* **Zero-Trust Communication:** All management requests to the Kubelet and etcd require TLS client certificates and valid authorization tokens.
* **Full Auditability:** Every execution request against a container is mediated through the API Server, subjected to RBAC policies, and logged to the central audit log.
* **Hardened Recovery:** Static pods and systemd services restart with explicit cryptographic requirements, alerting administrators immediately if certificates expire or configurations drift.

---

## 🔴 Failure Impact (What will happen without it)
* **Instant Total Cluster Compromise:** An attacker on the internal network can connect to etcd on port `2379` and dump bootstrap tokens, cluster-admin credentials, and private keys.
* **Stealth Container Takeover:** Attackers query Kubelet's `/runningpods` endpoint, locate high-value workloads, and attach interactive shell sessions without triggering API Server admission controllers or audit policies.

---

## 🔍 Deeper Dive Notes
* [[Main Notes/Kubernetes Component Security - Kubelet Port 10250, etcd Client Auth, and mTLS Handshake Mechanics|Kubelet Port 10250, etcd Client Auth, and mTLS Handshake Mechanics]]
* [[Main Notes/Kubernetes Node Maintenance - Kubeadm Upgrades, APT Hold Mechanics, and Package Lifecycle|Worker Node Maintenance, Kubeadm Upgrades & APT Hold Mechanics]]
* [[Main Notes/Kubernetes API Server Security - Request Lifecycle, NodeRestriction, and Protected Namespaces|API Server Security, NodeRestriction & Protected Namespaces]]
* [[Main Notes/Kubernetes Node Security - Host OS Hardening, Docker Daemon, and Socket Isolation|Host OS Hardening, Docker Daemon & Socket Isolation]]
* [[Main Notes/Kubernetes Secret Encryption at Rest - EncryptionConfiguration, Provider Chains, and etcd Verification|Secret Encryption at Rest, EncryptionConfiguration & etcd Verification]]

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

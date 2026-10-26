---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: security
domains:
  - kubernetes
related_concepts:
  - "[[Kubernetes Cluster Component Hardening and Communication Security]]"
  - "[[Kubernetes Network Security and Traffic Segregation]]"
  - "[[Kubernetes Pod Security and Policy Engines]]"
against: []
reference_guides:
  - "[[Reference Notes/0-7-1_rbac_service_accounts_and_certificates.md]]"
tags:
  - kubernetes/security
  - kubernetes/service-account
  - kubernetes/workload-identity
  - kubernetes/cks
  - status/completed
---

# Kubernetes ServiceAccounts and Workload Identity

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Security > **Kubernetes ServiceAccounts and Workload Identity**

---

## 🎯 Purpose (Why it is used)
Every process executing inside a Kubernetes cluster requires an identifiable cryptographic persona to interact with the API Server, participate in admission policies, and access external cloud services. **ServiceAccounts** provide in-cluster workload identities distinct from human user accounts. Hardening ServiceAccount credential delivery—moving from unbounded static secret tokens to dynamically projected, time-delimited, audience-bound tokens—ensures that workloads operate strictly under least privilege without leaving permanent credentials exposed on container filesystems.

---

## ⚙️ Functionality (What it is doing)
The ServiceAccount identity and credential system operates across three tiers:

1. **Control Plane Identity:** Assigns a persistent identity (`spec.serviceAccountName`) used by RBAC authorizers, admission controllers (PSA, OPA Gatekeeper), and cloud federation engines (AWS IRSA, GCP Workload Identity).
2. **Auto-Mount Suppression:** Permits administrators and developers to disable default credential injection (`automountServiceAccountToken: false`), ensuring that workloads with no API Server dependency expose zero credentials to attackers.
3. **Projected Token Issuance:** Leverages the Kubernetes `TokenRequest` API via `projected` volumes to dynamically mint short-lived, audience-scoped, pod-bound JSON Web Tokens (JWTs) automatically rotated on disk by the Kubelet.

```
+---------------------------------------------------------------------------------+
|                       KUBERNETES WORKLOAD IDENTITY MODEL                        |
|                                                                                 |
|   +--------------------------+                      +-----------------------+   |
|   |  Standard Web / DB Pod   |                      |  Audited Operator Pod |   |
|   |  automount: false        |                      |  automount: false     |   |
|   +--------------------------+                      +-----------------------+   |
|     │                                                 │                         |
|     ▼                                                 ▼ (Projected Volume)      |
|   [ Zero Token on Disk ]                            [ Time-Bound JWT Token ]    |
|   [ Impossible to Steal]                            - Expires in 3600s          |
|                                                     - Audience: Scoped          |
|                                                     - Auto-rotated by Kubelet   |
+---------------------------------------------------------------------------------+
```

---

## 🏛️ Architectural Context (How it fits in the architecture)
This domain operates across Layer 2 (**Cluster**) and Layer 3 (**Container**) of the 4Cs Security Model:
* It eliminates long-lived static bearer tokens from the data plane, neutering credential theft following Remote Code Execution (RCE).
* It bridges in-cluster pod identity to external cloud IAM providers via OIDC discovery endpoints (`/.well-known/openid-configuration`), enabling passwordless cloud access.
* It works in concert with RBAC RoleBindings, ensuring that even if a token is stolen, the token's blast radius is strictly constrained by time, audience, and namespace.

---

## 🧩 Problem Solver (What problem it solves)
* **Perpetual Credential Theft:** Replaces legacy, non-expiring ServiceAccount tokens stored in static Kubernetes Secrets with ephemeral tokens.
* **Token Replay Across Endpoints:** Eliminates cross-service token replay by enforcing audience scoping (`aud`), ensuring tokens minted for HashiCorp Vault or Cloud IAM cannot be reused against the Kubernetes API Server.
* **Sidecar & Multi-Container Exposure:** Allows fine-grained credential injection so that only trusted sidecars receive credentials, while public-facing application containers remain credential-less.

---

## 🟢 Operational Impact (What will happen with it operating)
* **Zero Residual Risk on Web Apps:** 90%+ of cluster workloads run with `automountServiceAccountToken: false`, presenting no usable credentials to web attackers.
* **Automated Key Rotation:** Kubelet periodically refreshes projected token files on disk before expiration without container restarts or application downtime.
* **Granular Audit Trails:** API Server audit logs capture the precise pod UID and ServiceAccount for every authenticated call.

---

## 🔴 Failure Impact (What will happen without it)
* **Indefinite Cluster Takeover:** An attacker exploiting a single public pod harvests `/var/run/secrets/kubernetes.io/serviceaccount/token` and maintains permanent administrative access from outside the cluster.
* **Audience Confusion Exploitation:** Tokens intended for external monitoring or metrics services are replayed against internal administrative APIs.

---

## 🔍 Deeper Dive Notes
* [[Main Notes/Kubernetes ServiceAccount Token Projection - Bound Tokens, Volume Projections, and Audience Scoping|ServiceAccount Token Projection, Bound Tokens, and Projected Volumes]]

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

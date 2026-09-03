---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: security
domains:
  - "kubernetes"
  - "security"
related_concepts:
  - "[[admission-controller]]"
  - "[[Trivy]]"
against:
  - "[[pod-security-admission]]"
reference_guides:
  - "[[Reference Notes/0-7-5_supply_chain_security_and_imagepolicywebhook.md]]"
tags:
  - kubernetes/security
  - kubernetes/admission-controllers
  - status/completed
---

# ImagePolicyWebhook

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Admission Controllers > **ImagePolicyWebhook**

---

## 🎯 Purpose (Why it is used)
**ImagePolicyWebhook** is a specialized validating admission controller plugin built into the `kube-apiserver`. Its purpose is to enforce container image governance by intercepting pod creation and update requests and querying an external webhook service to determine whether the requested container images are authorized to run.

---

## ⚙️ Functionality (What it is doing)
* **Image Interception:** Intercepts pod specifications before they are written to `etcd`.
* **External Webhook Query:** Sends an HTTP/HTTPS POST request containing an `image-policy.k8s.io/v1alpha1` `ImageReview` payload to an external security verification service.
* **Admission Enforcement:** Approves or rejects pod admission based on the external service's boolean decision and policy evaluation (e.g., verifying image signatures, scanning status, or trusted registries).
* **Fail-Closed Configuration:** Supports configuring `defaultAllow: false` to block all pod creations if the external verification service is unreachable.

---

## 🏛️ Architectural Context (How it fits in the architecture)
ImagePolicyWebhook executes as an admission plugin inside the `kube-apiserver` binary. It requires an admission configuration file (`--admission-control-config-file`) and an internal KubeConfig that points to the external backend webhook endpoint with mutual TLS credentials.

---

## 🧩 Problem Solver (What problem it solves)
CI/CD scanning pipelines can be bypassed by cluster administrators or compromised service accounts running imperative `kubectl run` commands with arbitrary images from untrusted public registries. ImagePolicyWebhook guarantees that only cryptographically verified, vulnerability-scanned images from approved registries can be instantiated in the cluster.

---

## 🟢 Operational Impact (What will happen with it operating)
Untrusted or unapproved container images are blocked at the API gateway with a descriptive error message explaining why the image was rejected.

---

## 🔴 Failure Impact (What will happen without it)
Users or automated controllers can pull and run malicious or vulnerable images from unverified registries, increasing cluster exposure to crypto-miners, backdoors, and unpatched CVEs.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **ImagePolicyWebhook**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

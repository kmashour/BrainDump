---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: security
domains:
  - "kubernetes"
  - "security"
related_concepts:
  - "[[ImagePolicyWebhook]]"
  - "[[kube-bench]]"
against:
  - "[[Falco]]"
reference_guides:
  - "[[Reference Notes/0-7-5_supply_chain_security_and_imagepolicywebhook.md]]"
tags:
  - kubernetes/security
  - kubernetes/supply-chain
  - status/completed
---

# Trivy

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Security > **Trivy**

---

## 🎯 Purpose (Why it is used)
**Trivy** is a comprehensive, open-source vulnerability, secret, and misconfiguration scanner for containers and cloud-native systems. It scans container images, filesystems, Git repositories, and Kubernetes manifests to identify known Common Vulnerabilities and Exposures (CVEs) before code or images are deployed.

---

## ⚙️ Functionality (What it is doing)
* **OS & Language Dependency Scanning:** Detects CVEs across Linux distribution packages (Alpine, Debian, Ubuntu, Red Hat) and language-specific package managers (npm, pip, Maven, Go modules).
* **Severity Filtering:** Filters scan results by severity thresholds (`UNKNOWN`, `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`).
* **CI/CD Integration & Automated Gating:** Returns non-zero exit codes (e.g. `--exit-code 1`) when severe vulnerabilities are identified, automatically failing deployment pipelines.
* **Secret & Misconfiguration Detection:** Scans for hardcoded credentials, exposed API keys, and insecure Kubernetes YAML manifests.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Trivy operates primarily in the **Supply Chain (Code & Container)** layers of the 4Cs model. It is integrated into CI/CD build pipelines (e.g., GitHub Actions, GitLab CI) and image registries, acting as a gatekeeper before images are admitted into the Kubernetes cluster.

---

## 🧩 Problem Solver (What problem it solves)
Container images frequently bundle hundreds of outdated operating system libraries containing documented vulnerabilities. Without automated scanning, developers unknowingly ship vulnerable software into production, exposing systems to known remote code execution exploits.

---

## 🟢 Operational Impact (What will happen with it operating)
Deployment pipelines automatically reject vulnerable images before they can be deployed to clusters. Teams gain precise remediation guidance (package name and patched target version).

---

## 🔴 Failure Impact (What will happen without it)
Vulnerable dependencies remain embedded in container workloads. Attackers can execute documented public exploits against known CVEs in libraries such as OpenSSL, glibc, or log4j.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Trivy**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

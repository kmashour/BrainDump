---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: client-tool
domains:
  - "terraform"
related_concepts:
  - "[[Main Notes/aws.md]]"
  - "[[Main Notes/kubernetes.md]]"
against:
  - "[[Main Notes/ansible.md]]"
reference_guides:
  - "[[Reference Notes/10-Index - Terraform on AWS.md]]"
tags:
  - terraform/tool
  - status/completed
---

# Terraform

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > IaC > **Terraform**

---

## 🎯 Purpose (Why it is used)
Terraform is an open-source, declarative Infrastructure as Code (IaC) tool designed to build, version, and manage cloud and on-premise resources safely and predictably using HashiCorp Configuration Language (HCL).

---

## ⚙️ Functionality (What it is doing)
*   **State Tracking:** Maintains a mapping database (`terraform.tfstate`) between your HCL resource code declarations and actual running cloud resources.
*   **Execution Planning:** Generates an execution plan showing the exact API calls (creates, updates, destroys) it will run to reach your desired state.
*   **Resource Graphing:** Constructs a dependency graph to resolve resource references and provision independent resources in parallel.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Terraform sits as the provisioning layer. It interfaces directly with cloud provider APIs (like AWS) using provider plugins, setting up baseline infrastructure (VPCs, databases, VM clusters) on top of which applications and container platforms (like Kubernetes) are deployed.

---

## 🧩 Problem Solver (What problem it solves)
*   **Eliminates Configuration Drift:** Enforces declarative declarations, overriding manual cloud console changes.
*   **Avoids Monolithic Lock-ins:** Simplifies infrastructure migrations and multi-cloud configurations using unified HCL patterns.
*   **Prevents Provisioning Collisions:** Uses state backend locking to stop concurrent runs from corrupting metadata.

---

## 🟢 Operational Impact (What will happen with it operating)
Infrastructure changes are reviewable via pull requests. Deployment speeds scale up, configurations are reproducible across test/prod environments, and resource properties are tracked transparently in version-controlled files.

---

## 🔴 Failure Impact (What will happen without it)
Infrastructure must be configured manually via CLI scripts or cloud consoles. Configuration drift becomes inevitable. Staging and production configurations drift apart, and disaster recovery processes are slow and prone to errors.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes and use cases associated with Terraform.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

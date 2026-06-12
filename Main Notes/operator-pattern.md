---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: control-plane
domains:
  - "kubernetes"
related_concepts:
  - "[[customresourcedefinition]]"
against:
  - "[[deployment]]"
reference_guides:
  - "[[Reference Notes/0-15_kubernetes_api_extension_and_operators.md]]"
tags:
  - kubernetes/extending
  - status/completed
---

# Operator Pattern

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > infra > **Operator Pattern**

---

## 🎯 Purpose (Why it is used)
The **Operator Pattern** is a software extension pattern that combines CustomResourceDefinitions (CRDs) with custom controller logic to automate the deployment, scaling, and management of complex, stateful application systems (such as databases or cache clusters).

---

## ⚙️ Functionality (What it is doing)
*   **Operational Packaging:** Translates human runbooks and admin procedures (e.g. database schema migrations, replication failover) into executable code loops.
*   **Active Reconciliation:** Monitors custom specifications and continuously performs actions on the cluster to enforce state requirements.
*   **Dynamic Healing:** Automates stateful failovers, backing up data, and executing rolling node upgrades without human intervention.

---

## 🏛️ Architectural Context (How it fits in the architecture)
*   **Control Loop Layer:** Runs as a standard workload pod (Custom Controller) inside the cluster, watching events on target CRD types and issuing requests back to the API Server.
*   **Resource Owner:** Acts as the parent controller that spawns and owns standard workloads (like StatefulSets, Services, and Secrets).

---

## 🧩 Problem Solver (What problem it solves)
Standard workloads (like Deployments or StatefulSets) only manage stateless processes or simple disk mounts. They cannot handle complex stateful actions, such as electing a database leader, syncing replica lag, or scheduling dynamic database backups. The Operator Pattern solves this by embedding domain-specific operations directly into the control loop.

---

## 🟢 Operational Impact (What will happen with it operating)
*   **Automated Runbooks:** Reduces the manual overhead of managing complex clustered databases.
*   **Standardized Deployments:** Creates predictable, declarative configurations for third-party tools.

---

## 🔴 Failure Impact (What will happen without it)
*   **Manual Upkeep:** Cluster administrators must manually execute database restarts, backups, and failovers, increasing the risk of downtime.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Operator Pattern**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND (contains(parent_concept, this.file.link) OR icontains(string(parent_concept), this.file.name))
SORT file.name ASC
```

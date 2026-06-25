---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
  - "kubernetes"
related_concepts:
  - "[[Amazon ECS]]"
  - "[[Amazon ECR]]"
  - "[[aws - Elastic Load Balancer]]"
  - "[[aws - Amazon EFS]]"
  - "[[Secrets Store CSI Driver]]"
against:
  - "[[Amazon ECS]]"
  - "[[kube-apiserver]]"
reference_guides:
  - "[[Reference Notes/3-17_containers_ecs_eks.md]]"
tags:
  - aws/eks
  - kubernetes/eks
  - status/completed
---

# Amazon EKS

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **Amazon EKS**

---

## 🎯 Purpose (Why it is used)
Amazon Elastic Kubernetes Service (EKS) is a managed service that runs the Kubernetes control plane (API server, etcd) across multiple Availability Zones on AWS. It allows developers to run standard, open-source Kubernetes workloads on AWS without the operational burden of bootstrapping and maintaining control plane components.

---

## ⚙️ Functionality (What it is doing)
*   **Managed Control Plane:** Automatically replicates and hosts API servers and etcd databases across multiple AZs, handling control plane upgrades and patches.
*   **Auto Mode Capacity Provisioning:** Integrates with built-in node management engines (powered by Karpenter) to dynamically spin up worker instances when pods lack capacity.
*   **IAM Roles for Service Accounts (IRSA):** Maps IAM Roles to Kubernetes ServiceAccounts, enabling fine-grained, least-privilege AWS access at the pod level.
*   **Storage CSI Integration:** Provisions AWS EBS, EFS, or FSx persistent volumes dynamically using Container Storage Interface (CSI) drivers.

---

## 🏛️ Architectural Context (How it fits in the architecture)
EKS serves as the interface between the standard Kubernetes API and AWS infrastructure resources. EKS worker nodes consume AWS VPC configurations, communicate with the managed control plane, pull images from Amazon ECR, and interface with AWS security and storage elements.

---

## 🧩 Problem Solver (What problem it solves)
Bootstraping a production-grade Kubernetes cluster requires managing highly available etcd databases, control plane certificates, load balancers, node join tokens, and upgrading API configurations without downtime. EKS automates this control plane lifecycle, ensuring high availability and compliance.

---

## 🟢 Operational Impact (What will happen with it operating)
Workloads are managed via standard Kubernetes YAML manifests (`deployments`, `services`, `pods`) using clients like `kubectl`. Worker nodes (either managed node groups, Fargate, or Auto Mode) scale automatically to fit resource request bounds, and Kubernetes DNS/network controllers manage routing.

---

## 🔴 Failure Impact (What will happen without it)
If the EKS control plane becomes unreachable:
*   Running worker nodes and active pods continue processing traffic, but no configuration changes can be made.
*   Pods cannot be rescheduled, created, updated, or deleted via the API.
*   Deployments and ReplicaSets cannot reconcile state in response to application pod crashes.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Amazon EKS**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

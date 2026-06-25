---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[Amazon ECS]]"
  - "[[Amazon EKS]]"
  - "[[aws - IAM Role]]"
  - "[[Amazon S3]]"
against: []
reference_guides:
  - "[[Reference Notes/3-17_containers_ecs_eks.md]]"
tags:
  - aws/ecr
  - status/completed
---

# Amazon ECR

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **Amazon ECR**

---

## 🎯 Purpose (Why it is used)
Amazon Elastic Container Registry (ECR) is a fully managed container registry that makes it easy for developers to store, manage, share, and deploy container images. It provides secure hosting of container layers with high availability and low latency.

---

## ⚙️ Functionality (What it is doing)
*   **Image Storage:** Securely stores Docker and OCI-compliant container image layers using Amazon S3 for 99.999999999% durability.
*   **Vulnerability Scanning:** Offers two scanning tiers: Basic scanning (static analysis powered by Clair, triggered on push) and Advanced scanning (continuous runtime and registry scanning integrated with Amazon Inspector).
*   **Lifecycle Management:** Automatically expires and deletes old or untagged image versions based on custom lifecycle policy rules to reduce S3 storage costs.
*   **Authentication & Access Control:** Leverages native AWS IAM policies. Users must run the `aws ecr get-login-password` CLI command to retrieve a temporary authorization token (valid for 12 hours) to perform `docker push` or `docker pull` operations.
*   **Public Registries:** Supports Amazon ECR Public Gallery to publish and share container images globally with free anonymous pull capacity.

---

## 🏛️ Architectural Context (How it fits in the architecture)
ECR serves as the build-artifact repository for CI/CD pipelines (e.g. GitHub Actions, Jenkins) pushing built Docker images. Orchestrators like Amazon ECS and Amazon EKS pull images directly from ECR to boot container workloads, relying on Task Execution Roles and Node IAM Roles to authenticate.

---

## 🧩 Problem Solver (What problem it solves)
Without ECR, organizations must host and secure their own private Docker registries, handle SSL certificates, manage storage capacity, and secure API endpoints. ECR eliminates this operational overhead, providing an out-of-the-box registry integrated natively with AWS security.

---

## 🟢 Operational Impact (What will happen with it operating)
Build pipelines push container images to ECR repositories. ECR checks for vulnerabilities and triggers notifications, while container hosts retrieve image layers over secure channels during application scaling or deployments.

---

## 🔴 Failure Impact (What will happen without it)
If ECR fails or permissions are misconfigured:
*   Workloads cannot pull images to start new containers.
*   ECS and EKS tasks fail to boot, throwing image pull error warnings.
*   CI/CD pipelines fail at the image upload phase, halting software deployment.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Amazon ECR**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

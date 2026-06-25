---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[Amazon EKS]]"
  - "[[Amazon ECR]]"
  - "[[aws - Elastic Load Balancer]]"
  - "[[aws - Auto Scaling Group]]"
  - "[[aws - Amazon EFS]]"
against:
  - "[[Amazon EKS]]"
  - "[[aws - EC2 Instance]]"
reference_guides:
  - "[[Reference Notes/3-17_containers_ecs_eks.md]]"
tags:
  - aws/ecs
  - status/completed
---

# Amazon ECS

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **Amazon ECS**

---

## 🎯 Purpose (Why it is used)
Amazon Elastic Container Service (ECS) is a fully managed container orchestration service designed to deploy, run, and scale containerized applications on AWS. It allows running Docker containers at scale without the complexity of managing a full Kubernetes API control plane.

---

## ⚙️ Functionality (What it is doing)
*   **Launch Types:** Computes tasks using two execution modes: EC2 Launch Type (user-managed VMs running the ECS Agent with an EC2 Instance Profile Role) and Fargate Launch Type (fully serverless, allocating a dedicated ENI per task using `awsvpc` mode).
*   **Granular IAM Roles:** Enforces security isolation using the ECS Task Execution Role (used by the agent *before* boot to pull images from ECR and fetch secrets from Secrets Manager/SSM Parameter Store) and the ECS Task Role (used by the application container *during* runtime to access AWS APIs like S3 or DynamoDB).
*   **Dynamic Port Mapping:** Enables load balancing compatibility. For EC2, ALB target groups map dynamic ephemeral host ports (32768-65535) to container ports. For Fargate, the ALB routes traffic directly to the private IP of the task ENI.
*   **Shared Storage:** Supports mounting Amazon EFS (Elastic File System) volumes directly inside ECS tasks, enabling multi-AZ persistent, shared file access for serverless and VM containers.
*   **Service & Infrastructure Scaling:** Automatically scales task count based on CPU/Memory utilization or ALB Request Count per Target. Also scales the underlying host infrastructure dynamically using ECS Cluster Capacity Providers to provision more EC2 instances in the Auto Scaling Group when tasks are pending capacity.

---

## 🏛️ Architectural Context (How it fits in the architecture)
ECS acts as the orchestrator connecting container images from Amazon ECR to compute resources (EC2 instances or Fargate serverless). It sits behind Application Load Balancers for traffic distribution and interfaces with Amazon EFS for multi-AZ shared storage volume mounting.

---

## 🧩 Problem Solver (What problem it solves)
Without ECS, developers must manually SSH into EC2 instances, manage Docker run commands, handle health routing, write custom scripts to replace crashed containers, and manage manual scaling. ECS automates this deployment and healing lifecycle, improving uptime and infrastructure efficiency.

---

## 🟢 Operational Impact (What will happen with it operating)
With ECS running, workloads are deployed as decoupled tasks across multiple Availability Zones. Services automatically scale task counts up or down in response to CloudWatch alarms tracking CPU, memory, or request metrics, while the orchestrator dynamically registers targets with the ALB.

---

## 🔴 Failure Impact (What will happen without it)
If the ECS orchestration service fails or becomes unreachable:
*   Running tasks continue to execute on hosts, but no new tasks can be started or scaled.
*   Crashed tasks are not replaced, leading to service degradation if host instances fail.
*   Target groups inside load balancers do not update, causing traffic to be routed to stale or unhealthy IPs.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Amazon ECS**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

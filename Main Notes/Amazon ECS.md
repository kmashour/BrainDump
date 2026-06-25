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
*   **Task Scheduling:** Places tasks (running container instances) onto compute capacity based on CPU, memory, and availability constraints.
*   **Service Maintenance:** Monitors task health and automatically recreates failed tasks to maintain a desired running state.
*   **Dynamic Port Mapping:** Integrates with Elastic Load Balancing (ELB) to register tasks using dynamic host port configurations.
*   **Capacity Provider Scaling:** Automatically scales the underlying EC2 Auto Scaling Groups (ASGs) when tasks are pending due to capacity constraints.

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

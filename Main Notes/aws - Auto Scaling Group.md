---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[aws - EC2 Instance]]"
  - "[[aws - Elastic Load Balancer]]"
against: []
reference_guides:
  - "[[Reference Notes/3-11_aws_asg_auto_scaling.md]]"
tags:
  - aws/autoscaling
  - status/completed
---

# aws - Auto Scaling Group

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - EC2 and Elastic Load Balancing]] > **Auto Scaling Group**

---

## 🎯 Purpose (Why it is used)
The AWS Auto Scaling Group (ASG) dynamically manages a fleet of EC2 instances, adjusting capacity horizontally to match demand. It is used to ensure application availability, scale compute resources in response to load spikes (elasticity), scale down to minimize compute costs, and automatically replace unhealthy instances.

---

## ⚙️ Functionality (What it is doing)
- **Fleet Sizing:** Maintains instance count bounds defined by Minimum, Maximum, and Desired capacities.
- **Auto-Healing:** Constantly checks instance health (via EC2 Status Checks and ELB Health Checks) and replaces failed instances automatically.
- **Dynamic & Predictive Scaling:** Adjusts capacity reactively based on CloudWatch alarms (Target Tracking, Step, or Simple policies) or proactively based on machine learning forecasts.
- **Lifecycle Integration:** Utilizes Lifecycle Hooks to pause instances during launch or termination for custom setups or data backups.
- **Cost Optimization:** Mixes On-Demand and Spot instances and supports different instance types in a single group (via Launch Templates).
- **AZ Balancing:** Automatically attempts to distribute EC2 instances evenly across all configured Availability Zones.

---

## 🏛️ Architectural Context (How it fits in the architecture)
ASG is configured to deploy EC2 instances using a **Launch Template**. It coordinates directly with an **Elastic Load Balancer** (ALB/NLB) to automatically register newly launched instances and deregister terminating instances. Subnets are defined at the ASG level to control network placement.

---

## 🧩 Problem Solver (What problem it solves)
Without an ASG, system administrators must manually provision, configure, and register servers to handle traffic increases, and manually replace crashed servers. ASG automates both provisioning and healing, preventing outages due to capacity exhaust or node failures.

---

## 🟢 Operational Impact (What will happen with it operating)
The compute tier scales dynamically with traffic load, maintaining optimal application performance while minimizing idle-resource costs. Failed instances are replaced within minutes.

---

## 🔴 Failure Impact (What will happen without it)
If the ASG is disabled, misconfigured, or fails:
- The application cannot handle unexpected traffic spikes, leading to performance degradation or outages.
- Unhealthy compute nodes will not be replaced, leading to capacity decay.
- Scaling down during low-traffic periods will not occur, increasing compute costs.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Auto Scaling Group**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

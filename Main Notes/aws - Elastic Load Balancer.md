---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[aws - EC2 Instance]]"
  - "[[aws - Application Load Balancer]]"
  - "[[aws - Network Load Balancer]]"
  - "[[aws - Gateway Load Balancer]]"
against: []
reference_guides:
  - "[[Reference Notes/3-10_aws_elb_load_balancing.md]]"
tags:
  - aws/loadbalancing
  - status/completed
---

# aws - Elastic Load Balancer

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - EC2 and Elastic Load Balancing]] > **Elastic Load Balancer**

---

## 🎯 Purpose (Why it is used)
Amazon Elastic Load Balancing (ELB) automatically distributes incoming traffic across multiple targets (such as EC2 instances, containers, and IP addresses) within one or more Availability Zones. It is used to achieve fault tolerance, high availability, and seamless elasticity for applications.

---

## ⚙️ Functionality (What it is doing)
- **Traffic Distribution:** Balances incoming client requests across registered healthy targets.
- **Health Monitoring:** Performs health checks on targets and stops routing traffic to unhealthy ones.
- **SSL/TLS Termination:** Decrypts HTTPS traffic at the load balancer, offloading processing overhead from backend instances.
- **Cross-Zone Balancing:** Distributes requests evenly across targets in all enabled Availability Zones.
- **Sticky Sessions:** Binds a client session to a specific target via cookies for stateful workloads.

---

## 🏛️ Architectural Context (How it fits in the architecture)
ELB serves as the single public or private ingress point for application traffic, sitting between clients and downstream backend resources. Security Groups are typically configured to allow instance-level traffic only when it originates from the load balancer's security group.

---

## 🧩 Problem Solver (What problem it solves)
Without an ELB, client traffic must be directed to individual public IPs of EC2 instances, leading to single points of failure, manual routing adjustments during crashes, and uneven workload distribution. ELB abstractly decouples the compute tier from clients, enabling dynamic scaling, patching, and failover without client disruption.

---

## 🟢 Operational Impact (What will happen with it operating)
Traffic is distributed evenly across multiple Availability Zones. If load increases, Auto Scaling adds instances which are dynamically registered to the ELB to absorb traffic. Certificate rotations are managed centrally on the ELB.

---

## 🔴 Failure Impact (What will happen without it)
If the load balancer fails or is misconfigured, inbound traffic to the application will be dropped. Individual backend server failures will directly impact clients.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Elastic Load Balancer**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

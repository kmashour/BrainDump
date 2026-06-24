---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[aws - Elastic Load Balancer]]"
  - "[[aws - Application Load Balancer]]"
  - "[[aws - Gateway Load Balancer]]"
against: []
reference_guides:
  - "[[Reference Notes/3-10_aws_elb_load_balancing.md]]"
tags:
  - aws/loadbalancing
  - status/completed
---

# aws - Network Load Balancer

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - Elastic Load Balancer]] > **Network Load Balancer**

---

## 🎯 Purpose (Why it is used)
The Network Load Balancer (NLB) is a Layer 4 load balancer designed to handle millions of requests per second with ultra-low latency. It is used for load balancing TCP, UDP, and TLS traffic where high performance, extreme throughput, and static IP addresses are required.

---

## ⚙️ Functionality (What it is doing)
- **Layer 4 Routing:** Routes connection requests at the transport layer (TCP/UDP/TLS) without inspecting the application payload.
- **Static & Elastic IPs:** Can be assigned a static IP (Elastic IP) per Availability Zone, providing a fixed entry point.
- **Ultra-Low Latency:** Offers sub-millisecond latencies, making it ideal for high-performance and gaming workloads.
- **Client IP Preservation:** Preserves the client's source IP address in TCP packets routed to registered EC2 instances (registered by Instance ID).
- **Target Routing to ALB:** Can load balance traffic to an Application Load Balancer (ALB), combining NLB's static IP advantages with ALB's Layer 7 routing rules.
- **PrivateLink Integration:** Acts as the backend service entry point for AWS PrivateLink (Interface VPC Endpoints).

---

## 🏛️ Architectural Context (How it fits in the architecture)
NLB sits at the networking layer, routing connections to EC2 targets, private IP targets, or ALBs. Since NLB does not support Security Groups directly (it forwards traffic directly without proxying HTTP), target EC2 instances must allow traffic from NLB nodes or subnet CIDRs in their security groups and NACLs.

---

## 🧩 Problem Solver (What problem it solves)
ALB cannot handle raw TCP/UDP traffic or provide static IP addresses (ALB's DNS name points to dynamic IP addresses). NLB solves the problem of high-velocity non-HTTP traffic, static firewall IP whitelist requirements, and secure private endpoint exposing via PrivateLink.

---

## 🟢 Operational Impact (What will happen with it operating)
Workloads can handle sudden spikes in traffic without pre-warming. Client connection details (IP/Port) are preserved. Cross-zone load balancing is disabled by default (and chargeable if enabled).

---

## 🔴 Failure Impact (What will happen without it)
If the NLB fails, all TCP/UDP connections to the service are cut off. Static IP entry points will become unreachable. Interface VPC endpoints mapped to the NLB will fail.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Network Load Balancer**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

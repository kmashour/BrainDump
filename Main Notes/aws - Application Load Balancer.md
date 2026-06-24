---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[aws - Elastic Load Balancer]]"
  - "[[aws - Network Load Balancer]]"
  - "[[aws - Gateway Load Balancer]]"
against: []
reference_guides:
  - "[[Reference Notes/3-10_aws_elb_load_balancing.md]]"
tags:
  - aws/loadbalancing
  - status/completed
---

# aws - Application Load Balancer

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - Elastic Load Balancer]] > **Application Load Balancer**

---

## 🎯 Purpose (Why it is used)
The Application Load Balancer (ALB) is a Layer 7 load balancer designed to route HTTP, HTTPS, and WebSocket traffic. It is used when applications require advanced, content-based routing decisions at the application layer, such as path-based, host-based, query-string, or header-based routing.

---

## ⚙️ Functionality (What it is doing)
- **Layer 7 Content Routing:** Evaluates request headers to route traffic to specific target groups (e.g., path-based routing like `/users` vs `/search`, host-based routing like `api.example.com`).
- **Dynamic Port Mapping:** Works with Amazon ECS to map traffic to dynamically allocated container ports on EC2 hosts.
- **SSL/TLS Termination & SNI:** Decrypts HTTPS traffic and supports Server Name Indication (SNI) to serve multiple domains and SSL certificates from a single listener.
- **Protocols Supported:** Supports HTTP/1.1, HTTP/2, and WebSockets.
- **Algorithms:** Supports Round Robin and Least Outstanding Requests load balancing.
- **WAF Integration:** Integrates directly with AWS Web Application Firewall (WAF) to secure HTTP traffic.

---

## 🏛️ Architectural Context (How it fits in the architecture)
ALB sits at the application layer ingress, accepting HTTP/HTTPS connections. It acts as the gateway to containerized microservices (ECS, EKS) and target EC2 fleets. Security groups are configured to lock down EC2 access to only accept traffic from the ALB's security group.

---

## 🧩 Problem Solver (What problem it solves)
Traditional Layer 4 load balancers cannot inspect HTTP/HTTPS payloads, meaning developers would need multiple load balancers to route `/api` traffic differently from `/images` traffic. ALB solves this by centralizing Layer 7 routing rules in a single resource, reducing architecture complexity and costs.

---

## 🟢 Operational Impact (What will happen with it operating)
Clients connect to a single DNS name, and ALB routes them to the appropriate backend target group. Path-based microservices scale independently, and cross-zone load balancing is on by default with no inter-AZ data transfer charges.

---

## 🔴 Failure Impact (What will happen without it)
If the ALB fails, all HTTP/HTTPS client access to the application stops. Advanced path-based routing rules and centralized WAF protections are disabled.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Application Load Balancer**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: network
domains:
  - "aws"
related_concepts:
  - "[[Amazon VPC]]"
against: []
reference_guides:
  - "[[Reference Notes/3-9_aws_vpc_networking.md]]"
tags:
  - aws/networking
  - status/completed
---

# Network Access Control List

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[Reference Notes/3-Index - AWS|AWS]] > [[Amazon VPC]] > **Network Access Control List**

---

## 🎯 Purpose (Why it is used)
A **Network Access Control List (NACL)** is a stateless network security layer that acts as a firewall at the **subnet boundary** within a VPC. It is used to define granular inbound and outbound traffic permissions for all resources inside an associated subnet, providing a second defense-in-depth security layer beneath instance-level Security Groups.

---

## ⚙️ Functionality (What it is doing)
- **Subnet-Level Filtering:** Applies security rules to all ingress and egress packets crossing the subnet boundary.
- **Stateless Evaluation:** Evaluates each packet individually. Outbound response traffic is NOT automatically allowed and must be explicitly permitted by outbound rules.
- **Numbered Rules:** Processes rules in order, from the lowest-numbered rule to the highest. Once a packet matches a rule, evaluation stops immediately.
- **Allow and Deny Rules:** Supports both allow rules (whitelisting) and deny rules (blacklisting, e.g., blocking malicious IP addresses).
- **Default/Custom Profiles:** Default NACL allows all traffic; custom NACL denies all traffic by default.

---

## 🏛️ Architectural Context (How it fits in the architecture)
NACLs sit between the subnets and the VPC Implied Router. Every subnet in a VPC must be associated with exactly one NACL; if no association is defined, the subnet defaults to the main VPC NACL. Outbound rules must be configured with a return path to the client's ephemeral port range (`TCP 1024-65535`) to allow responses from services like web servers.

---

## 🧩 Problem Solver (What problem it solves)
Security Groups are associated with individual instances and do not allow explicit **deny** rules, making it difficult to block specific hostile IP addresses or configure subnet-wide traffic gates. NACLs solve this problem by allowing administrative blocking of traffic at the subnet boundary, ensuring that blocked traffic never reaches instance network interfaces.

---

## 🟢 Operational Impact (What will happen with it operating)
Traffic is validated at the subnet edge, protecting resources from unauthorized scans. Stateless behavior requires administrators to double-configure routing (both inbound and outbound directions). Custom NACLs must be monitored closely to ensure the ephemeral port ranges are allowed outbound for client-server communication.

---

## 🔴 Failure Impact (What will happen without it)
If a NACL is misconfigured (e.g., missing an outbound rule to allow returning traffic on ephemeral ports, or an incorrect rule sequence), all connection handshakes to the subnet will fail. Clients will experience connection timeouts, and backend services will be isolated despite having fully permissive Security Groups.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Network Access Control List**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[Network Access Control List]]
SORT file.name ASC
```

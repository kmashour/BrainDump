---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: network
domains:
  - "networking"
related_concepts:
  - "[[routing]]"
against:
  - "[[ospf]]"
reference_guides:
  - "[[Reference Notes/4-Index - BGP Routing.md]]"
tags:
  - bgp/component
  - status/completed
---

# bgp

**Breadcrumbs:** [[0-Index|🏠 Index]] > Networking > **bgp**

---

## 🎯 Purpose (Why it is used)
BGP (Border Gateway Protocol) is a path-vector routing protocol designed to exchange routing and reachability information between Autonomous Systems (AS) on the internet.

---

## ⚙️ Functionality (What it is doing)
*   Routes packets across different network domains.
*   Enforces routing policies based on path attributes (e.g., AS-Path, Local Preference).
*   Maintains internal routing consistency using iBGP Route Reflectors.

---

## 🏛️ Architectural Context
BGP forms the control plane routing engine of the global internet and is frequently utilized inside enterprise networks and cloud datacenters (like AWS Transit Gateway or Kubernetes Calico CNI running in BGP mode) to advertise subnets dynamically.

---

## 🔍 Deeper Dive Notes
```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

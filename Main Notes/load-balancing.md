---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "networking"
  - "infra"
related_concepts:
  - "[[service]]"
  - "[[ingress]]"
against:
  - "[[dns-round-robin]]"
reference_guides:
  - "[[Reference Notes/1-2_load_balancing_topologies.md]]"
tags:
  - system-design/load-balancer
  - status/completed
---

# Load Balancing

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **Load Balancing**

---

## 🎯 Purpose (Why it is used)
Load Balancing is used to distribute incoming client network traffic across a pool of backend servers (or nodes) to prevent server overload, maximize resource utilization, and ensure high availability of application systems.

---

## ⚙️ Functionality (What it is doing)
- **Traffic Distribution:** Routes client requests to backend application servers using configured algorithms (e.g., Round Robin, Least Connections, IP Hash).
- **Health Monitoring:** Conducts periodic active checks (pings or HTTP requests) to assess backend server health.
- **Node Eviction and Re-entry:** Automatically evicts failed nodes from the routing pool and reinstates recovered nodes.
- **SSL/TLS Termination:** Offloads cryptographic handshake and encryption processing from backend servers.
- **Session Persistence (Sticky Sessions):** Routes requests from a specific client to the same backend server based on cookies or IP hashing.

---

## 🏛️ Architectural Context (How it fits in the architecture)
A Load Balancer sits between the clients (browsers, mobile apps) and the backend application servers. It intercepts all incoming requests, selects a healthy target server, proxies the request, and returns the server's response to the client.

---

## 🧩 Problem Solver (What problem it solves)
- **Single Server Overload:** Prevents a single host from running out of CPU, RAM, or disk I/O under high traffic.
- **Single Point of Failure (SPOF):** Eliminates downtime when an individual backend server crashes, as traffic is immediately rerouted to surviving instances.
- **No-Downtime Deployments:** Allows for rolling updates by temporarily evicting servers under maintenance without client interruption.

---

## 🟢 Operational Impact (What will happen with it operating)
With load balancing active, the system can scale horizontally by adding or removing backend servers dynamically. Traffic is distributed evenly, and individual node failures are masked from users, maintaining high system availability.

---

## 🔴 Failure Impact (What will happen without it)
Without a load balancer, clients must connect directly to backend server IPs. If a backend server fails, clients connecting to that IP will experience immediate service denial. Scaling must be done vertically (upgrading hardware), which has physical limits and introduces downtime.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Load Balancing**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "networking"
  - "infra"
related_concepts:
  - "[[caching]]"
  - "[[load-balancing]]"
against: []
reference_guides:
  - "[[Reference Notes/1-4_caching_and_content_delivery_networks.md]]"
tags:
  - system-design/cdn
  - status/completed
---

# Content Delivery Networks (CDNs)

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Networking > **Content Delivery Networks (CDNs)**

---

## 🎯 Purpose (Why it is used)
A Content Delivery Network (CDN) is used to serve static assets (images, video, JS, CSS, HTML files) to clients from a geographically distributed network of proxy servers, minimizing round-trip latency and reducing load on origin servers.

---

## ⚙️ Functionality (What it is doing)
- **Geographic Proxying:** Serves files from edge locations physically closer to users.
- **Edge Caching:** Caches static files based on HTTP cache-control headers and TTLs.
- **Anycast Routing:** Maps requests sharing a single IP address to the physically nearest edge server.
- **SSL Termination & Shielding:** Offloads SSL/TLS cryptographic handshakes and blocks DDoS attacks at the network edge.

---

## 🏛️ Architectural Context (How it fits in the architecture)
A CDN sits at the absolute outermost edge of the infrastructure, immediately following DNS resolution. When clients request static assets, the DNS points to the CDN. Only dynamic API requests pass through to the origin load balancer.

---

## 🧩 Problem Solver (What problem it solves)
- **High Latency:** Prevents round-trip latency caused by traversing long transoceanic cables.
- **Bandwidth Consumption:** Offloads massive static files (e.g. video streams) from the origin server's bandwidth limits.
- **Origin Server Exhaustion:** Protects application servers from crashing during traffic spikes by caching static assets.

---

## 🟢 Operational Impact (What will happen with it operating)
With a CDN operating, users across the globe experience near-instant page load times. Origin servers run with minimal CPU and network utilization since they only process dynamic APIs.

---

## 🔴 Failure Impact (What will happen without it)
Without a CDN, all static assets must be retrieved directly from the origin server. Under high traffic, this will exhaust the server's network bandwidth, causing massive slow-downs, timeout errors, and origin crashes.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **CDNs**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
WHERE class = "deeper-dive" AND contains(parent_concept, this.file.link)
SORT file.name ASC
```

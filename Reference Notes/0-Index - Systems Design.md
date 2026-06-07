---
obsidianUIMode: preview
class: index-note
tier: reference-note
tags:
  - system-design/reference-index
  - obsidian/moc
---

# 📐 Systems Design Reference MOC

**Breadcrumbs:** [[0-Index|🏠 Index]] > **Systems Design Reference MOC**

---

## 🏛️ Reference Modules & Frameworks

This index contains our system design study modules focused on high-level architecture scaling, caching, network communication protocols, and security guards.

- 🖥️ **[System Design Fundamentals](17_system_design_fundamentals.md)** (Module 17)
  *   **Scaling:** Single-server request loops, vertical vs. horizontal scaling, and master-replica consistency models.
  *   **Load Balancing:** Routing algorithms (Round Robin, Least Connections, IP Hashing), active health pings, and active-standby redundancy pairs.
  *   **Database Scaling:** Sharding partitioning keys, hot spot risks, and Consistent Hashing rings (including virtual nodes).
  *   **Caching & CDNs:** Caching write policies (Cache-Aside, Write-Through, Write-Behind), evictions (LRU, LFU, FIFO), failure outages (Cache Avalanche, Cache stampedes, Cache penetration), CDN Pull/Push styles, and Anycast BGP routing.
  *   **API Protocols:** RESTful CRUD, GraphQL single-endpoint client schemas, gRPC HTTP/2 stream multiplexing, and binary Protobuf serialization.
  *   **Transport Layers:** Connection-oriented TCP (three-way handshake) vs. connectionless UDP.
  *   **AAA Security:** Stateful session authentication, stateless JWT access/refresh token validation, RBAC/ABAC models, OAuth 2.0 authorization, OpenID Connect (OIDC) authentication, and edge shields (WAF, CORS, rate limiters, SQL injection parameterization).

---

## 🛠️ Verification Projects
Hands-on deployment setups, testing configurations, and verification curls compiled from systems design tracks:
- 🚀 **[Project: Secure Load-Balanced Web API](../Projects/Systems%20Design/Project%20-%20Secure%20Load-Balanced%20Web%20API.md)**

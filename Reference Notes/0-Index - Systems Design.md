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

- 🖥️ **[Module 1-1: Scaling & Single Server Setup](1-1_scaling_and_single_server.md)**
  *   Single-server request loops, DNS resolution, and vertical vs. horizontal scaling.
- 🚦 **[Module 1-2: Load Balancing Topologies & Algorithms](1-2_load_balancing_topologies.md)**
  *   Layer 4 vs. Layer 7 routing, LB algorithms (Round Robin, Least Conn, IP Hash), health checks, and SPOF redundancy.
- 🗄️ **[Module 1-3: Database Architectures & Sharding](1-3_database_architectures_and_sharding.md)**
  *   SQL vs. NoSQL vs. Graph databases, ACID vs. BASE, replicas, sharding partition keys, and Consistent Hashing rings.
- 💾 **[Module 1-4: Caching & Content Delivery Networks (CDNs)](1-4_caching_and_content_delivery_networks.md)**
  *   Write policies (Cache-Aside, Write-Through, Write-Behind), eviction algorithms, caching failures, CDNs, and Anycast BGP routing.
- 🔌 **[Module 1-5: API Protocols & gRPC](1-5_api_protocols_and_grpc.md)**
  *   RESTful HTTP, GraphQL single-endpoint client schemas, transport layer protocols (TCP vs. UDP), and gRPC multiplexing/Protobuf over HTTP/2.
- 🛡️ **[Module 1-6: Access Control & API Security](1-6_access_control_and_api_security.md)**
  *   AAA foundation, session-based vs. stateless JWT auth, RBAC/ABAC, OAuth 2.0/OIDC, and edge security shields (Rate Limiting, WAF, CORS, SQLi protection).

---

## 🛠️ Verification Projects
Hands-on deployment setups, testing configurations, and verification curls compiled from systems design tracks:
- 🚀 **[Project: Secure Load-Balanced Web API](../Projects/Systems%20Design/Project%20-%20Secure%20Load-Balanced%20Web%20API.md)**

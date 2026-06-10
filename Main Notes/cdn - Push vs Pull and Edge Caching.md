---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[cdn]]"
sub_type: core-concept
source_type: documentation
source_url: "https://www.youtube.com/watch?v=C842vFY5kRo"
author: "Hayk Simonyan"
course_title: "System Design Course"
tags:
  - system-design/cdn
  - system-design/deep-dive
---

# CDN - Push vs Pull and Edge Caching

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[cdn]] > **Push vs Pull and Edge Caching**

---

## 📑 Pull CDNs vs. Push CDNs

CDN caching models depend on resource update frequency and data volume:

### 1. Pull CDNs (Lazy Loading)
- **Mechanics:** The origin server does not push any content. When a user requests an asset:
  1. The request goes to the nearest CDN edge node.
  2. If the asset exists (*Cache Hit*), it returns it.
  3. If missing (*Cache Miss*), the edge server queries the origin server, stores a copy, and returns it.
- **Trade-offs:**
  - **Pros:** Low storage usage on edge nodes (only stores requested hot files); minimal management overhead.
  - **Cons:** First user requests experience slow response times (due to the cache miss write path).

### 2. Push CDNs (Proactive Uploads)
- **Mechanics:** The origin server proactively pushes new or updated content directly to CDN edge servers (e.g., via CI/CD pipelines or admin scripts).
- **Trade-offs:**
  - **Pros:** Zero cache miss latency for users; high file availability.
  - **Cons:** Storage costs are higher (files are cached even if never requested); requires custom logic to push updates.

---

## 📑 Routing Optimization: Anycast

To ensure requests reach the geographically nearest edge proxy, CDNs utilize **Anycast Routing**:
- **Mechanism:** Multiple physical edge servers share the exact same IP address.
- **Routing:** BGP (Border Gateway Protocol) routing selects the shortest path through the internet infrastructure to direct the client's packet to the closest edge server. This distributes the load naturally across points of presence (PoPs).

*Read more in [Caching & CDNs](../Reference%20Notes/1-4_caching_and_content_delivery_networks.md#3-content-delivery-networks-cdns)*

---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[load-balancing]]"
sub_type: core-concept
source_type: documentation
source_url: "https://www.youtube.com/watch?v=C842vFY5kRo"
author: "Hayk Simonyan"
course_title: "System Design Course"
tags:
  - system-design/load-balancing
  - system-design/deep-dive
---

# Load Balancing - Algorithms and L4-L7 Routing

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[load-balancing]] > **Algorithms and L4-L7 Routing**

---

## 📑 Routing Layers: L4 vs. L7

Load Balancing can be implemented at different layers of the network stack, offering varying degrees of performance and intelligence:

### 1. Layer 4 (L4) Transport-Level Routing
- **Operation:** Routes traffic based on packet headers at the transport layer (TCP/UDP), examining only IPs and port numbers. It does not inspect the message contents.
- **Characteristics:**
  - Extremely fast and CPU-efficient since it avoids deep packet inspection or SSL/TLS decryption.
  - Stateful at the TCP level (tracks TCP connection states).
  - Incapable of path routing (e.g., cannot separate traffic for `/api` vs. `/static`) or header-based manipulation.

### 2. Layer 7 (L7) Application-Level Routing
- **Operation:** Routes traffic based on HTTP/HTTPS data, including URL paths, request headers, cookies, and query strings.
- **Characteristics:**
  - Requires parsing the application payload (e.g., JSON request bodies) and performing SSL/TLS termination, which is CPU-intensive.
  - Allows highly intelligent routing (e.g., routing based on tenant ID in cookies, URL paths, or request methods).
  - Can modify requests (injecting headers like `X-Forwarded-For`) before proxying them to backends.

---

## 📑 Load Balancing Algorithms

Load balancers rely on specific mathematical algorithms to assign clients to backend targets:

| Algorithm | Routing Strategy | Optimal Use Cases | Trade-offs |
| :--- | :--- | :--- | :--- |
| **Round Robin** | Sequential distribution of requests across the server list. | Backend servers have identical hardware and request execution times are uniform. | Simple to implement, but can overload weaker servers. |
| **Weighted Round Robin** | Distributes requests based on a predefined capacity coefficient (weight) per server. | Heterogeneous server pools where some servers have higher CPU/RAM capacity. | Requires manual configuration of weights; doesn't adjust dynamically. |
| **Least Connections** | Directs new requests to the server with the lowest count of active TCP connections. | Systems with long-lived client transactions (e.g., SQL sessions, file uploads). | Requires LBs to maintain state of connections; high overhead. |
| **IP Hash** | Hashes the client's source IP address to compute a static target server. | Applications that require state/session persistence on a specific node. | Uneven traffic distribution if many clients originate from a single NAT proxy. |

*Read more in [[Reference Notes/1-2_load_balancing_topologies.md#2. Load Balancing Algorithms]]*

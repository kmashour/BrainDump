---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[service]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/"
author: "Kubernetes Authors"
course_title: "Kubernetes Service Concepts"
tags:
  - kubernetes/service
  - kubernetes/deep-dive
---

# service - EndpointSlices and Topology routing

**Breadcrumbs:** [[Index|🏠 Index]] > [[service]] > **EndpointSlices and Topology routing**

---

## 📑 EndpointSlices Scalability & Zone Routing

EndpointSlices provide a highly scalable, localized, and context-aware mechanism for managing service endpoints (typically Pod IPs) in large-scale Kubernetes clusters.

### 1. EndpointSlices vs Legacy Endpoints
The legacy `Endpoints` API suffers from severe scaling limitations because it stores all backend IPs for a Service in a single monolithic object. To resolve this, `EndpointSlices` slice endpoints into individual chunks:
*   **Chunking Limit:** Default is **100 endpoints per slice**.
*   **Transmitting Updates:** Any changes (crashes, scaling, rolling updates) only rewrite and propagate the single affected `EndpointSlice` rather than the entire list, reducing control plane CPU load and API server traffic by $O(N)$ where $N$ is the number of Pods.
*   **Dual-Stack Networking:** Automatically provisions separate EndpointSlices for IPv4 and IPv6 families on dual-stack clusters.

### 2. Endpoint Conditions & Graceful Draining
Each endpoint tracks specific conditions to ensure traffic is routed to healthy pods:
*   `Ready`: The pod is healthy and ready to accept new traffic.
*   `Serving`: Indicates the Pod is actively running and matches the readiness probe. Crucially, this stays `true` when a Pod is terminating, enabling traffic drains.
*   `Terminating`: Indicates the Pod is shutting down (e.g., received `SIGTERM`). `kube-proxy` can finish in-flight connections on this pod while bypassing it for new requests.

### 3. Topology Aware Routing (Zone Preference)
Topology-aware routing optimizes in-cluster traffic to prefer backend endpoints located in the same Availability Zone (AZ) as the client Pod.
*   **Activation:** Annotate the Service with:
    ```yaml
    service.kubernetes.io/topology-mode: Auto
    ```
*   **Hints Mechanism:** The endpoint controller appends hints (e.g. `us-east-1a`) to the endpoints inside `EndpointSlices`. `kube-proxy` reads these hints to build node-local/zone-local forwarding rules.
*   **Constraints & Fallback:** It requires an even distribution of Pods across zones. If zone capacity drops below a safe threshold (or has fewer than 3 endpoints), the controller disables hints, reverting to cross-zone routing to preserve service availability.

### 4. Node-Local Traffic Policy
For maximum performance, you can bypass cross-node network hops by restricting traffic to endpoints on the same node using `internalTrafficPolicy`:
*   `spec.internalTrafficPolicy: Local`: Forces requests to stay on the local node. If no local endpoint exists, traffic is dropped immediately. Highly useful for node-level agents or daemonsets.

*Read more in [10_networking_dns_and_ingress.md](../Reference%20Notes/10_networking_dns_and_ingress.md#72-endpointslices)*

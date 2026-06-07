---
obsidianUIMode: preview
class: pattern-note
tier: main-note
domains:
  - "kubernetes"
  - "networking"
components:
  - "[[service]]"
  - "[[gateway-api]]"
  - "[[pod]]"
sources:
  - "Kubernetes Service Documentation"
  - "Reference Notes/10_networking_dns_and_ingress.md"
tags:
  - architecture/pattern
  - kubernetes/networking
---

# Pattern: Multi-Zone Service Routing and Latency Mitigation

**Breadcrumbs:** [[0-Index|🏠 Index]] > Patterns > **Multi-Zone Service Routing and Latency Mitigation**

---

## 🏛️ Architectural Context

In multi-zone clusters (e.g. AWS EKS stretched across three Availability Zones), network traffic traversing zones incurs data transfer charges and latency penalties. This pattern combines **Topology Aware Routing** and the **Gateway API** to localize traffic pathing within the same Availability Zone.

```
       [ Client Pod (Zone A) ] 
                 |
        [ HTTPRoute / Gateway ]
          /                 \
 [ Local Pods (Zone A) ]   [ Remote Pods (Zone B) ]
   (Preferred: Hints/Auto)   (Fallback: Cross-Zone)
```

1.  **Ingress Entry:** A `Gateway` is deployed at the edge. The operator configures an `HTTPRoute` to forward requests to the app service.
2.  **Zone Tagging:** The control plane applies `topology.kubernetes.io/zone` labels to nodes and pods.
3.  **EndpointSlice hints:** The service controller evaluates topology and assigns AZ routing hints to matching `EndpointSlice` objects.
4.  **Local Redirection:** The `kube-proxy` proxier maps these hints to select local backends, directing the Client Pod to the target Pod in Zone A.

---

## ⚖️ Trade-offs & Alternatives

*   **Topology Aware Routing vs Service Mesh:**
    *   *Topology Routing (Built-in):* Lightweight, uses core `EndpointSlice` API, no sidecar proxy overhead. However, it requires an even distribution of pods across zones.
    *   *Service Mesh (Linkerd/Istio):* Provides robust, weighted locality-based load balancing, but introduces sidecar latency and resource overhead.
*   **internalTrafficPolicy: Local vs Cluster:**
    *   *`Local`:* Guarantees zero-network latency (restricts traffic to the same host node). However, it lacks node-level failover. If no local pod is running on the node, requests fail.
    *   *`Cluster` (with Topology Mode Auto):* Prefers local zone routing but falls back to other zones/nodes automatically if local pods are unhealthy.

---

## 🛠️ Verification & Practical Implementation

#### 1. Configure the Service for Topology routing:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: app-service
  annotations:
    service.kubernetes.io/topology-mode: Auto
spec:
  selector:
    app: app-backend
  ports:
  - name: http
    port: 80
    targetPort: 8080
```

#### 2. Verify endpoint slices contain topology hints:
```bash
# Get endpoint slice details for the service
kubectl get endpointslice -l kubernetes.io/service-name=app-service -o yaml
```
Verify the `endpoints` list contains the `hints` metadata matching the client zone:
```yaml
endpoints:
- addresses:
  - 10.244.1.45
  conditions:
    ready: true
  hints:
    forZones:
    - name: us-east-1a
  topology:
    kubernetes.io/zone: us-east-1a
```

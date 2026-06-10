---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[service]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/tutorials/services/source-ip/"
author: "Kubernetes Authors"
course_title: "Kubernetes Service Tutorials"
tags:
  - kubernetes/service
  - kubernetes/deep-dive
---

# service - Source IP and Pod Termination Lifecycle

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[service]] > **Source IP and Pod Termination Lifecycle**

---

## 📑 Source IP Preservation (`externalTrafficPolicy`)

When external traffic (from clients outside the cluster) hits a Service (e.g. NodePort or LoadBalancer), Kubernetes handles client source IP mapping in two ways:

### 1. `externalTrafficPolicy: Cluster` (Default)
* **Mechanics:** Traffic hitting any cluster node is routed by Kube-Proxy across all pods in the cluster. If the targeted pod resides on a different node, the packet is forwarded across the overlay network. This requires **Source NAT (SNAT)**, which overwrites the client's source IP with the forwarding node's IP.
* **Pros:** Even load distribution across all pods in the cluster.
* **Cons:** Loss of the original client source IP (the backend application sees node IPs).

### 2. `externalTrafficPolicy: Local`
* **Mechanics:** Traffic is only routed to pods running on the exact node that receives the traffic. No cross-node hop is performed, and **SNAT is bypassed**. The client's original source IP is fully preserved.
* **Pros:** Client source IP visibility is maintained.
* **Cons:**
  * If a node has no active pods for the service, traffic is dropped.
  * Risk of unequal traffic distribution if pods are not distributed evenly across nodes.

---

## 📑 Pod & Endpoint Termination Lifecycle

Gracefully decommissioning pods during rollouts or scale-downs is critical to prevent connection errors:

```mermaid
sequenceDiagram
    participant API as API Server
    participant EP as Endpoint Controller
    participant KP as Kube-Proxy / Ingress
    participant KL as Kubelet
    participant Pod as Pod Container

    API->>KL: 1. Set deletionTimestamp / Send SIGTERM
    API->>EP: 1. Mark Pod as Terminating
    EP->>API: 2. Remove IP from Endpoints
    API->>KP: 3. Watcher detects endpoint removal
    KP->>KP: 4. Remove Pod IP from routing rules
    KL->>Pod: 5. SIGTERM / Run preStop Hook
    Pod->>Pod: 6. Finish in-flight requests (sleep)
    Note over Pod: terminationGracePeriod (30s)
    KL->>Pod: 7. Force SIGKILL (if still running)
    API->>API: 8. Remove Pod from etcd
```

### The Race Condition and preStop Hook Mitigation
Because endpoint removal and SIGTERM signaling run asynchronously in parallel, there is a race condition where a container starts shutting down before Kube-proxy removes its IP from node routing rules. To prevent clients hitting terminating containers:
* **Mitigation:** Define a `preStop` hook to introduce a sleep delay (e.g., `sleep 5`). This holds container shutdown until Kube-proxy has completely updated local routing rules.
  ```yaml
  lifecycle:
    preStop:
      exec:
        command: ["/bin/sh", "-c", "sleep 5 && nginx -s quit"]
  ```

*Read more in [0-9_networking_dns_and_ingress.md](../Reference%20Notes/0-9_networking_dns_and_ingress.md#44-source-ip-preservation-externaltrafficpolicy)*

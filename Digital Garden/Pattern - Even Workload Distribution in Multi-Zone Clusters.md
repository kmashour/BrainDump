---
obsidianUIMode: preview
class: pattern-note
tier: main-note
domains:
  - "kubernetes"
  - "networking"
components:
  - "[[kube-scheduler]]"
  - "[[pod]]"
  - "[[node]]"
sources:
  - "Kubernetes Scheduling Documentation"
  - "Reference Notes/0-13_scheduling_logging_and_lifecycle.md"
tags:
  - architecture/pattern
  - kubernetes/scheduling
---

# Pattern: Even Workload Distribution in Multi-Zone Clusters

**Breadcrumbs:** [[Digital Garden/0-Index|🏠 Index]] > Patterns > **Even Workload Distribution in Multi-Zone Clusters**

---

## 🏛️ Architectural Context

When hosting highly available user-facing microservices in a multi-zone cluster, simply using node affinity or zone selectors is insufficient. A zone selector might place all replicas in a single zone if that zone has the most free resources, creating a single point of failure.

This pattern leverages **Topology Spread Constraints** combined with **Pod Priority Classes** to guarantee that Pod replicas are evenly distributed across availability zones, while protecting high-priority workloads from being starved.

```
                  [ PriorityClass: critical-app ]
                                 |
              [ Deployment: maxSkew: 1 / Zone Spread ]
             /                   |                    \
   [ Zone A (2 Pods) ]   [ Zone B (1 Pod) ]   [ Zone C (1 Pod) ]
```

1.  **Placement Constraints:** The deployment defines a `topologySpreadConstraints` matching the label selector of the frontend pods with a `maxSkew` of 1.
2.  **Resource Contention:** If zone resources are exhausted, the high-priority class forces the scheduler to preempt lower-priority batch jobs in the target zone to maintain the even zone spread.

---

## ⚖️ Trade-offs & Alternatives

*   **Topology Spread Constraints vs Pod Anti-Affinity:**
    *   *Pod Anti-Affinity (Hard):* Strictly prevents scheduling more than one Pod on the same topology domain. Extremely rigid; if you have 3 zones and request 4 replicas, the 4th replica will remain `Pending` forever.
    *   *Topology Spread Constraints:* Allows you to define a relaxed skew (e.g. `maxSkew: 1` or `maxSkew: 2`) which dynamically balances workloads even when replica counts exceed zone counts.
*   **whenUnsatisfiable: DoNotSchedule vs ScheduleAnyway:**
    *   *`DoNotSchedule`:* Hard constraint. Ensures strict zone balance, but can leave replicas `Pending` if resources in a zone are exhausted.
    *   *`ScheduleAnyway`:* Soft constraint. Prefers zone balance but prioritizes application availability by placing the Pod in another zone if resources are constrained.

---

## 🛠️ Verification & Practical Implementation

#### 1. Define the PriorityClass:
```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: critical-web-app
value: 500000
globalDefault: false
description: "Workload priority class for frontend services."
```

#### 2. Configure the Deployment spread constraints:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-frontend
spec:
  replicas: 4
  selector:
    matchLabels:
      app: web-nginx
  template:
    metadata:
      labels:
        app: web-nginx
    spec:
      priorityClassName: critical-web-app
      topologySpreadConstraints:
      - maxSkew: 1
        topologyKey: topology.kubernetes.io/zone
        whenUnsatisfiable: DoNotSchedule
        labelSelector:
          matchLabels:
            app: web-nginx
      containers:
      - name: nginx
        image: nginx:alpine
```

#### 3. Verify Pod spread across zones:
```bash
# Display pod names, node names, and zone details
kubectl get pods -l app=web-nginx -o wide
```
Verify that the output shows an even distribution of nodes across availability zones.

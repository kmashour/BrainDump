---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: control-plane
domains:
  - "kubernetes"
related_concepts:
  - "[[pod]]"
  - "[[deployment]]"
against:
  - "[[verticalpodautoscaler]]" # Horizontal scaling vs Vertical scaling
reference_guides:
  - "[[Reference Notes/0-6_kubernetes_workloads_and_controllers.md]]"
tags:
  - kubernetes/component
  - status/completed
---

# horizontalpodautoscaler

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > workloads > **horizontalpodautoscaler**

---

## 🎯 Purpose (Why it is used)
The **Horizontal Pod Autoscaler (HPA)** dynamically adjusts the number of replica Pods in a Deployment, ReplicaSet, or StatefulSet based on observed CPU utilization, memory usage, or custom application metrics. HPA ensures that applications automatically scale out to maintain performance during traffic spikes and scale in during idle periods to minimize cluster compute costs.

---

## ⚙️ Functionality (What it is doing)
*   **Metrics Collection:** Periodically queries the `metrics.k8s.io` API (supplied by the cluster's Metrics Server) to collect resource utilization data.
*   **Scale Calculations:** Compares current resource usage against the target threshold using the scaling formula:
    $$\text{desiredReplicas} = \left\lceil \text{currentReplicas} \times \frac{\text{currentMetricValue}}{\text{desiredMetricValue}} \right\rceil$$
*   **Scale-Up/Down Enforcements:** Safely scales out replicas up to the configured `maxReplicas` limit, and scales back in down to the `minReplicas` limit.
*   **Scale-Down Stabilization:** Applies a cooling period (typically 5 minutes) to prevent rapid fluctuations (thrashing) when metrics fluctuate near the threshold.

---

## 🏛️ Architectural Context (How it fits in the architecture)
*   **Metrics Server:** The primary telemetry provider that gathers stats from node-level `cAdvisor` agents and serves them to the API Server.
*   **Kube-Controller-Manager:** Runs the HPA controller loop periodically (sync period defaults to 15s).
*   **Deployment Controller:** Receives replica updates from the HPA controller and manages ReplicaSet scaling.

---

## 🧩 Problem Solver (What problem it solves)
Without HPA, administrators must manually scale deployments via `kubectl scale` to handle varying user traffic. This risks application downtime if traffic spikes occur while administrators are offline, or leads to resource waste (idle nodes) from statically provisioning for peak capacity. HPA automates the capacity sizing loop.

---

## 🟢 Operational Impact (What will happen with it operating)
*   **Automatic Load Handling:** Traffic spikes trigger fast scaling of replica counts to distribute load.
*   **Cost Control:** Pods are deleted when traffic recedes, allowing Kubernetes to consolidate nodes and reduce infrastructure costs.
*   **Infrastructure Dependency:** Requires a healthy Metrics Server installation; if the Metrics Server crashes, HPA cannot scale.

---

## 🔴 Failure Impact (What will happen without it)
*   **Service Instability:** Heavy traffic loads will saturate existing pods, leading to slow response times, connection timeouts, and application crashes.
*   **Manual Scaling Overhead:** Operators must continuously monitor utilization metrics and run manual scale actions.

---

## ⚙️ Operational Workflow

### 1. Imperative CLI Creation
Create an HPA targeting a Deployment with a CPU target of 80% and a replica boundary of 2 to 10:
```bash
kubectl autoscale deployment web-deploy --cpu-percent=80 --min=2 --max=10
```

### 2. Declaring HPA YAML (autoscaling/v2)
Define the HPA declaratively to monitor CPU resource metrics:
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: web-app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web-app-deployment
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 80
```

### 3. Monitoring HPA Status
View the target metrics, thresholds, and current replica counts:
```bash
kubectl get hpa
```

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **horizontalpodautoscaler**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

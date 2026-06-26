---
obsidianUIMode: preview
class: landing-note
tier: main-note
domains:
  - "kubernetes"
role: workload
related_concepts:
  - "[[node]]"
  - "[[container-runtime]]"
  - "[[kube-scheduler]]"
reference_guides:
  - "[[Reference Notes/0-5_containers_runtimes_and_lifecycle.md]]"
  - "[[Reference Notes/0-6_kubernetes_workloads_and_controllers.md]]"
  - "[[Reference Notes/0-12_kubernetes_api_management_and_pod_immutability.md]]"
tags:
  - kubernetes/workload
  - status/completed
against: []
deeper_dive: "[[pod-deeper]]"
---

# pod

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Workloads & Infrastructure > **pod**

---

## 🎯 Purpose (Why it is used)
The `Pod` is the smallest, most basic deployable object in Kubernetes. It represents a logical host for one or more tightly coupled containers that share the same network namespace, storage volumes, and scheduling context, facilitating application co-location and local communication.

---

## ⚙️ Functionality (What it is doing)
1. **Logical Hosting:** Wraps application containers and storage definitions into a single operational unit.
2. **Network Sharing:** Assigns a single IP address to the Pod. All containers inside the Pod share this IP and port space, enabling them to communicate via `localhost`.
3. **Volume Sharing:** Mounts shared storage directories into multiple containers simultaneously for collaborative read/write operations.
4. **Lifecycle Management:** Coordinates startup order (via Init containers), manages health checks (via probes), runs start/stop actions (via hooks), and executes graceful termination sequences.
5. **Security Enclosure:** Enforces security profiles, service account identities, and scheduling constraints at the Pod boundary.

---

## 📄 Pod Manifest Structure & Metadata Scopes

A Pod manifest consists of the four mandatory Kubernetes root fields: `apiVersion: v1`, `kind: Pod`, `metadata` (containing identification like `name` and `labels`), and `spec` (specifying container configuration like `image` and `ports`).

### Pod Metadata vs. Template Metadata
* **Pod Metadata (Outer Scope):** Configured at the root of the Pod manifest. Defines identification properties for the specific Pod resource instance (e.g., `metadata.name: my-app-pod`).
* **Template Metadata (Inner Scope):** Embedded under `spec.template.metadata` in higher-level controllers (such as Deployments or ReplicaSets). This defines the template from which Pods will be created, specifying labels that must match the controller's label selectors (`spec.selector.matchLabels`).

---

## 🏛️ Architectural Context (How it fits in the architecture)
The Pod is the building block of all workloads in the cluster:
* **The Scheduling Target:** The `kube-scheduler` assigns the Pod to a Node by updating its metadata in the API Server.
* **The Kubelet's Directive:** The `kubelet` parses the PodSpec and calls the local Container Runtime (CRI) to spin up the required containers.
* **Managed Objects:** In production, Pods are rarely created directly. They are created and managed by higher-level controllers (like `Deployments`, `StatefulSets`, or `DaemonSets`) which handle replica scaling, rollouts, and self-healing.

---

## 🧩 Problem Solver (What problem it solves)
* **Co-Location and Helper Patterns:** Solves the problem of running helper processes (e.g., logging sidecars, proxy agents, database sync adapters) alongside primary applications by ensuring they are scheduled on the exact same host node and can access the same files and network loop.
* **Dynamic IP Allocation:** Dynamically provisions a unique IP for each Pod in the cluster, removing port-allocation conflicts between containers on the same physical host.
* **Host User Isolation:** Solves container-escape vulnerabilities by mapping container user IDs to unprivileged host user IDs (using `spec.hostUsers: false`), ensuring that a root user inside the container does not carry root privileges on the host node.

---

## 🟢 Operational Impact (What will happen with it operating)
* **Workload Execution:** Application containers run with full network and storage integration.
* **Component Coordination:** Sidecars and main processes coordinate work seamlessly through shared filesystems or local ports.
* **Automatic Scaling:** Deployment controllers can scale the application up or down by spawning or terminating Pod instances.

---

## 🔴 Failure Impact (What will happen without it)
* **No Workloads:** The cluster cannot host or schedule any applications.
* **Loss of Orchestration:** Containers must be run manually as individual host processes or raw Docker containers, losing all automatic scheduling, scaling, and self-healing benefits.
* **Resource Leakage:** Without Pod-level cleanups, terminated containers, orphaned volumes, and stale network routes accumulate on the host OS.
* **Broken Helper Relationships:** Helper containers cannot easily share the same network address space or file systems with primary containers, breaking standard architectural patterns (like sidecar proxies).

---

## 📊 Observability (Logging)
* **Tailing Container Logs:** Standard output and standard error streams are read via the Kubelet:
  ```bash
  kubectl logs <pod-name>
  ```
* **Multi-Container Targets:** When a Pod runs multiple containers, omitting the target container results in a selection error. You must explicitly target the container name using `-c`:
  ```bash
  kubectl logs <pod-name> -c <container-name>
  ```
* **Logging Sidecars:** To capture application logs written to internal filesystem paths rather than stdout/stderr, pods can run streaming sidecars (which tail internal files to stdout) or log shipper sidecars (which read internal files and push metrics/logs directly to external engines).

---

## 🔍 Deeper Dive
For detailed configurations, sub-concepts, and step-by-step CKA playbooks, see:
* **[[pod-deeper]]**

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```



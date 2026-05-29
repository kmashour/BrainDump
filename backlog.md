# CKA Knowledge Base Update Backlog

This backlog tracks all updates, modifications, and restructuring activities performed in this CKA study knowledge base.

---

## [2026-05-29] - Ingestion & Consolidation of Container Mechanics

### Added
- **[05_containers_runtimes_and_lifecycle.md](05_containers_runtimes_and_lifecycle.md):** Compiled raw notes from `inflow/Containers.md` into a structured, production-grade guide covering OCI images, Kubelet-CRI architecture, process isolation topology via `RuntimeClass` and micro-virtualization overhead, custom container setup/shutdown hooks, standard and native sidecars, and `ephemeralContainers` process namespace target troubleshooting.
- **PoC Suite:** Created a complete hands-on verification pipeline inside Module 05 containing service links tests, log redirection hooks verification, native sidecar/init sequential boot order tests, and `/ephemeralcontainers` PID debugging.

### Changed / Updated
- **[README.md](README.md):** Updated search indexes and expanded the master Mermaid.js brain map to link CRI services, shims, runc execution paths, namespaces, probes, hooks, native sidecars, and runtime class constraints.
- **Cross-Linking:** Added Obsidian graph references between Module 05 and Modules 01, 02, 03, and 04.

## [2026-05-27] - Knowledge Base Restructuring & Obsidian Integration

### Added
- **`inflow/` Directory:** Created as a dedicated landing zone for raw transcripts, documentation links, and course notes.
- **[backlog.md](file:///home/karim/Desktop/CKA/backlog.md):** Created this backlog file to track knowledge base transaction history.

### Changed / Moved
- **Moved** `Overview-Architecuture-Kubernetes.md` to [inflow/Overview-Architecuture-Kubernetes.md](file:///home/karim/Desktop/CKA/inflow/Overview-Architecuture-Kubernetes.md) to serve as a raw ingestion source.
- **Updated** [instructions.md](file:///home/karim/Desktop/CKA/instructions.md) to define:
  - Clear compilation rules for migrating material from `inflow/` to consolidated study modules.
  - Standard markdown relative links for Obsidian graph visualization.
  - Thorough explanatory writing guidelines (mandatory examples, deep architectural context, no summaries unless strictly educational).
  - Iterative policy to keep updating the repository approach.
- **Updated** [README.md](file:///home/karim/Desktop/CKA/README.md) to map the new `inflow/` directory structure and integrate modules index links.
- **Restructured Study Modules** (cross-linked modules `01` through `04` to form a cohesive, bi-directional network for Obsidian):
  - [01_kube_api_and_kubectl.md](file:///home/karim/Desktop/CKA/01_kube_api_and_kubectl.md) linked to `02_cluster_architecture_and_components.md`.
  - [02_cluster_architecture_and_components.md](file:///home/karim/Desktop/CKA/02_cluster_architecture_and_components.md) linked to `01_kube_api_and_kubectl.md`, `03_node_mechanics_and_resource_limits.md`, and `04_workload_lifecycle_and_healing.md`.
  - [03_node_mechanics_and_resource_limits.md](file:///home/karim/Desktop/CKA/03_node_mechanics_and_resource_limits.md) linked to `02_cluster_architecture_and_components.md` and `04_workload_lifecycle_and_healing.md`.
  - [04_workload_lifecycle_and_healing.md](file:///home/karim/Desktop/CKA/04_workload_lifecycle_and_healing.md) linked to `02_cluster_architecture_and_components.md` and `03_node_mechanics_and_resource_limits.md`.

---

## [Before 2026-05-27] - Initial Knowledge Base Creation

### Added
- **Core Study Modules:**
  - [01_kube_api_and_kubectl.md](file:///home/karim/Desktop/CKA/01_kube_api_and_kubectl.md) (API server, API Groups, explain, Watch, kubectl syntax, output formats).
  - [02_cluster_architecture_and_components.md](file:///home/karim/Desktop/CKA/02_cluster_architecture_and_components.md) (Control plane vs worker, etcd/scheduler/controllers, HA design, CCM, version skew proxy).
  - [03_node_mechanics_and_resource_limits.md](file:///home/karim/Desktop/CKA/03_node_mechanics_and_resource_limits.md) (Node conditions, leases/heartbeats, cgroups, QoS classes, container runtimes).
  - [04_workload_lifecycle_and_healing.md](file:///home/karim/Desktop/CKA/04_workload_lifecycle_and_healing.md) (Self-healing pillars, probes, garbage collection).
- **Core Index & Guide:**
  - [README.md](file:///home/karim/Desktop/CKA/README.md) containing the architectural Mermaid.js "Brain Map" and course indexes.
  - [instructions.md](file:///home/karim/Desktop/CKA/instructions.md) outlining standard ingestion and formatting guidelines.

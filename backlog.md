# CKA Knowledge Base Update Backlog

This backlog tracks all updates, modifications, and restructuring activities performed in this CKA study knowledge base.

---

## [2026-06-05] - Gitea Ingestion Crossover Audit & CKA Checklist Update

### Added
- **CKA Exam Checklist Expansion (`Projects/CKA/Exam Checklist - Core Architecture and API.md`):**
  - Appended **Systemd Service & Kubelet Debugging** guidelines (using `systemctl` status/restart, `journalctl -u kubelet -e` to read log ends, systemd daemon-reload commands, and swap/cgroup troubleshooting).
  - Appended **HostPath Volume & Directory Traversal Troubleshooting** guidelines (explaining how directory execute `x` permissions on the host affect containers, FACL `setfacl` permissions bypass, how symlinks resolve during `hostPath` mounting, and SELinux contexts).

### Audited
- Audited `Reference Notes/06_gitea_installation_and_workflows.md`, `Main Notes/gitea.md`, and `Digital Garden/Pattern - Air-Gapped Git Architecture on RHEL.md` to extract high-yield crossover topics related to Linux systemd services and directory traversal permissions for Kubernetes cluster administrator tasks.

---

## [2026-06-05] - Create Air-Gapped Git Architecture Pattern Note

### Added
- **Digital Garden Pattern Note (`Digital Garden/Pattern - Air-Gapped Git Architecture on RHEL.md`):** Created a cross-domain architectural pattern note connecting git, linux, and database domains, and components `[[gitea]]`, `[[mysql]]`, `[[lvm]]`, `[[systemd]]`, and `[[openssh]]`. Detailed the coordination of unprivileged execution, SSH forced-commands, LVM symlink routing, MySQL database tenant isolation, and `act_runner` native host execution. Provided security critique comparison tables and RHEL service unit configuration sheets.

---

## [2026-06-05] - Gitea Installation Security Audit Script

### Added
- **Gitea Verification Script (`Reference Notes/scripts/verify_gitea_setup.sh`):** Created a robust, production-grade bash verification audit script to inspect a RHEL 8 host and verify Gitea conforms to security and architectural guidelines (User verification, storage/symlink checks, root:git permission flags, FACL traversal permissions, Systemd variables validation, port binding checks, and SELinux contexts).
- **Audit Documentation Integration:** Appended Section 12 to `Reference Notes/06_gitea_installation_and_workflows.md` outlining the execution command and verification scope of the diagnostics script.

---

## [2026-06-05] - Gitea Reference Note Context Expansion Audit

### Refactored / Upgraded
- **Context Expansion Audit in Gitea Reference Note (`Reference Notes/06_gitea_installation_and_workflows.md`):**
  - **Apache Reverse Proxy Snippet:** Added full SSL virtual host configuration block on port `:444` using `ProxyPass`, `ProxyPassReverse`, and `ProxyPreserveHost` directives, with architectural explanations of path preservation (`nocanon`), host header forwarding, and client real IP tracking with Gitea config (`REVERSE_PROXY_LIMIT` and `TRUSTED_PROXIES`).
  - **LVM & lsblk Concepts:** Expanded physical storage concepts (PV, VG, LV) with a Mermaid diagram, and provided a detailed step-by-step CLI run sheet on RHEL 8 to identify, create, extend (`vgextend` / `lvextend`), and resize filesystems (`xfs_growfs` / `resize2fs`) online for `/app`.
  - **OpenSSH Daemon (sshd) Configuration:** Documented sshd service configurations (`/etc/ssh/sshd_config`), active parameters required for Gitea's SSH multiplexing (`PubkeyAuthentication` and `AuthorizedKeysFile`), directory/file permissions (`StrictModes`), and RHEL 8 SELinux policy contexts (`restorecon` and `ssh_home_t`).
  - **Native Host CI/CD Security:** Addressed security trade-offs of the native host executor (`:host`) compared to container environments, detailing potential RCE, privilege escalation, and resource exhaustion vectors alongside mitigation guidelines (running unprivileged, restricting sudoers, and setting Systemd resource limits).

---


## [2026-06-05] - Second Brain & Digital Garden Expansion

### Added
- **Gitea Reference Note:** Created `Reference Notes/06_gitea_installation_and_workflows.md` detailing air-gapped installation, SQLite vs MySQL decisions, LVM storage design with symlinks, OpenSSH multiplexing/forced command Git-over-SSH mechanics, act_runner configuration with native host executor, custom pre-receive hooks for branch naming rules, and active-passive disaster recovery rollback playbooks.
- **CKA Exam Core Checklist:** Created `Projects/CKA/Exam Checklist - Core Architecture and API.md` mapping etcd backup/restore, Kubelet static pods pathing, scheduler bypass (spec.nodeName & Binding API), health probes (Startup, Liveness, Readiness via Exec/HTTP/TCP), and local `crictl` & `journalctl` diagnostics.
- **Specialized Subagent Team:** Defined 5 custom AI subagents under the repository namespace:
  - `ResearchAgent` (`research_refinement`): Cleans and refines raw Gemini logs and transcripts into Reference Notes.
  - `AuditAgent` (`research_audit`): Audits reference notes, identifies tangent domains, and appends background/explanations to keep notes self-contained.
  - `MultiDomainPoCAgent` (`poc_developer`): Programs high-density, accurate, hands-on Verification PoCs in Reference Notes across all domains (Linux, AWS, Kubernetes, Databases, Networking).
  - `GardenAgent` (`garden_architect`): Cultivates the `Digital Garden/` and connects cross-domain components into patterns.
  - `CKAExamAgent` (`cka_exam_expert`): Condenses study materials into exam-focused checklists, mock reviews, and VIM setups inside `Projects/CKA/`.
- **Dedicated Digital Garden (`Digital Garden/`):** Created a root folder specifically for mapping domains and architectural patterns, and moved the `Pattern - Postgres on EKS.md` here.
- **Projects Directory (`Projects/`):** Created a project folder containing `Projects/CKA/` specifically for CKA Exam preparation.
- **CKA Exam Workspace Notes:** Created `Projects/CKA/Index.md` (exam MOC) and `Projects/CKA/Vim and Terminal Setup.md` (high-speed commands and configs).
- **Reference Notes Index (`Reference Notes/Index.md`):** Created a dynamic index MOC to list detailed study modules and PoCs.
- **Digital Garden Index (`Digital Garden/Index.md`):** Created a dynamic MOC table to list architectural patterns.
- **Dynamic MOC Indexes:** Updated `Main Notes/Index.md` to point its pattern queries to the new `Digital Garden/` directory.

### Refactored / Upgraded
- **Landing Notes Properties:** Refactored properties across all 11 landing notes using Python automation to inject `domains: ["kubernetes"]` and `against: []` (opposing ideas/approaches).
- **Agent Profile (`Agent.md`):** Updated definition to govern multi-domain Second Brain structures, diverse inflow tracking, dynamic Dataview query enforcement, and the sequential execution pipeline.
- **Ingestion Skill (`instructions.md`):** Updated templates to incorporate source provenance metadata (`source_type`, `source_url`, `author`, `course_title`), `against` properties, and the new Architectural Pattern note schema.
- **Ingestion Workflow Chaining:** Documented and configured the default sequential ingestion pipeline (`ResearchAgent` -> `AuditAgent` -> `MultiDomainPoCAgent` -> Concepts -> `GardenAgent` -> `CKAExamAgent`) in both `instructions.md` and `Agent.md` to trigger on every new note ingestion by default, ensuring that after the initial refinement, secondary domains are audited/expanded with volume by `AuditAgent`, before PoC, Main Notes, Digital Garden, and `CKAExamAgent` checklists are created.

---

## [2026-05-31] - Two-Tier Knowledge Vault Reorganization

### Added
- **MOC Index File (`Main Notes/Index.md`):** Created a central Map of Content (MOC) index note for unified conceptual navigation across landing and deeper dive notes.
- **Main Notes Directory (`Main Notes/`):** Created and refactored 11 atomic landing notes and 11 deeper technical sub-resource notes for core CKA concepts, structured with Obsidian-compliant YAML Properties (role, related_concepts, deeper_dives, sub_concepts, etc.) and breadcrumb links:
  - `kube-apiserver` (Deeper: request lifecycle, API Groups, OpenAPI schema, watch mechanism, proxy, ephemeral containers).
  - `etcd` (Deeper: Raft consensus quorum, ports, CLI usage, client certificate TLS args, CKA backup/restore steps).
  - `kube-scheduler` (Deeper: filtering predicates, ranking priorities, custom schedulers config, manual node binding bypass).
  - `kube-controller-manager` (Deeper: reconciliation loops, cascading deletions, node eviction parameters, leader election).
  - `cloud-controller-manager` (Deeper: out-of-tree providers, EXTERNAL cloud flags, route/service controllers).
  - `kubelet` (Deeper: TLS bootstrapping, node conditions, lease optimization, CRI socket integration, static pods directory).
  - `kube-proxy` (Deeper: service virtual entity, userspace/iptables/IPVS performance modes, CKA debug commands).
  - `container-runtime` (Deeper: CRI dual services, high vs low OCI/runc engines, shims, pause container, cgroup systemd driver alignment, ctr/nerdctl/crictl tools).
  - `kubectl` (Deeper: Kubeconfig components, dry-run template formulas, force deletion flags, custom-columns and JSONPath filtering).
  - `pod` (Deeper: lifecycle states, QoS memory/CPU eviction classifications, startup/liveness/readiness probes, native sidecars, lifecycle hooks).
  - `node` (Deeper: manual/dynamic registration, resource capacity vs allocatable calculations, cgroups v1 vs v2).
- **Raw Inflow Sources (`inflow/docs/`):** Uploaded 198 files across 17 folders representing raw Mumshad CKA course transcripts for future module ingestion.

### Moved / Reorganized
- **Reference Notes Directory (`Reference Notes/`):** Created directory and moved study modules `01` to `05` containing high-verbosity notes and kind cluster validation PoCs using `git mv`.
- **README.md:** Updated overview directory map to reflect the new main vs reference division and updated relative paths.
- **instructions.md:** Redefined the ingestion workflow to match the new two-tier standard, specifying landing and deeper note layouts and Obsidian linking rules.

---

## [2026-05-29] - Ingestion & Integration of Mumshad Course Transcripts

### Integrated
- **[01_kube_api_and_kubectl.md](01_kube_api_and_kubectl.md):** Integrated Kube API Server request lifecycle details (creation flow, auth, schemas, scheduling binding, Kubelet execution).
- **[02_cluster_architecture_and_components.md](02_cluster_architecture_and_components.md):** Expanded core control plane components:
  - **API Server:** Added configuration details, systemd vs. static pod manifest verification, and execution checking.
  - **ETCD:** Added SQL vs Key-Value context, client/peer communication ports (2379/2380), Raft consensus peer configs, API v2 vs v3 migration commands (`put` vs `set`, versioning), and TLS-authorized registry keys check command.
  - **Kube Scheduler:** Added Filtering (predicates) and Ranking (priorities) pipeline descriptions, multiple custom schedulers context, and verification paths.
  - **Kube Proxy:** Added Services as virtual memory routing tables, host-level `iptables`/`IPVS` redirection mechanisms, and DaemonSet deployment verification.
  - **Reference Table:** Compiled a unified configuration paths guide for all control plane and core components.
- **[03_node_mechanics_and_resource_limits.md](03_node_mechanics_and_resource_limits.md):** Integrated Kubelet host system agent specifics, manual installation instructions (downloading binary, systemd configurations), and process verification flags.
- **[05_containers_runtimes_and_lifecycle.md](05_containers_runtimes_and_lifecycle.md):** Consolidated container runtimes evolution:
  - **Evolution & Decoupling:** Added Docker platform components, Dockershim adapter deprecation history (removed in v1.24), and native CRI/cri-dockerd setups.
  - **CLI Tools Comparison:** Added comparison table for CTR (debugging containerd), NerdCTL (Docker-compatible containerd shell, eStargz lazy pulls, P2P, signing), and Crictl (CRI troubleshooting debugger, Pod listing, Kubelet GC warnings).
  - **Endpoints Socket Skew:** Added default socket checklist and session export configurations.

### Changed / Updated
- **Cross-Module Consistency:** Fixed broken links in Modules 01, 03, and 04 pointing to renamed headings in Module 02. Verified complete linkage vault compliance.
- **Git Synchronization:** Updated SSH configurations to route github.com over port 443 (via ssh.github.com) to resolve local port 22 blocks, and pushed all updates.

---

## [2026-05-29] - Ingestion & Consolidation of Container Mechanics

### Added
- **[05_containers_runtimes_and_lifecycle.md](05_containers_runtimes_and_lifecycle.md):** Compiled raw notes from `inflow/Containers.md` into a structured, production-grade guide covering OCI images, Kubelet-CRI architecture, process isolation topology via `RuntimeClass` and micro-virtualization overhead, custom container setup/shutdown hooks, standard and native sidecars, and `ephemeralContainers` process namespace target troubleshooting.
- **PoC Suite:** Created a complete hands-on verification pipeline inside Module 05 containing service links tests, log redirection hooks verification, native sidecar/init sequential boot order tests, and `/ephemeralcontainers` PID debugging.

### Changed / Updated
- **[README.md](README.md):** Updated search indexes and expanded the master Mermaid.js brain map to link CRI services, shims, runc execution paths, namespaces, probes, hooks, native sidecars, and runtime class constraints.
- **[instructions.md](instructions.md):** Updated to add Step 6 to the Ingestion & Consolidation Workflow, requiring all updates to be committed and pushed to `git@github.com:kmashour/BrainDump.git`.
- **Cross-Linking:** Added Obsidian graph references between Module 05 and Modules 01, 02, 03, and 04.
- **Git Synchronization:** Initialized local Git repository, set remote origin to `git@github.com:kmashour/BrainDump.git`, configured `.gitignore`, and force-pushed all current materials.

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

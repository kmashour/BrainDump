# CKA Knowledge Base Update Backlog

This backlog tracks all updates, modifications, and restructuring activities performed in this CKA study knowledge base.

---

## [2026-06-05] - Re-ingestion and Coverage Audit of Course Transcripts

### Ingested Inflow Sources
The following raw inflow source files from `inflow/docs/` and link logs in `inflow/` have been recursively audited, verified as integrated into reference modules 01-14, and marked as covered:
- `docs/01-Introduction/01-Course-Introduction.md`
- `docs/01-Introduction/02-Certification.md`
- `docs/02-Core-Concepts/01-Core-Concepts-Section-Introduction.md`
- `docs/02-Core-Concepts/02-Cluster-Architecture.md`
- `docs/02-Core-Concepts/03-Docker-vs-ContainerD.md`
- `docs/02-Core-Concepts/04-ETCD-For-Beginners.md`
- `docs/02-Core-Concepts/05-ETCD-in-Kubernetes.md`
- `docs/02-Core-Concepts/06-Kube-API-Server.md`
- `docs/02-Core-Concepts/07-Kube-Controller-Manager.md`
- `docs/02-Core-Concepts/08-Kube-Scheduler.md`
- `docs/02-Core-Concepts/09-Kubelet.md`
- `docs/02-Core-Concepts/10-Kube-Proxy.md`
- `docs/02-Core-Concepts/11-Pods.md`
- `docs/02-Core-Concepts/12-Practice-Test-Introduction.md`
- `docs/02-Core-Concepts/13-Practice-Test-PODs.md`
- `docs/02-Core-Concepts/14-ReplicaSets.md`
- `docs/02-Core-Concepts/15-Practice-Tests-ReplicaSet.md`
- `docs/02-Core-Concepts/16-Deployments.md`
- `docs/02-Core-Concepts/17-Practice-Tests-Deployments.md`
- `docs/02-Core-Concepts/18-Namespaces.md`
- `docs/02-Core-Concepts/19-Practice-Test-Namespaces.md`
- `docs/02-Core-Concepts/20-Services.md`
- `docs/02-Core-Concepts/21-Services-ClusterIP.md`
- `docs/02-Core-Concepts/22-Practice-Test-Services.md`
- `docs/02-Core-Concepts/23-Imperative-Commands-with-kubectl.md`
- `docs/02-Core-Concepts/24-Practice-Test-Imperative-Commands.md`
- `docs/02-Core-Concepts/25-Attachments.md`
- `docs/03-Scheduling/01-Scheduling-Section-Introduction.md`
- `docs/03-Scheduling/02-Manual-Scheduling.md`
- `docs/03-Scheduling/03-Practice-Test-Manual-Scheduling.md`
- `docs/03-Scheduling/04-Labels-and-Selectors.md`
- `docs/03-Scheduling/05-Practice-Test-Labels-and-Selectors.md`
- `docs/03-Scheduling/06-Taints-and-Tolerations.md`
- `docs/03-Scheduling/07-Practice-Test-Taints-and-Tolerations.md`
- `docs/03-Scheduling/08-Node-Selectors.md`
- `docs/03-Scheduling/09-Node-Affinity.md`
- `docs/03-Scheduling/10-Practice-Test-Node-Affinity.md`
- `docs/03-Scheduling/11.Taints-and-Tolerations-vs-Node-Affinity.md`
- `docs/03-Scheduling/12-Resource-Limits.md`
- `docs/03-Scheduling/13-Practice-Test-Resource-Limits.md`
- `docs/03-Scheduling/14-DaemonSets.md`
- `docs/03-Scheduling/15-Practice-Test-DaemonSets.md`
- `docs/03-Scheduling/16-Static-Pods.md`
- `docs/03-Scheduling/17-Practice-Test-StaticPods.md`
- `docs/03-Scheduling/18-Multiple-Schedulers.md`
- `docs/03-Scheduling/19-Practice-Test-Multiple-Schedulers.md`
- `docs/03-Scheduling/20-Configuring-Kubernetes-Schedulers.md`
- `docs/03-Scheduling/21-Download-Presentation-Deck.md`
- `docs/04-Logging-and-Monitoring/01-Logging-and-Monitoring-Section-Introduction.md`
- `docs/04-Logging-and-Monitoring/02-Monitor-Cluster-Components.md`
- `docs/04-Logging-and-Monitoring/03-Practice-Test-Monitor-Cluster-Components.md`
- `docs/04-Logging-and-Monitoring/04-Managing-Application-Logs.md`
- `docs/04-Logging-and-Monitoring/05-Download-Presentation-Deck.md`
- `docs/04-Logging-and-Monitoring/06-Practice-Test-Managing-Application-Logs.md`
- `docs/05-Application-Lifecycle-Management/01-Application-Lifecycle-Management--Section-Introduction.md`
- `docs/05-Application-Lifecycle-Management/02-RollingUpdates-and-Rollback.md`
- `docs/05-Application-Lifecycle-Management/03-Practice-Test-RollingUpdates-Rollback.md`
- `docs/05-Application-Lifecycle-Management/04-Commands-and-Arguments-in-Docker.md`
- `docs/05-Application-Lifecycle-Management/05-Commands-and-Arguments-in-Kubernetes.md`
- `docs/05-Application-Lifecycle-Management/06-Practice-Test-Commands-and-Arguments.md`
- `docs/05-Application-Lifecycle-Management/07.Configure-Environment-Variables-in-Applications.md`
- `docs/05-Application-Lifecycle-Management/08-Configure-ConfigMaps-in-Applications.md`
- `docs/05-Application-Lifecycle-Management/09-Practice-Test-Env-Variables.md`
- `docs/05-Application-Lifecycle-Management/10.Secrets.md`
- `docs/05-Application-Lifecycle-Management/11.Practice-Test-Secrets.md`
- `docs/05-Application-Lifecycle-Management/12.Multi-Containers-PODs.md`
- `docs/05-Application-Lifecycle-Management/13-Practice-Test-Multi-Container-Pods.md`
- `docs/05-Application-Lifecycle-Management/14-Multi-Container-Pods-Design-Patterns.md`
- `docs/05-Application-Lifecycle-Management/15.Init-Containers.md`
- `docs/05-Application-Lifecycle-Management/16-Practice-Test-Init-Containers.md`
- `docs/05-Application-Lifecycle-Management/17.Self-Healing-Applications.md`
- `docs/05-Application-Lifecycle-Management/18.Download-Presentation-Deck.md`
- `docs/06-Cluster-Maintenance/01-Cluster-Maintenance-Section-Introduction.md`
- `docs/06-Cluster-Maintenance/02-OS-Upgrades.md`
- `docs/06-Cluster-Maintenance/03-Practice-Test-OS-Upgrades.md`
- `docs/06-Cluster-Maintenance/04-Kubernetes-Software-Versions.md`
- `docs/06-Cluster-Maintenance/05-Cluster-Upgrade-Introduction.md`
- `docs/06-Cluster-Maintenance/06-Practice-Test-Cluster-Upgrade-Process.md`
- `docs/06-Cluster-Maintenance/07-Backup-and-Restore-Methods.md`
- `docs/06-Cluster-Maintenance/08-Working-With-ETCDCTL.md`
- `docs/06-Cluster-Maintenance/09-Practice-Test-Backup-and-Restore-Methods.md`
- `docs/06-Cluster-Maintenance/10-Practice-Test-Backup-and-Restore-Methods-2.md`
- `docs/06-Cluster-Maintenance/11-Download-Presentation-Deck.md`
- `docs/07-Security/01-Security-Section-Introduction.md`
- `docs/07-Security/02-Kubernetes-Security-Primitives.md`
- `docs/07-Security/03-Authentication.md`
- `docs/07-Security/04-TLS-Certificates.md`
- `docs/07-Security/05-TLS-Basics.md`
- `docs/07-Security/06-TLS-in-Kubernetes.md`
- `docs/07-Security/07-TLS-in-Kubernetes-Certificate-Creation.md`
- `docs/07-Security/08-View-Certificate-Details.md`
- `docs/07-Security/09-Certificate-Health-Check-Spreadsheet.md`
- `docs/07-Security/10-Practice-Test-View-Certificate-Details.md`
- `docs/07-Security/11-Certificate-API.md`
- `docs/07-Security/12-Practice-Test-Certificates-API.md`
- `docs/07-Security/13-kubeconfig.md`
- `docs/07-Security/14-Practice-Test-KubeConfig.md`
- `docs/07-Security/15-API-Groups.md`
- `docs/07-Security/16-Authorization.md`
- `docs/07-Security/17-RBAC.md`
- `docs/07-Security/18-Practice-Test-RBAC.md`
- `docs/07-Security/19-Cluster-Roles.md`
- `docs/07-Security/20-Practice-Test-Cluster-Roles.md`
- `docs/07-Security/21-Service-Account.md`
- `docs/07-Security/22-Practice-Test-Service-Accounts.md`
- `docs/07-Security/23-Image-Security.md`
- `docs/07-Security/24-Practice-Test-Image-Security.md`
- `docs/07-Security/25-Security-Context.md`
- `docs/07-Security/26-Practice-Test-Security-Context.md`
- `docs/07-Security/27-Network-Policies.md`
- `docs/07-Security/28-Practice-Test-Network-Policies.md`
- `docs/07-Security/29-kubectx-and-kubens-commands.md`
- `docs/07-Security/30-Download-Presentation-Deck.md`
- `docs/08-Storage/01-Storage-Section-Introduction.md`
- `docs/08-Storage/02-Introduction-to-Docker-Storage.md`
- `docs/08-Storage/03-Storage-in-Docker.md`
- `docs/08-Storage/04-Volume-Driver-Plugins-in-Docker.md`
- `docs/08-Storage/05-Container.Storage-Interface.md`
- `docs/08-Storage/06-Volumes.md`
- `docs/08-Storage/07-Persistent-Volumes.md`
- `docs/08-Storage/08-Persistent-Volume-Claims.md`
- `docs/08-Storage/09-Using-PVC-in-PODs.md`
- `docs/08-Storage/10-Practice-Test-Persistent-Volume-Claims.md`
- `docs/08-Storage/11-Download-Presentation-Deck.md`
- `docs/08-Storage/12-Storage-Class.md`
- `docs/08-Storage/13-Practice-Test-Storage-Class.md`
- `docs/09-Networking/01-Networking-Introduction.md`
- `docs/09-Networking/02-Pre-requisite-Switching-Routing-Gateways.md`
- `docs/09-Networking/03-Pre-requisite-DNS.md`
- `docs/09-Networking/04-Pre-requisite-CoreDNS.md`
- `docs/09-Networking/05-Pre-requisite-Network-Namespace.md`
- `docs/09-Networking/06-Pre-requisite-Docker-Networking.md`
- `docs/09-Networking/07-Pre-requisite-CNI.md`
- `docs/09-Networking/08-Cluster-Networking.md`
- `docs/09-Networking/09-Practice-Test-Explore-Env.md`
- `docs/09-Networking/10-Pod-Networking.md`
- `docs/09-Networking/11-CNI-in-Kubernetes.md`
- `docs/09-Networking/12-CNI-weave.md`
- `docs/09-Networking/13-Practice-Test-CNI-weave.md`
- `docs/09-Networking/14-Practice-Test-Deploy-Network-Solution.md`
- `docs/09-Networking/15-ipam-weave.md`
- `docs/09-Networking/16-Practice-Test-Networking-weave.md`
- `docs/09-Networking/17-Service-Networking.md`
- `docs/09-Networking/18-Practice-Test-Service-Networking.md`
- `docs/09-Networking/19-DNS-in-kubernetes.md`
- `docs/09-Networking/20-CoreDNS-in-Kubernetes.md`
- `docs/09-Networking/21-Practice-Test-CoreDNS-in-Kubernetes.md`
- `docs/09-Networking/22-Ingress.md`
- `docs/09-Networking/23-Ingress-Annotations-and-rewrite-target.md`
- `docs/09-Networking/24-Practice-Test-CKA-Ingress-Net-1.md`
- `docs/09-Networking/25-Practice-Test-CKA-Ingress-Net-2.md`
- `docs/09-Networking/26-Dowload-Presentation-Deck.md`
- `docs/10-Design-and-Install-Kubernetes-Cluster/01-Designing-a-Kubernetes-Cluster.md`
- `docs/10-Design-and-Install-Kubernetes-Cluster/02-Choosing-Kubernetes-Infrastructure.md`
- `docs/10-Design-and-Install-Kubernetes-Cluster/03-Configure-High-Availability.md`
- `docs/10-Design-and-Install-Kubernetes-Cluster/04-ETCD-in-HA.md`
- `docs/10-Design-and-Install-Kubernetes-Cluster/05-Important-update-kubernetes-the-hard-way.md`
- `docs/10-Design-and-Install-Kubernetes-Cluster/06-Download-Presentation-Deck.md`
- `docs/11-Install-Kubernetes-the-kubeadm-way/01-Introduction-to-Deployment-with-kubeadm.md`
- `docs/11-Install-Kubernetes-the-kubeadm-way/02-Resources.md`
- `docs/11-Install-Kubernetes-the-kubeadm-way/03-Provision-VMs-with-Vagrant.md`
- `docs/11-Install-Kubernetes-the-kubeadm-way/04-Demo-Deployment-with-Kubeadm.md`
- `docs/11-Install-Kubernetes-the-kubeadm-way/05-Practice-Test-Deploy-Kubernetes-Cluster-using-Kubeadm.md`
- `docs/12-Troubleshooting/01-Troubelshooting-Section-Introduction.md`
- `docs/12-Troubleshooting/02-Application-Failure.md`
- `docs/12-Troubleshooting/03-Solution-Application-Failure.md`
- `docs/12-Troubleshooting/04-Control-Plane-Failure.md`
- `docs/12-Troubleshooting/05-Practice-Test-Control-Plane-Failure.md`
- `docs/12-Troubleshooting/06-Solution-Control-Plane-Failure.md`
- `docs/12-Troubleshooting/07-Worker-Node-Failure.md`
- `docs/12-Troubleshooting/08-Practice-Test-Worker-Node-Failure.md`
- `docs/12-Troubleshooting/09-Solution-Worker-Node-Failure.md`
- `docs/12-Troubleshooting/10-Practice-Test-Troubleshoot-Network.md`
- `docs/13-Other-Topics/01-Labs-JSON-PATH.md`
- `docs/13-Other-Topics/02-Pre-Requisites-JSON-PATH.md`
- `docs/13-Other-Topics/03-Advance-Kubectl-Commands.md`
- `docs/13-Other-Topics/04-Practice-Test-Advance-Kubectl-Commands.md`
- `docs/14-Lightning-Labs/01-Lightning-Labs-Introduction.md`
- `docs/14-Lightning-Labs/02-Lightning-Lab-1.md`
- `docs/15-Mock-Exams/01-Introduction.md`
- `docs/15-Mock-Exams/02-Mock-Exam-1.md`
- `docs/15-Mock-Exams/03-Mock-Exam-2.md`
- `docs/15-Mock-Exams/04-CKA-MockExam-2-Solution.md`
- `docs/15-Mock-Exams/05-Mock-Exam-3.md`
- `docs/15-Mock-Exams/06-CKA-MockExam-3-Solution.md`
- `docs/16-Ultimate-Mocks/02-Troubleshooting/README.md`
- `docs/16-Ultimate-Mocks/02-Troubleshooting/docs/11-C1-orange-pvc-cka13-trb.md`
- `docs/16-Ultimate-Mocks/02-Troubleshooting/docs/19-C1-netpol-cyan-pod-cka28-trb.md`
- `docs/16-Ultimate-Mocks/04-Storage/README.md`
- `docs/16-Ultimate-Mocks/04-Storage/docs/10-CI-olive-pvc-cka10-str.md`
- `docs/16-Ultimate-Mocks/05-Services-Networking/README.md`
- `docs/16-Ultimate-Mocks/05-Services-Networking/docs/03-C3-External-Webserver.md`
- `docs/16-Ultimate-Mocks/09-general/README.md`
- `docs/16-Ultimate-Mocks/09-general/docs/01-cluster-state-questions.md`
- `docs/16-Ultimate-Mocks/README.md`
- `docs/17-tips-and-tricks/README.md`
- `docs/17-tips-and-tricks/docs/01-server-for-testing-network-policies.md`
- `docs/17-tips-and-tricks/docs/02-client--for-testing-network-things.md`

---


## [2026-06-05] - Ingest ReplicaSets, API Merging, ETCD Client Management and Container Runtime Socket Updates

### Added
- **ReplicaSets Concept Deep Dive (`Main Notes/replicaset - MatchExpressions and Thrashing.md`):** Created a new deeper dive note detailing set-based selectors syntax, ownership/adoption mechanics, and troubleshooting scenarios for ReplicaSet thrashing loops (overlapping selectors and mutating webhook issues).

### Changed / Updated
- **Container Runtimes Reference Module (`Reference Notes/05_containers_runtimes_and_lifecycle.md`):** Ingested raw Mumshad transcripts to document Dockershim removal, the `cri-dockerd` adapter socket mechanics, manual Kubelet configuration, and the "Container Runtime Upgrade Trap" (Kubelet gRPC re-dial errors resolved via service restart).
- **Workloads & Controllers Reference Module (`Reference Notes/07_kubernetes_workloads_and_controllers.md`):** Integrated set-based selector operators, `ownerReferences` mechanics (adoption and orphaning), API validation safeguards, and advanced thrashing loop diagnostics.
- **Cluster Maintenance & ETCD Reference Module (`Reference Notes/11_maintenance_upgrades_and_etcd.md`):** Expanded details on ETCD client API v2 vs v3 management, persistent session configurations, and command-line syntax comparison.
- **API Management Reference Module (`Reference Notes/13_kubernetes_api_management_and_pod_immutability.md`):** Detailed the Mixed-Management Warning and the 2-Way Merge Fallback blind spot (where deletions fail due to missing last-applied-configuration annotations) and auto-recovery annotation patching.
- **Main Note (`Main Notes/kubectl - Declarative vs Imperative and 3-Way Merge.md`):** Added a dedicated section detailing the Mixed-Management Warning, 2-Way Merge Fallback mechanics, and auto-recovery annotation injection.
- **Main Note (`Main Notes/etcd-deeper.md`):** Appended section on ETCD client CLI version management (v2 vs v3) and operation commands cheat sheet.
- **Main Note (`Main Notes/container-runtime-deeper.md`):** Appended section on Dockershim deprecation, `cri-dockerd` adapter socket details, modern socket config requirements, and Kubelet service upgrade traps.
- **Exam Checklist (`Projects/CKA/Exam Checklist - Core Architecture and API.md`):** Integrated Dockershim removal milestones, `cri-dockerd` socket locations, the Container Runtime Upgrade Kubelet restart trap, and the 2-Way Merge Fallback blind spot / auto-recovery explanation.
- **Exam Checklist (`Projects/CKA/Exam Checklist - Workloads and Scheduling.md`):** Appended a new section detailing ReplicaSets matchExpressions, adoption/orphaning, API validation webhook checks, and thrashing loops (overlapping selectors and webhook interference).

### Ingested Inflow Sources
The following raw inflow source files have been fully ingested and integrated:
- `3wayMergevs2wayMergeKubernetes.md`
- `DockerVsContainerD_Mumshad.md`
- `KubernetesPracticalTips.md`
- `ReplicasetsNotesCKA.md`
- `dockerdepraction_mumshad.md`
- `etcd_mumshad.md`
- `kubeProxy_mumshad.md`
- `kube_apiserver_mumshad.md`
- `kubelete_mumshad.md`
- `scheduler_mumshad.md`


---

## [2026-06-05] - Create Scheduling and Lifecycle Verification PoC

### Added
- **Validation Script (`Reference Notes/scripts/verify_scheduling_lifecycle_poc.sh`):** Created a production-grade bash verification script that automates Node Labeling/Selector/Affinity, Taints/Tolerations, ConfigMap/Secret volume mount sync and env injection, and logging/monitoring audits against a local cluster.

### Changed / Updated
- **Scheduling, Logging, and Lifecycle Reference Module (`Reference Notes/14_scheduling_logging_and_lifecycle.md`):** Integrated Phase 4 documentation detailing the automated verification script, its functionality, and commands on how to run it.

---

## [2026-06-05] - Context Expansion Audit of Scheduling, Logging, and Lifecycle Reference Module

### Changed / Updated
- **Scheduling, Logging, and Lifecycle Reference Module (`Reference Notes/14_scheduling_logging_and_lifecycle.md`):**
  - **ConfigMap Symlink & inotify Sync Mechanics:** Expanded the ConfigMap/Secret volume mounts section. Detailed Kubelet's atomic directory update mechanism (timestamped subdirectories, user-facing symlinks, and the atomic swap of the `..data` symlink). Documented inotify event propagation inside containers (directory-level vs. file-level watches). Explained the `subPath` inode binding gotcha which binds directly to a file inode, preventing the container from receiving updates when the symlink target changes.
  - **ETCD Encryption Verification & Envelope Encryption:** Detailed the ETCD encryption at rest mechanism. Contrasted static providers (`identity`, `aescbc`, `secretbox`) with external KMS envelope encryption (DEK/KEK generation, remote gRPC plugin calls, local caches). Provided a step-by-step diagnostic run sheet to SSH into the control plane node, query the raw secret directly using `etcdctl` with client certificates, and verify it contains the `k8s:enc:aescbc:v1:` prefix.
  - **Custom Scheduler Reconciliation Loop & Binding API Walkthrough:** Expanded the multiple custom schedulers section. Provided a detailed step-by-step explanation of the reconciliation loop (Watch/Informer, Queueing, Filtering/Predicates, Scoring/Priorities, Selection, Binding) with a Mermaid flow diagram. Included complete, practical script implementations in Python (using the official `kubernetes` client library) and Bash (using `kubectl` and `curl` against the `/binding` subresource API) demonstrating how to programmatically schedule pending pods.

---

## [2026-06-05] - Create Scheduling, Logging, and Lifecycle Reference Module

### Added
- **Scheduling, Logging, and Lifecycle Reference Module (`Reference Notes/14_scheduling_logging_and_lifecycle.md`):** Compiled raw log transcripts into a highly structured, comprehensive reference module covering Advanced Scheduling and Node Placement (Manual scheduling, labels/selectors, taints/tolerations, node affinity, taints vs affinity combinations, and multiple custom schedulers), Logging and Monitoring (Metrics Server architecture, Kubelet Summary API, and application logs queries), and Application Lifecycle (container commands/arguments overriding, environment variables direct config, envFrom, valueFrom, ConfigMaps, Secrets, base64 encoding/decoding, and etcd encryption at rest).

---

## [2026-06-05] - CKA Exam Checklist Updates for API Management & Pod Immutability

### Changed / Updated
- **Exam Checklist - Core Architecture and API (`Projects/CKA/Exam Checklist - Core Architecture and API.md`):**
  - Added Section 6 covering **Kubernetes API Management & Validation**.
  - Documented how to bypass client-side pre-flight schema validations using `--validate=false` to work around version skew or caching issues.
  - Documented the `last-applied-configuration` mixed-management warning context, why it occurs, and how to ignore/resolve it using Server-Side Apply (`--server-side`).
- **Exam Checklist - Troubleshooting and Networking (`Projects/CKA/Exam Checklist - Troubleshooting and Networking.md`):**
  - Updated Section 1.3 to add the **`kubectl edit` & Temp File Recovery Playbook** for Pod spec immutability failures.
  - Provided the step-by-step workflow using `kubectl replace --force -f /tmp/kubectl-edit-xxxx.yaml`.
  - Explained the underlying process signal mechanics (`SIGKILL` vs `SIGTERM`) and immediate container namespace/cgroup teardown.


## [2026-06-05] - Cross-Domain Pattern Note Integration of API Management & Pod Immutability

### Changed / Updated
- **Digital Garden Pattern Note (`Digital Garden/Pattern - Stateful Database Clustering in Kubernetes.md`):**
  - Added section **Linux Process Signals & cgroup Eviction Mechanics in Databases**: Documented the cross-domain interactions between Kubernetes lifecycle events and Linux kernel mechanisms. Detailed graceful shutdown (`SIGTERM`/Signal 15) vs. immediate force deletion (`SIGKILL`/Signal 9) process flows and their impact on database WAL files, transaction logs, and replica coordination. Detailed Completely Fair Scheduler (CFS) bandwidth quotas and the Out-of-Memory (OOM) killer scoring adjustments (`oom_score_adj` mapping from Guaranteed, Burstable, and BestEffort QoS classes) in relation to container cgroups.
  - Updated frontmatter sources to include `Reference Notes/13_kubernetes_api_management_and_pod_immutability.md`.
- **Digital Garden Pattern Note (`Digital Garden/Pattern - Air-Gapped Git Architecture on RHEL.md`):**
  - Added section **GitOps Declarative Workflows & API Reconciliation Mechanics**: Connected the air-gapped version control server (Gitea) and host runner (`act_runner`) to declarative Kubernetes management. Detailed the client-side pre-flight validation cache and version skew issues, the 3-Way Merge Engine mechanics (role of `last-applied-configuration` annotation in tracking and processing field deletions), Server-Side Apply (SSA) (field ownership conflict resolutions under `metadata.managedFields`, and solving etcd metadata size constraints for large CRDs), and Pod spec immutability boundaries requiring the `/tmp/kubectl-edit-xxxx.yaml` recovery playbook using `kubectl replace --force` (triggering immediate cgroup teardown and container namespace unmounting via `SIGKILL`).
  - Updated frontmatter domains, components, sources, and tags to include `kubernetes`, `kubectl`, `pod`, `Reference Notes/13_kubernetes_api_management_and_pod_immutability.md`, and `kubernetes/gitops`.
  - Added references to the bottom of the note for `Reference Notes/13_kubernetes_api_management_and_pod_immutability.md` and `Reference Notes/scripts/verify_api_immutability.sh`.

---

## [2026-06-05] - Context Expansion Audit of API Management & Pod Immutability Reference Module

### Changed / Updated
- **API Management & Pod Immutability Reference Module (`Reference Notes/13_kubernetes_api_management_and_pod_immutability.md`):**
  - Expanded **Client-Side vs. Server-Side Validation**: Documented how `kubectl` validates manifests locally using Cached OpenAPI schemas (under `~/.kube/cache/schema`), how version skew and Custom Resource Definitions (CRDs) affect validation, and how `--validate=false` can bypass local pre-flight checks.
  - Expanded **Server-Side Apply (SSA)**: Added deep-dive explanations of Server-Side Apply (SSA) introduced as the default mechanism in v1.22+. Detailed field ownership tracking with `metadata.managedFields`, conflict detection, and how it resolves the metadata storage constraints of the `last-applied-configuration` annotation in `etcd`.
  - Expanded **Linux Process Signal Mechanics during Force Deletion**: Documented process-level behavior difference between graceful termination (SIGTERM, grace period countdown, and escalation to SIGKILL) and forceful deletion (immediate SIGKILL, grace-period=0, immediate cgroup and namespace cleanup).

---

## [2026-06-05] - Create API Management and Pod Immutability Reference Module

### Added
- **API Management & Pod Immutability Reference Module (`Reference Notes/13_kubernetes_api_management_and_pod_immutability.md`):** Compiled raw log transcripts into a highly structured reference module covering Declarative vs. Imperative Object Management (operational tradeoffs, exam vs. production workflows), the 3-Way Merge Engine (merge logic, the role of `last-applied-configuration` annotation in deletions, mixed-management warnings), Pod Immutability rules (reasons for immutability, exact mutable fields), and the `/tmp/kubectl-edit-xxxx.yaml` recovery workflow utilizing `kubectl replace --force`.
- **Validation Script (`Reference Notes/scripts/verify_api_immutability.sh`):** Created a programmatic verification script that automates the deployment, dry-run annotation check, immutability rejection validation, and the forceful recovery procedure.

---

## [2026-06-05] - Create CKA Exam Checklists

### Added
- **CKA Exam Checklist - Cluster Maintenance and Installation (`Projects/CKA/Exam Checklist - Cluster Maintenance and Installation.md`):** Created a targeted CKA study guide covering node maintenance (draining, cordoning), sequential upgrades using kubeadm (for master and worker nodes), and ETCD snapshot backup/restoration playbooks (for stacked and external topologies).
- **CKA Exam Checklist - Security and Storage (`Projects/CKA/Exam Checklist - Security and Storage.md`):** Created a targeted CKA study guide covering RBAC (Role, RoleBinding, ClusterRole, ClusterRoleBinding, and auth can-i permissions testing), Kubeconfig context configuration, ServiceAccount token automount policies, SecurityContext permissions, NetworkPolicy selector logic (AND/OR), and PV/PVC/StorageClass binding and reclaiming rules.
- **CKA Exam Checklist - Troubleshooting and Networking (`Projects/CKA/Exam Checklist - Troubleshooting and Networking.md`):** Created a targeted CKA study guide covering Pod troubleshooting workflows (CrashLoopBackOff, ImagePullBackOff, etc.), control plane and static pod failure diagnostics, worker node systemd/Kubelet config fixes, crictl socket auditing, cluster networking, service routing, CoreDNS troubleshooting, and Ingress path-rewriting.

---

## [2026-06-05] - Update and Create Pattern Notes

### Changed / Updated
- **Digital Garden Pattern Note (`Digital Garden/Pattern - Postgres on EKS.md`):** Updated the Postgres on EKS pattern note to integrate dynamic storage class mechanics (`volumeBindingMode: WaitForFirstConsumer`), pod-level TLS/SSL certificate generation using the Kubernetes Certificates API (`CertificateSigningRequest`), and L7 Ingress path-based routing (Nginx Ingress controller path matching and rewrite-target annotation).

### Added
- **Digital Garden Pattern Note (`Digital Garden/Pattern - CoreDNS Latency and Search Paths.md`):** Created a new pattern note describing the cross-domain interactions between the Linux resolver (`glibc`/`/etc/resolv.conf`), `ndots:5` search paths, and CoreDNS. Documented the latency amplification problem when querying external hosts, detailed mitigation alternatives (absolute names with trailing dot, Pod `dnsConfig` overrides, and NodeLocal DNSCache), and provided verification guides.
- **Digital Garden Pattern Note (`Digital Garden/Pattern - Automated ETCD Backups on Control Plane Hosts.md`):** Created a new pattern note outlining how control plane hosts run automated, secure ETCD snapshot backups. Evaluated the circular dependency vulnerability of Kubernetes-native `CronJobs` versus local host-level `systemd` timers and services, and provided a production-ready systemd configuration and backup shell script with retention rotation.

---

## [2026-06-05] - Create Security and Network Policies Reference Module

### Added
- **Kubernetes Security and Network Policies Reference Module (`Reference Notes/08_security_and_network_policies.md`):** Compiled a highly structured, comprehensive, and exhaustive Reference Module covering Kubernetes Security Primitives and Authentication (human vs. machine accounts, basic/token auth deprecation), TLS Basics & TLS in K8s (manual generation of CA, admin, apiserver, and kubelet certificates using openssl and cfssl, Subject Alternative Names, auditing certificate files), Certificates API (CertificateSigningRequest resources, spec.signerName values for v1, approval workflow, and Kubelet TLS bootstrapping), Kubeconfig (clusters, users, contexts structure, file merging), Authorization modes (Node, ABAC, RBAC, Webhook, AlwaysAllow/AlwaysDeny), RBAC (Role, RoleBinding, ClusterRole, ClusterRoleBinding, namespace scope, and kubectl auth can-i permission testing), ServiceAccounts (projected tokens, TokenRequest API v1.22+, manual secret-based token generation for v1.24+), Image Security (private registry credentials, docker-registry secrets, and ImagePullSecrets), SecurityContexts (Pod-level and Container-level users, groups, and Linux capabilities), and NetworkPolicies (Ingress/Egress, podSelector, namespaceSelector, ipBlock, and AND vs OR rules logic).

---

## [2026-06-05] - Create Storage Mechanics and CSI Reference Module

### Added
- **Storage Mechanics & CSI Reference Module (`Reference Notes/09_storage_mechanics_and_csi.md`):** Compiled a highly structured, comprehensive, and exhaustive Reference Module covering Container Storage Interface (CSI) architecture (Kubelet coordination, node vs. controller plugins, driver registration, sidecars), volume primitives (`emptyDir` and `hostPath` configurations, security risks, systemd/SELinux permissions, scheduling disconnects), PV and PVC mechanics (binding, access modes, reclaim policies, protection finalizers), Pod volume mounts, and StorageClasses (dynamic provisioning, `WaitForFirstConsumer` topology-aware scheduling, provisioners, online expansion).
- **Automated Verification Script (`Reference Notes/scripts/verify_storage_poc.sh`):** Created a production-grade bash verification script to test shared `emptyDir` mounts, `WaitForFirstConsumer` pending-to-bound transitions, and PVC deletion protection finalizers.

---

## [2026-06-05] - Create Networking, DNS, and Ingress Reference Module

### Added
- **Kubernetes Networking Reference Module (`Reference Notes/10_networking_dns_and_ingress.md`):** Created a comprehensive, production-grade study and reference module. Structured to cover Networking Prerequisites (Switching, routing, gateways, network namespaces, veth pairs, Linux bridge, NAT/MASQUERADE, DNAT), CNI specifications and host configurations (kubelet integration, plugins directory), Cluster & Pod networking (IPAM, WeaveNet overlay mechanism), Service networking (ClusterIP, NodePort, LoadBalancer routing, iptables vs IPVS proxy modes), DNS in Kubernetes (CoreDNS architecture, Corefile config, Pod/Service FQDN formats, /etc/resolv.conf search domains), and Ingress (Controllers vs Resources, routing patterns, SSL/TLS termination, rewrite-target annotations, networking.k8s.io/v1 templates).

---

## [2026-06-05] - Create Cluster Maintenance, Upgrades, and ETCD Reference Module

### Added
- **Reference Module (`Reference Notes/11_maintenance_upgrades_and_etcd.md`):** Compiled raw log transcripts into a highly structured, comprehensive reference module covering Node Maintenance (draining, cordoning), version skew policies, step-by-step kubeadm upgrade playbooks, ETCD snapshot backups and restores (for stacked and external topologies), High-Availability cluster architectures (stacked vs. external ETCD), and cluster bootstrapping using kubeadm with containerd systemd cgroups configurations.

---

## [2026-06-05] - Create Troubleshooting and Diagnostics Reference Note

### Added
- **Kubernetes Troubleshooting & Diagnostics Reference Note (`Reference Notes/12_troubleshooting_and_diagnostics.md`):** Compiled raw log transcripts into a highly structured, comprehensive Reference Module. The document covers:
  1. Troubleshooting Application Failures: Pod phases, logs, previous logs, health probes (Startup, Liveness, Readiness), Service Endpoints, and standalone pod re-creation.
  2. Troubleshooting Control Plane Failures: Static Pod manifest auditing, Systemd service logs, and ETCD endpoint health and membership checks.
  3. Troubleshooting Worker Node Failures: Node conditions, Kubelet systemd services and configuration fixes, CRI socket auditing, and container runtime investigations using `crictl`.
  4. Troubleshooting Cluster Networking: CNI configuration/binary checks, Service routing and `kube-proxy` daemonset/iptables auditing, and CoreDNS lookups with dnsutils.
  5. Advanced Kubectl Usage: JSONPATH syntax and query snippets, Custom Columns formatting, Resource Sorting (`--sort-by`), and Filtering using label and field selectors.

---


## [2026-06-05] - Create Workloads and Scheduling Exam Checklist

### Added
- **CKA Exam Checklist (`Projects/CKA/Exam Checklist - Workloads and Scheduling.md`):** Created a highly targeted study guide and checklist covering Pod YAML generation/modifications, health probes, deployment rollouts/rollbacks, DaemonSet migration steps, static pods management, jobs/cronjobs config, and StatefulSet database clustering.

---

## [2026-06-05] - Create Stateful Database Clustering Pattern Note

### Added
- **Digital Garden Pattern Note (`Digital Garden/Pattern - Stateful Database Clustering in Kubernetes.md`):** Created a cross-domain architectural pattern note connecting domains `kubernetes`, `networking`, `database`, and `linux`, and components `[[statefulset]]`, `[[pod]]`, `[[node]]`, and `[[container-runtime]]`. Detailed how StatefulSet ordinals, headless services, CoreDNS records, PVC templates, and local storage (LVM/hostPath) coordinate to host clustered stateful databases. Included a Mermaid sequence diagram for network pathing/DNS replication sync, a comparison of StatefulSets vs. Bare-metal VMs, local vs. remote storage, readiness probe impacts, and manual/automated verification guides.

---

## [2026-06-05] - Create Kubernetes Workloads Verification PoC Script

### Added
- **Workload & Controller Verification Script (`Reference Notes/scripts/verify_workloads_poc.sh`):** Created a production-grade automated verification script to validate multi-container IPC patterns, localhost network port sharing, native gRPC probes, and StatefulSet headless DNS architectures.
- **Verification Script Documentation (`Reference Notes/07_kubernetes_workloads_and_controllers.md`):** Appended Section 13.7 documenting the verification script scope, execution instructions, and clean-up options.

---

## [2026-06-05] - Kubernetes Workloads & Controllers Reference Note Expansion

### Refactored / Upgraded
- **Context Expansion Audit in Workloads & Controllers Reference Note (`Reference Notes/07_kubernetes_workloads_and_controllers.md`):**
  - **Linux Namespaces & Cgroups (CRI/OCI Level):** Added detailed architectural explanations for kernel namespaces (`net`, `ipc`, `pid`, `mnt`, `uts`, `user`). Documented the hierarchy and structural differences between cgroups v1 and v2. Explained resource constraints mapping to Completely Fair Scheduler (CFS) bandwidth quotas/periods and OOM killer score adjustment math (`oom_score_adj`) across QoS classes.
  - **Shared Pod IPC & Unix Sockets:** Documented container-to-container communication mechanics. Included complete, runnable YAML configurations for loopback port sharing and shared Unix domain sockets using `emptyDir` mounts.
  - **StatefulSet DNS & CoreDNS Resolution:** Documented the CoreDNS mapping mechanisms (A and SRV records) for StatefulSets. Provided a detailed troubleshooting run sheet using network debugging tools (`nslookup`, `dig`, `host`).
  - **gRPC Health Probe Protocol:** Explained protocol specifications for native gRPC probes, including the `grpc.health.v1.Health` service definition, Kubelet interaction mechanics, and success/failure criteria. Updated the reference YAML config to show gRPC health probes.

---

## [2026-06-05] - Create Kubernetes Workloads & Controllers Reference Module

### Added
- **Kubernetes Workloads & Controllers Reference Module (`Reference Notes/07_kubernetes_workloads_and_controllers.md`):** Created a comprehensive, production-grade study and reference module. Structured to cover Pods (Sandbox creation, namespace sharing), Pod Lifecycle (Phases, states, CrashLoopBackOff, conditions, readiness gates, hooks), Init and Native Sidecar containers (Resource calculations, sequencing, teardown), Ephemeral containers (kubectl debug), Health Probes (Liveness, Readiness, Startup, HTTP/TCP/Exec/gRPC handlers), Static Pods (configurations, mirror pods), ReplicaSets, Deployments (RollingUpdate, Recreate strategies, rollbacks), StatefulSets (Headless Services, stable identities, Volume Claim Templates), DaemonSets, and Jobs/CronJobs. Included a complete verification run sheet of kubectl commands.

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

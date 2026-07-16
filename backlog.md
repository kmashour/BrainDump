# CKA Knowledge Base Update Backlog

This backlog tracks all updates, modifications, and restructuring activities performed in this CKA study knowledge base.

## [2026-07-16] - Ingestion & Integration: AWS & Terraform Core & GitHub Actions Basics to Production

### Refactored / Upgraded
- **Reference Notes (AWS & Terraform Core):**
  - [[Reference Notes/10-1_terraform_foundations_and_state.md|Module 10-1: Terraform Foundations & State Management]]: Integrated core Terraform engine architecture (Directed Acyclic Graph), AWS provider credential authentication precedence, remote backend migration setups with S3 and DynamoDB write locking, directory best practices, local/remote provisioners, and legacy vs modern declarative import blocks.
  - [[Reference Notes/10-2_variables_types_and_expressions.md|Module 10-2: Variables, Types & Expression Syntax]]: Integrated input variable precedence hierarchy and custom validation blocks, homogeneous collections (lists vs sets) and heterogeneous structural objects, ternary conditionals, splat expressions, dynamic blocks iteration loops, built-in functions categories, and dynamic data sources querying.
  - [[Reference Notes/10-3_meta_arguments_lifecycle_and_state.md|Module 10-3: Meta-Arguments, Lifecycle Control & State Ops]]: Integrated list index shifting issues under count vs. key-value map boundaries inside for_each loops, explicit depends_on dependencies, and zero-downtime swaps via create_before_destroy, prevent_destroy, and ignore_changes.
  - [[Reference Notes/10-4_networking_website_and_security.md|Module 10-4: Networking, Static Website Hosting & Security Architecture]]: Integrated private S3 buckets with CloudFront OAC policies, VPC Peering requester/accepter connection routing, IAM programmatic user and group creation, and multi-tier scalable ASG/ALB clusters (2-Tier and 3-Tier topologies).
  - [[Reference Notes/10-5_modules_eks_and_serverless.md|Module 10-5: Production Architecture: Modules, EKS & Serverless]]: Integrated Elastic Beanstalk Blue-Green deployment models, serverless image processing event-driven pipelines (S3 triggers Lambda), and custom EKS modular architectures with IRSA OIDC mapping.
  - [[Reference Notes/10-6_cicd_gitops_observability_and_drift.md|Module 10-6: Enterprise CI/CD, Observability, GitOps & Drift Remediation]]: Integrated AWS CloudWatch agent setups (hypervisor vs OS metrics), HCP Terraform workspaces vs directories, GitHub Actions pipelines using OIDC trust, GitOps application sync via ArgoCD, and scheduled drift detection using detailed exit codes.
  - [[Reference Notes/3-2_aws_iam.md|Module 3-2: AWS IAM & Identity Management]]: Appended Terraform resource primitives for programmatic IAM users, groups, attachments, and AWS Organizations SCP configurations.
  - [[Reference Notes/3-6_aws_s3_storage.md|Module 3-6: AWS S3 Storage]]: Appended Terraform resource primitives for standard S3 buckets (versioning, encryption, block public access) and static website configurations.
  - [[Reference Notes/3-9_aws_vpc_networking.md|Module 3-9: AWS VPC Networking]]: Appended Terraform resource primitives for VPC Peering network routing.
  - [[Reference Notes/3-13_aws_cloudfront_cdn.md|Module 3-13: AWS CloudFront CDN & AWS Global Accelerator]]: Appended Terraform resource primitives for CloudFront distribution setups and Origin Access Control.
  - [[Reference Notes/3-18_serverless.md|Module 3-18: AWS Serverless]]: Appended Terraform resource primitives for Lambda function executions, roles, and S3 event triggers.
- **Reference Notes (GitHub Actions Basics to Production):**
  - [[Reference Notes/9-1_github_actions_architecture_and_workflows.md|Module 9-1: GitHub Actions Architecture & Workflow Design]]: Integrated core runner VM sandboxing, explicit checkout logic, outbound long-polling connectivity, custom trigger types, event filters (wildcards/globs), reusable actions, version pinning, Flask container build/push project, execution vm concurrency/parallelism logic, concurrent push event vm scaling scenarios, jobs vs steps execution trade-offs, and containerized job volume mounts.
  - [[Reference Notes/9-2_github_actions_advanced_execution.md|Module 9-2: Advanced Pipeline Control & Execution]]: Integrated orchestrator compile-time expressions vs runner VM runtime shell variables, general-purpose and status functions, inputs/outputs propagation across jobs and reusable workflows, artifacts archiving, dependency caching lookup rules (`hashFiles`), fail-fast matrix strategies, `fromJSON`/`toJSON` boundary serialization rules, dynamic matrices setup, access control contains gates, endsWith commit skip null-safety check workarounds, fine-grained `needs.<job_id>.result` Boolean evaluation logic vs job-level `continue-on-error`, and deferred failure script patterns.
  - [[Reference Notes/9-3_github_actions_administration_and_security.md|Module 9-3: Runner Administration & Pipeline Hardening]]: Integrated environment-scoped variables and deployment protection gates (reviews, timers), GITHUB_TOKEN scope hardening, secretless OpenID Connect (OIDC) JWT token exchange with AWS IAM, self-hosted runner systemd service installation, comparative architectural table of GHA vs Jenkins, concurrency grouping keys preventing deployment race conditions, and persistent VM state "dirty state" risks and mitigations.

### Ingested Inflow Sources
Processed and integrated the following files in `inflow/`:
- `inflow/Github-Actions-Notes.md`
- `inflow/Day 0—Learn AWS With Terraform in 30 Days (with real-time projects).txt`
- `inflow/130 - How Does Terraform Work  Intro to IAC.txt`
- `inflow/230 - Terraform AWS Provider explained.txt`
- `inflow/330 -  Create an AWS S3 Bucket Using Terraform (it's simple).txt`
- `inflow/430 - Terraform State file management with AWS S3  Remote Backend.txt`
- `inflow/530 - Terraform Variables in AWS - Input vs Output vs Local Variables.txt`
- `inflow/630 - AWS Terraform Project Structure Best Practices.txt`
- `inflow/730 - AWS Terraform Type Constraints Explained (with realtime examples).txt`
- `inflow/830 - AWS Terraform Meta Arguments Made EASY  Count, depends_on , for_each.txt`
- `inflow/930 - AWS Terraform Lifecycle Rules Explained.txt`
- `inflow/1030 - AWS Terraform  Conditional Expressions , Splat Expressions and Dynamic Block.txt`
- `inflow/1130 - AWS Terraform Functions - Part 1.txt`
- `inflow/1230 - AWS Terraform Functions - Part 2.txt`
- `inflow/1330 - Terraform Data Source AWS Explained (with demo).txt`
- `inflow/1430 - Host A Static Website In AWS S3 And Cloudfront (using terraform).txt`
- `inflow/1530 -  AWS VPC Peering Using Terraform - Mini project.txt`
- `inflow/1630 - AWS IAM User Management with Terraform - Mini Project.txt`
- `inflow/1730 - AWS Terraform Blue-Green Deployment Using Elastic Beanstalk.txt`
- `inflow/1830 - Image Processing Serverless Project using AWS Lambda(with terraform).txt`
- `inflow/1930 - Terraform Provisioners (with demo) - local vs remote vs file.txt`
- `inflow/2030 - Terraform Custom Modules for EKS - From Zero to Production.txt`
- `inflow/2130 - AWS Policy and Governance Setup Using Terraform.txt`
- `inflow/Day 2230 - 2-Tier Architecture Setup on AWS Using Terraform.txt`
- `inflow/2330 - Setup End-to-End Observability in AWS Using Terraform (Real-Time Project).txt`
- `inflow/2430 - Highly Available and Scalable Architecture Using Terraform.txt`
- `inflow/2530 - Terraform Import In AWS Explained With Demo.txt`
- `inflow/2630 - HCP Terraform Explained with Demo - Terraform Projects and Workspaces.txt`
- `inflow/2730 - Automate AWS Infra Using Terraform and GitHub Actions  Realtime Project.txt`
- `inflow/2830 - AWS 3-tier Architecture With Terraform  End-to-End Real-Time Project.txt`
- `inflow/2930 - End-to-end GitOps With Terraform and ArgoCD For EKS  Production-grade Kubernetes Project.txt`
- `inflow/3030 - Drift Detection and Remediation Using Terraform and GitHub Actions  Real Time Project.txt`
- `inflow/What is GitHub Actions  Build Your First Workflow from Scratch.txt`
- `inflow/GitHub Actions Triggers & Runners Explained  Events, Contexts & Hosted Runners.txt`
- `inflow/Build Your First Production-Style Workflow with GitHub Actions.txt`
- `inflow/GitHub Actions Workflow Logic Explained  Filters, Contexts, Variables & Expressions.txt`
- `inflow/GitHub Actions Functions Explained  Build a Production-Style CI Pipeline.txt`
- `inflow/GitHub Actions Outputs Explained  Step, Job & Reusable Workflow Outputs.txt`
- `inflow/GitHub Actions Artifacts & Caching Explained  Share Files & Optimize Builds.txt`
- `inflow/GitHub Actions Matrix Strategy Explained  Multi-OS, Multi-Version Testing at Scale.txt`
- `inflow/GitHub Actions Environments Explained  Variables, Secrets, Approvals & Protection Rules.txt`
- `inflow/GitHub Actions Inputs Explained  Workflow Inputs, Reusable Workflows & Production Use Cases.txt`
- `inflow/GithubAction-Elfakharny.md`
- `inflow/GitHub-Actions-Basics-To-Production-main/01-GitHub-Actions/README.md`
- `inflow/GitHub-Actions-Basics-To-Production-main/02-Workflow-Triggers/README.md`
- `inflow/GitHub-Actions-Basics-To-Production-main/03-Actions/README.md`
- `inflow/GitHub-Actions-Basics-To-Production-main/04-Filters-Variables-Expressions-Contexts/README.md`
- `inflow/GitHub-Actions-Basics-To-Production-main/05-Functions/README.md`
- `inflow/GitHub-Actions-Basics-To-Production-main/06-Inputs/README.md`
- `inflow/GitHub-Actions-Basics-To-Production-main/07-Outputs/README.md`
- `inflow/GitHub-Actions-Basics-To-Production-main/08-Artifacts-&-Caching/README.md`
- `inflow/GitHub-Actions-Basics-To-Production-main/09-Matrix-Strategy/README.md`
- `inflow/GitHub-Actions-Basics-To-Production-main/10-Environments/README.md`

---

## [2026-07-15] - Ingestion & Integration: GitHub Actions Deep Dive (Course Transcripts)

### Integrated / Upgraded
- **Reference Notes:**
  - [[Reference Notes/9-1_github_actions_architecture_and_workflows.md|Module 9-1: GitHub Actions Architecture & Workflow Design]]: Integrated basic workflow creation, Docker Hub secure authentication publishing, job/step status check conditional logic, manual parameters, tags triggers, runner VM sizes, and system contexts.
  - [[Reference Notes/9-2_github_actions_advanced_execution.md|Module 9-2: Advanced Pipeline Control & Execution]]: Integrated step/job/workflow outputs mapping, reusable workflows (`workflow_call`) parameters and secret inheritances, dependency caching key restoral prefixes, and parallel matrix customization (`include`/`exclude`).
  - [[Reference Notes/9-3_github_actions_administration_and_security.md|Module 9-3: Runner Administration & Pipeline Hardening]]: Integrated environment-scoped secret variables precedence hierarchy, manual required reviewer approvals, wait timers, and deployment branch restrictions.

### Ingested Inflow Sources
Processed and integrated the following files in `inflow/`:
- `inflow/What is GitHub Actions  Build Your First Workflow from Scratch.txt`
- `inflow/GitHub Actions Triggers & Runners Explained  Events, Contexts & Hosted Runners.txt`
- `inflow/Build Your First Production-Style Workflow with GitHub Actions.txt`
- `inflow/GitHub Actions Workflow Logic Explained  Filters, Contexts, Variables & Expressions.txt`
- `inflow/GitHub Actions Functions Explained  Build a Production-Style CI Pipeline.txt`
- `inflow/GitHub Actions Outputs Explained  Step, Job & Reusable Workflow Outputs.txt`
- `inflow/GitHub Actions Artifacts & Caching Explained  Share Files & Optimize Builds.txt`
- `inflow/GitHub Actions Matrix Strategy Explained  Multi-OS, Multi-Version Testing at Scale.txt`
- `inflow/GitHub Actions Environments Explained  Variables, Secrets, Approvals & Protection Rules.txt`
- `inflow/GitHub Actions Inputs Explained  Workflow Inputs, Reusable Workflows & Production Use Cases.txt`

---


## [2026-07-13] - Ingestion & Restructuring: Local Storage Models, Provisioners & Scheduling Traps

### Added
- **Reference Notes:**
  - [[Reference Notes/0-8-a_local_storage_models_and_scheduling_traps.md|0-8-a_local_storage_models_and_scheduling_traps.md]]: Created standalone reference note detailing the differences between CSI and StorageClass, the three local storage models (`hostPath`, static `local` volumes, dynamic `local-path`), and the `WaitForFirstConsumer` volume binding mode.
- **Projects:**
  - [[Projects/CKA/Project - Local Storage Models and Scheduling Traps.md|Project - Local Storage Models and Scheduling Traps.md]]: Created CKA-focused hands-on project to simulate local storage provisioning and the scheduling affinity deadlock failure loop.
- **Main Notes:**
  - [[Main Notes/storageclass - Volume Binding Modes and Scheduling Traps.md|storageclass - Volume Binding Modes and Scheduling Traps.md]]: Created deeper-dive note documenting the immediate binding trap and `WaitForFirstConsumer` scheduling coordination.

### Refactored / Upgraded
- **Reference Notes:**
  - [[Reference Notes/0-Index - Kubernetes.md|0-Index - Kubernetes.md]]: Indexed the new local storage models lecture note under Domain 5.
- **Main Notes:**
  - [[Main Notes/storageclass.md|storageclass.md]]: Linked the new reference guide.
  - [[Main Notes/persistentvolume.md|persistentvolume.md]]: Linked the new reference guide.
  - [[Main Notes/hostpath.md|hostpath.md]]: Linked the new reference guide.
- **Digital Garden:**
  - [[Digital Garden/Pattern - Stateful Database Clustering in Kubernetes.md|Pattern - Stateful Database Clustering in Kubernetes.md]]: Updated Section 5 and frontmatter to reference the new local storage models reference and project notes.
- **Projects:**
  - [[Projects/CKA/Practice Playbook - Topic Labs.md|Practice Playbook - Topic Labs.md]]: Added Q4 to the Storage section pointing to the scheduling deadlock simulation project.
  - [[Projects/CKA/Exam Checklist - Security and Storage.md|Exam Checklist - Security and Storage.md]]: Added CKA exam tip and troubleshooting commands for local storage scheduling traps.

### Ingested Inflow Sources
Processed and integrated the following file from `inflow/`:
- `inflow/StorageNotes.md`

---

## [2026-07-12] - Ingestion & Enhancement: Node Joins, SecurityContexts, CKA Debugging & TLS/mTLS Mechanics

### Added
- **Reference Notes:**
  - [[Reference Notes/0-10-a_vagrant_vm_provisioning_lecture.md|0-10-a_vagrant_vm_provisioning_lecture.md]]: Created standalone reference note detailing the VirtualBox/Vagrant VM local environment provisioning workflow.
  - [[Reference Notes/0-10-b_kubeadm_cluster_bootstrapping_lecture.md|0-10-b_kubeadm_cluster_bootstrapping_lecture.md]]: Created standalone reference note detailing bootstrapping a cluster (cgroup setup, kubeadm init, Flannel CNI, and worker joins).
  - [[Reference Notes/0-7-a_tls_and_mtls_handshake_troubleshooting_lecture.md|0-7-a_tls_and_mtls_handshake_troubleshooting_lecture.md]]: Created standalone reference note detailing the Kubelet-to-APIServer TLS and mTLS handshake, cryptographic verification (hashing, signatures, CA certificates), Subject Alternative Names (SANs) constraints, and /etc/hosts name resolution during bootstrap.

### Refactored / Upgraded
- **Reference Notes:**
  - [[Reference Notes/0-3_node_mechanics_and_resource_limits.md|0-3_node_mechanics_and_resource_limits.md]]: Expanded Section 1.B.4 to include a detailed explanation of the **Kubeadm Join Handshake**, detailing discovery token verification, bootstrap authentication, TLS bootstrapping, node registration, and adding a detailed Mermaid sequence diagram mapping the handshake.
  - [[Reference Notes/0-7_security_and_network_policies.md|0-7_security_and_network_policies.md]]:
    - Expanded Section 7 to clarify ServiceAccount mounting rules, namespace scoping, Pod exclusivity, and default token auto-mounting.
    - Added Sections 9.3, 9.4, and 9.5 covering **`fsGroup` Volume Mechanics** across storage types, **Kernel Tuning via safe/unsafe `sysctls`** contrasted with Linux Capabilities, and a deep-dive on **Linux Bind Mounts (`hostPath`), Symlink path breaks inside containers, and Symlink directory deletion permissions**.
  - [[Reference Notes/0-Index - Kubernetes.md|0-Index - Kubernetes.md]]: Indexed Vagrant, Kubeadm, and TLS/mTLS troubleshooting lecture notes.
  - [[Reference Notes/0-10_maintenance_upgrades_and_etcd.md|0-10_maintenance_upgrades_and_etcd.md]]: Linked both new lectures from the main cluster bootstrapping playbook section.
  - [[Reference Notes/0-11_troubleshooting_and_diagnostics.md|0-11_troubleshooting_and_diagnostics.md]]: Expanded Kubelet API Server port configuration error troubleshooting block, detailing local `/etc/hosts` name resolution success, the TLS SAN validation trap, and multi-network routing conflicts.

### Ingested Inflow Sources
Processed and integrated the following files from `inflow/`:
- `inflow/Some-KubernetesQuestions.md`
- `inflow/Vagrant_ForKubeAdm.md`
- `inflow/SettingUpwithKubeAdm.md`
- `inflow/CKA-Notes.md`

---

## [2026-07-11] - Ingestion & Enhancement: PV/PVC Parameter Mirroring & Storage Mechanics

### Refactored / Upgraded
- **Reference Notes:**
  - [[Reference Notes/0-8_storage_mechanics_and_csi.md|0-8_storage_mechanics_and_csi.md]]: 
    - Expanded section 1.E to detail CSI Control Plane sidecars and Worker Node components, adding a Mermaid diagram and Phase-by-Phase lifecycle.
    - Elaborated on Section 2.B.3 regarding Linux host execution permissions (`x`) directory traversal mechanics, non-root user UID conflicts (e.g. `0700` vs. runAsUser), error symptoms, and remediation methods (initContainers vs `fsGroup` limitations on `hostPath`).
    - Added Section 3.G covering **Volume Node Affinity (Topology-Aware Scheduling)**, explaining `.spec.nodeAffinity` on Local PVs, why PVCs do not have affinity, the root cause of `volume node affinity conflict` pending states, and a Q&A on local storage, nodeAffinity, and PVC selectors.
    - Integrated a detailed conceptual Q&A breakdown in Section 3.A explaining why PV and PVC parameters (Reclaim Policy, Capacity, Access Modes) do not need to mirror each other exactly, detailing the **1:1 Binding Lock & Wasted Capacity** constraint, the **Pod perspective (`df -h`)** showing full backing disk size, and adding a parameter match grid table.

### Ingested Inflow Sources
Processed and integrated the following file from `inflow/`:
- `inflow/PVC-PV-Example.md`

---

## [2026-07-11] - Ingestion: GitHub Actions Platform Fundamentals (Elfakharny Lecture)

### Added
- **Reference Notes:**
  - [[Reference Notes/9-4_github_actions_lecture_elfakharny.md|9-4_github_actions_lecture_elfakharny.md]]: Compiled, translated, and structured the raw Arabic speech-to-text transcript into a technical English reference module covering CI/CD principles, event triggers, YAML syntax, billing calculations, and Enterprise topologies.

### Refactored / Upgraded
- **Main Notes:**
  - [[Main Notes/github-actions.md|github-actions.md]]: Linked Module 9-4 under Deeper Dive Notes.
- **Reference Notes:**
  - [[Reference Notes/9-Index - GitHub Actions.md|9-Index - GitHub Actions.md]]: Indexed Module 9-4.
  - [[Reference Notes/9-1_github_actions_architecture_and_workflows.md|9-1_github_actions_architecture_and_workflows.md]]: Added source reference to Module 9-4.

### Ingested Inflow Sources
Processed and integrated the following file from `inflow/`:
- `inflow/GithubAction-Elfakharny.md`

---

## [2026-07-11] - Ingestion: Ingress Controllers & Services Networking

### Refactored / Upgraded
- **Main Notes:**
  - [[Main Notes/ingress.md|ingress.md]]: Enriched with core controller components (ConfigMap, ServiceAccount, Deployment, Service) and path/host rule examples, linking to Module 0-9.
- **Reference Notes:**
  - [[Reference Notes/0-9_networking_dns_and_ingress.md|0-9_networking_dns_and_ingress.md]]: Appended IngressController lecture transcript, inflow Services-Load Balancing-Networking note, and all 10 scraped official sub-links (Service, Ingress, DNS, EndpointSlices, Gateway API, NetworkPolicies) to the Sources list.

### Ingested Inflow Sources
Processed and integrated the following files from `inflow/`:
- `inflow/IngressController.md`
- `inflow/Services-Load Balancing-Networking.md`

---

## [2026-07-10] - Ingestion: Secrets Systems Rationale, Types & Update Propagation

### Refactored / Upgraded
- **Main Notes:**
  - [[Main Notes/secret.md|secret.md]]: Updated with 1MiB size limitations, Immutable secrets (`immutable: true`), and ServiceAccount Token Projection vs. legacy token secrets.
  - [[Main Notes/secret - Encryption at Rest and Ingestion.md|secret - Encryption at Rest and Ingestion.md]]: Integrated sections detailing built-in Secret types (basic-auth, ssh-auth, tls, dockerconfigjson, bootstrap token) and update propagation mechanics (static env vars, symlink-swap mounts, and the `subPath` gotcha).
- **Reference Notes:**
  - [[Reference Notes/0-13_scheduling_logging_and_lifecycle.md|0-13_scheduling_logging_and_lifecycle.md]]: Added Section 3's *Systems Rationale* subsection detailing Kubelet's atomic symlink-swap pattern, kernel-level atomic symlinks, multi-file consistency, active file descriptor inode locks, and read-only mount namespaces boundaries.

### Ingested Inflow Sources
Processed and integrated the following files from `inflow/`:
- `inflow/Secrets.md`
- `inflow/A Note on Secrets.md`

---

## [2026-07-07] - Ingestion: Helm Package Management & Release Lifecycles

### Added
- **Main Notes:**
  - [[Main Notes/helm.md|helm.md]]: Landing note for the Helm package manager.
- **Reference Notes:**
  - [[Reference Notes/12-3_helm_package_management.md|12-3_helm_package_management.md]]: Module 12-3 detailing Helm 3 client-side architecture, 3-way strategic merge patch, CLI command cheatsheet, and Chart structure.

### Refactored / Upgraded
- **Reference Notes:**
  - [[Reference Notes/0-Index - Kubernetes.md|0-Index - Kubernetes.md]]: Added Module 12-3 reference mapping under Domain 2 API extensibility.
  - [[Reference Notes/12-Index - CNCF References.md|12-Index - CNCF References.md]]: Listed Module 12-3 under CNCF Reference Modules.
  - [[Reference Notes/0-CKA Study Alignment Guide.md|0-CKA Study Alignment Guide.md]]: Mapped Helm section to syllabus table and Study Pathway Step 4.3.
- **Main Notes:**
  - [[Main Notes/0-CKA Study Roadmap.md|0-CKA Study Roadmap.md]]: Integrated Helm reference link.
- **Projects:**
  - [[Projects/CKA/Practice Playbook - Lightning Labs and Mock Exams.md|Practice Playbook - Lightning Labs and Mock Exams.md]]: Expanded Section 3 with values overrides, rollbacks, and local untar operations.

### Ingested Inflow Sources
Processed and integrated the following files from `inflow/`:
- `inflow/CustomizingChartParameters.md`
- `inflow/HelmCharts.md`
- `inflow/HelmComponents.md`
- `inflow/HelmIntroduction.md`
- `inflow/LifeCycleManagementWithHelm.md`
- `inflow/NoteOnHelm2vsHelm3.md`
- `inflow/WorkingWithHelmBasics.md`

---

## [2026-07-07] - Ingestion: CKA Networking Primitives & Gateway API Deep Dive

### Added
- **Main Notes:**
  - [[Main Notes/gateway-api - Advanced Traffic Routing.md|gateway-api - Advanced Traffic Routing.md]] (Deeper dive note on Gateway API standard configs: redirect, URLRewrite rewrite, header modification, mirroring, gRPC, and L4 listeners)

### Refactored / Upgraded
- **Reference Notes:**
  - [[Reference Notes/0-9_networking_dns_and_ingress.md|0-9_networking_dns_and_ingress.md]]:
    - Section 1.4: Added netmask configuration warning.
    - Section 1.5: Added firewall/iptables forward chain troubleshooting.
    - Section 10: Expanded Gateway API specs (Kustomize/Helm installation, RequestRedirect, URLRewrite, RequestHeaderModifier, RequestMirror filters, gRPC HTTPRoute, and L4 TCP/UDP listener configurations).
- **Main Notes:**
  - [[Main Notes/0-CKA Study Roadmap.md|0-CKA Study Roadmap.md]]: Integrated Gateway API Advanced Routing concept link.
- **Projects:**
  - [[Projects/CKA/Exam Checklist - Troubleshooting and Networking.md|Exam Checklist - Troubleshooting and Networking.md]]: Added controller logs verify, filters validation, and port binding diagnostics.

### Ingested Inflow Sources
Processed and integrated the following files from `inflow/`:
- `inflow/CNI-InKuberntes.md`
- `inflow/Cluster-Networking.md`
- `inflow/CoreDNS.md`
- `inflow/DNS in Kubernetes.md`
- `inflow/DNS-Kubernetes-reqw.md`
- `inflow/Docker-NetworkingForKubernets.md`
- `inflow/GatewayAPI.md`
- `inflow/GatewayAPINotes.md`
- `inflow/IPAM.md`
- `inflow/Ingress Notes.md`
- `inflow/IngressControllers.md`
- `inflow/Namespace-kubernetes-note.md`
- `inflow/Network-NameSpaces-Kuberentes.md`
- `inflow/Networking.md`
- `inflow/PodNetworking.md`
- `inflow/Pre-requisites-kubernetes-Gateways-switching.md`
- `inflow/Pre-requistes-CNI.md`
- `inflow/Service-Networking.md`

---

## [2026-07-05] - Ingestion: ETCD Port Roles and APIServer Watch Concurrency

### Refactored / Upgraded
- **Reference Notes:**
  - [[Reference Notes/0-10_maintenance_upgrades_and_etcd.md|0-10_maintenance_upgrades_and_etcd.md]]: Added Section 4.2.1 detailing the client, peer, and metrics ports and loopback vs routable IPs, and why the API Server opens dozens of simultaneous connections.
- **Main Notes:**
  - [[Main Notes/etcd-deeper.md|etcd-deeper.md]]: Expanded Section 2 with Port 2381 and api-server connections details.
- **Projects:**
  - [[Projects/CKA/Exam Checklist - Cluster Maintenance and Installation.md|Exam Checklist - Cluster Maintenance and Installation.md]]: Added Section 3.1.1 on ETCD network ports and API server connection pooling.

### Ingested Inflow Sources
Processed and integrated the following file from `inflow/`:
- `inflow/Some notes on networking.md`

---

## [2026-07-05] - Ingestion: CNI Specification Categories and Docker Networking Under the Hood

### Added
- **Main Notes:**
  - [[Main Notes/cni - Specification vs Plugins.md|cni - Specification vs Plugins.md]] (Deeper dive note clarifying CNI API specs vs plugin implementation binaries)

### Refactored / Upgraded
- **Reference Notes:**
  - [[Reference Notes/0-9_networking_dns_and_ingress.md|0-9_networking_dns_and_ingress.md]]: Expanded Section 2 with a new Subsection 2.0 (CNI Specification vs CNI Plugins), outlining vanilla vs managed defaults, building block CNI binaries, full solutions, and tunneling protocols.
  - [[Reference Notes/2-4_docker_networking_and_compose.md|2-4_docker_networking_and_compose.md]]: Added Section 1.1 (Bridge Networking Mechanics Under the Hood), detailing bridge creation commands, veth pair integration, the namespace directory Lookup hack, and NAT forwarding NAT rules.
- **Main Notes:**
  - [[Main Notes/docker - Networking Primitives.md|docker - Networking Primitives.md]]: Expanded with under-the-hood details on bridge switch setups, veth pairing, namespace hacks, and iptables nat forwards.
- **Study Guide:**
  - [[Main Notes/0-CKA Study Roadmap.md|0-CKA Study Roadmap.md]]: Integrated CNI Specification vs Plugins concept note.

### Ingested Inflow Sources
Processed and integrated the following files from `inflow/`:
- `inflow/CNI and Plugins Kubernetes.md`
- `inflow/Docker-Networking.md`

---

## [2026-07-05] - Ingestion: CNI Overlay Networks and IPAM Delegation

### Added
- **Main Notes:**
  - [[Main Notes/cni.md|cni.md]] (Landing note for Container Network Interface)
  - [[Main Notes/cni - Overlay Networks and Encapsulation.md|cni - Overlay Networks and Encapsulation.md]] (Deeper dive on VXLAN/UDP overlay encapsulation vs Calico BGP direct routing)
  - [[Main Notes/cni - IP Address Management (IPAM).md|cni - IP Address Management (IPAM).md]] (Deeper dive on decentralized PodCIDR delegation and host-local allocations)
- **Digital Garden:**
  - [[Digital Garden/Pattern - Cloud Provider Network Routing and CNI Encapsulation Bypasses.md|Pattern - Cloud Provider Network Routing and CNI Encapsulation Bypasses.md]] (Cross-domain pattern note mapping CNI overlays, AWS VPC source/dest checks, BGP peering, and AWS VPC CNI)

### Refactored / Upgraded
- **Reference Notes:**
  - [[Reference Notes/0-9_networking_dns_and_ingress.md|0-9_networking_dns_and_ingress.md]]: Expanded Section 3.2 (IPAM) to detail PodCIDR delegation hierarchy, subnet sizing formulas, and Kubelet maxPods constraints. Expanded Section 3.3 (CNI) to document SDN flat switch concepts, overlay encapsulation, and BGP naked routing. Added Mermaid diagrams for both sections.
- **Study Guide:**
  - [[Main Notes/0-CKA Study Roadmap.md|0-CKA Study Roadmap.md]]: Integrated CNI and its sub-notes into the Cluster Networking path.
- **Projects:**
  - [[Projects/CKA/Exam Checklist - Troubleshooting and Networking.md|Exam Checklist - Troubleshooting and Networking.md]]: Expanded Section 4.1 to cover local IPAM paths, Kube-Controller-Manager CIDR flags, and CNI log audits.

### Ingested Inflow Sources
Processed and integrated the following files from `inflow/`:
- `inflow/Kubernetes_Ovelay_Networks_vs_CalicoL3_CNI.md`
- `inflow/Networking_KuberentesIPAM.md`

---

## [2026-06-27] - Ingestion: CSR Workflows, Groups, and Vim/Tmux Speed Setup

### Added
- **Main Notes:** Created [[Main Notes/rbac - CertificateSigningRequests and Groups.md|rbac - CertificateSigningRequests and Groups.md]] deeper-dive note explaining CSR submission states, `signerName` departments, Extended Key Usages (EKU) validations, and token/cert Organization group mappings.

### Refactored / Upgraded
- **Reference Notes:**
  - Expanded Section 3 "Certificates API" in [[Reference Notes/0-7_security_and_network_policies.md|0-7_security_and_network_policies.md]] with granular details on usages constraints, TLS OID extensions, and group binding logic.
  - Expanded [[Projects/CKA/Vim and Terminal Setup.md|Vim and Terminal Setup.md]] to add high-speed string editing shortcuts (`C`, `D`, `daw`, `diw/diW`), Vim split escape remaps (`tnoremap`/`nnoremap`), and a Tmux split-pane configuration guide (mouse mode, scrolling, and Shift-highlight copy/paste workarounds).

### Ingested Inflow Sources
Processed and integrated the following file from `inflow/`:
- `Notes_On_CSRLABs.md`

---

## [2026-06-26] - Ingestion: CKA mTLS Diagnostics & SAN Troubleshooting

### Refactored / Upgraded
- **Reference Notes:**
  - Expanded [[Reference Notes/0-7_security_and_network_policies.md|0-7_security_and_network_policies.md]] to incorporate:
    - Detailed two-phase mTLS authentication breakdown (Phase 1 client-side SAN matching vs Phase 2 server-side authorization check).
    - Diagnostic symptoms for `x509: certificate is valid for...` SAN mismatches under external Load Balancer or Elastic IP setups.
    - CLI commands for boot-time `kubeadm` extra SAN overrides and post-install ConfigMap modification and certificate regeneration workflows.

### Ingested Inflow Sources
Processed and integrated the following file from `inflow/`:
- `More_Notes_On_MTLS_steps.md`

---

## [2026-06-26] - Ingestion: CKA ETCD Private CA Architecture

### Refactored / Upgraded
- **Reference Notes:**
  - Expanded [[Reference Notes/0-7_security_and_network_policies.md|0-7_security_and_network_policies.md]] to incorporate the architectural explanation of the separate Private Root CA for ETCD and the "Dual-Citizen" API server configuration bridging the isolated security domains.

### Ingested Inflow Sources
Processed and integrated the following file from `inflow/`:
- `CKA_ETCD_PrivateCA.md`

---

## [2026-06-26] - Ingestion: CKA Labs, Exams, and Conclusion Transcript

### Refactored / Upgraded
- **Projects & Playbooks:**
  - Expanded [[Projects/CKA/Practice Playbook - Lightning Labs and Mock Exams.md|Practice Playbook - Lightning Labs and Mock Exams.md]] to add Section 5 ("Ultimate Mock Exams & High-Density Exam Scenarios"):
    - Documented multi-cluster context management (`kubectl config use-context`) and boundary traversal commands.
    - Added Horizontal Pod Autoscaler (HPA) specifications detailing CPU target utilization and the scaleDown stabilization window.
    - Added Vertical Pod Autoscaler (VPA) autoscaling auto update mode configs.
    - Documented Gateway API resource schemas for modern routing configurations.
    - Compiled quick-fire troubleshooting playbooks for base64 secret decoding, local package runtime installation (`cri-docker` via `dpkg`), init container command spelling typo recoveries, custom NodePort service maps, PersistentVolume hostPath setups, and CRD listing and sorting filters.
    - Documented Helm repository updating and release version upgrades.

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/cka_split/`:
- `17_labs_exams_and_conclusion.txt`

---

## [2026-06-26] - Ingestion: CKA Troubleshooting Transcript

### Refactored / Upgraded
- **Reference Notes:**
  - Expanded [[Reference Notes/0-11_troubleshooting_and_diagnostics.md|0-11_troubleshooting_and_diagnostics.md]] to incorporate two-tier application troubleshooting checklists, Namespace context switching tricks, control plane failures for `kube-scheduler` and `kube-controller-manager` static pods, and a step-by-step query construction flow for JSONPath/Custom Columns.
  - Expanded [[Reference Notes/0-1_kube_api_and_kubectl.md|0-1_kube_api_and_kubectl.md]] to document `alias k=kubectl` and shell autocomplete setup for CKA efficiency.

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/cka_split/`:
- `16_troubleshooting.txt`

---

## [2026-06-26] - Ingestion: CKA Kustomize Basics Transcript

### Refactored / Upgraded
- **Reference Notes:**
  - Expanded [[Reference Notes/0-6_kubernetes_workloads_and_controllers.md|0-6_kubernetes_workloads_and_controllers.md]] to incorporate Kustomize concepts:
    - Added conceptual comparison matrix between Helm (template-based) and Kustomize (overlay-based).
    - Documented common transformers: `namespace`, `namePrefix`/`nameSuffix`, `commonLabels`, and `commonAnnotations`.
    - Detailed surgical modification types: Strategic Merge Patches and JSON 6902 Patches (op: add/remove/replace).

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/cka_split/`:
- `15_kustomize_basics.txt`

---

## [2026-06-26] - Ingestion: CKA Helm Basics Transcript

### Refactored / Upgraded
- **Reference Notes:**
  - Expanded [[Reference Notes/0-6_kubernetes_workloads_and_controllers.md|0-6_kubernetes_workloads_and_controllers.md]] to incorporate Helm 2 vs. Helm 3 evolution details:
    - Added security architecture details on Tiller removal and direct local `kubeconfig` client-side authentication.
    - Documented the Three-Way Strategic Merge Patch mechanism comparing recorded template state, target template state, and running cluster live state.

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/cka_split/`:
- `14_helm_basics.txt`

---

## [2026-06-26] - Ingestion: CKA Cluster HA and Bootstrapping Transcript

### Refactored / Upgraded
- **Reference Notes:**
  - Expanded [[Reference Notes/0-10_maintenance_upgrades_and_etcd.md|0-10_maintenance_upgrades_and_etcd.md]] to incorporate control plane leader election options:
    - Added specific configuration flags for scheduler and controller-manager active-passive lease management: `--leader-elect=true`, `--lease-duration=15s`, `--renew-deadline=10s`, and `--retry-period=2s`.

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/cka_split/`:
- `13_design_and_install_kubeadm.txt`

---

## [2026-06-26] - Ingestion: CKA Networking, DNS, and Ingress Transcript

### Refactored / Upgraded
- **Reference Notes:**
  - Expanded [[Reference Notes/0-9_networking_dns_and_ingress.md|0-9_networking_dns_and_ingress.md]] to incorporate additional troubleshooting utility patterns:
    - Added host bridge inspection command using `ip address show type bridge` to identify CNI bridges like `cni0`.
    - Added process-specific listening ports command using `netstat -npl` (e.g., grep for `scheduler` on port 10259).
    - Added socket status command using `netstat -npa` to audit client connections vs. peer-to-peer connections for ETCD (ports 2379/2380).

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/cka_split/`:
- `12_networking_dns_ingress_gateway_api.txt`

---

## [2026-06-26] - Ingestion: CKA Storage Mechanics Transcript

### Refactored / Upgraded
- **Reference Notes:**
  - Expanded [[Reference Notes/0-8_storage_mechanics_and_csi.md|0-8_storage_mechanics_and_csi.md]] to incorporate practical CKA troubleshoot and matching scenarios:
    - Added warning/tip on access mode matching constraints for PV and PVC binding.
    - Added troubleshooting scenario for PVCs stuck in `Terminating` due to the `kubernetes.io/pvc-protection` finalizer while in active pod use.
    - Added troubleshooting scenario for PVCs remaining `Pending` under `WaitForFirstConsumer` volume binding mode until a consumer Pod is scheduled.

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/cka_split/`:
- `11_storage_mechanics.txt`

---

## [2026-06-25] - Ingestion: CKA Kubernetes and Docker Storage (Mumshad)

### Refactored / Upgraded
- **Reference Notes:**
  - Expanded [[Reference Notes/0-8_storage_mechanics_and_csi.md|0-8_storage_mechanics_and_csi.md]] to incorporate detailed Container Storage Interface (CSI) Remote Procedure Calls (`CreateVolume`/`DeleteVolume`/`NodeStageVolume`/`NodePublishVolume`) and the evolutionary context on the deprecation of the `Recycle` reclaim policy (recycler pod filesystem scrub vulnerability vs out-of-tree CSI delete).
  - Expanded [[Reference Notes/2-3_docker_volumes_and_storage.md|2-3_docker_volumes_and_storage.md]] to document Docker storage drivers (layered architecture, read-only/writable layers, copy-on-write mechanism, default drivers like `overlay2`/`aufs`/`devicemapper`/`btrfs`/`zfs`) and Docker volume driver plugins (`local` default and third-party plugins like REX-Ray, Portworx, GlusterFS, NetApp, Convoy, Flocker, DigitalOcean).
- **Main Notes:**
  - Updated [[Main Notes/persistentvolume.md|persistentvolume.md]] to include deprecation details of the `Recycle` reclaim policy.

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/`:
- `StorageCKAMumshad.md`

---

## [2026-06-25] - Ingestion: AWS Deployment, Management & Optimization

### Added
- **Reference Notes:** Created [[Reference Notes/3-20_other_services_whitepapers.md|3-20_other_services_whitepapers.md]].
- **Projects:** Created [[Projects/aws-cloudops/Project - CloudFormation Stack Updates and Change Sets.md|Project - CloudFormation Stack Updates and Change Sets.md]] detailing declarative YAML layouts, parameterization, change set verification (`Replacement: True`), and stack teardown logs.
- **Main Notes:** Created 7 landing notes:
  - [[Main Notes/AWS CloudFormation.md|AWS CloudFormation.md]]
  - [[Main Notes/AWS Systems Manager.md|AWS Systems Manager.md]]
  - [[Main Notes/Amazon SES.md|Amazon SES.md]]
  - [[Main Notes/Amazon Pinpoint.md|Amazon Pinpoint.md]]
  - [[Main Notes/AWS Batch.md|AWS Batch.md]]
  - [[Main Notes/AWS Outposts.md|AWS Outposts.md]]
  - [[Main Notes/AWS Amplify.md|AWS Amplify.md]]

### Refactored / Upgraded
- **Reference Indexes:** Updated [[Reference Notes/3-Index - AWS.md|3-Index - AWS.md]] to catalog Module 3-20 and its verification project.
- **Main Notes:** Updated [[Main Notes/aws.md|aws.md]] to link to the new management, hybrid, batch, and communication landing notes.

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/aws_saa_split/`:
- `3-20_other_services_whitepapers.txt`

---

## [2026-06-25] - Ingestion: AWS Databases, Analytics & Machine Learning

### Added
- **Reference Notes:** Created [[Reference Notes/3-19_databases_analytics_ml.md|3-19_databases_analytics_ml.md]].
- **Projects:** Created [[Projects/aws-cloudops/Project - Athena S3 Access Log Analytics.md|Project - Athena S3 Access Log Analytics.md]] detailing serverless log query setups, DDL expressions with `RegexSerDe`, and HTTP status audits.
- **Main Notes:** Created 8 landing notes:
  - [[Main Notes/Amazon Athena.md|Amazon Athena.md]]
  - [[Main Notes/Amazon Redshift.md|Amazon Redshift.md]]
  - [[Main Notes/Amazon OpenSearch.md|Amazon OpenSearch.md]]
  - [[Main Notes/Amazon Neptune.md|Amazon Neptune.md]]
  - [[Main Notes/Amazon Timestream.md|Amazon Timestream.md]]
  - [[Main Notes/Amazon Keyspaces.md|Amazon Keyspaces.md]]
  - [[Main Notes/Amazon EMR.md|Amazon EMR.md]]
  - [[Main Notes/AWS Glue.md|AWS Glue.md]]

### Refactored / Upgraded
- **Reference Indexes:** Updated [[Reference Notes/3-Index - AWS.md|3-Index - AWS.md]] to catalog Module 3-19 and its verification project.
- **Main Notes:** Updated [[Main Notes/aws.md|aws.md]] to link to the new database, analytics, and Glue landing notes.

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/aws_saa_split/`:
- `3-19_databases_analytics_ml.txt`

---

## [2026-06-25] - Ingestion: AWS Serverless (Lambda, API Gateway, DynamoDB & Cognito)

### Added
- **Reference Notes:** Created [[Reference Notes/3-18_serverless.md|3-18_serverless.md]].
- **Projects:** Created [[Projects/kubernetes/Project - Serverless REST API with Lambda and API Gateway.md|Project - Serverless REST API with Lambda and API Gateway.md]] detailing hands-on playbooks for serverless setups, Python codes, and throttling/concurrency verification.
- **Main Notes:** Created 4 landing notes:
  - [[Main Notes/AWS Lambda.md|AWS Lambda.md]]
  - [[Main Notes/API Gateway.md|API Gateway.md]]
  - [[Main Notes/Amazon DynamoDB.md|Amazon DynamoDB.md]]
  - [[Main Notes/Amazon Cognito.md|Amazon Cognito.md]]

### Refactored / Upgraded
- **Reference Indexes:** Updated [[Reference Notes/3-Index - AWS.md|3-Index - AWS.md]] to catalog Module 3-18 and its verification project.
- **Main Notes:** Updated [[Main Notes/aws.md|aws.md]] to link to the new serverless-related landing notes.

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/aws_saa_split/`:
- `3-18_serverless.txt`

---

## [2026-06-25] - Ingestion: AWS Containers (ECS, EKS & ECR)

### Added
- **Reference Notes:** Created [[Reference Notes/3-17_containers_ecs_eks.md|3-17_containers_ecs_eks.md]].
- **Projects:** Created [[Projects/kubernetes/Project - ECS and EKS Cluster Deployments.md|Project - ECS and EKS Cluster Deployments.md]] detailing hands-on playbooks for ECS and EKS configurations and verification steps.
- **Main Notes:** Created 3 landing notes:
  - [[Main Notes/Amazon ECS.md|Amazon ECS.md]]
  - [[Main Notes/Amazon EKS.md|Amazon EKS.md]]
  - [[Main Notes/Amazon ECR.md|Amazon ECR.md]]

### Refactored / Upgraded
- **Reference Indexes:** Updated [[Reference Notes/3-Index - AWS.md|3-Index - AWS.md]] to catalog Module 3-17 and its verification project.
- **Main Notes:** Updated [[Main Notes/aws.md|aws.md]] to link to the new container-related landing notes.

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/aws_saa_split/`:
- `3-17_containers_ecs_eks.txt`

---

## [2026-06-25] - Ingestion: AWS IAM & Identity Governance

### Added
- **Main Notes:** Created 5 landing notes:
  - [[Main Notes/AWS Organizations.md|AWS Organizations.md]]
  - [[Main Notes/Service Control Policy.md|Service Control Policy.md]]
  - [[Main Notes/AWS IAM Identity Center.md|AWS IAM Identity Center.md]]
  - [[Main Notes/AWS Directory Services.md|AWS Directory Services.md]]
  - [[Main Notes/AWS Control Tower.md|AWS Control Tower.md]]

### Refactored / Upgraded
- **Reference Notes:** Consolidated and rewrote [[Reference Notes/3-2_aws_iam.md|3-2_aws_iam.md]] to clean out conversational fluff and merge detailed transcript context on AWS Organizations (OUs, member vs management, consolidated billing and aggregate usage/RI sharing), Service Control Policies (SCPs, OU inheritance and explicit allow requirements), Tag Policies (consistent tagging for cost-allocation and ABAC), Backup Policies, Advanced IAM Policy Conditions (SourceIP, RequestedRegion, ec2:ResourceTag, aws:PrincipalTag, aws:MultiFactorAuthPresent, aws:PrincipalOrgID), S3 Bucket-level vs Object-level ARNs scope, IAM Resource-based policies vs IAM Roles cross-account resource access nuances (assuming roles/relinquishing permissions vs direct resource access), EventBridge target invocation permissions (resource-based vs IAM roles), Permissions Boundaries (users & roles max permissions limits, intersection with identity-based policies and SCPs), AWS IAM Identity Center (successors to SSO, multi-account portals, permission sets, ABAC dynamic tag evaluations), AWS Directory Services (Managed Microsoft AD, AD Connector proxy gateway, Simple AD standalone domain controllers), Directory trust relationships and AD connectors integration with IAM Identity Center, and AWS Control Tower (governance baselines, Landing Zone Account Factory, preventive SCP guardrails vs detective Config rule guardrails). Added a comprehensive evaluation flowchart Mermaid diagram and detailed AARF breakdowns.
- **Main Notes:**
  - Updated [[Main Notes/aws.md|aws.md]] to link to the new IAM and Governance landing notes under related concepts.

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/aws_saa_split/`:
- `3-2_aws_iam_advanced.txt`

---

## [2026-06-25] - Ingestion: AWS KMS & Security Services

### Added
- **Main Notes:** Created 6 landing notes:
  - [[Main Notes/AWS Key Management Service.md|AWS Key Management Service.md]]
  - [[Main Notes/AWS Secrets Manager.md|AWS Secrets Manager.md]]
  - [[Main Notes/SSM Parameter Store.md|SSM Parameter Store.md]]
  - [[Main Notes/AWS WAF.md|AWS WAF.md]]
  - [[Main Notes/AWS Shield.md|AWS Shield.md]]
  - [[Main Notes/Amazon GuardDuty.md|Amazon GuardDuty.md]]

### Refactored / Upgraded
- **Reference Notes:** Consolidated and rewrote [[Reference Notes/3-3_aws_kms_security.md|3-3_aws_kms_security.md]] to clean out conversational fluff and integrate comprehensive transcript details including encryption types (in-transit TLS, redirect HTTP to HTTPS, server-side vs client-side), KMS key types (AWS owned, AWS managed, Customer Managed, and Imported), default vs custom key policies, regional scoping snapshot re-encryption flow, cross-account sharing permissions (`kms:CreateGrant`, `kms:DescribeKey`, `kms:ReEncrypt*`, `kms:Decrypt`), Multi-Region Keys (`mrk-`) client-side database column/field encryption flow (DynamoDB Encryption Client and AWS Encryption SDK), S3 Replication with KMS encryption rules, SSM Parameter Store standard vs advanced tiers and advanced Parameter Policies (Expiration, Expiration Notification, No-change Notification), Secrets Manager automatic credentials rotation and Lambda handlers, AWS Certificate Manager (ACM) public vs imported certificates validation/monitoring (EventBridge, AWS Config `acm-certificate-expiration-check` rule), AWS CloudHSM dedicated single-tenant HSM setups and Custom Key Store integration, Layer 7 AWS WAF web ACL rules (IP sets, rate limits), AWS Shield Standard vs Advanced DDoS protections, AWS Firewall Manager security policies, Amazon GuardDuty threat discovery logs/ML inputs and cryptocurrency warnings, Amazon Inspector vulnerability scanning (EC2, ECR, Lambda), and Amazon Macie data privacy scans. Inserted a strict-compliant Mermaid diagram depicting the Envelope Encryption workflow, and added a classic-to-modern HSM Evolutionary Conceptual Bridge.
- **Main Notes:**
  - Updated [[Main Notes/aws.md|aws.md]] to link to the new security and KMS landing notes under related concepts.
  - Updated [[Main Notes/aws - KMS and Security Services.md|aws - KMS and Security Services.md]] to reference the new atomic landing notes.

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/aws_saa_split/`:
- `3-3_aws_kms_security.txt`

---

## [2026-06-24] - Ingestion: AWS Disaster Recovery and Database Migrations

### Added
- **Main Notes:** Created 4 landing notes:
  - [[Main Notes/AWS Disaster Recovery.md|AWS Disaster Recovery.md]]
  - [[Main Notes/AWS Elastic Disaster Recovery.md|AWS Elastic Disaster Recovery.md]]
  - [[Main Notes/AWS Database Migration Service.md|AWS Database Migration Service.md]]
  - [[Main Notes/AWS Backup.md|AWS Backup.md]]

### Refactored / Upgraded
- **Reference Notes:** Consolidated and rewrote [[Reference Notes/3-15_aws_disaster_recovery.md|3-15_aws_disaster_recovery.md]] to merge detailed transcript context on RPO and RTO metrics, the 4 DR strategies (Backup and Restore, Pilot Light, Warm Standby, Multi-site Active-Active) with a comprehensive Mermaid visual comparison, AWS DRS continuous block-level replication, DMS and SCT homogeneous/heterogeneous CDC migrations, RDS/Aurora migration paths (snapshots, replica promotion, Percona XtraBackup, pg dump), AWS Backup plans and vaults (with Vault Lock WORM policy), AWS Application Migration Service (MGN) lift-and-shift, VMware Cloud on AWS hybrid capabilities, EC2 HA architectures (Elastic IP failovers, ASG active-passive, stateful ASG hooks with EBS snapshots), HPC configurations (ENA, EFA, Parallel Cluster, FSx for Lustre), Event Processing (SQS/SNS Lambda retries, Fan-Out, S3 events notifications, EventBridge/CloudTrail alerts), Caching policies, Subnet and IP blocking (NACL, SG, WAF), and Chaos testing.
- **Main Notes:**
  - Updated [[Main Notes/aws.md|aws.md]] to link to the new conceptual landing notes.
  - Updated [[Main Notes/aws - Disaster Recovery Strategies.md|aws - Disaster Recovery Strategies.md]] to reference [[Main Notes/AWS Disaster Recovery.md|AWS Disaster Recovery.md]] as its parent concept and updated breadcrumbs.

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/aws_saa_split/`:
- `3-15_aws_disaster_recovery.txt`

---

## [2026-06-24] - Ingestion: AWS SQS, SNS, Kinesis & Amazon MQ Decoupling

### Added
- **Main Notes:** Created 4 landing notes:
  - [[Main Notes/Amazon SQS.md|Amazon SQS.md]]
  - [[Main Notes/Amazon SNS.md|Amazon SNS.md]]
  - [[Main Notes/Amazon Kinesis.md|Amazon Kinesis.md]]
  - [[Main Notes/Amazon MQ.md|Amazon MQ.md]]

### Refactored / Upgraded
- **Reference Notes:** Consolidated and rewrote [[Reference Notes/3-14_aws_sqs_sns_decoupling.md|3-14_aws_sqs_sns_decoupling.md]] to integrate comprehensive SQS configuration settings (visibility timeout, long polling), queue types (Standard vs FIFO), SQS Auto Scaling integration and database write buffering patterns, SNS Topic pub/sub mechanics, message filtering, the SNS-to-SQS Fan-Out pattern (with a detailed Mermaid architecture diagram), real-time Amazon Kinesis Data Streams (shards, provisioned vs on-demand modes, KPL/KCL/EFO), near real-time Amazon Data Firehose targets/transformations, and Amazon MQ managed message broker active-standby HA deployment backed by shared Amazon EFS storage. Aligned Amazon MQ details with the Evolutionary Conceptual Bridging Rule.
- **Main Notes:**
  - Updated [[Main Notes/aws.md|aws.md]] to link to the new SQS, SNS, Kinesis, and MQ conceptual MOCs.
  - Updated [[Main Notes/aws - SQS, SNS, and Decoupled Microservices.md|aws - SQS, SNS, and Decoupled Microservices.md]] to refer to the new atomic landing notes.

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/aws_saa_split/`:
- `3-14_aws_sqs_sns_decoupling.txt`

---

## [2026-06-24] - Ingestion: AWS CloudFront CDN & AWS Global Accelerator

### Added
- **Main Notes:** Created 2 landing notes:
  - [[Main Notes/Amazon CloudFront.md|Amazon CloudFront.md]]
  - [[Main Notes/AWS Global Accelerator.md|AWS Global Accelerator.md]]

### Refactored / Upgraded
- **Reference Notes:** Consolidated and rewrote [[Reference Notes/3-13_aws_cloudfront_cdn.md|3-13_aws_cloudfront_cdn.md]] to merge detailed transcript context on CloudFront POP architecture (Edge locations, Regional caches), origins (S3 with OAC bucket policy, VPC origins, custom HTTP origins), caching behaviors, geo restriction mapping, invalidations (force refresh path wildcards), Signed URLs vs Signed Cookies, and AWS Global Accelerator Anycast IP routing flow and failover operations. Included a Mermaid comparison diagram and hands-on lab setups.
- **Main Notes:**
  - Updated [[Main Notes/aws.md|aws.md]] to link to the new Amazon CloudFront and AWS Global Accelerator landing notes under related concepts.
  - Updated [[Main Notes/aws - Route 53 DNS and CloudFront CDN.md|aws - Route 53 DNS and CloudFront CDN.md]] to reference the new atomic MOCs.

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/aws_saa_split/`:
- `3-13_aws_cloudfront_cdn.txt`

---

## [2026-06-24] - Ingestion: Amazon Route 53 DNS

### Added
- **Main Notes:** Created 4 landing notes:
  - [[Main Notes/Amazon Route 53.md|Amazon Route 53.md]]
  - [[Main Notes/Route 53 Hosted Zone.md|Route 53 Hosted Zone.md]]
  - [[Main Notes/Route 53 Routing Policies.md|Route 53 Routing Policies.md]]
  - [[Main Notes/Route 53 Resolver.md|Route 53 Resolver.md]]

### Refactored / Upgraded
- **Reference Notes:** Refactored [[Reference Notes/3-12_aws_route53_dns.md|3-12_aws_route53_dns.md]] to merge detailed transcript context on domain registration (auto-renew, WHOIS privacy protection, registrant contact options), default records (NS and SOA), DNS record types (A, AAAA, CNAME, Alias), TTL caching behavior, and all routing policies (Simple, Weighted, Latency, Geolocation, Geoproximity, IP-based, Failover, Multi-value), and resolver endpoints (Inbound/Outbound). Added a hands-on verification lab section (using AWS CloudShell, `nslookup`, and `dig` to monitor TTL cache decrement).
- **Main Notes:**
  - Updated [[Main Notes/aws.md|aws.md]] to link to the new Amazon Route 53 landing note.
  - Updated [[Main Notes/aws - Route 53 DNS and CloudFront CDN.md|aws - Route 53 DNS and CloudFront CDN.md]] to route to the individual atomic conceptual notes.

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/aws_saa_split/`:
- `3-12_aws_route53_dns.txt`

---

## [2026-06-24] - Ingestion: AWS RDS, Aurora, and ElastiCache

### Added
- **Main Notes:** Created 4 landing notes:
  - [[Main Notes/Amazon RDS.md|Amazon RDS.md]]
  - [[Main Notes/Amazon Aurora.md|Amazon Aurora.md]]
  - [[Main Notes/RDS Proxy.md|RDS Proxy.md]]
  - [[Main Notes/Amazon ElastiCache.md|Amazon ElastiCache.md]]

### Refactored / Upgraded
- **Reference Notes:** Overwrote and consolidated [[Reference Notes/3-7_aws_rds_aurora_databases.md|3-7_aws_rds_aurora_databases.md]] integrating RDS backups, snapshots, storage autoscaling, disaster recovery Multi-AZ vs. read replicas, RDS Custom access controls, Aurora storage virtualization and quorum topologies, Aurora writer/reader/custom endpoints, Aurora serverless and global database configurations, Amazon RDS Proxy connection pooling, and ElastiCache caching strategies (Lazy Loading, Write-Through) comparing Redis and Memcached. Inserted a Mermaid diagram comparing Multi-AZ and Read Replica topologies.
- **Main Notes:** Updated [[Main Notes/aws.md|aws.md]] and [[Main Notes/aws - RDS, Aurora, and DynamoDB.md|aws - RDS, Aurora, and DynamoDB.md]] to link to the new relational database and caching MOC concepts.

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/aws_saa_split/`:
- `3-7_aws_rds_aurora_databases.txt`

---

## [2026-06-24] - Ingestion: AWS ELB & ASG

### Added
- **Main Notes:** Created 5 landing notes:
  - [[Main Notes/aws - Elastic Load Balancer.md|aws - Elastic Load Balancer.md]]
  - [[Main Notes/aws - Application Load Balancer.md|aws - Application Load Balancer.md]]
  - [[Main Notes/aws - Network Load Balancer.md|aws - Network Load Balancer.md]]
  - [[Main Notes/aws - Gateway Load Balancer.md|aws - Gateway Load Balancer.md]]
  - [[Main Notes/aws - Auto Scaling Group.md|aws - Auto Scaling Group.md]]

### Refactored / Upgraded
- **Reference Notes:**
  - Refactored [[Reference Notes/3-10_aws_elb_load_balancing.md|3-10_aws_elb_load_balancing.md]] to merge detailed transcript context on ELB, ALB, NLB, and GWLB routing, sticky sessions, cross-zone load balancing, certificates/SNI, and connection draining. Inserted a Mermaid diagram of ELB/ALB/NLB/GWLB architectures.
  - Refactored [[Reference Notes/3-11_aws_asg_auto_scaling.md|3-11_aws_asg_auto_scaling.md]] to integrate ASG launch templates vs configurations, scaling policy types (manual, scheduled, dynamic, and predictive scaling), and inserted a Mermaid diagram depicting the ASG instance lifecycle hook flow.
- **Main Notes:**
  - Updated [[Main Notes/aws - EC2 and Elastic Load Balancing.md|aws - EC2 and Elastic Load Balancing.md]] to link to the new Elastic Load Balancer and Auto Scaling Group landing notes.

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/aws_saa_split/`:
- `3-10_3-11_aws_elb_asg.txt`

---

## [2026-06-24] - Ingestion: AWS S3 Storage

### Added
- **Main Notes:** Created 1 landing note and 4 atomic deeper-dive notes:
  - [[Main Notes/Amazon S3.md|Amazon S3.md]] (landing-note MOC)
  - [[Main Notes/S3 Storage Classes.md|S3 Storage Classes.md]] (deeper-dive)
  - [[Main Notes/S3 Lifecycle Rules.md|S3 Lifecycle Rules.md]] (deeper-dive)
  - [[Main Notes/S3 Encryption.md|S3 Encryption.md]] (deeper-dive)
  - [[Main Notes/S3 Object Lock.md|S3 Object Lock.md]] (deeper-dive)

### Refactored / Upgraded
- **Reference Notes:** Overwrote and consolidated [[Reference Notes/3-6_aws_s3_storage.md|3-6_aws_s3_storage.md]] (Module 3-6) integrating S3 key structure, versioning, CRR/SRR, all storage classes (including Intelligent-Tiering and Express One Zone), transition/expiration lifecycle policies, event notifications, baseline performance limits, multipart upload, transfer acceleration, byte-range fetches, all encryption methods (SSE-S3/KMS/C and DSSE-KMS), CORS, MFA Delete, Access Logs, Pre-signed URLs, object/vault lock, and Object Lambda. Inserted a Mermaid transition diagram.
- **Main Notes:** Updated [[Main Notes/aws.md|aws.md]] to link to `[[Amazon S3]]` under its related concepts. Removed the redundant `aws - Simple Storage Service.md` note.

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/aws_saa_split/`:
- `3-6_aws_s3_storage.txt`

---

## [2026-06-24] - Ingestion: AWS Storage Extras (Snow Family, FSx, Storage Gateway, Transfer Family, DataSync)

### Added
- **Main Notes:** Created 3 atomic conceptual deeper-dive notes:
  - [[Main Notes/aws - AWS Snow Family.md|aws - AWS Snow Family.md]]
  - [[Main Notes/aws - Amazon FSx.md|aws - Amazon FSx.md]]
  - [[Main Notes/aws - AWS Storage Gateway.md|aws - AWS Storage Gateway.md]]

### Refactored / Upgraded
- **Reference Notes:** Refactored [[Reference Notes/3-5_aws_ebs_efs_storage.md|3-5_aws_ebs_efs_storage.md]] to integrate details on AWS Snow Family models, FSx types (Lustre/ONTAP/Windows/OpenZFS) and deployment options, AWS Storage Gateway modes, AWS Transfer Family, and DataSync metadata preservation features. Inserted a comprehensive comparative table of all AWS storage options.
- **Main Notes:** Updated [[Main Notes/aws - EBS and EFS Storage.md|aws - EBS and EFS Storage.md]] MOC note to link to the new sub-concepts.

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/aws_saa_split/`:
- `3-5_aws_storage_extras.txt`

## [2026-06-24] - Ingestion: AWS EBS & EFS Storage

### Added
- **Main Notes:** Created 4 atomic conceptual deeper-dive notes:
  - [[Main Notes/aws - Amazon EBS.md|aws - Amazon EBS.md]]
  - [[Main Notes/aws - Amazon EFS.md|aws - Amazon EFS.md]]
  - [[Main Notes/aws - EBS Snapshot.md|aws - EBS Snapshot.md]]
  - [[Main Notes/aws - Instance Store.md|aws - Instance Store.md]]

### Refactored / Upgraded
- **Reference Notes:** Refactored [[Reference Notes/3-5_aws_ebs_efs_storage.md|3-5_aws_ebs_efs_storage.md]] to integrate detailed EBS volume types, snapshots, encryption, instance store, and EFS storage class parameters from the transcript, and inserted a comparative Mermaid diagram.
- **Main Notes:** Refactored [[Main Notes/aws - EBS and EFS Storage.md|aws - EBS and EFS Storage.md]] MOC note to reference new atomic sub-concept notes and added Dataview query aggregation.

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/aws_saa_split/`:
- `3-5_aws_ebs_efs_storage.txt`

## [2026-06-24] - Ingestion: AWS EC2 Compute Architecture

### Added
- **Main Notes:** Created 4 atomic conceptual deeper-dive notes:
  - [[Main Notes/aws - EC2 Instance.md|aws - EC2 Instance.md]]
  - [[Main Notes/aws - AMI.md|aws - AMI.md]]
  - [[Main Notes/aws - Placement Group.md|aws - Placement Group.md]]
  - [[Main Notes/aws - IMDS.md|aws - IMDS.md]]

### Refactored / Upgraded
- **Reference Notes:** Refactored [[Reference Notes/3-4_aws_ec2_compute.md|3-4_aws_ec2_compute.md]] to merge detailed EC2 transcript context, remove fluff, add Mermaid diagrams of Placement Group topologies, and compile IMDSv2 and Spot Fleet AARF breakdowns.
- **Main Notes:** Updated [[Main Notes/aws - EC2 and Elastic Load Balancing.md|aws - EC2 and Elastic Load Balancing.md]] with updated breadcrumbs, child references, and a dynamic Dataview query to catalog sub-concepts.

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/aws_saa_split/`:
- `3-4_aws_ec2_compute.txt`

## [2026-06-24] - Ingestion: AWS Identity & Access Management (IAM)

### Added
- **Main Notes:** Created 6 atomic conceptual deeper-dive notes:
  - [[Main Notes/aws - IAM User.md|aws - IAM User.md]]
  - [[Main Notes/aws - IAM Group.md|aws - IAM Group.md]]
  - [[Main Notes/aws - IAM Policy.md|aws - IAM Policy.md]]
  - [[Main Notes/aws - IAM Role.md|aws - IAM Role.md]]
  - [[Main Notes/aws - AWS STS.md|aws - AWS STS.md]]
  - [[Main Notes/aws - AWS CLI.md|aws - AWS CLI.md]]

### Refactored / Upgraded
- **Reference Notes:** Refactored [[Reference Notes/3-2_aws_iam.md|3-2_aws_iam.md]] by removing conversational fluff and duplicate headers, integrating comprehensive details on Users, Groups, Policies, MFA, Access Keys, AWS CLI, SDK, CloudShell, Roles, STS, security tools, and budgets. Added Mermaid diagrams mapping the IAM authentication flow and policy evaluation logic.
- **Main Notes:** Updated [[Main Notes/aws - Identity and Access Management.md|aws - Identity and Access Management.md]] with breadcrumbs and a dynamic Dataview query to catalog sub-concepts.

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/aws_saa_split/`:
- `3-2_aws_iam.txt`


## [2026-06-24] - Ingestion: AWS Global Infrastructure & Network Architecture


### Added
- **Main Notes:** Created 2 atomic conceptual deeper-dive notes:
  - [[Main Notes/aws - AWS Region.md|aws - AWS Region.md]]
  - [[Main Notes/aws - Availability Zone.md|aws - Availability Zone.md]]

### Refactored / Upgraded
- **Reference Notes:** Refactored [[Reference Notes/3-1_aws_global_infrastructure.md|3-1_aws_global_infrastructure.md]] by removing conversational fluff and redundant slide dumps, integrating AWS launch history (SQS in 2004, S3/EC2 in 2006), cloud economic benefits (CAPEX to OPEX, elasticity), region selection criteria (governance, latency, cost, availability), and a Mermaid diagram mapping the regions and Availability Zones hierarchy.

### Ingested Inflow Sources
Processed and integrated the following transcript file from `inflow/aws_saa_split/`:
- `3-1_aws_global_infrastructure.txt`

## [2026-06-24] - Ingestion: RHEL Central Authentication, Package Management, ACLs, LVM/RAID Review, BIND DNS Replication, and Custom Core Services Playbooks

### Added
- **Reference Notes:** Added new comprehensive sections to [[Reference Notes/8-9_redhat_enterprise_linux_administration.md|8-9_redhat_enterprise_linux_administration.md]]:
  - **Package Management (RPM, YUM, DNF, and Source Compilation):** Outlining low-level RPM command arrays, source code compilation procedures (configure, make, make install), caching rules, provides query methods, and transaction log management via `yum history` rollbacks.
  - **Centralized Authentication and Identity Management:** Explaining identity management strategies using FreeIPA servers/clients, replica HA promotion configurations (`ipa-replica-install`), and Active Directory integration via client enrollment (`realmd`) or cross-forest trusts (`ipa trust-add`).
  - **DHCP Server Configuration:** Dynamic Host Configuration Protocol subnet range allocations, lease timers, and static MAC reservation bindings.
  - **iSCSI Target and Initiator:** Configuring server side block mappings (backstores, LUNs, portals, target IQNs) and client side mounts using `iscsiadm` with `_netdev` mount properties.
  - **Database Administration (MariaDB):** Relational database installations, securing instances via `mysql_secure_installation`, provisioning users, and configuring access control tables.
  - **Central Logging (ELK Stack):** Centralized log observability configurations detailing Elasticsearch indices, Logstash grok parsing filter pipelines, and Kibana dashboard portal controls.
- **Projects:** Created 4 new hands-on project playbooks under `Projects/Linux/`:
  - [[Projects/Linux/Project - DHCP Server Installation and Dynamic IP Allocation.md|Project - DHCP Server Installation and Dynamic IP Allocation.md]]
  - [[Projects/Linux/Project - iSCSI Target and Initiator Storage Configuration.md|Project - iSCSI Target and Initiator Storage Configuration.md]]
  - [[Projects/Linux/Project - MariaDB Database Installation and User Security.md|Project - MariaDB Database Installation and User Security.md]]
  - [[Projects/Linux/Project - ELK Stack Log Aggregation Clustering.md|Project - ELK Stack Log Aggregation Clustering.md]]

### Refactored / Upgraded
- **Reference Notes:** Updated and expanded existing storage, security, DNS, and boot systems modules in [[Reference Notes/8-9_redhat_enterprise_linux_administration.md|8-9_redhat_enterprise_linux_administration.md]]:
  - Expanded LVM architecture commands to detail volume decommissioning CLI operations.
  - Expanded Software RAID configurations to show superblock wiping methods.
  - Added `systemctl daemon-reload` mount cache flushing troubleshooting to persistent storage mounting setup.
  - Expanded Apache configuration to address directory options (Indexes), basic auth (`htpasswd`), virtual hosts, and mod_ssl certificates.
  - Added BIND replication configuration specifying Master-Slave zone transfer options (`allow-transfer`, `also-notify`), SOA parameter rules, and slave write path directory guidelines under `/var/named/slaves/`.
  - Added systemd service masking/unmasking targets control.
  - Refactored POSIX ACLs section to address security limitations of UGO permissions, kernel compatibility options, explicit mount flags verification, recursive/default rules, and specific rule entries purging.
- **Projects:** Updated the [[Projects/Linux/Project - BIND DNS Server Installation and Caching Name Server.md|Project - BIND DNS Server Installation and Caching Name Server.md]] playbook to add a complete step-by-step master/slave DNS replication and zone transfer setup guide.
- **Reference MOCs:** Updated [[Reference Notes/8-Index - Linux and OS.md|8-Index - Linux and OS.md]] to catalog the 4 new project playbooks.

### Ingested Inflow Sources
Processed and integrated the following transcript files from `inflow/linux_administration/`:
- `59 - 59-Day-29_Reviewing_LVM&RAID.txt`
- `60 - 60-Day-29_Central_Authentication_IPA.txt`
- `61 - 61-Day-30_Central_Authentication_MS_AD.txt`
- `62 - 62-Day-31_Access_Control_Lists.txt`
- `63 - 63-Day-32_Package_Mnagament-YUM.txt`
- `83 - 84-Day-48_BIND_Cont-4.txt`


## [2026-06-23] - Ingestion: RHEL, CNCF DR, etcdutl, and 2-Tier AWS Terraform Transcripts

### Added
- **Reference Notes:** Created the new high-density RHEL administration reference module and CNCF references module:
  - [[Reference Notes/8-9_redhat_enterprise_linux_administration.md|8-9_redhat_enterprise_linux_administration.md]]
  - [[Reference Notes/12-Index - CNCF References.md|12-Index - CNCF References.md]]
  - [[Reference Notes/12-1_cncf_kubernetes_disaster_recovery.md|12-1_cncf_kubernetes_disaster_recovery.md]]
- **Projects:** Created 9 detailed hands-on project playbooks under `Projects/Linux/`, and 1 Terraform playbook under `Projects/terraform/`:
  - [[Projects/Linux/Project - User Administration & POSIX-ACL Hardening.md|Project - User Administration & POSIX-ACL Hardening.md]]
  - [[Projects/Linux/Project - GRUB Boot Security & Root Password Recovery.md|Project - GRUB Boot Security & Root Password Recovery.md]]
  - [[Projects/Linux/Project - Disk Partitioning, Software RAID & LVM Volume Expansion.md|Project - Disk Partitioning, Software RAID & LVM Volume Expansion.md]]
  - [[Projects/Linux/Project - Network Interface Profiles, Teaming & Bridging.md|Project - Network Interface Profiles, Teaming & Bridging.md]]
  - [[Projects/Linux/Project - Log Rotation, Text Filtering & Automation Backup.md|Project - Log Rotation, Text Filtering & Automation Backup.md]]
  - [[Projects/Linux/Project - NFS and FTP Secure Network File Shares.md|Project - NFS and FTP Secure Network File Shares.md]]
  - [[Projects/Linux/Project - Apache Web Server Deployment, Virtual Hosts, and Directory Security.md|Project - Apache Web Server Deployment, Virtual Hosts, and Directory Security.md]]
  - [[Projects/Linux/Project - BIND DNS Server Installation and Caching Name Server.md|Project - BIND DNS Server Installation and Caching Name Server.md]]
  - [[Projects/Linux/Project - Central LDAP-FreeIPA Domain Authentication.md|Project - Central LDAP-FreeIPA Domain Authentication.md]]
  - [[Projects/terraform/Project - 2-Tier Architecture Setup with RDS and Secret Manager.md|Project - 2-Tier Architecture Setup with RDS and Secret Manager.md]]
- **Main Notes:** Created 2 deeper-dive notes under `Main Notes/`:
  - [[Main Notes/linux - Logical Volume Manager.md|linux - Logical Volume Manager.md]]
  - [[Main Notes/linux - Boot Initialization and Systemd.md|linux - Boot Initialization and Systemd.md]]
- **Digital Garden:** Created 1 architectural pattern note:
  - [[Digital Garden/Pattern - Dynamic Volume Pooling and Online FileSystem Expansion.md|Pattern - Dynamic Volume Pooling and Online FileSystem Expansion.md]]

### Refactored / Upgraded
- **Reference Notes:** Updated Reference Notes 8-1 to 8-6 by appending cross-linking reference headers pointing to the new RHEL-specific commands in Module 8-9, and updated [[Reference Notes/0-10_maintenance_upgrades_and_etcd.md|0-10_maintenance_upgrades_and_etcd.md]] to incorporate the new `etcdutl` tool split commands for offline backups and snapshot restores.
- **Reference Indexes:** Updated [[Reference Notes/8-Index - Linux and OS.md|8-Index - Linux and OS.md]] to catalog Module 8-9 and all 9 playbooks, updated [[Reference Notes/--Index--.md|--Index--.md]] to catalog the new CNCF References MOC, and updated [[Reference Notes/10-Index - Terraform on AWS.md|10-Index - Terraform on AWS.md]] to catalog the new 2-Tier project playbook.
- **Main Notes:** Refactored [[Main Notes/etcd network ports.md|etcd network ports.md]] to integrate category breakdowns for etcd listener bindings (Listen, Advertise, Bootstrapping flags), client/peer network port configurations, port 2381 metrics monitoring, and CKA exam tips.

### Ingested Inflow Sources
Processed and integrated the following files from `inflow/`:
- `CKA-Exam Note on ETCD.md`
- `Disaster Recovery for your Kubernetes Clusters I - Andy Goldstein & Steve Kriss, Heptio.md`
- `ETCD BACKUP and REstore.md`
- `Practical Notes on working with ETCDCTL- ETCDUTL.md`
- `Day 0—Learn AWS With Terraform in 30 Days (with real-time projects).txt`
- `Day 2230 - 2-Tier Architecture Setup on AWS Using Terraform.txt`

And from `inflow/linux_administration/`:
- `01 - 1-Day-1_Course-Intro.txt`
- `02 - 2-Day-1_Course-Intro_Second_Group.txt`
- `03 - 3-Day-2_Basic_Installation.txt`
- `04 - 4-Day-2_Unix-Linux_History.txt`
- `05 - 5-Day-2_Basic_Commands.txt`
- `06 - 6-Day-3_Understanding_FHS.txt`
- `07 - 7-Day-3_Navigating_The_FileSystem.txt`
- `08 - 8-Day-4_FileSystem_Utilites.txt`
- `09 - 9-Day-4_FileSystem_Utilites_Cont.txt`
- `10 - 10-Day-5_Basic_User_Group_Administration.txt`
- `11 - 11-Day-5_Basic_Permissions.txt`
- `12 - 12-Day-6_Basic_Permissions_Cont.txt`
- `13 - 13-Day-6_Redirection.txt`
- `14 - 14-Day-6_Redirection_Cont-WH_Commands.txt`
- `15 - 15-Day-7_Inodes-Understanding_FileSystems.txt`
- `16 - 16-Day-8_Inodes_Cont.txt`
- `17 - 17-Day-8_Disks_and_Partations_Naming_Conventions.txt`
- `18 - 18-Day-9_Creating_and_Formatting_FileSystems.txt`
- `19 - 19-Day-10_Mounting_FileSystems.txt`
- `20 - 20-Day-10_Persistant_Mounting_Using_FSTAB.txt`
- `21 - 21-Day-10_Compressing_Archiving_Files_And_Directories.txt`
- `22 - 22-Day-11_Process_Management.txt`
- `23 - 23-Day-12_Process_Management_Cont.txt`
- `24 - 24-Day-12_Searching_And_Locating_Files_and_Dirs.txt`
- `25 - 25-Day-12_Searching_and_Extracting_Text.txt`
- `26 - 26-Day-13_VIM_Editor.txt`
- `27 - 27-Day-13_VIM_Editor_Cont.txt`
- `28 - 28-Day-13_Understanding_Boot_Process.txt`
- `29 - 29-Day-14_Understanding_Systemd.txt`
- `30 - 30-Day-14_Systemd_Targets.txt`
- `31 - 31-Day-15_Grub_BootLoader.txt`
- `32 - 32-Day-15_Resetting_Root_Password.txt`
- `33 - 33-Day-16_Systemd_Cont-Network_Basics.txt`
- `34 - 34-Day-16_Network_Basics_Cont.txt`
- `35 - 35-Day-17_Network_Basic_Config.txt`
- `36 - 36-Day-17_Network_Profiles.txt`
- `37 - 37-Day-18_IPV6_Intro.txt`
- `38 - 38-Day-18_IPV6_Cont.txt`
- `39 - 39-Day-19_IPV6_Cont.txt`
- `40 - 40-Day-19_IPV6_Config.txt`
- `41 - 41-Day-20_Network_TSHOOT.txt`
- `42 - 42-Day-20_Network_TSHOOT_Cont.txt`
- `43 - 43-Day-21_NIC_Teaming.txt`
- `44 - 44-Day-21_Network_Bridging.txt`
- `45 - 45-Day-22_Interface_Naming.txt`
- `46 - 46-Day-22_Setting_Grub_Password.txt`
- `47 - 47-Day-23_Getting_Help_Man_Pages.txt`
- `48 - 48-Day-23_Getting_Help_Cont.txt`
- `49 - 49-Day-23_History.txt`
- `50 - 49-Day-24_RAID.txt`
- `51 - 51-Day-24_RAID_Cont_1.txt`
- `52 - 52-Day-24_RAID_Cont_2.txt`
- `53 - 53-Day-25_RAID_Cont_3.txt`
- `54 - 54-Day-26_LVM_Basics.txt`
- `55 - 55-Day-27_LVM_Cont.txt`
- `56 - 56-Day-27_LVM_Cont_2.txt`
- `57 - 57-Day-28_SWAP.txt`
- `58 - 58-Day-28_Quota_Management.txt`
- `72 - 72-Day-40_Apache_Server_Part_3.txt`


## [2026-06-24] - Ingestion: AWS VPC Networking & Conceptual Integration

### Added
- **Main Notes:** Created 6 atomic conceptual landing notes:
  - [[Main Notes/Amazon VPC.md|Amazon VPC.md]]: Regional virtual network isolation, CIDR blocks planning, primary/secondary block constraints, and the 5 AWS reserved IPs per subnet.
  - [[Main Notes/AWS NAT Gateway.md|AWS NAT Gateway.md]]: Managed outbound-only internet connectivity for private subnets, AZ-independent HA design pattern.
  - [[Main Notes/Network Access Control List.md|Network Access Control List.md]]: Stateless subnet-level firewall rules, sequential rule evaluation, and outbound ephemeral port TCP 1024-65535 returns.
  - [[Main Notes/VPC Peering.md|VPC Peering.md]]: Highly available, non-transitive private inter-VPC connectivity on the AWS backbone.
  - [[Main Notes/VPC Endpoint.md|VPC Endpoint.md]]: Gateway endpoints (S3 and DynamoDB prefix routing) and Interface endpoints (PrivateLink ENI and DNS resolution).
  - [[Main Notes/Transit Gateway.md|Transit Gateway.md]]: Hub-and-spoke transit router connecting VPCs, VPNs, and DX links with transitive routing.

### Refactored / Upgraded
- **Reference Notes:** Refactored [[Reference Notes/3-9_aws_vpc_networking.md|3-9_aws_vpc_networking.md]] to clean out all conversational fluff, integrate detailed technical sections on Traffic Mirroring, AWS Network Firewall, IPv6 Egress-Only IGW, and VPC Flow Logs. Inserted a custom comparison Mermaid diagram for VPC endpoints.

### Ingested Inflow Sources
Processed and integrated the following files from the `inflow/` directory:
- `aws_saa_split/3-9_aws_vpc_networking.txt`

## [2026-06-22] - Ingestion: AWS CloudOps Study Guide & Projects

### Added
- **Reference Notes:** Created the central index note [[Reference Notes/11-Index - AWS CloudOps.md|11-Index - AWS CloudOps.md]] and 6 detailed reference modules:
  - [[Reference Notes/11-1_cloudops_monitoring_and_logging.md|11-1_cloudops_monitoring_and_logging.md]]
  - [[Reference Notes/11-2_incident_response_and_ssm.md|11-2_incident_response_and_ssm.md]]
  - [[Reference Notes/11-3_performance_optimization.md|11-3_performance_optimization.md]]
  - [[Reference Notes/11-4_disaster_recovery_and_backups.md|11-4_disaster_recovery_and_backups.md]]
  - [[Reference Notes/11-5_governance_and_compliance.md|11-5_governance_and_compliance.md]]
  - [[Reference Notes/11-6_automation_and_hybrid_networks.md|11-6_automation_and_hybrid_networks.md]]
- **Projects:** Created 3 detailed hands-on project playbooks:
  - [[Projects/aws-cloudops/Project - AWS Systems Manager Automation and Remediation.md|Project - AWS Systems Manager Automation and Remediation.md]]
  - [[Projects/aws-cloudops/Project - CloudWatch Log Streaming and Metric Filtering.md|Project - CloudWatch Log Streaming and Metric Filtering.md]]
  - [[Projects/aws-cloudops/Project - Hybrid VPC Peering and Transit Gateway Troubleshooting.md|Project - Hybrid VPC Peering and Transit Gateway Troubleshooting.md]]
- **Main Notes:** Created [[Main Notes/aws-cloudops.md|aws-cloudops.md]] landing note, [[Main Notes/aws-cloudops - Systems Manager and Runbooks.md|aws-cloudops - Systems Manager and Runbooks.md]] deeper-dive note, and [[Main Notes/aws-cloudops - CloudWatch Agent and Metrics.md|aws-cloudops - CloudWatch Agent and Metrics.md]] deeper-dive note.
- **Digital Garden:** Created [[Digital Garden/Pattern - Automated Operations and Event-Driven Remediation.md|Pattern - Automated Operations and Event-Driven Remediation.md]] pattern note.

### Refactored / Upgraded
- **Reference Indexes:** Updated [[Reference Notes/--Index--.md|--Index--.md]] and [[Main Notes/0-Index.md|0-Index.md]] to catalog the new AWS CloudOps study track.

### Ingested Inflow Sources
Processed and integrated the following files from the `inflow/` directory:
- `AWS_CloudOps.md`

## [2026-06-22] - Ingestion: AWS Terraform Study Guide & Projects

### Added
- **Reference Notes:** Created the central index note [[Reference Notes/10-Index - Terraform on AWS.md|10-Index - Terraform on AWS.md]] and 6 detailed reference modules:
  - [[Reference Notes/10-1_terraform_foundations_and_state.md|10-1_terraform_foundations_and_state.md]]
  - [[Reference Notes/10-2_variables_types_and_expressions.md|10-2_variables_types_and_expressions.md]]
  - [[Reference Notes/10-3_meta_arguments_lifecycle_and_state.md|10-3_meta_arguments_lifecycle_and_state.md]]
  - [[Reference Notes/10-4_networking_website_and_security.md|10-4_networking_website_and_security.md]]
  - [[Reference Notes/10-5_modules_eks_and_serverless.md|10-5_modules_eks_and_serverless.md]]
  - [[Reference Notes/10-6_cicd_gitops_observability_and_drift.md|10-6_cicd_gitops_observability_and_drift.md]]
- **Projects:** Created 3 detailed hands-on project playbooks:
  - [[Projects/terraform/Project - HA 3-Tier Architecture on AWS.md|Project - HA 3-Tier Architecture on AWS.md]]
  - [[Projects/terraform/Project - EKS GitOps and ArgoCD.md|Project - EKS GitOps and ArgoCD.md]]
  - [[Projects/terraform/Project - Terraform Automation and Drift Remediation.md|Project - Terraform Automation and Drift Remediation.md]]
- **Main Notes:** Created [[Main Notes/terraform.md|terraform.md]] landing note, [[Main Notes/terraform - State and Backend Locking.md|terraform - State and Backend Locking.md]] deeper-dive note, and [[Main Notes/terraform - Meta-Arguments and Loops.md|terraform - Meta-Arguments and Loops.md]] deeper-dive note.
- **Digital Garden:** Created [[Digital Garden/Pattern - Immutable Infrastructure and GitOps Reconciliation.md|Pattern - Immutable Infrastructure and GitOps Reconciliation.md]] pattern note.

### Refactored / Upgraded
- **Reference Indexes:** Updated [[Reference Notes/--Index--.md|--Index--.md]] and [[Main Notes/0-Index.md|0-Index.md]] to catalog the new Terraform on AWS study track.

### Ingested Inflow Sources
Processed and integrated the following files from the `inflow/` directory:
- `130 - How Does Terraform Work  Intro to IAC.txt`
- `230 - Terraform AWS Provider explained.txt`
- `330 -  Create an AWS S3 Bucket Using Terraform (it's simple).txt`
- `430 - Terraform State file management with AWS S3  Remote Backend.txt`
- `530 - Terraform Variables in AWS - Input vs Output vs Local Variables.txt`
- `630 - AWS Terraform Project Structure Best Practices.txt`
- `730 - AWS Terraform Type Constraints Explained (with realtime examples).txt`
- `830 - AWS Terraform Meta Arguments Made EASY  Count, depends_on , for_each.txt`
- `930 - AWS Terraform Lifecycle Rules Explained.txt`
- `1030 - AWS Terraform  Conditional Expressions , Splat Expressions and Dynamic Block.txt`
- `1130 - AWS Terraform Functions - Part 1.txt`
- `1230 - AWS Terraform Functions - Part 2.txt`
- `1330 - Terraform Data Source AWS Explained (with demo).txt`
- `1430 - Host A Static Website In AWS S3 And Cloudfront (using terraform).txt`
- `1530 -  AWS VPC Peering Using Terraform - Mini project.txt`
- `1630 - AWS IAM User Management with Terraform - Mini Project.txt`
- `1730 - AWS Terraform Blue-Green Deployment Using Elastic Beanstalk.txt`
- `1830 - Image Processing Serverless Project using AWS Lambda(with terraform).txt`
- `1930 - Terraform Provisioners (with demo) - local vs remote vs file.txt`
- `2030 - Terraform Custom Modules for EKS - From Zero to Production.txt`
- `2130 - AWS Policy and Governance Setup Using Terraform.txt`
- `2330 - Setup End-to-End Observability in AWS Using Terraform (Real-Time Project).txt`
- `2430 - Highly Available and Scalable Architecture Using Terraform.txt`
- `2530 - Terraform Import In AWS Explained With Demo.txt`
- `2630 - HCP Terraform Explained with Demo - Terraform Projects and Workspaces.txt`
- `2730 - Automate AWS Infra Using Terraform and GitHub Actions  Realtime Project.txt`
- `2830 - AWS 3-tier Architecture With Terraform  End-to-End Real-Time Project.txt`
- `2930 - End-to-end GitOps With Terraform and ArgoCD For EKS  Production-grade Kubernetes Project.txt`
- `3030 - Drift Detection and Remediation Using Terraform and GitHub Actions  Real Time Project.txt`

---

## [2026-06-22] - Ingestion: GitHub Actions Study Guide

### Added
- **Reference Notes:** Created the central index note [[Reference Notes/9-Index - GitHub Actions.md|9-Index - GitHub Actions.md]] and 3 detailed reference modules:
  - [[Reference Notes/9-1_github_actions_architecture_and_workflows.md|9-1_github_actions_architecture_and_workflows.md]]
  - [[Reference Notes/9-2_github_actions_advanced_execution.md|9-2_github_actions_advanced_execution.md]]
  - [[Reference Notes/9-3_github_actions_administration_and_security.md|9-3_github_actions_administration_and_security.md]]
- **Projects:** Created [[Projects/github-actions/Project - GitHub Actions CI-CD Pipelines.md|Project - GitHub Actions CI-CD Pipelines.md]] playbook.
- **Main Notes:** Created [[Main Notes/github-actions.md|github-actions.md]] landing note, [[Main Notes/github-actions - Security and Secrets.md|github-actions - Security and Secrets.md]] deeper note, and [[Main Notes/github-actions - Runner Environments.md|github-actions - Runner Environments.md]] deeper note.
- **Digital Garden:** Created [[Digital Garden/Pattern - Secure OIDC Cloud Authentication in CI-CD.md|Pattern - Secure OIDC Cloud Authentication in CI-CD.md]] pattern note.

### Refactored / Upgraded
- **Reference Indexes:** Updated [[Reference Notes/--Index--.md|--Index--.md]] and [[Main Notes/0-Index.md|0-Index.md]] to catalog the new Linux & OS and GitHub Actions study tracks.

### Ingested Inflow Sources
Processed and integrated the following files from the `inflow/` directory:
- `github-actions-study-guide.md`

---

## [2026-06-22] - Ingestion: Linux & Systems Administration Guides

### Added
- **Reference Notes:** Created the central index note [[Reference Notes/8-Index - Linux and OS.md|8-Index - Linux and OS.md]] and 8 detailed reference modules:
  - [[Reference Notes/8-1_linux_architecture_and_kernel.md|8-1_linux_architecture_and_kernel.md]]
  - [[Reference Notes/8-2_filesystems_and_storage.md|8-2_filesystems_and_storage.md]]
  - [[Reference Notes/8-3_networking_and_services.md|8-3_networking_and_services.md]]
  - [[Reference Notes/8-4_user_management_and_hardening.md|8-4_user_management_and_hardening.md]]
  - [[Reference Notes/8-5_system_services_and_initialization.md|8-5_system_services_and_initialization.md]]
  - [[Reference Notes/8-6_monitoring_logs_and_diagnostics.md|8-6_monitoring_logs_and_diagnostics.md]]
  - [[Reference Notes/8-7_high_availability_and_clustering.md|8-7_high_availability_and_clustering.md]]
  - [[Reference Notes/8-8_automation_backup_and_cloud.md|8-8_automation_backup_and_cloud.md]]
- **Projects:** Created [[Projects/Linux/Project - HA Keepalived Load Balancing.md|Project - HA Keepalived Load Balancing.md]] and [[Projects/Linux/Project - Migrating Legacy Init Scripts to systemd.md|Project - Migrating Legacy Init Scripts to systemd.md]] playbooks.
- **Main Notes:** Created [[Main Notes/linux.md|linux.md]] and [[Main Notes/process-supervision.md|process-supervision.md]] landing notes.

### Ingested Inflow Sources
Processed and integrated the following files from the `inflow/` directory:
- `linux-admin-comprehensive-guide.md`
- `linux-admin-2-comprehensive-guide.md`

---

## [2026-06-21] - Ingestion: Vertical Pod Autoscaler & In-Place Pod Resizing

### Added
- **Main Notes:** Created [[Main Notes/Vertical Pod Autoscaler.md|Vertical Pod Autoscaler.md]] landing note and [[Main Notes/Vertical Pod Autoscaler - In-Place Resizing.md|Vertical Pod Autoscaler - In-Place Resizing.md]] deeper-dive note detailing dynamic scaling, feature gates, and resize policies.
- **Projects:** Created [[Projects/kubernetes/Project - Vertical Pod Autoscaler.md|Project - Vertical Pod Autoscaler.md]] containing playbooks for VPA installation, Auto mode validation, and manual in-place patching diagnostics.

### Refactored / Upgraded
- **Reference Notes:** Upgraded Section 12.5 "Workload Autoscaling (HPA & VPA)" in [[Reference Notes/0-6_kubernetes_workloads_and_controllers.md|0-6_kubernetes_workloads_and_controllers.md]] to incorporate HPA vs VPA comparisons and manual in-place scaling workflows, aligned with v1.35 GA (container-level) and v1.36 Beta (pod-level) resource resize features.

### Ingested Inflow Sources
Processed and integrated the following files from the `inflow/` directory:
- `VPA_mumshad.md`
- `InPlace resizing.md`
- `InPlace Resizing Docs.md`

---

## [2026-06-21] - Ingestion: Secrets Store CSI Driver & AWS Integration

### Added
- **Main Notes:** Created [[Main Notes/Secrets Store CSI Driver.md|Secrets Store CSI Driver.md]] conceptual landing note detailing dynamic mounting, ServiceAccount annotations, and failure modes.
- **Projects:** Created [[Projects/kubernetes/Project - Secrets Store CSI Driver.md|Project - Secrets Store CSI Driver.md]] containing complete playbooks for Helm setup, IRSA trust policies, SecretProviderClass configuration, and auto-rotation verification.

### Refactored / Upgraded
- **Reference Notes:** Added Section 11.12 "Secrets Store CSI Driver Integration" in [[Reference Notes/0-7_security_and_network_policies.md|0-7_security_and_network_policies.md]] (Module 7) describing the external secrets pattern, volume setup, IRSA tokens, and auto-rotation hooks.

### Ingested Inflow Sources
Processed and integrated the following files from the `inflow/` directory:
- `Secret Store CSI Driver Tutorial  Kubernetes Secrets  AWS Secrets Manager  KodeKloud.md`
- `Secret Store CSI Driver Tutorial  Kubernetes Secrets  AWS Secrets Manager  KodeKloud 1.md`

---

## [2026-06-21] - Ingestion: Konnectivity Control Plane Egress Proxy

### Added
- **Main Notes:** Created [[Main Notes/Konnectivity.md|Konnectivity.md]] conceptual landing note detailing server-agent architecture, secure egress selectors, and operational deadlock scenarios.

### Refactored / Upgraded
- **Reference Notes:** Added Section 2.2 "Control Plane Egress Proxy (Konnectivity)" inside [[Reference Notes/0-2_cluster_architecture_and_components.md|0-2_cluster_architecture_and_components.md]] (Module 2) outlining the network split problem, tunnel flow topologies, API Server egress configuration, DaemonSet vs. Deployment deployment styles, and the validating admission webhook deadlock failure loop.

### Ingested Inflow Sources
Processed and integrated the following files from the `inflow/` directory:
- `Konnectivity reverse ssh tunnel Management.md`

---

## [2026-06-21] - Ingestion: Secrets Encryption at Rest Reference and Labs

### Refactored / Upgraded
- **Reference Notes:** Expanded [[Reference Notes/0-7_security_and_network_policies.md|0-7_security_and_network_policies.md]] (Module 7) with a comprehensive comparison table of all encryption providers, wildcard matching rules, resource exemption precedence, zero-downtime key rotation protocol steps, and automatic reloading configuration options.
- **Projects:** Updated [[Projects/kubernetes/Project - Secrets Management and Encryption.md|Project - Secrets Management and Encryption.md]] to detail local `etcd-client` diagnostic installation, process-checking queries, and a live key rotation and automatic reload validation lab.
- **CKA Exam Checklists:** Appended key rotation guidelines, host-level `etcdctl` query methods, and automatic reload configurations under Section 8 of [[Projects/CKA/Exam Checklist - Security and Storage.md|Exam Checklist - Security and Storage.md]].
- **Main Notes:** Added automatic reloading configuration parameters to [[Main Notes/secret - Encryption at Rest and Ingestion.md|secret - Encryption at Rest and Ingestion.md]].

### Ingested Inflow Sources
Processed and integrated the following files from the `inflow/` directory:
- `Encrypting Secrets At Rest.md`
- `Notes on Encryption at rest.md`

---

## [2026-06-21] - Ingestion: A Note on Secrets

### Refactored / Upgraded
- **Main Notes:** Integrated node-level distribution safety constraint (secrets are only sent to nodes running pods that require them) from `A Note on Secrets.md` into [[Main Notes/secret.md|secret.md]].

### Ingested Inflow Sources
Processed and integrated the following files from the `inflow/` directory:
- `A Note on Secrets.md`

---

## [2026-06-20] - Secrets Management Ingestion & Decoupling

### Added
- **Projects:** Created [[Projects/kubernetes/Project - Secrets Management and Encryption.md|Project - Secrets Management and Encryption.md]] containing complete playbooks for mounting diverse secret types, projected token volume configuration, and enabling symmetric etcd encryption.
- **Main Notes:** Created [[Main Notes/Secret - ServiceAccount Token Projection.md|Secret - ServiceAccount Token Projection.md]] describing token lifetimes and rotation mechanics.
- **Digital Garden:** Created [[Digital Garden/Pattern - Cryptographic Secret Partitioning and Volatile Memory Mounts.md|Pattern - Cryptographic Secret Partitioning and Volatile Memory Mounts.md]] mapping inter-container separation of concern patterns.

### Refactored / Upgraded
- **Reference Notes & Architecture Realignment:**
  - Relocated advanced Secrets security architecture, cryptography (Base64 vs. encryption math), Linux `tmpfs` page-cache mechanics, ServiceAccount Token Projection & auto-rotation, and Signer Container Partitioning from [[Reference Notes/0-13_scheduling_logging_and_lifecycle.md|0-13_scheduling_logging_and_lifecycle.md]] (Module 13) to Section 11 of [[Reference Notes/0-7_security_and_network_policies.md|0-7_security_and_network_policies.md]] (Module 7) to align with security boundaries.
  - Simplified Module 13's Secrets section to act purely as a configuration injection guide, linking directly to Module 7 for security hardening.
  - Updated all dependent links in [[Main Notes/secret.md|secret.md]], [[Main Notes/Secret - ServiceAccount Token Projection.md|Secret - ServiceAccount Token Projection.md]], [[Main Notes/secret - Encryption at Rest and Ingestion.md|secret - Encryption at Rest and Ingestion.md]], [[Digital Garden/Pattern - Cryptographic Secret Partitioning and Volatile Memory Mounts.md|Pattern - Cryptographic Secret Partitioning and Volatile Memory Mounts.md]], and [[Projects/CKA/Exam Checklist - Security and Storage.md|Projects/CKA/Exam Checklist - Security and Storage.md]] to reference Module 7.


### Ingested Inflow Sources
Processed and integrated the following files from the `inflow/` directory:
- `Secrets.md`

---

## [2026-06-20] - Admission Controllers Ingestion & Decoupling

### Added
- **Projects:** Created [[Projects/kubernetes/Project - Admission Webhooks.md|Project - Admission Webhooks.md]] containing complete playbooks for the ImagePolicyWebhook scan backend and custom mutating Flask server (including Kubernetes container resources and securityContext best practices).
- **Main Notes:** Created [[Main Notes/Admission Controllers - ValidatingAdmissionPolicy.md|Admission Controllers - ValidatingAdmissionPolicy.md]] to conceptualize the CEL-based validation engine in Kubernetes v1.36.
- **System Profiles:** Created [[System/Agents/poc_kubernetes_developer.md|poc_kubernetes_developer.md]] to act as the specialized domain developer.

### Refactored / Upgraded
- **Reference Notes:** 
  - Integrated 35 built-in admission plugins from `inflow/Admission-Controller_Docs.md` into [[Reference Notes/0-16_admission_controllers.md|0-16_admission_controllers.md]].
  - Decoupled hands-on lab code and configuration blocks into the new Project note, replacing them with wiki-links.
  - Expanded the module with deep-dive audits on JSON Patch syntax, mTLS verification, and CEL syntax.
- **Digital Garden:** Updated [[Digital Garden/Pattern - Dynamic Security Admission and Webhook TLS Verification.md|Pattern - Dynamic Security Admission and Webhook TLS Verification.md]] with links to the new project note.
- **CKA Exam Checklists:** Added cross-reference guides and hands-on project links to Sections 9 & 10 of [[Projects/CKA/Exam Checklist - Security and Storage.md|Exam Checklist - Security and Storage.md]].

### Ingested Inflow Sources
Processed and integrated the following files from the `inflow/` directory:
- `Admission-Controller_Docs.md`

---

## [2026-06-14] - Admission Controllers & Webhooks Ingestion

### Added
- **Reference Notes:** Created [[0-16_admission_controllers|0-16_admission_controllers.md]] (Module 16) covering the admission request lifecycle (mutating/validating), built-in admission plugins, dynamic admission webhooks, Flask webhook server configurations, an ImagePolicyWebhook configuration lab, and a custom mutating webhook deployment lab using the AARF framework.
- **Main Notes:** Created [[Admission Controllers - ImagePolicyWebhook|Admission Controllers - ImagePolicyWebhook.md]] detailing image vulnerability scanning at admission time.
- **Digital Garden:** Created [[Pattern - Dynamic Security Admission and Webhook TLS Verification|Pattern - Dynamic Security Admission and Webhook TLS Verification.md]] mapping cross-domain intersections between API admission gates, webhook configurations, and mutual TLS authentication.

### Refactored / Upgraded
- **Reference Indexes:** Updated [[0-Index - Kubernetes|0-Index - Kubernetes.md]] and [[0-CKA Study Alignment Guide|0-CKA Study Alignment Guide.md]] to catalog the new Module 16 and integrate it into the CKA syllabus roadmap.
- **Main Notes:** Updated [[Admission Controllers|Admission Controllers.md]] and [[Admission Webhooks - Mutating and Validating|Admission Webhooks - Mutating and Validating.md]] to link to the new Module 16 guide.
- **CKA Exam Checklists:** Appended Section 9 "ImagePolicyWebhook Configuration Checklist" and Section 10 "Custom Mutating Admission Webhook Configuration Checklist" to [[Exam Checklist - Security and Storage|Exam Checklist - Security and Storage.md]].

### Ingested Inflow Sources
Processed and integrated the following files from the `inflow/` directory:
- `Admission-Controller_Docs.md`
- `Mutation-Admission-Controller.md`
- `Notes on the labs.md`
- `Picture-Example-of-a-webhook-server-Python flask.md`
- `LAB_mutation and Admission.md`


## [2026-06-12] - Pure Flat MOC Architecture Implementation

### Refactored / Upgraded
- **Flat MOC Integration:** Consolidating user preference for direct backward/forward navigation by merging the technical contents of the 10 `-deeper` notes directly into their corresponding main landing notes (e.g. [kube-scheduler.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/kube-scheduler.md), [node.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/node.md), [pod.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/pod.md)).
- **Sub-concept Redirection:** Updated the `parent_concept` in all sub-concept notes (like [Scheduling Filtering Predicates.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Scheduling%20Filtering%20Predicates.md)) to link directly to their main landing notes and simplified their breadcrumbs to clean up navigation paths.
- **Query Restoration:** Restored the resilient `contains(parent_concept, this.file.link)` Dataview query directly at the bottom of the main landing notes, making all child sub-concepts discoverable in a single hop.
- **Redundant MOC Deletion:** Deleted the 10 intermediate `-deeper.md` notes to avoid duplicate index files.


## [2026-06-12] - Nested Deeper-Dive MOC Restructure

### Refactored / Upgraded
- **Nested MOC Architecture:** Restructured the 10 core control plane and component concepts to utilize a clean nested hierarchy.
  - Main landing notes (e.g. [kube-scheduler.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/kube-scheduler.md)) now have `deeper_dive: "[[kube-scheduler-deeper]]"` in their frontmatter and a visible, clickable body section pointing to the dedicated deeper MOC note, with their individual sub-concept Dataview tables removed.
  - Deeper MOC notes (e.g. [kube-scheduler-deeper.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/kube-scheduler-deeper.md)) now host the resilient Dataview query block, displaying all related sub-concepts and use cases.
  - All task-based sub-concept child notes (e.g. [Scheduling Filtering Predicates.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Scheduling%20Filtering%20Predicates.md)) have their `parent_concept` redirected to `"[[kube-scheduler-deeper]]"` (and corresponding MOCs) and their breadcrumbs updated to represent the intermediate path.
- **Flat Architecture Retention:** Left all other 38 landing notes on a clean, flat architecture where sub-concepts link directly to the main note and queries run there, as they lack intermediate `-deeper` MOC files.


## [2026-06-12] - Vault-wide Dataview Query Upgrade for Robust Search

### Refactored / Upgraded
- **Dataview Query Upgrades:** Upgraded all 48 landing notes in `Main Notes/` to use the case-insensitive and type-resilient `icontains(string(parent_concept), "<concept-name>")` filter. This resolves Dataview matching failures caused by link objects stored as quoted strings (e.g. `parent_concept: "[[aws]]"`) in frontmatter YAML, establishing absolute query integrity across the entire second brain.


## [2026-06-12] - Ingest Tasks Index and Core CKA Concept Resolutions

### Added
- **Main Notes / CKA Concepts:** Created 45+ detailed deeper-dive concept notes under `Main Notes/` covering the full range of CKA-relevant tasks from the official docs index and resolving all core placeholder warnings:
  - **Scheduling:** [Scheduling Filtering Predicates.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Scheduling%20Filtering%20Predicates.md), [Scheduling Scoring Priorities.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Scheduling%20Scoring%20Priorities.md), [Manual Node Assignment.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Manual%20Node%20Assignment.md), [Static nodeName Scheduling Bypass.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Static%20nodeName%20Scheduling%20Bypass.md).
...
- **Refactoring / Hierarchy Restructuring:** Restructured the vault hierarchy for all 10 core Kubernetes landing notes. Added the `deeper_dive: "[[<deeper-note-name>]]"` property to the frontmatter of all landing notes. Moved the dynamic Dataview query blocks from the main landing notes (e.g. `kube-scheduler.md`, `node.md`, `pod.md`) to their respective deeper notes (e.g. `kube-scheduler-deeper.md`, `node-deeper.md`). Updated the `parent_concept` property in all child sub-concept notes to point directly to their respective `-deeper` notes, matching the logical structural hierarchy.
  - **Controller Manager:** [Reconciliation Loop Mechanics.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Reconciliation%20Loop%20Mechanics.md), [Node Eviction Grace Periods.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Node%20Eviction%20Grace%20Periods.md), [HA Leader Election Leases.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/HA%20Leader%20Election%20Leases.md), [Cascading Deletions.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Cascading%20Deletions.md), [Garbage Collection Owner References.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Garbage%20Collection%20Owner%20References.md).
  - **Node Mechanics:** [Node Registration Pathway.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Node%20Registration%20Pathway.md), [Node Conditions & Lifecycle.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Node%20Conditions%20%26%20Lifecycle.md), [Node Allocatable Math.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Node%20Allocatable%20Math.md), [Node Leases (Heartbeat Mechanism).md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Node%20Leases%20(Heartbeat%20Mechanism).md), [cgroups v1 vs v2.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/cgroups%20v1%20vs%20v2.md), [Configuring kube-reserved and system-reserved limits.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Configuring%20kube-reserved%20and%20system-reserved%20limits.md).
  - **kubectl Client Tools:** [Kubeconfig Anatomy.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Kubeconfig%20Anatomy.md), [API Discovery and explanation.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/API%20Discovery%20and%20explanation.md), [kubectl YAML dry-run generation.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/kubectl%20YAML%20dry-run%20generation.md), [Force Deletion bypass.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Force%20Deletion%20bypass.md), [JSONPath and custom-columns filters.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/JSONPath%20and%20custom-columns%20filters.md).
  - **Storage:** [emptydir.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/emptydir.md), [hostpath.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/hostpath.md).
  - **Metadata:** [annotation.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/annotation.md).
  - **etcd Administration:** [etcd Backup and Restore.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/etcd%20Backup%20and%20Restore.md), [Raft Consensus.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Raft%20Consensus.md), [Raft Quorum Rules.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Raft%20Quorum%20Rules.md), [etcd network ports.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/etcd%20network%20ports.md), [etcd TLS certificate configurations.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/etcd%20TLS%20certificate%20configurations.md).
  - **Pod Lifecycle & Debugging:** [Pod Phases and Lifecycle States.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Pod%20Phases%20and%20Lifecycle%20States.md), [Quality of Service (QoS) Classes.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Quality%20of%20Service%20(QoS)%20Classes.md), [Health Probes (liveness readiness startup).md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Health%20Probes%20(liveness%20readiness%20startup).md), [Init Containers.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Init%20Containers.md), [Native Sidecars (v1.29+).md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Native%20Sidecars%20(v1.29%2B).md), [Debugging with Ephemeral Containers.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Debugging%20with%20Ephemeral%20Containers.md), [Container Lifecycle Hooks (postStart preStop).md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Container%20Lifecycle%20Hooks%20(postStart%20preStop).md).
  - **Kubelet & Runtime Mechanics:** [Node Bootstrap and TLS Bootstrapping.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Node%20Bootstrap%20and%20TLS%20Bootstrapping.md), [Node Conditions and Hard Eviction Thresholds.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Node%20Conditions%20and%20Hard%20Eviction%20Thresholds.md), [Kubelet Heartbeats & The Lease API.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Kubelet%20Heartbeats%20%26%20The%20Lease%20API.md), [CRI Socket Communication.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/CRI%20Socket%20Communication.md), [Static Pods.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Static%20Pods.md), [Inspecting kubelet systemd service logs.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Inspecting%20kubelet%20systemd%20service%20logs.md), [containerd-shim mechanics.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/containerd-shim%20mechanics.md), [Pause Container Namespace Holder.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Pause%20Container%20Namespace%20Holder.md), [Cgroup Drivers systemd vs cgroupfs.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Cgroup%20Drivers%20systemd%20vs%20cgroupfs.md), [Debugging containerd with ctr and nerdctl.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Debugging%20containerd%20with%20ctr%20and%20nerdctl.md), [CRI troubleshooting with crictl.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/CRI%20troubleshooting%20with%20crictl.md).

### Ingested Inflow Sources
Processed and integrated the following files:
- Scraped official Kubernetes documentation index `https://kubernetes.io/docs/tasks/` to extract CKA-relevant tasks and mapped them to core deep-dive notes, resolving all placeholder link warnings.

---

## [2026-06-12] - Ingest Tasks Index and Kubectl Plugins Inflows

### Added
- **Main Note / kubectl Plugins:** Created new deeper-dive concept note [kubectl - Plugins.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/kubectl%20-%20Plugins.md) detailing custom subcommand prefix rules (`kubectl-`), PATH loading resolution, listing/verifying commands, and a step-by-step custom CKA bash script scenario example.

### Refactored / Upgraded
- **Module 0-1 Upgrade:** Updated [0-1_kube_api_and_kubectl.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/0-1_kube_api_and_kubectl.md) to add Section 9 covering naming requirements, executable PATH settings, plugin verification list commands, and Krew plugin manager search/install instructions.
- **kubectl Deeper Concept:** Linked `[[kubectl - Plugins|kubectl Plugins]]` to the `sub_concepts` frontmatter list in [kubectl-deeper.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/kubectl-deeper.md), resolving a placeholder warning.
- **Core API Exam Checklist:** Appended Section 8 covering plugin naming/PATH rules, listing executables, and creation/test playbooks to the CKA Core API checklist: [Exam Checklist - Core Architecture and API.md](file:///home/karim/Desktop/BrainDump/Projects/CKA/Exam%20Checklist%20-%20Core%20Architecture%20and%20API.md).

### Ingested Inflow Sources
Processed and integrated the following files:
- `inflow/Docs-Tasks-section.md` (scraped tasks index `https://kubernetes.io/docs/tasks/` and extending page `https://kubernetes.io/docs/tasks/extend-kubectl/kubectl-plugins/` to isolate CKA-relevant topics)

---

## [2026-06-12] - Ingest Custom Scheduler Inflows

### Added
- **Main Note / Multiple Custom Schedulers:** Created new deeper-dive concept note [Multiple Custom Schedulers.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/Multiple%20Custom%20Schedulers.md) detailing custom scheduling purposes, filtering/scoring control loop mechanics, lease name isolation for High Availability (HA), RBAC authentication configurations, and CKA troubleshooting procedures, resolving the placeholder wiki-link.

### Refactored / Upgraded
- **Module 0-13 Upgrade:** Enriched [0-13_scheduling_logging_and_lifecycle.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/0-13_scheduling_logging_and_lifecycle.md) with concrete ServiceAccount, ClusterRoleBindings (for `system:kube-scheduler` and `system:volume-scheduler`), and RoleBinding (for `extension-apiserver-authentication-reader` in namespace `kube-system`) YAML configs to reflect Kubernetes production deployment requirements.
- **Workloads Exam Checklist:** Appended Section 13 covering custom scheduler deployment manifests, ConfigMaps configurations, pod assignment spec properties, and event-based/log-based debugging steps to the primary CKA workloads checklist: [Exam Checklist - Workloads and Scheduling.md](file:///home/karim/Desktop/BrainDump/Projects/CKA/Exam%20Checklist%20-%20Workloads%20and%20Scheduling.md).

### Ingested Inflow Sources
Processed and integrated the following files:
- `inflow/Custom_scheduler_mumshad.md` (and scraped official Kubernetes documentation from `https://kubernetes.io/docs/tasks/extend-kubernetes/configure-multiple-schedulers/`)

---

## [2026-06-12] - Ingest Scheduling and PriorityClass Inflows

### Refactored / Upgraded
- **Ingested PriorityClass Inflows:** Processed and audited the following files:
  - `inflow/PriorityClass_Mumshad.md` (verified and fully covered in [0-13_scheduling_logging_and_lifecycle.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/0-13_scheduling_logging_and_lifecycle.md))
  - `inflow/PriorityClass_Docs.md` (scraped core API & CLI reference URLs; ingested imperative commands)
  - `inflow/Mumshad-PriorityClass-Lab-studyCase.md` (ingested and covered in [0-13_scheduling_logging_and_lifecycle.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/0-13_scheduling_logging_and_lifecycle.md))
  - `inflow/docs/03-Scheduling/21-Admission Controllers.md` (empty/0-bytes, ignored)
  - `inflow/docs/03-Scheduling/Validating and Mutation Admission Controllers.md` (empty/0-bytes, ignored)
- **Verified Coverage & Placements:** Confirmed that PriorityClass 32-bit integer ranges (1B to -2B), system cluster critical values (2B), default priority value (0), preemption policies (`PreemptLowerPriority` vs. `Never`), and CLI verification commands are fully detailed in [0-13_scheduling_logging_and_lifecycle.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/0-13_scheduling_logging_and_lifecycle.md) and [kube-scheduler - Priority Preemption and Topology Spread.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/kube-scheduler%20-%20Priority%20Preemption%20and%20Topology%20Spread.md). Added imperative `kubectl create priorityclass` speed-run command patterns to the CKA Workloads exam checklist and Module 13 CLI reference. Added the Mutating Admission Controller timeline analysis and the Priority vs. Node Affinity Preemption Paradox.

---

## [2026-06-12] - Ingest AWS Raw Notes into Core Reference Modules

### Refactored / Upgraded
- **Consolidated AWS Reference Notes:** Decoupled and ingested all raw AWS files from `inflow/` and git history, specifically:
  - `inflow/AWS-SAA-Amazon-Web-Services-Solution-Architect-Associate.md`
  - `inflow/AWS-SAA-Amazon-Web-Services-Solution-Architect-Associate-LABS.md`
  - `inflow/AWS-KMS.md`
  - `inflow/AWS-Eissa-Abo-Sherif-Elastic-Load-Balancing-AutoScaling(6).md`
  - `inflow/AWS-Day-1-Practitioner.md` to `inflow/AWS-Day-5-Practitioner.md`
  - `inflow/AWS-NTI-VPC-EC2-DAY1.md`
  - `inflow/AWS-NTI-More-On-EC2-EBS-EFS-DAY2.md`
  - `inflow/AWS-NTI-S3-Database-RDS.md`
  - `inflow/AWS-NTI-Loadbalancing-Autoscaling-SystemManager-Day3.md`
  - `inflow/AWS-Practitioner-2025-4-15.md` to `inflow/AWS-Practitioner-2025-4-15-4.md`
  into exactly 16 domain-specific modules in `Reference Notes/`:
  - [3-1_aws_global_infrastructure.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/3-1_aws_global_infrastructure.md): Global footprint, Regions, AZs, Edge Locations, CloudFront edge caching, cloud deployment/provisioning models, 6 pillars of Well-Architected Framework, VPC CIDR subnets, Route Tables, Internet/NAT Gateways, SG/NACL ephemeral ports, NAT topologies, and SAA VPC deep-dive labs.
  - [3-2_aws_iam.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/3-2_aws_iam.md): Identity federation, AWS STS role assumptions, temporary credentials, IAM policies, multi-account governance (AWS Organizations & SCPs), and S3 EC2-role validation labs.
  - [3-3_aws_kms_security.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/3-3_aws_kms_security.md): KMS encryption key types (Customer Managed CMKs vs AWS Managed Keys), envelope encryption mechanics, key rotation policies, Secrets Manager vs SSM Parameter Store, Cognito user pools, WAF, and Shield.
  - [3-4_aws_ec2_compute.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/3-4_aws_ec2_compute.md): EC2 instance families, VM lifecycle, User Data bootstrapping, IMDSv1/v2 security, purchasing models (on-demand/spot/savings), placement groups, Elastic Load Balancers (ALB/NLB), Auto Scaling Groups (ASG), app integration decoupling (SQS/SNS), and SQS-RDS HA labs.
  - [3-5_aws_ebs_efs_storage.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/3-5_aws_ebs_efs_storage.md): EBS volume types (gp3 vs io2 Block Express), snapshots, encryption sharing, local ephemeral Instance Store, RAID configurations, and network EFS NFS shared storage.
  - [3-6_aws_s3_storage.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/3-6_aws_s3_storage.md): S3 bucket policies, storage classes (Standard to Glacier Deep Archive), lifecycle rules, versioning, replication, transfer acceleration, and Athena SQL analytics.
  - [3-7_aws_rds_aurora_databases.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/3-7_aws_rds_aurora_databases.md): RDS Multi-AZ vs Read Replicas, Aurora architecture, endpoints, database migrations (DMS), and schema conversion (SCT).
  - [3-8_aws_dynamodb_nosql.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/3-8_aws_dynamodb_nosql.md): DynamoDB partition key design, RCUs/WCUs, DynamoDB Accelerator (DAX) cache, ElastiCache (Redis vs Memcached), and Redshift data warehouse.
- **Updated MOC Index:** Re-indexed all AWS reference materials in [3-Index - AWS.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/3-Index%20-%20AWS.md) to link to exactly the 8 core modules.
- **Fixed Broken Links:** Resolved three broken relative links inside [aws - Virtual Private Cloud.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/aws%20-%20Virtual%20Private%20Cloud.md) and [aws - EC2 and Elastic Load Balancing.md](file:///home/karim/Desktop/BrainDump/Main%20Notes/aws%20-%20EC2%20and%20Elastic%20Load%20Balancing.md) pointing to obsolete/deleted modules.
- **Cleaned Up Obsolete Modules:** Deleted redundant modules `3-9_` to `3-16_` to keep vault reference structures clean and aligned.

---

## [2026-06-11] - BGP, Python, and Web Fundamentals Reference Consolidation

### Refactored / Upgraded
- **Consolidated BGP Routing Reference Notes:** Merged 6 raw BGP files (basic topologies, eBGP vs iBGP peering, path vector selection, route reflectors, and redundancy) into the primary BGP routing module:
  - [4-1_bgp_routing_fundamentals_and_topologies.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/4-1_bgp_routing_fundamentals_and_topologies.md): Expanded with deep-dive concepts on TCP connection mechanics, state machine transitions, path attributes (AS-PATH, NEXT-HOP, Origin Codes), loopback peering load-balancing, and Route Reflector Cluster ID loops prevention.
- **Consolidated Python Programming Reference Notes:** Merged 7 raw Python files (objects, statements, versions, comparison operators, and Flask modules) into the primary Python fundamentals module:
  - [7-1_python_programming_fundamentals.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/7-1_python_programming_fundamentals.md): Detailed with pyenv version switching, isolated virtual environments, dependency constraint structures (`requirements.txt`), custom f-string float formatting, zip/enumerate iterators, and the Flask App Factory pattern utilizing PyMongo DB connections.
- **Consolidated HTML Semantic Reference Notes:** Merged 5 raw HTML files (document hierarchy, semantic tags, content categories, and nesting limits) into the primary HTML module:
  - [6-1_html_semantics_and_document_structure.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/6-1_html_semantics_and_document_structure.md): Enriched with document-level layout definitions, viewport responsive scales, content category outlines (Flow vs Sectioning), accessibility navigation, and strict block-level nesting validations.
- **Consolidated CSS Box Model and Inheritance Reference Notes:** Merged 5 raw CSS files (box properties, units, inheritance rules, and spacing resets) into the primary CSS module:
  - [6-2_css_box_model_and_styling_inheritance.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/6-2_css_box_model_and_styling_inheritance.md): Detailed standard vs alternative box model sizing, universal `box-sizing: inherit` reset configurations, physical vs logical device pixels, em/rem responsive typography choices, and forced inheritance overrides via the `inherit` keyword.
- **Consolidated AWS S3 Transfer Acceleration Notes:** Integrated S3 Transfer Acceleration details from [Exam-1.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/Exam-1.md) into [3-2_aws_compute_and_storage_services.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/3-2_aws_compute_and_storage_services.md).
- **Created Miscellaneous (MISC) Reference Modules:** Merged 5 raw systems and cloud files into 3 new dedicated MISC reference modules cataloged in the main index:
  - [git_fundamentals_and_workflows.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/git_fundamentals_and_workflows.md): Detailing Git workspace staging areas, checkout/switch branch management, non-destructive reverts vs destructive resets, stashing, and collaborative forks/PRs.
  - [linux_system_administration_and_troubleshooting.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/linux_system_administration_and_troubleshooting.md): Detailing physical file type verification (`file`), common GNU/Linux exit codes mapping, system error translation (`perror`), password hashing (bcrypt), and remote SSH client control (`paramiko`).
  - [openstack_cloud_infrastructure.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/openstack_cloud_infrastructure.md): Detailing private cloud virtualization, comparing hyperscalers, and the 6 core components required to host an IaaS cloud environment.
- **Cleaned Up Raw Notes:** Deleted all 32 raw `.md` files and index files from `Reference Notes/` directory to maintain vault cleanliness.

---

## [2026-06-11] - Jenkins Reference Modules Consolidation

### Refactored / Upgraded
- **Consolidated Jenkins Reference Notes:** Merged 11 raw Jenkins files (e.g., architecture, history, triggers, variables, upgrades, troubleshooting, JUnit) into the 3 standardized Jenkins reference modules:
  - [5-1_jenkins_architecture_and_pipeline_structure.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/5-1_jenkins_architecture_and_pipeline_structure.md): Enriched with details on controller-agent distributed topologies (SSH vs JNLP protocols), Docker container runtimes (workspace mounts), and structural Declarative pipeline components.
  - [5-2_jenkins_build_triggers_and_pipeline_variables.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/5-2_jenkins_build_triggers_and_pipeline_variables.md): Consolidated Git triggers (webhooks vs polling schedules), Cron `H` hashing algorithms, and compilation environment scoping (`environment {}` block limitations vs dynamic script assignments), alongside JUnit XML reports and trends.
  - [5-3_jenkins_administration_and_troubleshooting.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/5-3_jenkins_administration_and_troubleshooting.md): Integrated Docker-based core upgrades, safe plugin installations, safe system restarts (`/safeRestart`), exit code debugging (`sh` step error detection), and manual gating CD release strategies (Blue-Green, Canary, Rolling).
- **Cleaned Up Raw Notes:** Deleted all 11 consolidated raw `.md` notes and the temporary `Jenkins-Index.md` from the `Reference Notes/` directory to maintain vault cleanliness.

---

## [2026-06-11] - Ingestion of NTI & Practitioner Study Notes (Notes_AWS_Docker_Kubernets)

### Added
- **Module Library: NTI & Practitioner Notes:** Integrated a comprehensive library of 134 study files under `Reference Notes/Notes_AWS_Docker_Kubernets/` covering AWS Cloud Practitioner, AWS Solution Architect Associate (SAA), BGP Routing, CSS/HTML Fundamentals, Docker Engine & Compose operations, Jenkins CI/CD Architecture, and Python programming fundamentals.
- **Media Attachments Library:** Tracked and validated 557 media files under `Attachments/` representing slides, diagrams, and screenshots linked within the study notes, achieving 100% link resolution.
- **Inflow Sources Tracking:** Tracked raw inflow clippings for Systems Design and API protocols to ensure complete source control.
- **Structured Reference Indices & Modules:** Formally compiled the raw study notes into structured reference indices and modules inside `Reference Notes/`:
  - **Docker (Track 2):** Created `2-Index - Docker.md` and 5 core AARF-style modules (`2-1_` to `2-5_`).
  - **AWS (Track 3):** Created `3-Index - AWS.md` and 4 core AARF-style modules (`3-1_` to `3-4_`).
  - **BGP Routing (Track 4):** Created `4-Index - BGP Routing.md` and module `4-1_`.
  - **Jenkins CI/CD (Track 5):** Created `5-Index - Jenkins.md` and 3 core AARF-style modules (`5-1_` to `5-3_`).
  - **Web Fundamentals (Track 6):** Created `6-Index - Web Fundamentals.md` and modules `6-1_`, `6-2_`.
  - **Python (Track 7):** Created `7-Index - Python.md` and module `7-1_`.
- **Conceptual Landing & Deeper-Dive Notes:** Created landing notes (e.g., `docker.md`, `aws.md`, `bgp.md`, `jenkins.md`, `web-fundamentals.md`, `python.md`) and their corresponding deeper-dive use case/architecture notes in `Main Notes/` in 100% template compliance.
- **OS Isolation Pattern Note:** Created `Digital Garden/Pattern - Container Runtime Socket Interface and OS Isolation.md` detailing Kubelet CRI Unix socket mechanics and Linux kernel isolation.

### Refactored / Upgraded
- **Image Link Auditing:** Verified 573 internal image links (`![[...]]` and standard markdown) mapping notes to their respective files in `Attachments/` with zero missing resources.
- **Central Index MOC Integrations:** Refactored `Reference Notes/--Index--.md` and `Main Notes/0-Index.md` to cleanly integrate all 6 new domains as first-class citizens.
- **Kubernetes Labs Indexing:** Appended a dedicated "Domain 8: NTI & Udemy Practice Labs" section to `Reference Notes/0-Index - Kubernetes.md` containing all 44 raw practice lab notes.

---

## [2026-06-11] - Systems Design & Architecture Patterns Ingestion

### Added
- **Module 1-7: Software Architecture Patterns:** Created new Reference Note `Reference Notes/1-7_software_architecture_patterns.md` in the AARF style, containing deep dives on Monolith, Modular Monolith, Microservices, Event-Driven Architecture, Serverless, DDD, Clean Architecture, Strangler Fig, BFF, and CQRS, complete with 10 custom Mermaid.js diagrams.
- **Module 1-8: Distributed Communication & Queues:** Created new Reference Note `Reference Notes/1-8_distributed_communication_and_queues.md` in the AARF style, containing deep dives on synchronous/asynchronous communication, Pub/Sub, message queues, and streaming (Kafka) with scaling diagrams.
- **Main Notes / Software Architecture Patterns:** Created landing note `Main Notes/software-architecture-patterns.md` and deeper-dive concept note `Main Notes/software-architecture-patterns - Core Patterns.md`.
- **Main Notes / Distributed Communication & Queues:** Created landing note `Main Notes/distributed-communication.md` and deeper-dive concept note `Main Notes/distributed-communication - Async Queues and Streams.md`.

### Refactored / Upgraded 
- **Frontmatter Compliance Sweep:** Proactively audited and resolved 22 frontmatter schema warnings across 14 atomic deeper-dive notes inside `Main Notes/`, ensuring 100% template compliance.
- **Reference Notes (1-1 to 1-6) Upgrades:** Distributed raw topics (Availability, Latency, Forward/Reverse Proxy, Connection Pooling, SQL/NoSQL Wide-column, Graph, Time-series, Vector databases, Sharding, Partitioning, Encryption, SSO, SAML) across existing modules in Deep-Intuition (AARF) style.
- **Advanced Clippings Ingestion:** Integrated advanced system design concepts: database consistency models (ACID vs. BASE in Module 1-3), API protocol trade-offs (REST, GraphQL, gRPC in Module 1-5), and security paradigms (OAuth 2.0 4-roles/3-tokens and JWT structure/stateless verification AARF breakdowns in Module 1-6).
- **Mermaid Visualizations:** Injected sequence and topology diagrams for Load Balancer Health Checking, Connection Pool checkout flows, JWT Token structure, database horizontal sharding vs partitioning, and the 10 architecture patterns.
- **Sequential Ingestion Protocols:** Updated root `workflow.md` and `Agent.md` to codify the sequential ingestion rule for multi-file batches to avoid write/merge conflicts and preserve link integrity.

### Ingested Inflow Sources
The following files have been processed and integrated:
- `inflow/Architecture_Patterns_Playbook_Raw.md`
- `inflow/System_Design_Handbook_Raw.md`
- `inflow/Level-UpCoding-OAuth-ClearlyExplained.md`
- `inflow/LevelUp-JWT.md`
- `inflow/LevelUpCoding-ACID-BASE.md`
- `inflow/LevelUp -codingGPPC.md`
- `inflow/Clippings/Level-Up-Coding-REST, GraphQL, or gRPC? Choosing the Right Tool for the Job.md`

---

## [2026-06-10] - CKA GOLD Extension & Advanced Playbook Release

### Added
- **Deep-Intuition Documentation Style (AARF):** Integrated the AARF framework (Answers, Assumptions, Rationale, Failures, and Alternatives) as a formal extension to the ingestion pipeline inside [Agent.md](file:///home/karim/Desktop/BrainDump/Agent.md) and [instructions.md](file:///home/karim/Desktop/BrainDump/instructions.md).
- **CKA GOLD Practice Suite Expansion:** Expanded the CKA prep suite under `Projects/CKA/kubernetes-CKA-Gold/` to exactly **175 tasks** (75 study Q&As + 100 environment-based scenarios), adding:
  - Pod debugging via ephemeral containers.
  - Advanced JSONPath data filters.
  - Multi-file ConfigMap mounts and sidecar log rotation handlers.
  - [walkthrough.md](file:///home/karim/Desktop/BrainDump/Projects/CKA/kubernetes-CKA-Gold/walkthrough.md): Playbook compiled dynamically for all 175 CKA GOLD tasks.
- **Advanced Kubernetes Playbook (Out-of-Scope):** Created a dedicated advanced directory under `Projects/kubernetes/` containing **50 advanced tasks** (25 study Q&As + 25 scenarios) covering:
  - Custom Resource Definitions (CRDs) with status/scale subresources.
  - Admission Webhooks (Mutating & Validating configurations).
  - CKS Security (AppArmor, Seccomp, RuntimeClasses, and PSA enforce/restricted modes).
  - CKAD Developer Tooling (Helm, Kustomize overrides).
  - Advanced Scheduling (PodTopologySpreadConstraint skew, PriorityClasses).
  - [walkthrough.md](file:///home/karim/Desktop/BrainDump/Projects/kubernetes/walkthrough.md): Programmatic walkthrough playbook for all 50 advanced tasks.
  - [primer.md](file:///home/karim/Desktop/BrainDump/Projects/kubernetes/primer.md): Advanced study guide.
  - CLI runner [gold.py](file:///home/karim/Desktop/BrainDump/Projects/kubernetes/gold.py) / [gold.sh](file:///home/karim/Desktop/BrainDump/Projects/kubernetes/gold.sh) sharing the same underlying 3-node KinD cluster context.
- **MOC Integration:** Integrated the new playbooks into the main CKA Index MOC ([0-Index.md](file:///home/karim/Desktop/BrainDump/Projects/CKA/0-Index.md)).


## [2026-06-10] - Domain-Based Reference Prefixing & MOC Restructuring

### Added
- **MISC Reference Category:** Created a Miscellaneous Projects section directly under the main indexes (`0-Index.md`), removing the irrelevant Local DevOps index and listing the standalone Gitea GitOps project there.

### Refactored / Upgraded
- **Reference Naming Scheme:** Restructured all reference notes to enforce domain-prefixed numbering by default:
  - Kubernetes reference notes are prefixed with `0-X_` (e.g. `0-1_`, `0-2_`, up to `0-15_`).
  - Systems Design reference notes are prefixed with `1-X_` (e.g. `1-1_` to `1-6_`).
  - Standalone projects without long-term history (like Gitea) are classified as miscellaneous chapters (without numbers) and grouped under `MISC`.
- **Troubleshooting Classification:** Moved the Kubernetes Troubleshooting & Diagnostics module (`0-11_troubleshooting_and_diagnostics.md`) to the primary Kubernetes index MOC (`0-Index - Kubernetes.md`).
- **YAML & Link Update Sweep:** Executed a vault-wide refactoring sweep to update all internal links, breadcrumbs, and frontmatter reference guides to point to the new domain-prefixed filenames, maintaining 100% link integrity.
- **Agent System Configs:** Updated `Agent.md`, `workflow.md`, `System/Skills/ingest_refinement.md`, and `System/Skills/orchestration.md` to establish the new domain-prefixed naming conventions as standard pipeline behaviors.

### Ingested Inflow Sources
The following files have been processed and integrated:
- `inflow/Note -on-Pod-editing_mumshad.md`
- `inflow/Important_labs_study cases_mumshad_GeminiQA.md`

---

## [2026-06-08] - System Design Re-Ingestion & PoC Decoupling Pass

### Added
- **Project note (`Projects/Systems Design/Project - Secure Load-Balanced Web API.md`):** Re-created and consolidated the hands-on configurations (Nginx load balancing, SSL, rate limiting, and CORS headers), the Python FastAPI service (JWT authentication, in-memory rate limiter, and database pool), the SQL schema migration, and the Curl verification playbook.
- **Conceptual Landing Notes (`Main Notes/`):** Created landing notes for `caching.md` and `cdn.md`.
- **Deeper-dive Notes (`Main Notes/`):** Created detailed deeper-dive notes for `caching - Strategies and Eviction Policies.md`, `cdn - Push vs Pull and Edge Caching.md`, `api-protocols - gRPC and Protobuf.md`, and `database-selection - Sharding and Consistent Hashing.md`.
- **Topic-Specific Index MOCs:** Created topic-specific index files to segregate subdomains and prevent mixing of study tracks:
  - `Reference Notes/0-Index - Kubernetes.md` & `Main Notes/0-Index - Kubernetes.md` (Kubernetes tracks, CKA/CKS/CKAD)
  - `Reference Notes/0-Index - Systems Design.md` & `Main Notes/0-Index - Systems Design.md` (Distributed systems, sharding, caching, CDNs)
  - `Reference Notes/0-Index - Local DevOps.md` & `Main Notes/0-Index - Local DevOps.md` (Gitea self-hosted source control, LVM partitions, act_runners CI/CD, troubleshooting)

### Refactored / Upgraded
- **Index Files & MOCs (`0-Index.md`):** Renamed all root directory map index files from `Index.md` to `0-Index.md` (across `Main Notes/`, `Reference Notes/`, `Digital Garden/`, and `Projects/CKA/`) to ensure they sort at the absolute top of their folders. Replaced all breadcrumbs and internal links referencing `[[Index]]` with `[[0-Index]]` across all 100+ files.
- **Logical Map of Content Structure:** Reorganized the indexes logically by systems domains (e.g. Cluster Administration, Core API Engine, Node & Container Runtimes, Workloads & Placements, Storage & Networking, Distributed System Design, GitOps Automation, and Tooling) instead of listing modules numerically.
- **Reference Notes Splitting:** Split the consolidated `Reference Notes/17_system_design_fundamentals.md` into six dedicated, topic-specific Reference Notes:
  - `Reference Notes/1-1_scaling_and_single_server.md`
  - `Reference Notes/1-2_load_balancing_topologies.md`
  - `Reference Notes/1-3_database_architectures_and_sharding.md`
  - `Reference Notes/1-4_caching_and_content_delivery_networks.md`
  - `Reference Notes/1-5_api_protocols_and_grpc.md` (created)
  - `Reference Notes/1-6_access_control_and_api_security.md` (created)
- **Reference File Deletion:** Removed the old consolidated `Reference Notes/17_system_design_fundamentals.md` file.
- **MOC & Index Update:** Updated `Reference Notes/0-Index - Systems Design.md` to reference the 6 split modules.
- **Conceptual Main Notes (`Main Notes/`):** Restored, updated, and validated the landing notes and deeper-dive notes for `load-balancing`, `database-selection`, `api-protocols`, and `api-security`, redirecting their YAML frontmatter `reference_guides` and footer wiki-links to the new split files.
- **Standardized Splitting Behavior:** Updated `Agent.md`, `workflow.md`, `System/Skills/ingest_refinement.md`, and `System/Skills/orchestration.md` to configure topic-based Reference Note splitting as the default behavior across the ingestion pipeline.
- **Link Auditing:** Validated the entire vault with `review_vault.py` achieving 100% link integrity and 100% inflow coverage across all modules.

### Ingested Inflow Sources
The following files and assets have been processed and integrated:
- `inflow/System Design Course – APIs, Databases, Caching, CDNs, Load Balancing & Production Infra.md`
- `inflow/System Design Explained APIs, Databases, Caching, CDNs, Load Balancing & Production Infra.md`
- `inflow/images/Readme.md` (ignored asset)

---

## [2026-06-07] - Ingest System Design Course Clippings & Diagram Pipeline Integration

### Added
- **Reference Note (`Reference Notes/17_system_design_fundamentals.md`):** Created a comprehensive study module summarizing the Hayk Simonyan System Design course clippings. Detailed single server topologies, horizontal vs. vertical scaling, SPOF mitigations, load balancer types (L4 vs. L7) and algorithms, health check mechanics, database models (SQL, NoSQL document/key-value/columnar, Graph), caching/CDNs, transport layers (TCP/UDP), API protocols (REST/GraphQL), session-based vs. JWT authentication, authorization models (RBAC, ABAC, ACLs, OAuth 2.0), and 7 core security defense mechanisms.
- **Landing Notes (`Main Notes/load-balancing.md`, `Main Notes/database-selection.md`, `Main Notes/api-protocols.md`, `Main Notes/api-security.md`):** Created 4 landing notes for the core systems design concepts, structured with frontmatter roles and dataview indexers.
- **Deeper-dive Notes (`Main Notes/load-balancing - Algorithms and L4-L7 Routing.md`, `Main Notes/database-selection - SQL vs NoSQL vs Graph.md`, `Main Notes/api-protocols - REST vs GraphQL.md`, `Main Notes/api-security - Defenses.md`):** Created 4 atomic deeper-dive notes elaborating sub-topics, trade-offs, and details.
- **Project note (`Projects/Systems Design/Project - Secure Load-Balanced Web API.md`):** Decoupled the practical implementation playbooks (such as Nginx gateway load balancing/timeouts, CLI curl tests, and SQL injection code comparisons) into a standalone project guide.
- **System Config Folder (`System/`):** Created a centralized configuration folder containing templates, agent profiles, and specific skill files:
  - **Templates (`System/Templates/`):** landing_note.md, deeper_note.md, pattern_note.md, reference_note.md, and project_note.md.
  - **Agents (`System/Agents/`):** researcher.md, auditor.md, diagrammer.md, poc_developer.md, garden_architect.md, and exam_expert.md.
  - **Skills (`System/Skills/`):** ingest_refinement.md, context_audit.md, diagram_generation.md, project_poc.md, garden_linking.md, and exam_checklists.md.
- **Central Workflow Mappings (`workflow.md`):** Created root-level central pipeline orchestrator detailing the 6 phases, mapping them to agent files and skills.

### Refactored / Upgraded
- **Diagram Designer Pipeline integration (`Agent.md` & `instructions.md`):** Formally integrated `Phase 2.5 (Diagram Design)` and `Step 4.5: Visual Concept Elaborations (Diagramming)` into the ingestion pipeline, defining the `diagram_designer` subagent to generate and insert Mermaid.js diagrams automatically.
- **Mermaid Diagrams Integration:** Invoked `diagram_designer` to generate and insert 6 high-fidelity, standard-compliant Mermaid diagrams into Module 17 (Cognitive Map, Vertical vs. Horizontal Scaling, Load Balancer Probing/Eviction, SQL vs. NoSQL vs. Graph DB structure, Stateful vs. Stateless JWT Auth flows, and layered API Security Shielding).
- **MOC Indices (`Reference Notes/0-Index.md` & `Main Notes/0-Index.md`):** Updated the indexes: added Track 6 for systems scaling in Reference Index, and added a "Systems Design & Core Infrastructure" Dataview section for `role: infra` notes in Conceptual Index.
- **Decoupled PoC Architecture:** Modified the System Design module to strip out Nginx/code configs, redirecting queries to the Project file to keep the core brain conceptual.

---

## [2026-06-07] - Ingestion of Node Heartbeat and Eviction Q&A

### Added
- **`inflow/node_heartbeat_and_eviction_qa.md`**: Created inflow note consolidating Q&A on Kubelet heartbeats, unreachable/not-ready taints, and API patch concurrency.

### Changed / Updated
- **`Reference Notes/0-10_maintenance_upgrades_and_etcd.md`**: Added Section 1.5 detailing Kubelet node leases, unhealthy taints, eviction grace periods (toleration seconds), and why controllers use `PATCH` instead of `PUT` to prevent concurrency conflict errors.
- **`Reference Notes/0-13_scheduling_logging_and_lifecycle.md`**: Expanded Pod Tolerations documentation with details on wildcard (omitted) effect matching and multi-taint scheduling additive evaluation logic.

---

## [2026-06-07] - Cognitive Map Integration Across Reference Notes

### Added
- **`Reference Notes/0-1_kube_api_and_kubectl.md`**: Added a Mermaid-based cognitive flow mapping the journey from API Gate & Request Lifecycle to CLI command execution.
- **`Reference Notes/0-2_cluster_architecture_and_components.md`**: Added a Mermaid-based cognitive flow detailing macro cluster topologies, micro daemons, HA designs, and the declarative object model.
- **`Reference Notes/0-3_node_mechanics_and_resource_limits.md`**: Added a Mermaid-based cognitive flow covering node bootstrapping, telemetry/leases, host sandboxing (cgroups/namespaces), resource scheduling, and hardware managers.
- **`Reference Notes/0-4_workload_lifecycle_and_healing.md`**: Added a Mermaid-based cognitive flow mapping the four pillars of self-healing, automated probes, garbage collection, and failure PoC testing.
- **`Reference Notes/0-5_containers_runtimes_and_lifecycle.md`**: Added a Mermaid-based cognitive flow detailing OCI blueprints, sandbox namespaces, custom RuntimeClasses, init/sidecar topologies, and ephemeral debugging.
- **`Reference Notes/gitea_installation_and_workflows.md`**: Added a Mermaid-based cognitive flow tracing topology planning, host configuration (LVM), server installation, GitOps runners, and disaster recovery.
- **`Reference Notes/0-6_kubernetes_workloads_and_controllers.md`**: Added a Mermaid-based cognitive flow detailing CRI sandboxing, stateless/stateful/daemonset controllers, batch execution, autoscaling, and template packaging.
- **`Reference Notes/0-7_security_and_network_policies.md`**: Added a Mermaid-based cognitive flow outlining client authentication, RBAC authorization, container securityContexts, network policies, and cluster governance (PSA/PSS).
- **`Reference Notes/0-8_storage_mechanics_and_csi.md`**: Added a Mermaid-based cognitive flow mapping out-of-tree CSI architecture, local volumes, PV/PVC lifecycles, StorageClasses, and workload mounts.
- **`Reference Notes/0-9_networking_dns_and_ingress.md`**: Added a Mermaid-based cognitive flow detailing Linux network primitives, CNI overlays, Services (iptables/IPVS), DNS resolution, and Ingress/Gateway API.
- **`Reference Notes/0-10_maintenance_upgrades_and_etcd.md`**: Added a Mermaid-based cognitive flow outlining node cordoning/draining, HA cluster bootstrapping, version lifecycle upgrades, and ETCD state restoration.
- **`Reference Notes/0-11_troubleshooting_and_diagnostics.md`**: Added a Mermaid-based cognitive flow detailing application debugging, node logging, control-plane recovery, service networking diagnostics, and advanced JSONPath telemetry.
- **`Reference Notes/0-12_kubernetes_api_management_and_pod_immutability.md`**: Added a Mermaid-based cognitive flow outlining imperative vs. declarative API management, 3-way merge engine internals, Pod spec immutability boundaries, and recovery playbooks.
- **`Reference Notes/0-13_scheduling_logging_and_lifecycle.md`**: Added a Mermaid-based cognitive flow mapping advanced scheduling placement, metrics observability, container lifecycle configuration, and graceful eviction/termination.
- **`Reference Notes/0-14_cluster_administration_and_observability.md`**: Added a Mermaid-based cognitive flow mapping graceful/non-graceful shutdowns, swap memory cgroups, certificates management, admission webhooks, observability, APF, and coordinated leader elections.
- **`Reference Notes/0-15_kubernetes_api_extension_and_operators.md`**: Added a Mermaid-based cognitive flow covering schema registration (CRDs), custom controllers, the operator pattern, device plugins, and API aggregation.

---

## [2026-06-07] - Ingestion and Knowledge Distribution of CKA Exam Prep Video Course Clipping

### Added
- **`Reference Notes/0-6_kubernetes_workloads_and_controllers.md`**: Added Section 14 detailing Helm packaging command runs (`repo add/update`, `install`, `upgrade`, `rollback`, `uninstall`, `list`) and Kustomize overlays (using `resources` instead of deprecated `bases`, and the `kustomize edit fix` command).
- **`Reference Notes/0-7_security_and_network_policies.md`**: Added Section 6.6 containing a step-by-step walkthrough of RBAC service account (`dev-user`), role, and rolebinding configuration with `auth can-i` checks. Added Section 10.3 containing a step-by-step walkthrough of default deny-all NetworkPolicy and label-based allow rules.
- **`Reference Notes/0-8_storage_mechanics_and_csi.md`**: Added Section 5.3 detailing Rancher local-path provisioner installation and configuration as a hostPath dynamic storage provider.

### Changed / Updated
- **`Projects/CKA/Vim and Terminal Setup.md`**: Added copy-paste shortcuts (`Ctrl+Shift+C`/`Ctrl+Shift+V`), avoiding `Ctrl + W` terminal close error, SSH node hopping, and privilege elevation with `sudo -i`.
- **`Reference Notes/0-2_cluster_architecture_and_components.md`**: Added Section 3D detailing stacked HA control plane configuration with `kubeadm` (`--control-plane-endpoint` and `--upload-certs` flags for `kubeadm init`, and `--control-plane` and `--certificate-key` flags for `kubeadm join`).
- **`Reference Notes/0-3_node_mechanics_and_resource_limits.md`**: Added Section 1.1 detailing worker node kernel modules (`overlay`, `br_netfilter`), sysctl network parameters (`net.bridge.bridge-nf-call-iptables`, `net.ipv4.ip_forward`), and `containerd` cgroup configuration (`SystemdCgroup = true` in `config.toml`).
- **`Reference Notes/0-4_workload_lifecycle_and_healing.md`**: Expanded Section 2 with detailed HTTP GET and TCP Socket probes, and a line-by-line configuration mechanical breakdown.
- **`Reference Notes/0-6_kubernetes_workloads_and_controllers.md`**: Updated rolling update parameters (`maxSurge` / `maxUnavailable` defaults and validations) and history rollback commands (`rollout undo --to-revision`).
- **`Reference Notes/0-9_networking_dns_and_ingress.md`**: Updated Section 5.5 to document forwarding private DNS queries for `mycorp.com` to corporate DNS `10.10.0.53` within the CoreDNS ConfigMap Corefile with explanation blocks.
- **`Reference Notes/0-10_maintenance_upgrades_and_etcd.md`**: Updated Section 4.3 to document the step-by-step stacked ETCD snapshot restore process (stopping kubelet, restoring to `/var/lib/etcd-restored`, modifying `hostPath` volumes in `/etc/kubernetes/manifests/etcd.yaml`, and restarting kubelet).
- **`Reference Notes/0-11_troubleshooting_and_diagnostics.md`**: Refined Section 1A with a detailed ASCII/Mermaid flowchart illustrating Pod Status flow and troubleshooting checklist for ImagePull failures. Refined Section 2A to detail API Server "Connection Refused" diagnostics and host-level static pod manifest debugging (`kubelet` status, `crictl ps -a`, `crictl logs`, etc.).
- **`Reference Notes/0-13_scheduling_logging_and_lifecycle.md`**: Expanded Section 3 ("Label Subset Match Evaluation") with Case D containing a comprehensive mechanical breakdown of set-based operators (`NotIn`, `Exists`, `DoesNotExist`, `Gt`, `Lt`) using target node resource configurations. Added a detailed explanation breakdown for how required (filtering/predicates) and preferred (scoring/priorities) node affinity rules are evaluated together during the scheduling cycle phases. Documented the definition and enforcement mechanisms of Node Exclusivity (Taints & Tolerations) vs. Pod Exclusivity (Node Affinity) to clarify the combined repel-and-attract isolation paradigm. Documented reconciliation loop defaults and HA leader election lease configuration requirements (including concrete examples of collision vs. isolation, and `kubectl get leases` verification commands).

### Ingested Inflow Sources
The following files and assets have been processed and integrated:
- `inflow/Clippings/Kubernetes Course – Certified Kubernetes Administrator Exam Preparation (2026 Update).md`

---

## [2026-06-07] - Batch Integration of Missing Diagrams and CKA Practice Playbooks

### Added
- **CKA Practice Playbook (`Projects/CKA/Practice Playbook - Lightning Labs and Mock Exams.md`):** Created a comprehensive, high-fidelity playbook compiling practice questions, scenario requirements, diagnostic steps, CLI solutions, and YAML manifests from all Lightning Labs, Mock Exams 1-3, Ultimate Mocks (Troubleshooting, Storage, Services & Networking, General/Cluster State), and Network Policy Testing tips and tricks. Fully validated all internal links and relative paths.
- **CKA Practice Playbook - Topic Labs (`Projects/CKA/Practice Playbook - Topic Labs.md`):** Restructured and audited the draft Topic Labs playbook, deduplicating repetitive questions and injecting comprehensive CKA "Battle-Test Notes" for Troubleshooting, Cluster Architecture/Security, Services/Networking, Workloads/Scheduling, and Storage. Added complete practice scenarios for PersistentVolumes, PersistentVolumeClaims, and manual PVC mount injections.

### Changed / Updated
- **`Reference Notes/0-9_networking_dns_and_ingress.md`:** Replaced L7 host/path routing text blocks with a detailed Mermaid.js Ingress traffic routing and logical service connection diagram. Added a CKA Battle-Test FAQ section comparing `kubectl expose` vs `kubectl create service` for ClusterIP and NodePort, including CLI syntax and a capability matrix.
- **`Projects/CKA/0-Index.md`:** Added a CKA Battle-Test FAQ detailing the location and ingestion pipeline of mock exams/lightning labs, and explaining the RAG capabilities of this vault.
- **`README.md`:** Added details on the active RAG integration for the AI coding assistant.
- **`Reference Notes/0-2_cluster_architecture_and_components.md`:** Replaced high-level cluster architecture text references with a detailed Mermaid.js control plane/worker node interaction diagram and corresponding structural description.
- **`Main Notes/kube-apiserver.md`:** Integrated a Mermaid.js diagram illustrating the central coordination role of `kube-apiserver` in the control plane hierarchy.
- **`Reference Notes/0-5_containers_runtimes_and_lifecycle.md`:** Replaced text-based process namespace diagrams with structured Mermaid.js diagrams for Pod Sandbox namespaces (cgroups, net/ipc/uts isolation) and ephemeral container target namespace sharing.
- **`Main Notes/container-runtime-deeper.md`:** Added a Mermaid.js namespace sandboxing diagram under the Pause Container section, and corrected frontmatter metadata (`sub_type`, `source_type`).
- **`Reference Notes/0-13_scheduling_logging_and_lifecycle.md`:** Converted the text-based scheduling framework pipeline layout into a clean, complete Mermaid.js flowchart (synchronous scheduling cycle and asynchronous binding cycle). Enhanced the Labels & Selectors and Node Selectors sections with comprehensive context, Services-to-Pods mapping diagrams, and a step-by-step production database SSD node-labeling walkthrough. Corrected manual pod binding instructions to use `kubectl create` / `kubectl post --raw` (replacing the invalid `kubectl replace` endpoint typo). Added CKA Selector Syntax & Behaviors FAQ to document the user's specific learning questions in context. Added multiple real-world implementation scenarios and examples of taints and tolerations (including NoSchedule GPU nodes, NoExecute maintenance draining with grace periods, PreferNoSchedule resource overloading, and wildcard diagnostic daemons). Added a mechanical breakdown scenario for label subset matches under node affinity rules (comparing single/multiple rules under nodeSelector, required nodeSelectorTerms, and preferred affinity scoring).
- **`Main Notes/kube-scheduler-deeper.md`:** Integrated the detailed Scheduling Framework Mermaid.js flowchart under the Detailed Scheduling Pipeline section, and corrected frontmatter metadata (`sub_type`, `source_type`).
- **`Main Notes/ingress.md`:** Added the Ingress routing data plane flow diagram under the Architectural Context section.

### Ingested Inflow Sources
The following files and assets have been processed and integrated:
- `inflow/docs/14-Lightning-Labs/`
- `inflow/docs/15-Mock-Exams/`
- `inflow/docs/16-Ultimate-Mocks/`
- `inflow/docs/17-tips-and-tricks/`
- Mapped, analyzed, and translated diagram assets from `inflow/images/` to active Mermaid.js configurations.

---

## [2026-06-06] - Ingestion of Core Objects, Policies, Services, Security, and Extensibility Scraped Files

### Added
- **Reference Note (`Reference Notes/0-15_kubernetes_api_extension_and_operators.md`):** Created a comprehensive study module covering CustomResourceDefinitions (CRDs), Custom Controllers, Operator Pattern, Device Plugins, and API Aggregation.
- **Landing Notes in `Main Notes/`:**
  - `label.md` (landing)
  - `finalizer.md` (landing)
  - `limitrange.md` (landing)
  - `resourcequota.md` (landing)
  - `pod-security-admission.md` (landing)
  - `dynamic-resource-allocation.md` (landing)
  - `customresourcedefinition.md` (landing)
  - `operator-pattern.md` (landing)
  - `device-plugin.md` (landing)
  - `api-aggregation.md` (landing)
- **Deeper-dive Notes in `Main Notes/`:**
  - `label - Selectors and Character Syntax.md` (deeper-dive)
  - `finalizer - Owners and BlockOwnerDeletion.md` (deeper-dive)
  - `pod-security-admission - Standards and Modes.md` (deeper-dive)
  - `dynamic-resource-allocation - Security Hardening.md` (deeper-dive)
  - `customresourcedefinition - Subresources and Schema.md` (deeper-dive)
  - `operator-pattern - Controllers and Informers.md` (deeper-dive)
  - `service - Source IP and Pod Termination Lifecycle.md` (deeper-dive)
- **Digital Garden Pattern (`Digital Garden/Pattern - Securing Hardware Accelerator (GPU) Workloads via DRA.md`):** Documented alignment between Topology Manager, Dynamic Resource Allocation (DRA) status update RBAC checks, and Linux host-level NUMA/cgroup tuning.

### Changed / Updated
- **`Reference Notes/0-2_cluster_architecture_and_components.md`:** Integrated Section 6 covering Core Object Model, Names/ID restrictions, Label syntax/selectors, Annotations metadata, namespaces, finalizers, and ownerReferences/garbage collection.
- **`Reference Notes/0-3_node_mechanics_and_resource_limits.md`:** Added warning about physical host recreation node object consistency. Added Section 7 covering host mechanics (Linux kernel cgroups v1 vs v2, namespace sharing via pause containers, AppArmor/Seccomp host-level security profiles, and systemd journal Kubelet logs). Added Section 8 covering Resource requests/limits, LimitRanges, and ResourceQuotas. Added Section 9 covering PID limiting and Node Resource Managers (CPU Manager static/none, Memory Manager, Device Manager, and Topology Manager alignment policies).
- **`Reference Notes/0-7_security_and_network_policies.md`:** Added Section 11 covering ConfigMap vs Secret properties, tmpfs mounts, Secrets encryption-at-rest in etcd, and environment/volume injection. Added Section 12 covering Pod Security Admission (PSA) and Pod Security Standards (PSS) levels/modes. Added Section 13 covering Dynamic Resource Allocation (DRA) status updates, synthetic subresources (binding/driver), and node-aware verbs. Added Section 14 compiling the Kubernetes Security Checklist.
- **`Reference Notes/0-9_networking_dns_and_ingress.md`:** Added Section 4.4 covering client source IP preservation (`externalTrafficPolicy: Local` vs `Cluster`). Added Section 4.5 detailing the Pod and Endpoint termination graceful draining lifecycle flow, warning on API-level race conditions, and preStop hook sleep delay mitigations. Added Section 4.6 on Service selector connectivity routing checks.
- **`Main Notes/namespace.md`:** Integrated system namespaces (`default`, `kube-system`, `kube-public`, `kube-node-lease`) and custom namespace `kube-` prefix constraints.
- **`Projects/CKA/Exam Checklist - Core Architecture and API.md`:** Appended Section 7 detailing Custom Resource discovery checks and `OwnerRefInvalidNamespace` event lookup commands.
- **`Projects/CKA/Exam Checklist - Security and Storage.md`:** Appended Section 8 detailing PSA namespace labeling, Secrets encryption-at-rest etcd check, and namespace metadata label patch access restrictions.
- **`Projects/CKA/Exam Checklist - Troubleshooting and Networking.md`:** Appended Section 5 covering Kube-Proxy mode log checks, `externalTrafficPolicy` patching, and graceful termination preStop lifecycle configs.
- **`Projects/CKA/Exam Checklist - Workloads and Scheduling.md`:** Appended Section 12 covering ResourceQuotas/LimitRanges status lookups, CPU Manager static affinity Guaranteed QoS requirements, and host PID pressure diagnostics.

### Ingested Inflow Sources
The following files have been processed and integrated:
- `inflow/KubernetesOverviewDocs_Scraped.md`
- `inflow/Kubernets_Config_CKA_Docs_Scraped.md`
- `inflow/kubernetes_Policy_CKA_Docs_Scraped.md`
- `inflow/Service_TaskCKA_DOCS_Scraped.md`
- `inflow/Kubernetes_Security_CKA_Docs_Scraped.md`
- `inflow/KubernetesExtending_CKA_DOCS_Scraped.md`

---

## [2026-06-06] - Ingestion of Cluster Administration and Observability Pipeline

### Added
- **Reference Note (`Reference Notes/0-14_cluster_administration_and_observability.md`):** Created a comprehensive study module covering Graceful Node Shutdown, Swap memory management, Node autoscaling, Certificates API, Admission Webhooks, Observability/Logging/Metrics, Flow Control (APF), and Coordinated Leader Election.
- **Landing Notes in `Main Notes/`:**
  - `APIPriorityAndFairness.md` (landing)
  - `Graceful Node Shutdown.md` (landing)
  - `Swap Management.md` (landing)
  - `Coordinated Leader Election.md` (landing)
- **Digital Garden Pattern (`Digital Garden/Pattern - Host-Level OS Integration for Graceful Node Shutdown and Swap.md`):** Documented the interaction between Linux systemd inhibitors, kernel swap parameters, and Kubernetes Kubelet configuration.

### Changed / Updated
- **`Projects/CKA/Exam Checklist - Cluster Maintenance and Installation.md`:** Added CKA exam checklists and commands for configuring kubelet swap, approving CSRs, verifying graceful shutdown locks, inspecting APF flowschemas, and testing webhooks.
- **`Main Notes/kubelet.md` & `Main Notes/kube-apiserver.md`:** Updated reference guides to link to the new Module 15 reference note.

### Ingested Inflow Sources
The following files have been processed under the scraper pipeline:
- `inflow/ClusterAdministration_CKA_Docs_Scraped.md`

---

## [2026-06-06] - Update Ingestion Rules for Diagrams and Sub-links

### Changed / Updated
- **Agent Operating Rules ([Agent.md](file:///home/karim/Desktop/BrainDump/Agent.md)):** Configured the `@ingest` trigger rules to automatically translate/handle diagrams and recursively scrape key sub-links in external documentation URLs by default.
- **Ingestion Workflow Instructions ([instructions.md](file:///home/karim/Desktop/BrainDump/instructions.md)):** Codified Step 1 Link Identification and Resolution protocols to explicitly parse diagrams into Mermaid/image references and scrape relevant sub-links, allowing the scraped knowledge to be dynamically distributed to appropriate note files.

---

## [2026-06-05] - Implement @ingest Command and Process Workloads Documentation Ingestion

### Added
- **Command Integration (`@ingest`):** Added the `@ingest` command to [Agent.md](Agent.md) and [instructions.md](instructions.md). This command triggers automated URL scanning and scraping of external documentation links within inflow files, consolidating fetched page content with the notes before running the multi-agent ingestion pipeline (Phases 1-6).

### Changed / Updated
- **Workloads & Controllers Reference Module (`Reference Notes/0-6_kubernetes_workloads_and_controllers.md`):** Appended technical details on User Namespaces in Pods (hostUsers configuration, dynamic UID mapping, idmap volume mounts, runtime constraints), Job TTL after completion (`ttlSecondsAfterFinished` cascading cleanup), CronJob 52-character naming limits (Job name length skew), and Autoscaling (HPA controller loop/metric scaling formula, VPA recommender/updater/webhook components, and VPA update policies).
- **landing Note (`Main Notes/cronjob.md`):** Documented the DNS subdomain 52-character naming limit.
- **landing Note (`Main Notes/pod.md`):** Added User Namespace host isolation details to the Problem Solver section.
- **Exam Checklist (`Projects/CKA/Exam Checklist - Workloads and Scheduling.md`):** Appended CLI troubleshooting and verification playbooks for HPA metric checks, and User Namespace UID mapping lookups.

### Ingested Inflow Sources
The following files have been processed under the new `@ingest` scraper pipeline:
- `inflow/Workloads_CKA_Docs.md`

---

## [2026-06-05] - Full Ingestion of Scheduling, Services, and Storage Documentation URLs

### Changed / Updated
- **Scheduling & Lifecycle Reference Module (`Reference Notes/0-13_scheduling_logging_and_lifecycle.md`):** Appended technical details on Node-pressure eviction signals (memory, nodefs, imagefs, containerfs, pid), hard/soft eviction thresholds, NodeResourcesFit bin-packing scoring strategies (MostAllocated, RequestedToCapacityRatio, shape curves), PodGroups Gang/Co-scheduling, Topology-Aware Workload Scheduling (TAS) plugins, and Node Declared Features (KEP-5328) version skew validation.
- **Networking Reference Module (`Reference Notes/0-9_networking_dns_and_ingress.md`):** Corrected Service ClusterIP allocation band behavior (lower band reserved for static allocation, upper band for dynamic allocation) and documented the allocation offset formula.
- **Storage Reference Module (`Reference Notes/0-8_storage_mechanics_and_csi.md`):** Appended default VolumeSnapshotClass configuration using annotations (`snapshot.storage.kubernetes.io/is-default-class: "true"`), driver-matching dynamic resolution, and resolution conflict checks.
- **Deeper Note (`Main Notes/kube-scheduler - Priority Preemption and Topology Spread.md`):** Documented eviction signals, bin-packing score strategies, PodGroups gang scheduling, TAS plugins, and Node Declared Features.
- **Deeper Note (`Main Notes/service - EndpointSlices and Topology routing.md`):** Added DNS resolution formats for normal/headless services and Pods, and documented the Service ClusterIP allocation band formula.
- **Exam Checklist (`Projects/CKA/Exam Checklist - Workloads and Scheduling.md`):** Appended configurations and debugging steps for NodeResourcesFit bin-packing strategies, PodGroup co-scheduling validation, and Kubelet eviction thresholds.
- **Audit Script (`Reference Notes/scripts/review_vault.py`):** Updated the coverage decision matrix to ignore the new `Workloads_CKA_Docs.md` URL index.

### Ingested Inflow Sources
The following documentation URL index files have been processed and fully integrated:
- `inflow/Scheduling_CKA_Docs.md`
- `inflow/Services-LoadBalancers-Networking_CKA_Docs.md`
- `inflow/Storage_CKA_Docs.md`
- `inflow/Workloads_CKA_Docs.md`

---

## [2026-06-05] - Ingest Services/Networking and Storage Documentation Pages

### Added
- **Landing Note (`Main Notes/gateway-api.md`):** Created a landing note for the Gateway API, outlining its role-oriented design (GatewayClass, Gateway, Route), Ingress comparison, and porting capabilities.
- **Deeper Note (`Main Notes/service - EndpointSlices and Topology routing.md`):** Explains EndpointSlice chunking limits, conditions (`Serving` vs `Ready` vs `Terminating`), and Topology Aware Routing hints.
- **Deeper Note (`Main Notes/persistentvolumeclaim - Snapshots and Attributes.md`):** Explains VolumeSnapshots, snapshot restores, dynamic tuning via `VolumeAttributesClass`, and health monitoring sidecars.
- **Deeper Note (`Main Notes/persistentvolume - Ephemeral and Projected.md`):** Explains Projected Volumes, CSI inline ephemeral volumes, Generic Ephemeral Volumes, and local ephemeral storage quotas/eviction.
- **Architectural Pattern Note (`Digital Garden/Pattern - Multi-Zone Service Routing and Latency Mitigation.md`):** Explains how Gateway API and Topology Aware Routing hints map network connections inside availability zones.

### Changed / Updated
- **Storage Reference Module (`Reference Notes/0-8_storage_mechanics_and_csi.md`):** Added Section 6 covering Projected Volumes, CSI/Generic Ephemeral Volumes, VolumeSnapshots, CSIStorageCapacity tracking, VolumeAttributesClass performance scaling, and local storage eviction.
- **Networking Reference Module (`Reference Notes/0-9_networking_dns_and_ingress.md`):** Added Section 7 covering Gateway API specifications, EndpointSlices scalability, Topology Aware Routing, internalTrafficPolicy, and v1.26+ static/dynamic ClusterIP allocation.
- **Exam Checklist (`Projects/CKA/Exam Checklist - Troubleshooting and Networking.md`):** Appended Section 4.5 detailing Gateway API status troubleshooting, EndpointSlice health inspections, and node-local internalTrafficPolicy debug workflows.
- **Exam Checklist (`Projects/CKA/Exam Checklist - Security and Storage.md`):** Appended Section 7 detailing Projected Volume configs, ephemeral storage limits eviction diagnostics, and Generic Ephemeral Volume templates.

### Ingested Inflow Sources
The following documentation URL index files have been processed and fully integrated:
- `inflow/Services-LoadBalancers-Networking_CKA_Docs.md`
- `inflow/Storage_CKA_Docs.md`

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
- **Container Runtimes Reference Module (`Reference Notes/0-5_containers_runtimes_and_lifecycle.md`):** Ingested raw Mumshad transcripts to document Dockershim removal, the `cri-dockerd` adapter socket mechanics, manual Kubelet configuration, and the "Container Runtime Upgrade Trap" (Kubelet gRPC re-dial errors resolved via service restart).
- **Workloads & Controllers Reference Module (`Reference Notes/0-6_kubernetes_workloads_and_controllers.md`):** Integrated set-based selector operators, `ownerReferences` mechanics (adoption and orphaning), API validation safeguards, and advanced thrashing loop diagnostics.
- **Cluster Maintenance & ETCD Reference Module (`Reference Notes/0-10_maintenance_upgrades_and_etcd.md`):** Expanded details on ETCD client API v2 vs v3 management, persistent session configurations, and command-line syntax comparison.
- **API Management Reference Module (`Reference Notes/0-12_kubernetes_api_management_and_pod_immutability.md`):** Detailed the Mixed-Management Warning and the 2-Way Merge Fallback blind spot (where deletions fail due to missing last-applied-configuration annotations) and auto-recovery annotation patching.
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
- **Scheduling, Logging, and Lifecycle Reference Module (`Reference Notes/0-13_scheduling_logging_and_lifecycle.md`):** Integrated Phase 4 documentation detailing the automated verification script, its functionality, and commands on how to run it.

---

## [2026-06-05] - Context Expansion Audit of Scheduling, Logging, and Lifecycle Reference Module

### Changed / Updated
- **Scheduling, Logging, and Lifecycle Reference Module (`Reference Notes/0-13_scheduling_logging_and_lifecycle.md`):**
  - **ConfigMap Symlink & inotify Sync Mechanics:** Expanded the ConfigMap/Secret volume mounts section. Detailed Kubelet's atomic directory update mechanism (timestamped subdirectories, user-facing symlinks, and the atomic swap of the `..data` symlink). Documented inotify event propagation inside containers (directory-level vs. file-level watches). Explained the `subPath` inode binding gotcha which binds directly to a file inode, preventing the container from receiving updates when the symlink target changes.
  - **ETCD Encryption Verification & Envelope Encryption:** Detailed the ETCD encryption at rest mechanism. Contrasted static providers (`identity`, `aescbc`, `secretbox`) with external KMS envelope encryption (DEK/KEK generation, remote gRPC plugin calls, local caches). Provided a step-by-step diagnostic run sheet to SSH into the control plane node, query the raw secret directly using `etcdctl` with client certificates, and verify it contains the `k8s:enc:aescbc:v1:` prefix.
  - **Custom Scheduler Reconciliation Loop & Binding API Walkthrough:** Expanded the multiple custom schedulers section. Provided a detailed step-by-step explanation of the reconciliation loop (Watch/Informer, Queueing, Filtering/Predicates, Scoring/Priorities, Selection, Binding) with a Mermaid flow diagram. Included complete, practical script implementations in Python (using the official `kubernetes` client library) and Bash (using `kubectl` and `curl` against the `/binding` subresource API) demonstrating how to programmatically schedule pending pods.

---

## [2026-06-05] - Create Scheduling, Logging, and Lifecycle Reference Module

### Added
- **Scheduling, Logging, and Lifecycle Reference Module (`Reference Notes/0-13_scheduling_logging_and_lifecycle.md`):** Compiled raw log transcripts into a highly structured, comprehensive reference module covering Advanced Scheduling and Node Placement (Manual scheduling, labels/selectors, taints/tolerations, node affinity, taints vs affinity combinations, and multiple custom schedulers), Logging and Monitoring (Metrics Server architecture, Kubelet Summary API, and application logs queries), and Application Lifecycle (container commands/arguments overriding, environment variables direct config, envFrom, valueFrom, ConfigMaps, Secrets, base64 encoding/decoding, and etcd encryption at rest).

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
  - Updated frontmatter sources to include `Reference Notes/0-12_kubernetes_api_management_and_pod_immutability.md`.
- **Digital Garden Pattern Note (`Digital Garden/Pattern - Air-Gapped Git Architecture on RHEL.md`):**
  - Added section **GitOps Declarative Workflows & API Reconciliation Mechanics**: Connected the air-gapped version control server (Gitea) and host runner (`act_runner`) to declarative Kubernetes management. Detailed the client-side pre-flight validation cache and version skew issues, the 3-Way Merge Engine mechanics (role of `last-applied-configuration` annotation in tracking and processing field deletions), Server-Side Apply (SSA) (field ownership conflict resolutions under `metadata.managedFields`, and solving etcd metadata size constraints for large CRDs), and Pod spec immutability boundaries requiring the `/tmp/kubectl-edit-xxxx.yaml` recovery playbook using `kubectl replace --force` (triggering immediate cgroup teardown and container namespace unmounting via `SIGKILL`).
  - Updated frontmatter domains, components, sources, and tags to include `kubernetes`, `kubectl`, `pod`, `Reference Notes/0-12_kubernetes_api_management_and_pod_immutability.md`, and `kubernetes/gitops`.
  - Added references to the bottom of the note for `Reference Notes/0-12_kubernetes_api_management_and_pod_immutability.md` and `Reference Notes/scripts/verify_api_immutability.sh`.

---

## [2026-06-05] - Context Expansion Audit of API Management & Pod Immutability Reference Module

### Changed / Updated
- **API Management & Pod Immutability Reference Module (`Reference Notes/0-12_kubernetes_api_management_and_pod_immutability.md`):**
  - Expanded **Client-Side vs. Server-Side Validation**: Documented how `kubectl` validates manifests locally using Cached OpenAPI schemas (under `~/.kube/cache/schema`), how version skew and Custom Resource Definitions (CRDs) affect validation, and how `--validate=false` can bypass local pre-flight checks.
  - Expanded **Server-Side Apply (SSA)**: Added deep-dive explanations of Server-Side Apply (SSA) introduced as the default mechanism in v1.22+. Detailed field ownership tracking with `metadata.managedFields`, conflict detection, and how it resolves the metadata storage constraints of the `last-applied-configuration` annotation in `etcd`.
  - Expanded **Linux Process Signal Mechanics during Force Deletion**: Documented process-level behavior difference between graceful termination (SIGTERM, grace period countdown, and escalation to SIGKILL) and forceful deletion (immediate SIGKILL, grace-period=0, immediate cgroup and namespace cleanup).

---

## [2026-06-05] - Create API Management and Pod Immutability Reference Module

### Added
- **API Management & Pod Immutability Reference Module (`Reference Notes/0-12_kubernetes_api_management_and_pod_immutability.md`):** Compiled raw log transcripts into a highly structured reference module covering Declarative vs. Imperative Object Management (operational tradeoffs, exam vs. production workflows), the 3-Way Merge Engine (merge logic, the role of `last-applied-configuration` annotation in deletions, mixed-management warnings), Pod Immutability rules (reasons for immutability, exact mutable fields), and the `/tmp/kubectl-edit-xxxx.yaml` recovery workflow utilizing `kubectl replace --force`.
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
- **Kubernetes Security and Network Policies Reference Module (`Reference Notes/0-7_security_and_network_policies.md`):** Compiled a highly structured, comprehensive, and exhaustive Reference Module covering Kubernetes Security Primitives and Authentication (human vs. machine accounts, basic/token auth deprecation), TLS Basics & TLS in K8s (manual generation of CA, admin, apiserver, and kubelet certificates using openssl and cfssl, Subject Alternative Names, auditing certificate files), Certificates API (CertificateSigningRequest resources, spec.signerName values for v1, approval workflow, and Kubelet TLS bootstrapping), Kubeconfig (clusters, users, contexts structure, file merging), Authorization modes (Node, ABAC, RBAC, Webhook, AlwaysAllow/AlwaysDeny), RBAC (Role, RoleBinding, ClusterRole, ClusterRoleBinding, namespace scope, and kubectl auth can-i permission testing), ServiceAccounts (projected tokens, TokenRequest API v1.22+, manual secret-based token generation for v1.24+), Image Security (private registry credentials, docker-registry secrets, and ImagePullSecrets), SecurityContexts (Pod-level and Container-level users, groups, and Linux capabilities), and NetworkPolicies (Ingress/Egress, podSelector, namespaceSelector, ipBlock, and AND vs OR rules logic).

---

## [2026-06-05] - Create Storage Mechanics and CSI Reference Module

### Added
- **Storage Mechanics & CSI Reference Module (`Reference Notes/0-8_storage_mechanics_and_csi.md`):** Compiled a highly structured, comprehensive, and exhaustive Reference Module covering Container Storage Interface (CSI) architecture (Kubelet coordination, node vs. controller plugins, driver registration, sidecars), volume primitives (`emptyDir` and `hostPath` configurations, security risks, systemd/SELinux permissions, scheduling disconnects), PV and PVC mechanics (binding, access modes, reclaim policies, protection finalizers), Pod volume mounts, and StorageClasses (dynamic provisioning, `WaitForFirstConsumer` topology-aware scheduling, provisioners, online expansion).
- **Automated Verification Script (`Reference Notes/scripts/verify_storage_poc.sh`):** Created a production-grade bash verification script to test shared `emptyDir` mounts, `WaitForFirstConsumer` pending-to-bound transitions, and PVC deletion protection finalizers.

---

## [2026-06-05] - Create Networking, DNS, and Ingress Reference Module

### Added
- **Kubernetes Networking Reference Module (`Reference Notes/0-9_networking_dns_and_ingress.md`):** Created a comprehensive, production-grade study and reference module. Structured to cover Networking Prerequisites (Switching, routing, gateways, network namespaces, veth pairs, Linux bridge, NAT/MASQUERADE, DNAT), CNI specifications and host configurations (kubelet integration, plugins directory), Cluster & Pod networking (IPAM, WeaveNet overlay mechanism), Service networking (ClusterIP, NodePort, LoadBalancer routing, iptables vs IPVS proxy modes), DNS in Kubernetes (CoreDNS architecture, Corefile config, Pod/Service FQDN formats, /etc/resolv.conf search domains), and Ingress (Controllers vs Resources, routing patterns, SSL/TLS termination, rewrite-target annotations, networking.k8s.io/v1 templates).

---

## [2026-06-05] - Create Cluster Maintenance, Upgrades, and ETCD Reference Module

### Added
- **Reference Module (`Reference Notes/0-10_maintenance_upgrades_and_etcd.md`):** Compiled raw log transcripts into a highly structured, comprehensive reference module covering Node Maintenance (draining, cordoning), version skew policies, step-by-step kubeadm upgrade playbooks, ETCD snapshot backups and restores (for stacked and external topologies), High-Availability cluster architectures (stacked vs. external ETCD), and cluster bootstrapping using kubeadm with containerd systemd cgroups configurations.

---

## [2026-06-05] - Create Troubleshooting and Diagnostics Reference Note

### Added
- **Kubernetes Troubleshooting & Diagnostics Reference Note (`Reference Notes/0-11_troubleshooting_and_diagnostics.md`):** Compiled raw log transcripts into a highly structured, comprehensive Reference Module. The document covers:
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
- **Verification Script Documentation (`Reference Notes/0-6_kubernetes_workloads_and_controllers.md`):** Appended Section 13.7 documenting the verification script scope, execution instructions, and clean-up options.

---

## [2026-06-05] - Kubernetes Workloads & Controllers Reference Note Expansion

### Refactored / Upgraded
- **Context Expansion Audit in Workloads & Controllers Reference Note (`Reference Notes/0-6_kubernetes_workloads_and_controllers.md`):**
  - **Linux Namespaces & Cgroups (CRI/OCI Level):** Added detailed architectural explanations for kernel namespaces (`net`, `ipc`, `pid`, `mnt`, `uts`, `user`). Documented the hierarchy and structural differences between cgroups v1 and v2. Explained resource constraints mapping to Completely Fair Scheduler (CFS) bandwidth quotas/periods and OOM killer score adjustment math (`oom_score_adj`) across QoS classes.
  - **Shared Pod IPC & Unix Sockets:** Documented container-to-container communication mechanics. Included complete, runnable YAML configurations for loopback port sharing and shared Unix domain sockets using `emptyDir` mounts.
  - **StatefulSet DNS & CoreDNS Resolution:** Documented the CoreDNS mapping mechanisms (A and SRV records) for StatefulSets. Provided a detailed troubleshooting run sheet using network debugging tools (`nslookup`, `dig`, `host`).
  - **gRPC Health Probe Protocol:** Explained protocol specifications for native gRPC probes, including the `grpc.health.v1.Health` service definition, Kubelet interaction mechanics, and success/failure criteria. Updated the reference YAML config to show gRPC health probes.

---

## [2026-06-05] - Create Kubernetes Workloads & Controllers Reference Module

### Added
- **Kubernetes Workloads & Controllers Reference Module (`Reference Notes/0-6_kubernetes_workloads_and_controllers.md`):** Created a comprehensive, production-grade study and reference module. Structured to cover Pods (Sandbox creation, namespace sharing), Pod Lifecycle (Phases, states, CrashLoopBackOff, conditions, readiness gates, hooks), Init and Native Sidecar containers (Resource calculations, sequencing, teardown), Ephemeral containers (kubectl debug), Health Probes (Liveness, Readiness, Startup, HTTP/TCP/Exec/gRPC handlers), Static Pods (configurations, mirror pods), ReplicaSets, Deployments (RollingUpdate, Recreate strategies, rollbacks), StatefulSets (Headless Services, stable identities, Volume Claim Templates), DaemonSets, and Jobs/CronJobs. Included a complete verification run sheet of kubectl commands.

---

## [2026-06-05] - Gitea Ingestion Crossover Audit & CKA Checklist Update

### Added
- **CKA Exam Checklist Expansion (`Projects/CKA/Exam Checklist - Core Architecture and API.md`):**
  - Appended **Systemd Service & Kubelet Debugging** guidelines (using `systemctl` status/restart, `journalctl -u kubelet -e` to read log ends, systemd daemon-reload commands, and swap/cgroup troubleshooting).
  - Appended **HostPath Volume & Directory Traversal Troubleshooting** guidelines (explaining how directory execute `x` permissions on the host affect containers, FACL `setfacl` permissions bypass, how symlinks resolve during `hostPath` mounting, and SELinux contexts).

### Audited
- Audited `Reference Notes/gitea_installation_and_workflows.md`, `Main Notes/gitea.md`, and `Digital Garden/Pattern - Air-Gapped Git Architecture on RHEL.md` to extract high-yield crossover topics related to Linux systemd services and directory traversal permissions for Kubernetes cluster administrator tasks.

---

## [2026-06-05] - Create Air-Gapped Git Architecture Pattern Note

### Added
- **Digital Garden Pattern Note (`Digital Garden/Pattern - Air-Gapped Git Architecture on RHEL.md`):** Created a cross-domain architectural pattern note connecting git, linux, and database domains, and components `[[gitea]]`, `[[mysql]]`, `[[lvm]]`, `[[systemd]]`, and `[[openssh]]`. Detailed the coordination of unprivileged execution, SSH forced-commands, LVM symlink routing, MySQL database tenant isolation, and `act_runner` native host execution. Provided security critique comparison tables and RHEL service unit configuration sheets.

---

## [2026-06-05] - Gitea Installation Security Audit Script

### Added
- **Gitea Verification Script (`Reference Notes/scripts/verify_gitea_setup.sh`):** Created a robust, production-grade bash verification audit script to inspect a RHEL 8 host and verify Gitea conforms to security and architectural guidelines (User verification, storage/symlink checks, root:git permission flags, FACL traversal permissions, Systemd variables validation, port binding checks, and SELinux contexts).
- **Audit Documentation Integration:** Appended Section 12 to `Reference Notes/gitea_installation_and_workflows.md` outlining the execution command and verification scope of the diagnostics script.

---

## [2026-06-05] - Gitea Reference Note Context Expansion Audit

### Refactored / Upgraded
- **Context Expansion Audit in Gitea Reference Note (`Reference Notes/gitea_installation_and_workflows.md`):**
  - **Apache Reverse Proxy Snippet:** Added full SSL virtual host configuration block on port `:444` using `ProxyPass`, `ProxyPassReverse`, and `ProxyPreserveHost` directives, with architectural explanations of path preservation (`nocanon`), host header forwarding, and client real IP tracking with Gitea config (`REVERSE_PROXY_LIMIT` and `TRUSTED_PROXIES`).
  - **LVM & lsblk Concepts:** Expanded physical storage concepts (PV, VG, LV) with a Mermaid diagram, and provided a detailed step-by-step CLI run sheet on RHEL 8 to identify, create, extend (`vgextend` / `lvextend`), and resize filesystems (`xfs_growfs` / `resize2fs`) online for `/app`.
  - **OpenSSH Daemon (sshd) Configuration:** Documented sshd service configurations (`/etc/ssh/sshd_config`), active parameters required for Gitea's SSH multiplexing (`PubkeyAuthentication` and `AuthorizedKeysFile`), directory/file permissions (`StrictModes`), and RHEL 8 SELinux policy contexts (`restorecon` and `ssh_home_t`).
  - **Native Host CI/CD Security:** Addressed security trade-offs of the native host executor (`:host`) compared to container environments, detailing potential RCE, privilege escalation, and resource exhaustion vectors alongside mitigation guidelines (running unprivileged, restricting sudoers, and setting Systemd resource limits).

---


## [2026-06-05] - Second Brain & Digital Garden Expansion

### Added
- **Gitea Reference Note:** Created `Reference Notes/gitea_installation_and_workflows.md` detailing air-gapped installation, SQLite vs MySQL decisions, LVM storage design with symlinks, OpenSSH multiplexing/forced command Git-over-SSH mechanics, act_runner configuration with native host executor, custom pre-receive hooks for branch naming rules, and active-passive disaster recovery rollback playbooks.
- **CKA Exam Core Checklist:** Created `Projects/CKA/Exam Checklist - Core Architecture and API.md` mapping etcd backup/restore, Kubelet static pods pathing, scheduler bypass (spec.nodeName & Binding API), health probes (Startup, Liveness, Readiness via Exec/HTTP/TCP), and local `crictl` & `journalctl` diagnostics.
- **Specialized Subagent Team:** Defined 5 custom AI subagents under the repository namespace:
  - `ResearchAgent` (`research_refinement`): Cleans and refines raw Gemini logs and transcripts into Reference Notes.
  - `AuditAgent` (`research_audit`): Audits reference notes, identifies tangent domains, and appends background/explanations to keep notes self-contained.
  - `MultiDomainPoCAgent` (`poc_developer`): Programs high-density, accurate, hands-on Verification PoCs in Reference Notes across all domains (Linux, AWS, Kubernetes, Databases, Networking).
  - `GardenAgent` (`garden_architect`): Cultivates the `Digital Garden/` and connects cross-domain components into patterns.
  - `CKAExamAgent` (`cka_exam_expert`): Condenses study materials into exam-focused checklists, mock reviews, and VIM setups inside `Projects/CKA/`.
- **Dedicated Digital Garden (`Digital Garden/`):** Created a root folder specifically for mapping domains and architectural patterns, and moved the `Pattern - Postgres on EKS.md` here.
- **Projects Directory (`Projects/`):** Created a project folder containing `Projects/CKA/` specifically for CKA Exam preparation.
- **CKA Exam Workspace Notes:** Created `Projects/CKA/0-Index.md` (exam MOC) and `Projects/CKA/Vim and Terminal Setup.md` (high-speed commands and configs).
- **Reference Notes Index (`Reference Notes/0-Index.md`):** Created a dynamic index MOC to list detailed study modules and PoCs.
- **Digital Garden Index (`Digital Garden/0-Index.md`):** Created a dynamic MOC table to list architectural patterns.
- **Dynamic MOC Indexes:** Updated `Main Notes/0-Index.md` to point its pattern queries to the new `Digital Garden/` directory.

### Refactored / Upgraded
- **Landing Notes Properties:** Refactored properties across all 11 landing notes using Python automation to inject `domains: ["kubernetes"]` and `against: []` (opposing ideas/approaches).
- **Agent Profile (`Agent.md`):** Updated definition to govern multi-domain Second Brain structures, diverse inflow tracking, dynamic Dataview query enforcement, and the sequential execution pipeline.
- **Ingestion Skill (`instructions.md`):** Updated templates to incorporate source provenance metadata (`source_type`, `source_url`, `author`, `course_title`), `against` properties, and the new Architectural Pattern note schema.
- **Ingestion Workflow Chaining:** Documented and configured the default sequential ingestion pipeline (`ResearchAgent` -> `AuditAgent` -> `MultiDomainPoCAgent` -> Concepts -> `GardenAgent` -> `CKAExamAgent`) in both `instructions.md` and `Agent.md` to trigger on every new note ingestion by default, ensuring that after the initial refinement, secondary domains are audited/expanded with volume by `AuditAgent`, before PoC, Main Notes, Digital Garden, and `CKAExamAgent` checklists are created.

---

## [2026-05-31] - Two-Tier Knowledge Vault Reorganization

### Added
- **MOC Index File (`Main Notes/0-Index.md`):** Created a central Map of Content (MOC) index note for unified conceptual navigation across landing and deeper dive notes.
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
- **[0-1_kube_api_and_kubectl.md](0-1_kube_api_and_kubectl.md):** Integrated Kube API Server request lifecycle details (creation flow, auth, schemas, scheduling binding, Kubelet execution).
- **[0-2_cluster_architecture_and_components.md](0-2_cluster_architecture_and_components.md):** Expanded core control plane components:
  - **API Server:** Added configuration details, systemd vs. static pod manifest verification, and execution checking.
  - **ETCD:** Added SQL vs Key-Value context, client/peer communication ports (2379/2380), Raft consensus peer configs, API v2 vs v3 migration commands (`put` vs `set`, versioning), and TLS-authorized registry keys check command.
  - **Kube Scheduler:** Added Filtering (predicates) and Ranking (priorities) pipeline descriptions, multiple custom schedulers context, and verification paths.
  - **Kube Proxy:** Added Services as virtual memory routing tables, host-level `iptables`/`IPVS` redirection mechanisms, and DaemonSet deployment verification.
  - **Reference Table:** Compiled a unified configuration paths guide for all control plane and core components.
- **[0-3_node_mechanics_and_resource_limits.md](0-3_node_mechanics_and_resource_limits.md):** Integrated Kubelet host system agent specifics, manual installation instructions (downloading binary, systemd configurations), and process verification flags.
- **[0-5_containers_runtimes_and_lifecycle.md](0-5_containers_runtimes_and_lifecycle.md):** Consolidated container runtimes evolution:
  - **Evolution & Decoupling:** Added Docker platform components, Dockershim adapter deprecation history (removed in v1.24), and native CRI/cri-dockerd setups.
  - **CLI Tools Comparison:** Added comparison table for CTR (debugging containerd), NerdCTL (Docker-compatible containerd shell, eStargz lazy pulls, P2P, signing), and Crictl (CRI troubleshooting debugger, Pod listing, Kubelet GC warnings).
  - **Endpoints Socket Skew:** Added default socket checklist and session export configurations.

### Changed / Updated
- **Cross-Module Consistency:** Fixed broken links in Modules 01, 03, and 04 pointing to renamed headings in Module 02. Verified complete linkage vault compliance.
- **Git Synchronization:** Updated SSH configurations to route github.com over port 443 (via ssh.github.com) to resolve local port 22 blocks, and pushed all updates.

---

## [2026-05-29] - Ingestion & Consolidation of Container Mechanics

### Added
- **[0-5_containers_runtimes_and_lifecycle.md](0-5_containers_runtimes_and_lifecycle.md):** Compiled raw notes from `inflow/Containers.md` into a structured, production-grade guide covering OCI images, Kubelet-CRI architecture, process isolation topology via `RuntimeClass` and micro-virtualization overhead, custom container setup/shutdown hooks, standard and native sidecars, and `ephemeralContainers` process namespace target troubleshooting.
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
  - [0-1_kube_api_and_kubectl.md](file:///home/karim/Desktop/CKA/0-1_kube_api_and_kubectl.md) linked to `0-2_cluster_architecture_and_components.md`.
  - [0-2_cluster_architecture_and_components.md](file:///home/karim/Desktop/CKA/0-2_cluster_architecture_and_components.md) linked to `0-1_kube_api_and_kubectl.md`, `0-3_node_mechanics_and_resource_limits.md`, and `0-4_workload_lifecycle_and_healing.md`.
  - [0-3_node_mechanics_and_resource_limits.md](file:///home/karim/Desktop/CKA/0-3_node_mechanics_and_resource_limits.md) linked to `0-2_cluster_architecture_and_components.md` and `0-4_workload_lifecycle_and_healing.md`.
  - [0-4_workload_lifecycle_and_healing.md](file:///home/karim/Desktop/CKA/0-4_workload_lifecycle_and_healing.md) linked to `0-2_cluster_architecture_and_components.md` and `0-3_node_mechanics_and_resource_limits.md`.

---

## [Before 2026-05-27] - Initial Knowledge Base Creation

### Added
- **Core Study Modules:**
  - [0-1_kube_api_and_kubectl.md](file:///home/karim/Desktop/CKA/0-1_kube_api_and_kubectl.md) (API server, API Groups, explain, Watch, kubectl syntax, output formats).
  - [0-2_cluster_architecture_and_components.md](file:///home/karim/Desktop/CKA/0-2_cluster_architecture_and_components.md) (Control plane vs worker, etcd/scheduler/controllers, HA design, CCM, version skew proxy).
  - [0-3_node_mechanics_and_resource_limits.md](file:///home/karim/Desktop/CKA/0-3_node_mechanics_and_resource_limits.md) (Node conditions, leases/heartbeats, cgroups, QoS classes, container runtimes).
  - [0-4_workload_lifecycle_and_healing.md](file:///home/karim/Desktop/CKA/0-4_workload_lifecycle_and_healing.md) (Self-healing pillars, probes, garbage collection).
- **Core Index & Guide:**
  - [README.md](file:///home/karim/Desktop/CKA/README.md) containing the architectural Mermaid.js "Brain Map" and course indexes.
  - [instructions.md](file:///home/karim/Desktop/CKA/instructions.md) outlining standard ingestion and formatting guidelines.

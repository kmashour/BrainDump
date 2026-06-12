---
domains:
  - "kubernetes"
  - "scheduling"
---

# Advanced Scheduling in Kubernetes

**Source:** https://kubernetes.io/blog/2017/03/advanced-scheduling-in-kubernetes/

---

Title: Live Content Description: Fetched live Source: https://kubernetes.io/blog/2017/03/advanced-scheduling-in-kubernetes/ \--- [Kubernetes](https://kubernetes.io/)

  * [Documentation](https://kubernetes.io/docs/home/)
  * [Kubernetes Blog](https://kubernetes.io/blog/)
  * [Training](https://kubernetes.io/training/)
  * [Careers](https://kubernetes.io/careers/)
  * [Partners](https://kubernetes.io/partners/)
  * [Community](https://kubernetes.io/community/)
  * Versions
    * [Release Information](https://kubernetes.io/releases)
    * [v1.36](https://kubernetes.io)
    * [v1.35](https://v1-35.docs.kubernetes.io)
    * [v1.34](https://v1-34.docs.kubernetes.io)
    * [v1.33](https://v1-33.docs.kubernetes.io)
    * [v1.32](https://v1-32.docs.kubernetes.io)

  * English
    * বাংলা (Bengali) [__](https://kubernetes.io/bn/)
    * 中文 (Chinese)[__](https://kubernetes.io/zh-cn/)
    * Français (French)[__](https://kubernetes.io/fr/)
    * Deutsch (German)[__](https://kubernetes.io/de/)
    * हिन्दी (Hindi)[__](https://kubernetes.io/hi/)
    * Bahasa Indonesia (Indonesian)[__](https://kubernetes.io/id/)
    * Italiano (Italian)[__](https://kubernetes.io/it/)
    * 日本語 (Japanese)[__](https://kubernetes.io/ja/)
    * 한국어 (Korean)[__](https://kubernetes.io/ko/)
    * فارسی (Persian)[__](https://kubernetes.io/fa/)
    * Polski (Polish)[__](https://kubernetes.io/pl/)
    * Português (Portuguese)[__](https://kubernetes.io/pt-br/)
    * Русский (Russian)[__](https://kubernetes.io/ru/)
    * Español (Spanish)[__](https://kubernetes.io/es/)
    * Українська (Ukrainian)[__](https://kubernetes.io/uk/)
    * Tiếng Việt (Vietnamese)[__](https://kubernetes.io/vi/)

  *     * Light
    * Dark
    * Auto



#### ![](https://kubernetes.io/images/announcements/kccnc-india-2026-black.svg) [KubeCon + CloudNativeCon India 2026](https://events.linuxfoundation.org/kubecon-cloudnativecon-india/)

Join us for two days of incredible opportunities to collaborate, learn and share with the cloud native community.  
[Buy your ticket now! 18 - 19 June | Mumbai, India](https://events.linuxfoundation.org/kubecon-cloudnativecon-india/register/?utm_source=kubernetes&utm_medium=homepage&utm_campaign=KubeCon-India-2026&utm_content=hero)

Hide this notice

## Kubernetes Blog

  *     * 2026
      * [From Kubernetes Dashboard to Headlamp: Understanding the Transition](https://kubernetes.io/blog/2026/06/01/dashboard-to-headlamp/)
      * [Reconciling the Past: Correcting Records for Unfixed Kubernetes CVEs](https://kubernetes.io/blog/2026/05/26/reconciling-unfixed-kubernetes-cves/)
      * [Announcing etcd 3.7.0-beta.0](https://kubernetes.io/blog/2026/05/20/etcd-370-beta/)
      * [Kubernetes v1.36: New Metric for Route Sync in the Cloud Controller Manager](https://kubernetes.io/blog/2026/05/15/ccm-new-metric-route-sync-total/)
      * [Kubernetes v1.36: Mixed Version Proxy Graduates to Beta](https://kubernetes.io/blog/2026/05/15/kubernetes-1-36-feature-mixed-version-proxy-beta/)
      * [Kubernetes v1.36: Deprecation and removal of Service ExternalIPs](https://kubernetes.io/blog/2026/05/14/kubernetes-v1-36-deprecation-and-removal-of-service-externalips/)
      * [Kubernetes v1.36: Advancing Workload-Aware Scheduling](https://kubernetes.io/blog/2026/05/13/kubernetes-v1-36-advancing-workload-aware-scheduling/)
      * [Kubernetes v1.36: PSI Metrics for Kubernetes Graduates to GA](https://kubernetes.io/blog/2026/05/12/kubernetes-v1-36-psi-metrics-ga/)
      * [Kubernetes v1.36: Moving Volume Group Snapshots to GA](https://kubernetes.io/blog/2026/05/08/kubernetes-v1-36-volume-group-snapshot-ga/)
      * [Kubernetes v1.36: More Drivers, New Features, and the Next Era of DRA](https://kubernetes.io/blog/2026/05/07/kubernetes-v1-36-dra-136-updates/)
      * [Kubernetes v1.36: Server-Side Sharded List and Watch](https://kubernetes.io/blog/2026/05/06/kubernetes-v1-36-server-side-sharded-list-and-watch/)
      * [Kubernetes v1.36: Declarative Validation Graduates to GA](https://kubernetes.io/blog/2026/05/05/kubernetes-v1-36-declarative-validation-ga/)
      * [Kubernetes v1.36: Admission Policies That Can't Be Deleted](https://kubernetes.io/blog/2026/05/04/kubernetes-v1-36-manifest-based-admission-control/)
      * [Kubernetes v1.36: Pod-Level Resource Managers (Alpha)](https://kubernetes.io/blog/2026/05/01/kubernetes-v1-36-feature-pod-level-resource-managers-alpha/)
      * [Kubernetes v1.36: In-Place Vertical Scaling for Pod-Level Resources Graduates to Beta](https://kubernetes.io/blog/2026/04/30/kubernetes-v1-36-inplace-pod-level-resources-beta/)
      * [Kubernetes v1.36: Tiered Memory Protection with Memory QoS](https://kubernetes.io/blog/2026/04/29/kubernetes-v1-36-memory-qos-tiered-protection/)
      * [Kubernetes v1.36: Staleness Mitigation and Observability for Controllers](https://kubernetes.io/blog/2026/04/28/kubernetes-v1-36-staleness-mitigation-for-controllers/)
      * [Kubernetes v1.36: Mutable Pod Resources for Suspended Jobs (beta)](https://kubernetes.io/blog/2026/04/27/kubernetes-v1-36-mutable-pod-resources-for-suspended-jobs/)
      * [Kubernetes v1.36: Fine-Grained Kubelet API Authorization Graduates to GA](https://kubernetes.io/blog/2026/04/24/kubernetes-v1-36-fine-grained-kubelet-authorization-ga/)
      * [Kubernetes v1.36: User Namespaces in Kubernetes are finally GA](https://kubernetes.io/blog/2026/04/23/kubernetes-v1-36-userns-ga/)
      * [SELinux Volume Label Changes goes GA (and likely implications in v1.37)](https://kubernetes.io/blog/2026/04/22/breaking-changes-in-selinux-volume-labeling/)
      * [Kubernetes v1.36: ハル (Haru)](https://kubernetes.io/blog/2026/04/22/kubernetes-v1-36-release/)
      * [Gateway API v1.5: Moving features to Stable](https://kubernetes.io/blog/2026/04/21/gateway-api-v1-5/)
      * [Kubernetes v1.36 Sneak Peek](https://kubernetes.io/blog/2026/03/30/kubernetes-v1-36-sneak-peek/)
      * [Announcing Ingress2Gateway 1.0: Your Path to Gateway API](https://kubernetes.io/blog/2026/03/20/ingress2gateway-1-0-release/)
      * [Running Agents on Kubernetes with Agent Sandbox](https://kubernetes.io/blog/2026/03/20/running-agents-on-kubernetes-with-agent-sandbox/)
      * [Securing Production Debugging in Kubernetes](https://kubernetes.io/blog/2026/03/18/securing-production-debugging-in-kubernetes/)
      * [The Invisible Rewrite: Modernizing the Kubernetes Image Promoter](https://kubernetes.io/blog/2026/03/17/image-promoter-rewrite/)
      * [Announcing the AI Gateway Working Group](https://kubernetes.io/blog/2026/03/09/announcing-ai-gateway-wg/)
      * [Before You Migrate: Five Surprising Ingress-NGINX Behaviors You Need to Know](https://kubernetes.io/blog/2026/02/27/ingress-nginx-before-you-migrate/)
      * [Spotlight on SIG Architecture: API Governance](https://kubernetes.io/blog/2026/02/12/sig-architecture-api-spotlight/)
      * [Introducing Node Readiness Controller](https://kubernetes.io/blog/2026/02/03/introducing-node-readiness-controller/)
      * [New Conversion from cgroup v1 CPU Shares to v2 CPU Weight](https://kubernetes.io/blog/2026/01/30/new-cgroup-v1-to-v2-cpu-conversion-formula/)
      * [Ingress NGINX: Statement from the Kubernetes Steering and Security Response Committees](https://kubernetes.io/blog/2026/01/29/ingress-nginx-statement/)
      * [Experimenting with Gateway API using kind](https://kubernetes.io/blog/2026/01/28/experimenting-gateway-api-with-kind/)
      * [Cluster API v1.12: Introducing In-place Updates and Chained Upgrades](https://kubernetes.io/blog/2026/01/27/cluster-api-v1-12-release/)
      * [Headlamp in 2025: Project Highlights](https://kubernetes.io/blog/2026/01/22/headlamp-in-2025-project-highlights/)
      * [Announcing the Checkpoint/Restore Working Group](https://kubernetes.io/blog/2026/01/21/introducing-checkpoint-restore-wg/)
      * [Uniform API server access using clientcmd](https://kubernetes.io/blog/2026/01/19/clientcmd-apiserver-access/)
      * [Kubernetes v1.35: Restricting executables invoked by kubeconfigs via exec plugin allowList added to kuberc](https://kubernetes.io/blog/2026/01/09/kubernetes-v1-35-kuberc-credential-plugin-allowlist/)
      * [Kubernetes v1.35: Mutable PersistentVolume Node Affinity (alpha)](https://kubernetes.io/blog/2026/01/08/kubernetes-v1-35-mutable-pv-nodeaffinity/)
      * [Kubernetes v1.35: A Better Way to Pass Service Account Tokens to CSI Drivers](https://kubernetes.io/blog/2026/01/07/kubernetes-v1-35-csi-sa-tokens-secrets-field-beta/)
      * [Kubernetes v1.35: Extended Toleration Operators to Support Numeric Comparisons (Alpha)](https://kubernetes.io/blog/2026/01/05/kubernetes-v1-35-numeric-toleration-operators/)
      * [Kubernetes v1.35: New level of efficiency with in-place Pod restart](https://kubernetes.io/blog/2026/01/02/kubernetes-v1-35-restart-all-containers/)
    * 2025
      * [Kubernetes 1.35: Enhanced Debugging with Versioned z-pages APIs](https://kubernetes.io/blog/2025/12/31/kubernetes-v1-35-structured-zpages/)
      * [Kubernetes v1.35: Watch Based Route Reconciliation in the Cloud Controller Manager](https://kubernetes.io/blog/2025/12/30/kubernetes-v1-35-watch-based-route-reconciliation-in-ccm/)
      * [Kubernetes v1.35: Introducing Workload Aware Scheduling](https://kubernetes.io/blog/2025/12/29/kubernetes-v1-35-introducing-workload-aware-scheduling/)
      * [Kubernetes v1.35: Fine-grained Supplemental Groups Control Graduates to GA](https://kubernetes.io/blog/2025/12/23/kubernetes-v1-35-fine-grained-supplementalgroups-control-ga/)
      * [Kubernetes v1.35: Kubelet Configuration Drop-in Directory Graduates to GA](https://kubernetes.io/blog/2025/12/22/kubernetes-v1-35-kubelet-config-drop-in-directory-ga/)
      * [Avoiding Zombie Cluster Members When Upgrading to etcd v3.6](https://kubernetes.io/blog/2025/12/21/preventing-etcd-zombies/)
      * [Kubernetes 1.35: In-Place Pod Resize Graduates to Stable](https://kubernetes.io/blog/2025/12/19/kubernetes-v1-35-in-place-pod-resize-ga/)
      * [Kubernetes v1.35: Job Managed By Goes GA](https://kubernetes.io/blog/2025/12/18/kubernetes-v1-35-job-managedby-for-jobs-goes-ga/)
      * [Kubernetes v1.35: Timbernetes (The World Tree Release)](https://kubernetes.io/blog/2025/12/17/kubernetes-v1-35-release/)
      * [Kubernetes v1.35 Sneak Peek](https://kubernetes.io/blog/2025/11/26/kubernetes-v1-35-sneak-peek/)
      * [Kubernetes Configuration Good Practices](https://kubernetes.io/blog/2025/11/25/configuration-good-practices/)
      * [Ingress NGINX Retirement: What You Need to Know](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/)
      * [Announcing the 2025 Steering Committee Election Results](https://kubernetes.io/blog/2025/11/09/steering-committee-results-2025/)
      * [Gateway API 1.4: New Features](https://kubernetes.io/blog/2025/11/06/gateway-api-v1-4/)
      * [7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)](https://kubernetes.io/blog/2025/10/20/seven-kubernetes-pitfalls-and-how-to-avoid/)
      * [Spotlight on Policy Working Group](https://kubernetes.io/blog/2025/10/18/wg-policy-spotlight-2025/)
      * [Introducing Headlamp Plugin for Karpenter - Scaling and Visibility](https://kubernetes.io/blog/2025/10/06/introducing-headlamp-plugin-for-karpenter/)
      * [Announcing Changed Block Tracking API support (alpha)](https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/)
      * [Kubernetes v1.34: Pod Level Resources Graduated to Beta](https://kubernetes.io/blog/2025/09/22/kubernetes-v1-34-pod-level-resources/)
      * [Kubernetes v1.34: Recovery From Volume Expansion Failure (GA)](https://kubernetes.io/blog/2025/09/19/kubernetes-v1-34-recover-expansion-failure/)
      * [Kubernetes v1.34: DRA Consumable Capacity](https://kubernetes.io/blog/2025/09/18/kubernetes-v1-34-dra-consumable-capacity/)
      * [Kubernetes v1.34: Pods Report DRA Resource Health](https://kubernetes.io/blog/2025/09/17/kubernetes-v1-34-pods-report-dra-resource-health/)
      * [Kubernetes v1.34: Moving Volume Group Snapshots to v1beta2](https://kubernetes.io/blog/2025/09/16/kubernetes-v1-34-volume-group-snapshot-beta-2/)
      * [Kubernetes v1.34: Decoupled Taint Manager Is Now Stable](https://kubernetes.io/blog/2025/09/15/kubernetes-v1-34-decoupled-taint-manager-is-now-stable/)
      * [Kubernetes v1.34: Autoconfiguration for Node Cgroup Driver Goes GA](https://kubernetes.io/blog/2025/09/12/kubernetes-v1-34-cri-cgroup-driver-lookup-now-ga/)
      * [Kubernetes v1.34: Mutable CSI Node Allocatable Graduates to Beta](https://kubernetes.io/blog/2025/09/11/kubernetes-v1-34-mutable-csi-node-allocatable-count/)
      * [Kubernetes v1.34: Use An Init Container To Define App Environment Variables](https://kubernetes.io/blog/2025/09/10/kubernetes-v1-34-env-files/)
      * [Kubernetes v1.34: Snapshottable API server cache](https://kubernetes.io/blog/2025/09/09/kubernetes-v1-34-snapshottable-api-server-cache/)
      * [Kubernetes v1.34: VolumeAttributesClass for Volume Modification GA](https://kubernetes.io/blog/2025/09/08/kubernetes-v1-34-volume-attributes-class/)
      * [Kubernetes v1.34: Pod Replacement Policy for Jobs Goes GA](https://kubernetes.io/blog/2025/09/05/kubernetes-v1-34-pod-replacement-policy-for-jobs-goes-ga/)
      * [Kubernetes v1.34: PSI Metrics for Kubernetes Graduates to Beta](https://kubernetes.io/blog/2025/09/04/kubernetes-v1-34-introducing-psi-metrics-beta/)
      * [Kubernetes v1.34: Service Account Token Integration for Image Pulls Graduates to Beta](https://kubernetes.io/blog/2025/09/03/kubernetes-v1-34-sa-tokens-image-pulls-beta/)
      * [Kubernetes v1.34: Introducing CPU Manager Static Policy Option for Uncore Cache Alignment](https://kubernetes.io/blog/2025/09/02/kubernetes-v1-34-prefer-align-by-uncore-cache-cpumanager-static-policy-optimization/)
      * [Kubernetes v1.34: DRA has graduated to GA](https://kubernetes.io/blog/2025/09/01/kubernetes-v1-34-dra-updates/)
      * [Kubernetes v1.34: Finer-Grained Control Over Container Restarts](https://kubernetes.io/blog/2025/08/29/kubernetes-v1-34-per-container-restart-policy/)
      * [Kubernetes v1.34: User preferences (kuberc) are available for testing in kubectl 1.34](https://kubernetes.io/blog/2025/08/28/kubernetes-v1-34-kubectl-kuberc-beta/)
      * [Kubernetes v1.34: Of Wind & Will (O' WaW)](https://kubernetes.io/blog/2025/08/27/kubernetes-v1-34-release/)
      * [Tuning Linux Swap for Kubernetes: A Deep Dive](https://kubernetes.io/blog/2025/08/19/tuning-linux-swap-for-kubernetes-a-deep-dive/)
      * [Introducing Headlamp AI Assistant](https://kubernetes.io/blog/2025/08/07/introducing-headlamp-ai-assistant/)
      * [Kubernetes v1.34 Sneak Peek](https://kubernetes.io/blog/2025/07/28/kubernetes-v1-34-sneak-peek/)
      * [Post-Quantum Cryptography in Kubernetes](https://kubernetes.io/blog/2025/07/18/pqc-in-k8s/)
      * [Navigating Failures in Pods With Devices](https://kubernetes.io/blog/2025/07/03/navigating-failures-in-pods-with-devices/)
      * [Image Compatibility In Cloud Native Environments](https://kubernetes.io/blog/2025/06/25/image-compatibility-in-cloud-native-environments/)
      * [Changes to Kubernetes Slack](https://kubernetes.io/blog/2025/06/16/changes-to-kubernetes-slack/)
      * [Enhancing Kubernetes Event Management with Custom Aggregation](https://kubernetes.io/blog/2025/06/10/enhancing-kubernetes-event-management-custom-aggregation/)
      * [Introducing Gateway API Inference Extension](https://kubernetes.io/blog/2025/06/05/introducing-gateway-api-inference-extension/)
      * [Start Sidecar First: How To Avoid Snags](https://kubernetes.io/blog/2025/06/03/start-sidecar-first/)
      * [Gateway API v1.3.0: Advancements in Request Mirroring, CORS, Gateway Merging, and Retry Budgets](https://kubernetes.io/blog/2025/06/02/gateway-api-v1-3/)
      * [Kubernetes v1.33: In-Place Pod Resize Graduated to Beta](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)
      * [Announcing etcd v3.6.0](https://kubernetes.io/blog/2025/05/15/announcing-etcd-3.6/)
      * [Kubernetes 1.33: Job's SuccessPolicy Goes GA](https://kubernetes.io/blog/2025/05/15/kubernetes-1-33-jobs-success-policy-goes-ga/)
      * [Kubernetes v1.33: Updates to Container Lifecycle](https://kubernetes.io/blog/2025/05/14/kubernetes-v1-33-updates-to-container-lifecycle/)
      * [Kubernetes v1.33: Job's Backoff Limit Per Index Goes GA](https://kubernetes.io/blog/2025/05/13/kubernetes-v1-33-jobs-backoff-limit-per-index-goes-ga/)
      * [Kubernetes v1.33: Image Pull Policy the way you always thought it worked!](https://kubernetes.io/blog/2025/05/12/kubernetes-v1-33-ensure-secret-pulled-images-alpha/)
      * [Kubernetes v1.33: Streaming List responses](https://kubernetes.io/blog/2025/05/09/kubernetes-v1-33-streaming-list-responses/)
      * [Kubernetes 1.33: Volume Populators Graduate to GA](https://kubernetes.io/blog/2025/05/08/kubernetes-v1-33-volume-populators-ga/)
      * [Kubernetes v1.33: From Secrets to Service Accounts: Kubernetes Image Pulls Evolved](https://kubernetes.io/blog/2025/05/07/kubernetes-v1-33-wi-for-image-pulls/)
      * [Kubernetes v1.33: Fine-grained SupplementalGroups Control Graduates to Beta](https://kubernetes.io/blog/2025/05/06/kubernetes-v1-33-fine-grained-supplementalgroups-control-beta/)
      * [Kubernetes v1.33: Prevent PersistentVolume Leaks When Deleting out of Order graduates to GA](https://kubernetes.io/blog/2025/05/05/kubernetes-v1-33-prevent-persistentvolume-leaks-when-deleting-out-of-order-graduate-to-ga/)
      * [Kubernetes v1.33: Mutable CSI Node Allocatable Count](https://kubernetes.io/blog/2025/05/02/kubernetes-1-33-mutable-csi-node-allocatable-count/)
      * [Kubernetes v1.33: New features in DRA](https://kubernetes.io/blog/2025/05/01/kubernetes-v1-33-dra-updates/)
      * [Kubernetes v1.33: Storage Capacity Scoring of Nodes for Dynamic Provisioning (alpha)](https://kubernetes.io/blog/2025/04/30/kubernetes-v1-33-storage-capacity-scoring-feature/)
      * [Kubernetes v1.33: Image Volumes graduate to beta!](https://kubernetes.io/blog/2025/04/29/kubernetes-v1-33-image-volume-beta/)
      * [Kubernetes v1.33: HorizontalPodAutoscaler Configurable Tolerance](https://kubernetes.io/blog/2025/04/28/kubernetes-v1-33-hpa-configurable-tolerance/)
      * [Kubernetes v1.33: User Namespaces enabled by default!](https://kubernetes.io/blog/2025/04/25/userns-enabled-by-default/)
      * [Kubernetes v1.33: Continuing the transition from Endpoints to EndpointSlices](https://kubernetes.io/blog/2025/04/24/endpoints-deprecation/)
      * [Kubernetes v1.33: Octarine](https://kubernetes.io/blog/2025/04/23/kubernetes-v1-33-release/)
      * [Kubernetes Multicontainer Pods: An Overview](https://kubernetes.io/blog/2025/04/22/multi-container-pods-overview/)
      * [Introducing kube-scheduler-simulator](https://kubernetes.io/blog/2025/04/07/introducing-kube-scheduler-simulator/)
      * [Kubernetes v1.33 sneak peek](https://kubernetes.io/blog/2025/03/26/kubernetes-v1-33-upcoming-changes/)
      * [Fresh Swap Features for Linux Users in Kubernetes 1.32](https://kubernetes.io/blog/2025/03/25/swap-linux-improvements/)
      * [Ingress-nginx CVE-2025-1974: What You Need to Know](https://kubernetes.io/blog/2025/03/24/ingress-nginx-cve-2025-1974/)
      * [Introducing JobSet](https://kubernetes.io/blog/2025/03/23/introducing-jobset/)
      * [Spotlight on SIG Apps](https://kubernetes.io/blog/2025/03/12/sig-apps-spotlight-2025/)
      * [Spotlight on SIG etcd](https://kubernetes.io/blog/2025/03/04/sig-etcd-spotlight/)
      * [NFTables mode for kube-proxy](https://kubernetes.io/blog/2025/02/28/nftables-kube-proxy/)
      * [The Cloud Controller Manager Chicken and Egg Problem](https://kubernetes.io/blog/2025/02/14/cloud-controller-manager-chicken-egg-problem/)
      * [Spotlight on SIG Architecture: Enhancements](https://kubernetes.io/blog/2025/01/21/sig-architecture-enhancements/)
    * 2024
      * [Kubernetes 1.32: Moving Volume Group Snapshots to Beta](https://kubernetes.io/blog/2024/12/18/kubernetes-1-32-volume-group-snapshot-beta/)
      * [Enhancing Kubernetes API Server Efficiency with API Streaming](https://kubernetes.io/blog/2024/12/17/kube-apiserver-api-streaming/)
      * [Kubernetes v1.32 Adds A New CPU Manager Static Policy Option For Strict CPU Reservation](https://kubernetes.io/blog/2024/12/16/cpumanager-strict-cpu-reservation/)
      * [Kubernetes v1.32: Memory Manager Goes GA](https://kubernetes.io/blog/2024/12/13/memory-manager-goes-ga/)
      * [Kubernetes v1.32: QueueingHint Brings a New Possibility to Optimize Pod Scheduling](https://kubernetes.io/blog/2024/12/12/scheduler-queueinghint/)
      * [Kubernetes v1.32: Penelope](https://kubernetes.io/blog/2024/12/11/kubernetes-v1-32-release/)
      * [Gateway API v1.2: WebSockets, Timeouts, Retries, and More](https://kubernetes.io/blog/2024/11/21/gateway-api-v1-2/)
      * [How we built a dynamic Kubernetes API Server for the API Aggregation Layer in Cozystack](https://kubernetes.io/blog/2024/11/21/dynamic-kubernetes-api-server-for-cozystack/)
      * [Kubernetes v1.32 sneak peek](https://kubernetes.io/blog/2024/11/08/kubernetes-1-32-upcoming-changes/)
      * [Spotlight on Kubernetes Upstream Training in Japan](https://kubernetes.io/blog/2024/10/28/k8s-upstream-training-japan-spotlight/)
      * [Announcing the 2024 Steering Committee Election Results](https://kubernetes.io/blog/2024/10/02/steering-committee-results-2024/)
      * [Spotlight on CNCF Deaf and Hard-of-hearing Working Group (DHHWG)](https://kubernetes.io/blog/2024/09/30/cncf-deaf-and-hard-of-hearing-working-group-spotlight/)
      * [Spotlight on SIG Scheduling](https://kubernetes.io/blog/2024/09/24/sig-scheduling-spotlight-2024/)
      * [Kubernetes v1.31: kubeadm v1beta4](https://kubernetes.io/blog/2024/08/23/kubernetes-1-31-kubeadm-v1beta4/)
      * [Kubernetes v1.31: New Kubernetes CPUManager Static Policy: Distribute CPUs Across Cores](https://kubernetes.io/blog/2024/08/22/cpumanager-static-policy-distributed-cpu-across-cores/)
      * [Kubernetes 1.31: Fine-grained SupplementalGroups control](https://kubernetes.io/blog/2024/08/22/fine-grained-supplementalgroups-control/)
      * [Kubernetes 1.31: Custom Profiling in Kubectl Debug Graduates to Beta](https://kubernetes.io/blog/2024/08/22/kubernetes-1-31-custom-profiling-kubectl-debug/)
      * [Kubernetes 1.31: Autoconfiguration For Node Cgroup Driver (beta)](https://kubernetes.io/blog/2024/08/21/cri-cgroup-driver-lookup-now-beta/)
      * [Kubernetes 1.31: Streaming Transitions from SPDY to WebSockets](https://kubernetes.io/blog/2024/08/20/websockets-transition/)
      * [Kubernetes 1.31: Pod Failure Policy for Jobs Goes GA](https://kubernetes.io/blog/2024/08/19/kubernetes-1-31-pod-failure-policy-for-jobs-goes-ga/)
      * [Kubernetes 1.31: Read Only Volumes Based On OCI Artifacts (alpha)](https://kubernetes.io/blog/2024/08/16/kubernetes-1-31-image-volume-source/)
      * [Kubernetes 1.31: Prevent PersistentVolume Leaks When Deleting out of Order](https://kubernetes.io/blog/2024/08/16/kubernetes-1-31-prevent-persistentvolume-leaks-when-deleting-out-of-order/)
      * [Kubernetes 1.31: MatchLabelKeys in PodAffinity graduates to beta](https://kubernetes.io/blog/2024/08/16/matchlabelkeys-podaffinity/)
      * [Kubernetes v1.31: Accelerating Cluster Performance with Consistent Reads from Cache](https://kubernetes.io/blog/2024/08/15/consistent-read-from-cache-beta/)
      * [Kubernetes 1.31: VolumeAttributesClass for Volume Modification Beta](https://kubernetes.io/blog/2024/08/15/kubernetes-1-31-volume-attributes-class/)
      * [Kubernetes v1.31: PersistentVolume Last Phase Transition Time Moves to GA](https://kubernetes.io/blog/2024/08/14/last-phase-transition-time-ga/)
      * [Kubernetes 1.31: Moving cgroup v1 Support into Maintenance Mode](https://kubernetes.io/blog/2024/08/14/kubernetes-1-31-moving-cgroup-v1-support-maintenance-mode/)
      * [Kubernetes v1.31: Elli](https://kubernetes.io/blog/2024/08/13/kubernetes-v1-31-release/)
      * [Introducing Feature Gates to Client-Go: Enhancing Flexibility and Control](https://kubernetes.io/blog/2024/08/12/feature-gates-in-client-go/)
      * [Spotlight on SIG API Machinery](https://kubernetes.io/blog/2024/08/07/sig-api-machinery-spotlight-2024/)
      * [Kubernetes Removals and Major Changes In v1.31](https://kubernetes.io/blog/2024/07/19/kubernetes-1-31-upcoming-changes/)
      * [Spotlight on SIG Node](https://kubernetes.io/blog/2024/06/20/sig-node-spotlight-2024/)
      * [10 Years of Kubernetes](https://kubernetes.io/blog/2024/06/06/10-years-of-kubernetes/)
      * [Completing the largest migration in Kubernetes history](https://kubernetes.io/blog/2024/05/20/completing-cloud-provider-migration/)
      * [Gateway API v1.1: Service mesh, GRPCRoute, and a whole lot more](https://kubernetes.io/blog/2024/05/09/gateway-api-v1-1/)
      * [Container Runtime Interface streaming explained](https://kubernetes.io/blog/2024/05/01/cri-streaming-explained/)
      * [Kubernetes 1.30: Preventing unauthorized volume mode conversion moves to GA](https://kubernetes.io/blog/2024/04/30/prevent-unauthorized-volume-mode-conversion-ga/)
      * [Kubernetes 1.30: Multi-Webhook and Modular Authorization Made Much Easier](https://kubernetes.io/blog/2024/04/26/multi-webhook-and-modular-authorization-made-much-easier/)
      * [Kubernetes 1.30: Structured Authentication Configuration Moves to Beta](https://kubernetes.io/blog/2024/04/25/structured-authentication-moves-to-beta/)
      * [Kubernetes 1.30: Validating Admission Policy Is Generally Available](https://kubernetes.io/blog/2024/04/24/validating-admission-policy-ga/)
      * [Kubernetes 1.30: Read-only volume mounts can be finally literally read-only](https://kubernetes.io/blog/2024/04/23/recursive-read-only-mounts/)
      * [Kubernetes 1.30: Beta Support For Pods With User Namespaces](https://kubernetes.io/blog/2024/04/22/userns-beta/)
      * [Kubernetes v1.30: Uwubernetes](https://kubernetes.io/blog/2024/04/17/kubernetes-v1-30-release/)
      * [Spotlight on SIG Architecture: Code Organization](https://kubernetes.io/blog/2024/04/11/sig-architecture-code-spotlight-2024/)
      * [DIY: Create Your Own Cloud with Kubernetes (Part 3)](https://kubernetes.io/blog/2024/04/05/diy-create-your-own-cloud-with-kubernetes-part-3/)
      * [DIY: Create Your Own Cloud with Kubernetes (Part 2)](https://kubernetes.io/blog/2024/04/05/diy-create-your-own-cloud-with-kubernetes-part-2/)
      * [DIY: Create Your Own Cloud with Kubernetes (Part 1)](https://kubernetes.io/blog/2024/04/05/diy-create-your-own-cloud-with-kubernetes-part-1/)
      * [Introducing the Windows Operational Readiness Specification](https://kubernetes.io/blog/2024/04/03/intro-windows-ops-readiness/)
      * [A Peek at Kubernetes v1.30](https://kubernetes.io/blog/2024/03/12/kubernetes-1-30-upcoming-changes/)
      * [CRI-O: Applying seccomp profiles from OCI registries](https://kubernetes.io/blog/2024/03/07/cri-o-seccomp-oci-artifacts/)
      * [Spotlight on SIG Cloud Provider](https://kubernetes.io/blog/2024/03/01/sig-cloud-provider-spotlight-2024/)
      * [A look into the Kubernetes Book Club](https://kubernetes.io/blog/2024/02/22/k8s-book-club/)
      * [Image Filesystem: Configuring Kubernetes to store containers on a separate filesystem](https://kubernetes.io/blog/2024/01/23/kubernetes-separate-image-filesystem/)
      * [Spotlight on SIG Release (Release Team Subproject)](https://kubernetes.io/blog/2024/01/15/sig-release-spotlight-2023/)
    * 2023
      * [Contextual logging in Kubernetes 1.29: Better troubleshooting and enhanced logging](https://kubernetes.io/blog/2023/12/20/contextual-logging-in-kubernetes-1-29/)
      * [Kubernetes 1.29: PodReadyToStartContainers Condition Moves to Beta](https://kubernetes.io/blog/2023/12/19/pod-ready-to-start-containers-condition-now-in-beta/)
      * [Kubernetes 1.29: Decoupling taint manager from node lifecycle controller](https://kubernetes.io/blog/2023/12/19/kubernetes-1-29-taint-eviction-controller/)
      * [Kubernetes 1.29: Single Pod Access Mode for PersistentVolumes Graduates to Stable](https://kubernetes.io/blog/2023/12/18/read-write-once-pod-access-mode-ga/)
      * [Kubernetes 1.29: New (alpha) Feature, Load Balancer IP Mode for Services](https://kubernetes.io/blog/2023/12/18/kubernetes-1-29-feature-loadbalancer-ip-mode-alpha/)
      * [Kubernetes 1.29: VolumeAttributesClass for Volume Modification](https://kubernetes.io/blog/2023/12/15/kubernetes-1-29-volume-attributes-class/)
      * [Kubernetes 1.29: CSI Storage Resizing Authenticated and Generally Available in v1.29](https://kubernetes.io/blog/2023/12/15/csi-node-expand-secret-support-ga/)
      * [Kubernetes 1.29: Cloud Provider Integrations Are Now Separate Components](https://kubernetes.io/blog/2023/12/14/cloud-provider-integration-changes/)
      * [Kubernetes v1.29: Mandala](https://kubernetes.io/blog/2023/12/13/kubernetes-v1-29-release/)
      * [New Experimental Features in Gateway API v1.0](https://kubernetes.io/blog/2023/11/28/gateway-api-ga/)
      * [Spotlight on SIG Testing](https://kubernetes.io/blog/2023/11/24/sig-testing-spotlight-2023/)
      * [The Case for Kubernetes Resource Limits: Predictability vs. Efficiency](https://kubernetes.io/blog/2023/11/16/the-case-for-kubernetes-resource-limits/)
      * [Kubernetes Removals, Deprecations, and Major Changes in Kubernetes 1.29](https://kubernetes.io/blog/2023/11/16/kubernetes-1-29-upcoming-changes/)
      * [Introducing SIG etcd](https://kubernetes.io/blog/2023/11/07/introducing-sig-etcd/)
      * [Kubernetes Contributor Summit: Behind-the-scenes](https://kubernetes.io/blog/2023/11/03/k8s-contributor-summit-behind-the-scenes/)
      * [Spotlight on SIG Architecture: Production Readiness](https://kubernetes.io/blog/2023/11/02/sig-architecture-production-readiness-spotlight-2023/)
      * [Gateway API v1.0: GA Release](https://kubernetes.io/blog/2023/10/31/gateway-api-ga/)
      * [Introducing ingress2gateway; Simplifying Upgrades to Gateway API](https://kubernetes.io/blog/2023/10/25/introducing-ingress2gateway/)
      * [Plants, process and parties: the Kubernetes 1.28 release interview](https://kubernetes.io/blog/2023/10/24/plants-process-and-parties-the-kubernetes-1.28-release-interview/)
      * [PersistentVolume Last Phase Transition Time in Kubernetes](https://kubernetes.io/blog/2023/10/23/persistent-volume-last-phase-transition-time/)
      * [A Quick Recap of 2023 China Kubernetes Contributor Summit](https://kubernetes.io/blog/2023/10/20/kcs-shanghai/)
      * [Bootstrap an Air Gapped Cluster With Kubeadm](https://kubernetes.io/blog/2023/10/12/bootstrap-an-air-gapped-cluster-with-kubeadm/)
      * [CRI-O is moving towards pkgs.k8s.io](https://kubernetes.io/blog/2023/10/10/cri-o-community-package-infrastructure/)
      * [Spotlight on SIG Architecture: Conformance](https://kubernetes.io/blog/2023/10/05/sig-architecture-conformance-spotlight-2023/)
      * [Announcing the 2023 Steering Committee Election Results](https://kubernetes.io/blog/2023/10/02/steering-committee-results-2023/)
      * [Happy 7th Birthday kubeadm!](https://kubernetes.io/blog/2023/09/26/happy-7th-birthday-kubeadm/)
      * [kubeadm: Use etcd Learner to Join a Control Plane Node Safely](https://kubernetes.io/blog/2023/09/25/kubeadm-use-etcd-learner-mode/)
      * [User Namespaces: Now Supports Running Stateful Pods in Alpha!](https://kubernetes.io/blog/2023/09/13/userns-alpha/)
      * [Comparing Local Kubernetes Development Tools: Telepresence, Gefyra, and mirrord](https://kubernetes.io/blog/2023/09/12/local-k8s-development-tools/)
      * [Kubernetes Legacy Package Repositories Will Be Frozen On September 13, 2023](https://kubernetes.io/blog/2023/08/31/legacy-package-repository-deprecation/)
      * [Gateway API v0.8.0: Introducing Service Mesh Support](https://kubernetes.io/blog/2023/08/29/gateway-api-v0-8/)
      * [Kubernetes 1.28: A New (alpha) Mechanism For Safer Cluster Upgrades](https://kubernetes.io/blog/2023/08/28/kubernetes-1-28-feature-mixed-version-proxy-alpha/)
      * [Kubernetes v1.28: Introducing native sidecar containers](https://kubernetes.io/blog/2023/08/25/native-sidecar-containers/)
      * [Kubernetes 1.28: Beta support for using swap on Linux](https://kubernetes.io/blog/2023/08/24/swap-linux-beta/)
      * [Kubernetes 1.28: Node podresources API Graduates to GA](https://kubernetes.io/blog/2023/08/23/kubelet-podresources-api-ga/)
      * [Kubernetes 1.28: Improved failure handling for Jobs](https://kubernetes.io/blog/2023/08/21/kubernetes-1-28-jobapi-update/)
      * [Kubernetes v1.28: Retroactive Default StorageClass move to GA](https://kubernetes.io/blog/2023/08/18/retroactive-default-storage-class-ga/)
      * [Kubernetes 1.28: Non-Graceful Node Shutdown Moves to GA](https://kubernetes.io/blog/2023/08/16/kubernetes-1-28-non-graceful-node-shutdown-ga/)
      * [pkgs.k8s.io: Introducing Kubernetes Community-Owned Package Repositories](https://kubernetes.io/blog/2023/08/15/pkgs-k8s-io-introduction/)
      * [Kubernetes v1.28: Planternetes](https://kubernetes.io/blog/2023/08/15/kubernetes-v1-28-release/)
      * [Spotlight on SIG ContribEx](https://kubernetes.io/blog/2023/08/14/sig-contribex-spotlight-2023/)
      * [Spotlight on SIG CLI](https://kubernetes.io/blog/2023/07/20/sig-cli-spotlight-2023/)
      * [Confidential Kubernetes: Use Confidential Virtual Machines and Enclaves to improve your cluster security](https://kubernetes.io/blog/2023/07/06/confidential-kubernetes/)
      * [Verifying Container Image Signatures Within CRI Runtimes](https://kubernetes.io/blog/2023/06/29/container-image-signature-verification/)
      * [dl.k8s.io to adopt a Content Delivery Network](https://kubernetes.io/blog/2023/06/09/dl-adopt-cdn/)
      * [Using OCI artifacts to distribute security profiles for seccomp, SELinux and AppArmor](https://kubernetes.io/blog/2023/05/24/oci-security-profiles/)
      * [Having fun with seccomp profiles on the edge](https://kubernetes.io/blog/2023/05/18/seccomp-profiles-edge/)
      * [Kubernetes 1.27: KMS V2 Moves to Beta](https://kubernetes.io/blog/2023/05/16/kms-v2-moves-to-beta/)
      * [Kubernetes 1.27: updates on speeding up Pod startup](https://kubernetes.io/blog/2023/05/15/speed-up-pod-startup/)
      * [Kubernetes 1.27: In-place Resource Resize for Kubernetes Pods (alpha)](https://kubernetes.io/blog/2023/05/12/in-place-pod-resize-alpha/)
      * [Kubernetes 1.27: Avoid Collisions Assigning Ports to NodePort Services](https://kubernetes.io/blog/2023/05/11/nodeport-dynamic-and-static-allocation/)
      * [Kubernetes 1.27: Safer, More Performant Pruning in kubectl apply](https://kubernetes.io/blog/2023/05/09/introducing-kubectl-applyset-pruning/)
      * [Kubernetes 1.27: Introducing An API For Volume Group Snapshots](https://kubernetes.io/blog/2023/05/08/kubernetes-1-27-volume-group-snapshot-alpha/)
      * [Kubernetes 1.27: Quality-of-Service for Memory Resources (alpha)](https://kubernetes.io/blog/2023/05/05/qos-memory-resources/)
      * [Kubernetes 1.27: StatefulSet PVC Auto-Deletion (beta)](https://kubernetes.io/blog/2023/05/04/kubernetes-1-27-statefulset-pvc-auto-deletion-beta/)
      * [Kubernetes 1.27: HorizontalPodAutoscaler ContainerResource type metric moves to beta](https://kubernetes.io/blog/2023/05/02/hpa-container-resource-metric/)
      * [Kubernetes 1.27: StatefulSet Start Ordinal Simplifies Migration](https://kubernetes.io/blog/2023/04/28/statefulset-start-ordinal/)
      * [Updates to the Auto-refreshing Official CVE Feed](https://kubernetes.io/blog/2023/04/25/k8s-cve-feed-beta/)
      * [Kubernetes 1.27: Server Side Field Validation and OpenAPI V3 move to GA](https://kubernetes.io/blog/2023/04/24/openapi-v3-field-validation-ga/)
      * [Kubernetes 1.27: Query Node Logs Using The Kubelet API](https://kubernetes.io/blog/2023/04/21/node-log-query-alpha/)
      * [Kubernetes 1.27: Single Pod Access Mode for PersistentVolumes Graduates to Beta](https://kubernetes.io/blog/2023/04/20/read-write-once-pod-access-mode-beta/)
      * [Kubernetes 1.27: Efficient SELinux volume relabeling (Beta)](https://kubernetes.io/blog/2023/04/18/kubernetes-1-27-efficient-selinux-relabeling-beta/)
      * [Kubernetes 1.27: More fine-grained pod topology spread policies reached beta](https://kubernetes.io/blog/2023/04/17/fine-grained-pod-topology-spread-features-beta/)
      * [Kubernetes v1.27: Chill Vibes](https://kubernetes.io/blog/2023/04/11/kubernetes-v1-27-release/)
      * [Keeping Kubernetes Secure with Updated Go Versions](https://kubernetes.io/blog/2023/04/06/keeping-kubernetes-secure-with-updated-go-versions/)
      * [Kubernetes Validating Admission Policies: A Practical Example](https://kubernetes.io/blog/2023/03/30/kubescape-validating-admission-policy-library/)
      * [Kubernetes Removals and Major Changes In v1.27](https://kubernetes.io/blog/2023/03/17/upcoming-changes-in-kubernetes-v1-27/)
      * [k8s.gcr.io Redirect to registry.k8s.io - What You Need to Know](https://kubernetes.io/blog/2023/03/10/image-registry-redirect/)
      * [Forensic container analysis](https://kubernetes.io/blog/2023/03/10/forensic-container-analysis/)
      * [Introducing KWOK: Kubernetes WithOut Kubelet](https://kubernetes.io/blog/2023/03/01/introducing-kwok/)
      * [Free Katacoda Kubernetes Tutorials Are Shutting Down](https://kubernetes.io/blog/2023/02/14/kubernetes-katacoda-tutorials-stop-from-2023-03-31/)
      * [k8s.gcr.io Image Registry Will Be Frozen From the 3rd of April 2023](https://kubernetes.io/blog/2023/02/06/k8s-gcr-io-freeze-announcement/)
      * [Spotlight on SIG Instrumentation](https://kubernetes.io/blog/2023/02/03/sig-instrumentation-spotlight-2023/)
      * [Consider All Microservices Vulnerable — And Monitor Their Behavior](https://kubernetes.io/blog/2023/01/20/security-behavior-analysis/)
      * [Protect Your Mission-Critical Pods From Eviction With PriorityClass](https://kubernetes.io/blog/2023/01/12/protect-mission-critical-pods-priorityclass/)
      * [Kubernetes 1.26: Eviction policy for unhealthy pods guarded by PodDisruptionBudgets](https://kubernetes.io/blog/2023/01/06/unhealthy-pod-eviction-policy-for-pdbs/)
      * [Kubernetes v1.26: Retroactive Default StorageClass](https://kubernetes.io/blog/2023/01/05/retroactive-default-storage-class/)
      * [Kubernetes v1.26: Alpha support for cross-namespace storage data sources](https://kubernetes.io/blog/2023/01/02/cross-namespace-data-sources-alpha/)
    * 2022
      * [Kubernetes v1.26: Advancements in Kubernetes Traffic Engineering](https://kubernetes.io/blog/2022/12/30/advancements-in-kubernetes-traffic-engineering/)
      * [Kubernetes 1.26: Job Tracking, to Support Massively Parallel Batch Workloads, Is Generally Available](https://kubernetes.io/blog/2022/12/29/scalable-job-tracking-ga/)
      * [Kubernetes v1.26: CPUManager goes GA](https://kubernetes.io/blog/2022/12/27/cpumanager-ga/)
      * [Kubernetes 1.26: Pod Scheduling Readiness](https://kubernetes.io/blog/2022/12/26/pod-scheduling-readiness-alpha/)
      * [Kubernetes 1.26: Support for Passing Pod fsGroup to CSI Drivers At Mount Time](https://kubernetes.io/blog/2022/12/23/kubernetes-12-06-fsgroup-on-mount/)
      * [Kubernetes v1.26: GA Support for Kubelet Credential Providers](https://kubernetes.io/blog/2022/12/22/kubelet-credential-providers/)
      * [Kubernetes 1.26: Introducing Validating Admission Policies](https://kubernetes.io/blog/2022/12/20/validating-admission-policies-alpha/)
      * [Kubernetes 1.26: Device Manager graduates to GA](https://kubernetes.io/blog/2022/12/19/devicemanager-ga/)
      * [Kubernetes 1.26: Non-Graceful Node Shutdown Moves to Beta](https://kubernetes.io/blog/2022/12/16/kubernetes-1-26-non-graceful-node-shutdown-beta/)
      * [Kubernetes 1.26: Alpha API For Dynamic Resource Allocation](https://kubernetes.io/blog/2022/12/15/dynamic-resource-allocation/)
      * [Kubernetes 1.26: Windows HostProcess Containers Are Generally Available](https://kubernetes.io/blog/2022/12/13/windows-host-process-containers-ga/)
      * [Kubernetes 1.26: We're now signing our binary release artifacts!](https://kubernetes.io/blog/2022/12/12/kubernetes-release-artifact-signing/)
      * [Kubernetes v1.26: Electrifying](https://kubernetes.io/blog/2022/12/09/kubernetes-v1-26-release/)
      * [Forensic container checkpointing in Kubernetes](https://kubernetes.io/blog/2022/12/05/forensic-container-checkpointing-alpha/)
      * [Finding suspicious syscalls with the seccomp notifier](https://kubernetes.io/blog/2022/12/02/seccomp-notifier/)
      * [Boosting Kubernetes container runtime observability with OpenTelemetry](https://kubernetes.io/blog/2022/12/01/runtime-observability-opentelemetry/)
      * [registry.k8s.io: faster, cheaper and Generally Available (GA)](https://kubernetes.io/blog/2022/11/28/registry-k8s-io-faster-cheaper-ga/)
      * [Kubernetes Removals, Deprecations, and Major Changes in 1.26](https://kubernetes.io/blog/2022/11/18/upcoming-changes-in-kubernetes-1-26/)
      * [Live and let live with Kluctl and Server Side Apply](https://kubernetes.io/blog/2022/11/04/live-and-let-live-with-kluctl-and-ssa/)
      * [Server Side Apply Is Great And You Should Be Using It](https://kubernetes.io/blog/2022/10/20/advanced-server-side-apply/)
      * [Current State: 2019 Third Party Security Audit of Kubernetes](https://kubernetes.io/blog/2022/10/05/current-state-2019-third-party-audit/)
      * [Introducing Kueue](https://kubernetes.io/blog/2022/10/04/introducing-kueue/)
      * [Kubernetes 1.25: alpha support for running Pods with user namespaces](https://kubernetes.io/blog/2022/10/03/userns-alpha/)
      * [Enforce CRD Immutability with CEL Transition Rules](https://kubernetes.io/blog/2022/09/29/enforce-immutability-using-cel/)
      * [Kubernetes 1.25: Kubernetes In-Tree to CSI Volume Migration Status Update](https://kubernetes.io/blog/2022/09/26/storage-in-tree-to-csi-migration-status-update-1.25/)
      * [Kubernetes 1.25: CustomResourceDefinition Validation Rules Graduate to Beta](https://kubernetes.io/blog/2022/09/23/crd-validation-rules-beta/)
      * [Kubernetes 1.25: Use Secrets for Node-Driven Expansion of CSI Volumes](https://kubernetes.io/blog/2022/09/21/kubernetes-1-25-use-secrets-while-expanding-csi-volumes-on-node-alpha/)
      * [Kubernetes 1.25: Local Storage Capacity Isolation Reaches GA](https://kubernetes.io/blog/2022/09/19/local-storage-capacity-isolation-ga/)
      * [Kubernetes 1.25: Two Features for Apps Rollouts Graduate to Stable](https://kubernetes.io/blog/2022/09/15/app-rollout-features-reach-stable/)
      * [Kubernetes 1.25: PodHasNetwork Condition for Pods](https://kubernetes.io/blog/2022/09/14/pod-has-network-condition/)
      * [Announcing the Auto-refreshing Official Kubernetes CVE Feed](https://kubernetes.io/blog/2022/09/12/k8s-cve-feed-alpha/)
      * [Kubernetes 1.25: KMS V2 Improvements](https://kubernetes.io/blog/2022/09/09/kms-v2-improvements/)
      * [Kubernetes’s IPTables Chains Are Not API](https://kubernetes.io/blog/2022/09/07/iptables-chains-not-api/)
      * [Introducing COSI: Object Storage Management using Kubernetes APIs](https://kubernetes.io/blog/2022/09/02/cosi-kubernetes-object-storage-management/)
      * [Kubernetes 1.25: cgroup v2 graduates to GA](https://kubernetes.io/blog/2022/08/31/cgroupv2-ga-1-25/)
      * [Kubernetes 1.25: CSI Inline Volumes have graduated to GA](https://kubernetes.io/blog/2022/08/29/csi-inline-volumes-ga/)
      * [Kubernetes v1.25: Pod Security Admission Controller in Stable](https://kubernetes.io/blog/2022/08/25/pod-security-admission-stable/)
      * [PodSecurityPolicy: The Historical Context](https://kubernetes.io/blog/2022/08/23/podsecuritypolicy-the-historical-context/)
      * [Kubernetes v1.25: Combiner](https://kubernetes.io/blog/2022/08/23/kubernetes-v1-25-release/)
      * [Spotlight on SIG Storage](https://kubernetes.io/blog/2022/08/22/sig-storage-spotlight/)
      * [Meet Our Contributors - APAC (China region)](https://kubernetes.io/blog/2022/08/15/meet-our-contributors-china-ep-03/)
      * [Enhancing Kubernetes one KEP at a Time](https://kubernetes.io/blog/2022/08/11/enhancing-kubernetes-one-kep-at-a-time/)
      * [Kubernetes Removals and Major Changes In 1.25](https://kubernetes.io/blog/2022/08/04/upcoming-changes-in-kubernetes-1-25/)
      * [Spotlight on SIG Docs](https://kubernetes.io/blog/2022/08/02/sig-docs-spotlight-2022/)
      * [Kubernetes Gateway API Graduates to Beta](https://kubernetes.io/blog/2022/07/13/gateway-api-graduates-to-beta/)
      * [Annual Report Summary 2021](https://kubernetes.io/blog/2022/06/01/annual-report-summary-2021/)
      * [Kubernetes 1.24: Maximum Unavailable Replicas for StatefulSet](https://kubernetes.io/blog/2022/05/27/maxunavailable-for-statefulset/)
      * [Contextual Logging in Kubernetes 1.24](https://kubernetes.io/blog/2022/05/25/contextual-logging/)
      * [Kubernetes 1.24: Avoid Collisions Assigning IP Addresses to Services](https://kubernetes.io/blog/2022/05/23/service-ip-dynamic-and-static-allocation/)
      * [Kubernetes 1.24: Introducing Non-Graceful Node Shutdown Alpha](https://kubernetes.io/blog/2022/05/20/kubernetes-1-24-non-graceful-node-shutdown-alpha/)
      * [Kubernetes 1.24: Prevent unauthorised volume mode conversion](https://kubernetes.io/blog/2022/05/18/prevent-unauthorised-volume-mode-conversion-alpha/)
      * [Kubernetes 1.24: Volume Populators Graduate to Beta](https://kubernetes.io/blog/2022/05/16/volume-populators-beta/)
      * [Kubernetes 1.24: gRPC container probes in beta](https://kubernetes.io/blog/2022/05/13/grpc-probes-now-in-beta/)
      * [Kubernetes 1.24: Storage Capacity Tracking Now Generally Available](https://kubernetes.io/blog/2022/05/06/storage-capacity-ga/)
      * [Kubernetes 1.24: Volume Expansion Now A Stable Feature](https://kubernetes.io/blog/2022/05/05/volume-expansion-ga/)
      * [Kubernetes 1.24: Stargazer](https://kubernetes.io/blog/2022/05/03/kubernetes-1-24-release-announcement/)
      * [Dockershim: The Historical Context](https://kubernetes.io/blog/2022/05/03/dockershim-historical-context/)
      * [Increasing the security bar in Ingress-NGINX v1.2.0](https://kubernetes.io/blog/2022/04/28/ingress-nginx-1-2-0/)
      * [Kubernetes Removals and Deprecations In 1.24](https://kubernetes.io/blog/2022/04/07/upcoming-changes-in-kubernetes-1-24/)
      * [Is Your Cluster Ready for v1.24?](https://kubernetes.io/blog/2022/03/31/ready-for-dockershim-removal/)
      * [Meet Our Contributors - APAC (Aus-NZ region)](https://kubernetes.io/blog/2022/03/16/meet-our-contributors-au-nz-ep-02/)
      * [Dockershim Removal FAQ](https://kubernetes.io/blog/2022/02/17/dockershim-faq/ "Updated: Dockershim Removal FAQ")
      * [SIG Node CI Subproject Celebrates Two Years of Test Improvements](https://kubernetes.io/blog/2022/02/16/sig-node-ci-subproject-celebrates/)
      * [Spotlight on SIG Multicluster](https://kubernetes.io/blog/2022/02/07/sig-multicluster-spotlight-2022/)
      * [Securing Admission Controllers](https://kubernetes.io/blog/2022/01/19/secure-your-admission-controllers-and-webhooks/)
      * [Meet Our Contributors - APAC (India region)](https://kubernetes.io/blog/2022/01/10/meet-our-contributors-india-ep-01/)
      * [Kubernetes is Moving on From Dockershim: Commitments and Next Steps](https://kubernetes.io/blog/2022/01/07/kubernetes-is-moving-on-from-dockershim/)
    * 2021
      * [Kubernetes-in-Kubernetes and the WEDOS PXE bootable server farm](https://kubernetes.io/blog/2021/12/22/kubernetes-in-kubernetes-and-pxe-bootable-server-farm/)
      * [Using Admission Controllers to Detect Container Drift at Runtime](https://kubernetes.io/blog/2021/12/21/admission-controllers-for-container-drift/)
      * [What's new in Security Profiles Operator v0.4.0](https://kubernetes.io/blog/2021/12/17/security-profiles-operator/)
      * [Kubernetes 1.23: StatefulSet PVC Auto-Deletion (alpha)](https://kubernetes.io/blog/2021/12/16/kubernetes-1-23-statefulset-pvc-auto-deletion/)
      * [Kubernetes 1.23: Prevent PersistentVolume leaks when deleting out of order](https://kubernetes.io/blog/2021/12/15/kubernetes-1-23-prevent-persistentvolume-leaks-when-deleting-out-of-order/)
      * [Kubernetes 1.23: Kubernetes In-Tree to CSI Volume Migration Status Update](https://kubernetes.io/blog/2021/12/10/storage-in-tree-to-csi-migration-status-update/)
      * [Kubernetes 1.23: Pod Security Graduates to Beta](https://kubernetes.io/blog/2021/12/09/pod-security-admission-beta/)
      * [Kubernetes 1.23: Dual-stack IPv4/IPv6 Networking Reaches GA](https://kubernetes.io/blog/2021/12/08/dual-stack-networking-ga/)
      * [Kubernetes 1.23: The Next Frontier](https://kubernetes.io/blog/2021/12/07/kubernetes-1-23-release-announcement/)
      * [Contribution, containers and cricket: the Kubernetes 1.22 release interview](https://kubernetes.io/blog/2021/12/01/contribution-containers-and-cricket-the-kubernetes-1.22-release-interview/)
      * [Quality-of-Service for Memory Resources](https://kubernetes.io/blog/2021/11/26/qos-memory-resources/)
      * [Dockershim removal is coming. Are you ready?](https://kubernetes.io/blog/2021/11/12/are-you-ready-for-dockershim-removal/)
      * [Non-root Containers And Devices](https://kubernetes.io/blog/2021/11/09/non-root-containers-and-devices/)
      * [Announcing the 2021 Steering Committee Election Results](https://kubernetes.io/blog/2021/11/08/steering-committee-results-2021/)
      * [Use KPNG to Write Specialized kube-proxiers](https://kubernetes.io/blog/2021/10/18/use-kpng-to-write-specialized-kube-proxiers/)
      * [Introducing ClusterClass and Managed Topologies in Cluster API](https://kubernetes.io/blog/2021/10/08/capi-clusterclass-and-managed-topologies/)
      * [A Closer Look at NSA/CISA Kubernetes Hardening Guidance](https://kubernetes.io/blog/2021/10/05/nsa-cisa-kubernetes-hardening-guidance/)
      * [How to Handle Data Duplication in Data-Heavy Kubernetes Environments](https://kubernetes.io/blog/2021/09/29/how-to-handle-data-duplication-in-data-heavy-kubernetes-environments/)
      * [Spotlight on SIG Node](https://kubernetes.io/blog/2021/09/27/sig-node-spotlight-2021/)
      * [Introducing Single Pod Access Mode for PersistentVolumes](https://kubernetes.io/blog/2021/09/13/read-write-once-pod-access-mode-alpha/)
      * [Alpha in Kubernetes v1.22: API Server Tracing](https://kubernetes.io/blog/2021/09/03/api-server-tracing/)
      * [Kubernetes 1.22: A New Design for Volume Populators](https://kubernetes.io/blog/2021/08/30/volume-populators-redesigned/)
      * [Minimum Ready Seconds for StatefulSets](https://kubernetes.io/blog/2021/08/27/minreadyseconds-statefulsets/)
      * [Enable seccomp for all workloads with a new v1.22 alpha feature](https://kubernetes.io/blog/2021/08/25/seccomp-default/)
      * [Alpha in v1.22: Windows HostProcess Containers](https://kubernetes.io/blog/2021/08/16/windows-hostprocess-containers/)
      * [Kubernetes Memory Manager moves to beta](https://kubernetes.io/blog/2021/08/11/kubernetes-1-22-feature-memory-manager-moves-to-beta/)
      * [New in Kubernetes v1.22: alpha support for using swap memory](https://kubernetes.io/blog/2021/08/09/run-nodes-with-swap-alpha/)
      * [Kubernetes 1.22: CSI Windows Support (with CSI Proxy) reaches GA](https://kubernetes.io/blog/2021/08/09/csi-windows-support-with-csi-proxy-reaches-ga/)
      * [Kubernetes 1.22: Server Side Apply moves to GA](https://kubernetes.io/blog/2021/08/06/server-side-apply-ga/)
      * [Kubernetes 1.22: Reaching New Peaks](https://kubernetes.io/blog/2021/08/04/kubernetes-1-22-release-announcement/)
      * [Roorkee robots, releases and racing: the Kubernetes 1.21 release interview](https://kubernetes.io/blog/2021/07/29/roorkee-robots-releases-and-racing-the-kubernetes-1.21-release-interview/)
      * [Updating NGINX-Ingress to use the stable Ingress API](https://kubernetes.io/blog/2021/07/26/update-with-ingress-nginx/)
      * [Kubernetes Release Cadence Change: Here’s What You Need To Know](https://kubernetes.io/blog/2021/07/20/new-kubernetes-release-cadence/)
      * [Spotlight on SIG Usability](https://kubernetes.io/blog/2021/07/15/sig-usability-spotlight-2021/)
      * [Kubernetes API and Feature Removals In 1.22: Here’s What You Need To Know](https://kubernetes.io/blog/2021/07/14/upcoming-changes-in-kubernetes-1-22/)
      * [Announcing Kubernetes Community Group Annual Reports](https://kubernetes.io/blog/2021/06/28/announcing-kubernetes-community-group-annual-reports/)
      * [Writing a Controller for Pod Labels](https://kubernetes.io/blog/2021/06/21/writing-a-controller-for-pod-labels/)
      * [Using Finalizers to Control Deletion](https://kubernetes.io/blog/2021/05/14/using-finalizers-to-control-deletion/)
      * [Kubernetes 1.21: Metrics Stability hits GA](https://kubernetes.io/blog/2021/04/23/kubernetes-release-1.21-metrics-stability-ga/)
      * [Evolving Kubernetes networking with the Gateway API](https://kubernetes.io/blog/2021/04/22/evolving-kubernetes-networking-with-the-gateway-api/)
      * [Graceful Node Shutdown Goes Beta](https://kubernetes.io/blog/2021/04/21/graceful-node-shutdown-beta/)
      * [Defining Network Policy Conformance for Container Network Interface (CNI) providers](https://kubernetes.io/blog/2021/04/20/defining-networkpolicy-conformance-cni-providers/)
      * [Annotating Kubernetes Services for Humans](https://kubernetes.io/blog/2021/04/20/annotating-k8s-for-humans/)
      * [Introducing Indexed Jobs](https://kubernetes.io/blog/2021/04/19/introducing-indexed-jobs/)
      * [Volume Health Monitoring Alpha Update](https://kubernetes.io/blog/2021/04/16/volume-health-monitoring-alpha-update/)
      * [Three Tenancy Models For Kubernetes](https://kubernetes.io/blog/2021/04/15/three-tenancy-models-for-kubernetes/)
      * [Local Storage: Storage Capacity Tracking, Distributed Provisioning and Generic Ephemeral Volumes hit Beta](https://kubernetes.io/blog/2021/04/14/local-storage-features-go-beta/)
      * [kube-state-metrics goes v2.0](https://kubernetes.io/blog/2021/04/13/kube-state-metrics-v-2-0/)
      * [Introducing Suspended Jobs](https://kubernetes.io/blog/2021/04/12/introducing-suspended-jobs/)
      * [Kubernetes 1.21: CronJob Reaches GA](https://kubernetes.io/blog/2021/04/09/kubernetes-release-1.21-cronjob-ga/)
      * [Kubernetes 1.21: Power to the Community](https://kubernetes.io/blog/2021/04/08/kubernetes-1-21-release-announcement/)
      * [PodSecurityPolicy Deprecation: Past, Present, and Future](https://kubernetes.io/blog/2021/04/06/podsecuritypolicy-deprecation-past-present-and-future/)
      * [The Evolution of Kubernetes Dashboard](https://kubernetes.io/blog/2021/03/09/the-evolution-of-kubernetes-dashboard/)
    * 2020
      * [A Custom Kubernetes Scheduler to Orchestrate Highly Available Applications](https://kubernetes.io/blog/2020/12/21/writing-crl-scheduler/)
      * [Kubernetes 1.20: Pod Impersonation and Short-lived Volumes in CSI Drivers](https://kubernetes.io/blog/2020/12/18/kubernetes-1.20-pod-impersonation-short-lived-volumes-in-csi/)
      * [Third Party Device Metrics Reaches GA](https://kubernetes.io/blog/2020/12/16/third-party-device-metrics-reaches-ga/)
      * [Kubernetes 1.20: Granular Control of Volume Permission Changes](https://kubernetes.io/blog/2020/12/14/kubernetes-release-1.20-fsgroupchangepolicy-fsgrouppolicy/)
      * [Kubernetes 1.20: Kubernetes Volume Snapshot Moves to GA](https://kubernetes.io/blog/2020/12/10/kubernetes-1.20-volume-snapshot-moves-to-ga/)
      * [Kubernetes 1.20: The Raddest Release](https://kubernetes.io/blog/2020/12/08/kubernetes-1-20-release-announcement/)
      * [GSoD 2020: Improving the API Reference Experience](https://kubernetes.io/blog/2020/12/04/gsod-2020-improving-api-reference-experience/)
      * [Don't Panic: Kubernetes and Docker](https://kubernetes.io/blog/2020/12/02/dont-panic-kubernetes-and-docker/)
      * [Dockershim Deprecation FAQ](https://kubernetes.io/blog/2020/12/02/dockershim-faq/)
      * [Cloud native security for your clusters](https://kubernetes.io/blog/2020/11/18/cloud-native-security-for-your-clusters/)
      * [Remembering Dan Kohn](https://kubernetes.io/blog/2020/11/02/remembering-dan-kohn/)
      * [Announcing the 2020 Steering Committee Election Results](https://kubernetes.io/blog/2020/10/12/steering-committee-results-2020/)
      * [Contributing to the Development Guide](https://kubernetes.io/blog/2020/10/01/contributing-to-the-development-guide/)
      * [GSoC 2020 - Building operators for cluster addons](https://kubernetes.io/blog/2020/09/16/gsoc20-building-operators-for-cluster-addons/)
      * [Introducing Structured Logs](https://kubernetes.io/blog/2020/09/04/kubernetes-1-19-introducing-structured-logs/)
      * [Warning: Helpful Warnings Ahead](https://kubernetes.io/blog/2020/09/03/warnings/)
      * [Scaling Kubernetes Networking With EndpointSlices](https://kubernetes.io/blog/2020/09/02/scaling-kubernetes-networking-with-endpointslices/)
      * [Ephemeral volumes with storage capacity tracking: EmptyDir on steroids](https://kubernetes.io/blog/2020/09/01/ephemeral-volumes-with-storage-capacity-tracking/)
      * [Increasing the Kubernetes Support Window to One Year](https://kubernetes.io/blog/2020/08/31/kubernetes-1-19-feature-one-year-support/)
      * [Kubernetes 1.19: Accentuate the Paw-sitive](https://kubernetes.io/blog/2020/08/26/kubernetes-release-1.19-accentuate-the-paw-sitive/)
      * [Moving Forward From Beta](https://kubernetes.io/blog/2020/08/21/moving-forward-from-beta/)
      * [Introducing Hierarchical Namespaces](https://kubernetes.io/blog/2020/08/14/introducing-hierarchical-namespaces/)
      * [Physics, politics and Pull Requests: the Kubernetes 1.18 release interview](https://kubernetes.io/blog/2020/08/03/physics-politics-and-pull-requests-the-kubernetes-1.18-release-interview/)
      * [Music and math: the Kubernetes 1.17 release interview](https://kubernetes.io/blog/2020/07/27/music-and-math-the-kubernetes-1.17-release-interview/)
      * [SIG-Windows Spotlight](https://kubernetes.io/blog/2020/06/30/sig-windows-spotlight-2020/)
      * [Working with Terraform and Kubernetes](https://kubernetes.io/blog/2020/06/working-with-terraform-and-kubernetes/)
      * [A Better Docs UX With Docsy](https://kubernetes.io/blog/2020/06/better-docs-ux-with-docsy/)
      * [Supporting the Evolving Ingress Specification in Kubernetes 1.18](https://kubernetes.io/blog/2020/06/05/supporting-the-evolving-ingress-specification-in-kubernetes-1.18/)
      * [K8s KPIs with Kuberhealthy](https://kubernetes.io/blog/2020/05/29/k8s-kpis-with-kuberhealthy/)
      * [My exciting journey into Kubernetes’ history](https://kubernetes.io/blog/2020/05/my-exciting-journey-into-kubernetes-history/)
      * [An Introduction to the K8s-Infrastructure Working Group](https://kubernetes.io/blog/2020/05/27/an-introduction-to-the-k8s-infrastructure-working-group/)
      * [WSL+Docker: Kubernetes on the Windows Desktop](https://kubernetes.io/blog/2020/05/21/wsl-docker-kubernetes-on-the-windows-desktop/)
      * [How Docs Handle Third Party and Dual Sourced Content](https://kubernetes.io/blog/2020/05/third-party-dual-sourced-content/)
      * [Introducing PodTopologySpread](https://kubernetes.io/blog/2020/05/Introducing-PodTopologySpread/)
      * [Two-phased Canary Rollout with Open Source Gloo](https://kubernetes.io/blog/2020/04/Two-phased-Canary-Rollout-With-Gloo/)
      * [How Kubernetes contributors are building a better communication process](https://kubernetes.io/blog/2020/04/21/contributor-communication/)
      * [Cluster API v1alpha3 Delivers New Features and an Improved User Experience](https://kubernetes.io/blog/2020/04/21/cluster-api-v1alpha3-delivers-new-features-and-an-improved-user-experience/)
      * [API Priority and Fairness Alpha](https://kubernetes.io/blog/2020/04/06/kubernetes-1-18-feature-api-priority-and-fairness-alpha/)
      * [Introducing Windows CSI support alpha for Kubernetes](https://kubernetes.io/blog/2020/04/03/kubernetes-1-18-feature-windows-csi-support-alpha/)
      * [Improvements to the Ingress API in Kubernetes 1.18](https://kubernetes.io/blog/2020/04/02/improvements-to-the-ingress-api-in-kubernetes-1.18/)
      * [Kubernetes Topology Manager Moves to Beta - Align Up!](https://kubernetes.io/blog/2020/04/01/kubernetes-1-18-feature-topology-manager-beta/)
      * [Kubernetes 1.18 Feature Server-side Apply Beta 2](https://kubernetes.io/blog/2020/04/01/kubernetes-1.18-feature-server-side-apply-beta-2/)
      * [Kubernetes 1.18: Fit & Finish](https://kubernetes.io/blog/2020/03/25/kubernetes-1-18-release-announcement/)
      * [Join SIG Scalability and Learn Kubernetes the Hard Way](https://kubernetes.io/blog/2020/03/19/join-sig-scalability/)
      * [Kong Ingress Controller and Service Mesh: Setting up Ingress to Istio on Kubernetes](https://kubernetes.io/blog/2020/03/18/kong-ingress-controller-and-istio-service-mesh/)
      * [Contributor Summit Amsterdam Postponed](https://kubernetes.io/blog/2020/03/04/contributor-summit-delayed/)
      * [Bring your ideas to the world with kubectl plugins](https://kubernetes.io/blog/2020/02/28/bring-your-ideas-to-the-world-with-kubectl-plugins/)
      * [Contributor Summit Amsterdam Schedule Announced](https://kubernetes.io/blog/2020/02/18/contributor-summit-amsterdam-schedule-announced/)
      * [Deploying External OpenStack Cloud Provider with Kubeadm](https://kubernetes.io/blog/2020/02/07/deploying-external-openstack-cloud-provider-with-kubeadm/)
      * [KubeInvaders - Gamified Chaos Engineering Tool for Kubernetes](https://kubernetes.io/blog/2020/01/22/kubeinvaders-gamified-chaos-engineering-tool-for-kubernetes/)
      * [Reviewing 2019 in Docs](https://kubernetes.io/blog/2020/01/21/reviewing-2019-in-docs/)
      * [CSI Ephemeral Inline Volumes](https://kubernetes.io/blog/2020/01/21/csi-ephemeral-inline-volumes/)
      * [Kubernetes on MIPS](https://kubernetes.io/blog/2020/01/15/kubernetes-on-mips/)
      * [Announcing the Kubernetes bug bounty program](https://kubernetes.io/blog/2020/01/14/kubernetes-bug-bounty-announcement/)
      * [Remembering Brad Childs](https://kubernetes.io/blog/2020/01/10/remembering-brad-childs/)
      * [Testing of CSI drivers](https://kubernetes.io/blog/2020/01/08/testing-of-csi-drivers/)
    * 2019
      * [Kubernetes 1.17: Stability](https://kubernetes.io/blog/2019/12/09/kubernetes-1-17-release-announcement/)
      * [Kubernetes 1.17 Feature: Kubernetes Volume Snapshot Moves to Beta](https://kubernetes.io/blog/2019/12/09/kubernetes-1-17-feature-cis-volume-snapshot-beta/)
      * [Kubernetes 1.17 Feature: Kubernetes In-Tree to CSI Volume Migration Moves to Beta](https://kubernetes.io/blog/2019/12/09/kubernetes-1-17-feature-csi-migration-beta/)
      * [When you're in the release team, you're family: the Kubernetes 1.16 release interview](https://kubernetes.io/blog/2019/12/06/when-youre-in-the-release-team-youre-family-the-kubernetes-1.16-release-interview/)
      * [Gardener Project Update](https://kubernetes.io/blog/2019/12/02/gardener-project-update/)
      * [Running Kubernetes locally on Linux with Microk8s](https://kubernetes.io/blog/2019/11/26/running-kubernetes-locally-on-linux-with-microk8s/)
      * [Develop a Kubernetes controller in Java](https://kubernetes.io/blog/2019/11/26/develop-a-kubernetes-controller-in-java/)
      * [Grokkin' the Docs](https://kubernetes.io/blog/2019/11/05/grokkin-the-docs/)
      * [Kubernetes Documentation Survey](https://kubernetes.io/blog/2019/10/29/kubernetes-documentation-end-user-survey/)
      * [Contributor Summit San Diego Schedule Announced!](https://kubernetes.io/blog/2019/10/10/contributor-summit-san-diego-schedule/)
      * [2019 Steering Committee Election Results](https://kubernetes.io/blog/2019/10/03/2019-steering-committee-election-results/)
      * [Contributor Summit San Diego Registration Open!](https://kubernetes.io/blog/2019/09/24/san-diego-contributor-summit/)
      * [Kubernetes 1.16: Custom Resources, Overhauled Metrics, and Volume Extensions](https://kubernetes.io/blog/2019/09/18/kubernetes-1-16-release-announcement/)
      * [Announcing etcd 3.4](https://kubernetes.io/blog/2019/08/30/announcing-etcd-3-4/)
      * [OPA Gatekeeper: Policy and Governance for Kubernetes](https://kubernetes.io/blog/2019/08/06/opa-gatekeeper-policy-and-governance-for-kubernetes/)
      * [Get started with Kubernetes (using Python)](https://kubernetes.io/blog/2019/07/23/get-started-with-kubernetes-using-python/)
      * [Deprecated APIs Removed In 1.16: Here’s What You Need To Know](https://kubernetes.io/blog/2019/07/18/api-deprecations-in-1-16/)
      * [Recap of Kubernetes Contributor Summit Barcelona 2019](https://kubernetes.io/blog/2019/06/25/recap-of-kubernetes-contributor-summit-barcelona-2019/)
      * [Automated High Availability in kubeadm v1.15: Batteries Included But Swappable](https://kubernetes.io/blog/2019/06/24/automated-high-availability-in-kubeadm-v1.15-batteries-included-but-swappable/)
      * [Introducing Volume Cloning Alpha for Kubernetes](https://kubernetes.io/blog/2019/06/21/introducing-volume-cloning-alpha-for-kubernetes/)
      * [Future of CRDs: Structural Schemas](https://kubernetes.io/blog/2019/06/20/crd-structural-schema/)
      * [Kubernetes 1.15: Extensibility and Continuous Improvement](https://kubernetes.io/blog/2019/06/19/kubernetes-1-15-release-announcement/)
      * [Join us at the Contributor Summit in Shanghai](https://kubernetes.io/blog/2019/06/12/join-us-at-the-contributor-summit-in-shanghai/)
      * [Kyma - extend and build on Kubernetes with ease](https://kubernetes.io/blog/2019/05/23/kyma-extend-and-build-on-kubernetes-with-ease/)
      * [Kubernetes, Cloud Native, and the Future of Software](https://kubernetes.io/blog/2019/05/17/kubernetes-cloud-native-and-the-future-of-software/)
      * [Expanding our Contributor Workshops](https://kubernetes.io/blog/2019/05/14/expanding-our-contributor-workshops/)
      * [Cat shirts and Groundhog Day: the Kubernetes 1.14 release interview](https://kubernetes.io/blog/2019/05/13/cat-shirts-and-groundhog-day-the-kubernetes-1.14-release-interview/)
      * [Join us for the 2019 KubeCon Diversity Lunch & Hack](https://kubernetes.io/blog/2019/05/02/kubecon-diversity-lunch-and-hack/)
      * [How You Can Help Localize Kubernetes Docs](https://kubernetes.io/blog/2019/04/26/how-you-can-help-localize-kubernetes-docs/)
      * [Hardware Accelerated SSL/TLS Termination in Ingress Controllers using Kubernetes Device Plugins and RuntimeClass](https://kubernetes.io/blog/2019/04/24/hardware-accelerated-ssl/tls-termination-in-ingress-controllers-using-kubernetes-device-plugins-and-runtimeclass/)
      * [Introducing kube-iptables-tailer: Better Networking Visibility in Kubernetes Clusters](https://kubernetes.io/blog/2019/04/19/introducing-kube-iptables-tailer/)
      * [The Future of Cloud Providers in Kubernetes](https://kubernetes.io/blog/2019/04/17/the-future-of-cloud-providers-in-kubernetes/)
      * [Pod Priority and Preemption in Kubernetes](https://kubernetes.io/blog/2019/04/16/pod-priority-and-preemption-in-kubernetes/)
      * [Process ID Limiting for Stability Improvements in Kubernetes 1.14](https://kubernetes.io/blog/2019/04/15/process-id-limiting-for-stability-improvements-in-kubernetes-1.14/)
      * [Kubernetes 1.14: Local Persistent Volumes GA](https://kubernetes.io/blog/2019/04/04/kubernetes-1.14-local-persistent-volumes-ga/)
      * [Kubernetes v1.14 delivers production-level support for Windows nodes and Windows containers](https://kubernetes.io/blog/2019/04/01/kubernetes-v1.14-delivers-production-level-support-for-windows-nodes-and-windows-containers/)
      * [kube-proxy Subtleties: Debugging an Intermittent Connection Reset](https://kubernetes.io/blog/2019/03/29/kube-proxy-subtleties-debugging-an-intermittent-connection-reset/)
      * [Running Kubernetes locally on Linux with Minikube - now with Kubernetes 1.14 support](https://kubernetes.io/blog/2019/03/28/running-kubernetes-locally-on-linux-with-minikube-now-with-kubernetes-1.14-support/)
      * [Kubernetes 1.14: Production-level support for Windows Nodes, Kubectl Updates, Persistent Local Volumes GA](https://kubernetes.io/blog/2019/03/25/kubernetes-1-14-release-announcement/)
      * [Kubernetes End-to-end Testing for Everyone](https://kubernetes.io/blog/2019/03/22/kubernetes-end-to-end-testing-for-everyone/)
      * [A Guide to Kubernetes Admission Controllers](https://kubernetes.io/blog/2019/03/21/a-guide-to-kubernetes-admission-controllers/)
      * [A Look Back and What's in Store for Kubernetes Contributor Summits](https://kubernetes.io/blog/2019/03/20/a-look-back-and-whats-in-store-for-kubernetes-contributor-summits/)
      * [KubeEdge, a Kubernetes Native Edge Computing Framework](https://kubernetes.io/blog/2019/03/19/kubeedge-k8s-based-edge-intro/)
      * [Kubernetes Setup Using Ansible and Vagrant](https://kubernetes.io/blog/2019/03/15/kubernetes-setup-using-ansible-and-vagrant/)
      * [Raw Block Volume support to Beta](https://kubernetes.io/blog/2019/03/07/raw-block-volume-support-to-beta/)
      * [Automate Operations on your Cluster with OperatorHub.io](https://kubernetes.io/blog/2019/02/28/automate-operations-on-your-cluster-with-operatorhub.io/)
      * [Building a Kubernetes Edge (Ingress) Control Plane for Envoy v2](https://kubernetes.io/blog/2019/02/12/building-a-kubernetes-edge-control-plane-for-envoy-v2/)
      * [Runc and CVE-2019-5736](https://kubernetes.io/blog/2019/02/11/runc-and-cve-2019-5736/)
      * [Poseidon-Firmament Scheduler – Flow Network Graph Based Scheduler](https://kubernetes.io/blog/2019/02/06/poseidon-firmament-scheduler-flow-network-graph-based-scheduler/)
      * [Update on Volume Snapshot Alpha for Kubernetes](https://kubernetes.io/blog/2019/01/17/update-on-volume-snapshot-alpha-for-kubernetes/)
      * [Container Storage Interface (CSI) for Kubernetes GA](https://kubernetes.io/blog/2019/01/15/container-storage-interface-ga/)
      * [APIServer dry-run and kubectl diff](https://kubernetes.io/blog/2019/01/14/apiserver-dry-run-and-kubectl-diff/)
    * 2018
      * [Kubernetes Federation Evolution](https://kubernetes.io/blog/2018/12/12/kubernetes-federation-evolution/)
      * [etcd: Current status and future roadmap](https://kubernetes.io/blog/2018/12/11/etcd-current-status-and-future-roadmap/)
      * [New Contributor Workshop Shanghai](https://kubernetes.io/blog/2018/12/05/new-contributor-workshop-shanghai/)
      * [Production-Ready Kubernetes Cluster Creation with kubeadm](https://kubernetes.io/blog/2018/12/04/production-ready-kubernetes-cluster-creation-with-kubeadm/)
      * [Kubernetes 1.13: Simplified Cluster Management with Kubeadm, Container Storage Interface (CSI), and CoreDNS as Default DNS are Now Generally Available](https://kubernetes.io/blog/2018/12/03/kubernetes-1-13-release-announcement/)
      * [Kubernetes Docs Updates, International Edition](https://kubernetes.io/blog/2018/11/08/kubernetes-docs-updates-international-edition/)
      * [gRPC Load Balancing on Kubernetes without Tears](https://kubernetes.io/blog/2018/11/07/grpc-load-balancing-on-kubernetes-without-tears/)
      * [Tips for Your First Kubecon Presentation - Part 2](https://kubernetes.io/blog/2018/10/26/tips-for-your-first-kubecon-presentation-part-2/)
      * [Tips for Your First Kubecon Presentation - Part 1](https://kubernetes.io/blog/2018/10/18/tips-for-your-first-kubecon-presentation-part-1/)
      * [Kubernetes 2018 North American Contributor Summit](https://kubernetes.io/blog/2018/10/16/kubernetes-2018-north-american-contributor-summit/)
      * [2018 Steering Committee Election Results](https://kubernetes.io/blog/2018/10/15/2018-steering-committee-election-results/)
      * [Topology-Aware Volume Provisioning in Kubernetes](https://kubernetes.io/blog/2018/10/11/topology-aware-volume-provisioning-in-kubernetes/)
      * [Kubernetes v1.12: Introducing RuntimeClass](https://kubernetes.io/blog/2018/10/10/kubernetes-v1.12-introducing-runtimeclass/)
      * [Introducing Volume Snapshot Alpha for Kubernetes](https://kubernetes.io/blog/2018/10/09/introducing-volume-snapshot-alpha-for-kubernetes/)
      * [Support for Azure VMSS, Cluster-Autoscaler and User Assigned Identity](https://kubernetes.io/blog/2018/10/08/support-for-azure-vmss-cluster-autoscaler-and-user-assigned-identity/)
      * [Introducing the Non-Code Contributor’s Guide](https://kubernetes.io/blog/2018/10/04/introducing-the-non-code-contributors-guide/)
      * [KubeDirector: The easy way to run complex stateful applications on Kubernetes](https://kubernetes.io/blog/2018/10/03/kubedirector-the-easy-way-to-run-complex-stateful-applications-on-kubernetes/)
      * [Building a Network Bootable Server Farm for Kubernetes with LTSP](https://kubernetes.io/blog/2018/10/02/building-a-network-bootable-server-farm-for-kubernetes-with-ltsp/)
      * [Health checking gRPC servers on Kubernetes](https://kubernetes.io/blog/2018/10/01/health-checking-grpc-servers-on-kubernetes/)
      * [Kubernetes 1.12: Kubelet TLS Bootstrap and Azure Virtual Machine Scale Sets (VMSS) Move to General Availability](https://kubernetes.io/blog/2018/09/27/kubernetes-1-12-release-announcement/)
      * [Hands On With Linkerd 2.0](https://kubernetes.io/blog/2018/09/18/hands-on-with-linkerd-2.0/)
      * [2018 Steering Committee Election Cycle Kicks Off](https://kubernetes.io/blog/2018/09/06/2018-steering-committee-election-cycle-kicks-off/)
      * [The Machines Can Do the Work, a Story of Kubernetes Testing, CI, and Automating the Contributor Experience](https://kubernetes.io/blog/2018/08/29/the-machines-can-do-the-work-a-story-of-kubernetes-testing-ci-and-automating-the-contributor-experience/)
      * [Introducing Kubebuilder: an SDK for building Kubernetes APIs using CRDs](https://kubernetes.io/blog/2018/08/10/introducing-kubebuilder-an-sdk-for-building-kubernetes-apis-using-crds/)
      * [Out of the Clouds onto the Ground: How to Make Kubernetes Production Grade Anywhere](https://kubernetes.io/blog/2018/08/03/out-of-the-clouds-onto-the-ground-how-to-make-kubernetes-production-grade-anywhere/)
      * [Dynamically Expand Volume with CSI and Kubernetes](https://kubernetes.io/blog/2018/08/02/dynamically-expand-volume-with-csi-and-kubernetes/)
      * [KubeVirt: Extending Kubernetes with CRDs for Virtualized Workloads](https://kubernetes.io/blog/2018/07/27/kubevirt-extending-kubernetes-with-crds-for-virtualized-workloads/)
      * [Feature Highlight: CPU Manager](https://kubernetes.io/blog/2018/07/24/feature-highlight-cpu-manager/)
      * [The History of Kubernetes & the Community Behind It](https://kubernetes.io/blog/2018/07/20/the-history-of-kubernetes-the-community-behind-it/)
      * [Kubernetes Wins the 2018 OSCON Most Impact Award](https://kubernetes.io/blog/2018/07/19/kubernetes-wins-2018-oscon-most-impact-award/)
      * [11 Ways (Not) to Get Hacked](https://kubernetes.io/blog/2018/07/18/11-ways-not-to-get-hacked/)
      * [How the sausage is made: the Kubernetes 1.11 release interview, from the Kubernetes Podcast](https://kubernetes.io/blog/2018/07/16/how-the-sausage-is-made-the-kubernetes-1.11-release-interview-from-the-kubernetes-podcast/)
      * [Resizing Persistent Volumes using Kubernetes](https://kubernetes.io/blog/2018/07/12/resizing-persistent-volumes-using-kubernetes/)
      * [Dynamic Kubelet Configuration](https://kubernetes.io/blog/2018/07/11/dynamic-kubelet-configuration/)
      * [Meet Our Contributors - Monthly Streaming YouTube Mentoring Series](https://kubernetes.io/blog/2018/07/10/meet-our-contributors-monthly-streaming-youtube-mentoring-series/)
      * [CoreDNS GA for Kubernetes Cluster DNS](https://kubernetes.io/blog/2018/07/10/coredns-ga-for-kubernetes-cluster-dns/)
      * [IPVS-Based In-Cluster Load Balancing Deep Dive](https://kubernetes.io/blog/2018/07/09/ipvs-based-in-cluster-load-balancing-deep-dive/)
      * [Airflow on Kubernetes (Part 1): A Different Kind of Operator](https://kubernetes.io/blog/2018/06/28/airflow-on-kubernetes-part-1-a-different-kind-of-operator/)
      * [Kubernetes 1.11: In-Cluster Load Balancing and CoreDNS Plugin Graduate to General Availability](https://kubernetes.io/blog/2018/06/27/kubernetes-1.11-release-announcement/)
      * [Dynamic Ingress in Kubernetes](https://kubernetes.io/blog/2018/06/07/dynamic-ingress-in-kubernetes/)
      * [4 Years of K8s](https://kubernetes.io/blog/2018/06/06/4-years-of-k8s/)
      * [Say Hello to Discuss Kubernetes](https://kubernetes.io/blog/2018/05/30/say-hello-to-discuss-kubernetes/)
      * [Introducing kustomize; Template-free Configuration Customization for Kubernetes](https://kubernetes.io/blog/2018/05/29/introducing-kustomize-template-free-configuration-customization-for-kubernetes/)
      * [Kubernetes Containerd Integration Goes GA](https://kubernetes.io/blog/2018/05/24/kubernetes-containerd-integration-goes-ga/)
      * [Getting to Know Kubevirt](https://kubernetes.io/blog/2018/05/22/getting-to-know-kubevirt/)
      * [Gardener - The Kubernetes Botanist](https://kubernetes.io/blog/2018/05/17/gardener/)
      * [Docs are Migrating from Jekyll to Hugo](https://kubernetes.io/blog/2018/05/05/hugo-migration/)
      * [Announcing Kubeflow 0.1](https://kubernetes.io/blog/2018/05/04/announcing-kubeflow-0.1/)
      * [Current State of Policy in Kubernetes](https://kubernetes.io/blog/2018/05/02/policy-in-kubernetes/)
      * [Developing on Kubernetes](https://kubernetes.io/blog/2018/05/01/developing-on-kubernetes/)
      * [Zero-downtime Deployment in Kubernetes with Jenkins](https://kubernetes.io/blog/2018/04/30/zero-downtime-deployment-kubernetes-jenkins/)
      * [Kubernetes Community - Top of the Open Source Charts in 2017](https://kubernetes.io/blog/2018/04/25/open-source-charts-2017/)
      * [Kubernetes Application Survey 2018 Results](https://kubernetes.io/blog/2018/04/24/kubernetes-application-survey-results-2018/)
      * [Local Persistent Volumes for Kubernetes Goes Beta](https://kubernetes.io/blog/2018/04/13/local-persistent-volumes-beta/)
      * [Migrating the Kubernetes Blog](https://kubernetes.io/blog/2018/04/11/migrating-the-kubernetes-blog/)
      * [Container Storage Interface (CSI) for Kubernetes Goes Beta](https://kubernetes.io/blog/2018/04/10/container-storage-interface-beta/)
      * [Fixing the Subpath Volume Vulnerability in Kubernetes](https://kubernetes.io/blog/2018/04/04/fixing-subpath-volume-vulnerability/)
      * [Kubernetes 1.10: Stabilizing Storage, Security, and Networking](https://kubernetes.io/blog/2018/03/26/kubernetes-1.10-stabilizing-storage-security-networking/)
      * [Principles of Container-based Application Design](https://kubernetes.io/blog/2018/03/principles-of-container-app-design/)
      * [Expanding User Support with Office Hours](https://kubernetes.io/blog/2018/03/expanding-user-support-with-office-hours/)
      * [How to Integrate RollingUpdate Strategy for TPR in Kubernetes](https://kubernetes.io/blog/2018/03/how-to-integrate-rollingupdate-strategy/)
      * [Apache Spark 2.3 with Native Kubernetes Support](https://kubernetes.io/blog/2018/03/apache-spark-23-with-native-kubernetes/)
      * [Kubernetes: First Beta Version of Kubernetes 1.10 is Here](https://kubernetes.io/blog/2018/03/first-beta-version-of-kubernetes-1-10/)
      * [Reporting Errors from Control Plane to Applications Using Kubernetes Events](https://kubernetes.io/blog/2018/01/reporting-errors-using-kubernetes-events/)
      * [Core Workloads API GA](https://kubernetes.io/blog/2018/01/core-workloads-api-ga/)
      * [Introducing client-go version 6](https://kubernetes.io/blog/2018/01/introducing-client-go-version-6/)
      * [Extensible Admission is Beta](https://kubernetes.io/blog/2018/01/extensible-admission-is-beta/)
      * [Introducing Container Storage Interface (CSI) Alpha for Kubernetes](https://kubernetes.io/blog/2018/01/introducing-container-storage-interface/)
      * [Kubernetes v1.9 releases beta support for Windows Server Containers](https://kubernetes.io/blog/2018/01/kubernetes-v19-beta-windows-support/)
      * [Five Days of Kubernetes 1.9](https://kubernetes.io/blog/2018/01/five-days-of-kubernetes-19/)
    * 2017
      * [Introducing Kubeflow - A Composable, Portable, Scalable ML Stack Built for Kubernetes](https://kubernetes.io/blog/2017/12/introducing-kubeflow-composable/)
      * [Kubernetes 1.9: Apps Workloads GA and Expanded Ecosystem](https://kubernetes.io/blog/2017/12/kubernetes-19-workloads-expanded-ecosystem/)
      * [Using eBPF in Kubernetes](https://kubernetes.io/blog/2017/12/using-ebpf-in-kubernetes/)
      * [PaddlePaddle Fluid: Elastic Deep Learning on Kubernetes](https://kubernetes.io/blog/2017/12/paddle-paddle-fluid-elastic-learning/)
      * [Autoscaling in Kubernetes](https://kubernetes.io/blog/2017/11/autoscaling-in-kubernetes/)
      * [Certified Kubernetes Conformance Program: Launch Celebration Round Up](https://kubernetes.io/blog/2017/11/certified-kubernetes-conformance/)
      * [Kubernetes is Still Hard (for Developers)](https://kubernetes.io/blog/2017/11/kubernetes-is-still-hard-for-developers/)
      * [Securing Software Supply Chain with Grafeas](https://kubernetes.io/blog/2017/11/securing-software-supply-chain-grafeas/)
      * [Containerd Brings More Container Runtime Options for Kubernetes](https://kubernetes.io/blog/2017/11/containerd-container-runtime-options-kubernetes/)
      * [Kubernetes the Easy Way](https://kubernetes.io/blog/2017/11/kubernetes-easy-way/)
      * [Enforcing Network Policies in Kubernetes](https://kubernetes.io/blog/2017/10/enforcing-network-policies-in-kubernetes/)
      * [Using RBAC, Generally Available in Kubernetes v1.8](https://kubernetes.io/blog/2017/10/using-rbac-generally-available-18/)
      * [It Takes a Village to Raise a Kubernetes](https://kubernetes.io/blog/2017/10/it-takes-village-to-raise-kubernetes/)
      * [kubeadm v1.8 Released: Introducing Easy Upgrades for Kubernetes Clusters](https://kubernetes.io/blog/2017/10/kubeadm-v18-released/)
      * [Five Days of Kubernetes 1.8](https://kubernetes.io/blog/2017/10/five-days-of-kubernetes-18/)
      * [Introducing Software Certification for Kubernetes](https://kubernetes.io/blog/2017/10/software-conformance-certification/)
      * [Request Routing and Policy Management with the Istio Service Mesh](https://kubernetes.io/blog/2017/10/request-routing-and-policy-management/)
      * [Kubernetes Community Steering Committee Election Results](https://kubernetes.io/blog/2017/10/kubernetes-community-steering-committee-election-results/)
      * [Kubernetes 1.8: Security, Workloads and Feature Depth](https://kubernetes.io/blog/2017/09/kubernetes-18-security-workloads-and/)
      * [Kubernetes StatefulSets & DaemonSets Updates](https://kubernetes.io/blog/2017/09/kubernetes-statefulsets-daemonsets/)
      * [Introducing the Resource Management Working Group](https://kubernetes.io/blog/2017/09/introducing-resource-management-working/)
      * [Windows Networking at Parity with Linux for Kubernetes](https://kubernetes.io/blog/2017/09/windows-networking-at-parity-with-linux/)
      * [Kubernetes Meets High-Performance Computing](https://kubernetes.io/blog/2017/08/kubernetes-meets-high-performance/)
      * [High Performance Networking with EC2 Virtual Private Clouds](https://kubernetes.io/blog/2017/08/high-performance-networking-with-ec2/)
      * [Kompose Helps Developers Move Docker Compose Files to Kubernetes](https://kubernetes.io/blog/2017/08/kompose-helps-developers-move-docker/)
      * [Happy Second Birthday: A Kubernetes Retrospective](https://kubernetes.io/blog/2017/07/happy-second-birthday-kubernetes/)
      * [How Watson Health Cloud Deploys Applications with Kubernetes](https://kubernetes.io/blog/2017/07/how-watson-health-cloud-deploys/)
      * [Kubernetes 1.7: Security Hardening, Stateful Application Updates and Extensibility](https://kubernetes.io/blog/2017/06/kubernetes-1-7-security-hardening-stateful-application-extensibility-updates/)
      * [Draft: Kubernetes container development made easy](https://kubernetes.io/blog/2017/05/draft-kubernetes-container-development/)
      * [Managing microservices with the Istio service mesh](https://kubernetes.io/blog/2017/05/managing-microservices-with-istio-service-mesh/)
      * [Kubespray Ansible Playbooks foster Collaborative Kubernetes Ops](https://kubernetes.io/blog/2017/05/kubespray-ansible-collaborative-kubernetes-ops/)
      * [Kubernetes: a monitoring guide](https://kubernetes.io/blog/2017/05/kubernetes-monitoring-guide/)
      * [Dancing at the Lip of a Volcano: The Kubernetes Security Process - Explained](https://kubernetes.io/blog/2017/05/kubernetes-security-process-explained/)
      * [How Bitmovin is Doing Multi-Stage Canary Deployments with Kubernetes in the Cloud and On-Prem](https://kubernetes.io/blog/2017/04/multi-stage-canary-deployments-with-kubernetes-in-the-cloud-onprem/)
      * [RBAC Support in Kubernetes](https://kubernetes.io/blog/2017/04/rbac-support-in-kubernetes/)
      * [Configuring Private DNS Zones and Upstream Nameservers in Kubernetes](https://kubernetes.io/blog/2017/04/configuring-private-dns-zones-upstream-nameservers-kubernetes/)
      * [Advanced Scheduling in Kubernetes](https://kubernetes.io/blog/2017/03/advanced-scheduling-in-kubernetes/)
      * [Scalability updates in Kubernetes 1.6: 5,000 node and 150,000 pod clusters](https://kubernetes.io/blog/2017/03/scalability-updates-in-kubernetes-1-6/)
      * [Five Days of Kubernetes 1.6](https://kubernetes.io/blog/2017/03/five-days-of-kubernetes-1-6/)
      * [Dynamic Provisioning and Storage Classes in Kubernetes](https://kubernetes.io/blog/2017/03/dynamic-provisioning-and-storage-classes-kubernetes/)
      * [Kubernetes 1.6: Multi-user, Multi-workloads at Scale](https://kubernetes.io/blog/2017/03/kubernetes-1-6-multi-user-multi-workloads-at-scale/)
      * [The K8sPort: Engaging Kubernetes Community One Activity at a Time](https://kubernetes.io/blog/2017/03/k8sport-engaging-the-kubernetes-community/)
      * [Deploying PostgreSQL Clusters using StatefulSets](https://kubernetes.io/blog/2017/02/postgresql-clusters-kubernetes-statefulsets/)
      * [Containers as a Service, the foundation for next generation PaaS](https://kubernetes.io/blog/2017/02/caas-the-foundation-for-next-gen-paas/)
      * [Inside JD.com's Shift to Kubernetes from OpenStack](https://kubernetes.io/blog/2017/02/inside-jd-com-shift-to-kubernetes-from-openstack/)
      * [Run Deep Learning with PaddlePaddle on Kubernetes](https://kubernetes.io/blog/2017/02/run-deep-learning-with-paddlepaddle-on-kubernetes/)
      * [Highly Available Kubernetes Clusters](https://kubernetes.io/blog/2017/02/highly-available-kubernetes-clusters/)
      * [Running MongoDB on Kubernetes with StatefulSets](https://kubernetes.io/blog/2017/01/running-mongodb-on-kubernetes-with-statefulsets/)
      * [Fission: Serverless Functions as a Service for Kubernetes](https://kubernetes.io/blog/2017/01/fission-serverless-functions-as-service-for-kubernetes/)
      * [How we run Kubernetes in Kubernetes aka Kubeception](https://kubernetes.io/blog/2017/01/how-we-run-kubernetes-in-kubernetes-kubeception/)
      * [Scaling Kubernetes deployments with Policy-Based Networking](https://kubernetes.io/blog/2017/01/scaling-kubernetes-deployments-with-policy-base-networking/)
      * [A Stronger Foundation for Creating and Managing Kubernetes Clusters](https://kubernetes.io/blog/2017/01/stronger-foundation-for-creating-and-managing-kubernetes-clusters/)
      * [Kubernetes UX Survey Infographic](https://kubernetes.io/blog/2017/01/kubernetes-ux-survey-infographic/)
    * 2016
      * [Kubernetes supports OpenAPI](https://kubernetes.io/blog/2016/12/kubernetes-supports-openapi/)
      * [Cluster Federation in Kubernetes 1.5](https://kubernetes.io/blog/2016/12/cluster-federation-in-kubernetes-1-5/)
      * [Windows Server Support Comes to Kubernetes](https://kubernetes.io/blog/2016/12/windows-server-support-kubernetes/)
      * [StatefulSet: Run and Scale Stateful Applications Easily in Kubernetes](https://kubernetes.io/blog/2016/12/statefulset-run-scale-stateful-applications-in-kubernetes/)
      * [Introducing Container Runtime Interface (CRI) in Kubernetes](https://kubernetes.io/blog/2016/12/container-runtime-interface-cri-in-kubernetes/)
      * [Five Days of Kubernetes 1.5](https://kubernetes.io/blog/2016/12/five-days-of-kubernetes-1-5/)
      * [Kubernetes 1.5: Supporting Production Workloads](https://kubernetes.io/blog/2016/12/kubernetes-1-5-supporting-production-workloads/)
      * [From Network Policies to Security Policies](https://kubernetes.io/blog/2016/12/from-network-policies-to-security-policies/)
      * [Kompose: a tool to go from Docker-compose to Kubernetes](https://kubernetes.io/blog/2016/11/kompose-tool-go-from-docker-compose-to-kubernetes/)
      * [Kubernetes Containers Logging and Monitoring with Sematext](https://kubernetes.io/blog/2016/11/kubernetes-containers-logging-monitoring-with-sematext/)
      * [Visualize Kubelet Performance with Node Dashboard](https://kubernetes.io/blog/2016/11/visualize-kubelet-performance-with-node-dashboard/)
      * [CNCF Partners With The Linux Foundation To Launch New Kubernetes Certification, Training and Managed Service Provider Program](https://kubernetes.io/blog/2016/11/kubernetes-certification-training-and-managed-service-provider-program/)
      * [Modernizing the Skytap Cloud Micro-Service Architecture with Kubernetes](https://kubernetes.io/blog/2016/11/skytap-modernizing-microservice-architecture-with-kubernetes/)
      * [Bringing Kubernetes Support to Azure Container Service](https://kubernetes.io/blog/2016/11/bringing-kubernetes-support-to-azure/)
      * [Tail Kubernetes with Stern](https://kubernetes.io/blog/2016/10/tail-kubernetes-with-stern/)
      * [Introducing Kubernetes Service Partners program and a redesigned Partners page](https://kubernetes.io/blog/2016/10/kubernetes-service-technology-partners-program/)
      * [How We Architected and Run Kubernetes on OpenStack at Scale at Yahoo! JAPAN](https://kubernetes.io/blog/2016/10/kubernetes-and-openstack-at-yahoo-japan/)
      * [Building Globally Distributed Services using Kubernetes Cluster Federation](https://kubernetes.io/blog/2016/10/globally-distributed-services-kubernetes-cluster-federation/)
      * [Helm Charts: making it simple to package and deploy common applications on Kubernetes](https://kubernetes.io/blog/2016/10/helm-charts-making-it-simple-to-package-and-deploy-apps-on-kubernetes/)
      * [Dynamic Provisioning and Storage Classes in Kubernetes](https://kubernetes.io/blog/2016/10/dynamic-provisioning-and-storage-in-kubernetes/)
      * [How we improved Kubernetes Dashboard UI in 1.4 for your production needs​](https://kubernetes.io/blog/2016/10/production-kubernetes-dashboard-ui-1-4-improvements_3/)
      * [How we made Kubernetes insanely easy to install](https://kubernetes.io/blog/2016/09/how-we-made-kubernetes-easy-to-install/)
      * [How Qbox Saved 50% per Month on AWS Bills Using Kubernetes and Supergiant](https://kubernetes.io/blog/2016/09/how-qbox-saved-50-percent-on-aws-bills/)
      * [Kubernetes 1.4: Making it easy to run on Kubernetes anywhere](https://kubernetes.io/blog/2016/09/kubernetes-1-4-making-it-easy-to-run-on-kuberentes-anywhere/)
      * [High performance network policies in Kubernetes clusters](https://kubernetes.io/blog/2016/09/high-performance-network-policies-kubernetes/)
      * [Creating a PostgreSQL Cluster using Helm](https://kubernetes.io/blog/2016/09/creating-postgresql-cluster-using-helm/)
      * [Deploying to Multiple Kubernetes Clusters with kit](https://kubernetes.io/blog/2016/09/deploying-to-multiple-kubernetes-with-kit/)
      * [Cloud Native Application Interfaces](https://kubernetes.io/blog/2016/09/cloud-native-application-interfaces/)
      * [Security Best Practices for Kubernetes Deployment](https://kubernetes.io/blog/2016/08/security-best-practices-kubernetes-deployment/)
      * [Scaling Stateful Applications using Kubernetes Pet Sets and FlexVolumes with Datera Elastic Data Fabric](https://kubernetes.io/blog/2016/08/stateful-applications-using-kubernetes-datera/)
      * [SIG Apps: build apps for and operate them in Kubernetes](https://kubernetes.io/blog/2016/08/sig-apps-running-apps-in-kubernetes/)
      * [Kubernetes Namespaces: use cases and insights](https://kubernetes.io/blog/2016/08/kubernetes-namespaces-use-cases-insights/)
      * [Create a Couchbase cluster using Kubernetes](https://kubernetes.io/blog/2016/08/create-couchbase-cluster-using-kubernetes/)
      * [Challenges of a Remotely Managed, On-Premises, Bare-Metal Kubernetes Cluster](https://kubernetes.io/blog/2016/08/challenges-remotely-managed-onpremise-kubernetes-cluster/)
      * [Why OpenStack's embrace of Kubernetes is great for both communities](https://kubernetes.io/blog/2016/07/openstack-kubernetes-communities/)
      * [The Bet on Kubernetes, a Red Hat Perspective](https://kubernetes.io/blog/2016/07/the-bet-on-kubernetes/)
      * [Happy Birthday Kubernetes. Oh, the places you’ll go!](https://kubernetes.io/blog/2016/07/oh-the-places-you-will-go/)
      * [A Very Happy Birthday Kubernetes](https://kubernetes.io/blog/2016/07/happy-k8sbday-1/)
      * [Bringing End-to-End Kubernetes Testing to Azure (Part 2)](https://kubernetes.io/blog/2016/07/bringing-end-to-end-kubernetes-testing-to-azure-2/)
      * [Steering an Automation Platform at Wercker with Kubernetes](https://kubernetes.io/blog/2016/07/automation-platform-at-wercker-with-kubernetes/)
      * [Dashboard - Full Featured Web Interface for Kubernetes](https://kubernetes.io/blog/2016/07/dashboard-web-interface-for-kubernetes/)
      * [Cross Cluster Services - Achieving Higher Availability for your Kubernetes Applications](https://kubernetes.io/blog/2016/07/cross-cluster-services/)
      * [Citrix + Kubernetes = A Home Run](https://kubernetes.io/blog/2016/07/citrix-netscaler-and-kubernetes/)
      * [Thousand Instances of Cassandra using Kubernetes Pet Set](https://kubernetes.io/blog/2016/07/thousand-instances-of-cassandra-using-kubernetes-pet-set/)
      * [Stateful Applications in Containers!? Kubernetes 1.3 Says “Yes!”](https://kubernetes.io/blog/2016/07/stateful-applications-in-containers-kubernetes/)
      * [Kubernetes in Rancher: the further evolution](https://kubernetes.io/blog/2016/07/kubernetes-in-rancher-further-evolution/)
      * [Autoscaling in Kubernetes](https://kubernetes.io/blog/2016/07/autoscaling-in-kubernetes/)
      * [rktnetes brings rkt container engine to Kubernetes](https://kubernetes.io/blog/2016/07/rktnetes-brings-rkt-container-engine-to-kubernetes/)
      * [Minikube: easily run Kubernetes locally](https://kubernetes.io/blog/2016/07/minikube-easily-run-kubernetes-locally/)
      * [Five Days of Kubernetes 1.3](https://kubernetes.io/blog/2016/07/five-days-of-kubernetes-1-3/)
      * [Updates to Performance and Scalability in Kubernetes 1.3 -- 2,000 node 60,000 pod clusters](https://kubernetes.io/blog/2016/07/update-on-kubernetes-for-windows-server-containers/)
      * [Kubernetes 1.3: Bridging Cloud Native and Enterprise Workloads](https://kubernetes.io/blog/2016/07/kubernetes-1-3-bridging-cloud-native-and-enterprise-workloads/)
      * [Container Design Patterns](https://kubernetes.io/blog/2016/06/container-design-patterns/)
      * [The Illustrated Children's Guide to Kubernetes](https://kubernetes.io/blog/2016/06/illustrated-childrens-guide-to-kubernetes/)
      * [Bringing End-to-End Kubernetes Testing to Azure (Part 1)](https://kubernetes.io/blog/2016/06/bringing-end-to-end-testing-to-azure/)
      * [Hypernetes: Bringing Security and Multi-tenancy to Kubernetes](https://kubernetes.io/blog/2016/05/hypernetes-security-and-multi-tenancy-in-kubernetes/)
      * [CoreOS Fest 2016: CoreOS and Kubernetes Community meet in Berlin (& San Francisco)](https://kubernetes.io/blog/2016/05/coreosfest2016-kubernetes-community/)
      * [Introducing the Kubernetes OpenStack Special Interest Group](https://kubernetes.io/blog/2016/04/introducing-kubernetes-openstack-sig/)
      * [SIG-UI: the place for building awesome user interfaces for Kubernetes](https://kubernetes.io/blog/2016/04/building-awesome-user-interfaces-for-kubernetes/)
      * [SIG-ClusterOps: Promote operability and interoperability of Kubernetes clusters](https://kubernetes.io/blog/2016/04/sig-clusterops-promote-operability-and-interoperability-of-k8s-clusters/)
      * [SIG-Networking: Kubernetes Network Policy APIs Coming in 1.3](https://kubernetes.io/blog/2016/04/kubernetes-network-policy-apis/)
      * [How to deploy secure, auditable, and reproducible Kubernetes clusters on AWS](https://kubernetes.io/blog/2016/04/kubernetes-on-aws_15/)
      * [Container survey results - March 2016](https://kubernetes.io/blog/2016/04/container-survey-results-march-2016/)
      * [Adding Support for Kubernetes in Rancher](https://kubernetes.io/blog/2016/04/adding-support-for-kubernetes-in-rancher/)
      * [Configuration management with Containers](https://kubernetes.io/blog/2016/04/configuration-management-with-containers/)
      * [Using Deployment objects with Kubernetes 1.2](https://kubernetes.io/blog/2016/04/using-deployment-objects-with/)
      * [Kubernetes 1.2 and simplifying advanced networking with Ingress](https://kubernetes.io/blog/2016/03/kubernetes-1-2-and-simplifying-advanced-networking-with-ingress/)
      * [Using Spark and Zeppelin to process big data on Kubernetes 1.2](https://kubernetes.io/blog/2016/03/using-spark-and-zeppelin-to-process-big-data-on-kubernetes/)
      * [Building highly available applications using Kubernetes new multi-zone clusters (a.k.a. 'Ubernetes Lite')](https://kubernetes.io/blog/2016/03/building-highly-available-applications-using-kubernetes-new-multi-zone-clusters-aka-ubernetes-lite/)
      * [AppFormix: Helping Enterprises Operationalize Kubernetes](https://kubernetes.io/blog/2016/03/appformix-helping-enterprises/)
      * [How container metadata changes your point of view](https://kubernetes.io/blog/2016/03/how-container-metadata-changes-your-point-of-view/)
      * [Five Days of Kubernetes 1.2](https://kubernetes.io/blog/2016/03/five-days-of-kubernetes-12/)
      * [1000 nodes and beyond: updates to Kubernetes performance and scalability in 1.2](https://kubernetes.io/blog/2016/03/1000-nodes-and-beyond-updates-to-kubernetes-performance-and-scalability-in-12/)
      * [Scaling neural network image classification using Kubernetes with TensorFlow Serving](https://kubernetes.io/blog/2016/03/scaling-neural-network-image-classification-using-kubernetes-with-tensorflow-serving/)
      * [Kubernetes 1.2: Even more performance upgrades, plus easier application deployment and management](https://kubernetes.io/blog/2016/03/kubernetes-1-2-even-more-performance-upgrades-plus-easier-application-deployment-and-management/)
      * [Kubernetes in the Enterprise with Fujitsu’s Cloud Load Control](https://kubernetes.io/blog/2016/03/kubernetes-in-enterprise-with-fujitsus/)
      * [ElasticBox introduces ElasticKube to help manage Kubernetes within the enterprise](https://kubernetes.io/blog/2016/03/elasticbox-introduces-elastickube-to/)
      * [State of the Container World, February 2016](https://kubernetes.io/blog/2016/03/state-of-container-world-february-2016/)
      * [Kubernetes Community Meeting Notes - 20160225](https://kubernetes.io/blog/2016/03/kubernetes-community-meeting-notes/)
      * [KubeCon EU 2016: Kubernetes Community in London](https://kubernetes.io/blog/2016/02/kubecon-eu-2016-kubernetes-community-in/)
      * [Kubernetes Community Meeting Notes - 20160218](https://kubernetes.io/blog/2016/02/kubernetes-community-meeting-notes_23/)
      * [Kubernetes Community Meeting Notes - 20160211](https://kubernetes.io/blog/2016/02/kubernetes-community-meeting-notes-20160211/)
      * [ShareThis: Kubernetes In Production](https://kubernetes.io/blog/2016/02/sharethis-kubernetes-in-production/)
      * [Kubernetes Community Meeting Notes - 20160204](https://kubernetes.io/blog/2016/02/kubernetes-community-meeting-notes/)
      * [Kubernetes Community Meeting Notes - 20160128](https://kubernetes.io/blog/2016/02/kubernetes-community-meeting-notes-20160128/)
      * [State of the Container World, January 2016](https://kubernetes.io/blog/2016/02/state-of-container-world-january-2016/)
      * [Kubernetes Community Meeting Notes - 20160121](https://kubernetes.io/blog/2016/01/kubernetes-community-meeting-notes_28/)
      * [Kubernetes Community Meeting Notes - 20160114](https://kubernetes.io/blog/2016/01/Kubernetes-Community-Meeting-Notes/)
      * [Why Kubernetes doesn’t use libnetwork](https://kubernetes.io/blog/2016/01/why-kubernetes-doesnt-use-libnetwork/)
      * [Simple leader election with Kubernetes and Docker](https://kubernetes.io/blog/2016/01/simple-leader-election-with-kubernetes/)
    * 2015
      * [Creating a Raspberry Pi cluster running Kubernetes, the installation (Part 2)](https://kubernetes.io/blog/2015/12/creating-raspberry-pi-cluster-running/)
      * [Managing Kubernetes Pods, Services and Replication Controllers with Puppet](https://kubernetes.io/blog/2015/12/managing-kubernetes-pods-services-and-replication-controllers-with-puppet/)
      * [How Weave built a multi-deployment solution for Scope using Kubernetes](https://kubernetes.io/blog/2015/12/how-weave-built-a-multi-deployment-solution-for-scope-using-kubernetes/)
      * [Creating a Raspberry Pi cluster running Kubernetes, the shopping list (Part 1)](https://kubernetes.io/blog/2015/11/creating-a-raspberry-pi-cluster-running-kubernetes-the-shopping-list-part-1/)
      * [Monitoring Kubernetes with Sysdig](https://kubernetes.io/blog/2015/11/monitoring-kubernetes-with-sysdig/)
      * [One million requests per second: Dependable and dynamic distributed systems at scale](https://kubernetes.io/blog/2015/11/one-million-requests-per-second-dependable-and-dynamic-distributed-systems-at-scale/)
      * [Kubernetes 1.1 Performance upgrades, improved tooling and a growing community](https://kubernetes.io/blog/2015/11/kubernetes-1-1-performance-upgrades-improved-tooling-and-a-growing-community/)
      * [Kubernetes as Foundation for Cloud Native PaaS](https://kubernetes.io/blog/2015/11/kubernetes-as-foundation-for-cloud-native-paas/)
      * [Some things you didn’t know about kubectl](https://kubernetes.io/blog/2015/10/some-things-you-didnt-know-about-kubectl_28/)
      * [Kubernetes Performance Measurements and Roadmap](https://kubernetes.io/blog/2015/09/kubernetes-performance-measurements-and/)
      * [Using Kubernetes Namespaces to Manage Environments](https://kubernetes.io/blog/2015/08/using-kubernetes-namespaces-to-manage/)
      * [Weekly Kubernetes Community Hangout Notes - July 31 2015](https://kubernetes.io/blog/2015/08/Weekly-Kubernetes-Community-Hangout/)
      * [The Growing Kubernetes Ecosystem](https://kubernetes.io/blog/2015/07/the-growing-kubernetes-ecosystem/)
      * [Weekly Kubernetes Community Hangout Notes - July 17 2015](https://kubernetes.io/blog/2015/07/weekly-kubernetes-community-hangout_23/)
      * [Strong, Simple SSL for Kubernetes Services](https://kubernetes.io/blog/2015/07/strong-simple-ssl-for-kubernetes/)
      * [Weekly Kubernetes Community Hangout Notes - July 10 2015](https://kubernetes.io/blog/2015/07/Weekly-Kubernetes-Community-Hangout/)
      * [Announcing the First Kubernetes Enterprise Training Course](https://kubernetes.io/blog/2015/07/announcing-first-kubernetes-enterprise/)
      * [Kubernetes 1.0 Launch Event at OSCON](https://kubernetes.io/blog/2015/07/kubernetes-10-launch-party-at-oscon/)
      * [How did the Quake demo from DockerCon Work?](https://kubernetes.io/blog/2015/07/how-did-quake-demo-from-dockercon-work/)
      * [The Distributed System ToolKit: Patterns for Composite Containers](https://kubernetes.io/blog/2015/06/the-distributed-system-toolkit-patterns/)
      * [Slides: Cluster Management with Kubernetes, talk given at the University of Edinburgh](https://kubernetes.io/blog/2015/06/slides-cluster-management-with/)
      * [Cluster Level Logging with Kubernetes](https://kubernetes.io/blog/2015/06/cluster-level-logging-with-kubernetes/)
      * [Weekly Kubernetes Community Hangout Notes - May 22 2015](https://kubernetes.io/blog/2015/06/Weekly-Kubernetes-Community-Hangout/)
      * [Kubernetes on OpenStack](https://kubernetes.io/blog/2015/05/kubernetes-on-openstack/)
      * [Weekly Kubernetes Community Hangout Notes - May 15 2015](https://kubernetes.io/blog/2015/05/weekly-kubernetes-community-hangout_18/)
      * [Docker and Kubernetes and AppC](https://kubernetes.io/blog/2015/05/docker-and-kubernetes-and-appc/)
      * [Kubernetes Release: 0.17.0](https://kubernetes.io/blog/2015/05/kubernetes-release-0170/)
      * [Resource Usage Monitoring in Kubernetes](https://kubernetes.io/blog/2015/05/resource-usage-monitoring-kubernetes/)
      * [Kubernetes Release: 0.16.0](https://kubernetes.io/blog/2015/05/kubernetes-release-0160/)
      * [Weekly Kubernetes Community Hangout Notes - May 1 2015](https://kubernetes.io/blog/2015/05/Weekly-Kubernetes-Community-Hangout/)
      * [AppC Support for Kubernetes through RKT](https://kubernetes.io/blog/2015/05/appc-support-for-kubernetes-through-rkt/)
      * [Weekly Kubernetes Community Hangout Notes - April 24 2015](https://kubernetes.io/blog/2015/04/weekly-kubernetes-community-hangout_29/)
      * [Borg: The Predecessor to Kubernetes](https://kubernetes.io/blog/2015/04/borg-predecessor-to-kubernetes/)
      * [Kubernetes and the Mesosphere DCOS](https://kubernetes.io/blog/2015/04/kubernetes-and-mesosphere-dcos/)
      * [Weekly Kubernetes Community Hangout Notes - April 17 2015](https://kubernetes.io/blog/2015/04/weekly-kubernetes-community-hangout_17/)
      * [Kubernetes Release: 0.15.0](https://kubernetes.io/blog/2015/04/kubernetes-release-0150/)
      * [Introducing Kubernetes API Version v1beta3](https://kubernetes.io/blog/2015/04/introducing-kubernetes-v1beta3/)
      * [Weekly Kubernetes Community Hangout Notes - April 10 2015](https://kubernetes.io/blog/2015/04/weekly-kubernetes-community-hangout_11/)
      * [Faster than a speeding Latte](https://kubernetes.io/blog/2015/04/faster-than-speeding-latte/)
      * [Weekly Kubernetes Community Hangout Notes - April 3 2015](https://kubernetes.io/blog/2015/04/Weekly-Kubernetes-Community-Hangout/)
      * [Participate in a Kubernetes User Experience Study](https://kubernetes.io/blog/2015/03/participate-in-kubernetes-user/)
      * [Weekly Kubernetes Community Hangout Notes - March 27 2015](https://kubernetes.io/blog/2015/03/Weekly-Kubernetes-Community-Hangout/)
      * [Kubernetes Gathering Videos](https://kubernetes.io/blog/2015/03/kubernetes-gathering-videos/)
      * [Welcome to the Kubernetes Blog!](https://kubernetes.io/blog/2015/03/welcome-to-kubernetes-blog/)



This article is more than one year old. Older articles may contain outdated content. Check that the information in the page has not become incorrect since its publication.

# Advanced Scheduling in Kubernetes

By **Ian Lewis (Google), David Oppenheimer (Google)** | Friday, March 31, 2017

 _Editor’s note: this post is part of a[series of in-depth articles](https://kubernetes.io/blog/2017/03/five-days-of-kubernetes-1-6) on what's new in Kubernetes 1.6_

The Kubernetes scheduler’s default behavior works well for most cases -- for example, it ensures that pods are only placed on nodes that have sufficient free resources, it ties to spread pods from the same set ([ReplicaSet](https://kubernetes.io/docs/user-guide/replicasets/), [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/), etc.) across nodes, it tries to balance out the resource utilization of nodes, etc.

But sometimes you want to control how your pods are scheduled. For example, perhaps you want to ensure that certain pods only schedule on nodes with specialized hardware, or you want to co-locate services that communicate frequently, or you want to dedicate a set of nodes to a particular set of users. Ultimately, you know much more about how your applications should be scheduled and deployed than Kubernetes ever will. So **[Kubernetes 1.6](https://kubernetes.io/blog/2017/03/kubernetes-1-6-multi-user-multi-workloads-at-scale) offers four advanced scheduling features: node affinity/anti-affinity, taints and tolerations, pod affinity/anti-affinity, and custom schedulers**. Each of these features are now in _beta_ in Kubernetes 1.6.

**Node Affinity/Anti-Affinity**

[Node Affinity/Anti-Affinity](https://kubernetes.io/docs/user-guide/node-selection/#node-affinity-beta-feature) is one way to set rules on which nodes are selected by the scheduler. This feature is a generalization of the [nodeSelector](https://kubernetes.io/docs/user-guide/node-selection/#nodeselector) feature which has been in Kubernetes since version 1.0. The rules are defined using the familiar concepts of custom labels on nodes and selectors specified in pods, and they can be either required or preferred, depending on how strictly you want the scheduler to enforce them.

Required rules must be met for a pod to schedule on a particular node. If no node matches the criteria (plus all of the other normal criteria, such as having enough free resources for the pod’s resource request), then the pod won’t be scheduled. Required rules are specified in the requiredDuringSchedulingIgnoredDuringExecution field of nodeAffinity.

For example, if we want to require scheduling on a node that is in the us-central1-a GCE zone of a multi-zone Kubernetes cluster, we can specify the following affinity rule as part of the Pod spec:
    
    
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
              - matchExpressions:
                - key: "failure-domain.beta.kubernetes.io/zone"
                  operator: In
                  values: ["us-central1-a"]
    

“IgnoredDuringExecution” means that the pod will still run if labels on a node change and affinity rules are no longer met. There are future plans to offer requiredDuringSchedulingRequiredDuringExecution which will evict pods from nodes as soon as they don’t satisfy the node affinity rule(s).

Preferred rules mean that if nodes match the rules, they will be chosen first, and only if no preferred nodes are available will non-preferred nodes be chosen. You can prefer instead of require that pods are deployed to us-central1-a by slightly changing the pod spec to use preferredDuringSchedulingIgnoredDuringExecution:
    
    
      affinity:
        nodeAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
              - matchExpressions:
                - key: "failure-domain.beta.kubernetes.io/zone"
                  operator: In
                  values: ["us-central1-a"]
    

Node anti-affinity can be achieved by using negative operators. So for instance if we want our pods to avoid us-central1-a we can do this:
    
    
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
              - matchExpressions:
                - key: "failure-domain.beta.kubernetes.io/zone"
                  operator: NotIn
                  values: ["us-central1-a"]
    

Valid operators you can use are In, NotIn, Exists, DoesNotExist. Gt, and Lt.

Additional use cases for this feature are to restrict scheduling based on nodes’ hardware architecture, operating system version, or specialized hardware. Node affinity/anti-affinity is _beta_ in Kubernetes 1.6.

**Taints and Tolerations**

A related feature is “[taints and tolerations](https://kubernetes.io/docs/user-guide/node-selection/#taints-and-toleations-beta-feature),” which allows you to mark (“taint”) a node so that no pods can schedule onto it unless a pod explicitly “tolerates” the taint. Marking nodes instead of pods (as in node affinity/anti-affinity) is particularly useful for situations where most pods in the cluster should avoid scheduling onto the node. For example, you might want to mark your master node as schedulable only by Kubernetes system components, or dedicate a set of nodes to a particular group of users, or keep regular pods away from nodes that have special hardware so as to leave room for pods that need the special hardware.

The kubectl command allows you to set taints on nodes, for example:
    
    
    kubectl taint nodes node1 key=value:NoSchedule
    

creates a taint that marks the node as unschedulable by any pods that do not have a toleration for taint with key key, value value, and effect NoSchedule. (The other taint effects are PreferNoSchedule, which is the preferred version of NoSchedule, and NoExecute, which means any pods that are running on the node when the taint is applied will be evicted unless they tolerate the taint.) The toleration you would add to a PodSpec to have the corresponding pod tolerate this taint would look like this
    
    
      tolerations:
      - key: "key"
        operator: "Equal"
        value: "value"
        effect: "NoSchedule"
    

In addition to moving taints and tolerations to _beta_ in Kubernetes 1.6, we have introduced an _alpha_ feature that uses taints and tolerations to allow you to customize how long a pod stays bound to a node when the node experiences a problem like a network partition instead of using the default five minutes. See [this section](https://kubernetes.io/docs/user-guide/node-selection/#per-pod-configurable-eviction-behavior-when-there-are-node-problems-alpha-feature) of the documentation for more details.

**Pod Affinity/Anti-Affinity**

Node affinity/anti-affinity allows you to constrain which nodes a pod can run on based on the nodes’ labels. But what if you want to specify rules about how pods should be placed relative to one another, for example to spread or pack pods within a service or relative to pods in other services? For that you can use [pod affinity/anti-affinity](https://kubernetes.io/docs/user-guide/node-selection/#inter-pod-affinity-and-anti-affinity-beta-feature), which is also _beta_ in Kubernetes 1.6.

Let’s look at an example. Say you have front-ends in service S1, and they communicate frequently with back-ends that are in service S2 (a “north-south” communication pattern). So you want these two services to be co-located in the same cloud provider zone, but you don’t want to have to choose the zone manually--if the zone fails, you want the pods to be rescheduled to another (single) zone. You can specify this with a pod affinity rule that looks like this (assuming you give the pods of this service a label “service=S2” and the pods of the other service a label “service=S1”):
    
    
    affinity:
        podAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
              matchExpressions:
              - key: service
                operator: In
                values: [“S1”]
            topologyKey: failure-domain.beta.kubernetes.io/zone
    

As with node affinity/anti-affinity, there is also a preferredDuringSchedulingIgnoredDuringExecution variant.

Pod affinity/anti-affinity is very flexible. Imagine you have profiled the performance of your services and found that containers from service S1 interfere with containers from service S2 when they share the same node, perhaps due to cache interference effects or saturating the network link. Or maybe due to security concerns you never want containers of S1 and S2 to share a node. To implement these rules, just make two changes to the snippet above -- change podAffinity to podAntiAffinity and change topologyKey to kubernetes.io/hostname.

**Custom Schedulers**

If the Kubernetes scheduler’s various features don’t give you enough control over the scheduling of your workloads, you can delegate responsibility for scheduling arbitrary subsets of pods to your own custom scheduler(s) that run(s) alongside, or instead of, the default Kubernetes scheduler. [Multiple schedulers](https://kubernetes.io/docs/admin/multiple-schedulers/) is _beta_ in Kubernetes 1.6.

Each new pod is normally scheduled by the default scheduler. But if you provide the name of your own custom scheduler, the default scheduler will ignore that Pod and allow your scheduler to schedule the Pod to a node. Let’s look at an example.

Here we have a Pod where we specify the schedulerName field:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx
      labels:
        app: nginx
    spec:
      schedulerName: my-scheduler
      containers:
      - name: nginx
        image: nginx:1.10
    

If we create this Pod without deploying a custom scheduler, the default scheduler will ignore it and it will remain in a Pending state. So we need a custom scheduler that looks for, and schedules, pods whose schedulerName field is my-scheduler.

A custom scheduler can be written in any language and can be as simple or complex as you need. Here is a very simple example of a custom scheduler written in Bash that assigns a node randomly. Note that you need to run this along with kubectl proxy for it to work.
    
    
    #!/bin/bash
    
    SERVER='localhost:8001'
    
    while true;
    
    do
    
        for PODNAME in $(kubectl --server $SERVER get pods -o json | jq '.items[] | select(.spec.schedulerName == "my-scheduler") | select(.spec.nodeName == null) | .metadata.name' | tr -d '"')
    
    ;
    
        do
    
            NODES=($(kubectl --server $SERVER get nodes -o json | jq '.items[].metadata.name' | tr -d '"'))
    
    
            NUMNODES=${#NODES[@]}
    
            CHOSEN=${NODES[$[$RANDOM % $NUMNODES]]}
    
            curl --header "Content-Type:application/json" --request POST --data '{"apiVersion":"v1", "kind": "Binding", "metadata": {"name": "'$PODNAME'"}, "target": {"apiVersion": "v1", "kind"
    
    : "Node", "name": "'$CHOSEN'"}}' http://$SERVER/api/v1/namespaces/default/pods/$PODNAME/binding/
    
            echo "Assigned $PODNAME to $CHOSEN"
    
        done
    
        sleep 1
    
    done
    

**Learn more**

The Kubernetes 1.6 [release notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md#v160) have more information about these features, including details about how to change your configurations if you are already using the alpha version of one or more of these features (this is required, as the move from alpha to beta is a breaking change for these features).

**Acknowledgements**

The features described here, both in their alpha and beta forms, were a true community effort, involving engineers from Google, Huawei, IBM, Red Hat and more.

**Get Involved**

Share your voice at our weekly [community meeting](https://github.com/kubernetes/community/blob/master/communication.md#weekly-meeting):

  * Post questions (or answer questions) on [Stack Overflow](http://stackoverflow.com/questions/tagged/kubernetes)
  * Follow us on Twitter [@Kubernetesio](https://twitter.com/kubernetesio) for latest updates
  * Connect with the community on [Slack](http://slack.k8s.io/) (room #sig-scheduling)



Many thanks for your contributions.

  * [←Previous](https://kubernetes.io/blog/2017/03/scalability-updates-in-kubernetes-1-6/)
  * [Next→](https://kubernetes.io/blog/2017/04/configuring-private-dns-zones-upstream-nameservers-kubernetes/)



Last modified January 03, 2026 at 2:39 PM PST: [Reorganize 2017 blog content (4ccfc3cc8a)](https://github.com/kubernetes/website/commit/4ccfc3cc8af28b9da189db878cd6f8883c479e37)

[__RSS Feed](https://kubernetes.io/feed.xml)[ __ Submit a Post](https://kubernetes.io/docs/contribute/new-content/blogs-case-studies/)[ __@kubernetes.io](https://bsky.app/profile/kubernetes.io)[ __@Kubernetesio](https://x.com/kubernetesio)[ __ on GitHub](https://github.com/kubernetes/kubernetes)[ __#kubernetes-users](http://slack.k8s.io)[ __ Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes)[ __Forum](https://discuss.kubernetes.io)[ __ Kubernetes](https://kubernetes.io/docs/setup)

  * [ __](https://youtube.com/kubernetescommunity)
  * [__](https://discuss.kubernetes.io)
  * [__](https://serverfault.com/questions/tagged/kubernetes)
  * [__](https://www.linkedin.com/company/kubernetes/)
  * [__](https://bsky.app/profile/kubernetes.io)
  * [__](https://x.com/kubernetesio)



(C) 2026 The Kubernetes Authors | Documentation Distributed under [CC BY 4.0](https://git.k8s.io/website/LICENSE)

(C) 2026 The Linux Foundation ®. All rights reserved. The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage page](https://www.linuxfoundation.org/trademark-usage)

ICP license: 京ICP备17074266号-3

  * [ __](https://k8s.dev/)
  * [__](https://github.com/kubernetes/kubernetes)
  * [__](https://slack.k8s.io)
  * [__](https://calendar.google.com/calendar/embed?src=calendar%40kubernetes.io)



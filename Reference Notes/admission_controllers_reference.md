---
domains:
  - "kubernetes"
  - "security"
---

# Admission Controllers Reference

**Source:** https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/

---

Title: Live Content Description: Fetched live Source: https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/ \--- [Kubernetes](https://kubernetes.io/)

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
    * [中文 (Chinese)](https://kubernetes.io/zh-cn/docs/reference/access-authn-authz/admission-controllers/)
    * বাংলা (Bengali) [__](https://kubernetes.io/bn/)
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

# Admission Control in Kubernetes

English

  * [বাংলা (Bengali)](https://kubernetes.io/bn/docs/concepts/)
  * [中文 (Chinese)](https://kubernetes.io/zh-cn/docs/concepts/)
  * [Français (French)](https://kubernetes.io/fr/docs/concepts/)
  * [Deutsch (German)](https://kubernetes.io/de/docs/concepts/)
  * [हिन्दी (Hindi)](https://kubernetes.io/hi/docs/concepts/)
  * [Bahasa Indonesia (Indonesian)](https://kubernetes.io/id/docs/concepts/)
  * [Italiano (Italian)](https://kubernetes.io/it/docs/concepts/)
  * [日本語 (Japanese)](https://kubernetes.io/ja/docs/concepts/)
  * [한국어 (Korean)](https://kubernetes.io/ko/docs/concepts/)
  * [Polski (Polish)](https://kubernetes.io/pl/docs/concepts/)
  * [Português (Portuguese)](https://kubernetes.io/pt-br/docs/concepts/)
  * [Русский (Russian)](https://kubernetes.io/ru/docs/concepts/)
  * [Español (Spanish)](https://kubernetes.io/es/docs/concepts/)
  * [Українська (Ukrainian)](https://kubernetes.io/uk/docs/concepts/)
  * [Tiếng Việt (Vietnamese)](https://kubernetes.io/vi/docs/concepts/)
  * فارسی (Persian) [__](https://kubernetes.io/fa/)



  * [Kubernetes Documentation](https://kubernetes.io/docs/ "Documentation")
    * [Documentation](https://kubernetes.io/docs/home/ "Kubernetes Documentation")
      * [Available Documentation Versions](https://kubernetes.io/docs/home/supported-doc-versions/)
    * [Getting started](https://kubernetes.io/docs/setup/)
      * [Learning environment](https://kubernetes.io/docs/setup/learning-environment/)
      * [Production environment](https://kubernetes.io/docs/setup/production-environment/)
        * [Container Runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)
        * [Installing Kubernetes with deployment tools](https://kubernetes.io/docs/setup/production-environment/tools/)
          * [Bootstrapping clusters with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/)
            * [Installing kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
            * [Troubleshooting kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/)
            * [Creating a cluster with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)
            * [Customizing components with the kubeadm API](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/control-plane-flags/)
            * [Options for Highly Available Topology](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/ha-topology/)
            * [Creating Highly Available Clusters with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/)
            * [Set up a High Availability etcd Cluster with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/setup-ha-etcd-with-kubeadm/)
            * [Configuring each kubelet in your cluster using kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/kubelet-integration/)
            * [Dual-stack support with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/dual-stack-support/)
        * [Turnkey Cloud Solutions](https://kubernetes.io/docs/setup/production-environment/turnkey-solutions/)
      * [Best practices](https://kubernetes.io/docs/setup/best-practices/)
        * [Considerations for large clusters](https://kubernetes.io/docs/setup/best-practices/cluster-large/)
        * [Running in multiple zones](https://kubernetes.io/docs/setup/best-practices/multiple-zones/)
        * [Validate node setup](https://kubernetes.io/docs/setup/best-practices/node-conformance/)
        * [Enforcing Pod Security Standards](https://kubernetes.io/docs/setup/best-practices/enforcing-pod-security-standards/)
        * [PKI certificates and requirements](https://kubernetes.io/docs/setup/best-practices/certificates/)
    * [Concepts](https://kubernetes.io/docs/concepts/)
      * [Overview](https://kubernetes.io/docs/concepts/overview/)
        * [Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/)
        * [Objects In Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/)
          * [Kubernetes Object Management](https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/)
          * [Object Names and IDs](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/)
          * [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)
          * [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)
          * [Annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)
          * [Field Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/)
          * [Finalizers](https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/)
          * [Owners and Dependents](https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/)
          * [Recommended Labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/)
          * [Storage Versions](https://kubernetes.io/docs/concepts/overview/working-with-objects/storage-version/)
        * [The Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/)
        * [The kubectl command-line tool](https://kubernetes.io/docs/concepts/overview/kubectl/)
      * [Cluster Architecture](https://kubernetes.io/docs/concepts/architecture/)
        * [Nodes](https://kubernetes.io/docs/concepts/architecture/nodes/)
        * [Communication between Nodes and the Control Plane](https://kubernetes.io/docs/concepts/architecture/control-plane-node-communication/)
        * [Controllers](https://kubernetes.io/docs/concepts/architecture/controller/)
        * [Leases](https://kubernetes.io/docs/concepts/architecture/leases/)
        * [Cloud Controller Manager](https://kubernetes.io/docs/concepts/architecture/cloud-controller/)
        * [About cgroup v2](https://kubernetes.io/docs/concepts/architecture/cgroups/)
        * [Kubernetes Self-Healing](https://kubernetes.io/docs/concepts/architecture/self-healing/)
        * [Garbage Collection](https://kubernetes.io/docs/concepts/architecture/garbage-collection/)
        * [Mixed Version Proxy](https://kubernetes.io/docs/concepts/architecture/mixed-version-proxy/)
      * [Containers](https://kubernetes.io/docs/concepts/containers/)
        * [Images](https://kubernetes.io/docs/concepts/containers/images/)
        * [Container Environment](https://kubernetes.io/docs/concepts/containers/container-environment/)
        * [Runtime Class](https://kubernetes.io/docs/concepts/containers/runtime-class/)
        * [Container Lifecycle Hooks](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/)
        * [Container Runtime Interface (CRI)](https://kubernetes.io/docs/concepts/containers/cri/)
      * [Workloads](https://kubernetes.io/docs/concepts/workloads/)
        * [Pods](https://kubernetes.io/docs/concepts/workloads/pods/)
          * [Pod Lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)
          * [Pod Conditions](https://kubernetes.io/docs/concepts/workloads/pods/pod-condition/)
          * [Init Containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/)
          * [Sidecar Containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/)
          * [Ephemeral Containers](https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/)
          * [Liveness, Readiness, and Startup Probes](https://kubernetes.io/docs/concepts/workloads/pods/probes/)
          * [Disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/)
          * [Pod Hostname](https://kubernetes.io/docs/concepts/workloads/pods/pod-hostname/)
          * [Pod Quality of Service Classes](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/)
          * [Scheduling Group](https://kubernetes.io/docs/concepts/workloads/pods/scheduling-group/)
          * [Static Pods](https://kubernetes.io/docs/concepts/workloads/pods/static-pods/)
          * [User Namespaces](https://kubernetes.io/docs/concepts/workloads/pods/user-namespaces/)
          * [Downward API](https://kubernetes.io/docs/concepts/workloads/pods/downward-api/)
          * [Advanced Pod Configuration](https://kubernetes.io/docs/concepts/workloads/pods/advanced-pod-config/)
        * [Workload API](https://kubernetes.io/docs/concepts/workloads/workload-api/)
          * [Pod Group Disruption and Priority](https://kubernetes.io/docs/concepts/workloads/workload-api/disruption-and-priority/)
          * [PodGroup Scheduling Policies](https://kubernetes.io/docs/concepts/workloads/workload-api/policies/)
          * [Topology-Aware Workload Scheduling](https://kubernetes.io/docs/concepts/workloads/workload-api/topology-aware-scheduling/)
        * [Workload Management](https://kubernetes.io/docs/concepts/workloads/controllers/)
          * [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
          * [ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)
          * [StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
          * [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)
          * [Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/)
          * [Automatic Cleanup for Finished Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/ttlafterfinished/)
          * [CronJob](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/)
          * [ReplicationController](https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/)
        * [PodGroup API](https://kubernetes.io/docs/concepts/workloads/podgroup-api/)
          * [PodGroup Lifecycle](https://kubernetes.io/docs/concepts/workloads/podgroup-api/lifecycle/)
        * [Managing Workloads](https://kubernetes.io/docs/concepts/workloads/management/)
        * [Autoscaling Workloads](https://kubernetes.io/docs/concepts/workloads/autoscaling/)
        * [Horizontal Pod Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)
        * [Resource managers](https://kubernetes.io/docs/concepts/workloads/resource-managers/)
        * [Vertical Pod Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/)
      * [Services, Load Balancing, and Networking](https://kubernetes.io/docs/concepts/services-networking/)
        * [Service](https://kubernetes.io/docs/concepts/services-networking/service/)
        * [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
        * [Ingress Controllers](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/)
        * [Gateway API](https://kubernetes.io/docs/concepts/services-networking/gateway/)
        * [EndpointSlices](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/)
        * [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
        * [DNS for Services and Pods](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)
        * [IPv4/IPv6 dual-stack](https://kubernetes.io/docs/concepts/services-networking/dual-stack/)
        * [Topology Aware Routing](https://kubernetes.io/docs/concepts/services-networking/topology-aware-routing/)
        * [Networking on Windows](https://kubernetes.io/docs/concepts/services-networking/windows-networking/)
        * [Service ClusterIP allocation](https://kubernetes.io/docs/concepts/services-networking/cluster-ip-allocation/)
        * [Service Internal Traffic Policy](https://kubernetes.io/docs/concepts/services-networking/service-traffic-policy/)
      * [Storage](https://kubernetes.io/docs/concepts/storage/)
        * [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/)
        * [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
        * [Projected Volumes](https://kubernetes.io/docs/concepts/storage/projected-volumes/)
        * [Ephemeral Volumes](https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/)
        * [Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes/)
        * [Volume Attributes Classes](https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/)
        * [Dynamic Volume Provisioning](https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/)
        * [Volume Snapshots](https://kubernetes.io/docs/concepts/storage/volume-snapshots/)
        * [Volume Snapshot Classes](https://kubernetes.io/docs/concepts/storage/volume-snapshot-classes/)
        * [CSI Volume Cloning](https://kubernetes.io/docs/concepts/storage/volume-pvc-datasource/)
        * [Storage Capacity](https://kubernetes.io/docs/concepts/storage/storage-capacity/)
        * [Node-specific Volume Limits](https://kubernetes.io/docs/concepts/storage/storage-limits/)
        * [Local ephemeral storage](https://kubernetes.io/docs/concepts/storage/ephemeral-storage/)
        * [Volume Health Monitoring](https://kubernetes.io/docs/concepts/storage/volume-health-monitoring/)
        * [Windows Storage](https://kubernetes.io/docs/concepts/storage/windows-storage/)
      * [Configuration](https://kubernetes.io/docs/concepts/configuration/)
        * [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)
        * [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
        * [Resource Management for Pods and Containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
        * [Organizing Cluster Access Using kubeconfig Files](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/)
        * [Resource Management for Windows nodes](https://kubernetes.io/docs/concepts/configuration/windows-resource-management/)
      * [Security](https://kubernetes.io/docs/concepts/security/)
        * [Cloud Native Security](https://kubernetes.io/docs/concepts/security/cloud-native-security/ "Cloud Native Security and Kubernetes")
        * [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)
        * [Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/)
        * [Service Accounts](https://kubernetes.io/docs/concepts/security/service-accounts/)
        * [Pod Security Policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/)
        * [Security For Linux Nodes](https://kubernetes.io/docs/concepts/security/linux-security/)
        * [Security For Windows Nodes](https://kubernetes.io/docs/concepts/security/windows-security/)
        * [Controlling Access to the Kubernetes API](https://kubernetes.io/docs/concepts/security/controlling-access/)
        * [Role Based Access Control Good Practices](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)
        * [Good practices for Kubernetes Secrets](https://kubernetes.io/docs/concepts/security/secrets-good-practices/)
        * [Multi-tenancy](https://kubernetes.io/docs/concepts/security/multi-tenancy/)
        * [Hardening Guide - Authentication Mechanisms](https://kubernetes.io/docs/concepts/security/hardening-guide/authentication-mechanisms/)
        * [Hardening Guide - Dynamic Resource Allocation](https://kubernetes.io/docs/concepts/security/hardening-guide/dynamic-resource-allocation/)
        * [Hardening Guide - Scheduler Configuration](https://kubernetes.io/docs/concepts/security/hardening-guide/scheduler/)
        * [Kubernetes API Server Bypass Risks](https://kubernetes.io/docs/concepts/security/api-server-bypass-risks/)
        * [Linux kernel security constraints for Pods and containers](https://kubernetes.io/docs/concepts/security/linux-kernel-security-constraints/)
        * [Security Checklist](https://kubernetes.io/docs/concepts/security/security-checklist/)
        * [Application Security Checklist](https://kubernetes.io/docs/concepts/security/application-security-checklist/)
      * [Policies](https://kubernetes.io/docs/concepts/policy/)
        * [Limit Ranges](https://kubernetes.io/docs/concepts/policy/limit-range/)
        * [Resource Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/)
        * [Process ID Limits And Reservations](https://kubernetes.io/docs/concepts/policy/pid-limiting/)
      * [Scheduling, Preemption and Eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/)
        * [Kubernetes Scheduler](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/)
        * [Topology-Aware Workload Scheduling](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-aware-scheduling/)
        * [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
        * [Pod Overhead](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-overhead/)
        * [Pod Scheduling Readiness](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-scheduling-readiness/)
        * [Pod Topology Spread Constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/)
        * [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)
        * [Scheduling Framework](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/)
        * [Dynamic Resource Allocation](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/)
        * [Gang Scheduling](https://kubernetes.io/docs/concepts/scheduling-eviction/gang-scheduling/)
        * [Scheduler Performance Tuning](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduler-perf-tuning/)
        * [PodGroup Scheduling](https://kubernetes.io/docs/concepts/scheduling-eviction/podgroup-scheduling/)
        * [Resource Bin Packing](https://kubernetes.io/docs/concepts/scheduling-eviction/resource-bin-packing/)
        * [Workload-Aware Preemption](https://kubernetes.io/docs/concepts/scheduling-eviction/workload-aware-preemption/)
        * [Pod Priority and Preemption](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/)
        * [Node-pressure Eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/)
        * [API-initiated Eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/api-eviction/)
        * [Node Declared Features](https://kubernetes.io/docs/concepts/scheduling-eviction/node-declared-features/)
      * [Cluster Administration](https://kubernetes.io/docs/concepts/cluster-administration/)
        * [Node Shutdowns](https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/)
        * [Swap memory management](https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/)
        * [Node Autoscaling](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/)
        * [Certificates](https://kubernetes.io/docs/concepts/cluster-administration/certificates/)
        * [Cluster Networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/)
        * [Observability](https://kubernetes.io/docs/concepts/cluster-administration/observability/)
        * [Admission Webhook Good Practices](https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/)
        * [Good practices for Dynamic Resource Allocation as a Cluster Admin](https://kubernetes.io/docs/concepts/cluster-administration/dra/)
        * [Logging Architecture](https://kubernetes.io/docs/concepts/cluster-administration/logging/)
        * [Compatibility Version For Kubernetes Control Plane Components](https://kubernetes.io/docs/concepts/cluster-administration/compatibility-version/)
        * [Metrics For Kubernetes System Components](https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/)
        * [Metrics for Kubernetes Object States](https://kubernetes.io/docs/concepts/cluster-administration/kube-state-metrics/)
        * [System Logs](https://kubernetes.io/docs/concepts/cluster-administration/system-logs/)
        * [Traces For Kubernetes System Components](https://kubernetes.io/docs/concepts/cluster-administration/system-traces/)
        * [Proxies in Kubernetes](https://kubernetes.io/docs/concepts/cluster-administration/proxies/)
        * [API Priority and Fairness](https://kubernetes.io/docs/concepts/cluster-administration/flow-control/)
        * [Installing Addons](https://kubernetes.io/docs/concepts/cluster-administration/addons/)
        * [Coordinated Leader Election](https://kubernetes.io/docs/concepts/cluster-administration/coordinated-leader-election/)
      * [Windows in Kubernetes](https://kubernetes.io/docs/concepts/windows/)
        * [Windows containers in Kubernetes](https://kubernetes.io/docs/concepts/windows/intro/)
        * [Guide for Running Windows Containers in Kubernetes](https://kubernetes.io/docs/concepts/windows/user-guide/)
      * [Extending Kubernetes](https://kubernetes.io/docs/concepts/extend-kubernetes/)
        * [Compute, Storage, and Networking Extensions](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/)
          * [Network Plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)
          * [Device Plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/)
        * [Extending the Kubernetes API](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/)
          * [Custom Resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
          * [Kubernetes API Aggregation Layer](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/)
        * [Operator pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)
    * [Tasks](https://kubernetes.io/docs/tasks/)
      * [Install Tools](https://kubernetes.io/docs/tasks/tools/)
        * [Install and Set Up kubectl on Linux](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)
        * [Install and Set Up kubectl on macOS](https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/)
        * [Install and Set Up kubectl on Windows](https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/)
      * [Administer a Cluster](https://kubernetes.io/docs/tasks/administer-cluster/)
        * [Administration with kubeadm](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/)
          * [Adding Linux worker nodes](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/adding-linux-nodes/)
          * [Adding Windows worker nodes](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/adding-windows-nodes/)
          * [Upgrading kubeadm clusters](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
          * [Upgrading Linux nodes](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/upgrading-linux-nodes/)
          * [Upgrading Windows nodes](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/upgrading-windows-nodes/)
          * [Configuring a cgroup driver](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/configure-cgroup-driver/)
          * [Certificate Management with kubeadm](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/)
          * [Reconfiguring a kubeadm cluster](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-reconfigure/)
          * [Changing The Kubernetes Package Repository](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/change-package-repository/)
        * [Overprovision Node Capacity For A Cluster](https://kubernetes.io/docs/tasks/administer-cluster/node-overprovisioning/)
        * [Migrating from dockershim](https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/)
          * [Changing the Container Runtime on a Node from Docker Engine to containerd](https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd/)
          * [Find Out What Container Runtime is Used on a Node](https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/find-out-runtime-you-use/)
          * [Troubleshooting CNI plugin-related errors](https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/troubleshooting-cni-plugin-related-errors/)
          * [Check whether dockershim removal affects you](https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you/)
          * [Migrating telemetry and security agents from dockershim](https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents/)
        * [Generate Certificates Manually](https://kubernetes.io/docs/tasks/administer-cluster/certificates/)
        * [Manage Memory, CPU, and API Resources](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/)
          * [Configure Default Memory Requests and Limits for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/)
          * [Configure Default CPU Requests and Limits for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/)
          * [Configure Minimum and Maximum Memory Constraints for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/)
          * [Configure Minimum and Maximum CPU Constraints for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/)
          * [Configure Memory and CPU Quotas for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/)
          * [Configure a Pod Quota for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-pod-namespace/)
        * [Install a Network Policy Provider](https://kubernetes.io/docs/tasks/administer-cluster/network-policy-provider/)
          * [Use Antrea for NetworkPolicy](https://kubernetes.io/docs/tasks/administer-cluster/network-policy-provider/antrea-network-policy/)
          * [Use Calico for NetworkPolicy](https://kubernetes.io/docs/tasks/administer-cluster/network-policy-provider/calico-network-policy/)
          * [Use Cilium for NetworkPolicy](https://kubernetes.io/docs/tasks/administer-cluster/network-policy-provider/cilium-network-policy/)
          * [Use Kube-router for NetworkPolicy](https://kubernetes.io/docs/tasks/administer-cluster/network-policy-provider/kube-router-network-policy/)
          * [Romana for NetworkPolicy](https://kubernetes.io/docs/tasks/administer-cluster/network-policy-provider/romana-network-policy/)
          * [Weave Net for NetworkPolicy](https://kubernetes.io/docs/tasks/administer-cluster/network-policy-provider/weave-network-policy/)
        * [Access Clusters Using the Kubernetes API](https://kubernetes.io/docs/tasks/administer-cluster/access-cluster-api/)
        * [Enable Or Disable Feature Gates](https://kubernetes.io/docs/tasks/administer-cluster/configure-feature-gates/)
        * [Advertise Extended Resources for a Node](https://kubernetes.io/docs/tasks/administer-cluster/extended-resource-node/)
        * [Autoscale the DNS Service in a Cluster](https://kubernetes.io/docs/tasks/administer-cluster/dns-horizontal-autoscaling/)
        * [Change the Access Mode of a PersistentVolume to ReadWriteOncePod](https://kubernetes.io/docs/tasks/administer-cluster/change-pv-access-mode-readwriteoncepod/)
        * [Change the default StorageClass](https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/)
        * [Switching from Polling to CRI Event-based Updates to Container Status](https://kubernetes.io/docs/tasks/administer-cluster/switch-to-evented-pleg/)
        * [Change the Reclaim Policy of a PersistentVolume](https://kubernetes.io/docs/tasks/administer-cluster/change-pv-reclaim-policy/)
        * [Cloud Controller Manager Administration](https://kubernetes.io/docs/tasks/administer-cluster/running-cloud-controller/)
        * [Configure a kubelet image credential provider](https://kubernetes.io/docs/tasks/administer-cluster/kubelet-credential-provider/)
        * [Configure Quotas for API Objects](https://kubernetes.io/docs/tasks/administer-cluster/quota-api-object/)
        * [Control CPU Management Policies on the Node](https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/)
        * [Control Memory Management Policies on a Node](https://kubernetes.io/docs/tasks/administer-cluster/memory-manager/)
        * [Control Topology Management Policies on a node](https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/)
        * [Customizing DNS Service](https://kubernetes.io/docs/tasks/administer-cluster/dns-custom-nameservers/)
        * [Debugging DNS Resolution](https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/)
        * [Declare Network Policy](https://kubernetes.io/docs/tasks/administer-cluster/declare-network-policy/)
        * [Developing Cloud Controller Manager](https://kubernetes.io/docs/tasks/administer-cluster/developing-cloud-controller-manager/)
        * [Enable Or Disable A Kubernetes API](https://kubernetes.io/docs/tasks/administer-cluster/enable-disable-api/)
        * [Encrypting Confidential Data at Rest](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/)
        * [Decrypt Confidential Data that is Already Encrypted at Rest](https://kubernetes.io/docs/tasks/administer-cluster/decrypt-data/)
        * [Guaranteed Scheduling For Critical Add-On Pods](https://kubernetes.io/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/)
        * [IP Masquerade Agent User Guide](https://kubernetes.io/docs/tasks/administer-cluster/ip-masq-agent/)
        * [Limit Storage Consumption](https://kubernetes.io/docs/tasks/administer-cluster/limit-storage-consumption/)
        * [Migrate Replicated Control Plane To Use Cloud Controller Manager](https://kubernetes.io/docs/tasks/administer-cluster/controller-manager-leader-migration/)
        * [Operating etcd clusters for Kubernetes](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/)
        * [Reserve Compute Resources for System Daemons](https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/)
        * [Running Kubernetes Node Components as a Non-root User](https://kubernetes.io/docs/tasks/administer-cluster/kubelet-in-userns/)
        * [Safely Drain a Node](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/)
        * [Securing a Cluster](https://kubernetes.io/docs/tasks/administer-cluster/securing-a-cluster/)
        * [Harden Dynamic Resource Allocation in Your Cluster](https://kubernetes.io/docs/tasks/administer-cluster/hardening-dra/)
        * [Set Kubelet Parameters Via A Configuration File](https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/)
        * [Share a Cluster with Namespaces](https://kubernetes.io/docs/tasks/administer-cluster/namespaces/)
        * [Upgrade A Cluster](https://kubernetes.io/docs/tasks/administer-cluster/cluster-upgrade/)
        * [Use Cascading Deletion in a Cluster](https://kubernetes.io/docs/tasks/administer-cluster/use-cascading-deletion/)
        * [Using a KMS provider for data encryption](https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/)
        * [Using CoreDNS for Service Discovery](https://kubernetes.io/docs/tasks/administer-cluster/coredns/)
        * [Using NodeLocal DNSCache in Kubernetes Clusters](https://kubernetes.io/docs/tasks/administer-cluster/nodelocaldns/)
        * [Using sysctls in a Kubernetes Cluster](https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/)
        * [Verify Signed Kubernetes Artifacts](https://kubernetes.io/docs/tasks/administer-cluster/verify-signed-artifacts/)
      * [Configure Pods and Containers](https://kubernetes.io/docs/tasks/configure-pod-container/)
        * [Assign Memory Resources to Containers and Pods](https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/)
        * [Assign CPU Resources to Containers and Pods](https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/)
        * [Assign Devices to Pods and Containers](https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/)
          * [Set Up DRA in a Cluster](https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/set-up-dra-cluster/)
          * [Allocate Devices to Workloads with DRA](https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/allocate-devices-dra/)
          * [Access DRA Device Metadata](https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/access-dra-device-metadata/)
        * [Assign Pod-level CPU and memory resources](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pod-level-resources/)
        * [Configure GMSA for Windows Pods and containers](https://kubernetes.io/docs/tasks/configure-pod-container/configure-gmsa/)
        * [Resize CPU and Memory Resources assigned to Containers](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/)
        * [Resize CPU and Memory Resources assigned to Pods](https://kubernetes.io/docs/tasks/configure-pod-container/resize-pod-resources/)
        * [Configure RunAsUserName for Windows pods and containers](https://kubernetes.io/docs/tasks/configure-pod-container/configure-runasusername/)
        * [Create a Windows HostProcess Pod](https://kubernetes.io/docs/tasks/configure-pod-container/create-hostprocess-pod/)
        * [Configure Quality of Service for Pods](https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/)
        * [Assign Extended Resources to a Container](https://kubernetes.io/docs/tasks/configure-pod-container/extended-resource/)
        * [Configure a Pod to Use a Volume for Storage](https://kubernetes.io/docs/tasks/configure-pod-container/configure-volume-storage/)
        * [Configure a Pod to Use a Projected Volume for Storage](https://kubernetes.io/docs/tasks/configure-pod-container/configure-projected-volume-storage/)
        * [Configure a Security Context for a Pod or Container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)
        * [Configure Service Accounts for Pods](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)
        * [Pull an Image from a Private Registry](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/)
        * [Configure Liveness, Readiness and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
        * [Assign Pods to Nodes](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes/)
        * [Assign Pods to Nodes using Node Affinity](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity/)
        * [Configure Pod Initialization](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-initialization/)
        * [Attach Handlers to Container Lifecycle Events](https://kubernetes.io/docs/tasks/configure-pod-container/attach-handler-lifecycle-event/)
        * [Configure a Pod to Use a ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/)
        * [Share Process Namespace between Containers in a Pod](https://kubernetes.io/docs/tasks/configure-pod-container/share-process-namespace/)
        * [Use a User Namespace With a Pod](https://kubernetes.io/docs/tasks/configure-pod-container/user-namespaces/)
        * [Use an Image Volume With a Pod](https://kubernetes.io/docs/tasks/configure-pod-container/image-volumes/)
        * [Create static Pods](https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/)
        * [Translate a Docker Compose File to Kubernetes Resources](https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/)
        * [Enforce Pod Security Standards by Configuring the Built-in Admission Controller](https://kubernetes.io/docs/tasks/configure-pod-container/enforce-standards-admission-controller/)
        * [Enforce Pod Security Standards with Namespace Labels](https://kubernetes.io/docs/tasks/configure-pod-container/enforce-standards-namespace-labels/)
        * [Migrate from PodSecurityPolicy to the Built-In PodSecurity Admission Controller](https://kubernetes.io/docs/tasks/configure-pod-container/migrate-from-psp/)
      * [Monitoring, Logging, and Debugging](https://kubernetes.io/docs/tasks/debug/)
        * [Logging in Kubernetes](https://kubernetes.io/docs/tasks/debug/logging/)
        * [Monitoring in Kubernetes](https://kubernetes.io/docs/tasks/debug/monitoring/)
        * [Troubleshooting Applications](https://kubernetes.io/docs/tasks/debug/debug-application/)
          * [Debug Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-pods/)
          * [Debug Services](https://kubernetes.io/docs/tasks/debug/debug-application/debug-service/)
          * [Debug a StatefulSet](https://kubernetes.io/docs/tasks/debug/debug-application/debug-statefulset/)
          * [Determine the Reason for Pod Failure](https://kubernetes.io/docs/tasks/debug/debug-application/determine-reason-pod-failure/)
          * [Debug Init Containers](https://kubernetes.io/docs/tasks/debug/debug-application/debug-init-containers/)
          * [Debug Running Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/)
          * [Get a Shell to a Running Container](https://kubernetes.io/docs/tasks/debug/debug-application/get-shell-running-container/)
        * [Troubleshooting Clusters](https://kubernetes.io/docs/tasks/debug/debug-cluster/)
          * [Troubleshooting kubectl](https://kubernetes.io/docs/tasks/debug/debug-cluster/troubleshoot-kubectl/)
          * [Resource metrics pipeline](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/)
          * [Tools for Monitoring Resources](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-usage-monitoring/)
          * [Monitor Node Health](https://kubernetes.io/docs/tasks/debug/debug-cluster/monitor-node-health/)
          * [Debugging Kubernetes nodes with crictl](https://kubernetes.io/docs/tasks/debug/debug-cluster/crictl/)
          * [Troubleshooting Topology Management](https://kubernetes.io/docs/tasks/debug/debug-cluster/topology/)
          * [Auditing](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/)
          * [Debugging Kubernetes Nodes With Kubectl](https://kubernetes.io/docs/tasks/debug/debug-cluster/kubectl-node-debug/)
          * [Developing and debugging services locally using telepresence](https://kubernetes.io/docs/tasks/debug/debug-cluster/local-debugging/)
          * [Windows debugging tips](https://kubernetes.io/docs/tasks/debug/debug-cluster/windows/)
      * [Manage Kubernetes Objects](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/)
        * [Declarative Management of Kubernetes Objects Using Configuration Files](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/)
        * [Declarative Management of Kubernetes Objects Using Kustomize](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/)
        * [Managing Kubernetes Objects Using Imperative Commands](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/imperative-command/)
        * [Imperative Management of Kubernetes Objects Using Configuration Files](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/imperative-config/)
        * [Update API Objects in Place Using kubectl patch](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch/)
        * [Migrate Kubernetes Objects Using Storage Version Migration](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/storage-version-migration/)
      * [Managing Secrets](https://kubernetes.io/docs/tasks/configmap-secret/)
        * [Managing Secrets using kubectl](https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kubectl/)
        * [Managing Secrets using Configuration File](https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-config-file/)
        * [Managing Secrets using Kustomize](https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kustomize/)
      * [Inject Data Into Applications](https://kubernetes.io/docs/tasks/inject-data-application/)
        * [Define a Command and Arguments for a Container](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/)
        * [Define Dependent Environment Variables](https://kubernetes.io/docs/tasks/inject-data-application/define-interdependent-environment-variables/)
        * [Define Environment Variables for a Container](https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/)
        * [Define Environment Variable Values Using An Init Container](https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-via-file/)
        * [Expose Pod Information to Containers Through Environment Variables](https://kubernetes.io/docs/tasks/inject-data-application/environment-variable-expose-pod-information/)
        * [Expose Pod Information to Containers Through Files](https://kubernetes.io/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/)
        * [Distribute Credentials Securely Using Secrets](https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/)
      * [Run Applications](https://kubernetes.io/docs/tasks/run-application/)
        * [Run a Stateless Application Using a Deployment](https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/)
        * [Horizontal Manual Scaling for a Deployment](https://kubernetes.io/docs/tasks/run-application/scale-deployment/)
        * [Update a Deployment Without Downtime](https://kubernetes.io/docs/tasks/run-application/update-deployment-rolling/)
        * [Run a Single-Instance Stateful Application](https://kubernetes.io/docs/tasks/run-application/run-single-instance-stateful-application/)
        * [Run a Replicated Stateful Application](https://kubernetes.io/docs/tasks/run-application/run-replicated-stateful-application/)
        * [Scale a StatefulSet](https://kubernetes.io/docs/tasks/run-application/scale-stateful-set/)
        * [Delete a StatefulSet](https://kubernetes.io/docs/tasks/run-application/delete-stateful-set/)
        * [Force Delete StatefulSet Pods](https://kubernetes.io/docs/tasks/run-application/force-delete-stateful-set-pod/)
        * [HorizontalPodAutoscaler Walkthrough](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/)
        * [Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb/)
        * [Accessing the Kubernetes API from a Pod](https://kubernetes.io/docs/tasks/run-application/access-api-from-pod/)
      * [Run Jobs](https://kubernetes.io/docs/tasks/job/)
        * [Running Automated Tasks with a CronJob](https://kubernetes.io/docs/tasks/job/automated-tasks-with-cron-jobs/)
        * [Coarse Parallel Processing Using a Work Queue](https://kubernetes.io/docs/tasks/job/coarse-parallel-processing-work-queue/)
        * [Fine Parallel Processing Using a Work Queue](https://kubernetes.io/docs/tasks/job/fine-parallel-processing-work-queue/)
        * [Indexed Job for Parallel Processing with Static Work Assignment](https://kubernetes.io/docs/tasks/job/indexed-parallel-processing-static/)
        * [Job with Pod-to-Pod Communication](https://kubernetes.io/docs/tasks/job/job-with-pod-to-pod-communication/)
        * [Parallel Processing using Expansions](https://kubernetes.io/docs/tasks/job/parallel-processing-expansion/)
        * [Handling retriable and non-retriable pod failures with Pod failure policy](https://kubernetes.io/docs/tasks/job/pod-failure-policy/)
      * [Access Applications in a Cluster](https://kubernetes.io/docs/tasks/access-application-cluster/)
        * [Deploy and Access the Kubernetes Dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)
        * [Accessing Clusters](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/)
        * [Configure Access to Multiple Clusters](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/)
        * [Use Port Forwarding to Access Applications in a Cluster](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/)
        * [Use a Service to Access an Application in a Cluster](https://kubernetes.io/docs/tasks/access-application-cluster/service-access-application-cluster/)
        * [Connect a Frontend to a Backend Using Services](https://kubernetes.io/docs/tasks/access-application-cluster/connecting-frontend-backend/)
        * [Create an External Load Balancer](https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/)
        * [List All Container Images Running in a Cluster](https://kubernetes.io/docs/tasks/access-application-cluster/list-all-running-container-images/)
        * [Communicate Between Containers in the Same Pod Using a Shared Volume](https://kubernetes.io/docs/tasks/access-application-cluster/communicate-containers-same-pod-shared-volume/)
        * [Configure DNS for a Cluster](https://kubernetes.io/docs/tasks/access-application-cluster/configure-dns-cluster/)
        * [Access Services Running on Clusters](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster-services/)
      * [Extend Kubernetes](https://kubernetes.io/docs/tasks/extend-kubernetes/)
        * [Configure the Aggregation Layer](https://kubernetes.io/docs/tasks/extend-kubernetes/configure-aggregation-layer/)
        * [Use Custom Resources](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/)
          * [Extend the Kubernetes API with CustomResourceDefinitions](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/)
          * [Versions in CustomResourceDefinitions](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/)
        * [Set up an Extension API Server](https://kubernetes.io/docs/tasks/extend-kubernetes/setup-extension-api-server/)
        * [Configure Multiple Schedulers](https://kubernetes.io/docs/tasks/extend-kubernetes/configure-multiple-schedulers/)
        * [Use an HTTP Proxy to Access the Kubernetes API](https://kubernetes.io/docs/tasks/extend-kubernetes/http-proxy-access-api/)
        * [Use a SOCKS5 Proxy to Access the Kubernetes API](https://kubernetes.io/docs/tasks/extend-kubernetes/socks5-proxy-access-api/)
        * [Set up Konnectivity service](https://kubernetes.io/docs/tasks/extend-kubernetes/setup-konnectivity/)
      * [TLS](https://kubernetes.io/docs/tasks/tls/)
        * [Issue a Certificate for a Kubernetes API Client Using A CertificateSigningRequest](https://kubernetes.io/docs/tasks/tls/certificate-issue-client-csr/)
        * [Configure Certificate Rotation for the Kubelet](https://kubernetes.io/docs/tasks/tls/certificate-rotation/)
        * [Manage TLS Certificates in a Cluster](https://kubernetes.io/docs/tasks/tls/managing-tls-in-a-cluster/)
        * [Manual Rotation of CA Certificates](https://kubernetes.io/docs/tasks/tls/manual-rotation-of-ca-certificates/)
      * [Manage Cluster Daemons](https://kubernetes.io/docs/tasks/manage-daemon/)
        * [Building a Basic DaemonSet](https://kubernetes.io/docs/tasks/manage-daemon/create-daemon-set/)
        * [Perform a Rolling Update on a DaemonSet](https://kubernetes.io/docs/tasks/manage-daemon/update-daemon-set/)
        * [Perform a Rollback on a DaemonSet](https://kubernetes.io/docs/tasks/manage-daemon/rollback-daemon-set/)
        * [Running Pods on Only Some Nodes](https://kubernetes.io/docs/tasks/manage-daemon/pods-some-nodes/)
      * [Networking](https://kubernetes.io/docs/tasks/network/)
        * [Adding entries to Pod /etc/hosts with HostAliases](https://kubernetes.io/docs/tasks/network/customize-hosts-file-for-pods/)
        * [Extend Service IP Ranges](https://kubernetes.io/docs/tasks/network/extend-service-ip-ranges/)
        * [Kubernetes Default ServiceCIDR Reconfiguration](https://kubernetes.io/docs/tasks/network/reconfigure-default-service-ip-ranges/)
        * [Validate IPv4/IPv6 dual-stack](https://kubernetes.io/docs/tasks/network/validate-dual-stack/)
      * [Extend kubectl with plugins](https://kubernetes.io/docs/tasks/extend-kubectl/kubectl-plugins/)
      * [Manage HugePages](https://kubernetes.io/docs/tasks/manage-hugepages/scheduling-hugepages/)
      * [Schedule GPUs](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/)
    * [Tutorials](https://kubernetes.io/docs/tutorials/)
      * [Hello Minikube](https://kubernetes.io/docs/tutorials/hello-minikube/)
      * [Learn Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
        * [Create a Cluster](https://kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/)
          * [Using Minikube to Create a Cluster](https://kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/cluster-intro/)
        * [Deploy an App](https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/)
          * [Using kubectl to Create a Deployment](https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/)
        * [Explore Your App](https://kubernetes.io/docs/tutorials/kubernetes-basics/explore/)
          * [Viewing Pods and Nodes](https://kubernetes.io/docs/tutorials/kubernetes-basics/explore/explore-intro/)
        * [Expose Your App Publicly](https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/)
          * [Using a Service to Expose Your App](https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/expose-intro/)
        * [Scale Your App](https://kubernetes.io/docs/tutorials/kubernetes-basics/scale/)
          * [Running Multiple Instances of Your App](https://kubernetes.io/docs/tutorials/kubernetes-basics/scale/scale-intro/)
        * [Update Your App](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/)
          * [Performing a Rolling Update](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/)
      * [Configuration](https://kubernetes.io/docs/tutorials/configuration/)
        * [Updating Configuration via a ConfigMap](https://kubernetes.io/docs/tutorials/configuration/updating-configuration-via-a-configmap/)
        * [Configuring Redis using a ConfigMap](https://kubernetes.io/docs/tutorials/configuration/configure-redis-using-configmap/)
        * [Adopting Sidecar Containers](https://kubernetes.io/docs/tutorials/configuration/pod-sidecar-containers/)
        * [Configure a Pod to Use a PersistentVolume for Storage](https://kubernetes.io/docs/tutorials/configuration/configure-persistent-volume-storage/)
      * [Security](https://kubernetes.io/docs/tutorials/security/)
        * [Apply Pod Security Standards at the Cluster Level](https://kubernetes.io/docs/tutorials/security/cluster-level-pss/)
        * [Apply Pod Security Standards at the Namespace Level](https://kubernetes.io/docs/tutorials/security/ns-level-pss/)
        * [Restrict a Container's Access to Resources with AppArmor](https://kubernetes.io/docs/tutorials/security/apparmor/)
        * [Restrict a Container's Syscalls with seccomp](https://kubernetes.io/docs/tutorials/security/seccomp/)
      * [Stateless Applications](https://kubernetes.io/docs/tutorials/stateless-application/)
        * [Exposing an External IP Address to Access an Application in a Cluster](https://kubernetes.io/docs/tutorials/stateless-application/expose-external-ip-address/)
        * [Example: Deploying PHP Guestbook application with Redis](https://kubernetes.io/docs/tutorials/stateless-application/guestbook/)
      * [Stateful Applications](https://kubernetes.io/docs/tutorials/stateful-application/)
        * [StatefulSet Basics](https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/)
        * [Example: Deploying WordPress and MySQL with Persistent Volumes](https://kubernetes.io/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/)
        * [Example: Deploying Cassandra with a StatefulSet](https://kubernetes.io/docs/tutorials/stateful-application/cassandra/)
        * [Running ZooKeeper, A Distributed System Coordinator](https://kubernetes.io/docs/tutorials/stateful-application/zookeeper/)
      * [Cluster Management](https://kubernetes.io/docs/tutorials/cluster-management/)
        * [Running Kubelet in Standalone Mode](https://kubernetes.io/docs/tutorials/cluster-management/kubelet-standalone/)
        * [Configuring swap memory on Kubernetes nodes](https://kubernetes.io/docs/tutorials/cluster-management/provision-swap-memory/)
        * [Install Drivers and Allocate Devices with DRA](https://kubernetes.io/docs/tutorials/cluster-management/install-use-dra/)
        * [Namespaces Walkthrough](https://kubernetes.io/docs/tutorials/cluster-management/namespaces-walkthrough/)
      * [Services](https://kubernetes.io/docs/tutorials/services/)
        * [Connecting Applications with Services](https://kubernetes.io/docs/tutorials/services/connect-applications-service/)
        * [Using Source IP](https://kubernetes.io/docs/tutorials/services/source-ip/)
        * [Explore Termination Behavior for Pods And Their Endpoints](https://kubernetes.io/docs/tutorials/services/pods-and-endpoint-termination-flow/)
    * [Reference](https://kubernetes.io/docs/reference/)
      * [Glossary](https://kubernetes.io/docs/reference/glossary/)
      * [API Overview](https://kubernetes.io/docs/reference/using-api/)
        * [Declarative API Validation](https://kubernetes.io/docs/reference/using-api/declarative-validation/)
        * [Kubernetes API Concepts](https://kubernetes.io/docs/reference/using-api/api-concepts/)
        * [Server-Side Apply](https://kubernetes.io/docs/reference/using-api/server-side-apply/)
        * [Client Libraries](https://kubernetes.io/docs/reference/using-api/client-libraries/)
        * [Common Expression Language in Kubernetes](https://kubernetes.io/docs/reference/using-api/cel/)
        * [Kubernetes Deprecation Policy](https://kubernetes.io/docs/reference/using-api/deprecation-policy/)
        * [Deprecated API Migration Guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/)
        * [Kubernetes API health endpoints](https://kubernetes.io/docs/reference/using-api/health-checks/)
      * [API Access Control](https://kubernetes.io/docs/reference/access-authn-authz/)
        * [Authenticating](https://kubernetes.io/docs/reference/access-authn-authz/authentication/)
        * [Authenticating with Bootstrap Tokens](https://kubernetes.io/docs/reference/access-authn-authz/bootstrap-tokens/)
        * [Authorization](https://kubernetes.io/docs/reference/access-authn-authz/authorization/)
        * [Using RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
        * [Using Node Authorization](https://kubernetes.io/docs/reference/access-authn-authz/node/)
        * [Webhook Mode](https://kubernetes.io/docs/reference/access-authn-authz/webhook/)
        * [Using ABAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/abac/)
        * [Admission Control](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/ "Admission Control in Kubernetes")
        * [Dynamic Admission Control](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/)
        * [Managing Service Accounts](https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/)
        * [User Impersonation](https://kubernetes.io/docs/reference/access-authn-authz/user-impersonation/)
        * [Certificates and Certificate Signing Requests](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/)
        * [Mapping PodSecurityPolicies to Pod Security Standards](https://kubernetes.io/docs/reference/access-authn-authz/psp-to-pod-security-standards/)
        * [Kubelet authentication/authorization](https://kubernetes.io/docs/reference/access-authn-authz/kubelet-authn-authz/)
        * [TLS bootstrapping](https://kubernetes.io/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/)
        * [Manifest-Based Admission Control](https://kubernetes.io/docs/reference/access-authn-authz/manifest-admission-control/)
        * [Mutating Admission Policy](https://kubernetes.io/docs/reference/access-authn-authz/mutating-admission-policy/)
        * [Validating Admission Policy](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/)
      * [Well-Known Labels, Annotations and Taints](https://kubernetes.io/docs/reference/labels-annotations-taints/)
        * [Audit Annotations](https://kubernetes.io/docs/reference/labels-annotations-taints/audit-annotations/)
      * [Kubernetes API](https://kubernetes.io/docs/reference/kubernetes-api/)
        * [API Groups](https://kubernetes.io/docs/reference/kubernetes-api/group-versions/)
        * [Admissionregistration](https://kubernetes.io/docs/reference/kubernetes-api/admissionregistration/)
          * [MutatingAdmissionPolicy](https://kubernetes.io/docs/reference/kubernetes-api/admissionregistration/mutating-admission-policy-v1/)
          * [MutatingAdmissionPolicyBinding](https://kubernetes.io/docs/reference/kubernetes-api/admissionregistration/mutating-admission-policy-binding-v1/)
          * [MutatingWebhookConfiguration](https://kubernetes.io/docs/reference/kubernetes-api/admissionregistration/mutating-webhook-configuration-v1/)
          * [ValidatingAdmissionPolicy](https://kubernetes.io/docs/reference/kubernetes-api/admissionregistration/validating-admission-policy-v1/)
          * [ValidatingAdmissionPolicyBinding](https://kubernetes.io/docs/reference/kubernetes-api/admissionregistration/validating-admission-policy-binding-v1/)
          * [ValidatingWebhookConfiguration](https://kubernetes.io/docs/reference/kubernetes-api/admissionregistration/validating-webhook-configuration-v1/)
        * [Apiextensions](https://kubernetes.io/docs/reference/kubernetes-api/apiextensions/)
          * [CustomResourceDefinition](https://kubernetes.io/docs/reference/kubernetes-api/apiextensions/custom-resource-definition-v1/)
        * [Apiregistration](https://kubernetes.io/docs/reference/kubernetes-api/apiregistration/)
          * [APIService](https://kubernetes.io/docs/reference/kubernetes-api/apiregistration/api-service-v1/)
        * [Apiserverinternal](https://kubernetes.io/docs/reference/kubernetes-api/apiserverinternal/)
          * [StorageVersion](https://kubernetes.io/docs/reference/kubernetes-api/apiserverinternal/storage-version-v1alpha1/)
        * [Apps](https://kubernetes.io/docs/reference/kubernetes-api/apps/)
          * [ControllerRevision](https://kubernetes.io/docs/reference/kubernetes-api/apps/controller-revision-v1/)
          * [DaemonSet](https://kubernetes.io/docs/reference/kubernetes-api/apps/daemon-set-v1/)
          * [Deployment](https://kubernetes.io/docs/reference/kubernetes-api/apps/deployment-v1/)
          * [ReplicaSet](https://kubernetes.io/docs/reference/kubernetes-api/apps/replica-set-v1/)
          * [StatefulSet](https://kubernetes.io/docs/reference/kubernetes-api/apps/stateful-set-v1/)
        * [Autoscaling](https://kubernetes.io/docs/reference/kubernetes-api/autoscaling/)
          * [HorizontalPodAutoscaler](https://kubernetes.io/docs/reference/kubernetes-api/autoscaling/horizontal-pod-autoscaler-v2/)
        * [Batch](https://kubernetes.io/docs/reference/kubernetes-api/batch/)
          * [CronJob](https://kubernetes.io/docs/reference/kubernetes-api/batch/cron-job-v1/)
          * [Job](https://kubernetes.io/docs/reference/kubernetes-api/batch/job-v1/)
        * [Certificates](https://kubernetes.io/docs/reference/kubernetes-api/certificates/)
          * [CertificateSigningRequest](https://kubernetes.io/docs/reference/kubernetes-api/certificates/certificate-signing-request-v1/)
          * [ClusterTrustBundle](https://kubernetes.io/docs/reference/kubernetes-api/certificates/cluster-trust-bundle-v1beta1/)
          * [PodCertificateRequest](https://kubernetes.io/docs/reference/kubernetes-api/certificates/pod-certificate-request-v1beta1/)
        * [Coordination](https://kubernetes.io/docs/reference/kubernetes-api/coordination/)
          * [Lease](https://kubernetes.io/docs/reference/kubernetes-api/coordination/lease-v1/)
          * [LeaseCandidate](https://kubernetes.io/docs/reference/kubernetes-api/coordination/lease-candidate-v1beta1/)
        * [Events](https://kubernetes.io/docs/reference/kubernetes-api/events/)
          * [Event](https://kubernetes.io/docs/reference/kubernetes-api/events/event-v1/)
        * [Core](https://kubernetes.io/docs/reference/kubernetes-api/core/)
          * [ComponentStatus](https://kubernetes.io/docs/reference/kubernetes-api/core/component-status-v1/)
          * [ConfigMap](https://kubernetes.io/docs/reference/kubernetes-api/core/config-map-v1/)
          * [Endpoints](https://kubernetes.io/docs/reference/kubernetes-api/core/endpoints-v1/)
          * [Event](https://kubernetes.io/docs/reference/kubernetes-api/core/event-v1/)
          * [LimitRange](https://kubernetes.io/docs/reference/kubernetes-api/core/limit-range-v1/)
          * [Namespace](https://kubernetes.io/docs/reference/kubernetes-api/core/namespace-v1/)
          * [Node](https://kubernetes.io/docs/reference/kubernetes-api/core/node-v1/)
          * [PersistentVolume](https://kubernetes.io/docs/reference/kubernetes-api/core/persistent-volume-v1/)
          * [PersistentVolumeClaim](https://kubernetes.io/docs/reference/kubernetes-api/core/persistent-volume-claim-v1/)
          * [Pod](https://kubernetes.io/docs/reference/kubernetes-api/core/pod-v1/)
          * [PodTemplate](https://kubernetes.io/docs/reference/kubernetes-api/core/pod-template-v1/)
          * [ReplicationController](https://kubernetes.io/docs/reference/kubernetes-api/core/replication-controller-v1/)
          * [ResourceQuota](https://kubernetes.io/docs/reference/kubernetes-api/core/resource-quota-v1/)
          * [Secret](https://kubernetes.io/docs/reference/kubernetes-api/core/secret-v1/)
          * [Service](https://kubernetes.io/docs/reference/kubernetes-api/core/service-v1/)
          * [ServiceAccount](https://kubernetes.io/docs/reference/kubernetes-api/core/service-account-v1/)
        * [Discovery](https://kubernetes.io/docs/reference/kubernetes-api/discovery/)
          * [EndpointSlice](https://kubernetes.io/docs/reference/kubernetes-api/discovery/endpoint-slice-v1/)
        * [Flowcontrol](https://kubernetes.io/docs/reference/kubernetes-api/flowcontrol/)
          * [FlowSchema](https://kubernetes.io/docs/reference/kubernetes-api/flowcontrol/flow-schema-v1/)
          * [PriorityLevelConfiguration](https://kubernetes.io/docs/reference/kubernetes-api/flowcontrol/priority-level-configuration-v1/)
        * [Networking](https://kubernetes.io/docs/reference/kubernetes-api/networking/)
          * [IPAddress](https://kubernetes.io/docs/reference/kubernetes-api/networking/ip-address-v1/)
          * [Ingress](https://kubernetes.io/docs/reference/kubernetes-api/networking/ingress-v1/)
          * [IngressClass](https://kubernetes.io/docs/reference/kubernetes-api/networking/ingress-class-v1/)
          * [NetworkPolicy](https://kubernetes.io/docs/reference/kubernetes-api/networking/network-policy-v1/)
          * [ServiceCIDR](https://kubernetes.io/docs/reference/kubernetes-api/networking/service-cidr-v1/)
        * [Node](https://kubernetes.io/docs/reference/kubernetes-api/node/)
          * [RuntimeClass](https://kubernetes.io/docs/reference/kubernetes-api/node/runtime-class-v1/)
        * [Policy](https://kubernetes.io/docs/reference/kubernetes-api/policy/)
          * [PodDisruptionBudget](https://kubernetes.io/docs/reference/kubernetes-api/policy/pod-disruption-budget-v1/)
        * [Rbac](https://kubernetes.io/docs/reference/kubernetes-api/rbac/)
          * [ClusterRole](https://kubernetes.io/docs/reference/kubernetes-api/rbac/cluster-role-v1/)
          * [ClusterRoleBinding](https://kubernetes.io/docs/reference/kubernetes-api/rbac/cluster-role-binding-v1/)
          * [Role](https://kubernetes.io/docs/reference/kubernetes-api/rbac/role-v1/)
          * [RoleBinding](https://kubernetes.io/docs/reference/kubernetes-api/rbac/role-binding-v1/)
        * [Resource](https://kubernetes.io/docs/reference/kubernetes-api/resource/)
          * [DeviceClass](https://kubernetes.io/docs/reference/kubernetes-api/resource/device-class-v1/)
          * [DeviceTaintRule](https://kubernetes.io/docs/reference/kubernetes-api/resource/device-taint-rule-v1beta2/)
          * [ResourceClaim](https://kubernetes.io/docs/reference/kubernetes-api/resource/resource-claim-v1/)
          * [ResourceClaimTemplate](https://kubernetes.io/docs/reference/kubernetes-api/resource/resource-claim-template-v1/)
          * [ResourcePoolStatusRequest](https://kubernetes.io/docs/reference/kubernetes-api/resource/resource-pool-status-request-v1alpha3/)
          * [ResourceSlice](https://kubernetes.io/docs/reference/kubernetes-api/resource/resource-slice-v1/)
        * [Scheduling](https://kubernetes.io/docs/reference/kubernetes-api/scheduling/)
          * [PodGroup](https://kubernetes.io/docs/reference/kubernetes-api/scheduling/pod-group-v1alpha2/)
          * [PriorityClass](https://kubernetes.io/docs/reference/kubernetes-api/scheduling/priority-class-v1/)
          * [Workload](https://kubernetes.io/docs/reference/kubernetes-api/scheduling/workload-v1alpha2/)
        * [Storage](https://kubernetes.io/docs/reference/kubernetes-api/storage/)
          * [CSIDriver](https://kubernetes.io/docs/reference/kubernetes-api/storage/csi-driver-v1/)
          * [CSINode](https://kubernetes.io/docs/reference/kubernetes-api/storage/csi-node-v1/)
          * [CSIStorageCapacity](https://kubernetes.io/docs/reference/kubernetes-api/storage/csi-storage-capacity-v1/)
          * [StorageClass](https://kubernetes.io/docs/reference/kubernetes-api/storage/storage-class-v1/)
          * [VolumeAttachment](https://kubernetes.io/docs/reference/kubernetes-api/storage/volume-attachment-v1/)
          * [VolumeAttributesClass](https://kubernetes.io/docs/reference/kubernetes-api/storage/volume-attributes-class-v1/)
        * [Storagemigration](https://kubernetes.io/docs/reference/kubernetes-api/storagemigration/)
          * [StorageVersionMigration](https://kubernetes.io/docs/reference/kubernetes-api/storagemigration/storage-version-migration-v1beta1/)
      * [Instrumentation](https://kubernetes.io/docs/reference/instrumentation/)
        * [Service Level Indicator Metrics](https://kubernetes.io/docs/reference/instrumentation/slis/ "Kubernetes Component SLI Metrics")
        * [CRI Pod & Container Metrics](https://kubernetes.io/docs/reference/instrumentation/cri-pod-container-metrics/)
        * [Native Histograms](https://kubernetes.io/docs/reference/instrumentation/native-histograms/ "Native Histogram Support for Kubernetes Metrics")
        * [Node metrics data](https://kubernetes.io/docs/reference/instrumentation/node-metrics/)
        * [Understand Pressure Stall Information (PSI) Metrics](https://kubernetes.io/docs/reference/instrumentation/understand-psi-metrics/)
        * [Kubernetes z-pages](https://kubernetes.io/docs/reference/instrumentation/zpages/)
        * [Kubernetes Metrics Reference](https://kubernetes.io/docs/reference/instrumentation/metrics/)
      * [Kubernetes Issues and Security](https://kubernetes.io/docs/reference/issues-security/)
        * [Kubernetes Issue Tracker](https://kubernetes.io/docs/reference/issues-security/issues/)
        * [Kubernetes Security and Disclosure Information](https://kubernetes.io/docs/reference/issues-security/security/)
        * [CVE feed](https://kubernetes.io/docs/reference/issues-security/official-cve-feed/ "Official CVE Feed")
      * [Node Reference Information](https://kubernetes.io/docs/reference/node/)
        * [Kubelet Checkpoint API](https://kubernetes.io/docs/reference/node/kubelet-checkpoint-api/)
        * [Linux Kernel Version Requirements](https://kubernetes.io/docs/reference/node/kernel-version-requirements/)
        * [Articles on dockershim Removal and on Using CRI-compatible Runtimes](https://kubernetes.io/docs/reference/node/topics-on-dockershim-and-cri-compatible-runtimes/)
        * [Kubelet Pod Info gRPC API](https://kubernetes.io/docs/reference/node/kubelet-pod-info-grpc-api/)
        * [Node Labels Populated By The Kubelet](https://kubernetes.io/docs/reference/node/node-labels/)
        * [Kubelet Sync Loop](https://kubernetes.io/docs/reference/node/kubelet-sync-loop/)
        * [Local Files And Paths Used By The Kubelet](https://kubernetes.io/docs/reference/node/kubelet-files/)
        * [Kubelet Configuration Directory Merging](https://kubernetes.io/docs/reference/node/kubelet-config-directory-merging/)
        * [Kubelet Device Manager API Versions](https://kubernetes.io/docs/reference/node/device-plugin-api-versions/)
        * [Kubelet Systemd Watchdog](https://kubernetes.io/docs/reference/node/systemd-watchdog/)
        * [Node Status](https://kubernetes.io/docs/reference/node/node-status/)
        * [Seccomp and Kubernetes](https://kubernetes.io/docs/reference/node/seccomp/)
        * [Linux Node Swap Behaviors](https://kubernetes.io/docs/reference/node/swap-behavior/)
      * [Networking Reference](https://kubernetes.io/docs/reference/networking/)
        * [Protocols for Services](https://kubernetes.io/docs/reference/networking/service-protocols/)
        * [Ports and Protocols](https://kubernetes.io/docs/reference/networking/ports-and-protocols/)
        * [Virtual IPs and Service Proxies](https://kubernetes.io/docs/reference/networking/virtual-ips/)
      * [Setup tools](https://kubernetes.io/docs/reference/setup-tools/)
        * [Kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/)
          * [kubeadm init](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/)
          * [kubeadm join](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-join/)
          * [kubeadm upgrade](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-upgrade/)
          * [kubeadm upgrade phases](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-upgrade-phase/)
          * [kubeadm config](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-config/)
          * [kubeadm reset](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-reset/)
          * [kubeadm token](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-token/)
          * [kubeadm version](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-version/)
          * [kubeadm alpha](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-alpha/)
          * [kubeadm certs](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-certs/)
          * [kubeadm init phase](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init-phase/)
          * [kubeadm join phase](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-join-phase/)
          * [kubeadm kubeconfig](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-kubeconfig/)
          * [kubeadm reset phase](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-reset-phase/)
          * [Implementation details](https://kubernetes.io/docs/reference/setup-tools/kubeadm/implementation-details/)
      * [Command line tool (kubectl)](https://kubernetes.io/docs/reference/kubectl/)
        * [Introduction to kubectl](https://kubernetes.io/docs/reference/kubectl/introduction/)
        * [kubectl Quick Reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/)
        * [kubectl reference](https://kubernetes.io/docs/reference/kubectl/generated/)
          * [kubectl](https://kubernetes.io/docs/reference/kubectl/generated/kubectl/)
          * [kubectl annotate](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_annotate/)
          * [kubectl api-resources](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_api-resources/)
          * [kubectl api-versions](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_api-versions/)
          * [kubectl apply](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply/)
            * [kubectl apply edit-last-applied](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply/kubectl_apply_edit-last-applied/)
            * [kubectl apply set-last-applied](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply/kubectl_apply_set-last-applied/)
            * [kubectl apply view-last-applied](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply/kubectl_apply_view-last-applied/)
          * [kubectl attach](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_attach/)
          * [kubectl auth](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_auth/)
            * [kubectl auth can-i](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_auth/kubectl_auth_can-i/)
            * [kubectl auth reconcile](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_auth/kubectl_auth_reconcile/)
            * [kubectl auth whoami](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_auth/kubectl_auth_whoami/)
          * [kubectl autoscale](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_autoscale/)
          * [kubectl certificate](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_certificate/)
            * [kubectl certificate approve](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_certificate/kubectl_certificate_approve/)
            * [kubectl certificate deny](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_certificate/kubectl_certificate_deny/)
          * [kubectl cluster-info](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_cluster-info/)
            * [kubectl cluster-info dump](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_cluster-info/kubectl_cluster-info_dump/)
          * [kubectl completion](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_completion/)
          * [kubectl config](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/)
            * [kubectl config current-context](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_current-context/)
            * [kubectl config delete-cluster](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_delete-cluster/)
            * [kubectl config delete-context](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_delete-context/)
            * [kubectl config delete-user](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_delete-user/)
            * [kubectl config get-clusters](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_get-clusters/)
            * [kubectl config get-contexts](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_get-contexts/)
            * [kubectl config get-users](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_get-users/)
            * [kubectl config rename-context](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_rename-context/)
            * [kubectl config set](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_set/)
            * [kubectl config set-cluster](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_set-cluster/)
            * [kubectl config set-context](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_set-context/)
            * [kubectl config set-credentials](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_set-credentials/)
            * [kubectl config unset](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_unset/)
            * [kubectl config use-context](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_use-context/)
            * [kubectl config view](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_view/)
          * [kubectl cordon](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_cordon/)
          * [kubectl cp](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_cp/)
          * [kubectl create](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/)
            * [kubectl create clusterrole](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_clusterrole/)
            * [kubectl create clusterrolebinding](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_clusterrolebinding/)
            * [kubectl create configmap](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_configmap/)
            * [kubectl create cronjob](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_cronjob/)
            * [kubectl create deployment](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_deployment/)
            * [kubectl create ingress](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_ingress/)
            * [kubectl create job](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_job/)
            * [kubectl create namespace](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_namespace/)
            * [kubectl create poddisruptionbudget](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_poddisruptionbudget/)
            * [kubectl create priorityclass](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_priorityclass/)
            * [kubectl create quota](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_quota/)
            * [kubectl create role](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_role/)
            * [kubectl create rolebinding](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_rolebinding/)
            * [kubectl create secret](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_secret/)
            * [kubectl create secret docker-registry](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_secret_docker-registry/)
            * [kubectl create secret generic](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_secret_generic/)
            * [kubectl create secret tls](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_secret_tls/)
            * [kubectl create service](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_service/)
            * [kubectl create service clusterip](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_service_clusterip/)
            * [kubectl create service externalname](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_service_externalname/)
            * [kubectl create service loadbalancer](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_service_loadbalancer/)
            * [kubectl create service nodeport](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_service_nodeport/)
            * [kubectl create serviceaccount](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_serviceaccount/)
            * [kubectl create token](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_token/)
          * [kubectl debug](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_debug/)
          * [kubectl delete](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_delete/)
          * [kubectl describe](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_describe/)
          * [kubectl diff](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_diff/)
          * [kubectl drain](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_drain/)
          * [kubectl edit](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_edit/)
          * [kubectl events](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_events/)
          * [kubectl exec](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_exec/)
          * [kubectl explain](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_explain/)
          * [kubectl expose](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_expose/)
          * [kubectl get](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_get/)
          * [kubectl kuberc](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_kuberc/)
            * [kubectl kuberc set](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_kuberc/kubectl_kuberc_set/)
            * [kubectl kuberc view](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_kuberc/kubectl_kuberc_view/)
          * [kubectl kustomize](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_kustomize/)
          * [kubectl label](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_label/)
          * [kubectl logs](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_logs/)
          * [kubectl options](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_options/)
          * [kubectl patch](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_patch/)
          * [kubectl plugin](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_plugin/)
            * [kubectl plugin list](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_plugin/kubectl_plugin_list/)
          * [kubectl port-forward](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_port-forward/)
          * [kubectl proxy](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_proxy/)
          * [kubectl replace](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_replace/)
          * [kubectl rollout](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/)
            * [kubectl rollout history](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_history/)
            * [kubectl rollout pause](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_pause/)
            * [kubectl rollout restart](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_restart/)
            * [kubectl rollout resume](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_resume/)
            * [kubectl rollout status](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_status/)
            * [kubectl rollout undo](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_undo/)
          * [kubectl run](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_run/)
          * [kubectl scale](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_scale/)
          * [kubectl set](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_set/)
            * [kubectl set env](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_set/kubectl_set_env/)
            * [kubectl set image](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_set/kubectl_set_image/)
            * [kubectl set resources](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_set/kubectl_set_resources/)
            * [kubectl set selector](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_set/kubectl_set_selector/)
            * [kubectl set serviceaccount](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_set/kubectl_set_serviceaccount/)
            * [kubectl set subject](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_set/kubectl_set_subject/)
          * [kubectl taint](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_taint/)
          * [kubectl top](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_top/)
            * [kubectl top node](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_top/kubectl_top_node/)
            * [kubectl top pod](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_top/kubectl_top_pod/)
          * [kubectl uncordon](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_uncordon/)
          * [kubectl version](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_version/)
          * [kubectl wait](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_wait/)
        * [kubectl Commands](https://kubernetes.io/docs/reference/kubectl/kubectl-cmds/)
        * [kubectl](https://kubernetes.io/docs/reference/kubectl/kubectl/)
        * [JSONPath Support](https://kubernetes.io/docs/reference/kubectl/jsonpath/)
        * [kubectl for Docker Users](https://kubernetes.io/docs/reference/kubectl/docker-cli-to-kubectl/)
        * [kubectl Usage Conventions](https://kubernetes.io/docs/reference/kubectl/conventions/)
        * [Kubectl user preferences (kuberc)](https://kubernetes.io/docs/reference/kubectl/kuberc/)
      * [Encodings](https://kubernetes.io/docs/reference/encodings/)
        * [KYAML Reference](https://kubernetes.io/docs/reference/encodings/kyaml/)
      * [Component tools](https://kubernetes.io/docs/reference/command-line-tools-reference/)
        * [Feature Gates](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/)
        * [Feature Gates (removed)](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates-removed/)
        * [kube-apiserver](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/)
        * [kube-controller-manager](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/)
        * [kube-proxy](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/)
        * [kube-scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/)
        * [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/)
      * [Debug cluster](https://kubernetes.io/docs/reference/debug-cluster/)
        * [Flow control](https://kubernetes.io/docs/reference/debug-cluster/flow-control/)
      * [Configuration APIs](https://kubernetes.io/docs/reference/config-api/)
        * [Client Authentication (v1)](https://kubernetes.io/docs/reference/config-api/client-authentication.v1/)
        * [Client Authentication (v1beta1)](https://kubernetes.io/docs/reference/config-api/client-authentication.v1beta1/)
        * [Event Rate Limit Configuration (v1alpha1)](https://kubernetes.io/docs/reference/config-api/apiserver-eventratelimit.v1alpha1/)
        * [Image Policy API (v1alpha1)](https://kubernetes.io/docs/reference/config-api/imagepolicy.v1alpha1/)
        * [kube-apiserver Admission (v1)](https://kubernetes.io/docs/reference/config-api/apiserver-admission.v1/)
        * [kube-apiserver Audit Configuration (v1)](https://kubernetes.io/docs/reference/config-api/apiserver-audit.v1/)
        * [kube-apiserver Configuration (v1)](https://kubernetes.io/docs/reference/config-api/apiserver-config.v1/)
        * [kube-apiserver Configuration (v1alpha1)](https://kubernetes.io/docs/reference/config-api/apiserver-config.v1alpha1/)
        * [kube-apiserver Configuration (v1beta1)](https://kubernetes.io/docs/reference/config-api/apiserver-config.v1beta1/)
        * [kube-controller-manager Configuration (v1alpha1)](https://kubernetes.io/docs/reference/config-api/kube-controller-manager-config.v1alpha1/)
        * [kube-proxy Configuration (v1alpha1)](https://kubernetes.io/docs/reference/config-api/kube-proxy-config.v1alpha1/)
        * [kube-scheduler Configuration (v1)](https://kubernetes.io/docs/reference/config-api/kube-scheduler-config.v1/)
        * [kubeadm Configuration (v1beta3)](https://kubernetes.io/docs/reference/config-api/kubeadm-config.v1beta3/)
        * [kubeadm Configuration (v1beta4)](https://kubernetes.io/docs/reference/config-api/kubeadm-config.v1beta4/)
        * [kubeconfig (v1)](https://kubernetes.io/docs/reference/config-api/kubeconfig.v1/)
        * [Kubelet Configuration (v1)](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1/)
        * [Kubelet Configuration (v1alpha1)](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1alpha1/)
        * [Kubelet Configuration (v1beta1)](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1beta1/)
        * [Kubelet CredentialProvider (v1)](https://kubernetes.io/docs/reference/config-api/kubelet-credentialprovider.v1/)
        * [kuberc (v1alpha1)](https://kubernetes.io/docs/reference/config-api/kuberc.v1alpha1/)
        * [kuberc (v1beta1)](https://kubernetes.io/docs/reference/config-api/kuberc.v1beta1/)
        * [WebhookAdmission Configuration (v1)](https://kubernetes.io/docs/reference/config-api/apiserver-webhookadmission.v1/)
      * [External APIs](https://kubernetes.io/docs/reference/external-api/)
        * [Kubernetes Custom Metrics (v1beta2)](https://kubernetes.io/docs/reference/external-api/custom-metrics.v1beta2/)
        * [Kubernetes External Metrics (v1beta1)](https://kubernetes.io/docs/reference/external-api/external-metrics.v1beta1/)
        * [Kubernetes Metrics (v1beta1)](https://kubernetes.io/docs/reference/external-api/metrics.v1beta1/)
      * [Scheduling](https://kubernetes.io/docs/reference/scheduling/)
        * [Scheduler Configuration](https://kubernetes.io/docs/reference/scheduling/config/)
        * [Scheduling Policies](https://kubernetes.io/docs/reference/scheduling/policies/)
      * [Other Tools](https://kubernetes.io/docs/reference/tools/)
    * [Contribute](https://kubernetes.io/docs/contribute/ "Contribute to Kubernetes")
      * [Contribute to Kubernetes Documentation](https://kubernetes.io/docs/contribute/docs/)
      * [Contributing to Kubernetes blogs](https://kubernetes.io/docs/contribute/blog/)
        * [Submitting articles to Kubernetes blogs](https://kubernetes.io/docs/contribute/blog/article-submission/)
        * [Blog guidelines](https://kubernetes.io/docs/contribute/blog/guidelines/)
        * [Blog article mirroring](https://kubernetes.io/docs/contribute/blog/article-mirroring/)
        * [Post-release communications](https://kubernetes.io/docs/contribute/blog/release-comms/)
        * [Helping as a blog writing buddy](https://kubernetes.io/docs/contribute/blog/writing-buddy/)
      * [Suggesting content improvements](https://kubernetes.io/docs/contribute/suggesting-improvements/)
      * [Contributing new content](https://kubernetes.io/docs/contribute/new-content/)
        * [Opening a pull request](https://kubernetes.io/docs/contribute/new-content/open-a-pr/)
        * [Previewing locally](https://kubernetes.io/docs/contribute/new-content/preview-locally/)
        * [Documenting for a release](https://kubernetes.io/docs/contribute/new-content/new-features/ "Documenting a feature for a release")
        * [Case studies](https://kubernetes.io/docs/contribute/new-content/case-studies/ "Submitting case studies")
      * [Reviewing changes](https://kubernetes.io/docs/contribute/review/)
        * [Reviewing pull requests](https://kubernetes.io/docs/contribute/review/reviewing-prs/)
        * [For approvers and reviewers](https://kubernetes.io/docs/contribute/review/for-approvers/ "Reviewing for approvers and reviewers")
      * [Localizing Kubernetes documentation](https://kubernetes.io/docs/contribute/localization/)
      * [Participating in SIG Docs](https://kubernetes.io/docs/contribute/participate/)
        * [Roles and responsibilities](https://kubernetes.io/docs/contribute/participate/roles-and-responsibilities/)
        * [Issue Wranglers](https://kubernetes.io/docs/contribute/participate/issue-wrangler/)
        * [PR wranglers](https://kubernetes.io/docs/contribute/participate/pr-wranglers/)
      * [Documentation style overview](https://kubernetes.io/docs/contribute/style/)
        * [Content guide](https://kubernetes.io/docs/contribute/style/content-guide/ "Documentation Content Guide")
        * [Style guide](https://kubernetes.io/docs/contribute/style/style-guide/ "Documentation Style Guide")
        * [Diagram guide](https://kubernetes.io/docs/contribute/style/diagram-guide/ "Diagram Guide")
        * [Writing a new topic](https://kubernetes.io/docs/contribute/style/write-new-topic/)
        * [Page content types](https://kubernetes.io/docs/contribute/style/page-content-types/)
        * [Content organization](https://kubernetes.io/docs/contribute/style/content-organization/)
        * [Custom Hugo Shortcodes](https://kubernetes.io/docs/contribute/style/hugo-shortcodes/)
      * [Updating Reference Documentation](https://kubernetes.io/docs/contribute/generate-ref-docs/)
        * [Quickstart](https://kubernetes.io/docs/contribute/generate-ref-docs/quickstart/ "Reference Documentation Quickstart")
        * [Contributing to the Upstream Kubernetes Code](https://kubernetes.io/docs/contribute/generate-ref-docs/contribute-upstream/)
        * [Generating Reference Documentation for the Kubernetes API](https://kubernetes.io/docs/contribute/generate-ref-docs/kubernetes-api/)
        * [Generating Reference Documentation for kubectl Commands](https://kubernetes.io/docs/contribute/generate-ref-docs/kubectl/)
        * [Generating Reference Documentation for Metrics](https://kubernetes.io/docs/contribute/generate-ref-docs/metrics-reference/)
        * [Generating Reference Pages for Kubernetes Components and Tools](https://kubernetes.io/docs/contribute/generate-ref-docs/kubernetes-components/)
        * [](https://kubernetes.io/docs/contribute/generate-ref-docs/prerequisites-ref-docs/)
      * [Advanced contributing](https://kubernetes.io/docs/contribute/advanced/)
      * [Viewing Site Analytics](https://kubernetes.io/docs/contribute/analytics/)
    * [Docs smoke test page](https://kubernetes.io/docs/test/)



[ __Edit this page](https://github.com/kubernetes/website/edit/main/content/en/docs/reference/access-authn-authz/admission-controllers.md) [__Create child page](https://github.com/kubernetes/website/new/main/content/en/docs/reference/access-authn-authz/admission-controllers.md?filename=change-me.md&value=---%0Atitle%3A+%22Long+Page+Title%22%0AlinkTitle%3A+%22Short+Nav+Title%22%0Aweight%3A+100%0Adescription%3A+%3E-%0A+++++Page+description+for+heading+and+indexes.%0A---%0A%0A%23%23+Heading%0A%0AEdit+this+template+to+create+your+new+page.%0A%0A%2A+Give+it+a+good+name%2C+ending+in+%60.md%60+-+e.g.+%60getting-started.md%60%0A%2A+Edit+the+%22front+matter%22+section+at+the+top+of+the+page+%28weight+controls+how+its+ordered+amongst+other+pages+in+the+same+directory%3B+lowest+number+first%29.%0A%2A+Add+a+good+commit+message+at+the+bottom+of+the+page+%28%3C80+characters%3B+use+the+extended+description+field+for+more+detail%29.%0A%2A+Create+a+new+branch+so+you+can+preview+your+new+file+and+request+a+review+via+Pull+Request.%0A) [__Create an issue](https://github.com/kubernetes/website/issues/new?title=Admission%20Control%20in%20Kubernetes) [__Print entire section](https://kubernetes.io/docs/reference/access-authn-authz/_print/)

  * What are they?
    * Admission control extension points
    * Admission control phases
  * Why do I need them?
  * How do I turn on an admission controller?
  * How do I turn off an admission controller?
  * Which plugins are enabled by default?
  * What does each admission controller do?
    * AlwaysAdmit
    * AlwaysDeny
    * AlwaysPullImages
    * CertificateApproval
    * CertificateSigning
    * CertificateSubjectRestriction
    * DefaultIngressClass
    * DefaultStorageClass
    * DefaultTolerationSeconds
    * DenyServiceExternalIPs
    * EventRateLimit
    * ExtendedResourceToleration
    * ImagePolicyWebhook
    * LimitPodHardAntiAffinityTopology
    * LimitRanger
    * MutatingAdmissionWebhook
    * NamespaceAutoProvision
    * NamespaceExists
    * NamespaceLifecycle
    * NodeDeclaredFeatureValidator
    * NodeRestriction
    * OwnerReferencesPermissionEnforcement
    * PersistentVolumeClaimResize
    * PodNodeSelector
    * PodSecurity
    * PodTolerationRestriction
    * PodTopologyLabels
    * Priority
    * ResourceQuota
    * RuntimeClass
    * ServiceAccount
    * StorageObjectInUseProtection
    * TaintNodesByCondition
    * ValidatingAdmissionPolicy
    * ValidatingAdmissionWebhook
  * Is there a recommended set of admission controllers to use?



  1. [Kubernetes Documentation](https://kubernetes.io/docs/)
  2. [Reference](https://kubernetes.io/docs/reference/)
  3. [API Access Control](https://kubernetes.io/docs/reference/access-authn-authz/)
  4. Admission Control



# Admission Control in Kubernetes

This page provides an overview of _admission controllers_.

An admission controller is a piece of code that intercepts requests to the Kubernetes API server prior to persistence of the resource, but after the request is authenticated and authorized.

Several important features of Kubernetes require an admission controller to be enabled in order to properly support the feature. As a result, a Kubernetes API server that is not properly configured with the right set of admission controllers is an incomplete server that will not support all the features you expect.

## What are they?

Admission controllers are code within the Kubernetes [API server](https://kubernetes.io/docs/concepts/architecture/#kube-apiserver "Control plane component that serves the Kubernetes API.") that check the data arriving in a request to modify a resource.

Admission controllers apply to requests that create, delete, or modify objects. Admission controllers can also block custom verbs, such as a request to connect to a pod via an API server proxy. Admission controllers do _not_ (and cannot) block requests to read (**get** , **watch** or **list**) objects, because reads bypass the admission control layer.

Admission control mechanisms may be _validating_ , _mutating_ , or both. Mutating controllers may modify the data for the resource being modified; validating controllers may not.

The admission controllers in Kubernetes 1.36 consist of the list below, are compiled into the `kube-apiserver` binary, and may only be configured by the cluster administrator.

### Admission control extension points

Within the full list, there are three special controllers: MutatingAdmissionWebhook, ValidatingAdmissionWebhook, and ValidatingAdmissionPolicy. The two webhook controllers execute the mutating and validating (respectively) [admission control webhooks](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#admission-webhooks) which are configured in the API. ValidatingAdmissionPolicy provides a way to embed declarative validation code within the API, without relying on any external HTTP callouts.

You can use these three admission controllers to customize cluster behavior at admission time.

### Admission control phases

The admission control process proceeds in two phases. In the first phase, mutating admission controllers are run. In the second phase, validating admission controllers are run. Note again that some of the controllers are both.

If any of the controllers in either phase reject the request, the entire request is rejected immediately and an error is returned to the end-user.

Finally, in addition to sometimes mutating the object in question, admission controllers may sometimes have side effects, that is, mutate related resources as part of request processing. Incrementing quota usage is the canonical example of why this is necessary. Any such side-effect needs a corresponding reclamation or reconciliation process, as a given admission controller does not know for sure that a given request will pass all of the other admission controllers.

The ordering of these calls can be seen below.

![Sequence diagram for kube-apiserver handling requests during the admission phase showing mutation webhooks, followed by validatingadmissionpolicies and finally validating webhooks. It shows that the continue until the first rejection, or being accepted by all of them. It also shows that mutations by mutating webhooks cause all previously called webhooks to be called again.](https://kubernetes.io/docs/reference/access-authn-authz/admission-control-phases.svg)

## Why do I need them?

Several important features of Kubernetes require an admission controller to be enabled in order to properly support the feature. As a result, a Kubernetes API server that is not properly configured with the right set of admission controllers is an incomplete server and will not support all the features you expect.

## How do I turn on an admission controller?

The Kubernetes API server flag `enable-admission-plugins` takes a comma-delimited list of admission control plugins to invoke prior to modifying objects in the cluster. For example, the following command line enables the `NamespaceLifecycle` and the `LimitRanger` admission control plugins:
    
    
    kube-apiserver --enable-admission-plugins=NamespaceLifecycle,LimitRanger ...
    

#### Note:

Depending on the way your Kubernetes cluster is deployed and how the API server is started, you may need to apply the settings in different ways. For example, you may have to modify the systemd unit file if the API server is deployed as a systemd service, you may modify the manifest file for the API server if Kubernetes is deployed in a self-hosted way.

## How do I turn off an admission controller?

The Kubernetes API server flag `disable-admission-plugins` takes a comma-delimited list of admission control plugins to be disabled, even if they are in the list of plugins enabled by default.
    
    
    kube-apiserver --disable-admission-plugins=PodNodeSelector,AlwaysDeny ...
    

## Which plugins are enabled by default?

To see which admission plugins are enabled:
    
    
    kube-apiserver -h | grep enable-admission-plugins
    

In Kubernetes 1.36, the default ones are:
    
    
    CertificateApproval, CertificateSigning, CertificateSubjectRestriction, DefaultIngressClass, DefaultStorageClass, DefaultTolerationSeconds, LimitRanger, MutatingAdmissionWebhook, NamespaceLifecycle, PersistentVolumeClaimResize, PodSecurity, Priority, ResourceQuota, RuntimeClass, ServiceAccount, StorageObjectInUseProtection, TaintNodesByCondition, ValidatingAdmissionPolicy, ValidatingAdmissionWebhook
    

## What does each admission controller do?

### AlwaysAdmit

FEATURE STATE: `Kubernetes v1.13 [deprecated]`

**Type** : Validating.

This admission controller allows all pods into the cluster. It is **deprecated** because its behavior is the same as if there were no admission controller at all.

### AlwaysDeny

FEATURE STATE: `Kubernetes v1.13 [deprecated]`

**Type** : Validating.

Rejects all requests. AlwaysDeny is **deprecated** as it has no real meaning.

### AlwaysPullImages

**Type** : Mutating and Validating.

This admission controller modifies every new Pod to force the image pull policy to `Always`. This is useful in a multitenant cluster so that users can be assured that their private images can only be used by those who have the credentials to pull them. Without this admission controller, once an image has been pulled to a node, any pod from any user can use it by knowing the image's name (assuming the Pod is scheduled onto the right node), without any authorization check against the image. When this admission controller is enabled, images are always pulled prior to starting containers, which means valid credentials are required.

### CertificateApproval

**Type** : Validating.

This admission controller observes requests to approve CertificateSigningRequest resources and performs additional authorization checks to ensure the approving user has permission to **approve** certificate requests with the `spec.signerName` requested on the CertificateSigningRequest resource.

See [Certificate Signing Requests](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/) for more information on the permissions required to perform different actions on CertificateSigningRequest resources.

### CertificateSigning

**Type** : Validating.

This admission controller observes updates to the `status.certificate` field of CertificateSigningRequest resources and performs an additional authorization checks to ensure the signing user has permission to **sign** certificate requests with the `spec.signerName` requested on the CertificateSigningRequest resource.

See [Certificate Signing Requests](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/) for more information on the permissions required to perform different actions on CertificateSigningRequest resources.

### CertificateSubjectRestriction

**Type** : Validating.

This admission controller observes creation of CertificateSigningRequest resources that have a `spec.signerName` of `kubernetes.io/kube-apiserver-client`. It rejects any request that specifies a 'group' (or 'organization attribute') of `system:masters`.

### DefaultIngressClass

**Type** : Mutating.

This admission controller observes creation of `Ingress` objects that do not request any specific ingress class and automatically adds a default ingress class to them. This way, users that do not request any special ingress class do not need to care about them at all and they will get the default one.

This admission controller does not do anything when no default ingress class is configured. When more than one ingress class is marked as default, it rejects any creation of `Ingress` with an error and an administrator must revisit their `IngressClass` objects and mark only one as default (with the annotation "ingressclass.kubernetes.io/is-default-class"). This admission controller ignores any `Ingress` updates; it acts only on creation.

See the [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) documentation for more about ingress classes and how to mark one as default.

### DefaultStorageClass

**Type** : Mutating.

This admission controller observes creation of `PersistentVolumeClaim` objects that do not request any specific storage class and automatically adds a default storage class to them. This way, users that do not request any special storage class do not need to care about them at all and they will get the default one.

This admission controller does nothing when no default `StorageClass` exists. When more than one storage class is marked as default, and you then create a `PersistentVolumeClaim` with no `storageClassName` set, Kubernetes uses the most recently created default `StorageClass`. When a `PersistentVolumeClaim` is created with a specified `volumeName`, it remains in a pending state if the static volume's `storageClassName` does not match the `storageClassName` on the `PersistentVolumeClaim` after any default StorageClass is applied to it. This admission controller ignores any `PersistentVolumeClaim` updates; it acts only on creation.

See [persistent volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) documentation about persistent volume claims and storage classes and how to mark a storage class as default.

### DefaultTolerationSeconds

**Type** : Mutating.

This admission controller sets the default forgiveness toleration for pods to tolerate the taints `notready:NoExecute` and `unreachable:NoExecute` based on the k8s-apiserver input parameters `default-not-ready-toleration-seconds` and `default-unreachable-toleration-seconds` if the pods don't already have toleration for taints `node.kubernetes.io/not-ready:NoExecute` or `node.kubernetes.io/unreachable:NoExecute`. The default value for `default-not-ready-toleration-seconds` and `default-unreachable-toleration-seconds` is 5 minutes.

### DenyServiceExternalIPs

**Type** : Validating.

This admission controller rejects all net-new usage of the `Service` field `externalIPs`. This feature is very powerful (allows network traffic interception) and not well controlled by policy. When enabled, users of the cluster may not create new Services which use `externalIPs` and may not add new values to `externalIPs` on existing `Service` objects. Existing uses of `externalIPs` are not affected, and users may remove values from `externalIPs` on existing `Service` objects.

Most users do not need this feature at all, and cluster admins should consider disabling it. Clusters that do need to use this feature should consider using some custom policy to manage usage of it.

This admission controller is disabled by default.

### EventRateLimit

FEATURE STATE: `Kubernetes v1.13 [alpha]`

**Type** : Validating.

This admission controller mitigates the problem where the API server gets flooded by requests to store new Events. The cluster admin can specify event rate limits by:

  * Enabling the `EventRateLimit` admission controller;
  * Referencing an `EventRateLimit` configuration file from the file provided to the API server's command line flag `--admission-control-config-file`:


    
    
    apiVersion: apiserver.config.k8s.io/v1
    kind: AdmissionConfiguration
    plugins:
      - name: EventRateLimit
        path: eventconfig.yaml
    ...
    

There are four types of limits that can be specified in the configuration:

  * `Server`: All Event requests (creation or modifications) received by the API server share a single bucket.
  * `Namespace`: Each namespace has a dedicated bucket.
  * `User`: Each user is allocated a bucket.
  * `SourceAndObject`: A bucket is assigned by each combination of source and involved object of the event.



Below is a sample `eventconfig.yaml` for such a configuration:
    
    
    apiVersion: eventratelimit.admission.k8s.io/v1alpha1
    kind: Configuration
    limits:
      - type: Namespace
        qps: 50
        burst: 100
        cacheSize: 2000
      - type: User
        qps: 10
        burst: 50
    

See the [EventRateLimit Config API (v1alpha1)](https://kubernetes.io/docs/reference/config-api/apiserver-eventratelimit.v1alpha1/) for more details.

This admission controller is disabled by default.

### ExtendedResourceToleration

**Type** : Mutating.

This plug-in facilitates creation of dedicated nodes with extended resources. If operators want to create dedicated nodes with extended resources (like GPUs, FPGAs etc.), they are expected to [taint the node](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#example-use-cases) with the extended resource name as the key. This admission controller, if enabled, automatically adds tolerations for such taints to pods requesting extended resources, so users don't have to manually add these tolerations.

This admission controller is disabled by default.

### ImagePolicyWebhook

**Type** : Validating.

The ImagePolicyWebhook admission controller allows a backend webhook to make admission decisions.

This admission controller is disabled by default.

#### Configuration file format

ImagePolicyWebhook uses a configuration file to set options for the behavior of the backend. This file may be json or yaml and has the following format:
    
    
    imagePolicy:
      kubeConfigFile: /path/to/kubeconfig/for/backend
      # time in s to cache approval
      allowTTL: 50
      # time in s to cache denial
      denyTTL: 50
      # time in ms to wait between retries
      retryBackoff: 500
      # determines behavior if the webhook backend fails
      defaultAllow: true
    

Reference the ImagePolicyWebhook configuration file from the file provided to the API server's command line flag `--admission-control-config-file`:
    
    
    apiVersion: apiserver.config.k8s.io/v1
    kind: AdmissionConfiguration
    plugins:
      - name: ImagePolicyWebhook
        path: imagepolicyconfig.yaml
    ...
    

Alternatively, you can embed the configuration directly in the file:
    
    
    apiVersion: apiserver.config.k8s.io/v1
    kind: AdmissionConfiguration
    plugins:
      - name: ImagePolicyWebhook
        configuration:
          imagePolicy:
            kubeConfigFile: <path-to-kubeconfig-file>
            allowTTL: 50
            denyTTL: 50
            retryBackoff: 500
            defaultAllow: true
    

The ImagePolicyWebhook config file must reference a [kubeconfig](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) formatted file which sets up the connection to the backend. It is required that the backend communicate over TLS.

The kubeconfig file's `cluster` field must point to the remote service, and the `user` field must contain the returned authorizer.
    
    
    # clusters refers to the remote service.
    clusters:
      - name: name-of-remote-imagepolicy-service
        cluster:
          certificate-authority: /path/to/ca.pem    # CA for verifying the remote service.
          server: https://images.example.com/policy # URL of remote service to query. Must use 'https'.
    
    # users refers to the API server's webhook configuration.
    users:
      - name: name-of-api-server
        user:
          client-certificate: /path/to/cert.pem # cert for the webhook admission controller to use
          client-key: /path/to/key.pem          # key matching the cert
    

For additional HTTP configuration, refer to the [kubeconfig](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) documentation.

#### Request payloads

When faced with an admission decision, the API Server POSTs a JSON serialized `imagepolicy.k8s.io/v1alpha1` `ImageReview` object describing the action. This object contains fields describing the containers being admitted, as well as any pod annotations that match `*.image-policy.k8s.io/*`.

#### Note:

The webhook API objects are subject to the same versioning compatibility rules as other Kubernetes API objects. Implementers should be aware of looser compatibility promises for alpha objects and check the `apiVersion` field of the request to ensure correct deserialization. Additionally, the API Server must enable the `imagepolicy.k8s.io/v1alpha1` API extensions group (`--runtime-config=imagepolicy.k8s.io/v1alpha1=true`).

An example request body:
    
    
    {
      "apiVersion": "imagepolicy.k8s.io/v1alpha1",
      "kind": "ImageReview",
      "spec": {
        "containers": [
          {
            "image": "myrepo/myimage:v1"
          },
          {
            "image": "myrepo/myimage@sha256:beb6bd6a68f114c1dc2ea4b28db81bdf91de202a9014972bec5e4d9171d90ed"
          }
        ],
        "annotations": {
          "mycluster.image-policy.k8s.io/ticket-1234": "break-glass"
        },
        "namespace": "mynamespace"
      }
    }
    

The remote service is expected to fill the `status` field of the request and respond to either allow or disallow access. The response body's `spec` field is ignored, and may be omitted. A permissive response would return:
    
    
    {
      "apiVersion": "imagepolicy.k8s.io/v1alpha1",
      "kind": "ImageReview",
      "status": {
        "allowed": true
      }
    }
    

To disallow access, the service would return:
    
    
    {
      "apiVersion": "imagepolicy.k8s.io/v1alpha1",
      "kind": "ImageReview",
      "status": {
        "allowed": false,
        "reason": "image currently blacklisted"
      }
    }
    

#### Note:

`ImageReview` objects will include all images in Pods intended to be executed as containers. This covers images specified as part of the containers, initContainers, or ephemeralContainers fields in a Pod specification. As a result, images included under image volumes are not in scope for the ImagePolicyWebhook.

For further documentation refer to the [`imagepolicy.v1alpha1` API](https://kubernetes.io/docs/reference/config-api/imagepolicy.v1alpha1/).

#### Extending with Annotations

All annotations on a Pod that match `*.image-policy.k8s.io/*` are sent to the webhook. Sending annotations allows users who are aware of the image policy backend to send extra information to it, and for different backends implementations to accept different information.

Examples of information you might put here are:

  * request to "break glass" to override a policy, in case of emergency.
  * a ticket number from a ticket system that documents the break-glass request
  * provide a hint to the policy server as to the imageID of the image being provided, to save it a lookup



In any case, the annotations are provided by the user and are not validated by Kubernetes in any way.

### LimitPodHardAntiAffinityTopology

**Type** : Validating.

This admission controller denies any pod that defines an `AntiAffinity` topology key other than `kubernetes.io/hostname` in `requiredDuringSchedulingIgnoredDuringExecution`.

This admission controller is disabled by default.

### LimitRanger

**Type** : Mutating and Validating.

This admission controller will observe the incoming request and ensure that it does not violate any of the constraints enumerated in the `LimitRange` object in a `Namespace`. If you are using `LimitRange` objects in your Kubernetes deployment, you MUST use this admission controller to enforce those constraints. LimitRanger can also be used to apply default resource requests to Pods that don't specify any; currently, the default LimitRanger applies a 0.1 CPU requirement to all Pods in the `default` namespace.

See the [LimitRange API reference](https://kubernetes.io/docs/reference/kubernetes-api/policy-resources/limit-range-v1/) and the [example of LimitRange](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/) for more details.

### MutatingAdmissionWebhook

**Type** : Mutating.

This admission controller calls any mutating webhooks which match the request. Matching webhooks are called in serial; each one may modify the object if it desires.

This admission controller (as implied by the name) only runs in the mutating phase.

If a webhook called by this has side effects (for example, decrementing quota) it _must_ have a reconciliation system, as it is not guaranteed that subsequent webhooks or validating admission controllers will permit the request to finish.

If you disable the MutatingAdmissionWebhook, you must also disable the `MutatingWebhookConfiguration` object in the `admissionregistration.k8s.io/v1` group/version via the `--runtime-config` flag, both are on by default.

#### Use caution when authoring and installing mutating webhooks

  * Users may be confused when the objects they try to create are different from what they get back.
  * Built in control loops may break when the objects they try to create are different when read back.
    * Setting originally unset fields is less likely to cause problems than overwriting fields set in the original request. Avoid doing the latter.
  * Future changes to control loops for built-in resources or third-party resources may break webhooks that work well today. Even when the webhook installation API is finalized, not all possible webhook behaviors will be guaranteed to be supported indefinitely.



### NamespaceAutoProvision

**Type** : Mutating.

This admission controller examines all incoming requests on namespaced resources and checks if the referenced namespace does exist. It creates a namespace if it cannot be found. This admission controller is useful in deployments that do not want to restrict creation of a namespace prior to its usage.

### NamespaceExists

**Type** : Validating.

This admission controller checks all requests on namespaced resources other than `Namespace` itself. If the namespace referenced from a request doesn't exist, the request is rejected.

### NamespaceLifecycle

**Type** : Validating.

This admission controller enforces that a `Namespace` that is undergoing termination cannot have new objects created in it, and ensures that requests in a non-existent `Namespace` are rejected. This admission controller also prevents deletion of three system reserved namespaces `default`, `kube-system`, `kube-public`.

A `Namespace` deletion kicks off a sequence of operations that remove all objects (pods, services, etc.) in that namespace. In order to enforce integrity of that process, we strongly recommend running this admission controller.

### NodeDeclaredFeatureValidator

FEATURE STATE: `Kubernetes v1.36 [beta]`(enabled by default)

**Type** : Validating.

This admission controller intercepts writes to bound Pods, to ensure that the changes are compatible with the features declared by the node where the Pod is currently running. It uses the `.status.declaredFeatures` field of the Node to determine the set of enabled features. If a Pod update requires a feature that is not listed in the features of its current node, the admission controller will reject the update request. This prevents runtime failures due to feature mismatch after a Pod has been scheduled.

This admission controller is enabled by default if the [`NodeDeclaredFeatures`](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#NodeDeclaredFeatures) feature gate is enabled.

### NodeRestriction

**Type** : Validating.

This admission controller limits the `Node` and `Pod` objects a kubelet can modify. In order to be limited by this admission controller, kubelets must use credentials in the `system:nodes` group, with a username in the form `system:node:<nodeName>`. Such kubelets will only be allowed to modify their own `Node` API object, and only modify `Pod` API objects that are bound to their node. kubelets are not allowed to update or remove taints from their `Node` API object.

The `NodeRestriction` admission plugin prevents kubelets from deleting their `Node` API object, and enforces kubelet modification of labels under the `kubernetes.io/` or `k8s.io/` prefixes as follows:

  * **Forbidden** (Kubelets are blocked from modifying these):
    * Labels with a `node-restriction.kubernetes.io/` prefix. This prefix is reserved for administrators to label `Node` objects for workload isolation.
    * Labels with a `node-role.kubernetes.io/` prefix (for example: `node-role.kubernetes.io/control-plane`). These are restricted to prevent unprivileged nodes from self-declaring cluster roles.
  * **Allowed** (Kubelets can add/remove/update these):
    * `kubernetes.io/hostname`
    * `kubernetes.io/arch`
    * `kubernetes.io/os`
    * `beta.kubernetes.io/instance-type`
    * `node.kubernetes.io/instance-type`
    * `failure-domain.beta.kubernetes.io/region` (deprecated)
    * `failure-domain.beta.kubernetes.io/zone` (deprecated)
    * `topology.kubernetes.io/region`
    * `topology.kubernetes.io/zone`
    * `kubelet.kubernetes.io/`-prefixed labels
    * `node.kubernetes.io/`-prefixed labels
  * **Reserved** : Use of any other labels under the `kubernetes.io` or `k8s.io` prefixes by kubelets is reserved. The `NodeRestriction` admission plugin generally disallows these to prevent unauthorized self-labeling, but may allow additional labels under these prefixes in the future as part of future features.



When the `ServiceAccountNodeAudienceRestriction` [feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) is enabled, this admission plugin also restricts the audiences for which a kubelet can request service account tokens via the `TokenRequest` API. The kubelet can only request tokens for audiences already referenced by pods on that node (through projected service account token volumes or CSI driver token requests), or for audiences explicitly granted through RBAC using the `request-serviceaccounts-token-audience` verb. For more details, see [Service account token audience restriction](https://kubernetes.io/docs/reference/access-authn-authz/node/#service-account-token-audience-restriction).

Future versions may add additional restrictions to ensure kubelets have the minimal set of permissions required to operate correctly.

### OwnerReferencesPermissionEnforcement

**Type** : Validating.

This admission controller protects the access to the `metadata.ownerReferences` of an object so that only users with **delete** permission to the object can change it. This admission controller also protects the access to `metadata.ownerReferences[x].blockOwnerDeletion` of an object, so that only users with **update** permission to the `finalizers` subresource of the referenced _owner_ can change it.

### PersistentVolumeClaimResize

FEATURE STATE: `Kubernetes v1.24 [stable]`

**Type** : Validating.

This admission controller implements additional validations for checking incoming `PersistentVolumeClaim` resize requests.

Enabling the `PersistentVolumeClaimResize` admission controller is recommended. This admission controller prevents resizing of all claims by default unless a claim's `StorageClass` explicitly enables resizing by setting `allowVolumeExpansion` to `true`.

For example: all `PersistentVolumeClaim`s created from the following `StorageClass` support volume expansion:
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: gluster-vol-default
    provisioner: kubernetes.io/glusterfs
    parameters:
      resturl: "http://192.168.10.100:8080"
      restuser: ""
      secretNamespace: ""
      secretName: ""
    allowVolumeExpansion: true
    

For more information about persistent volume claims, see [PersistentVolumeClaims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims).

### PodNodeSelector

FEATURE STATE: `Kubernetes v1.5 [alpha]`

**Type** : Validating.

This admission controller defaults and limits what node selectors may be used within a namespace by reading a namespace annotation and a global configuration.

This admission controller is disabled by default.

#### Configuration file format

`PodNodeSelector` uses a configuration file to set options for the behavior of the backend. Note that the configuration file format will move to a versioned file in a future release. This file may be json or yaml and has the following format:
    
    
    podNodeSelectorPluginConfig:
      clusterDefaultNodeSelector: name-of-node-selector
      namespace1: name-of-node-selector
      namespace2: name-of-node-selector
    

Reference the `PodNodeSelector` configuration file from the file provided to the API server's command line flag `--admission-control-config-file`:
    
    
    apiVersion: apiserver.config.k8s.io/v1
    kind: AdmissionConfiguration
    plugins:
    - name: PodNodeSelector
      path: podnodeselector.yaml
    ...
    

#### Configuration Annotation Format

`PodNodeSelector` uses the annotation key `scheduler.alpha.kubernetes.io/node-selector` to assign node selectors to namespaces.
    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      annotations:
        scheduler.alpha.kubernetes.io/node-selector: name-of-node-selector
      name: namespace3
    

#### Internal Behavior

This admission controller has the following behavior:

  1. If the `Namespace` has an annotation with a key `scheduler.alpha.kubernetes.io/node-selector`, use its value as the node selector.
  2. If the namespace lacks such an annotation, use the `clusterDefaultNodeSelector` defined in the `PodNodeSelector` plugin configuration file as the node selector.
  3. Evaluate the pod's node selector against the namespace node selector for conflicts. Conflicts result in rejection.
  4. Evaluate the pod's node selector against the namespace-specific allowed selector defined the plugin configuration file. Conflicts result in rejection.



#### Note:

PodNodeSelector allows forcing pods to run on specifically labeled nodes. Also see the PodTolerationRestriction admission plugin, which allows preventing pods from running on specifically tainted nodes.

### PodSecurity

FEATURE STATE: `Kubernetes v1.25 [stable]`

**Type** : Validating.

The PodSecurity admission controller checks new Pods before they are admitted, determines if it should be admitted based on the requested security context and the restrictions on permitted [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) for the namespace that the Pod would be in.

See the [Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/) documentation for more information.

PodSecurity replaced an older admission controller named PodSecurityPolicy.

### PodTolerationRestriction

FEATURE STATE: `Kubernetes v1.7 [alpha]`

**Type** : Mutating and Validating.

The PodTolerationRestriction admission controller verifies any conflict between tolerations of a pod and the tolerations of its namespace. It rejects the pod request if there is a conflict. It then merges the tolerations annotated on the namespace into the tolerations of the pod. The resulting tolerations are checked against a list of allowed tolerations annotated to the namespace. If the check succeeds, the pod request is admitted otherwise it is rejected.

If the namespace of the pod does not have any associated default tolerations or allowed tolerations annotated, the cluster-level default tolerations or cluster-level list of allowed tolerations are used instead if they are specified.

Tolerations to a namespace are assigned via the `scheduler.alpha.kubernetes.io/defaultTolerations` annotation key. The list of allowed tolerations can be added via the `scheduler.alpha.kubernetes.io/tolerationsWhitelist` annotation key.

Example for namespace annotations:
    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      name: apps-that-need-nodes-exclusively
      annotations:
        scheduler.alpha.kubernetes.io/defaultTolerations: '[{"operator": "Exists", "effect": "NoSchedule", "key": "dedicated-node"}]'
        scheduler.alpha.kubernetes.io/tolerationsWhitelist: '[{"operator": "Exists", "effect": "NoSchedule", "key": "dedicated-node"}]'
    

This admission controller is disabled by default.

### PodTopologyLabels

FEATURE STATE: `Kubernetes v1.35 [beta]`(enabled by default)

**Type** : Mutating

The PodTopologyLabels admission controller mutates the `pods/binding` subresources for all pods bound to a Node, adding topology labels matching those of the bound Node. This allows Node topology labels to be available as pod labels, which can be surfaced to running containers using the [Downward API](https://kubernetes.io/docs/concepts/workloads/pods/downward-api/). The labels available as a result of this controller are the [topology.kubernetes.io/region](https://kubernetes.io/docs/reference/labels-annotations-taints/#topologykubernetesioregion) and [topology.kuberentes.io/zone](https://kubernetes.io/docs/reference/labels-annotations-taints/#topologykubernetesiozone) labels.

#### Note:

If any mutating admission webhook adds or modifies labels of the `pods/binding` subresource, these changes will propagate to pod labels as a result of this controller, overwriting labels with conflicting keys.

This admission controller is enabled when the `PodTopologyLabelsAdmission` feature gate is enabled.

### Priority

**Type** : Mutating and Validating.

The priority admission controller uses the `priorityClassName` field and populates the integer value of the priority. If the priority class is not found, the Pod is rejected.

### ResourceQuota

**Type** : Validating.

This admission controller will observe the incoming request and ensure that it does not violate any of the constraints enumerated in the `ResourceQuota` object in a `Namespace`. If you are using `ResourceQuota` objects in your Kubernetes deployment, you MUST use this admission controller to enforce quota constraints.

See the [ResourceQuota API reference](https://kubernetes.io/docs/reference/kubernetes-api/policy-resources/resource-quota-v1/) and the [example of Resource Quota](https://kubernetes.io/docs/concepts/policy/resource-quotas/) for more details.

### RuntimeClass

**Type** : Mutating and Validating.

If you define a RuntimeClass with [Pod overhead](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-overhead/) configured, this admission controller checks incoming Pods. When enabled, this admission controller rejects any Pod create requests that have the overhead already set. For Pods that have a RuntimeClass configured and selected in their `.spec`, this admission controller sets `.spec.overhead` in the Pod based on the value defined in the corresponding RuntimeClass.

See also [Pod Overhead](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-overhead/) for more information.

### ServiceAccount

**Type** : Mutating and Validating.

This admission controller implements automation for [serviceAccounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/). The Kubernetes project strongly recommends enabling this admission controller. You should enable this admission controller if you intend to make any use of Kubernetes `ServiceAccount` objects.

To enhance the security measures around Secrets, use separate namespaces to isolate access to mounted secrets.

### StorageObjectInUseProtection

**Type** : Mutating.

The `StorageObjectInUseProtection` plugin adds the `kubernetes.io/pvc-protection` or `kubernetes.io/pv-protection` finalizers to newly created Persistent Volume Claims (PVCs) or Persistent Volumes (PV). In case a user deletes a PVC or PV the PVC or PV is not removed until the finalizer is removed from the PVC or PV by PVC or PV Protection Controller. Refer to the [Storage Object in Use Protection](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#storage-object-in-use-protection) for more detailed information.

### TaintNodesByCondition

**Type** : Mutating.

This admission controller [taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/ "A core object consisting of three required properties: key, value, and effect. Taints prevent the scheduling of pods on nodes or node groups.") newly created Nodes as `NotReady` and `NoSchedule`. That tainting avoids a race condition that could cause Pods to be scheduled on new Nodes before their taints were updated to accurately reflect their reported conditions.

### ValidatingAdmissionPolicy

**Type** : Validating.

[This admission controller](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/) implements the CEL validation for incoming matched requests. It is enabled when both feature gate `validatingadmissionpolicy` and `admissionregistration.k8s.io/v1alpha1` group/version are enabled. If any of the ValidatingAdmissionPolicy fails, the request fails.

### ValidatingAdmissionWebhook

**Type** : Validating.

This admission controller calls any validating webhooks which match the request. Matching webhooks are called in parallel; if any of them rejects the request, the request fails. This admission controller only runs in the validation phase; the webhooks it calls may not mutate the object, as opposed to the webhooks called by the `MutatingAdmissionWebhook` admission controller.

If a webhook called by this has side effects (for example, decrementing quota) it _must_ have a reconciliation system, as it is not guaranteed that subsequent webhooks or other validating admission controllers will permit the request to finish.

If you disable the ValidatingAdmissionWebhook, you must also disable the `ValidatingWebhookConfiguration` object in the `admissionregistration.k8s.io/v1` group/version via the `--runtime-config` flag.

## Is there a recommended set of admission controllers to use?

Yes. The recommended admission controllers are enabled by default (shown [here](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/#options)), so you do not need to explicitly specify them. You can enable additional admission controllers beyond the default set using the `--enable-admission-plugins` flag (**order doesn't matter**).

## Feedback

Was this page helpful?

Yes No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes). Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to [report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io) or [suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).

Last modified March 16, 2026 at 6:05 PM PST: [Add documentation for ServiceAccountNodeAudienceRestriction feature (65a8302b72)](https://github.com/kubernetes/website/commit/65a8302b72fc82fe7c15829462b2ac31891813ea)

  * [__](https://youtube.com/kubernetescommunity)
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



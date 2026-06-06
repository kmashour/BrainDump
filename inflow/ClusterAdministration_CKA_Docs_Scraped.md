# Consolidated Kubernetes Docs - Cluster Administration

This file is automatically scraped and consolidated by the ingestion pipeline.



# Source: https://kubernetes.io/docs/concepts/cluster-administration/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. Cluster Administration

# Cluster AdministrationLower-level detail relevant to creating or administering a Kubernetes cluster.

The cluster administration overview is for anyone creating or administering a Kubernetes cluster. It assumes some familiarity with core Kubernetes [concepts](https://kubernetes.io/docs/concepts/).

## Planning a cluster[](https://kubernetes.io/docs/concepts/cluster-administration/#planning-a-cluster)

See the guides in [Setup](https://kubernetes.io/docs/setup/) for examples of how to plan, set up, and configure Kubernetes clusters. The solutions listed in this article are called distros.

#### Note:Not all distros are actively maintained. Choose distros which have been tested with a recent version of Kubernetes.

Before choosing a guide, here are some considerations:
* Do you want to try out Kubernetes on your computer, or do you want to build a high-availability, multi-node cluster? Choose distros best suited for your needs.
* Will you be using a hosted Kubernetes cluster, such as [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/), or hosting your own cluster?
* Will your cluster be on-premises, or in the cloud (IaaS)? Kubernetes does not directly support hybrid clusters. Instead, you can set up multiple clusters.
* If you are configuring Kubernetes on-premises, consider which [networking model](https://kubernetes.io/docs/concepts/cluster-administration/networking/) fits best.
* Will you be running Kubernetes on "bare metal" hardware or on virtual machines (VMs)?
* Do you want to run a cluster, or do you expect to do active development of Kubernetes project code? If the latter, choose an actively-developed distro. Some distros only use binary releases, but offer a greater variety of choices.
* Familiarize yourself with the [components](https://kubernetes.io/docs/concepts/overview/components/) needed to run a cluster.

## Managing a cluster[](https://kubernetes.io/docs/concepts/cluster-administration/#managing-a-cluster)
* 

Learn how to [manage nodes](https://kubernetes.io/docs/concepts/architecture/nodes/).
  * Read about [Node autoscaling](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/).
* 

Learn how to set up and manage the [resource quota](https://kubernetes.io/docs/concepts/policy/resource-quotas/) for shared clusters.

## Securing a cluster[](https://kubernetes.io/docs/concepts/cluster-administration/#securing-a-cluster)
* 

[Generate Certificates](https://kubernetes.io/docs/tasks/administer-cluster/certificates/) describes the steps to generate certificates using different tool chains.
* 

[Kubernetes Container Environment](https://kubernetes.io/docs/concepts/containers/container-environment/) describes the environment for Kubelet managed containers on a Kubernetes node.
* 

[Controlling Access to the Kubernetes API](https://kubernetes.io/docs/concepts/security/controlling-access/) describes how Kubernetes implements access control for its own API.
* 

[Authenticating](https://kubernetes.io/docs/reference/access-authn-authz/authentication/) explains authentication in Kubernetes, including the various authentication options.
* 

[Authorization](https://kubernetes.io/docs/reference/access-authn-authz/authorization/) is separate from authentication, and controls how HTTP calls are handled.
* 

[Using Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) explains plug-ins which intercepts requests to the Kubernetes API server after authentication and authorization.
* 

[Admission Webhook Good Practices](https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/) provides good practices and considerations when designing mutating admission webhooks and validating admission webhooks.
* 

[Using Sysctls in a Kubernetes Cluster](https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/) describes to an administrator how to use the `sysctl` command-line tool to set kernel parameters .
* 

[Auditing](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/) describes how to interact with Kubernetes' audit logs.

### Securing the kubelet[](https://kubernetes.io/docs/concepts/cluster-administration/#securing-the-kubelet)
* [Control Plane-Node communication](https://kubernetes.io/docs/concepts/architecture/control-plane-node-communication/)
* [TLS bootstrapping](https://kubernetes.io/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/)
* [Kubelet authentication/authorization](https://kubernetes.io/docs/reference/access-authn-authz/kubelet-authn-authz/)

## Optional Cluster Services[](https://kubernetes.io/docs/concepts/cluster-administration/#optional-cluster-services)
* 

[DNS Integration](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/) describes how to resolve a DNS name directly to a Kubernetes service.
* 

[Logging and Monitoring Cluster Activity](https://kubernetes.io/docs/concepts/cluster-administration/logging/) explains how logging in Kubernetes works and how to implement it.

---



# Source: https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Cluster Administration](https://kubernetes.io/docs/concepts/cluster-administration/)
4. Node Shutdowns

# Node Shutdowns

In a Kubernetes cluster, a [node](https://kubernetes.io/docs/concepts/architecture/nodes/) can be shut down in a planned graceful way or unexpectedly because of reasons such as a power outage or something else external. A node shutdown could lead to workload failure if the node is not drained before the shutdown. A node shutdown can be either graceful or non-graceful.

#### Caution:

The `unattended-upgrades` package from Debian conflicts with node graceful shutdown in its normal configuration. If you use the default configuration of `unattended-upgrades`, which customizes the server shutdown grace period, then the kubelet fails to obtain the necessary lock to handle shutdown events properly.

This happens if the `shutdownGracePeriod` value is greater than 30 seconds. To avoid this, you can suppress part of the `unattended-upgrades` configuration, by making `/etc/systemd/logind.conf.d/unattended-upgrades-logind-maxdelay.conf` be a symbolic link to `/dev/null`.

For more details, refer to the [`logind.conf` documentation](https://www.freedesktop.org/software/systemd/man/latest/logind.conf.html).

## Graceful node shutdown[](https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/#graceful-node-shutdown)

The kubelet attempts to detect node system shutdown and terminates pods running on the node.

Kubelet ensures that pods follow the normal [pod termination process](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination) during the node shutdown. During node shutdown, the kubelet does not accept new Pods (even if those Pods are already bound to the node).

### Enabling graceful node shutdown[](https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/#enabling-graceful-node-shutdown)
*  Linux
*  Windows
FEATURE STATE: `Kubernetes v1.21 [beta]`(enabled by default)

On Linux, the graceful node shutdown feature is controlled with the `GracefulNodeShutdown` [feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) which is enabled by default in 1.21.

#### Note:The graceful node shutdown feature depends on systemd since it takes advantage of [systemd inhibitor locks](https://www.freedesktop.org/wiki/Software/systemd/inhibit/) to delay the node shutdown with a given duration.

---



# Source: https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Cluster Administration](https://kubernetes.io/docs/concepts/cluster-administration/)
4. Swap memory management

# Swap memory management

Kubernetes can be configured to use swap memory on a [node](https://kubernetes.io/docs/concepts/architecture/nodes/), allowing the kernel to free up physical memory by swapping out pages to backing storage. This is useful for multiple use-cases. For example, nodes running workloads that can benefit from using swap, such as those that have large memory footprints but only access a portion of that memory at any given time. It also helps prevent Pods from being terminated during memory pressure spikes, shields nodes from system-level memory spikes that might compromise its stability, allows for more flexible memory management on the node, and much more.

To learn about configuring swap in your cluster, read [Configuring swap memory on Kubernetes nodes](https://kubernetes.io/docs/tutorials/cluster-management/provision-swap-memory/).

## Operating system support[](https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/#operating-system-support)
* Linux nodes support swap; you need to configure each node to enable it. By default, the kubelet will not start on a Linux node that has swap enabled.
* Windows nodes require swap space. By default, the kubelet does not start on a Windows node that has swap disabled.

## How does it work?[](https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/#how-does-it-work)

There are a number of possible ways that one could envision swap use on a node. If kubelet is already running on a node, it would need to be restarted after swap is provisioned in order to identify it.

When kubelet starts on a node in which swap is provisioned and available (with the `failSwapOn: false` configuration), kubelet will:
* Be able to start on this swap-enabled node.
* Direct the Container Runtime Interface (CRI) implementation, often referred to as the container runtime, to allocate zero swap memory to Kubernetes workloads by default.

Swap configuration on a node is exposed to a cluster admin via the [`memorySwap` in the KubeletConfiguration](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1/). As a cluster administrator, you can specify the node's behaviour in the presence of swap memory by setting `memorySwap.swapBehavior`.

### Swap behaviors[](https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/#swap-behaviors)

You need to pick a [swap behavior](https://kubernetes.io/docs/reference/node/swap-behavior/) to use. Different nodes in your cluster can use different swap behaviors.

The swap behaviors you can choose for Linux nodes are:`NoSwap` (default)Workloads running as Pods on this node do not and cannot use swap.`LimitedSwap`Kubernetes workloads can utilize swap memory.

#### Note:

If you choose the NoSwap behavior, and you configure the kubelet to tolerate swap space (`failSwapOn: false`), then your workloads don't use any swap.

However, processes outside of Kubernetes-managed containers, such as systemi services (and even the kubelet itself!) can utilize swap.

You can read [configuring swap memory on Kubernetes nodes](https://kubernetes.io/docs/tutorials/cluster-management/provision-swap-memory/) to learn about enabling swap for your cluster.

### Container runtime integration[](https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/#container-runtime-integration)

The kubelet uses the container runtime API, and directs the container runtime to apply specific configuration (for example, in the cgroup v2 case, `memory.swap.max`) in a manner that will enable the desired swap configuration for a container. For runtimes that use control groups, or cgroups, the container runtime is then responsible for writing these settings to the container-level cgroup.

## Observability for swap use[](https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/#observability-for-swap-use)

### Node and container level metric statistics[](https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/#node-and-container-level-metric-statistics)

Kubelet now collects node and container level metric statistics, which can be accessed at the `/metrics/resource` (which is used mainly by monitoring tools like Prometheus) and `/stats/summary` (which is used mainly by Autoscalers) kubelet HTTP endpoints. This allows clients who can directly request the kubelet to monitor swap usage and remaining swap memory when using `LimitedSwap`. Additionally, a `machine_swap_bytes` metric has been added to cadvisor to show the total physical swap capacity of the machine. See [this page](https://kubernetes.io/docs/reference/instrumentation/node-metrics/) for more info.

For example, these `/metrics/resource` are supported:
* `node_swap_usage_bytes`: Current swap usage of the node in bytes.
* `container_swap_usage_bytes`: Current amount of the container swap usage in bytes.
* `container_swap_limit_bytes`: Current amount of the container swap limit in bytes.

### Using `kubectl top --show-swap`[](https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/#using-kubectl-top-show-swap)

Querying metrics is valuable, but somewhat cumbersome, as these metrics are designed to be used by software rather than humans. In order to consume this data in a more user-friendly way, the `kubectl top` command has been extended to support swap metrics, using the `--show-swap` flag.

In order to receive information about swap usage on nodes, `kubectl top nodes --show-swap` can be used:
```yaml
kubectl top nodes --show-swap
```

This will result in an output similar to:
```yaml
NAME    CPU(cores)   CPU(%)   MEMORY(bytes)   MEMORY(%)   SWAP(bytes)    SWAP(%)       
node1   1m           10%      2Mi             10%         1Mi            0%   
node2   5m           10%      6Mi             10%         2Mi            0%   
node3   3m           10%      4Mi             10%         <unknown>      <unknown>
```

In order to receive information about swap usage by pods, `kubectl top pods --show-swap` can be used:
```yaml
kubectl top pod -n kube-system --show-swap
```

---



# Source: https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Cluster Administration](https://kubernetes.io/docs/concepts/cluster-administration/)
4. Node Autoscaling

# Node AutoscalingAutomatically provision and consolidate the Nodes in your cluster to adapt to demand and optimize cost.

In order to run workloads in your cluster, you need [Nodes](https://kubernetes.io/docs/concepts/architecture/nodes/). Nodes in your cluster can be autoscaled - dynamically [provisioned](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/#provisioning), or [consolidated](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/#consolidation) to provide needed capacity while optimizing cost. Autoscaling is performed by Node [autoscalers](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/#autoscalers).

## Node provisioning[](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/#provisioning)

If there are Pods in a cluster that can't be scheduled on existing Nodes, new Nodes can be automatically added to the cluster—provisioned—to accommodate the Pods. This is especially useful if the number of Pods changes over time, for example as a result of [combining horizontal workload with Node autoscaling](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/#horizontal-workload-autoscaling).

Autoscalers provision the Nodes by creating and deleting cloud provider resources backing them. Most commonly, the resources backing the Nodes are Virtual Machines.

The main goal of provisioning is to make all Pods schedulable. This goal is not always attainable because of various limitations, including reaching configured provisioning limits, provisioning configuration not being compatible with a particular set of pods, or the lack of cloud provider capacity. While provisioning, Node autoscalers often try to achieve additional goals (for example minimizing the cost of the provisioned Nodes or balancing the number of Nodes between failure domains).

There are two main inputs to a Node autoscaler when determining Nodes to provision—[Pod scheduling constraints](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/#provisioning-pod-constraints), and [Node constraints imposed by autoscaler configuration](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/#provisioning-node-constraints).

Autoscaler configuration may also include other Node provisioning triggers (for example the number of Nodes falling below a configured minimum limit).

#### Note:Provisioning was formerly known as scale-up in Cluster Autoscaler.

### Pod scheduling constraints[](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/#provisioning-pod-constraints)

Pods can express [scheduling constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) to impose limitations on the kind of Nodes they can be scheduled on. Node autoscalers take these constraints into account to ensure that the pending Pods can be scheduled on the provisioned Nodes.

The most common kind of scheduling constraints are the resource requests specified by Pod containers. Autoscalers will make sure that the provisioned Nodes have enough resources to satisfy the requests. However, they don't directly take into account the real resource usage of the Pods after they start running. In order to autoscale Nodes based on actual workload resource usage, you can combine [horizontal workload autoscaling](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/#horizontal-workload-autoscaling) with Node autoscaling.

Other common Pod scheduling constraints include [Node affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity), [inter-Pod affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity), or a requirement for a particular [storage volume](https://kubernetes.io/docs/concepts/storage/volumes/).

### Node constraints imposed by autoscaler configuration[](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/#provisioning-node-constraints)

The specifics of the provisioned Nodes (for example the amount of resources, the presence of a given label) depend on autoscaler configuration. Autoscalers can either choose them from a pre-defined set of Node configurations, or use [auto-provisioning](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/#autoprovisioning).

### Auto-provisioning[](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/#autoprovisioning)

Node auto-provisioning is a mode of provisioning in which a user doesn't have to fully configure the specifics of the Nodes that can be provisioned. Instead, the autoscaler dynamically chooses the Node configuration based on the pending Pods it's reacting to, as well as pre-configured constraints (for example, the minimum amount of resources or the need for a given label).

## Node consolidation[](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/#consolidation)

The main consideration when running a cluster is ensuring that all schedulable pods are running, whilst keeping the cost of the cluster as low as possible. To achieve this, the Pods' resource requests should utilize as much of the Nodes' resources as possible. From this perspective, the overall Node utilization in a cluster can be used as a proxy for how cost-effective the cluster is.

#### Note:Correctly setting the resource requests of your Pods is as important to the overall cost-effectiveness of a cluster as optimizing Node utilization. Combining Node autoscaling with [vertical workload autoscaling](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/#vertical-workload-autoscaling) can help you achieve this.

---



# Source: https://kubernetes.io/docs/concepts/cluster-administration/certificates/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Cluster Administration](https://kubernetes.io/docs/concepts/cluster-administration/)
4. Certificates

# Certificates

To learn how to generate certificates for your cluster, see [Certificates](https://kubernetes.io/docs/tasks/administer-cluster/certificates/).

## Feedback

Was this page helpful?Yes No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes). Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to [report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io) or [suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).const yes=document.querySelector(".feedback--yes"),no=document.querySelector(".feedback--no");document.querySelectorAll(".feedback--link").forEach(e=>{e.href=e.href+window.location.pathname});const sendFeedback=e=>{typeof gtag=="function"?gtag("event","page_helpful",{event_category:"Helpful",event_label:window.location.pathname,value:e}):console.log("gtag not available; skipping analytics event")},disableButtons=()=>{yes.disabled=!0,yes.classList.add("feedback--button__disabled"),no.disabled=!0,no.classList.add("feedback--button__disabled")};yes.addEventListener("click",()=>{sendFeedback(100),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")}),no.addEventListener("click",()=>{sendFeedback(0),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")})Last modified January 16, 2021 at 7:16 PM PST: [Migrate https://kubernetes.io/docs/concepts/cluster-administration/certificates/ to tasks section (41220636ec)](https://github.com/kubernetes/website/commit/41220636ec55c393f6b2725f79d0a375d61059b3)

---



# Source: https://kubernetes.io/docs/tasks/administer-cluster/certificates/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Tasks](https://kubernetes.io/docs/tasks/)
3. [Administer a Cluster](https://kubernetes.io/docs/tasks/administer-cluster/)
4. Generate Certificates Manually

# Generate Certificates Manually

When using client certificate authentication, you can generate certificates manually through [`easyrsa`](https://github.com/OpenVPN/easy-rsa), [`openssl`](https://github.com/openssl/openssl) or [`cfssl`](https://github.com/cloudflare/cfssl).

### easyrsa[](https://kubernetes.io/docs/tasks/administer-cluster/certificates/#easyrsa)

easyrsa can manually generate certificates for your cluster.
1. 

Download, unpack, and initialize the patched version of `easyrsa3`.
```yaml
curl -LO https://dl.k8s.io/easy-rsa/easy-rsa.tar.gz
tar xzf easy-rsa.tar.gz
cd easy-rsa-master/easyrsa3
./easyrsa init-pki
```

2. 

Generate a new certificate authority (CA). `--batch` sets automatic mode; `--req-cn` specifies the Common Name (CN) for the CA's new root certificate.
```yaml
./easyrsa --batch "--req-cn=${MASTER_IP}@`date +%s`" build-ca nopass
```

3. 

Generate server certificate and key.

The argument `--subject-alt-name` sets the possible IPs and DNS names the API server will be accessed with. The `MASTER_CLUSTER_IP` is usually the first IP from the service CIDR that is specified as the `--service-cluster-ip-range` argument for both the API server and the controller manager component. The argument `--days` is used to set the number of days after which the certificate expires. The sample below also assumes that you are using `cluster.local` as the default DNS domain name.
```yaml
./easyrsa --subject-alt-name="IP:${MASTER_IP},"\
"IP:${MASTER_CLUSTER_IP},"\
"DNS:kubernetes,"\
"DNS:kubernetes.default,"\
"DNS:kubernetes.default.svc,"\
"DNS:kubernetes.default.svc.cluster,"\
"DNS:kubernetes.default.svc.cluster.local" \
--days=10000 \
build-server-full server nopass
```

---



# Source: https://kubernetes.io/docs/concepts/cluster-administration/networking/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Cluster Administration](https://kubernetes.io/docs/concepts/cluster-administration/)
4. Cluster Networking

# Cluster Networking

Networking is a central part of Kubernetes, but it can be challenging to understand exactly how it is expected to work. There are 4 distinct networking problems to address:
1. Highly-coupled container-to-container communications: this is solved by [Pods](https://kubernetes.io/docs/concepts/workloads/pods/) and `localhost` communications.
2. Pod-to-Pod communications: this is the primary focus of this document.
3. Pod-to-Service communications: this is covered by [Services](https://kubernetes.io/docs/concepts/services-networking/service/).
4. External-to-Service communications: this is also covered by Services.

Kubernetes is all about sharing machines among applications. Typically, sharing machines requires ensuring that two applications do not try to use the same ports. Coordinating ports across multiple developers is very difficult to do at scale and exposes users to cluster-level issues outside of their control.

Dynamic port allocation brings a lot of complications to the system - every application has to take ports as flags, the API servers have to know how to insert dynamic port numbers into configuration blocks, services have to know how to find each other, etc. Rather than deal with this, Kubernetes takes a different approach.

To learn about the Kubernetes networking model, see [here](https://kubernetes.io/docs/concepts/services-networking/).

## Kubernetes IP address ranges[](https://kubernetes.io/docs/concepts/cluster-administration/networking/#kubernetes-ip-address-ranges)

Kubernetes clusters require to allocate non-overlapping IP addresses for Pods, Services and Nodes, from a range of available addresses configured in the following components:
* The network plugin is configured to assign IP addresses to Pods.
* The kube-apiserver is configured to assign IP addresses to Services.
* The kubelet or the cloud-controller-manager is configured to assign IP addresses to Nodes.

![A figure illustrating the different network ranges in a kubernetes cluster](https://kubernetes.io/docs/images/kubernetes-cluster-network.svg)

## Cluster networking types[](https://kubernetes.io/docs/concepts/cluster-administration/networking/#cluster-network-ipfamilies)

Kubernetes clusters, attending to the IP families configured, can be categorized into:
* IPv4 only: The network plugin, kube-apiserver and kubelet/cloud-controller-manager are configured to assign only IPv4 addresses.
* IPv6 only: The network plugin, kube-apiserver and kubelet/cloud-controller-manager are configured to assign only IPv6 addresses.
* IPv4/IPv6 or IPv6/IPv4 [dual-stack](https://kubernetes.io/docs/concepts/services-networking/dual-stack/):
  * The network plugin is configured to assign IPv4 and IPv6 addresses.
  * The kube-apiserver is configured to assign IPv4 and IPv6 addresses.
  * The kubelet or cloud-controller-manager is configured to assign IPv4 and IPv6 address.
  * All components must agree on the configured primary IP family.

Kubernetes clusters only consider the IP families present on the Pods, Services and Nodes objects, independently of the existing IPs of the represented objects. For example, a server or a pod can have multiple IP addresses assigned to its interfaces, but only the IP addresses in `node.status.addresses` or `pod.status.ips` are considered when implementing the Kubernetes network model and defining the cluster type.

## How to implement the Kubernetes network model[](https://kubernetes.io/docs/concepts/cluster-administration/networking/#how-to-implement-the-kubernetes-network-model)

The network model is implemented by the container runtime on each node. The most common container runtimes use [Container Network Interface](https://github.com/containernetworking/cni) (CNI) plugins to manage their network and security capabilities. Many different CNI plugins exist from many different vendors. Some of these provide only basic features of adding and removing network interfaces, while others provide more sophisticated solutions, such as integration with other container orchestration systems, running multiple CNI plugins, advanced IPAM features etc.

See [this page](https://kubernetes.io/docs/concepts/cluster-administration/addons/#networking-and-network-policy) for a non-exhaustive list of networking addons supported by Kubernetes.

## What's next[](https://kubernetes.io/docs/concepts/cluster-administration/networking/#what-s-next)

The early design of the networking model and its rationale are described in more detail in the [networking design document](https://git.k8s.io/design-proposals-archive/network/networking.md). For future plans and some on-going efforts that aim to improve Kubernetes networking, please refer to the SIG-Network [KEPs](https://github.com/kubernetes/enhancements/tree/master/keps/sig-network).

## Feedback

Was this page helpful?Yes No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes). Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to [report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io) or [suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).const yes=document.querySelector(".feedback--yes"),no=document.querySelector(".feedback--no");document.querySelectorAll(".feedback--link").forEach(e=>{e.href=e.href+window.location.pathname});const sendFeedback=e=>{typeof gtag=="function"?gtag("event","page_helpful",{event_category:"Helpful",event_label:window.location.pathname,value:e}):console.log("gtag not available; skipping analytics event")},disableButtons=()=>{yes.disabled=!0,yes.classList.add("feedback--button__disabled"),no.disabled=!0,no.classList.add("feedback--button__disabled")};yes.addEventListener("click",()=>{sendFeedback(100),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")}),no.addEventListener("click",()=>{sendFeedback(0),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")})Last modified October 26, 2025 at 2:21 PM PST: [Update content/en/docs/concepts/cluster-administration/networking.md (be90770c29)](https://github.com/kubernetes/website/commit/be90770c29778e608f04bda7392b9786a56fa210)

---



# Source: https://kubernetes.io/docs/concepts/cluster-administration/observability/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Cluster Administration](https://kubernetes.io/docs/concepts/cluster-administration/)
4. Observability

# ObservabilityUnderstand how to gain end-to-end visibility of a Kubernetes cluster through the collection of metrics, logs, and traces.

In Kubernetes, observability is the process of collecting and analyzing metrics, logs, and traces—often referred to as the three pillars of observability—in order to obtain a better understanding of the internal state, performance, and health of the cluster.

Kubernetes control plane components, as well as many add-ons, generate and emit these signals. By aggregating and correlating them, you can gain a unified picture of the control plane, add-ons, and applications across the cluster.

Figure 1 outlines how cluster components emit the three primary signal types.
```yaml
flowchart LR
    A[Cluster components] --> M[Metrics pipeline]
    A --> L[Log pipeline]
    A --> T[Trace pipeline]
    M --> S[(Storage and analysis)]
    L --> S
    T --> S
    S --> O[Operators and automation]
```

Figure 1. High-level signals emitted by cluster components and their consumers.

## Metrics[](https://kubernetes.io/docs/concepts/cluster-administration/observability/#metrics)

Kubernetes components emit metrics in [Prometheus format](https://prometheus.io/docs/instrumenting/exposition_formats/) from their `/metrics` endpoints, including:
* kube-controller-manager
* kube-proxy
* kube-apiserver
* kube-scheduler
* kubelet

The kubelet also exposes metrics at `/metrics/cadvisor`, `/metrics/resource`, and `/metrics/probes`, and add-ons such as [kube-state-metrics](https://kubernetes.io/docs/concepts/cluster-administration/kube-state-metrics/) enrich those control plane signals with Kubernetes object status.

A typical Kubernetes metrics pipeline periodically scrapes these endpoints and stores the samples in a time series database (for example with Prometheus).

See the [system metrics guide](https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/) for details and configuration options.

Figure 2 outlines a common Kubernetes metrics pipeline.
```yaml
flowchart LR
    C[Cluster components] --> P[Prometheus scraper]
    P --> TS[(Time series storage)]
    TS --> D[Dashboards and alerts]
    TS --> A[Automated actions]
```

Figure 2. Components of a typical Kubernetes metrics pipeline.

For multi-cluster or multi-cloud visibility, distributed time series databases (for example Thanos or Cortex) can complement Prometheus.

See [Common observability tools - metrics tools](https://kubernetes.io/docs/concepts/cluster-administration/observability/#metrics-tools) for metrics scrapers and time series databases.

#### See Also[](https://kubernetes.io/docs/concepts/cluster-administration/observability/#see-also)
* [System metrics for Kubernetes components](https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/)
* [Resource usage monitoring with metrics-server](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-usage-monitoring/)
* [kube-state-metrics concept](https://kubernetes.io/docs/concepts/cluster-administration/kube-state-metrics/)
* [Resource metrics pipeline overview](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/)

## Logs[](https://kubernetes.io/docs/concepts/cluster-administration/observability/#logs)

Logs provide a chronological record of events inside applications, Kubernetes system components, and security-related activities such as audit logging.

Container runtimes capture a containerized application’s output from standard output (`stdout`) and standard error (`stderr`) streams. While runtimes implement this differently, the integration with the kubelet is standardized through the CRI logging format, and the kubelet makes these logs available through `kubectl logs`.

![Node-level logging](https://kubernetes.io/images/docs/user-guide/logging/logging-node-level.png)

Figure 3a. Node-level logging architecture.

System component logs capture events from the cluster and are often useful for debugging and troubleshooting. These components are classified in two different ways: those that run in a container and those that do not. For example, the `kube-scheduler` and `kube-proxy` usually run in containers, whereas the `kubelet` and the container runtime run directly on the host.
* On machines with `systemd`, the kubelet and container runtime write to journald. Otherwise, they write to `.log` files in the `/var/log` directory.
* System components that run inside containers always write to `.log` files in `/var/log`, bypassing the default container logging mechanism.

System component and container logs stored under `/var/log` require log rotation to prevent uncontrolled growth. Some cluster provisioning scripts install log rotation by default; verify your environment and adjust as needed. See the [system logs reference](https://kubernetes.io/docs/concepts/cluster-administration/system-logs/) for details on locations, formats, and configuration options.

Most clusters run a node-level logging agent (for example, Fluent Bit or Fluentd) that tails these files and forwards entries to a central log store. The [logging architecture guidance](https://kubernetes.io/docs/concepts/cluster-administration/logging/) explains how to design such pipelines, apply retention, and log flows to backends.

Figure 3 outlines a common log aggregation pipeline.
```yaml
flowchart LR
    subgraph Sources
        A[Application stdout / stderr]
        B[Control plane logs]
        C[Audit records]
    end
    A --> N[Node log agent]
    B --> N
    C --> N
    N --> L[Central log store]
    L --> Q[Dashboards, alerting, SIEM]
```

Figure 3. Components of a typical Kubernetes logs pipeline.

See [Common observability tools - logging tools](https://kubernetes.io/docs/concepts/cluster-administration/observability/#logging-tools) for logging agents and central log stores.

#### See Also[](https://kubernetes.io/docs/concepts/cluster-administration/observability/#see-also-1)
* [Logging architecture](https://kubernetes.io/docs/concepts/cluster-administration/logging/)
* [System logs](https://kubernetes.io/docs/concepts/cluster-administration/system-logs/)
* [Logging tasks and tutorials](https://kubernetes.io/docs/tasks/debug/logging/)
* [Configure audit logging](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/)

## Traces[](https://kubernetes.io/docs/concepts/cluster-administration/observability/#traces)

Traces capture how requests moves across Kubernetes components and applications, linking latency, timing and relationships between operations.By collecting traces, you can visualize end-to-end request flow, diagnose performance issues, and identify bottlenecks or unexpected interactions in the control plane, add-ons, or applications.

Kubernetes 1.36 can export spans over the [OpenTelemetry Protocol](https://kubernetes.io/docs/concepts/cluster-administration/system-traces/) (OTLP), either directly via built-in gRPC exporters or by forwarding them through an OpenTelemetry Collector.

The OpenTelemetry Collector receives spans from components and applications, processes them (for example by applying sampling or redaction), and forwards them to a tracing backend for storage and analysis.

Figure 4 outlines a typical distributed tracing pipeline.
```yaml
flowchart LR
    subgraph Sources
        A[Control plane spans]
        B[Application spans]
    end
    A --> X[OTLP exporter]
    B --> X
    X --> COL[OpenTelemetry Collector]
    COL --> TS[(Tracing backend)]
    TS --> V[Visualization and analysis]
```

Figure 4. Components of a typical Kubernetes traces pipeline.

See [Common observability tools - tracing tools](https://kubernetes.io/docs/concepts/cluster-administration/observability/#tracing-tools) for tracing collectors and backends.

#### See Also[](https://kubernetes.io/docs/concepts/cluster-administration/observability/#see-also-2)
* [System traces for Kubernetes components](https://kubernetes.io/docs/concepts/cluster-administration/system-traces/)
* [OpenTelemetry Collector getting started guide](https://opentelemetry.io/docs/collector/getting-started/)
* [Monitoring and tracing tasks](https://kubernetes.io/docs/tasks/debug/monitoring/)

## Common observability tools[](https://kubernetes.io/docs/concepts/cluster-administration/observability/#common-observability-tools)Note: This section links to third party projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for these projects, which are listed alphabetically. To add a project to this list, read the [content guide](https://kubernetes.io/docs/contribute/style/content-guide/#third-party-content) before submitting a change. [More information.](https://kubernetes.io/docs/concepts/cluster-administration/observability/#third-party-content-disclaimer)

Note: This section links to third-party projects that provide observability capabilities required by Kubernetes. The Kubernetes project authors aren't responsible for these projects, which are listed alphabetically. To add a project to this list, read the [content guide](https://kubernetes.io/docs/contribute/style/content-guide/) before submitting a change.

### Metrics tools[](https://kubernetes.io/docs/concepts/cluster-administration/observability/#metrics-tools)
* [Cortex](https://cortexmetrics.io/) offers horizontally scalable, long-term Prometheus storage.
* [Grafana Mimir](https://grafana.com/oss/mimir/) is a Grafana Labs project that provides multi-tenant, horizontally scalable Prometheus-compatible storage.
* [Prometheus](https://prometheus.io/) is the monitoring system that scrapes and stores metrics from Kubernetes components.
* [Thanos](https://thanos.io/) extends Prometheus with global querying, downsampling, and object storage support.

### Logging tools[](https://kubernetes.io/docs/concepts/cluster-administration/observability/#logging-tools)
* [Elasticsearch](https://www.elastic.co/elasticsearch/) delivers distributed log indexing and search.
* [Fluent Bit](https://fluentbit.io/) collects and forwards container and node logs with a low resource footprint.
* [Fluentd](https://www.fluentd.org/) routes and transforms logs to multiple destinations.
* [Grafana Loki](https://grafana.com/oss/loki/) stores logs in a Prometheus-inspired, label-based format.
* [OpenSearch](https://opensearch.org/) provides open source log indexing and search compatible with Elasticsearch APIs.

### Tracing tools[](https://kubernetes.io/docs/concepts/cluster-administration/observability/#tracing-tools)
* [Grafana Tempo](https://grafana.com/oss/tempo/) offers scalable, low-cost distributed tracing storage.
* [Jaeger](https://www.jaegertracing.io/) captures and visualizes distributed traces for microservices.
* [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) receives, processes, and exports telemetry data including traces.
* [Zipkin](https://zipkin.io/) provides distributed tracing collection and visualization.

## What's next[](https://kubernetes.io/docs/concepts/cluster-administration/observability/#what-s-next)
* Learn how to [collect resource usage metrics with metrics-server](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-usage-monitoring/)
* Explore [logging tasks and tutorials](https://kubernetes.io/docs/tasks/debug/logging/)
* Follow the [monitoring and tracing task guides](https://kubernetes.io/docs/tasks/debug/monitoring/)
* Review the [system metrics guide](https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/) for component endpoints and stability
* Review the [common observability tools](https://kubernetes.io/docs/concepts/cluster-administration/observability/#common-observability-tools) section for vetted third-party options

## Feedback

Was this page helpful?Yes No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes). Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to [report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io) or [suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).

---



# Source: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Cluster Administration](https://kubernetes.io/docs/concepts/cluster-administration/)
4. Admission Webhook Good Practices

# Admission Webhook Good PracticesRecommendations for designing and deploying admission webhooks in Kubernetes.

This page provides good practices and considerations when designing admission webhooks in Kubernetes. This information is intended for cluster operators who run admission webhook servers or third-party applications that modify or validate your API requests.

Before reading this page, ensure that you're familiar with the following concepts:
* [Admission controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/)
* [Admission webhooks](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#what-are-admission-webhooks)

## Importance of good webhook design[](https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/#why-good-webhook-design-matters)

Admission control occurs when any create, update, or delete request is sent to the Kubernetes API. Admission controllers intercept requests that match specific criteria that you define. These requests are then sent to mutating admission webhooks or validating admission webhooks. These webhooks are often written to ensure that specific fields in object specifications exist or have specific allowed values.

Webhooks are a powerful mechanism to extend the Kubernetes API. Badly-designed webhooks often result in workload disruptions because of how much control the webhooks have over objects in the cluster. Like other API extension mechanisms, webhooks are challenging to test at scale for compatibility with all of your workloads, other webhooks, add-ons, and plugins.

Additionally, with every release, Kubernetes adds or modifies the API with new features, feature promotions to beta or stable status, and deprecations. Even stable Kubernetes APIs are likely to change. For example, the `Pod` API changed in v1.29 to add the [Sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) feature. While it's rare for a Kubernetes object to enter a broken state because of a new Kubernetes API, webhooks that worked as expected with earlier versions of an API might not be able to reconcile more recent changes to that API. This can result in unexpected behavior after you upgrade your clusters to newer versions.

This page describes common webhook failure scenarios and how to avoid them by cautiously and thoughtfully designing and implementing your webhooks.

## Identify whether you use admission webhooks[](https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/#identify-admission-webhooks)

Even if you don't run your own admission webhooks, some third-party applications that you run in your clusters might use mutating or validating admission webhooks.

To check whether your cluster has any mutating admission webhooks, run the following command:
```yaml
kubectl get mutatingwebhookconfigurations
```

The output lists any mutating admission controllers in the cluster.

To check whether your cluster has any validating admission webhooks, run the following command:
```yaml
kubectl get validatingwebhookconfigurations
```

---



# Source: https://kubernetes.io/docs/concepts/cluster-administration/dra/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Cluster Administration](https://kubernetes.io/docs/concepts/cluster-administration/)
4. Good practices for Dynamic Resource Allocation as a Cluster Admin

# Good practices for Dynamic Resource Allocation as a Cluster Admin

This page describes good practices when configuring a Kubernetes cluster utilizing Dynamic Resource Allocation (DRA). These instructions are for cluster administrators.

## Separate permissions to DRA related APIs[](https://kubernetes.io/docs/concepts/cluster-administration/dra/#separate-permissions-to-dra-related-apis)

DRA is orchestrated through a number of different APIs. Use authorization tools (like RBAC, or another solution) to control access to the right APIs depending on the persona of your user.

In general, DeviceClasses and ResourceSlices should be restricted to admins and the DRA drivers. Cluster operators that will be deploying Pods with claims will need access to ResourceClaim and ResourceClaimTemplate APIs; both of these APIs are namespace scoped.

## DRA driver deployment and maintenance[](https://kubernetes.io/docs/concepts/cluster-administration/dra/#dra-driver-deployment-and-maintenance)

DRA drivers are third-party applications that run on each node of your cluster to interface with the hardware of that node and Kubernetes' native DRA components. The installation procedure depends on the driver you choose, but is likely deployed as a DaemonSet to all or a selection of the nodes (using node selectors or similar mechanisms) in your cluster.

### Use drivers with seamless upgrade if available[](https://kubernetes.io/docs/concepts/cluster-administration/dra/#use-drivers-with-seamless-upgrade-if-available)

DRA drivers implement the [`kubeletplugin` package interface](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/kubeletplugin). Your driver may support seamless upgrades by implementing a property of this interface that allows two versions of the same DRA driver to coexist for a short time. This is only available for kubelet versions 1.33 and above and may not be supported by your driver for heterogeneous clusters with attached nodes running older versions of Kubernetes - check your driver's documentation to be sure.

If seamless upgrades are available for your situation, consider using it to minimize scheduling delays when your driver updates.

If you cannot use seamless upgrades, during driver downtime for upgrades you may observe that:
* Pods cannot start unless the claims they depend on were already prepared for use.
* Cleanup after the last pod which used a claim gets delayed until the driver is available again. The pod is not marked as terminated. This prevents reusing the resources used by the pod for other pods.
* Running pods will continue to run.

### Confirm your DRA driver exposes a liveness probe and utilize it[](https://kubernetes.io/docs/concepts/cluster-administration/dra/#confirm-your-dra-driver-exposes-a-liveness-probe-and-utilize-it)

Your DRA driver likely implements a gRPC socket for healthchecks as part of DRA driver good practices. The easiest way to utilize this grpc socket is to configure it as a liveness probe for the DaemonSet deploying your DRA driver. Your driver's documentation or deployment tooling may already include this, but if you are building your configuration separately or not running your DRA driver as a Kubernetes pod, be sure that your orchestration tooling restarts the DRA driver on failed healthchecks to this grpc socket. Doing so will minimize any accidental downtime of the DRA driver and give it more opportunities to self heal, reducing scheduling delays or troubleshooting time.

### When draining a node, drain the DRA driver as late as possible[](https://kubernetes.io/docs/concepts/cluster-administration/dra/#when-draining-a-node-drain-the-dra-driver-as-late-as-possible)

The DRA driver is responsible for unpreparing any devices that were allocated to Pods, and if the DRA driver is [drained](https://kubernetes.io/docs/reference/glossary/?all=true#term-drain) before Pods with claims have been deleted, it will not be able to finalize its cleanup. If you implement custom drain logic for nodes, consider checking that there are no allocated/reserved ResourceClaim or ResourceClaimTemplates before terminating the DRA driver itself.

## Monitor and tune components for higher load, especially in high scale environments[](https://kubernetes.io/docs/concepts/cluster-administration/dra/#monitor-and-tune-components-for-higher-load-especially-in-high-scale-environments)

Control plane component [kube-scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/) and the internal ResourceClaim controller orchestrated by the component [kube-controller-manager](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/) do the heavy lifting during scheduling of Pods with claims based on metadata stored in the DRA APIs. Compared to non-DRA scheduled Pods, the number of API server calls, memory, and CPU utilization needed by these components is increased for Pods using DRA claims. In addition, node local components like the DRA driver and kubelet utilize DRA APIs to allocated the hardware request at Pod sandbox creation time. Especially in high scale environments where clusters have many nodes, and/or deploy many workloads that heavily utilize DRA defined resource claims, the cluster administrator should configure the relevant components to anticipate the increased load.

The effects of mistuned components can have direct or snowballing affects causing different symptoms during the Pod lifecycle. If the `kube-scheduler` component's QPS and burst configurations are too low, the scheduler might quickly identify a suitable node for a Pod but take longer to bind the Pod to that node. With DRA, during Pod scheduling, the QPS and Burst parameters in the client-go configuration within `kube-controller-manager` are critical.

The specific values to tune your cluster to depend on a variety of factors like number of nodes/pods, rate of pod creation, churn, even in non-DRA environments; see the [SIG Scalability README on Kubernetes scalability thresholds](https://github.com/kubernetes/community/blob/main/sig-scalability/configs-and-limits/thresholds.md) for more information. In scale tests performed against a DRA enabled cluster with 100 nodes, involving 720 long-lived pods (90% saturation) and 80 churn pods (10% churn, 10 times), with a job creation QPS of 10, `kube-controller-manager` QPS could be set to as low as 75 and Burst to 150 to meet equivalent metric targets for non-DRA deployments. At this lower bound, it was observed that the client side rate limiter was triggered enough to protect the API server from explosive burst but was high enough that pod startup SLOs were not impacted. While this is a good starting point, you can get a better idea of how to tune the different components that have the biggest effect on DRA performance for your deployment by monitoring the following metrics. For more information on all the stable metrics in Kubernetes, see the [Kubernetes Metrics Reference](https://kubernetes.io/docs/reference/instrumentation/metrics/).

### `kube-controller-manager` metrics[](https://kubernetes.io/docs/concepts/cluster-administration/dra/#kube-controller-manager-metrics)

The following metrics look closely at the internal ResourceClaim controller managed by the `kube-controller-manager` component.
* Workqueue Add Rate: Monitor `sum(rate(workqueue_adds_total{name="resource_claim"}[5m])) `to gauge how quickly items are added to the ResourceClaim controller.
* Workqueue Depth: Track `sum(workqueue_depth{endpoint="kube-controller-manager",
name="resource_claim"})` to identify any backlogs in the ResourceClaim controller.
* Workqueue Work Duration: Observe `histogram_quantile(0.99,
sum(rate(workqueue_work_duration_seconds_bucket{name="resource_claim"}[5m]))
by (le))` to understand the speed at which the ResourceClaim controller processes work.

If you are experiencing low Workqueue Add Rate, high Workqueue Depth, and/or high Workqueue Work Duration, this suggests the controller isn't performing optimally. Consider tuning parameters like QPS, burst, and CPU/memory configurations.

If you are experiencing high Workequeue Add Rate, high Workqueue Depth, but reasonable Workqueue Work Duration, this indicates the controller is processing work, but concurrency might be insufficient. Concurrency is hardcoded in the controller, so as a cluster administrator, you can tune for this by reducing the pod creation QPS, so the add rate to the resource claim workqueue is more manageable.

### `kube-scheduler` metrics[](https://kubernetes.io/docs/concepts/cluster-administration/dra/#kube-scheduler-metrics)

The following scheduler metrics are high level metrics aggregating performance across all Pods scheduled, not just those using DRA. It is important to note that the end-to-end metrics are ultimately influenced by the `kube-controller-manager`'s performance in creating ResourceClaims from ResourceClainTemplates in deployments that heavily use ResourceClainTemplates.
* Scheduler End-to-End Duration: Monitor `histogram_quantile(0.99,
sum(increase(scheduler_pod_scheduling_sli_duration_seconds_bucket[5m])) by
(le))`.
* Scheduler Algorithm Latency: Track `histogram_quantile(0.99,
sum(increase(scheduler_scheduling_algorithm_duration_seconds_bucket[5m])) by
(le))`.

### `kubelet` metrics[](https://kubernetes.io/docs/concepts/cluster-administration/dra/#kubelet-metrics)

When a Pod bound to a node must have a ResourceClaim satisfied, kubelet calls the `NodePrepareResources` and `NodeUnprepareResources` methods of the DRA driver. You can observe this behavior from the kubelet's point of view with the following metrics.
* Kubelet NodePrepareResources: Monitor `histogram_quantile(0.99,
sum(rate(dra_operations_duration_seconds_bucket{operation_name="PrepareResources"}[5m]))
by (le))`.
* Kubelet NodeUnprepareResources: Track `histogram_quantile(0.99,
sum(rate(dra_operations_duration_seconds_bucket{operation_name="UnprepareResources"}[5m]))
by (le))`.

### DRA kubeletplugin operations[](https://kubernetes.io/docs/concepts/cluster-administration/dra/#dra-kubeletplugin-operations)

DRA drivers implement the [`kubeletplugin` package interface](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/kubeletplugin) which surfaces its own metric for the underlying gRPC operation `NodePrepareResources` and `NodeUnprepareResources`. You can observe this behavior from the point of view of the internal kubeletplugin with the following metrics.
* DRA kubeletplugin gRPC NodePrepareResources operation: Observe `histogram_quantile(0.99,
sum(rate(dra_grpc_operations_duration_seconds_bucket{method_name=~".*NodePrepareResources"}[5m]))
by (le))`.
* DRA kubeletplugin gRPC NodeUnprepareResources operation: Observe `histogram_quantile(0.99,
sum(rate(dra_grpc_operations_duration_seconds_bucket{method_name=~".*NodeUnprepareResources"}[5m]))
by (le))`.

## What's next[](https://kubernetes.io/docs/concepts/cluster-administration/dra/#what-s-next)
* [Learn more about DRA](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/)
* Read the [Kubernetes Metrics Reference](https://kubernetes.io/docs/reference/instrumentation/metrics/)

## Feedback

Was this page helpful?Yes No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes). Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to [report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io) or [suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).const yes=document.querySelector(".feedback--yes"),no=document.querySelector(".feedback--no");document.querySelectorAll(".feedback--link").forEach(e=>{e.href=e.href+window.location.pathname});const sendFeedback=e=>{typeof gtag=="function"?gtag("event","page_helpful",{event_category:"Helpful",event_label:window.location.pathname,value:e}):console.log("gtag not available; skipping analytics event")},disableButtons=()=>{yes.disabled=!0,yes.classList.add("feedback--button__disabled"),no.disabled=!0,no.classList.add("feedback--button__disabled")};yes.addEventListener("click",()=>{sendFeedback(100),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")}),no.addEventListener("click",()=>{sendFeedback(0),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")})Last modified April 14, 2026 at 1:15 AM PST: [fix(links): update kubernetes/community links from master to main (03c191bcc4)](https://github.com/kubernetes/website/commit/03c191bcc446f9c15a9e68d6cd1154b53bde4291)

---



# Source: https://kubernetes.io/docs/concepts/cluster-administration/logging/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Cluster Administration](https://kubernetes.io/docs/concepts/cluster-administration/)
4. Logging Architecture

# Logging Architecture

Application logs can help you understand what is happening inside your application. The logs are particularly useful for debugging problems and monitoring cluster activity. Most modern applications have some kind of logging mechanism. Likewise, container engines are designed to support logging. The easiest and most adopted logging method for containerized applications is writing to standard output and standard error streams.

However, the native functionality provided by a container engine or runtime is usually not enough for a complete logging solution.

For example, you may want to access your application's logs if a container crashes, a pod gets evicted, or a node dies.

In a cluster, logs should have a separate storage and lifecycle independent of nodes, pods, or containers. This concept is called [cluster-level logging](https://kubernetes.io/docs/concepts/cluster-administration/logging/#cluster-level-logging-architectures).

Cluster-level logging architectures require a separate backend to store, analyze, and query logs. Kubernetes does not provide a native storage solution for log data. Instead, there are many logging solutions that integrate with Kubernetes. The following sections describe how to handle and store logs on nodes.

## Pod and container logs[](https://kubernetes.io/docs/concepts/cluster-administration/logging/#basic-logging-in-kubernetes)

Kubernetes captures logs from each container in a running Pod.

This example uses a manifest for a `Pod` with a container that writes text to the standard output stream, once per second.[`debug/counter-pod.yaml` ](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/debug/counter-pod.yaml)

![Diagram](https://kubernetes.io/images/copycode.svg)

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: counter
spec:
  containers:
  - name: count
    image: busybox:1.28
    args: [/bin/sh, -c,
            'i=0; while true; do echo "$i: $(date)"; i=$((i+1)); sleep 1; done']
```

---



# Source: https://kubernetes.io/docs/concepts/cluster-administration/compatibility-version/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Cluster Administration](https://kubernetes.io/docs/concepts/cluster-administration/)
4. Compatibility Version For Kubernetes Control Plane Components

# Compatibility Version For Kubernetes Control Plane Components

Since release v1.32, we introduced configurable version compatibility and emulation options to Kubernetes control plane components to make upgrades safer by providing more control and increasing the granularity of steps available to cluster administrators.

## Emulated Version[](https://kubernetes.io/docs/concepts/cluster-administration/compatibility-version/#emulated-version)

The emulation option is set by the `--emulated-version` flag of control plane components. It allows the component to emulate the behavior (APIs, features, ...) of an earlier version of Kubernetes.

When used, the capabilities available will match the emulated version:
* Any capabilities present in the binary version that were introduced after the emulation version will be unavailable.
* Any capabilities removed after the emulation version will be available.

This enables a binary from a particular Kubernetes release to emulate the behavior of a previous version with sufficient fidelity that interoperability with other system components can be defined in terms of the emulated version.

The `--emulated-version` must be <= `binaryVersion`. See the help message of the `--emulated-version` flag for supported range of emulated versions.

## Feedback

Was this page helpful?Yes No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes). Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to [report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io) or [suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).const yes=document.querySelector(".feedback--yes"),no=document.querySelector(".feedback--no");document.querySelectorAll(".feedback--link").forEach(e=>{e.href=e.href+window.location.pathname});const sendFeedback=e=>{typeof gtag=="function"?gtag("event","page_helpful",{event_category:"Helpful",event_label:window.location.pathname,value:e}):console.log("gtag not available; skipping analytics event")},disableButtons=()=>{yes.disabled=!0,yes.classList.add("feedback--button__disabled"),no.disabled=!0,no.classList.add("feedback--button__disabled")};yes.addEventListener("click",()=>{sendFeedback(100),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")}),no.addEventListener("click",()=>{sendFeedback(0),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")})Last modified November 05, 2024 at 4:12 PM PST: [remove min-compat-version (f0ca297ac6)](https://github.com/kubernetes/website/commit/f0ca297ac692c70f20a0519a3e2d345707e4639d)

---



# Source: https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Cluster Administration](https://kubernetes.io/docs/concepts/cluster-administration/)
4. Metrics For Kubernetes System Components

# Metrics For Kubernetes System Components

System component metrics can give a better look into what is happening inside them. Metrics are particularly useful for building dashboards and alerts.

Kubernetes components emit metrics in [Prometheus format](https://prometheus.io/docs/instrumenting/exposition_formats/). This format is structured plain text, designed so that people and machines can both read it.

## Metrics in Kubernetes[](https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/#metrics-in-kubernetes)

In most cases metrics are available on `/metrics` endpoint of the HTTP server. For components that don't expose endpoint by default, it can be enabled using `--bind-address` flag.

Examples of those components:
* [kube-controller-manager](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/)
* [kube-proxy](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/)
* [kube-apiserver](https://kubernetes.io/docs/concepts/architecture/#kube-apiserver)
* [kube-scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/)
* [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet)

In a production environment you may want to configure [Prometheus Server](https://prometheus.io/) or some other metrics scraper to periodically gather these metrics and make them available in some kind of time series database.

Note that [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet) also exposes metrics in `/metrics/cadvisor`, `/metrics/resource` and `/metrics/probes` endpoints. Those metrics do not have the same lifecycle.

If your cluster uses [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/), reading metrics requires authorization via a user, group or ServiceAccount with a ClusterRole that allows accessing `/metrics`. For example:
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: prometheus
rules:
  - nonResourceURLs:
      - "/metrics"
    verbs:
      - get
```

## Metric lifecycle[](https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/#metric-lifecycle)

Alpha metric → Beta metric → Stable metric → Deprecated metric → Hidden metric → Deleted metric

Alpha metrics have no stability guarantees. These metrics can be modified or deleted at any time.

Beta metrics observe a looser API contract than its stable counterparts. No labels can be removed from beta metrics during their lifetime, however, labels can be added while the metric is in the beta stage.

Stable metrics are guaranteed to not change. This means:
* A stable metric without a deprecated signature will not be deleted or renamed
* A stable metric's type will not be modified

Deprecated metrics are slated for deletion, but are still available for use. These metrics include an annotation about the version in which they became deprecated.

For example:
* 

Before deprecation
```yaml
# HELP some_counter this counts things
# TYPE some_counter counter
some_counter 0
```

* 

After deprecation
```yaml
# HELP some_counter (Deprecated since 1.15.0) this counts things
# TYPE some_counter counter
some_counter 0
```

Hidden metrics are no longer published for scraping, but are still available for use. A deprecated metric becomes a hidden metric after a period of time, based on its stability level:
* STABLE metrics become hidden after a minimum of 3 releases or 9 months, whichever is longer.
* BETA metrics become hidden after a minimum of 1 release or 4 months, whichever is longer.
* ALPHA metrics can be hidden or removed in the same release in which they are deprecated.

To use a hidden metric, you must enable it. For more details, refer to the [Show hidden metrics](https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/#show-hidden-metrics) section.

Deleted metrics are no longer published and cannot be used.

## Show hidden metrics[](https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/#show-hidden-metrics)

As described above, admins can enable hidden metrics through a command-line flag on a specific binary. This intends to be used as an escape hatch for admins if they missed the migration of the metrics deprecated in the last release.

The flag `show-hidden-metrics-for-version` takes a version for which you want to show metrics deprecated in that release. The version is expressed as x.y, where x is the major version, y is the minor version. The patch version is not needed even though a metrics can be deprecated in a patch release, the reason for that is the metrics deprecation policy runs against the minor release.

The flag can only take the previous minor version as its value. If you want to show all metrics hidden in the previous release, you can set the `show-hidden-metrics-for-version` flag to the previous version. Using a version that is too old is not allowed because it violates the metrics deprecation policy.

For example, let's assume metric `A` is deprecated in `1.29`. The version in which metric `A` becomes hidden depends on its stability level:
* If metric `A` is ALPHA, it could be hidden in `1.29`.
* If metric `A` is BETA, it will be hidden in `1.30` at the earliest. If you are upgrading to `1.30` and still need `A`, you must use the command-line flag `--show-hidden-metrics-for-version=1.29`.
* If metric `A` is STABLE, it will be hidden in `1.32` at the earliest. If you are upgrading to `1.32` and still need `A`, you must use the command-line flag `--show-hidden-metrics-for-version=1.31`.

## Component metrics[](https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/#component-metrics)

### kube-controller-manager metrics[](https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/#kube-controller-manager-metrics)

Controller manager metrics provide important insight into the performance and health of the controller manager. These metrics include common Go language runtime metrics such as go_routine count and controller specific metrics such as etcd request latencies or Cloudprovider (AWS, GCE, OpenStack) API latencies that can be used to gauge the health of a cluster.

Starting from Kubernetes 1.7, detailed Cloudprovider metrics are available for storage operations for GCE, AWS, Vsphere and OpenStack. These metrics can be used to monitor health of persistent volume operations.

For example, for GCE these metrics are called:
```yaml
cloudprovider_gce_api_request_duration_seconds { request = "instance_list"}
cloudprovider_gce_api_request_duration_seconds { request = "disk_insert"}
cloudprovider_gce_api_request_duration_seconds { request = "disk_delete"}
cloudprovider_gce_api_request_duration_seconds { request = "attach_disk"}
cloudprovider_gce_api_request_duration_seconds { request = "detach_disk"}
cloudprovider_gce_api_request_duration_seconds { request = "list_disk"}
```

### kube-scheduler metrics[](https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/#kube-scheduler-metrics)FEATURE STATE: `Kubernetes v1.21 [beta]`

The scheduler exposes optional metrics that reports the requested resources and the desired limits of all running pods. These metrics can be used to build capacity planning dashboards, assess current or historical scheduling limits, quickly identify workloads that cannot schedule due to lack of resources, and compare actual usage to the pod's request.

The kube-scheduler identifies the resource [requests and limits](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) configured for each Pod; when either a request or limit is non-zero, the kube-scheduler reports a metrics timeseries. The time series is labelled by:
* namespace
* pod name
* the node where the pod is scheduled or an empty string if not yet scheduled
* priority
* the assigned scheduler for that pod
* the name of the resource (for example, `cpu`)
* the unit of the resource if known (for example, `cores`)

Once a pod reaches completion (has a `restartPolicy` of `Never` or `OnFailure` and is in the `Succeeded` or `Failed` pod phase, or has been deleted and all containers have a terminated state) the series is no longer reported since the scheduler is now free to schedule other pods to run. The two metrics are called `kube_pod_resource_request` and `kube_pod_resource_limit`.

The metrics are exposed at the HTTP endpoint `/metrics/resources`. They require authorization for the `/metrics/resources` endpoint, usually granted by a ClusterRole with the `get` verb for the `/metrics/resources` non-resource URL.

On Kubernetes 1.21 you must use the `--show-hidden-metrics-for-version=1.20` flag to expose these alpha stability metrics.

### kubelet Pressure Stall Information (PSI) metrics[](https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/#kubelet-pressure-stall-information-psi-metrics)FEATURE STATE: `Kubernetes v1.36 [stable]`(enabled by default)

---



# Source: https://kubernetes.io/docs/concepts/cluster-administration/kube-state-metrics/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Cluster Administration](https://kubernetes.io/docs/concepts/cluster-administration/)
4. Metrics for Kubernetes Object States

# Metrics for Kubernetes Object Stateskube-state-metrics, an add-on agent to generate and expose cluster-level metrics.

The state of Kubernetes objects in the Kubernetes API can be exposed as metrics. An add-on agent called [kube-state-metrics](https://github.com/kubernetes/kube-state-metrics) can connect to the Kubernetes API server and expose a HTTP endpoint with metrics generated from the state of individual objects in the cluster. It exposes various information about the state of objects like labels and annotations, startup and termination times, status or the phase the object currently is in. For example, containers running in pods create a `kube_pod_container_info` metric. This includes the name of the container, the name of the pod it is part of, the [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces) the pod is running in, the name of the container image, the ID of the image, the image name from the spec of the container, the ID of the running container and the ID of the pod as labels.🛇 This item links to a third party project or product that is not part of Kubernetes itself. [More information](https://kubernetes.io/docs/concepts/cluster-administration/kube-state-metrics/#third-party-content-disclaimer)

An external component that is able and capable to scrape the endpoint of kube-state-metrics (for example via Prometheus) can now be used to enable the following use cases.

## Example: using metrics from kube-state-metrics to query the cluster state[](https://kubernetes.io/docs/concepts/cluster-administration/kube-state-metrics/#example-kube-state-metrics-query-1)

Metric series generated by kube-state-metrics are helpful to gather further insights into the cluster, as they can be used for querying.

If you use Prometheus or another tool that uses the same query language, the following PromQL query returns the number of pods that are not ready:
```yaml
count(kube_pod_status_ready{condition="false"}) by (namespace, pod)
```

## Example: alerting based on from kube-state-metrics[](https://kubernetes.io/docs/concepts/cluster-administration/kube-state-metrics/#example-kube-state-metrics-alert-1)

Metrics generated from kube-state-metrics also allow for alerting on issues in the cluster.

If you use Prometheus or a similar tool that uses the same alert rule language, the following alert will fire if there are pods that have been in a `Terminating` state for more than 5 minutes:
```yaml
groups:
- name: Pod state
  rules:
  - alert: PodsBlockedInTerminatingState
    expr: count(kube_pod_deletion_timestamp) by (namespace, pod) * count(kube_pod_status_reason{reason="NodeLost"} == 0) by (namespace, pod) > 0
    for: 5m
    labels:
      severity: page
    annotations:
      summary: Pod {{$labels.namespace}}/{{$labels.pod}} blocked in Terminating state.
```

---



# Source: https://kubernetes.io/docs/concepts/cluster-administration/system-logs/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Cluster Administration](https://kubernetes.io/docs/concepts/cluster-administration/)
4. System Logs

# System Logs

System component logs record events happening in cluster, which can be very useful for debugging. You can configure log verbosity to see more or less detail. Logs can be as coarse-grained as showing errors within a component, or as fine-grained as showing step-by-step traces of events (like HTTP access logs, pod state changes, controller actions, or scheduler decisions).

#### Warning:In contrast to the command line flags described here, the log output itself does not fall under the Kubernetes API stability guarantees: individual log entries and their formatting may change from one release to the next!

## Klog[](https://kubernetes.io/docs/concepts/cluster-administration/system-logs/#klog)

klog is the Kubernetes logging library. [klog](https://github.com/kubernetes/klog) generates log messages for the Kubernetes system components.

Kubernetes is in the process of simplifying logging in its components. The following klog command line flags [are deprecated](https://github.com/kubernetes/enhancements/tree/master/keps/sig-instrumentation/2845-deprecate-klog-specific-flags-in-k8s-components) starting with Kubernetes v1.23 and removed in Kubernetes v1.26:
* `--add-dir-header`
* `--alsologtostderr`
* `--log-backtrace-at`
* `--log-dir`
* `--log-file`
* `--log-file-max-size`
* `--logtostderr`
* `--one-output`
* `--skip-headers`
* `--skip-log-headers`
* `--stderrthreshold`

Output will always be written to stderr, regardless of the output format. Output redirection is expected to be handled by the component which invokes a Kubernetes component. This can be a POSIX shell or a tool like systemd.

In some cases, for example a distroless container or a Windows system service, those options are not available. Then the [`kube-log-runner`](https://github.com/kubernetes/kubernetes/blob/d2a8a81639fcff8d1221b900f66d28361a170654/staging/src/k8s.io/component-base/logs/kube-log-runner/README.md) binary can be used as wrapper around a Kubernetes component to redirect output. A prebuilt binary is included in several Kubernetes base images under its traditional name as `/go-runner` and as `kube-log-runner` in server and node release archives.

This table shows how `kube-log-runner` invocations correspond to shell redirection:``````````````````

| Usage | POSIX shell (such as bash) | kube-log-runner <options> <cmd> || --- | --- | --- || Merge stderr and stdout, write to stdout | 2>&1 | kube-log-runner (default behavior) || Redirect both into log file | 1>>/tmp/log 2>&1 | kube-log-runner -log-file=/tmp/log || Copy into log file and to stdout | 2>&1 | tee -a /tmp/log | kube-log-runner -log-file=/tmp/log -also-stdout || Redirect only stdout into log file | >/tmp/log | kube-log-runner -log-file=/tmp/log -redirect-stderr=false |

### Klog output[](https://kubernetes.io/docs/concepts/cluster-administration/system-logs/#klog-output)

An example of the traditional klog native format:
```yaml
I1025 00:15:15.525108       1 httplog.go:79] GET /api/v1/namespaces/kube-system/pods/metrics-server-v0.3.1-57c75779f-9p8wg: (1.512ms) 200 [pod_nanny/v0.0.0 (linux/amd64) kubernetes/$Format 10.56.1.19:51756]
```

The message string may contain line breaks:
```yaml
I1025 00:15:15.525108       1 example.go:79] This is a message
which has a line break.
```

### Structured Logging[](https://kubernetes.io/docs/concepts/cluster-administration/system-logs/#structured-logging)FEATURE STATE: `Kubernetes v1.23 [beta]`

#### Warning:

Migration to structured log messages is an ongoing process. Not all log messages are structured in this version. When parsing log files, you must also handle unstructured log messages.

Log formatting and value serialization are subject to change.

---



# Source: https://kubernetes.io/docs/concepts/cluster-administration/system-traces/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Cluster Administration](https://kubernetes.io/docs/concepts/cluster-administration/)
4. Traces For Kubernetes System Components

# Traces For Kubernetes System ComponentsFEATURE STATE: `Kubernetes v1.27 [beta]`

System component traces record the latency of and relationships between operations in the cluster.

Kubernetes components emit traces using the [OpenTelemetry Protocol](https://opentelemetry.io/docs/specs/otlp/) with the gRPC exporter and can be collected and routed to tracing backends using an [OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector#-opentelemetry-collector).

## Trace Collection[](https://kubernetes.io/docs/concepts/cluster-administration/system-traces/#trace-collection)

Kubernetes components have built-in gRPC exporters for OTLP to export traces, either with an OpenTelemetry Collector, or without an OpenTelemetry Collector.

For a complete guide to collecting traces and using the collector, see [Getting Started with the OpenTelemetry Collector](https://opentelemetry.io/docs/collector/getting-started/). However, there are a few things to note that are specific to Kubernetes components.

By default, Kubernetes components export traces using the grpc exporter for OTLP on the [IANA OpenTelemetry port](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?search=opentelemetry), 4317. As an example, if the collector is running as a sidecar to a Kubernetes component, the following receiver configuration will collect spans and log them to standard output:
```yaml
receivers:
  otlp:
    protocols:
      grpc:
exporters:
  # Replace this exporter with the exporter for your backend
  exporters:
    debug:
      verbosity: detailed
service:
  pipelines:
    traces:
      receivers: [otlp]
      exporters: [debug]
```

To directly emit traces to a backend without utilizing a collector, specify the endpoint field in the Kubernetes tracing configuration file with the desired trace backend address. This method negates the need for a collector and simplifies the overall structure.

For trace backend header configuration, including authentication details, environment variables can be used with `OTEL_EXPORTER_OTLP_HEADERS`, see [OTLP Exporter Configuration](https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/).

Additionally, for trace resource attribute configuration such as Kubernetes cluster name, namespace, Pod name, etc., environment variables can also be used with `OTEL_RESOURCE_ATTRIBUTES`, see [OTLP Kubernetes Resource](https://opentelemetry.io/docs/specs/semconv/resource/k8s/).

## Component traces[](https://kubernetes.io/docs/concepts/cluster-administration/system-traces/#component-traces)

### kube-apiserver traces[](https://kubernetes.io/docs/concepts/cluster-administration/system-traces/#kube-apiserver-traces)

The kube-apiserver generates spans for incoming HTTP requests, and for outgoing requests to webhooks, etcd, and re-entrant requests. It propagates the [W3C Trace Context](https://www.w3.org/TR/trace-context/) with outgoing requests but does not make use of the trace context attached to incoming requests, as the kube-apiserver is often a public endpoint.

#### Enabling tracing in the kube-apiserver[](https://kubernetes.io/docs/concepts/cluster-administration/system-traces/#enabling-tracing-in-the-kube-apiserver)

To enable tracing, provide the kube-apiserver with a tracing configuration file with `--tracing-config-file=<path-to-config>`. This is an example config that records spans for 1 in 10000 requests, and uses the default OpenTelemetry endpoint:
```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: TracingConfiguration
# default value
#endpoint: localhost:4317
samplingRatePerMillion: 100
```

---



# Source: https://kubernetes.io/docs/concepts/cluster-administration/proxies/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Cluster Administration](https://kubernetes.io/docs/concepts/cluster-administration/)
4. Proxies in Kubernetes

# Proxies in Kubernetes

This page explains proxies used with Kubernetes.

## Proxies[](https://kubernetes.io/docs/concepts/cluster-administration/proxies/#proxies)

There are several different proxies you may encounter when using Kubernetes:
1. 

The [kubectl proxy](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/#directly-accessing-the-rest-api):
  * runs on a user's desktop or in a pod
  * proxies from a localhost address to the Kubernetes apiserver
  * client to proxy uses HTTP
  * proxy to apiserver uses HTTPS
  * locates apiserver
  * adds authentication headers
2. 

The [apiserver proxy](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster-services/#discovering-builtin-services):
  * is a bastion built into the apiserver
  * connects a user outside of the cluster to cluster IPs which otherwise might not be reachable
  * runs in the apiserver processes
  * client to proxy uses HTTPS (or http if apiserver so configured)
  * proxy to target may use HTTP or HTTPS as chosen by proxy using available information
  * can be used to reach a Node, Pod, or Service
  * does load balancing when used to reach a Service
3. 

The [kube proxy](https://kubernetes.io/docs/concepts/services-networking/service/#ips-and-vips):
  * runs on each node
  * proxies UDP, TCP and SCTP
  * does not understand HTTP
  * provides load balancing
  * is only used to reach services
4. 

A Proxy/Load-balancer in front of apiserver(s):
  * existence and implementation varies from cluster to cluster (e.g. nginx)
  * sits between all clients and one or more apiservers
  * acts as load balancer if there are several apiservers.
5. 

Cloud Load Balancers on external services:
  * are provided by some cloud providers (e.g. AWS ELB, Google Cloud Load Balancer)
  * are created automatically when the Kubernetes service has type `LoadBalancer`
  * usually supports UDP/TCP only
  * SCTP support is up to the load balancer implementation of the cloud provider
  * implementation varies by cloud provider.

Kubernetes users will typically not need to worry about anything other than the first two types. The cluster admin will typically ensure that the latter types are set up correctly.

## Requesting redirects[](https://kubernetes.io/docs/concepts/cluster-administration/proxies/#requesting-redirects)

Proxies have replaced redirect capabilities. Redirects have been deprecated.

## Feedback

Was this page helpful?Yes No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes). Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to [report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io) or [suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).const yes=document.querySelector(".feedback--yes"),no=document.querySelector(".feedback--no");document.querySelectorAll(".feedback--link").forEach(e=>{e.href=e.href+window.location.pathname});const sendFeedback=e=>{typeof gtag=="function"?gtag("event","page_helpful",{event_category:"Helpful",event_label:window.location.pathname,value:e}):console.log("gtag not available; skipping analytics event")},disableButtons=()=>{yes.disabled=!0,yes.classList.add("feedback--button__disabled"),no.disabled=!0,no.classList.add("feedback--button__disabled")};yes.addEventListener("click",()=>{sendFeedback(100),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")}),no.addEventListener("click",()=>{sendFeedback(0),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")})Last modified October 24, 2022 at 1:43 PM PST: [KubeCon Docs Sprint: Update page weights for content/en/docs/concepts/cluster-administration. (ac5e7c0bd0)](https://github.com/kubernetes/website/commit/ac5e7c0bd046d4ba88c1cf5f9a624e8fbe4d9193)

---



# Source: https://kubernetes.io/docs/concepts/cluster-administration/flow-control/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Cluster Administration](https://kubernetes.io/docs/concepts/cluster-administration/)
4. API Priority and Fairness

# API Priority and FairnessFEATURE STATE: `Kubernetes v1.29 [stable]`

Controlling the behavior of the Kubernetes API server in an overload situation is a key task for cluster administrators. The [kube-apiserver](https://kubernetes.io/docs/concepts/architecture/#kube-apiserver) has some controls available (i.e. the `--max-requests-inflight` and `--max-mutating-requests-inflight` command-line flags) to limit the amount of outstanding work that will be accepted, preventing a flood of inbound requests from overloading and potentially crashing the API server, but these flags are not enough to ensure that the most important requests get through in a period of high traffic.

The API Priority and Fairness feature (APF) is an alternative that improves upon aforementioned max-inflight limitations. APF classifies and isolates requests in a more fine-grained way. It also introduces a limited amount of queuing, so that no requests are rejected in cases of very brief bursts. Requests are dispatched from queues using a fair queuing technique so that, for example, a poorly-behaved [controller](https://kubernetes.io/docs/concepts/architecture/controller/) need not starve others (even at the same priority level).

This feature is designed to work well with standard controllers, which use informers and react to failures of API requests with exponential back-off, and other clients that also work this way.

#### Caution:Some requests classified as "long-running"—such as remote command execution or log tailing—are not subject to the API Priority and Fairness filter. This is also true for the `--max-requests-inflight` flag without the API Priority and Fairness feature enabled. API Priority and Fairness does apply to watch requests. When API Priority and Fairness is disabled, watch requests are not subject to the `--max-requests-inflight` limit.

## Enabling/Disabling API Priority and Fairness[](https://kubernetes.io/docs/concepts/cluster-administration/flow-control/#enabling-disabling-api-priority-and-fairness)

The API Priority and Fairness feature is controlled by a command-line flag and is enabled by default. See [Options](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/#options) for a general explanation of the available kube-apiserver command-line options and how to enable and disable them. The name of the command-line option for APF is "--enable-priority-and-fairness". This feature also involves an [API Group](https://kubernetes.io/docs/concepts/overview/kubernetes-api/#api-groups-and-versioning) with: (a) a stable `v1` version, introduced in 1.29, and enabled by default (b) a `v1beta3` version, enabled by default, and deprecated in v1.29. You can disable the API group beta version `v1beta3` by adding the following command-line flags to your `kube-apiserver` invocation:
```yaml
kube-apiserver \
--runtime-config=flowcontrol.apiserver.k8s.io/v1beta3=false \
 # …and other flags as usual
```

---



# Source: https://kubernetes.io/docs/concepts/cluster-administration/addons/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Cluster Administration](https://kubernetes.io/docs/concepts/cluster-administration/)
4. Installing Addons

# Installing AddonsNote: This section links to third party projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for these projects, which are listed alphabetically. To add a project to this list, read the [content guide](https://kubernetes.io/docs/contribute/style/content-guide/#third-party-content) before submitting a change. [More information.](https://kubernetes.io/docs/concepts/cluster-administration/addons/#third-party-content-disclaimer)

Add-ons extend the functionality of Kubernetes.

This page lists some of the available add-ons and links to their respective installation instructions. The list does not try to be exhaustive.

## Networking and Network Policy[](https://kubernetes.io/docs/concepts/cluster-administration/addons/#networking-and-network-policy)
* [ACI](https://www.github.com/noironetworks/aci-containers) provides integrated container networking and network security with Cisco ACI.
* [Antrea](https://antrea.io/) operates at Layer 3/4 to provide networking and security services for Kubernetes, leveraging Open vSwitch as the networking data plane. Antrea is a [CNCF project at the Sandbox level](https://www.cncf.io/projects/antrea/).
* [Calico](https://www.tigera.io/project-calico/) is a networking and network policy provider. Calico supports a flexible set of networking options so you can choose the most efficient option for your situation, including non-overlay and overlay networks, with or without BGP. Calico uses the same engine to enforce network policy for hosts, pods, and (if using Istio & Envoy) applications at the service mesh layer.
* [Canal](https://projectcalico.docs.tigera.io/getting-started/kubernetes/flannel/flannel) unites Flannel and Calico, providing networking and network policy.
* [Cilium](https://github.com/cilium/cilium) is a networking, observability, and security solution with an eBPF-based data plane. Cilium provides a simple flat Layer 3 network with the ability to span multiple clusters in either a native routing or overlay/encapsulation mode, and can enforce network policies on L3-L7 using an identity-based security model that is decoupled from network addressing. Cilium can act as a replacement for kube-proxy; it also offers additional, opt-in observability and security features. Cilium is a [CNCF project at the Graduated level](https://www.cncf.io/projects/cilium/).
* [CNI-Genie](https://github.com/cni-genie/CNI-Genie) enables Kubernetes to seamlessly connect to a choice of CNI plugins, such as Calico, Canal, Flannel, or Weave. CNI-Genie is a [CNCF project at the Sandbox level](https://www.cncf.io/projects/cni-genie/).
* [Contiv](https://contivpp.io/) provides configurable networking (native L3 using BGP, overlay using vxlan, classic L2, and Cisco-SDN/ACI) for various use cases and a rich policy framework. Contiv project is fully [open sourced](https://github.com/contiv). The [installer](https://github.com/contiv/install) provides both kubeadm and non-kubeadm based installation options.
* [Contrail](https://www.juniper.net/us/en/products-services/sdn/contrail/contrail-networking/), based on [Tungsten Fabric](https://tungsten.io), is an open source, multi-cloud network virtualization and policy management platform. Contrail and Tungsten Fabric are integrated with orchestration systems such as Kubernetes, OpenShift, OpenStack and Mesos, and provide isolation modes for virtual machines, containers/pods and bare metal workloads.
* [Flannel](https://github.com/flannel-io/flannel#deploying-flannel-manually) is an overlay network provider that can be used with Kubernetes.
* [Gateway API](https://kubernetes.io/docs/concepts/services-networking/gateway/) is an open source project managed by the [SIG Network](https://github.com/kubernetes/community/tree/main/sig-network) community and provides an expressive, extensible, and role-oriented API for modeling service networking.
* [Knitter](https://github.com/ZTE/Knitter/) is a plugin to support multiple network interfaces in a Kubernetes pod.
* [kube-router](https://github.com/cloudnativelabs/kube-router) is an open source turnkey solution for Kubernetes networking with the aim to provide operational simplicity and high performance. It leverages the Kubernetes API, BGP, and Golang for the control path and Linux networking primitives (IPVS, nftables, etc.) for the data path. It provides a low overhead alternative and is used in both k0s and k3s.
* [Multus](https://github.com/k8snetworkplumbingwg/multus-cni) is a Multi plugin for multiple network support in Kubernetes to support all CNI plugins (e.g. Calico, Cilium, Contiv, Flannel), in addition to SRIOV, DPDK, OVS-DPDK and VPP based workloads in Kubernetes.
* [OVN-Kubernetes](https://github.com/ovn-org/ovn-kubernetes/) is a networking provider for Kubernetes based on [OVN (Open Virtual Network)](https://github.com/ovn-org/ovn/), a virtual networking implementation that came out of the Open vSwitch (OVS) project. OVN-Kubernetes provides an overlay based networking implementation for Kubernetes, including an OVS based implementation of load balancing and network policy.
* [Nodus](https://github.com/akraino-edge-stack/icn-nodus) is an OVN based CNI controller plugin to provide cloud native based Service function chaining(SFC).
* [NSX-T](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/index.html) Container Plug-in (NCP) provides integration between VMware NSX-T and container orchestrators such as Kubernetes, as well as integration between NSX-T and container-based CaaS/PaaS platforms such as Pivotal Container Service (PKS) and OpenShift.
* [Nuage](https://github.com/nuagenetworks/nuage-kubernetes/blob/v5.1.1-1/docs/kubernetes-1-installation.rst) is an SDN platform that provides policy-based networking between Kubernetes Pods and non-Kubernetes environments with visibility and security monitoring.
* [Romana](https://github.com/romana) is a Layer 3 networking solution for pod networks that also supports the [NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/network-policies/) API.
* [Spiderpool](https://github.com/spidernet-io/spiderpool) is an underlay and RDMA networking solution for Kubernetes. Spiderpool is supported on bare metal, virtual machines, and public cloud environments.
* [Terway](https://github.com/AliyunContainerService/terway/) is a suite of CNI plugins based on AlibabaCloud's VPC and ECS network products. It provides native VPC networking and network policies in AlibabaCloud environments.
* [Weave Net](https://github.com/rajch/weave#using-weave-on-kubernetes) provides networking and network policy, will carry on working on both sides of a network partition, and does not require an external database.

## Service Discovery[](https://kubernetes.io/docs/concepts/cluster-administration/addons/#service-discovery)
* [CoreDNS](https://coredns.io) is a flexible, extensible DNS server which can be [installed](https://github.com/coredns/helm) as the in-cluster DNS for pods.

## Visualization & Control[](https://kubernetes.io/docs/concepts/cluster-administration/addons/#visualization-control)
* [Dashboard](https://github.com/kubernetes/dashboard#kubernetes-dashboard) is a dashboard web interface for Kubernetes.
* [Headlamp](https://headlamp.dev/) is an extensible Kubernetes UI that can be deployed in-cluster or used as a desktop application.

## Infrastructure[](https://kubernetes.io/docs/concepts/cluster-administration/addons/#infrastructure)
* [KubeVirt](https://kubevirt.io/user-guide/#/installation/installation) is an add-on to run virtual machines on Kubernetes. Usually run on bare-metal clusters.
* The [node problem detector](https://github.com/kubernetes/node-problem-detector) runs on Linux nodes and reports system issues as either [Events](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/event-v1/) or [Node conditions](https://kubernetes.io/docs/concepts/architecture/nodes/#condition).

## Instrumentation[](https://kubernetes.io/docs/concepts/cluster-administration/addons/#instrumentation)
* [kube-state-metrics](https://kubernetes.io/docs/concepts/cluster-administration/kube-state-metrics/)

## Legacy Add-ons[](https://kubernetes.io/docs/concepts/cluster-administration/addons/#legacy-add-ons)

There are several other add-ons documented in the deprecated [cluster/addons](https://git.k8s.io/kubernetes/cluster/addons) directory.

Well-maintained ones should be linked to here. PRs welcome!

## Feedback

Was this page helpful?Yes No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes). Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to [report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io) or [suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).const yes=document.querySelector(".feedback--yes"),no=document.querySelector(".feedback--no");document.querySelectorAll(".feedback--link").forEach(e=>{e.href=e.href+window.location.pathname});const sendFeedback=e=>{typeof gtag=="function"?gtag("event","page_helpful",{event_category:"Helpful",event_label:window.location.pathname,value:e}):console.log("gtag not available; skipping analytics event")},disableButtons=()=>{yes.disabled=!0,yes.classList.add("feedback--button__disabled"),no.disabled=!0,no.classList.add("feedback--button__disabled")};yes.addEventListener("click",()=>{sendFeedback(100),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")}),no.addEventListener("click",()=>{sendFeedback(0),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")})Last modified April 14, 2026 at 1:15 AM PST: [fix(links): update kubernetes/community links from master to main (03c191bcc4)](https://github.com/kubernetes/website/commit/03c191bcc446f9c15a9e68d6cd1154b53bde4291)

---



# Source: https://kubernetes.io/docs/concepts/cluster-administration/coordinated-leader-election/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Cluster Administration](https://kubernetes.io/docs/concepts/cluster-administration/)
4. Coordinated Leader Election

# Coordinated Leader ElectionFEATURE STATE: `Kubernetes v1.33 [beta]`(disabled by default)

Kubernetes 1.36 includes a beta feature that allows [control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane) components to deterministically select a leader via coordinated leader election. This is useful to satisfy Kubernetes version skew constraints during cluster upgrades. Currently, the only builtin selection strategy is `OldestEmulationVersion`, preferring the leader with the lowest emulation version, followed by binary version, followed by creation timestamp.

## Enabling coordinated leader election[](https://kubernetes.io/docs/concepts/cluster-administration/coordinated-leader-election/#enabling-coordinated-leader-election)

Ensure that `CoordinatedLeaderElection` [feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) is enabled when you start the [API Server](https://kubernetes.io/docs/concepts/architecture/#kube-apiserver): and that the `coordination.k8s.io/v1beta1` API group is enabled.

This can be done by setting flags `--feature-gates="CoordinatedLeaderElection=true"` and `--runtime-config="coordination.k8s.io/v1beta1=true"`.

## Component configuration[](https://kubernetes.io/docs/concepts/cluster-administration/coordinated-leader-election/#component-configuration)

Provided that you have enabled the `CoordinatedLeaderElection` feature gate and
have the `coordination.k8s.io/v1beta1` API group enabled, compatible control plane
components automatically use the LeaseCandidate and Lease APIs to elect a leader
as needed.

For Kubernetes 1.36, two control plane components
(kube-controller-manager and kube-scheduler) automatically use coordinated
leader election when the feature gate and API group are enabled.

## Leader selection for Kubernetes components[](https://kubernetes.io/docs/concepts/cluster-administration/coordinated-leader-election/#leader-selection-for-kubernetes-components)

Kubernetes uses the [Lease API](https://kubernetes.io/docs/concepts/architecture/leases/) to perform leader election among multiple instances of the same control-plane component in a high-availability cluster, such as `kube-controller-manager` or `kube-scheduler`.

A [Lease](https://kubernetes.io/docs/concepts/architecture/leases/) acts as a lightweight distributed lock. stored by the [Kubernetes API server](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/). All running instances of a component watch or periodically read the relevant Lease object to determine which instance is currently acting as the leader.

The [Lease API](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/lease-v1/) defines fields such as:`holderIdentity`the identity (for example: pod name or hostname-based string) of the current leader.`acquireTime`timestamp when leadership was acquired.`renewTime`timestamp of the most recent renewal by the leader.`leaseDurationSeconds`the validity period of the lease (candidates should wait this long plus a small grace period before attempting to acquire an expired lease).`leaseTransitions`counter of how many times leadership has changed hands.

These fields indicate which instance holds leadership and how long that leadership remains valid.

When the [Lease](https://kubernetes.io/docs/concepts/architecture/leases/) does not exist or has expired (current time > `renewTime` + `leaseDurationSeconds`), candidate instances attempt to update the Lease with their identity. Kubernetes relies on optimistic concurrency control via the object's `resourceVersion`: only one update succeeds due to version mismatch on concurrent attempts. The instance whose update is accepted becomes the leader.

Kubernetes uses the [LeaseCandidate](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/lease-candidate-v1beta1/) API to manage leader elections. Control plane components such as `kube-controller-manager` and `kube-scheduler` register their role as a candidate by creating LeaseCandidate objects, which track all instances competing for leadership and carry metadata including the candidate's identity, binary version, and emulation version.

During an election, candidates coordinate through a shared [Lease](https://kubernetes.io/docs/concepts/architecture/leases/). The Kubernetes control plane guarantees that only one candidate successfully acquires the [Lease](https://kubernetes.io/docs/concepts/architecture/leases/) and assumes the role of leader, while all others remain as followers. If the current leader fails to renew the [Lease](https://kubernetes.io/docs/concepts/architecture/leases/) within the selected timeout period, the remaining candidates compete to acquire leadership and elect a new leader.

Once elected, the leader periodically renews its Lease by updating the `renewTime` field

(for example, performing renewal every `leaseDurationSeconds` ÷ 2, in order to avoid conflicts when the [Lease](https://kubernetes.io/docs/concepts/architecture/leases/) is about to expire). As long as renewals occur before the lease expires, the current leader instance retains leadership. If the leader crashes, becomes unreachable, or stops renewing the Lease, that Lease expires. Other healthy instances detect the expired Lease and attempt a new election.

This mechanism ensures that even though multiple replicas of a component may be running for stability and recovery, only one instance actively performs control tasks at a time, while the others remain on standby, watching the Lease and ready to take over quickly if needed.

## Feedback

Was this page helpful?Yes No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes). Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to [report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io) or [suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).const yes=document.querySelector(".feedback--yes"),no=document.querySelector(".feedback--no");document.querySelectorAll(".feedback--link").forEach(e=>{e.href=e.href+window.location.pathname});const sendFeedback=e=>{typeof gtag=="function"?gtag("event","page_helpful",{event_category:"Helpful",event_label:window.location.pathname,value:e}):console.log("gtag not available; skipping analytics event")},disableButtons=()=>{yes.disabled=!0,yes.classList.add("feedback--button__disabled"),no.disabled=!0,no.classList.add("feedback--button__disabled")};yes.addEventListener("click",()=>{sendFeedback(100),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")}),no.addEventListener("click",()=>{sendFeedback(0),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")})Last modified March 09, 2026 at 6:43 PM PST: [Lease API (7d0638aae7)](https://github.com/kubernetes/website/commit/7d0638aae73425ce7d12dabf5b5867b1f30819fa)

---



# Source (Sub-link): https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Tasks](https://kubernetes.io/docs/tasks/)
3. [Administer a Cluster](https://kubernetes.io/docs/tasks/administer-cluster/)
4. Using sysctls in a Kubernetes Cluster

# Using sysctls in a Kubernetes ClusterFEATURE STATE: `Kubernetes v1.21 [stable]`

This document describes how to configure and use kernel parameters within a Kubernetes cluster using the [sysctl](https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/) interface.

#### Note:Starting from Kubernetes version 1.23, the kubelet supports the use of either `/` or `.` as separators for sysctl names. Starting from Kubernetes version 1.25, setting Sysctls for a Pod supports setting sysctls with slashes. For example, you can represent the same sysctl name as `kernel.shm_rmid_forced` using a period as the separator, or as `kernel/shm_rmid_forced` using a slash as a separator. For more sysctl parameter conversion method details, please refer to the page [sysctl.d(5)](https://man7.org/linux/man-pages/man5/sysctl.d.5.html) from the Linux man-pages project.

## Before you begin[](https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/#before-you-begin)

#### Note:`sysctl` is a Linux-specific command-line tool used to configure various kernel parameters and it is not available on non-Linux operating systems.

---



# Source (Sub-link): https://kubernetes.io/docs/tasks/administer-cluster/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Tasks](https://kubernetes.io/docs/tasks/)
3. Administer a Cluster

# Administer a ClusterLearn common tasks for administering a cluster.

##### [Administration with kubeadm](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/)

##### [Overprovision Node Capacity For A Cluster](https://kubernetes.io/docs/tasks/administer-cluster/node-overprovisioning/)

---

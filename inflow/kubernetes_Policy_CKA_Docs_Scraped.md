# Consolidated kubernetes Policy CKA Docs.md

This file is automatically scraped and consolidated by the batch ingestion pipeline.



# Source: https://kubernetes.io/docs/concepts/policy/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. Policies

# PoliciesManage security and best-practices with policies.

Kubernetes policies are configurations that manage other configurations or runtime behaviors. Kubernetes offers various forms of policies, described below:

## Apply policies using API objects[](https://kubernetes.io/docs/concepts/policy/#apply-policies-using-api-objects)

Some API objects act as policies. Here are some examples:
* [NetworkPolicies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) can be used to restrict ingress and egress traffic for a workload.
* [LimitRanges](https://kubernetes.io/docs/concepts/policy/limit-range/) manage resource allocation constraints across different object kinds.
* [ResourceQuotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/) limit resource consumption for a [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces).

## Apply policies using admission controllers[](https://kubernetes.io/docs/concepts/policy/#apply-policies-using-admission-controllers)

An [admission controller](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) runs in the API server and can validate or mutate API requests. Some admission controllers act to apply policies. For example, the [AlwaysPullImages](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#alwayspullimages) admission controller modifies a new Pod to set the image pull policy to `Always`.

Kubernetes has several built-in admission controllers that are configurable via the API server `--enable-admission-plugins` flag.

Details on admission controllers, with the complete list of available admission controllers, are documented in a dedicated section:
* [Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/)

## Apply policies using ValidatingAdmissionPolicy[](https://kubernetes.io/docs/concepts/policy/#apply-policies-using-validatingadmissionpolicy)

Validating admission policies allow configurable validation checks to be executed in the API server using the Common Expression Language (CEL). For example, a `ValidatingAdmissionPolicy` can be used to disallow use of the `latest` image tag.

A `ValidatingAdmissionPolicy` operates on an API request and can be used to block, audit, and warn users about non-compliant configurations.

Details on the `ValidatingAdmissionPolicy` API, with examples, are documented in a dedicated section:
* [Validating Admission Policy](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/)

## Apply policies using dynamic admission control[](https://kubernetes.io/docs/concepts/policy/#apply-policies-using-dynamic-admission-control)

Dynamic admission controllers (or admission webhooks) run outside the API server as separate applications that register to receive webhooks requests to perform validation or mutation of API requests.

Dynamic admission controllers can be used to apply policies on API requests and trigger other policy-based workflows. A dynamic admission controller can perform complex checks including those that require retrieval of other cluster resources and external data. For example, an image verification check can lookup data from OCI registries to validate the container image signatures and attestations.

Details on dynamic admission control are documented in a dedicated section:
* [Dynamic Admission Control](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/)

### Implementations[](https://kubernetes.io/docs/concepts/policy/#implementations-admission-control)Note: This section links to third party projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for these projects, which are listed alphabetically. To add a project to this list, read the [content guide](https://kubernetes.io/docs/contribute/style/content-guide/#third-party-content) before submitting a change. [More information.](https://kubernetes.io/docs/concepts/policy/#third-party-content-disclaimer)

Dynamic Admission Controllers that act as flexible policy engines are being developed in the Kubernetes ecosystem, such as:
* [Kubewarden](https://github.com/kubewarden)
* [Kyverno](https://kyverno.io)
* [OPA Gatekeeper](https://github.com/open-policy-agent/gatekeeper)
* [Polaris](https://polaris.docs.fairwinds.com/admission-controller/)

## Apply policies using Kubelet configurations[](https://kubernetes.io/docs/concepts/policy/#apply-policies-using-kubelet-configurations)

Kubernetes allows configuring the Kubelet on each worker node. Some Kubelet configurations act as policies:
* [Process ID limits and reservations](https://kubernetes.io/docs/concepts/policy/pid-limiting/) are used to limit and reserve allocatable PIDs.
* [Node Resource Managers](https://kubernetes.io/docs/concepts/policy/node-resource-managers/) can manage compute, memory, and device resources for latency-critical and high-throughput workloads.

---



# Source: https://kubernetes.io/docs/concepts/policy/limit-range/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Policies](https://kubernetes.io/docs/concepts/policy/)
4. Limit Ranges

# Limit Ranges

By default, containers run with unbounded [compute resources](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) on a Kubernetes cluster. Using Kubernetes [resource quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/), administrators (also termed cluster operators) can restrict consumption and creation of cluster resources (such as CPU time, memory, and persistent storage) within a specified [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces). Within a namespace, a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/) can consume as much CPU and memory as is allowed by the ResourceQuotas that apply to that namespace. As a cluster operator, or as a namespace-level administrator, you might also be concerned about making sure that a single object cannot monopolize all available resources within a namespace.

A LimitRange is a policy to constrain the resource allocations (limits and requests) that you can specify for each applicable object kind (such as Pod or [PersistentVolumeClaim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims)) in a namespace.

A LimitRange provides constraints that can:
* Enforce minimum and maximum compute resources usage per Pod or Container in a namespace.
* Enforce minimum and maximum storage request per [PersistentVolumeClaim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) in a namespace.
* Enforce a ratio between request and limit for a resource in a namespace.
* Set default request/limit for compute resources in a namespace and automatically inject them to Containers at runtime.

Kubernetes constrains resource allocations to Pods in a particular namespace whenever there is at least one LimitRange object in that namespace.

The name of a LimitRange object must be a valid [DNS subdomain name](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names).

## Constraints on resource limits and requests[](https://kubernetes.io/docs/concepts/policy/limit-range/#constraints-on-resource-limits-and-requests)
* The administrator creates a LimitRange in a namespace.
* Users create (or try to create) objects in that namespace, such as Pods or PersistentVolumeClaims.
* First, the LimitRange admission controller applies default request and limit values for all Pods (and their containers) that do not set compute resource requirements.
* Second, the LimitRange tracks usage to ensure it does not exceed resource minimum, maximum and ratio defined in any LimitRange present in the namespace.
* If you attempt to create or update an object (Pod or PersistentVolumeClaim) that violates a LimitRange constraint, your request to the API server will fail with an HTTP status code `403 Forbidden` and a message explaining the constraint that has been violated.
* If you add a LimitRange in a namespace that applies to compute-related resources such as `cpu` and `memory`, you must specify requests or limits for those values. Otherwise, the system may reject Pod creation.
* LimitRange validations occur only at Pod admission stage, not on running Pods. If you add or modify a LimitRange, the Pods that already exist in that namespace continue unchanged.
* If two or more LimitRange objects exist in the namespace, it is not deterministic which default value will be applied.

## LimitRange and admission checks for Pods[](https://kubernetes.io/docs/concepts/policy/limit-range/#limitrange-and-admission-checks-for-pods)

A LimitRange does not check the consistency of the default values it applies. This means that a default value for the limit that is set by LimitRange may be less than the request value specified for the container in the spec that a client submits to the API server. If that happens, the final Pod will not be schedulable.

For example, you define a LimitRange with below manifest:

#### Note:The following examples operate within the default namespace of your cluster, as the namespace parameter is undefined and the LimitRange scope is limited to the namespace level. This implies that any references or operations within these examples will interact with elements within the default namespace of your cluster. You can override the operating namespace by configuring namespace in the `metadata.namespace` field.[`concepts/policy/limit-range/problematic-limit-range.yaml` ](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/concepts/policy/limit-range/problematic-limit-range.yaml)

![Diagram](https://kubernetes.io/images/copycode.svg)

```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: cpu-resource-constraint
spec:
  limits:
  - default: # this section defines default limits
      cpu: 500m
    defaultRequest: # this section defines default requests
      cpu: 500m
    max: # max and min define the limit range
      cpu: "1"
    min:
      cpu: 100m
    type: Container
```

---



# Source: https://kubernetes.io/docs/concepts/policy/resource-quotas/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Policies](https://kubernetes.io/docs/concepts/policy/)
4. Resource Quotas

# Resource Quotas

When several users or teams share a cluster with a fixed number of nodes, there is a concern that one team could use more than its fair share of resources.

Resource quotas are a tool for administrators to address this concern.

A resource quota, defined by a ResourceQuota object, provides constraints that limit aggregate resource consumption per [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces). A ResourceQuota can also limit the [quantity of objects that can be created in a namespace](https://kubernetes.io/docs/concepts/policy/resource-quotas/#quota-on-object-count) by API kind, as well as the total amount of [infrastructure resources](https://kubernetes.io/docs/reference/glossary/?all=true#term-infrastructure-resource) that may be consumed by API objects found in that namespace.

#### Caution:Neither contention nor changes to quota will affect already created resources.

## How Kubernetes ResourceQuotas work[](https://kubernetes.io/docs/concepts/policy/resource-quotas/#how-kubernetes-resourcequotas-work)

ResourceQuotas work like this:
* 

Different teams work in different namespaces. This separation can be enforced with [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) or any other [authorization](https://kubernetes.io/docs/reference/access-authn-authz/authorization/) mechanism.
* 

A cluster administrator creates at least one ResourceQuota for each namespace.
  * To make sure the enforcement stays enforced, the cluster administrator should also restrict access to delete or update that ResourceQuota; for example, by defining a [ValidatingAdmissionPolicy](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/).
* 

Users create resources (pods, services, etc.) in the namespace, and the quota system tracks usage to ensure it does not exceed hard resource limits defined in a ResourceQuota.

You can apply a [scope](https://kubernetes.io/docs/concepts/policy/resource-quotas/#quota-scopes) to a ResourceQuota to limit where it applies,
* 

If creating or updating a resource violates a quota constraint, the control plane rejects that request with HTTP status code `403 Forbidden`. The error includes a message explaining the constraint that would have been violated.
* 

If quotas are enabled in a namespace for [resource](https://kubernetes.io/docs/reference/glossary/?all=true#term-infrastructure-resource) such as `cpu` and `memory`, users must specify requests or limits for those values when they define a Pod; otherwise, the quota system may reject pod creation.

The resource quota [walkthrough](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/) shows an example of how to avoid this problem.

#### Note:
* You can define a [LimitRange](https://kubernetes.io/docs/concepts/policy/limit-range/) to force defaults on pods that make no compute resource requirements (so that users don't have to remember to do that).

You often do not create Pods directly; for example, you more usually create a [workload management](https://kubernetes.io/docs/concepts/workloads/controllers/) object such as a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/). If you create a Deployment that tries to use more resources than are available, the creation of the Deployment (or other workload management object) succeeds, but the Deployment may not be able to get all of the Pods it manages to exist. In that case you can check the status of the Deployment, for example with `kubectl describe`, to see what has happened.
* For `cpu` and `memory` resources, ResourceQuotas enforce that every (new) pod in that namespace sets a limit for that resource. If you enforce a resource quota in a namespace for either `cpu` or `memory`, you and other clients, must specify either `requests` or `limits` for that resource, for every new Pod you submit. If you don't, the control plane may reject admission for that Pod.
* For other resources: ResourceQuota works and will ignore pods in the namespace without setting a limit or request for that resource. It means that you can create a new pod without limit/request for ephemeral storage if the resource quota limits the ephemeral storage of this namespace.

You can use a [LimitRange](https://kubernetes.io/docs/concepts/policy/limit-range/) to automatically set a default request for these resources.

The name of a ResourceQuota object must be a valid [DNS subdomain name](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names).

Examples of policies that could be created using namespaces and quotas are:
* In a cluster with a capacity of 32 GiB RAM, and 16 cores, let team A use 20 GiB and 10 cores, let B use 10GiB and 4 cores, and hold 2GiB and 2 cores in reserve for future allocation.
* Limit the "testing" namespace to using 1 core and 1GiB RAM. Let the "production" namespace use any amount.

In the case where the total capacity of the cluster is less than the sum of the quotas of the namespaces, there may be contention for resources. This is handled on a first-come-first-served basis.

## Enabling Resource Quota[](https://kubernetes.io/docs/concepts/policy/resource-quotas/#enabling-resource-quota)

ResourceQuota support is enabled by default for many Kubernetes distributions. It is enabled when the [API server](https://kubernetes.io/docs/concepts/architecture/#kube-apiserver) `--enable-admission-plugins=` flag has `ResourceQuota` as one of its arguments.

A resource quota is enforced in a particular namespace when there is a ResourceQuota in that namespace.

## Types of resource quota[](https://kubernetes.io/docs/concepts/policy/resource-quotas/#types-of-resource-quota)

The ResourceQuota mechanism lets you enforce different kinds of limits. This section describes the types of limit that you can enforce.

### Quota for infrastructure resources[](https://kubernetes.io/docs/concepts/policy/resource-quotas/#compute-resource-quota)

You can limit the total sum of [compute resources](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) that can be requested in a given namespace.

The following resource types are supported:``````````````````

| Resource Name | Description || --- | --- || limits.cpu | Across all pods in a non-terminal state, the sum of CPU limits cannot exceed this value. || limits.memory | Across all pods in a non-terminal state, the sum of memory limits cannot exceed this value. || requests.cpu | Across all pods in a non-terminal state, the sum of CPU requests cannot exceed this value. || requests.memory | Across all pods in a non-terminal state, the sum of memory requests cannot exceed this value. || hugepages-<size> | Across all pods in a non-terminal state, the number of huge page requests of the specified size cannot exceed this value. || cpu | Same as requests.cpu || memory | Same as requests.memory |

### Quota for extended resources[](https://kubernetes.io/docs/concepts/policy/resource-quotas/#quota-for-extended-resources)

In addition to the resources mentioned above, in release 1.10, quota support for [extended resources](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#extended-resources) is added.

As overcommit is not allowed for extended resources, it makes no sense to specify both `requests` and `limits` for the same extended resource in a quota. So for extended resources, only quota items with prefix `requests.` are allowed.

Take the GPU resource as an example, if the resource name is `nvidia.com/gpu`, and you want to limit the total number of GPUs requested in a namespace to 4, you can define a quota as follows:
* `requests.nvidia.com/gpu: 4`

See [Viewing and Setting Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/#viewing-and-setting-quotas) for more details.

### Quota for DRA resource claims[](https://kubernetes.io/docs/concepts/policy/resource-quotas/#quota-for-dra-resource-claims)

DRA (Dynamic Resource Allocation) resource claims can request DRA resources by device class. For an example device class named `examplegpu`, you want to limit the total number of GPUs requested in a namespace to 4, you can define a quota as follows:
* `examplegpu.deviceclass.resource.k8s.io/devices: 4`

When [Extended Resource allocation by DRA](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#extended-resource) is enabled, the same device class named `examplegpu` can be requested via extended resource either explicitly when the device class's ExtendedResourceName field is given, say, `example.com/gpu`, then you can define a quota as follows:
* `requests.example.com/gpu: 4`

or implicitly using the derived extended resource name from device class name `examplegpu`, you can define a quota as follows:
* `requests.deviceclass.resource.kubernetes.io/examplegpu: 4`

All devices requested from resource claims or extended resources are counted towards all three quotas listed above. The extended resource quota e.g. `requests.example.com/gpu: 4`, also counts the devices provided by device plugin.

See [Viewing and Setting Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/#viewing-and-setting-quotas) for more details.

### Quota for storage[](https://kubernetes.io/docs/concepts/policy/resource-quotas/#quota-for-storage)

You can limit the total sum of [storage](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) for volumes that can be requested in a given namespace.

In addition, you can limit consumption of storage resources based on associated [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/).````[](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims)````````[](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims)

| Resource Name | Description || --- | --- || requests.storage | Across all persistent volume claims, the sum of storage requests cannot exceed this value. || persistentvolumeclaims | The total number of PersistentVolumeClaims that can exist in the namespace. || <storage-class-name>.storageclass.storage.k8s.io/requests.storage | Across all persistent volume claims associated with the <storage-class-name>, the sum of storage requests cannot exceed this value. || <storage-class-name>.storageclass.storage.k8s.io/persistentvolumeclaims | Across all persistent volume claims associated with the <storage-class-name>, the total number of persistent volume claims that can exist in the namespace. |

For example, if you want to quota storage with `gold` StorageClass separate from a `bronze` StorageClass, you can define a quota as follows:
* `gold.storageclass.storage.k8s.io/requests.storage: 500Gi`
* `bronze.storageclass.storage.k8s.io/requests.storage: 100Gi`

#### Quota for local ephemeral storage[](https://kubernetes.io/docs/concepts/policy/resource-quotas/#quota-for-local-ephemeral-storage)FEATURE STATE: `Kubernetes v1.8 [alpha]`

---



# Source: https://kubernetes.io/docs/concepts/policy/pid-limiting/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Policies](https://kubernetes.io/docs/concepts/policy/)
4. Process ID Limits And Reservations

# Process ID Limits And ReservationsFEATURE STATE: `Kubernetes v1.20 [stable]`

Kubernetes allow you to limit the number of process IDs (PIDs) that a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/) can use. You can also reserve a number of allocatable PIDs for each [node](https://kubernetes.io/docs/concepts/architecture/nodes/) for use by the operating system and daemons (rather than by Pods).

Process IDs (PIDs) are a fundamental resource on nodes. It is trivial to hit the task limit without hitting any other resource limits, which can then cause instability to a host machine.

Cluster administrators require mechanisms to ensure that Pods running in the cluster cannot induce PID exhaustion that prevents host daemons (such as the [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet) or [kube-proxy](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/), and potentially also the container runtime) from running. In addition, it is important to ensure that PIDs are limited among Pods in order to ensure they have limited impact on other workloads on the same node.

#### Note:On certain Linux installations, the operating system sets the PIDs limit to a low default, such as `32768`. Consider raising the value of `/proc/sys/kernel/pid_max`.

You can configure a kubelet to limit the number of PIDs a given Pod can consume. For example, if your node's host OS is set to use a maximum of `262144` PIDs and expect to host less than `250` Pods, one can give each Pod a budget of `1000` PIDs to prevent using up that node's overall number of available PIDs. If the admin wants to overcommit PIDs similar to CPU or memory, they may do so as well with some additional risks. Either way, a single Pod will not be able to bring the whole machine down. This kind of resource limiting helps to prevent simple fork bombs from affecting operation of an entire cluster.

Per-Pod PID limiting allows administrators to protect one Pod from another, but does not ensure that all Pods scheduled onto that host are unable to impact the node overall. Per-Pod limiting also does not protect the node agents themselves from PID exhaustion.

You can also reserve an amount of PIDs for node overhead, separate from the allocation to Pods. This is similar to how you can reserve CPU, memory, or other resources for use by the operating system and other facilities outside of Pods and their containers.

PID limiting is an important sibling to [compute resource](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) requests and limits. However, you specify it in a different way: rather than defining a Pod's resource limit in the `.spec` for a Pod, you configure the limit as a setting on the kubelet. Pod-defined PID limits are not currently supported.

#### Caution:This means that the limit that applies to a Pod may be different depending on where the Pod is scheduled. To make things simple, it's easiest if all Nodes use the same PID resource limits and reservations.

---



# Source (Sub-link): https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Overview](https://kubernetes.io/docs/concepts/overview/)
4. [Objects In Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/)
5. Namespaces

# Namespaces

In Kubernetes, namespaces provide a mechanism for isolating groups of resources within a single cluster. Names of resources need to be unique within a namespace, but not across namespaces. Namespace-based scoping is applicable only for namespaced [objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects) (e.g. Deployments, Services, etc.) and not for cluster-wide objects (e.g. StorageClass, Nodes, PersistentVolumes, etc.).

## When to Use Multiple Namespaces[](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces#when-to-use-multiple-namespaces)

Namespaces are intended for use in environments with many users spread across multiple teams, or projects. For clusters with a few to tens of users, you should not need to create or think about namespaces at all. Start using namespaces when you need the features they provide.

Namespaces provide a scope for names. Names of resources need to be unique within a namespace, but not across namespaces. Namespaces cannot be nested inside one another and each Kubernetes resource can only be in one namespace.

Namespaces are a way to divide cluster resources between multiple users (via [resource quota](https://kubernetes.io/docs/concepts/policy/resource-quotas/)).

It is not necessary to use multiple namespaces to separate slightly different resources, such as different versions of the same software: use [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels) to distinguish resources within the same namespace.

#### Note:For a production cluster, consider not using the `default` namespace. Instead, make other namespaces and use those.

## Initial namespaces[](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces#initial-namespaces)

Kubernetes starts with four initial namespaces:`default`Kubernetes includes this namespace so that you can start using your new cluster without first creating a namespace.`kube-node-lease`This namespace holds [Lease](https://kubernetes.io/docs/concepts/architecture/leases/) objects associated with each node. Node leases allow the kubelet to send [heartbeats](https://kubernetes.io/docs/concepts/architecture/nodes/#node-heartbeats) so that the control plane can detect node failure.`kube-public`This namespace is readable by all clients (including those not authenticated). This namespace is mostly reserved for cluster usage, in case that some resources should be visible and readable publicly throughout the whole cluster. The public aspect of this namespace is only a convention, not a requirement.`kube-system`The namespace for objects created by the Kubernetes system.

## Working with Namespaces[](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces#working-with-namespaces)

Creation and deletion of namespaces are described in the [Admin Guide documentation for namespaces](https://kubernetes.io/docs/tasks/administer-cluster/namespaces/).

#### Note:Avoid creating namespaces with the prefix `kube-`, since it is reserved for Kubernetes system namespaces.

### Viewing namespaces[](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces#viewing-namespaces)

You can list the current namespaces in a cluster using:
```yaml
kubectl get namespace
```

---



# Source (Sub-link): https://kubernetes.io/docs/concepts/policy/node-resource-managers/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Workloads](https://kubernetes.io/docs/concepts/workloads/)
4. Resource managers

# Resource managers

In order to support latency-critical and high-throughput workloads, Kubernetes offers a suite of Resource Managers. The managers aim to co-ordinate and optimize the alignment of node's resources for pods configured with a specific requirement for CPUs, devices, and memory (hugepages) resources.

## Topology manager[](https://kubernetes.io/docs/concepts/policy/node-resource-managers/#topology-manager)FEATURE STATE: `Kubernetes v1.27 [stable]`(enabled by default)

Topology Manager is a kubelet component that aims to coordinate the set of components that are responsible for these optimizations. To learn more, read [Control Topology Management Policies on a Node](https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/).

## CPU manager[](https://kubernetes.io/docs/concepts/policy/node-resource-managers/#cpu-manager)FEATURE STATE: `Kubernetes v1.26 [stable]`(enabled by default)

CPU Manager is a kubelet component that provides exclusive resource allocation for CPU resources. It consults with the Topology Manager to make resource assignment decisions. To learn more, read [Control CPU Management Policies on the Node](https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/).

### Policies for assigning CPUs to Pods[](https://kubernetes.io/docs/concepts/policy/node-resource-managers/#policies-for-assigning-cpus-to-pods)

Once a Pod is bound to a Node, the kubelet on that node may need to either multiplex the existing hardware (for example, sharing CPUs across multiple Pods) or allocate hardware by dedicating some resource (for example, assigning one of more CPUs for a Pod's exclusive use).

By default, the kubelet uses [CFS quota](https://en.wikipedia.org/wiki/Completely_Fair_Scheduler) to enforce pod CPU limits. When the node runs many CPU-bound pods, the workload can move to different CPU cores depending on whether the pod is throttled and which CPU cores are available at scheduling time. Many workloads are not sensitive to this migration and thus work fine without any intervention.

However, in workloads where CPU cache affinity and scheduling latency significantly affect workload performance, the kubelet allows alternative CPU management policies to determine some placement preferences on the node. This is implemented using the CPU Manager and its policy. There are two available policies:
* `none`: the `none` policy explicitly enables the existing default CPU affinity scheme, providing no affinity beyond what the OS scheduler does automatically. Limits on CPU usage for [Guaranteed pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/) and [Burstable pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/) are enforced using CFS quota.
* `static`: the `static` policy allows containers in `Guaranteed` pods with integer CPU `requests` access to exclusive CPUs on the node. This exclusivity is enforced using the [cpuset cgroup controller](https://www.kernel.org/doc/Documentation/cgroup-v2.txt).

#### Note:System services such as the container runtime and the kubelet itself can continue to run on these exclusive CPUs. The exclusivity only extends to other pods.

---



# Source (Sub-link): https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Configuration](https://kubernetes.io/docs/concepts/configuration/)
4. Resource Management for Pods and Containers

# Resource Management for Pods and Containers

When you specify a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/), you can optionally specify how much of each resource a [container](https://kubernetes.io/docs/concepts/containers/) needs. The most common resources to specify are CPU and memory (RAM); there are others.

When you specify the resource request for containers in a Pod, the [kube-scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/) uses this information to decide which node to place the Pod on. When you specify a resource limit for a container, the [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet) enforces those limits so that the running container is not allowed to use more of that resource than the limit you set. The kubelet also reserves at least the request amount of that system resource specifically for that container to use.

## Requests and limits[](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#requests-and-limits)

If the node where a Pod is running has enough of a resource available, it's possible (and allowed) for a container to use more resource than its `request` for that resource specifies.

For example, if you set a `memory` request of 256 MiB for a container, and that container is in a Pod scheduled to a Node with 8GiB of memory and no other Pods, then the container can try to use more RAM.

Limits are a different story. Both `cpu` and `memory` limits are applied by the kubelet (and [container runtime](https://kubernetes.io/docs/setup/production-environment/container-runtimes)), and are ultimately enforced by the kernel. On Linux nodes, the Linux kernel enforces limits with [cgroups](https://kubernetes.io/docs/reference/glossary/?all=true#term-cgroup). The behavior of `cpu` and `memory` limit enforcement is slightly different.

`cpu` limits are enforced by CPU throttling. When a container approaches its `cpu` limit, the kernel will restrict access to the CPU corresponding to the container's limit. Thus, a `cpu` limit is a hard limit the kernel enforces. Containers may not use more CPU than is specified in their `cpu` limit.

`memory` limits are enforced by the kernel with out of memory (OOM) kills. When a container uses more than its `memory` limit, the kernel may terminate it. However, terminations only happen when the kernel detects memory pressure. Thus, a container that over allocates memory may not be immediately killed. This means `memory` limits are enforced reactively. A container may use more memory than its `memory` limit, but if it does, it may get killed.

#### Note:There is an alpha feature `MemoryQoS` which adds memory throttling and optional tiered memory reservation on Linux nodes using cgroup v2. For details, see [Memory QoS with cgroup v2](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#memory-qos-with-cgroup-v2).

#### Note:If you specify a limit for a resource, but do not specify any request, and no admission-time mechanism has applied a default request for that resource, then Kubernetes copies the limit you specified and uses it as the requested value for the resource.

## Resource types[](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-types)

A resource type has a base unit and can be requested, limited, or both. Kubernetes has the following built-in resource types:``````[](https://kubernetes.io/docs/concepts/storage/ephemeral-storage/)``[](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#huge-pages)

| Resource type | Description | Base unit || --- | --- | --- || cpu | Compute processing | cpu (core) || memory | RAM | Bytes || ephemeral-storage | Local ephemeral storage | Bytes || hugepages-<size> | Huge pages (Linux only) | Bytes |

Clusters can also provide [extended resources](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#extended-resources) (resources with a custom name, typically exposed by device plugins).

### Huge pages[](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#huge-pages)

For Linux workloads, you can specify huge page resources. Huge pages are a Linux-specific feature where the node kernel allocates blocks of memory that are much larger than the default page size.

For example, on a system where the default page size is 4KiB, you could specify a limit, `hugepages-2Mi: 80Mi`. If the container tries allocating over 40 2MiB huge pages (a total of 80 MiB), that allocation fails.

#### Note:You cannot overcommit `hugepages-*` resources. This is different from the `memory` and `cpu` resources.

---



# Source (Sub-link): https://kubernetes.io/docs/concepts/overview/working-with-objects/names/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Overview](https://kubernetes.io/docs/concepts/overview/)
4. [Objects In Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/)
5. Object Names and IDs

# Object Names and IDs

Each [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects) in your cluster has a [Name](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names) that is unique for that type of resource. Every Kubernetes object also has a [UID](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids) that is unique across your whole cluster.

For example, you can only have one Pod named `myapp-1234` within the same [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/), but you can have one Pod and one Deployment that are each named `myapp-1234`.

For non-unique user-provided attributes, Kubernetes provides [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) and [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).

## Names[](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names)

A client-provided string that refers to an object in a [resource](https://kubernetes.io/docs/reference/using-api/api-concepts/#standard-api-terminology) URL, such as `/api/v1/pods/some-name`.

Only one object of a given kind can have a given name at a time. However, if you delete the object, you can make a new object with the same name.

Names must be unique across all [API versions](https://kubernetes.io/docs/concepts/overview/kubernetes-api/#api-groups-and-versioning) of the same resource.

Kubernetes uniquely identifies objects using a combination of four attributes:
* API group (e.g., `apps`)
* Resource type (e.g., `deployments`)
* Namespace (for namespaced resources)
* Name

While you can access a resource through different API versions (such as `v1` or `v1beta1`), the version is simply a different representation of the same underlying object. Because the version is not part of the unique identification, you cannot create two objects with the same name and resource type in the same namespace by using different API versions.

#### Note:In cases when objects represent a physical entity, like a Node representing a physical host, when the host is re-created under the same name without deleting and re-creating the Node, Kubernetes treats the new host as the old one, which may lead to inconsistencies.

The server may generate a name when `generateName` is provided instead of `name` in a resource create request. When `generateName` is used, the provided value is used as a name prefix, which server appends a generated suffix to. Even though the name is generated, it may conflict with existing names resulting in an HTTP 409 response. This became far less likely to happen in Kubernetes v1.31 and later, since the server will make up to 8 attempts to generate a unique name before returning an HTTP 409 response.

Below are four types of commonly used name constraints for resources.

### DNS Subdomain Names[](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names)

Most resource types require a name that can be used as a DNS subdomain name as defined in [RFC 1123](https://tools.ietf.org/html/rfc1123). This means the name must:
* contain no more than 253 characters
* contain only lowercase alphanumeric characters, '-' or '.'
* start with an alphanumeric character
* end with an alphanumeric character

### RFC 1123 Label Names[](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-label-names)

Some resource types require their names to follow the DNS label standard as defined in [RFC 1123](https://tools.ietf.org/html/rfc1123). This means the name must:
* contain at most 63 characters
* contain only lowercase alphanumeric characters or '-'
* start with an alphabetic character
* end with an alphanumeric character

#### Note:When the `RelaxedServiceNameValidation` feature gate is enabled, Service object names are allowed to start with a digit.

### RFC 1035 Label Names[](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#rfc-1035-label-names)

Some resource types require their names to follow the DNS label standard as defined in [RFC 1035](https://tools.ietf.org/html/rfc1035). This means the name must:
* contain at most 63 characters
* contain only lowercase alphanumeric characters or '-'
* start with an alphabetic character
* end with an alphanumeric character

#### Note:While RFC 1123 technically allows labels to start with digits, the current Kubernetes implementation requires both RFC 1035 and RFC 1123 labels to start with an alphabetic character. The exception is when the `RelaxedServiceNameValidation` feature gate is enabled for Service objects, which allows Service names to start with digits.

---

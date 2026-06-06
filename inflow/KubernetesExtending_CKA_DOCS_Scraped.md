# Consolidated KubernetesExtending CKA DOCS.md

This file is automatically scraped and consolidated by the batch ingestion pipeline.



# Source: https://kubernetes.io/docs/concepts/extend-kubernetes/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. Extending Kubernetes

# Extending KubernetesDifferent ways to change the behavior of your Kubernetes cluster.

Kubernetes is highly configurable and extensible. As a result, there is rarely a need to fork or submit patches to the Kubernetes project code.

This guide describes the options for customizing a Kubernetes cluster. It is aimed at [cluster operators](https://kubernetes.io/docs/reference/glossary/?all=true#term-cluster-operator) who want to understand how to adapt their Kubernetes cluster to the needs of their work environment. Developers who are prospective [Platform Developers](https://kubernetes.io/docs/reference/glossary/?all=true#term-platform-developer) or Kubernetes Project [Contributors](https://kubernetes.io/docs/reference/glossary/?all=true#term-contributor) will also find it useful as an introduction to what extension points and patterns exist, and their trade-offs and limitations.

Customization approaches can be broadly divided into [configuration](https://kubernetes.io/docs/concepts/extend-kubernetes/#configuration), which only involves changing command line arguments, local configuration files, or API resources; and [extensions](https://kubernetes.io/docs/concepts/extend-kubernetes/#extensions), which involve running additional programs, additional network services, or both. This document is primarily about extensions.

## Configuration[](https://kubernetes.io/docs/concepts/extend-kubernetes/#configuration)

Configuration files and command arguments are documented in the [Reference](https://kubernetes.io/docs/reference/) section of the online documentation, with a page for each binary:
* [`kube-apiserver`](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/)
* [`kube-controller-manager`](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/)
* [`kube-scheduler`](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/)
* [`kubelet`](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/)
* [`kube-proxy`](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/)

Command arguments and configuration files may not always be changeable in a hosted Kubernetes service or a distribution with managed installation. When they are changeable, they are usually only changeable by the cluster operator. Also, they are subject to change in future Kubernetes versions, and setting them may require restarting processes. For those reasons, they should be used only when there are no other options.

Built-in policy APIs, such as [ResourceQuota](https://kubernetes.io/docs/concepts/policy/resource-quotas/), [NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/network-policies/) and Role-based Access Control ([RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)), are built-in Kubernetes APIs that provide declaratively configured policy settings. APIs are typically usable even with hosted Kubernetes services and with managed Kubernetes installations. The built-in policy APIs follow the same conventions as other Kubernetes resources such as Pods. When you use a policy APIs that is [stable](https://kubernetes.io/docs/reference/using-api/#api-versioning), you benefit from a [defined support policy](https://kubernetes.io/docs/reference/using-api/deprecation-policy/) like other Kubernetes APIs. For these reasons, policy APIs are recommended over configuration files and command arguments where suitable.

## Extensions[](https://kubernetes.io/docs/concepts/extend-kubernetes/#extensions)

Extensions are software components that extend and deeply integrate with Kubernetes. They adapt it to support new types and new kinds of hardware.

Many cluster administrators use a hosted or distribution instance of Kubernetes. These clusters come with extensions pre-installed. As a result, most Kubernetes users will not need to install extensions and even fewer users will need to author new ones.

### Extension patterns[](https://kubernetes.io/docs/concepts/extend-kubernetes/#extension-patterns)

Kubernetes is designed to be automated by writing client programs. Any program that reads and/or writes to the Kubernetes API can provide useful automation. Automation can run on the cluster or off it. By following the guidance in this doc you can write highly available and robust automation. Automation generally works with any Kubernetes cluster, including hosted clusters and managed installations.

There is a specific pattern for writing client programs that work well with Kubernetes called the [controller](https://kubernetes.io/docs/concepts/architecture/controller/) pattern. Controllers typically read an object's `.spec`, possibly do things, and then update the object's `.status`.

A controller is a client of the Kubernetes API. When Kubernetes is the client and calls out to a remote service, Kubernetes calls this a webhook. The remote service is called a webhook backend. As with custom controllers, webhooks do add a point of failure.

#### Note:Outside of Kubernetes, the term “webhook” typically refers to a mechanism for asynchronous notifications, where the webhook call serves as a one-way notification to another system or component. In the Kubernetes ecosystem, even synchronous HTTP callouts are often described as “webhooks”.

In the webhook model, Kubernetes makes a network request to a remote service. With the alternative binary Plugin model, Kubernetes executes a binary (program). Binary plugins are used by the kubelet (for example, [CSI storage plugins](https://kubernetes-csi.github.io/docs/) and [CNI network plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)), and by kubectl (see [Extend kubectl with plugins](https://kubernetes.io/docs/tasks/extend-kubectl/kubectl-plugins/)).

### Extension points[](https://kubernetes.io/docs/concepts/extend-kubernetes/#extension-points)

This diagram shows the extension points in a Kubernetes cluster and the clients that access it.

![Symbolic representation of seven numbered extension points for Kubernetes](https://kubernetes.io/docs/concepts/extend-kubernetes/extension-points.png)

Kubernetes extension points

#### Key to the figure[](https://kubernetes.io/docs/concepts/extend-kubernetes/#key-to-the-figure)
1. 

Users often interact with the Kubernetes API using `kubectl`. [Plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/#client-extensions) customise the behaviour of clients. There are generic extensions that can apply to different clients, as well as specific ways to extend `kubectl`.
2. 

The API server handles all requests. Several types of extension points in the API server allow authenticating requests, or blocking them based on their content, editing content, and handling deletion. These are described in the [API Access Extensions](https://kubernetes.io/docs/concepts/extend-kubernetes/#api-access-extensions) section.
3. 

The API server serves various kinds of resources. Built-in resource kinds, such as `pods`, are defined by the Kubernetes project and can't be changed. Read [API extensions](https://kubernetes.io/docs/concepts/extend-kubernetes/#api-extensions) to learn about extending the Kubernetes API.
4. 

The Kubernetes scheduler [decides](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) which nodes to place pods on. There are several ways to extend scheduling, which are described in the [Scheduling extensions](https://kubernetes.io/docs/concepts/extend-kubernetes/#scheduling-extensions) section.
5. 

Much of the behavior of Kubernetes is implemented by programs called [controllers](https://kubernetes.io/docs/concepts/architecture/controller/), that are clients of the API server. Controllers are often used in conjunction with custom resources. Read [combining new APIs with automation](https://kubernetes.io/docs/concepts/extend-kubernetes/#combining-new-apis-with-automation) and [Changing built-in resources](https://kubernetes.io/docs/concepts/extend-kubernetes/#changing-built-in-resources) to learn more.
6. 

The kubelet runs on servers (nodes), and helps pods appear like virtual servers with their own IPs on the cluster network. [Network Plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/#network-plugins) allow for different implementations of pod networking.
7. 

You can use [Device Plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/#device-plugins) to integrate custom hardware or other special node-local facilities, and make these available to Pods running in your cluster. The kubelet includes support for working with device plugins.

The kubelet also mounts and unmounts [volume](https://kubernetes.io/docs/concepts/storage/volumes/) for pods and their containers. You can use [Storage Plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/#storage-plugins) to add support for new kinds of storage and other volume types.

#### Extension point choice flowchart[](https://kubernetes.io/docs/concepts/extend-kubernetes/#extension-flowchart)

If you are unsure where to start, this flowchart can help. Note that some solutions may involve several types of extensions.

![Flowchart with questions about use cases and guidance for implementers. Green circles indicate yes; red circles indicate no.](https://kubernetes.io/docs/concepts/extend-kubernetes/flowchart.svg)

Flowchart guide to select an extension approach

## Client extensions[](https://kubernetes.io/docs/concepts/extend-kubernetes/#client-extensions)

Plugins for kubectl are separate binaries that add or replace the behavior of specific subcommands. The `kubectl` tool can also integrate with [credential plugins](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#client-go-credential-plugins) These extensions only affect a individual user's local environment, and so cannot enforce site-wide policies.

If you want to extend the `kubectl` tool, read [Extend kubectl with plugins](https://kubernetes.io/docs/tasks/extend-kubectl/kubectl-plugins/).

## API extensions[](https://kubernetes.io/docs/concepts/extend-kubernetes/#api-extensions)

### Custom resource definitions[](https://kubernetes.io/docs/concepts/extend-kubernetes/#custom-resource-definitions)

Consider adding a Custom Resource to Kubernetes if you want to define new controllers, application configuration objects or other declarative APIs, and to manage them using Kubernetes tools, such as `kubectl`.

For more about Custom Resources, see the [Custom Resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) concept guide.

### API aggregation layer[](https://kubernetes.io/docs/concepts/extend-kubernetes/#api-aggregation-layer)

You can use Kubernetes' [API Aggregation Layer](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/) to integrate the Kubernetes API with additional services such as for [metrics](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/).

### Combining new APIs with automation[](https://kubernetes.io/docs/concepts/extend-kubernetes/#combining-new-apis-with-automation)

A combination of a custom resource API and a control loop is called the [controllers](https://kubernetes.io/docs/concepts/architecture/controller/) pattern. If your controller takes the place of a human operator deploying infrastructure based on a desired state, then the controller may also be following the [operator pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/). The Operator pattern is used to manage specific applications; usually, these are applications that maintain state and require care in how they are managed.

You can also make your own custom APIs and control loops that manage other resources, such as storage, or to define policies (such as an access control restriction).

### Changing built-in resources[](https://kubernetes.io/docs/concepts/extend-kubernetes/#changing-built-in-resources)

When you extend the Kubernetes API by adding custom resources, the added resources always fall into a new API Groups. You cannot replace or change existing API groups. Adding an API does not directly let you affect the behavior of existing APIs (such as Pods), whereas API Access Extensions do.

## API access extensions[](https://kubernetes.io/docs/concepts/extend-kubernetes/#api-access-extensions)

When a request reaches the Kubernetes API Server, it is first authenticated, then authorized, and is then subject to various types of admission control (some requests are in fact not authenticated, and get special treatment). See [Controlling Access to the Kubernetes API](https://kubernetes.io/docs/concepts/security/controlling-access/) for more on this flow.

Each of the steps in the Kubernetes authentication / authorization flow offers extension points.

### Authentication[](https://kubernetes.io/docs/concepts/extend-kubernetes/#authentication)

[Authentication](https://kubernetes.io/docs/reference/access-authn-authz/authentication/) maps headers or certificates in all requests to a username for the client making the request.

Kubernetes has several built-in authentication methods that it supports. It can also sit behind an authenticating proxy, and it can send a token from an `Authorization:` header to a remote service for verification (an [authentication webhook](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#webhook-token-authentication)) if those don't meet your needs.

### Authorization[](https://kubernetes.io/docs/concepts/extend-kubernetes/#authorization)

[Authorization](https://kubernetes.io/docs/reference/access-authn-authz/authorization/) determines whether specific users can read, write, and do other operations on API resources. It works at the level of whole resources -- it doesn't discriminate based on arbitrary object fields.

If the built-in authorization options don't meet your needs, an [authorization webhook](https://kubernetes.io/docs/reference/access-authn-authz/webhook/) allows calling out to custom code that makes an authorization decision.

### Dynamic admission control[](https://kubernetes.io/docs/concepts/extend-kubernetes/#dynamic-admission-control)

After a request is authorized, if it is a write operation, it also goes through [Admission Control](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) steps. In addition to the built-in steps, there are several extensions:
* The [Image Policy webhook](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#imagepolicywebhook) restricts what images can be run in containers.
* To make arbitrary admission control decisions, a general [Admission webhook](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#admission-webhooks) can be used. Admission webhooks can reject creations or updates. Some admission webhooks modify the incoming request data before it is handled further by Kubernetes.

## Infrastructure extensions[](https://kubernetes.io/docs/concepts/extend-kubernetes/#infrastructure-extensions)

### Device plugins[](https://kubernetes.io/docs/concepts/extend-kubernetes/#device-plugins)

Device plugins allow a node to discover new Node resources (in addition to the builtin ones like cpu and memory) via a [Device Plugin](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/).

### Storage plugins[](https://kubernetes.io/docs/concepts/extend-kubernetes/#storage-plugins)

[Container Storage Interface](https://kubernetes.io/docs/concepts/storage/volumes/#csi) (CSI) plugins provide a way to extend Kubernetes with supports for new kinds of volumes. The volumes can be backed by durable external storage, or provide ephemeral storage, or they might offer a read-only interface to information using a filesystem paradigm.

Kubernetes also includes support for [FlexVolume](https://kubernetes.io/docs/concepts/storage/volumes/#flexvolume) plugins, which are deprecated since Kubernetes v1.23 (in favour of CSI).

FlexVolume plugins allow users to mount volume types that aren't natively supported by Kubernetes. When you run a Pod that relies on FlexVolume storage, the kubelet calls a binary plugin to mount the volume. The archived [FlexVolume](https://git.k8s.io/design-proposals-archive/storage/flexvolume-deployment.md) design proposal has more detail on this approach.

The [Kubernetes Volume Plugin FAQ for Storage Vendors](https://github.com/kubernetes/community/blob/main/sig-storage/volume-plugin-faq.md#kubernetes-volume-plugin-faq-for-storage-vendors) includes general information on storage plugins.

### Network plugins[](https://kubernetes.io/docs/concepts/extend-kubernetes/#network-plugins)

Your Kubernetes cluster needs a network plugin in order to have a working Pod network and to support other aspects of the Kubernetes network model.

[Network Plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/) allow Kubernetes to work with different networking topologies and technologies.

### Kubelet image credential provider plugins[](https://kubernetes.io/docs/concepts/extend-kubernetes/#kubelet-image-credential-provider-plugins)

FEATURE STATE: `Kubernetes v1.26 [stable]`

---



# Source: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Extending Kubernetes](https://kubernetes.io/docs/concepts/extend-kubernetes/)
4. Compute, Storage, and Networking Extensions

# Compute, Storage, and Networking Extensions

This section covers extensions to your cluster that do not come as part as Kubernetes itself. You can use these extensions to enhance the nodes in your cluster, or to provide the network fabric that links Pods together.
* 

[CSI](https://kubernetes.io/docs/concepts/storage/volumes/#csi) and [FlexVolume](https://kubernetes.io/docs/concepts/storage/volumes/#flexvolume) storage plugins

[Container Storage Interface](https://kubernetes.io/docs/concepts/storage/volumes/#csi) (CSI) plugins provide a way to extend Kubernetes with supports for new kinds of volumes. The volumes can be backed by durable external storage, or provide ephemeral storage, or they might offer a read-only interface to information using a filesystem paradigm.

Kubernetes also includes support for [FlexVolume](https://kubernetes.io/docs/concepts/storage/volumes/#flexvolume) plugins, which are deprecated since Kubernetes v1.23 (in favour of CSI).

FlexVolume plugins allow users to mount volume types that aren't natively supported by Kubernetes. When you run a Pod that relies on FlexVolume storage, the kubelet calls a binary plugin to mount the volume. The archived [FlexVolume](https://git.k8s.io/design-proposals-archive/storage/flexvolume-deployment.md) design proposal has more detail on this approach.

The [Kubernetes Volume Plugin FAQ for Storage Vendors](https://github.com/kubernetes/community/blob/main/sig-storage/volume-plugin-faq.md#kubernetes-volume-plugin-faq-for-storage-vendors) includes general information on storage plugins.
* 

[Device plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/)

Device plugins allow a node to discover new Node facilities (in addition to the built-in node resources such as `cpu` and `memory`), and provide these custom node-local facilities to Pods that request them.
* 

[Network plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)

Network plugins allow Kubernetes to work with different networking topologies and technologies. Your Kubernetes cluster needs a network plugin in order to have a working Pod network and to support other aspects of the Kubernetes network model.

Kubernetes 1.36 is compatible with [CNI](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/) network plugins.

## Feedback

Was this page helpful?Yes No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes). Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to [report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io) or [suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).const yes=document.querySelector(".feedback--yes"),no=document.querySelector(".feedback--no");document.querySelectorAll(".feedback--link").forEach(e=>{e.href=e.href+window.location.pathname});const sendFeedback=e=>{typeof gtag=="function"?gtag("event","page_helpful",{event_category:"Helpful",event_label:window.location.pathname,value:e}):console.log("gtag not available; skipping analytics event")},disableButtons=()=>{yes.disabled=!0,yes.classList.add("feedback--button__disabled"),no.disabled=!0,no.classList.add("feedback--button__disabled")};yes.addEventListener("click",()=>{sendFeedback(100),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")}),no.addEventListener("click",()=>{sendFeedback(0),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")})Last modified April 14, 2026 at 1:15 AM PST: [fix(links): update kubernetes/community links from master to main (03c191bcc4)](https://github.com/kubernetes/website/commit/03c191bcc446f9c15a9e68d6cd1154b53bde4291)

---



# Source: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Extending Kubernetes](https://kubernetes.io/docs/concepts/extend-kubernetes/)
4. [Compute, Storage, and Networking Extensions](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/)
5. Network Plugins

# Network Plugins

Kubernetes (version 1.3 through to the latest 1.36, and likely onwards) lets you use [Container Network Interface](https://github.com/containernetworking/cni) (CNI) plugins for cluster networking. You must use a CNI plugin that is compatible with your cluster and that suits your needs. Different plugins are available (both open- and closed- source) in the wider Kubernetes ecosystem.

A CNI plugin is required to implement the [Kubernetes network model](https://kubernetes.io/docs/concepts/services-networking/#the-kubernetes-network-model).

You must use a CNI plugin that is compatible with the [v0.4.0](https://github.com/containernetworking/cni/blob/spec-v0.4.0/SPEC.md) or later releases of the CNI specification. The Kubernetes project recommends using a plugin that is compatible with the [v1.0.0](https://github.com/containernetworking/cni/blob/spec-v1.0.0/SPEC.md) CNI specification (plugins can be compatible with multiple spec versions).

## Installation[](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/#installation)

A Container Runtime, in the networking context, is a daemon on a node configured to provide CRI Services for kubelet. In particular, the Container Runtime must be configured to load the CNI plugins required to implement the Kubernetes network model.

#### Note:

Prior to Kubernetes 1.24, the CNI plugins could also be managed by the kubelet using the `cni-bin-dir` and `network-plugin` command-line parameters. These command-line parameters were removed in Kubernetes 1.24, with management of the CNI no longer in scope for kubelet.

See [Troubleshooting CNI plugin-related errors](https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/troubleshooting-cni-plugin-related-errors/) if you are facing issues following the removal of dockershim.

For specific information about how a Container Runtime manages the CNI plugins, see the documentation for that Container Runtime, for example:
* [containerd](https://github.com/containerd/containerd/blob/main/script/setup/install-cni)
* [CRI-O](https://github.com/cri-o/cri-o/blob/main/contrib/cni/README.md)

For specific information about how to install and manage a CNI plugin, see the documentation for that plugin or [networking provider](https://kubernetes.io/docs/concepts/cluster-administration/networking/#how-to-implement-the-kubernetes-network-model).

## Network Plugin Requirements[](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/#network-plugin-requirements)

### Loopback CNI[](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/#loopback-cni)

In addition to the CNI plugin installed on the nodes for implementing the Kubernetes network model, Kubernetes also requires the container runtimes to provide a loopback interface `lo`, which is used for each sandbox (pod sandboxes, vm sandboxes, ...). Implementing the loopback interface can be accomplished by re-using the [CNI loopback plugin.](https://github.com/containernetworking/plugins/blob/master/plugins/main/loopback/loopback.go) or by developing your own code to achieve this (see [this example from CRI-O](https://github.com/cri-o/ocicni/blob/release-1.24/pkg/ocicni/util_linux.go#L91)).

### Support hostPort[](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/#support-hostport)

The CNI networking plugin supports `hostPort`. You can use the official [portmap](https://github.com/containernetworking/plugins/tree/master/plugins/meta/portmap) plugin offered by the CNI plugin team or use your own plugin with portMapping functionality.

If you want to enable `hostPort` support, you must specify `portMappings capability` in your `cni-conf-dir`. For example:
```yaml
{
  "name": "k8s-pod-network",
  "cniVersion": "0.4.0",
  "plugins": [
    {
      "type": "calico",
      "log_level": "info",
      "datastore_type": "kubernetes",
      "nodename": "127.0.0.1",
      "ipam": {
        "type": "host-local",
        "subnet": "usePodCidr"
      },
      "policy": {
        "type": "k8s"
      },
      "kubernetes": {
        "kubeconfig": "/etc/cni/net.d/calico-kubeconfig"
      }
    },
    {
      "type": "portmap",
      "capabilities": {"portMappings": true},
      "externalSetMarkChain": "KUBE-MARK-MASQ"
    }
  ]
}
```

### Support traffic shaping[](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/#support-traffic-shaping)

Experimental Feature

The CNI networking plugin also supports pod ingress and egress traffic shaping. You can use the official [bandwidth](https://github.com/containernetworking/plugins/tree/master/plugins/meta/bandwidth) plugin offered by the CNI plugin team or use your own plugin with bandwidth control functionality.

If you want to enable traffic shaping support, you must add the `bandwidth` plugin to your CNI configuration file (default `/etc/cni/net.d`) and ensure that the binary is included in your CNI bin dir (default `/opt/cni/bin`).
```yaml
{
  "name": "k8s-pod-network",
  "cniVersion": "0.4.0",
  "plugins": [
    {
      "type": "calico",
      "log_level": "info",
      "datastore_type": "kubernetes",
      "nodename": "127.0.0.1",
      "ipam": {
        "type": "host-local",
        "subnet": "usePodCidr"
      },
      "policy": {
        "type": "k8s"
      },
      "kubernetes": {
        "kubeconfig": "/etc/cni/net.d/calico-kubeconfig"
      }
    },
    {
      "type": "bandwidth",
      "capabilities": {"bandwidth": true}
    }
  ]
}
```

---



# Source: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Extending Kubernetes](https://kubernetes.io/docs/concepts/extend-kubernetes/)
4. [Compute, Storage, and Networking Extensions](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/)
5. Device Plugins

# Device PluginsDevice plugins let you configure your cluster with support for devices or resources that require vendor-specific setup, such as GPUs, NICs, FPGAs, or non-volatile main memory.FEATURE STATE: `Kubernetes v1.26 [stable]`

Kubernetes provides a device plugin framework that you can use to advertise system hardware resources to the [Kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet).

Instead of customizing the code for Kubernetes itself, vendors can implement a device plugin that you deploy either manually or as a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset). The targeted devices include GPUs, high-performance NICs, FPGAs, InfiniBand adapters, and other similar computing resources that may require vendor specific initialization and setup.

## Device plugin registration[](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#device-plugin-registration)

The kubelet exports a `Registration` gRPC service:
```yaml
service Registration {
	rpc Register(RegisterRequest) returns (Empty) {}
}
```

A device plugin can register itself with the kubelet through this gRPC service. During the registration, the device plugin needs to send:
* The name of its Unix socket.
* The Device Plugin API version against which it was built.
* The `ResourceName` it wants to advertise. Here `ResourceName` needs to follow the [extended resource naming scheme](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#extended-resources) as `vendor-domain/resourcetype`. (For example, an NVIDIA GPU is advertised as `nvidia.com/gpu`.)

Following a successful registration, the device plugin sends the kubelet the list of devices it manages, and the kubelet is then in charge of advertising those resources to the API server as part of the kubelet node status update. For example, after a device plugin registers `hardware-vendor.example/foo` with the kubelet and reports two healthy devices on a node, the node status is updated to advertise that the node has 2 "Foo" devices installed and available.

Then, users can request devices as part of a Pod specification (see [`container`](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#Container)). Requesting extended resources is similar to how you manage requests and limits for other resources, with the following differences:
* Extended resources are only supported as integer resources and cannot be overcommitted.
* Devices cannot be shared between containers.

### Example[](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#example-pod)

Suppose a Kubernetes cluster is running a device plugin that advertises resource `hardware-vendor.example/foo` on certain nodes. Here is an example of a pod requesting this resource to run a demo workload:
```yaml
---
apiVersion: v1
kind: Pod
metadata:
  name: demo-pod
spec:
  containers:
    - name: demo-container-1
      image: registry.k8s.io/pause:3.8
      resources:
        limits:
          hardware-vendor.example/foo: 2
#
# This Pod needs 2 of the hardware-vendor.example/foo devices
# and can only schedule onto a Node that's able to satisfy
# that need.
#
# If the Node has more than 2 of those devices available, the
# remainder would be available for other Pods to use.
```

---



# Source: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Extending Kubernetes](https://kubernetes.io/docs/concepts/extend-kubernetes/)
4. Extending the Kubernetes API

# Extending the Kubernetes API

Custom resources are extensions of the Kubernetes API. Kubernetes provides two ways to add custom resources to your cluster:
* The [CustomResourceDefinition](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) (CRD) mechanism allows you to declaratively define a new custom API with an API group, kind, and schema that you specify. The Kubernetes control plane serves and handles the storage of your custom resource. CRDs allow you to create new types of resources for your cluster without writing and running a custom API server.
* The [aggregation layer](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/) sits behind the primary API server, which acts as a proxy. This arrangement is called API Aggregation (AA), which allows you to provide specialized implementations for your custom resources by writing and deploying your own API server. The main API server delegates requests to your API server for the custom APIs that you specify, making them available to all of its clients.

## Feedback

Was this page helpful?Yes No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes). Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to [report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io) or [suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).const yes=document.querySelector(".feedback--yes"),no=document.querySelector(".feedback--no");document.querySelectorAll(".feedback--link").forEach(e=>{e.href=e.href+window.location.pathname});const sendFeedback=e=>{typeof gtag=="function"?gtag("event","page_helpful",{event_category:"Helpful",event_label:window.location.pathname,value:e}):console.log("gtag not available; skipping analytics event")},disableButtons=()=>{yes.disabled=!0,yes.classList.add("feedback--button__disabled"),no.disabled=!0,no.classList.add("feedback--button__disabled")};yes.addEventListener("click",()=>{sendFeedback(100),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")}),no.addEventListener("click",()=>{sendFeedback(0),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")})Last modified March 27, 2026 at 11:20 PM PST: [remove duplicate links (3605e11ec8)](https://github.com/kubernetes/website/commit/3605e11ec86182314efb71e8f2a5dbf113c0b869)

---



# Source: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Extending Kubernetes](https://kubernetes.io/docs/concepts/extend-kubernetes/)
4. [Extending the Kubernetes API](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/)
5. Custom Resources

# Custom Resources

Custom resources are extensions of the Kubernetes API. This page discusses when to add a custom resource to your Kubernetes cluster and when to use a standalone service. It describes the two methods for adding custom resources and how to choose between them.

## Custom resources[](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#custom-resources)

A resource is an endpoint in the [Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/) that stores a collection of [API objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects) of a certain kind; for example, the built-in pods resource contains a collection of Pod objects.

A custom resource is an extension of the Kubernetes API that is not necessarily available in a default Kubernetes installation. It represents a customization of a particular Kubernetes installation. However, many core Kubernetes functions are now built using custom resources, making Kubernetes more modular.

Custom resources can appear and disappear in a running cluster through dynamic registration, and cluster admins can update custom resources independently of the cluster itself. Once a custom resource is installed, users can create and access its objects using [kubectl](https://kubernetes.io/docs/reference/kubectl/), just as they do for built-in resources like Pods.

## Custom controllers[](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#custom-controllers)

On their own, custom resources let you store and retrieve structured data. When you combine a custom resource with a custom controller, custom resources provide a true declarative API.

The Kubernetes [declarative API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/) enforces a separation of responsibilities. You declare the desired state of your resource. The Kubernetes controller keeps the current state of Kubernetes objects in sync with your declared desired state. This is in contrast to an imperative API, where you instruct a server what to do.

You can deploy and update a custom controller on a running cluster, independently of the cluster's lifecycle. Custom controllers can work with any kind of resource, but they are especially effective when combined with custom resources. The [Operator pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) combines custom resources and custom controllers. You can use custom controllers to encode domain knowledge for specific applications into an extension of the Kubernetes API.

## Should I add a custom resource to my Kubernetes cluster?[](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#should-i-add-a-custom-resource-to-my-kubernetes-cluster)

When creating a new API, consider whether to [aggregate your API with the Kubernetes cluster APIs](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/) or let your API stand alone.[](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#declarative-apis)[](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#declarative-apis)````[](https://kubernetes.io/docs/concepts/overview/kubernetes-api/)[](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#common-features)

| Consider API aggregation if: | Prefer a stand-alone API if: || --- | --- || Your API is Declarative. | Your API does not fit the Declarative model. || You want your new types to be readable and writable using kubectl. | kubectl support is not required || You want to view your new types in a Kubernetes UI, such as dashboard, alongside built-in types. | Kubernetes UI support is not required. || You are developing a new API. | You already have a program that serves your API and works well. || You are willing to accept the format restriction that Kubernetes puts on REST resource paths, such as API Groups and Namespaces. (See the API Overview.) | You need to have specific REST paths to be compatible with an already defined REST API. || Your resources are naturally scoped to a cluster or namespaces of a cluster. | Cluster or namespace scoped resources are a poor fit; you need control over the specifics of resource paths. || You want to reuse Kubernetes API support features. | You don't need those features. |

### Declarative APIs[](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#declarative-apis)

In a Declarative API, typically:
* Your API consists of a relatively small number of relatively small objects (resources).
* The objects define configuration of applications or infrastructure.
* The objects are updated relatively infrequently.
* Humans often need to read and write the objects.
* The main operations on the objects are CRUD-y (creating, reading, updating and deleting).
* Transactions across objects are not required: the API represents a desired state, not an exact state.

Imperative APIs are not declarative. Signs that your API might not be declarative include:
* The client says "do this", and then gets a synchronous response back when it is done.
* The client says "do this", and then gets an operation ID back, and has to check a separate Operation object to determine completion of the request.
* You talk about Remote Procedure Calls (RPCs).
* Directly storing large amounts of data; for example, > a few kB per object, or > 1000s of objects.
* High bandwidth access (10s of requests per second sustained) needed.
* Store end-user data (such as images, PII, etc.) or other large-scale data processed by applications.
* The natural operations on the objects are not CRUD-y.
* The API is not easily modeled as objects.
* You chose to represent pending operations with an operation ID or an operation object.

## Should I use a ConfigMap or a custom resource?[](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#should-i-use-a-configmap-or-a-custom-resource)

Use a ConfigMap if any of the following apply:
* There is an existing, well-documented configuration file format, such as a `mysql.cnf` or `pom.xml`.
* You want to put the entire configuration into one key of a ConfigMap.
* The main use of the configuration file is for a program running in a Pod on your cluster to consume the file to configure itself.
* Consumers of the file prefer to consume via file in a Pod or environment variable in a pod, rather than the Kubernetes API.
* You want to perform rolling updates via Deployment, etc., when the file is updated.

#### Note:Use a [Secret](https://kubernetes.io/docs/concepts/configuration/secret/) for sensitive data, which is similar to a ConfigMap but more secure.

Use a custom resource (CRD or Aggregated API) if most of the following apply:
* You want to use Kubernetes client libraries and CLIs to create and update the new resource.
* You want top-level support from `kubectl`; for example, `kubectl get my-object object-name`.
* You want to build new automation that watches for updates on the new object, and then CRUD other objects, or vice versa.
* You want to write automation that handles updates to the object.
* You want to use Kubernetes API conventions like `.spec`, `.status`, and `.metadata`.
* You want the object to be an abstraction over a collection of controlled resources, or a summarization of other resources.

## Adding custom resources[](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#adding-custom-resources)

Kubernetes provides two ways to add custom resources to your cluster:
* CRDs are simple and can be created without any programming.
* [API Aggregation](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/) requires programming, but allows more control over API behaviors like how data is stored and conversion between API versions.

Kubernetes provides these two options to meet the needs of different users, so that neither ease of use nor flexibility is compromised.

Aggregated APIs are subordinate API servers that sit behind the primary API server, which acts as a proxy. This arrangement is called [API Aggregation](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/)(AA). To users, the Kubernetes API appears extended.

CRDs allow users to create new types of resources without adding another API server. You do not need to understand API Aggregation to use CRDs.

Regardless of how they are installed, the new resources are referred to as Custom Resources to distinguish them from built-in Kubernetes resources (like pods).

#### Note:

Avoid using a Custom Resource as data storage for application, end user, or monitoring data: architecture designs that store application data within the Kubernetes API typically represent a design that is too closely coupled.

Architecturally, [cloud native](https://www.cncf.io/about/faq/#what-is-cloud-native) application architectures favor loose coupling between components. If part of your workload requires a backing service for its routine operation, run that backing service as a component or consume it as an external service. This way, your workload does not rely on the Kubernetes API for its normal operation.

## CustomResourceDefinitions[](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#customresourcedefinitions)

The [CustomResourceDefinition](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/) API resource allows you to define custom resources. Defining a CRD object creates a new custom resource with a name and schema that you specify. The Kubernetes API serves and handles the storage of your custom resource. The name of the CRD object itself must be a valid [DNS subdomain name](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names) derived from the defined resource name and its API group; see [how to create a CRD](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#create-a-customresourcedefinition) for more details. Further, the name of an object whose kind/resource is defined by a CRD must also be a valid DNS subdomain name.

This frees you from writing your own API server to handle the custom resource, but the generic nature of the implementation means you have less flexibility than with [API server aggregation](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#api-server-aggregation).

Refer to the [custom controller example](https://github.com/kubernetes/sample-controller) for an example of how to register a new custom resource, work with instances of your new resource type, and use a controller to handle events.

## API server aggregation[](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#api-server-aggregation)

Usually, each resource in the Kubernetes API requires code that handles REST requests and manages persistent storage of objects. The main Kubernetes API server handles built-in resources like pods and services, and can also generically handle custom resources through [CRDs](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#customresourcedefinitions).

The [aggregation layer](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/) allows you to provide specialized implementations for your custom resources by writing and deploying your own API server. The main API server delegates requests to your API server for the custom resources that you handle, making them available to all of its clients.

## Choosing a method for adding custom resources[](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#choosing-a-method-for-adding-custom-resources)

CRDs are easier to use. Aggregated APIs are more flexible. Choose the method that best meets your needs.

Typically, CRDs are a good fit if:
* You have a handful of fields
* You are using the resource within your company, or as part of a small open-source project (as opposed to a commercial product)

### Comparing ease of use[](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#comparing-ease-of-use)

CRDs are easier to create than Aggregated APIs.

| CRDs | Aggregated API || --- | --- || Do not require programming. Users can choose any language for a CRD controller. | Requires programming and building binary and image. || No additional service to run; CRDs are handled by API server. | An additional service to create and that could fail. || No ongoing support once the CRD is created. Any bug fixes are picked up as part of normal Kubernetes Master upgrades. | May need to periodically pickup bug fixes from upstream and rebuild and update the Aggregated API server. || No need to handle multiple versions of your API; for example, when you control the client for this resource, you can upgrade it in sync with the API. | You need to handle multiple versions of your API; for example, when developing an extension to share with the world. |

### Advanced features and flexibility[](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#advanced-features-and-flexibility)

Aggregated APIs offer more advanced API features and customization of other features; for example, the storage layer.[](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#validation)[](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#validation-ratcheting)[](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#validatingadmissionwebhook-alpha-in-1-8-beta-in-1-9)[](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#defaulting)``[](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#mutatingadmissionwebhook)[](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/)[](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#admission-webhooks)[](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#scale-subresource)[](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#status-subresource)``[](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch/)````[](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#validation)

| Feature | Description | CRDs | Aggregated API || --- | --- | --- | --- || Validation | Help users prevent errors and allow you to evolve your API independently of your clients. These features are most useful when there are many clients who can't all update at the same time. | Yes. Most validation can be specified in the CRD using OpenAPI v3.0 validation. CRDValidationRatcheting feature gate allows failing validations specified using OpenAPI also can be ignored if the failing part of the resource was unchanged. Any other validations supported by addition of a Validating Webhook. | Yes, arbitrary validation checks || Defaulting | See above | Yes, either via OpenAPI v3.0 validation default keyword (GA in 1.17), or via a Mutating Webhook (though this will not be run when reading from etcd for old objects). | Yes || Multi-versioning | Allows serving the same object through two API versions. Can help ease API changes like renaming fields. Less important if you control your client versions. | Yes | Yes || Custom Storage | If you need storage with a different performance mode (for example, a time-series database instead of key-value store) or isolation for security (for example, encryption of sensitive information, etc.) | No | Yes || Custom Business Logic | Perform arbitrary checks or actions when creating, reading, updating or deleting an object | Yes, using Webhooks. | Yes || Scale Subresource | Allows systems like HorizontalPodAutoscaler and PodDisruptionBudget interact with your new resource | Yes | Yes || Status Subresource | Allows fine-grained access control where user writes the spec section and the controller writes the status section. Allows incrementing object Generation on custom resource data mutation (requires separate spec and status sections in the resource) | Yes | Yes || Other Subresources | Add operations other than CRUD, such as "logs" or "exec". | No | Yes || strategic-merge-patch | The new endpoints support PATCH with Content-Type: application/strategic-merge-patch+json. Useful for updating objects that may be modified both locally, and by the server. For more information, see "Update API Objects in Place Using kubectl patch" | No | Yes || Protocol Buffers | The new resource supports clients that want to use Protocol Buffers | No | Yes || OpenAPI Schema | Is there an OpenAPI (swagger) schema for the types that can be dynamically fetched from the server? Is the user protected from misspelling field names by ensuring only allowed fields are set? Are types enforced (in other words, don't put an int in a string field?) | Yes, based on the OpenAPI v3.0 validation schema (GA in 1.16). | Yes || Instance Name | Does this extension mechanism impose any constraints on the names of objects whose kind/resource is defined this way? | Yes, such an object's name must be a valid DNS subdomain name. | No |

### Common Features[](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#common-features)

When you create a custom resource, either via a CRD or an AA, you get many features for your API, compared to implementing it outside the Kubernetes platform:````````

| Feature | What it does || --- | --- || CRUD | The new endpoints support CRUD basic operations via HTTP and kubectl || Watch | The new endpoints support Kubernetes Watch operations via HTTP || Discovery | Clients like kubectl and dashboard automatically offer list, display, and field edit operations on your resources || json-patch | The new endpoints support PATCH with Content-Type: application/json-patch+json || merge-patch | The new endpoints support PATCH with Content-Type: application/merge-patch+json || HTTPS | The new endpoints uses HTTPS || Built-in Authentication | Access to the extension uses the core API server (aggregation layer) for authentication || Built-in Authorization | Access to the extension can reuse the authorization used by the core API server; for example, RBAC. || Finalizers | Block deletion of extension resources until external cleanup happens. || Admission Webhooks | Set default values and validate extension resources during any create/update/delete operation. || UI/CLI Display | Kubectl, dashboard can display extension resources. || Unset versus Empty | Clients can distinguish unset fields from zero-valued fields. || Client Libraries Generation | Kubernetes provides generic client libraries, as well as tools to generate type-specific client libraries. || Labels and annotations | Common metadata across objects that tools know how to edit for core and custom resources. |

## Preparing to install a custom resource[](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#preparing-to-install-a-custom-resource)

There are several points to be aware of before adding a custom resource to your cluster.

### Third party code and new points of failure[](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#third-party-code-and-new-points-of-failure)

While creating a CRD does not automatically add any new points of failure (for example, by causing third party code to run on your API server), packages (for example, Charts) or other installation bundles often include CRDs as well as a Deployment of third-party code that implements the business logic for a new custom resource.

Installing an Aggregated API server always involves running a new Deployment.

### Storage[](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#storage)

Custom resources consume storage space in the same way that ConfigMaps do. Creating too many custom resources may overload your API server's storage space.

Custom resources are placed into storage based upon the the current storage version of the resource, defined in the CRD spec. Any update to a custom resource will use the currently defined storage version to store the resource. All other versions either need to have all the fields of that version or define conversions to work properly.

Aggregated API servers may use the same storage as the main API server, in which case the same warning applies.

### Authentication, authorization, and auditing[](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#authentication-authorization-and-auditing)

CRDs always use the same authentication, authorization, and audit logging as the built-in resources of your API server.

If you use RBAC for authorization, most RBAC roles will not grant access to the new resources (except the cluster-admin role or any role created with wildcard rules). You'll need to explicitly grant access to the new resources. CRDs and Aggregated APIs often come bundled with new role definitions for the types they add.

Aggregated API servers may or may not use the same authentication, authorization, and auditing as the primary API server.

## Accessing a custom resource[](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#accessing-a-custom-resource)

Kubernetes [client libraries](https://kubernetes.io/docs/reference/using-api/client-libraries/) can be used to access custom resources. Not all client libraries support custom resources. The Go and Python client libraries do.

When you add a custom resource, you can access it using:
* `kubectl`
* The Kubernetes dynamic client.
* A REST client that you write.
* A client generated using [Kubernetes client generation tools](https://github.com/kubernetes/code-generator) (generating one is an advanced undertaking, but some projects may provide a client along with the CRD or AA).

## Custom resource field selectors[](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#custom-resource-field-selectors)

[Field Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/) let clients select custom resources based on the value of one or more resource fields.

All custom resources support the `metadata.name` and `metadata.namespace` field selectors.

Fields declared in a [CustomResourceDefinition](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/) may also be used with field selectors when included in the `spec.versions[*].selectableFields` field of the [CustomResourceDefinition](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/).

### Selectable fields for custom resources[](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#crd-selectable-fields)FEATURE STATE: `Kubernetes v1.32 [stable]`(enabled by default)

---



# Source: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Extending Kubernetes](https://kubernetes.io/docs/concepts/extend-kubernetes/)
4. Operator pattern

# Operator pattern

Operators are software extensions to Kubernetes that make use of [custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) to manage applications and their components. Operators follow Kubernetes principles, notably the [control loop](https://kubernetes.io/docs/concepts/architecture/controller/).

## Motivation[](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/#motivation)

The operator pattern aims to capture the key aim of a human operator who is managing a service or set of services. Human operators who look after specific applications and services have deep knowledge of how the system ought to behave, how to deploy it, and how to react if there are problems.

People who run workloads on Kubernetes often like to use automation to take care of repeatable tasks. The operator pattern captures how you can write code to automate a task beyond what Kubernetes itself provides.

## Operators in Kubernetes[](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/#operators-in-kubernetes)

Kubernetes is designed for automation. Out of the box, you get lots of built-in automation from the core of Kubernetes. You can use Kubernetes to automate deploying and running workloads, and you can automate how Kubernetes does that.

Kubernetes' [operator pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) concept lets you extend the cluster's behaviour without modifying the code of Kubernetes itself by linking [controllers](https://kubernetes.io/docs/concepts/architecture/controller/) to one or more custom resources. Operators are clients of the Kubernetes API that act as controllers for a [Custom Resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/).

## An example operator[](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/#example)

Some of the things that you can use an operator to automate include:
* deploying an application on demand
* taking and restoring backups of that application's state
* handling upgrades of the application code alongside related changes such as database schemas or extra configuration settings
* publishing a Service to applications that don't support Kubernetes APIs to discover them
* simulating failure in all or part of your cluster to test its resilience
* choosing a leader for a distributed application without an internal member election process

What might an operator look like in more detail? Here's an example:
1. A custom resource named SampleDB, that you can configure into the cluster.
2. A Deployment that makes sure a Pod is running that contains the controller part of the operator.
3. A container image of the operator code.
4. Controller code that queries the control plane to find out what SampleDB resources are configured.
5. The core of the operator is code to tell the API server how to make reality match the configured resources.
  * If you add a new SampleDB, the operator sets up PersistentVolumeClaims to provide durable database storage, a StatefulSet to run SampleDB and a Job to handle initial configuration.
  * If you delete it, the operator takes a snapshot, then makes sure that the StatefulSet and Volumes are also removed.
6. The operator also manages regular database backups. For each SampleDB resource, the operator determines when to create a Pod that can connect to the database and take backups. These Pods would rely on a ConfigMap and / or a Secret that has database connection details and credentials.
7. Because the operator aims to provide robust automation for the resource it manages, there would be additional supporting code. For this example, code checks to see if the database is running an old version and, if so, creates Job objects that upgrade it for you.

## Deploying operators[](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/#deploying-operators)

The most common way to deploy an operator is to add the Custom Resource Definition and its associated Controller to your cluster. The Controller will normally run outside of the [control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane), much as you would run any containerized application. For example, you can run the controller in your cluster as a Deployment.

## Using an operator[](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/#using-operators)

Once you have an operator deployed, you'd use it by adding, modifying or deleting the kind of resource that the operator uses. Following the above example, you would set up a Deployment for the operator itself, and then:
```yaml
kubectl get SampleDB                   # find configured databases

kubectl edit SampleDB/example-database # manually change some settings
```

…and that's it! The operator will take care of applying the changes as well as keeping the existing service in good shape.

## Writing your own operator[](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/#writing-operator)

If there isn't an operator in the ecosystem that implements the behavior you want, you can code your own.

You also implement an operator (that is, a Controller) using any language / runtime that can act as a [client for the Kubernetes API](https://kubernetes.io/docs/reference/using-api/client-libraries/).

Following are a few libraries and tools you can use to write your own cloud native operator.Note: This section links to third party projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for these projects, which are listed alphabetically. To add a project to this list, read the [content guide](https://kubernetes.io/docs/contribute/style/content-guide/#third-party-content) before submitting a change. [More information.](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/#third-party-content-disclaimer)
* [Charmed Operator Framework](https://juju.is/)
* [Java Operator SDK](https://github.com/operator-framework/java-operator-sdk)
* [Kopf](https://github.com/nolar/kopf) (Kubernetes Operator Pythonic Framework)
* [kube-rs](https://kube.rs/) (Rust)
* [kubebuilder](https://book.kubebuilder.io/)
* [KubeOps](https://dotnet.github.io/dotnet-operator-sdk/) (.NET operator SDK)
* [Mast](https://docs.ansi.services/mast/user_guide/operator/)
* [Metacontroller](https://metacontroller.github.io/metacontroller/intro.html) along with WebHooks that you implement yourself
* [Operator Framework](https://operatorframework.io)
* [shell-operator](https://github.com/flant/shell-operator)

## What's next[](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/#what-s-next)
* Read the [CNCF](https://cncf.io/) [Operator White Paper](https://github.com/cncf/tag-app-delivery/blob/163962c4b1cd70d085107fc579e3e04c2e14d59c/operator-wg/whitepaper/Operator-WhitePaper_v1-0.md).
* Learn more about [Custom Resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
* Find ready-made operators on [OperatorHub.io](https://operatorhub.io/) to suit your use case
* [Publish](https://operatorhub.io/) your operator for other people to use
* Read [CoreOS' original article](https://web.archive.org/web/20170129131616/https://coreos.com/blog/introducing-operators.html) that introduced the operator pattern (this is an archived version of the original article).
* Read an [article](https://cloud.google.com/blog/products/containers-kubernetes/best-practices-for-building-kubernetes-operators-and-stateful-apps) from Google Cloud about best practices for building operators

## Feedback

Was this page helpful?Yes No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes). Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to [report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io) or [suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).

---



# Source (Sub-link): https://kubernetes.io/docs/concepts/policy/resource-quotas/

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



# Source (Sub-link): https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Extending Kubernetes](https://kubernetes.io/docs/concepts/extend-kubernetes/)
4. [Extending the Kubernetes API](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/)
5. Kubernetes API Aggregation Layer

# Kubernetes API Aggregation Layer

The aggregation layer allows Kubernetes to be extended with additional APIs, beyond what is offered by the core Kubernetes APIs. The additional APIs can either be ready-made solutions such as a [metrics server](https://github.com/kubernetes-sigs/metrics-server), or APIs that you develop yourself.

The aggregation layer is different from [Custom Resource Definitions](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/), which are a way to make the [kube-apiserver](https://kubernetes.io/docs/concepts/architecture/#kube-apiserver) recognise new kinds of object.

## Aggregation layer[](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/#aggregation-layer)

The aggregation layer runs in-process with the kube-apiserver. Until an extension resource is registered, the aggregation layer will do nothing. To register an API, you add an APIService object, which "claims" the URL path in the Kubernetes API. At that point, the aggregation layer will proxy anything sent to that API path (e.g. `/apis/myextension.mycompany.io/v1/…`) to the registered APIService.

The most common way to implement the APIService is to run an extension API server in Pod(s) that run in your cluster. If you're using the extension API server to manage resources in your cluster, the extension API server (also written as "extension-apiserver") is typically paired with one or more [controllers](https://kubernetes.io/docs/concepts/architecture/controller/). The apiserver-builder library provides a skeleton for both extension API servers and the associated controller(s).

### Response latency[](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/#response-latency)

Extension API servers should have low latency networking to and from the kube-apiserver. Discovery requests are required to round-trip from the kube-apiserver in five seconds or less.

If your extension API server cannot achieve that latency requirement, consider making changes that let you meet it.

## What's next[](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/#what-s-next)
* To get the aggregator working in your environment, [configure the aggregation layer](https://kubernetes.io/docs/tasks/extend-kubernetes/configure-aggregation-layer/).
* Then, [setup an extension api-server](https://kubernetes.io/docs/tasks/extend-kubernetes/setup-extension-api-server/) to work with the aggregation layer.
* Read about [APIService](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/api-service-v1/) in the API reference
* Learn about [Declarative Validation Concepts](https://kubernetes.io/docs/reference/using-api/declarative-validation/), an internal mechanism for defining validation rules that in the future will help support validation for extension API server development.

Alternatively: learn how to extend the Kubernetes API using [Custom Resource Definitions](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/).

## Feedback

Was this page helpful?Yes No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes). Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to [report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io) or [suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).const yes=document.querySelector(".feedback--yes"),no=document.querySelector(".feedback--no");document.querySelectorAll(".feedback--link").forEach(e=>{e.href=e.href+window.location.pathname});const sendFeedback=e=>{typeof gtag=="function"?gtag("event","page_helpful",{event_category:"Helpful",event_label:window.location.pathname,value:e}):console.log("gtag not available; skipping analytics event")},disableButtons=()=>{yes.disabled=!0,yes.classList.add("feedback--button__disabled"),no.disabled=!0,no.classList.add("feedback--button__disabled")};yes.addEventListener("click",()=>{sendFeedback(100),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")}),no.addEventListener("click",()=>{sendFeedback(0),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")})Last modified February 19, 2026 at 3:34 PM PST: [Fix some links in the En docs (95b7685f71)](https://github.com/kubernetes/website/commit/95b7685f7156c317aa59d86618e8ec4535d2015f)

---



# Source (Sub-link): https://kubernetes.io/docs/concepts/security/controlling-access/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Security](https://kubernetes.io/docs/concepts/security/)
4. Controlling Access to the Kubernetes API

# Controlling Access to the Kubernetes API

This page provides an overview of controlling access to the Kubernetes API.

Users access the [Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/) using `kubectl`, client libraries, or by making REST requests. Both human users and [Kubernetes service accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) can be authorized for API access. When a request reaches the API, it goes through several stages, illustrated in the following diagram:

![Diagram of request handling steps for Kubernetes API request](https://kubernetes.io/images/docs/admin/access-control-overview.svg)

## Transport security[](https://kubernetes.io/docs/concepts/security/controlling-access/#transport-security)

By default, the Kubernetes API server listens on port 6443 on the first non-localhost network interface, protected by TLS. In a typical production Kubernetes cluster, the API serves on port 443. The port can be changed with the `--secure-port`, and the listening IP address with the `--bind-address` flag.

The API server presents a certificate. This certificate may be signed using a private certificate authority (CA), or based on a public key infrastructure linked to a generally recognized CA. The certificate and corresponding private key can be set by using the `--tls-cert-file` and `--tls-private-key-file` flags.

If your cluster uses a private certificate authority, you need a copy of that CA certificate configured into your `~/.kube/config` on the client, so that you can trust the connection and be confident it was not intercepted.

Your client can present a TLS client certificate at this stage.

## Authentication[](https://kubernetes.io/docs/concepts/security/controlling-access/#authentication)

Once TLS is established, the HTTP request moves to the Authentication step. This is shown as step 1 in the diagram. The cluster creation script or cluster admin configures the API server to run one or more Authenticator modules. Authenticators are described in more detail in [Authentication](https://kubernetes.io/docs/reference/access-authn-authz/authentication/).

The input to the authentication step is the entire HTTP request; however, it typically examines the headers and/or client certificate.

Authentication modules include client certificates, password, and plain tokens, bootstrap tokens, and JSON Web Tokens (used for service accounts).

Multiple authentication modules can be specified, in which case each one is tried in sequence, until one of them succeeds.

If the request cannot be authenticated, it is rejected with HTTP status code 401. Otherwise, the user is authenticated as a specific `username`, and the user name is available to subsequent steps to use in their decisions. Some authenticators also provide the group memberships of the user, while other authenticators do not.

While Kubernetes uses usernames for access control decisions and in request logging, it does not have a `User` object nor does it store usernames or other information about users in its API.

## Authorization[](https://kubernetes.io/docs/concepts/security/controlling-access/#authorization)

After the request is authenticated as coming from a specific user, the request must be authorized. This is shown as step 2 in the diagram.

A request must include the username of the requester, the requested action, and the object affected by the action. The request is authorized if an existing policy declares that the user has permissions to complete the requested action.

For example, if Bob has the policy below, then he can read pods only in the namespace `projectCaribou`:
```yaml
{
    "apiVersion": "abac.authorization.kubernetes.io/v1beta1",
    "kind": "Policy",
    "spec": {
        "user": "bob",
        "namespace": "projectCaribou",
        "resource": "pods",
        "readonly": true
    }
}
```

If Bob makes the following request, the request is authorized because he is allowed to read objects in the `projectCaribou` namespace:
```yaml
{
  "apiVersion": "authorization.k8s.io/v1beta1",
  "kind": "SubjectAccessReview",
  "spec": {
    "resourceAttributes": {
      "namespace": "projectCaribou",
      "verb": "get",
      "group": "unicorn.example.org",
      "resource": "pods"
    }
  }
}
```

If Bob makes a request to write (`create` or `update`) to the objects in the `projectCaribou` namespace, his authorization is denied. If Bob makes a request to read (`get`) objects in a different namespace such as `projectFish`, then his authorization is denied.

Kubernetes authorization requires that you use common REST attributes to interact with existing organization-wide or cloud-provider-wide access control systems. It is important to use REST formatting because these control systems might interact with other APIs besides the Kubernetes API.

Kubernetes supports multiple authorization modules, such as ABAC mode, RBAC Mode, and Webhook mode. When an administrator creates a cluster, they configure the authorization modules that should be used in the API server. If more than one authorization modules are configured, Kubernetes checks each module, and if any module authorizes the request, then the request can proceed. If all of the modules deny the request, then the request is denied (HTTP status code 403).

To learn more about Kubernetes authorization, including details about creating policies using the supported authorization modules, see [Authorization](https://kubernetes.io/docs/reference/access-authn-authz/authorization/).

## Admission control[](https://kubernetes.io/docs/concepts/security/controlling-access/#admission-control)

Admission Control modules are software modules that can modify or reject requests. In addition to the attributes available to Authorization modules, Admission Control modules can access the contents of the object that is being created or modified.

Admission controllers act on requests that create, modify, delete, or connect to (proxy) an object. Admission controllers do not act on requests that merely read objects. When multiple admission controllers are configured, they are called in order.

This is shown as step 3 in the diagram.

Unlike Authentication and Authorization modules, if any admission controller module rejects, then the request is immediately rejected.

In addition to rejecting objects, admission controllers can also set complex defaults for fields.

The available Admission Control modules are described in [Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/).

Once a request passes all admission controllers, it is validated using the validation routines for the corresponding API object, and then written to the object store (shown as step 4).

## Auditing[](https://kubernetes.io/docs/concepts/security/controlling-access/#auditing)

Kubernetes auditing provides a security-relevant, chronological set of records documenting the sequence of actions in a cluster. The cluster audits the activities generated by users, by applications that use the Kubernetes API, and by the control plane itself.

For more information, see [Auditing](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/).

## What's next[](https://kubernetes.io/docs/concepts/security/controlling-access/#what-s-next)

Read more documentation on authentication, authorization and API access control:
* [Authenticating](https://kubernetes.io/docs/reference/access-authn-authz/authentication/)
  * [Authenticating with Bootstrap Tokens](https://kubernetes.io/docs/reference/access-authn-authz/bootstrap-tokens/)
* [Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/)
  * [Dynamic Admission Control](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/)
* [Authorization](https://kubernetes.io/docs/reference/access-authn-authz/authorization/)
  * [Role Based Access Control](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
  * [Attribute Based Access Control](https://kubernetes.io/docs/reference/access-authn-authz/abac/)
  * [Node Authorization](https://kubernetes.io/docs/reference/access-authn-authz/node/)
  * [Webhook Authorization](https://kubernetes.io/docs/reference/access-authn-authz/webhook/)
* [Certificate Signing Requests](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/)
  * including [CSR approval](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/#approval-rejection) and [certificate signing](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/#signing)
* Service accounts
  * [Developer guide](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)
  * [Administration](https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/)

You can learn about:
* how Pods can use [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/#service-accounts-automatically-create-and-attach-secrets-with-api-credentials) to obtain API credentials.

## Feedback

Was this page helpful?Yes No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes). Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to [report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io) or [suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).

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



# Source (Sub-link): https://kubernetes.io/docs/concepts/overview/kubernetes-api/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Overview](https://kubernetes.io/docs/concepts/overview/)
4. The Kubernetes API

# The Kubernetes APIThe Kubernetes API lets you query and manipulate the state of objects in Kubernetes. The core of Kubernetes' control plane is the API server and the HTTP API that it exposes. Users, the different parts of your cluster, and external components all communicate with one another through the API server.

The core of Kubernetes' [control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane) is the [API server](https://kubernetes.io/docs/concepts/architecture/#kube-apiserver). The API server exposes an HTTP API that lets end users, different parts of your cluster, and external components communicate with one another.

The Kubernetes API lets you query and manipulate the state of API objects in Kubernetes (for example: Pods, Namespaces, ConfigMaps, and Events).

Most operations can be performed through the [kubectl](https://kubernetes.io/docs/reference/kubectl/) command-line interface or other command-line tools, such as [kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/), which in turn use the API. However, you can also access the API directly using REST calls. Kubernetes provides a set of [client libraries](https://kubernetes.io/docs/reference/using-api/client-libraries/) for those looking to write applications using the Kubernetes API.

Each Kubernetes cluster publishes the specification of the APIs that the cluster serves. There are two mechanisms that Kubernetes uses to publish these API specifications; both are useful to enable automatic interoperability. For example, the `kubectl` tool fetches and caches the API specification for enabling command-line completion and other features. The two supported mechanisms are as follows:
* 

[The Discovery API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/#discovery-api) provides information about the Kubernetes APIs: API names, resources, versions, and supported operations. This is a Kubernetes specific term as it is a separate API from the Kubernetes OpenAPI. It is intended to be a brief summary of the available resources and it does not detail specific schema for the resources. For reference about resource schemas, please refer to the OpenAPI document.
* 

The [Kubernetes OpenAPI Document](https://kubernetes.io/docs/concepts/overview/kubernetes-api/#openapi-interface-definition) provides (full) [OpenAPI v2.0 and 3.0 schemas](https://www.openapis.org/) for all Kubernetes API endpoints. The OpenAPI v3 is the preferred method for accessing OpenAPI as it provides a more comprehensive and accurate view of the API. It includes all the available API paths, as well as all resources consumed and produced for every operations on every endpoints. It also includes any extensibility components that a cluster supports. The data is a complete specification and is significantly larger than that from the Discovery API.

## Discovery API[](https://kubernetes.io/docs/concepts/overview/kubernetes-api/#discovery-api)

Kubernetes publishes a list of all group versions and resources supported via the Discovery API. This includes the following for each resource:
* Name
* Cluster or namespaced scope
* Endpoint URL and supported verbs
* Alternative names
* Group, version, kind

The API is available in both aggregated and unaggregated form. The aggregated discovery serves two endpoints, while the unaggregated discovery serves a separate endpoint for each group version.

### Aggregated discovery[](https://kubernetes.io/docs/concepts/overview/kubernetes-api/#aggregated-discovery)FEATURE STATE: `Kubernetes v1.30 [stable]`(enabled by default)

Kubernetes offers stable support for aggregated discovery, publishing all resources supported by a cluster through two endpoints (`/api` and `/apis`). Requesting this endpoint drastically reduces the number of requests sent to fetch the discovery data from the cluster. You can access the data by requesting the respective endpoints with an `Accept` header indicating the aggregated discovery resource: `Accept: application/json;v=v2;g=apidiscovery.k8s.io;as=APIGroupDiscoveryList`.

Without indicating the resource type using the `Accept` header, the default response for the `/api` and `/apis` endpoint is an unaggregated discovery document.

The [discovery document](https://github.com/kubernetes/kubernetes/blob/release-1.36/api/discovery/aggregated_v2.json) for the built-in resources can be found in the Kubernetes GitHub repository. This Github document can be used as a reference of the base set of the available resources if a Kubernetes cluster is not available to query.

The endpoint also supports ETag and protobuf encoding.

### Unaggregated discovery[](https://kubernetes.io/docs/concepts/overview/kubernetes-api/#unaggregated-discovery)

Without discovery aggregation, discovery is published in levels, with the root endpoints publishing discovery information for downstream documents.

A list of all group versions supported by a cluster is published at the `/api` and `/apis` endpoints. Example:
```yaml
{
  "kind": "APIGroupList",
  "apiVersion": "v1",
  "groups": [
    {
      "name": "apiregistration.k8s.io",
      "versions": [
        {
          "groupVersion": "apiregistration.k8s.io/v1",
          "version": "v1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "apiregistration.k8s.io/v1",
        "version": "v1"
      }
    },
    {
      "name": "apps",
      "versions": [
        {
          "groupVersion": "apps/v1",
          "version": "v1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "apps/v1",
        "version": "v1"
      }
    },
    ...
}
```

Additional requests are needed to obtain the discovery document for each group version at `/apis/<group>/<version>` (for example: `/apis/rbac.authorization.k8s.io/v1alpha1`), which advertises the list of resources served under a particular group version. These endpoints are used by kubectl to fetch the list of resources supported by a cluster.[

## OpenAPI interface definition[](https://kubernetes.io/docs/concepts/overview/kubernetes-api/#openapi-interface-definition)

For details about the OpenAPI specifications, see the [OpenAPI documentation](https://www.openapis.org/).

Kubernetes serves both OpenAPI v2.0 and OpenAPI v3.0. OpenAPI v3 is the preferred method of accessing the OpenAPI because it offers a more comprehensive (lossless) representation of Kubernetes resources. Due to limitations of OpenAPI version 2, certain fields are dropped from the published OpenAPI including but not limited to `default`, `nullable`, `oneOf`.

### OpenAPI V2[](https://kubernetes.io/docs/concepts/overview/kubernetes-api/#openapi-v2)

The Kubernetes API server serves an aggregated OpenAPI v2 spec via the `/openapi/v2` endpoint. You can request the response format using request headers as follows:Valid request header values for OpenAPI v2 queries``````````````

| Header | Possible values | Notes || --- | --- | --- || Accept-Encoding | gzip | not supplying this header is also acceptable || Accept | application/com.github.proto-openapi.spec.v2@v1.0+protobuf | mainly for intra-cluster use || application/json | default |  || * | serves application/json |  |

#### Warning:The validation rules published as part of OpenAPI schemas may not be complete, and usually aren't. Additional validation occurs within the API server. If you want precise and complete verification, a `kubectl apply --dry-run=server` runs all the applicable validation (and also activates admission-time checks).

---



# Source (Sub-link): https://kubernetes.io/docs/concepts/overview/working-with-objects/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Overview](https://kubernetes.io/docs/concepts/overview/)
4. Objects In Kubernetes

# Objects In KubernetesKubernetes objects are persistent entities in the Kubernetes system. Kubernetes uses these entities to represent the state of your cluster. Learn about the Kubernetes object model and how to work with these objects.

This page explains how Kubernetes objects are represented in the Kubernetes API, and how you can express them in `.yaml` format.

## Understanding Kubernetes objects[](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects)

Kubernetes objects are persistent entities in the Kubernetes system. Kubernetes uses these entities to represent the state of your cluster. Specifically, they can describe:
* What containerized applications are running (and on which nodes)
* The resources available to those applications
* The policies around how those applications behave, such as restart policies, upgrades, and fault-tolerance

A Kubernetes object is a "record of intent"--once you create the object, the Kubernetes system will constantly work to ensure that the object exists. By creating an object, you're effectively telling the Kubernetes system what you want your cluster's workload to look like; this is your cluster's desired state.

To work with Kubernetes objects—whether to create, modify, or delete them—you'll need to use the [Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/). When you use the `kubectl` command-line interface, for example, the CLI makes the necessary Kubernetes API calls for you. You can also use the Kubernetes API directly in your own programs using one of the [Client Libraries](https://kubernetes.io/docs/reference/using-api/client-libraries/).

### Object spec and status[](https://kubernetes.io/docs/concepts/overview/working-with-objects/#object-spec-and-status)

Almost every Kubernetes object includes two nested object fields that govern the object's configuration: the object `spec` and the object `status`. For objects that have a `spec`, you have to set this when you create the object, providing a description of the characteristics you want the resource to have: its desired state.

The `status` describes the current state of the object, supplied and updated by the Kubernetes system and its components. The Kubernetes [control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane) continually and actively manages every object's actual state to match the desired state you supplied.

For example: in Kubernetes, a Deployment is an object that can represent an application running on your cluster. When you create the Deployment, you might set the Deployment `spec` to specify that you want three replicas of the application to be running. The Kubernetes system reads the Deployment spec and starts three instances of your desired application--updating the status to match your spec. If any of those instances should fail (a status change), the Kubernetes system responds to the difference between spec and status by making a correction--in this case, starting a replacement instance.

For more information on the object spec, status, and metadata, see the [Kubernetes API Conventions](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md).

### Describing a Kubernetes object[](https://kubernetes.io/docs/concepts/overview/working-with-objects/#describing-a-kubernetes-object)

When you create an object in Kubernetes, you must provide the object spec that describes its desired state, as well as some basic information about the object (such as a name). When you use the Kubernetes API to create the object (either directly or via `kubectl`), that API request must include that information as JSON in the request body. Most often, you provide the information to `kubectl` in a file known as a manifest. By convention, manifests are YAML (you could also use JSON format). Tools such as `kubectl` convert the information from a manifest into JSON or another supported serialization format when making the API request over HTTP.

Here's an example manifest that shows the required fields and object spec for a Kubernetes Deployment:[`application/deployment.yaml` ](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/application/deployment.yaml)

![Diagram](https://kubernetes.io/images/copycode.svg)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 2 # tells deployment to run 2 pods matching the template
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

---



# Source (Sub-link): https://kubernetes.io/docs/concepts/configuration/secret/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Configuration](https://kubernetes.io/docs/concepts/configuration/)
4. Secrets

# Secrets

A Secret is an object that contains a small amount of sensitive data such as a password, a token, or a key. Such information might otherwise be put in a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/) specification or in a [container image](https://kubernetes.io/docs/reference/glossary/?all=true#term-image). Using a Secret means that you don't need to include confidential data in your application code.

Because Secrets can be created independently of the Pods that use them, there is less risk of the Secret (and its data) being exposed during the workflow of creating, viewing, and editing Pods. Kubernetes, and applications that run in your cluster, can also take additional precautions with Secrets, such as avoiding writing sensitive data to nonvolatile storage.

Secrets are similar to [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/) but are specifically intended to hold confidential data.

#### Caution:

Kubernetes Secrets are, by default, stored unencrypted in the API server's underlying data store (etcd). Anyone with API access can retrieve or modify a Secret, and so can anyone with access to etcd. Additionally, anyone who is authorized to create a Pod in a namespace can use that access to read any Secret in that namespace; this includes indirect access such as the ability to create a Deployment.

In order to safely use Secrets, take at least the following steps:
1. [Enable Encryption at Rest](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/) for Secrets.
2. [Enable or configure RBAC rules](https://kubernetes.io/docs/reference/access-authn-authz/authorization/) with least-privilege access to Secrets.
3. Restrict Secret access to specific containers.
4. [Consider using external Secret store providers](https://secrets-store-csi-driver.sigs.k8s.io/concepts.html#provider-for-the-secrets-store-csi-driver).

For more guidelines to manage and improve the security of your Secrets, refer to [Good practices for Kubernetes Secrets](https://kubernetes.io/docs/concepts/security/secrets-good-practices/).

See [Information security for Secrets](https://kubernetes.io/docs/concepts/configuration/secret/#information-security-for-secrets) for more details.

## Uses for Secrets[](https://kubernetes.io/docs/concepts/configuration/secret/#uses-for-secrets)

You can use Secrets for purposes such as the following:
* [Set environment variables for a container](https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/#define-container-environment-variables-using-secret-data).
* [Provide credentials such as SSH keys or passwords to Pods](https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/#provide-prod-test-creds).
* [Allow the kubelet to pull container images from private registries](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/).

The Kubernetes control plane also uses Secrets; for example, [bootstrap token Secrets](https://kubernetes.io/docs/concepts/configuration/secret/#bootstrap-token-secrets) are a mechanism to help automate node registration.

### Use case: dotfiles in a secret volume[](https://kubernetes.io/docs/concepts/configuration/secret/#use-case-dotfiles-in-a-secret-volume)

You can make your data "hidden" by defining a key that begins with a dot. This key represents a dotfile or "hidden" file. For example, when the following Secret is mounted into a volume, `secret-volume`, the volume will contain a single file, called `.secret-file`, and the `dotfile-test-container` will have this file present at the path `/etc/secret-volume/.secret-file`.

#### Note:Files beginning with dot characters are hidden from the output of `ls -l`; you must use `ls -la` to see them when listing directory contents.[`secret/dotfile-secret.yaml` ](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/secret/dotfile-secret.yaml)

![Diagram](https://kubernetes.io/images/copycode.svg)

---



# Source (Sub-link): https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Tasks](https://kubernetes.io/docs/tasks/)
3. [Extend Kubernetes](https://kubernetes.io/docs/tasks/extend-kubernetes/)
4. [Use Custom Resources](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/)
5. Extend the Kubernetes API with CustomResourceDefinitions

# Extend the Kubernetes API with CustomResourceDefinitions

This page shows how to install a [custom resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) into the Kubernetes API by creating a [CustomResourceDefinition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.36/#customresourcedefinition-v1-apiextensions-k8s-io).

## Before you begin[](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#before-you-begin)

You need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a cluster, you can create one by using [minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/) or you can use one of these Kubernetes playgrounds:
* [iximiuz Labs](https://labs.iximiuz.com/playgrounds?category=kubernetes&filter=all)
* [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
* [KodeKloud](https://kodekloud.com/public-playgrounds)
Your Kubernetes server must be at or later than version 1.16.

To check the version, enter `kubectl version`.If you are using an older version of Kubernetes that is still supported, switch to the documentation for that version to see advice that is relevant for your cluster.

## Create a CustomResourceDefinition[](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#create-a-customresourcedefinition)

When you create a new CustomResourceDefinition (CRD), the Kubernetes API Server creates a new RESTful resource path for each version you specify. The custom resource created from a CRD object can be either namespaced or cluster-scoped, as specified in the CRD's `spec.scope` field. As with existing built-in objects, deleting a namespace deletes all custom objects in that namespace. CustomResourceDefinitions themselves are non-namespaced and are available to all namespaces.

For example, if you save the following CustomResourceDefinition to `resourcedefinition.yaml`:
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  # name must match the spec fields below, and be in the form: <plural>.<group>
  name: crontabs.stable.example.com
spec:
  # group name to use for REST API: /apis/<group>/<version>
  group: stable.example.com
  # list of versions supported by this CustomResourceDefinition
  versions:
    - name: v1
      # Each version can be enabled/disabled by Served flag.
      served: true
      # One and only one version must be marked as the storage version.
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                cronSpec:
                  type: string
                image:
                  type: string
                replicas:
                  type: integer
  # either Namespaced or Cluster
  scope: Namespaced
  names:
    # plural name to be used in the URL: /apis/<group>/<version>/<plural>
    plural: crontabs
    # singular name to be used as an alias on the CLI and for display
    singular: crontab
    # kind is normally the CamelCased singular type. Your resource manifests use this.
    kind: CronTab
    # shortNames allow shorter string to match your resource on the CLI
    shortNames:
    - ct
```

and create it:
```yaml
kubectl apply -f resourcedefinition.yaml
```

Then a new namespaced RESTful API endpoint is created at:
```yaml
/apis/stable.example.com/v1/namespaces/*/crontabs/...
```

This endpoint URL can then be used to create and manage custom objects. The `kind` of these objects will be `CronTab` from the spec of the CustomResourceDefinition object you created above.

It might take a few seconds for the endpoint to be created. You can watch the `Established` condition of your CustomResourceDefinition to be true or watch the discovery information of the API server for your resource to show up.

## Create custom objects[](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#create-custom-objects)

After the CustomResourceDefinition object has been created, you can create custom objects. Custom objects can contain custom fields. These fields can contain arbitrary JSON. In the following example, the `cronSpec` and `image` custom fields are set in a custom object of kind `CronTab`. The kind `CronTab` comes from the spec of the CustomResourceDefinition object you created above.

If you save the following YAML to `my-crontab.yaml`:
```yaml
apiVersion: "stable.example.com/v1"
kind: CronTab
metadata:
  name: my-new-cron-object
spec:
  cronSpec: "* * * * */5"
  image: my-awesome-cron-image
```

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



# Source (Sub-link): https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Tasks](https://kubernetes.io/docs/tasks/)
3. [Extend Kubernetes](https://kubernetes.io/docs/tasks/extend-kubernetes/)
4. [Use Custom Resources](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/)
5. Versions in CustomResourceDefinitions

# Versions in CustomResourceDefinitions

This page explains how to add versioning information to [CustomResourceDefinitions](https://kubernetes.io/docs/reference/kubernetes-api/extend-resources/custom-resource-definition-v1/), to indicate the stability level of your CustomResourceDefinitions or advance your API to a new version with conversion between API representations. It also describes how to upgrade an object from one version to another.

## Before you begin[](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/#before-you-begin)

You need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a cluster, you can create one by using [minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/) or you can use one of these Kubernetes playgrounds:
* [iximiuz Labs](https://labs.iximiuz.com/playgrounds?category=kubernetes&filter=all)
* [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
* [KodeKloud](https://kodekloud.com/public-playgrounds)

You should have an initial understanding of [custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/).Your Kubernetes server must be at or later than version v1.16.

To check the version, enter `kubectl version`.

## Overview[](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/#overview)

The CustomResourceDefinition API provides a workflow for introducing and upgrading to new versions of a CustomResourceDefinition.

When a CustomResourceDefinition is created, the first version is set in the CustomResourceDefinition `spec.versions` list to an appropriate stability level and a version number. For example `v1beta1` would indicate that the first version is not yet stable. All custom resource objects will initially be stored at this version.

Once the CustomResourceDefinition is created, clients may begin using the `v1beta1` API.

Later it might be necessary to add new version such as `v1`.

Adding a new version:
1. Pick a conversion strategy. Since custom resource objects need the ability to be served at both versions, that means they will sometimes be served in a different version than the one stored. To make this possible, the custom resource objects must sometimes be converted between the version they are stored at and the version they are served at. If the conversion involves schema changes and requires custom logic, a conversion webhook should be used. If there are no schema changes, the default `None` conversion strategy may be used and only the `apiVersion` field will be modified when serving different versions.
2. If using conversion webhooks, create and deploy the conversion webhook. See the [Webhook conversion](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/#webhook-conversion) for more details.
3. Update the CustomResourceDefinition to include the new version in the `spec.versions` list with `served:true`. Also, set `spec.conversion` field to the selected conversion strategy. If using a conversion webhook, configure `spec.conversion.webhookClientConfig` field to call the webhook.

Once the new version is added, clients may incrementally migrate to the new version. It is perfectly safe for some clients to use the old version while others use the new version.

Migrate stored objects to the new version:
1. See the [upgrade existing objects to a new stored version](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/#upgrade-existing-objects-to-a-new-stored-version) section.

It is safe for clients to use both the old and new version before, during and after upgrading the objects to a new stored version.

Removing an old version:
1. Ensure all clients are fully migrated to the new version. The kube-apiserver logs can be reviewed to help identify any clients that are still accessing via the old version.
2. Set `served` to `false` for the old version in the `spec.versions` list. If any clients are still unexpectedly using the old version they may begin reporting errors attempting to access the custom resource objects at the old version. If this occurs, switch back to using `served:true` on the old version, migrate the remaining clients to the new version and repeat this step.
3. Ensure the [upgrade of existing objects to the new stored version](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/#upgrade-existing-objects-to-a-new-stored-version) step has been completed.
  1. Verify that the `storage` is set to `true` for the new version in the `spec.versions` list in the CustomResourceDefinition.
  2. Verify that the old version is no longer listed in the CustomResourceDefinition `status.storedVersions`.
4. Remove the old version from the CustomResourceDefinition `spec.versions` list.
5. Drop conversion support for the old version in conversion webhooks.

## Specify multiple versions[](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/#specify-multiple-versions)

The CustomResourceDefinition API `versions` field can be used to support multiple versions of custom resources that you have developed. Versions can have different schemas, and conversion webhooks can convert custom resources between versions. Webhook conversions should follow the [Kubernetes API conventions](https://github.com/kubernetes/community/blob/main/contributors/devel/sig-architecture/api-conventions.md) wherever applicable. Specifically, See the [API change documentation](https://github.com/kubernetes/community/blob/main/contributors/devel/sig-architecture/api_changes.md) for a set of useful gotchas and suggestions.

#### Note:In `apiextensions.k8s.io/v1beta1`, there was a `version` field instead of `versions`. The `version` field is deprecated and optional, but if it is not empty, it must match the first item in the `versions` field.

This example shows a CustomResourceDefinition with two versions. For the first example, the assumption is all versions share the same schema with no conversion between them. The comments in the YAML provide more context.
*  apiextensions.k8s.io/v1
*  apiextensions.k8s.io/v1beta1

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  # name must match the spec fields below, and be in the form: <plural>.<group>
  name: crontabs.example.com
spec:
  # group name to use for REST API: /apis/<group>/<version>
  group: example.com
  # list of versions supported by this CustomResourceDefinition
  versions:
  - name: v1beta1
    # Each version can be enabled/disabled by Served flag.
    served: true
    # One and only one version must be marked as the storage version.
    storage: true
    # A schema is required
    schema:
      openAPIV3Schema:
        type: object
        properties:
          host:
            type: string
          port:
            type: string
  - name: v1
    served: true
    storage: false
    schema:
      openAPIV3Schema:
        type: object
        properties:
          host:
            type: string
          port:
            type: string
  # The conversion section is introduced in Kubernetes 1.13+ with a default value of
  # None conversion (strategy sub-field set to None).
  conversion:
    # None conversion assumes the same schema for all versions and only sets the apiVersion
    # field of custom resources to the proper value
    strategy: None
  # either Namespaced or Cluster
  scope: Namespaced
  names:
    # plural name to be used in the URL: /apis/<group>/<version>/<plural>
    plural: crontabs
    # singular name to be used as an alias on the CLI and for display
    singular: crontab
    # kind is normally the CamelCased singular type. Your resource manifests use this.
    kind: CronTab
    # shortNames allow shorter string to match your resource on the CLI
    shortNames:
    - ct
```

---



# Source (Sub-link): https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Overview](https://kubernetes.io/docs/concepts/overview/)
4. [Objects In Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/)
5. Field Selectors

# Field Selectors

Field selectors let you select Kubernetes [objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects) based on the value of one or more resource fields. Here are some examples of field selector queries:
* `metadata.name=my-service`
* `metadata.namespace!=default`
* `status.phase=Pending`

This `kubectl` command selects all Pods for which the value of the [`status.phase`](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase) field is `Running`:
```yaml
kubectl get pods --field-selector status.phase=Running
```

#### Note:Field selectors are essentially resource filters. By default, no selectors/filters are applied, meaning that all resources of the specified type are selected. This makes the `kubectl` queries `kubectl get pods` and `kubectl get pods --field-selector ""` equivalent.

## Supported fields[](https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/#supported-fields)

Supported field selectors vary by Kubernetes resource type. All resource types support the `metadata.name` and `metadata.namespace` fields. Using unsupported field selectors produces an error. For example:
```yaml
kubectl get ingress --field-selector foo.bar=baz
```

---

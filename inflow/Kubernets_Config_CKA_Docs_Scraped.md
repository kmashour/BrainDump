# Consolidated Kubernets Config CKA Docs.md

This file is automatically scraped and consolidated by the batch ingestion pipeline.



# Source: https://kubernetes.io/docs/concepts/configuration/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. Configuration

# ConfigurationResources that Kubernetes provides for configuring Pods.

##### [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)

##### [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

---



# Source: https://kubernetes.io/docs/concepts/configuration/configmap/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Configuration](https://kubernetes.io/docs/concepts/configuration/)
4. ConfigMaps

# ConfigMaps

A ConfigMap is an API object used to store non-confidential data in key-value pairs. [Pods](https://kubernetes.io/docs/concepts/workloads/pods/) can consume ConfigMaps as environment variables, command-line arguments, or as configuration files in a [volume](https://kubernetes.io/docs/concepts/storage/volumes/).

A ConfigMap allows you to decouple environment-specific configuration from your [container images](https://kubernetes.io/docs/reference/glossary/?all=true#term-image), so that your applications are easily portable.

#### Caution:ConfigMap does not provide secrecy or encryption. If the data you want to store are confidential, use a [Secret](https://kubernetes.io/docs/concepts/configuration/secret/) rather than a ConfigMap, or use additional (third party) tools to keep your data private.

## Motivation[](https://kubernetes.io/docs/concepts/configuration/configmap/#motivation)

Use a ConfigMap for setting configuration data separately from application code.

For example, imagine that you are developing an application that you can run on your own computer (for development) and in the cloud (to handle real traffic). You write the code to look in an environment variable named `DATABASE_HOST`. Locally, you set that variable to `localhost`. In the cloud, you set it to refer to a Kubernetes [Service](https://kubernetes.io/docs/concepts/services-networking/service/) that exposes the database component to your cluster. This lets you fetch a container image running in the cloud and debug the exact same code locally if needed.

#### Note:A ConfigMap is not designed to hold large chunks of data. The data stored in a ConfigMap cannot exceed 1 MiB. If you need to store settings that are larger than this limit, you may want to consider mounting a volume or use a separate database or file service.

## ConfigMap object[](https://kubernetes.io/docs/concepts/configuration/configmap/#configmap-object)

A ConfigMap is an [API object](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects) that lets you store configuration for other objects to use. Unlike most Kubernetes objects that have a `spec`, a ConfigMap has `data` and `binaryData` fields. These fields accept key-value pairs as their values. Both the `data` field and the `binaryData` are optional. The `data` field is designed to contain UTF-8 strings while the `binaryData` field is designed to contain binary data as base64-encoded strings.

The name of a ConfigMap must be a valid [DNS subdomain name](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names).

Each key under the `data` or the `binaryData` field must consist of alphanumeric characters, `-`, `_` or `.`. The keys stored in `data` must not overlap with the keys in the `binaryData` field.

Starting from v1.19, you can add an `immutable` field to a ConfigMap definition to create an [immutable ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/#configmap-immutable).

## ConfigMaps and Pods[](https://kubernetes.io/docs/concepts/configuration/configmap/#configmaps-and-pods)

You can write a Pod `spec` that refers to a ConfigMap and configures the container(s) in that Pod based on the data in the ConfigMap. The Pod and the ConfigMap must be in the same [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces).

#### Note:The `spec` of a [static Pod](https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/) cannot refer to a ConfigMap or any other API objects.

---



# Source: https://kubernetes.io/docs/concepts/configuration/secret/

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



# Source: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

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



# Source: https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Configuration](https://kubernetes.io/docs/concepts/configuration/)
4. Organizing Cluster Access Using kubeconfig Files

# Organizing Cluster Access Using kubeconfig Files

Use kubeconfig files to organize information about clusters, users, namespaces, and authentication mechanisms. The `kubectl` command-line tool uses kubeconfig files to find the information it needs to choose a cluster and communicate with the API server of a cluster.

#### Note:A file that is used to configure access to clusters is called a kubeconfig file. This is a generic way of referring to configuration files. It does not mean that there is a file named `kubeconfig`.

#### Warning:Only use kubeconfig files from trusted sources. Using a specially-crafted kubeconfig file could result in malicious code execution or file exposure. If you must use an untrusted kubeconfig file, inspect it carefully first, much as you would a shell script.

By default, `kubectl` looks for a file named `config` in the `$HOME/.kube` directory. You can specify other kubeconfig files by setting the `KUBECONFIG` environment variable or by setting the [`--kubeconfig`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl/) flag.

For step-by-step instructions on creating and specifying kubeconfig files, see [Configure Access to Multiple Clusters](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/).

## Supporting multiple clusters, users, and authentication mechanisms[](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/#supporting-multiple-clusters-users-and-authentication-mechanisms)

Suppose you have several clusters, and your users and components authenticate in a variety of ways. For example:
* A running kubelet might authenticate using certificates.
* A user might authenticate using tokens.
* Administrators might have sets of certificates that they provide to individual users.

With kubeconfig files, you can organize your clusters, users, and namespaces. You can also define contexts to quickly and easily switch between clusters and namespaces.

## Context[](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/#context)

A context element in a kubeconfig file is used to group access parameters under a convenient name. Each context has three parameters: cluster, namespace, and user. By default, the `kubectl` command-line tool uses parameters from the current context to communicate with the cluster.

To choose the current context:
```yaml
kubectl config use-context
```

## The KUBECONFIG environment variable[](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/#the-kubeconfig-environment-variable)

The `KUBECONFIG` environment variable holds a list of kubeconfig files. For Linux and Mac, the list is colon-delimited. For Windows, the list is semicolon-delimited. The `KUBECONFIG` environment variable is not required. If the `KUBECONFIG` environment variable doesn't exist, `kubectl` uses the default kubeconfig file, `$HOME/.kube/config`.

If the `KUBECONFIG` environment variable does exist, `kubectl` uses an effective configuration that is the result of merging the files listed in the `KUBECONFIG` environment variable.

## Merging kubeconfig files[](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/#merging-kubeconfig-files)

To see your configuration, enter this command:
```yaml
kubectl config view
```

---



# Source: https://kubernetes.io/docs/concepts/configuration/windows-resource-management/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Configuration](https://kubernetes.io/docs/concepts/configuration/)
4. Resource Management for Windows nodes

# Resource Management for Windows nodes

This page outlines the differences in how resources are managed between Linux and Windows.

On Linux nodes, [cgroups](https://kubernetes.io/docs/reference/glossary/?all=true#term-cgroup) are used as a pod boundary for resource control. Containers are created within that boundary for network, process and file system isolation. The Linux cgroup APIs can be used to gather CPU, I/O, and memory use statistics.

In contrast, Windows uses a [job object](https://docs.microsoft.com/windows/win32/procthread/job-objects) per container with a system namespace filter to contain all processes in a container and provide logical isolation from the host. (Job objects are a Windows process isolation mechanism and are different from what Kubernetes refers to as a [Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/)).

There is no way to run a Windows container without the namespace filtering in place. This means that system privileges cannot be asserted in the context of the host, and thus privileged containers are not available on Windows. Containers cannot assume an identity from the host because the Security Account Manager (SAM) is separate.

## Memory management[](https://kubernetes.io/docs/concepts/configuration/windows-resource-management/#resource-management-memory)

Windows does not have an out-of-memory process killer as Linux does. Windows always treats all user-mode memory allocations as virtual, and pagefiles are mandatory.

Windows nodes do not overcommit memory for processes. The net effect is that Windows won't reach out of memory conditions the same way Linux does, and processes page to disk instead of being subject to out of memory (OOM) termination. If memory is over-provisioned and all physical memory is exhausted, then paging can slow down performance.

## CPU management[](https://kubernetes.io/docs/concepts/configuration/windows-resource-management/#resource-management-cpu)

Windows can limit the amount of CPU time allocated for different processes but cannot guarantee a minimum amount of CPU time.

On Windows, the kubelet supports a command-line flag to set the [scheduling priority](https://docs.microsoft.com/windows/win32/procthread/scheduling-priorities) of the kubelet process: `--windows-priorityclass`. This flag allows the kubelet process to get more CPU time slices when compared to other processes running on the Windows host. More information on the allowable values and their meaning is available at [Windows Priority Classes](https://docs.microsoft.com/en-us/windows/win32/procthread/scheduling-priorities#priority-class). To ensure that running Pods do not starve the kubelet of CPU cycles, set this flag to `ABOVE_NORMAL_PRIORITY_CLASS` or above.

## Resource reservation[](https://kubernetes.io/docs/concepts/configuration/windows-resource-management/#resource-reservation)

To account for memory and CPU used by the operating system, the container runtime, and by Kubernetes host processes such as the kubelet, you can (and should) reserve memory and CPU resources with the `--kube-reserved` and/or `--system-reserved` kubelet flags. On Windows these values are only used to calculate the node's [allocatable](https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable) resources.

#### Caution:

As you deploy workloads, set resource memory and CPU limits on containers. This also subtracts from `NodeAllocatable` and helps the cluster-wide scheduler in determining which pods to place on which nodes.

Scheduling pods without limits may over-provision the Windows nodes and in extreme cases can cause the nodes to become unhealthy.

On Windows, a good practice is to reserve at least 2GiB of memory.

To determine how much CPU to reserve, identify the maximum pod density for each node and monitor the CPU usage of the system services running there, then choose a value that meets your workload needs.

## Feedback

Was this page helpful?Yes No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes). Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to [report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io) or [suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).const yes=document.querySelector(".feedback--yes"),no=document.querySelector(".feedback--no");document.querySelectorAll(".feedback--link").forEach(e=>{e.href=e.href+window.location.pathname});const sendFeedback=e=>{typeof gtag=="function"?gtag("event","page_helpful",{event_category:"Helpful",event_label:window.location.pathname,value:e}):console.log("gtag not available; skipping analytics event")},disableButtons=()=>{yes.disabled=!0,yes.classList.add("feedback--button__disabled"),no.disabled=!0,no.classList.add("feedback--button__disabled")};yes.addEventListener("click",()=>{sendFeedback(100),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")}),no.addEventListener("click",()=>{sendFeedback(0),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")})Last modified June 06, 2022 at 2:04 PM PST: [Updating Windows intro and resource management pages (#34083) (eb88ef7c3e)](https://github.com/kubernetes/website/commit/eb88ef7c3ef920a36041781c0702bb4a77d5cf23)

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



# Source (Sub-link): https://kubernetes.io/docs/concepts/security/secrets-good-practices/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Security](https://kubernetes.io/docs/concepts/security/)
4. Good practices for Kubernetes Secrets

# Good practices for Kubernetes SecretsPrinciples and practices for good Secret management for cluster administrators and application developers.

In Kubernetes, a Secret is an object that stores sensitive information, such as passwords, OAuth tokens, and SSH keys.

Secrets give you more control over how sensitive information is used and reduces the risk of accidental exposure. Secret values are encoded as base64 strings and are stored unencrypted by default, but can be configured to be [encrypted at rest](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/#ensure-all-secrets-are-encrypted).

A [Pod](https://kubernetes.io/docs/concepts/workloads/pods/) can reference the Secret in a variety of ways, such as in a volume mount or as an environment variable. Secrets are designed for confidential data and [ConfigMaps](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) are designed for non-confidential data.

The following good practices are intended for both cluster administrators and application developers. Use these guidelines to improve the security of your sensitive information in Secret objects, as well as to more effectively manage your Secrets.

## Cluster administrators[](https://kubernetes.io/docs/concepts/security/secrets-good-practices/#cluster-administrators)

This section provides good practices that cluster administrators can use to improve the security of confidential information in the cluster.

### Configure encryption at rest[](https://kubernetes.io/docs/concepts/security/secrets-good-practices/#configure-encryption-at-rest)

By default, Secret objects are stored unencrypted in [etcd](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/). You should configure encryption of your Secret data in `etcd`. For instructions, refer to [Encrypt Secret Data at Rest](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/).

### Configure least-privilege access to Secrets[](https://kubernetes.io/docs/concepts/security/secrets-good-practices/#least-privilege-secrets)

When planning your access control mechanism, such as Kubernetes [Role-based Access Control](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) [(RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/), consider the following guidelines for access to `Secret` objects. You should also follow the other guidelines in [RBAC good practices](https://kubernetes.io/docs/concepts/security/rbac-good-practices/).
* Components: Restrict `watch` or `list` access to only the most privileged, system-level components. Only grant `get` access for Secrets if the component's normal behavior requires it.
* Humans: Restrict `get`, `watch`, or `list` access to Secrets. Only allow cluster administrators to access `etcd`. This includes read-only access. For more complex access control, such as restricting access to Secrets with specific annotations, consider using third-party authorization mechanisms.

#### Caution:Granting `list` access to Secrets implicitly lets the subject fetch the contents of the Secrets.

A user who can create a Pod that uses a Secret can also see the value of that Secret. Even if cluster policies do not allow a user to read the Secret directly, the same user could have access to run a Pod that then exposes the Secret. You can detect or limit the impact caused by Secret data being exposed, either intentionally or unintentionally, by a user with this access. Some recommendations include:
* Use short-lived Secrets
* Implement audit rules that alert on specific events, such as concurrent reading of multiple Secrets by a single user

#### Restrict Access for Secrets[](https://kubernetes.io/docs/concepts/security/secrets-good-practices/#restrict-access-for-secrets)

Use separate namespaces to isolate access to mounted secrets.

### Improve etcd management policies[](https://kubernetes.io/docs/concepts/security/secrets-good-practices/#improve-etcd-management-policies)

Consider wiping or shredding the durable storage used by `etcd` once it is no longer in use.

If there are multiple `etcd` instances, configure encrypted SSL/TLS communication between the instances to protect the Secret data in transit.

### Configure access to external Secrets[](https://kubernetes.io/docs/concepts/security/secrets-good-practices/#configure-access-to-external-secrets)Note: This section links to third party projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for these projects, which are listed alphabetically. To add a project to this list, read the [content guide](https://kubernetes.io/docs/contribute/style/content-guide/#third-party-content) before submitting a change. [More information.](https://kubernetes.io/docs/concepts/security/secrets-good-practices/#third-party-content-disclaimer)

---

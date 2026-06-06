# Consolidated KubernetesOverviewDocs.md

This file is automatically scraped and consolidated by the batch ingestion pipeline.



# Source: https://kubernetes.io/docs/concepts/overview/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. Overview

# OverviewKubernetes is a portable, extensible, open source platform for managing containerized workloads and services that facilitate both declarative configuration and automation. It has a large, rapidly growing ecosystem. Kubernetes services, support, and tools are widely available.

This page is an overview of Kubernetes.

The name Kubernetes originates from Greek, meaning helmsman or pilot. K8s as an abbreviation results from counting the eight letters between the "K" and the "s". Google open sourced the Kubernetes project in 2014. Kubernetes combines [over 15 years of Google's experience](https://kubernetes.io/blog/2015/04/borg-predecessor-to-kubernetes/) running production workloads at scale with best-of-breed ideas and practices from the community.

## Why you need Kubernetes and what it can do[](https://kubernetes.io/docs/concepts/overview/#why-you-need-kubernetes-and-what-can-it-do)

Containers are a good way to bundle and run your applications. In a production environment, you need to manage the containers that run the applications and ensure that there is no downtime. For example, if a container goes down, another container needs to start. Wouldn't it be easier if this behavior was handled by a system?

That's how Kubernetes comes to the rescue! Kubernetes provides you with a framework to run distributed systems resiliently. It takes care of scaling and failover for your application, provides deployment patterns, and more. For example: Kubernetes can easily manage a canary deployment for your system.

Kubernetes provides you with:
* Service discovery and load balancing Kubernetes can expose a container using a DNS name or its own IP address. If traffic to a container is high, Kubernetes is able to load balance and distribute the network traffic so that the deployment is stable.
* Storage orchestration Kubernetes allows you to automatically mount a storage system of your choice, such as local storage, public cloud providers, and more.
* Automated rollouts and rollbacks You can describe the desired state for your deployed containers using Kubernetes, and it can change the actual state to the desired state at a controlled rate. For example, you can automate Kubernetes to create new containers for your deployment, remove existing containers and adopt all their resources to the new container.
* Automatic bin packing You provide Kubernetes with a cluster of nodes that it can use to run containerized tasks. You tell Kubernetes how much CPU and memory (RAM) each container needs. Kubernetes can fit containers onto your nodes to make the best use of your resources.
* Self-healing Kubernetes restarts containers that fail, replaces containers, kills containers that don't respond to your user-defined health check, and doesn't advertise them to clients until they are ready to serve.
* Secret and configuration management Kubernetes lets you store and manage sensitive information, such as passwords, OAuth tokens, and SSH keys. You can deploy and update secrets and application configuration without rebuilding your container images, and without exposing secrets in your stack configuration.
* Batch execution In addition to services, Kubernetes can manage your batch and CI workloads, replacing containers that fail, if desired.
* Horizontal scaling Scale your application up and down with a simple command, with a UI, or automatically based on CPU usage.
* IPv4/IPv6 dual-stack Allocation of IPv4 and IPv6 addresses to Pods and Services.
* Designed for extensibility Add features to your Kubernetes cluster without changing upstream source code.

## What Kubernetes is not[](https://kubernetes.io/docs/concepts/overview/#what-kubernetes-is-not)

Kubernetes is not a traditional, all-inclusive PaaS (Platform as a Service) system. Since Kubernetes operates at the container level rather than at the hardware level, it provides some generally applicable features common to PaaS offerings, such as deployment, scaling, load balancing, and lets users integrate their logging, monitoring, and alerting solutions. However, Kubernetes is not monolithic, and these default solutions are optional and pluggable. Kubernetes provides the building blocks for building developer platforms, but preserves user choice and flexibility where it is important.

Kubernetes:
* Does not limit the types of applications supported. Kubernetes aims to support an extremely diverse variety of workloads, including stateless, stateful, and data-processing workloads. If an application can run in a container, it should run great on Kubernetes.
* Does not deploy source code and does not build your application. Continuous Integration, Delivery, and Deployment (CI/CD) workflows are determined by organization cultures and preferences as well as technical requirements.
* Does not provide application-level services, such as middleware (for example, message buses), data-processing frameworks (for example, Spark), databases (for example, MySQL), caches, nor cluster storage systems (for example, Ceph) as built-in services. Such components can run on Kubernetes, and/or can be accessed by applications running on Kubernetes through portable mechanisms, such as the [Open Service Broker](https://openservicebrokerapi.org/).
* Does not dictate logging, monitoring, or alerting solutions. It provides some integrations as proof of concept, and mechanisms to collect and export metrics.
* Does not provide nor mandate a configuration language/system (for example, Jsonnet). It provides a declarative API that may be targeted by arbitrary forms of declarative specifications.
* Does not provide nor adopt any comprehensive machine configuration, maintenance, management, or self-healing systems.
* Additionally, Kubernetes is not a mere orchestration system. In fact, it eliminates the need for orchestration. The technical definition of orchestration is execution of a defined workflow: first do A, then B, then C. In contrast, Kubernetes comprises a set of independent, composable control processes that continuously drive the current state towards the provided desired state. It shouldn't matter how you get from A to C. Centralized control is also not required. This results in a system that is easier to use and more powerful, robust, resilient, and extensible.

## Historical context for Kubernetes[](https://kubernetes.io/docs/concepts/overview/#going-back-in-time)

Let's take a look at why Kubernetes is so useful by going back in time.

![Deployment evolution](https://kubernetes.io/images/docs/Container_Evolution.svg)

Traditional deployment era:

Early on, organizations ran applications on physical servers. There was no way to define resource boundaries for applications in a physical server, and this caused resource allocation issues. For example, if multiple applications run on a physical server, there can be instances where one application would take up most of the resources, and as a result, the other applications would underperform. A solution for this would be to run each application on a different physical server. But this did not scale as resources were underutilized, and it was expensive for organizations to maintain many physical servers.

Virtualized deployment era:

As a solution, virtualization was introduced. It allows you to run multiple Virtual Machines (VMs) on a single physical server's CPU. Virtualization allows applications to be isolated between VMs and provides a level of security as the information of one application cannot be freely accessed by another application.

Virtualization allows better utilization of resources in a physical server and allows better scalability because an application can be added or updated easily, reduces hardware costs, and much more. With virtualization you can present a set of physical resources as a cluster of disposable virtual machines.

Each VM is a full machine running all the components, including its own operating system, on top of the virtualized hardware.

Container deployment era:

Containers are similar to VMs, but they have relaxed isolation properties to share the Operating System (OS) among the applications. Therefore, containers are considered lightweight. Similar to a VM, a container has its own filesystem, share of CPU, memory, process space, and more. As they are decoupled from the underlying infrastructure, they are portable across clouds and OS distributions.

Containers have become popular because they provide extra benefits, such as:
* Agile application creation and deployment: increased ease and efficiency of container image creation compared to VM image use.
* Continuous development, integration, and deployment: provides reliable and frequent container image build and deployment with quick and efficient rollbacks (due to image immutability).
* Dev and Ops separation of concerns: create application container images at build/release time rather than deployment time, thereby decoupling applications from infrastructure.
* Observability: not only surfaces OS-level information and metrics, but also application health and other signals.
* Environmental consistency across development, testing, and production: runs the same on a laptop as it does in the cloud.
* Cloud and OS distribution portability: runs on Ubuntu, RHEL, CoreOS, on-premises, on major public clouds, and anywhere else.
* Application-centric management: raises the level of abstraction from running an OS on virtual hardware to running an application on an OS using logical resources.
* Loosely coupled, distributed, elastic, liberated micro-services: applications are broken into smaller, independent pieces and can be deployed and managed dynamically – not a monolithic stack running on one big single-purpose machine.
* Resource isolation: predictable application performance.
* Resource utilization: high efficiency and density.

## What's next[](https://kubernetes.io/docs/concepts/overview/#what-s-next)
* Take a look at the [Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/)
* Take a look at the [Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/)
* Take a look at [kubectl](https://kubernetes.io/docs/concepts/overview/kubectl/): the primary CLI for Kubernetes
* Take a look at the [Cluster Architecture](https://kubernetes.io/docs/concepts/architecture/)
* Ready to [Get Started](https://kubernetes.io/docs/setup/)?

## Feedback

Was this page helpful?Yes No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes). Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to [report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io) or [suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).

---



# Source: https://kubernetes.io/docs/concepts/overview/components/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Overview](https://kubernetes.io/docs/concepts/overview/)
4. Kubernetes Components

# Kubernetes ComponentsAn overview of the key components that make up a Kubernetes cluster.

This page provides a high-level overview of the essential components that make up a Kubernetes cluster.

![Components of Kubernetes](https://kubernetes.io/images/docs/components-of-kubernetes.svg)

The components of a Kubernetes cluster

## Core Components[](https://kubernetes.io/docs/concepts/overview/components/#core-components)

A Kubernetes cluster consists of a control plane and one or more worker nodes. Here's a brief overview of the main components:

### Control Plane Components[](https://kubernetes.io/docs/concepts/overview/components/#control-plane-components)

Manage the overall state of the cluster:[kube-apiserver](https://kubernetes.io/docs/concepts/architecture/#kube-apiserver)The core component server that exposes the Kubernetes HTTP API.[etcd](https://kubernetes.io/docs/concepts/architecture/#etcd)Consistent and highly-available key value store for all API server data.[kube-scheduler](https://kubernetes.io/docs/concepts/architecture/#kube-scheduler)Looks for Pods not yet bound to a node, and assigns each Pod to a suitable node.[kube-controller-manager](https://kubernetes.io/docs/concepts/architecture/#kube-controller-manager)Runs [controllers](https://kubernetes.io/docs/concepts/architecture/controller/) to implement Kubernetes API behavior.[cloud-controller-manager](https://kubernetes.io/docs/concepts/architecture/#cloud-controller-manager) (optional)Integrates with underlying cloud provider(s).

### Node Components[](https://kubernetes.io/docs/concepts/overview/components/#node-components)

Run on every node, maintaining running pods and providing the Kubernetes runtime environment:[kubelet](https://kubernetes.io/docs/concepts/architecture/#kubelet)Ensures that Pods are running, including their containers.[kube-proxy](https://kubernetes.io/docs/concepts/architecture/#kube-proxy) (optional)Maintains network rules on nodes to implement [Services](https://kubernetes.io/docs/concepts/services-networking/service/).[Container runtime](https://kubernetes.io/docs/concepts/architecture/#container-runtime)Software responsible for running containers. Read [Container Runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/) to learn more.🛇 This item links to a third party project or product that is not part of Kubernetes itself. [More information](https://kubernetes.io/docs/concepts/overview/components/#third-party-content-disclaimer)

Your cluster may require additional software on each node; for example, you might also run [systemd](https://systemd.io/) on a Linux node to supervise local components.

## Addons[](https://kubernetes.io/docs/concepts/overview/components/#addons)

Addons extend the functionality of Kubernetes. A few important examples include:[DNS](https://kubernetes.io/docs/concepts/architecture/#dns)For cluster-wide DNS resolution.[Web UI](https://kubernetes.io/docs/concepts/architecture/#web-ui-dashboard) (Dashboard)For cluster management via a web interface.[Container Resource Monitoring](https://kubernetes.io/docs/concepts/architecture/#container-resource-monitoring)For collecting and storing container metrics.[Cluster-level Logging](https://kubernetes.io/docs/concepts/architecture/#cluster-level-logging)For saving container logs to a central log store.

## Flexibility in Architecture[](https://kubernetes.io/docs/concepts/overview/components/#flexibility-in-architecture)

Kubernetes allows for flexibility in how these components are deployed and managed. The architecture can be adapted to various needs, from small development environments to large-scale production deployments.

For more detailed information about each component and various ways to configure your cluster architecture, see the [Cluster Architecture](https://kubernetes.io/docs/concepts/architecture/) page.

## Feedback

Was this page helpful?Yes No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes). Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to [report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io) or [suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).

---



# Source: https://kubernetes.io/docs/concepts/overview/working-with-objects/

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



# Source: https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Overview](https://kubernetes.io/docs/concepts/overview/)
4. [Objects In Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/)
5. Kubernetes Object Management

# Kubernetes Object Management

The `kubectl` command-line tool supports several different ways to create and manage Kubernetes [objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects). This document provides an overview of the different approaches. Read the [Kubectl book](https://kubectl.docs.kubernetes.io) for details of managing objects by Kubectl.

## Management techniques[](https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/#management-techniques)

#### Warning:A Kubernetes object should be managed using only one technique. Mixing and matching techniques for the same object results in undefined behavior.

| Management technique | Operates on | Recommended environment | Supported writers | Learning curve || --- | --- | --- | --- | --- || Imperative commands | Live objects | Development projects | 1+ | Lowest || Imperative object configuration | Individual files | Production projects | 1 | Moderate || Declarative object configuration | Directories of files | Production projects | 1+ | Highest |

## Imperative commands[](https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/#imperative-commands)

When using imperative commands, a user operates directly on live objects in a cluster. The user provides operations to the `kubectl` command as arguments or flags.

This is the recommended way to get started or to run a one-off task in a cluster. Because this technique operates directly on live objects, it provides no history of previous configurations.

### Examples[](https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/#examples)

Run an instance of the nginx container by creating a Deployment object:
```yaml
kubectl create deployment nginx --image nginx
```

### Trade-offs[](https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/#trade-offs)

Advantages compared to object configuration:
* Commands are expressed as a single action word.
* Commands require only a single step to make changes to the cluster.

Disadvantages compared to object configuration:
* Commands do not integrate with change review processes.
* Commands do not provide an audit trail associated with changes.
* Commands do not provide a source of records except for what is live.
* Commands do not provide a template for creating new objects.

## Imperative object configuration[](https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/#imperative-object-configuration)

In imperative object configuration, the kubectl command specifies the operation (create, replace, etc.), optional flags and at least one file name. The file specified must contain a full definition of the object in YAML or JSON format.

See the [API reference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.36/) for more details on object definitions.

#### Warning:The imperative `replace` command replaces the existing spec with the newly provided one, dropping all changes to the object missing from the configuration file. This approach should not be used with resource types whose specs are updated independently of the configuration file. Services of type `LoadBalancer`, for example, have their `externalIPs` field updated independently from the configuration by the cluster.

---



# Source: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/

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



# Source: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Overview](https://kubernetes.io/docs/concepts/overview/)
4. [Objects In Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/)
5. Labels and Selectors

# Labels and Selectors

Labels are key/value pairs that are attached to [objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects) such as Pods. Labels are intended to be used to specify identifying attributes of objects that are meaningful and relevant to users, but do not directly imply semantics to the core system. Labels can be used to organize and to select subsets of objects. Labels can be attached to objects at creation time and subsequently added and modified at any time. Each object can have a set of key/value labels defined. Each Key must be unique for a given object.
```yaml
"metadata": {
  "labels": {
    "key1" : "value1",
    "key2" : "value2"
  }
}
```

Labels allow for efficient queries and watches and are ideal for use in UIs and CLIs. Non-identifying information should be recorded using [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).

## Motivation[](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#motivation)

Labels enable users to map their own organizational structures onto system objects in a loosely coupled fashion, without requiring clients to store these mappings.

Service deployments and batch processing pipelines are often multi-dimensional entities (e.g., multiple partitions or deployments, multiple release tracks, multiple tiers, multiple micro-services per tier). Management often requires cross-cutting operations, which breaks encapsulation of strictly hierarchical representations, especially rigid hierarchies determined by the infrastructure rather than by users.

Example labels:
* `"release" : "stable"`, `"release" : "canary"`
* `"environment" : "dev"`, `"environment" : "qa"`, `"environment" : "production"`
* `"tier" : "frontend"`, `"tier" : "backend"`, `"tier" : "cache"`
* `"partition" : "customerA"`, `"partition" : "customerB"`
* `"track" : "daily"`, `"track" : "weekly"`

These are examples of [commonly used labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/); you are free to develop your own conventions. Keep in mind that label Key must be unique for a given object.

## Syntax and character set[](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set)

Labels are key/value pairs. Valid label keys have two segments: an optional prefix and name, separated by a slash (`/`). The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (`.`), not longer than 253 characters in total, followed by a slash (`/`).

If the prefix is omitted, the label Key is presumed to be private to the user. Automated system components (e.g. `kube-scheduler`, `kube-controller-manager`, `kube-apiserver`, `kubectl`, or other third-party automation) which add labels to end-user objects must specify a prefix.

The `kubernetes.io/` and `k8s.io/` prefixes are [reserved](https://kubernetes.io/docs/reference/labels-annotations-taints/) for Kubernetes core components.

Valid label value:
* must be 63 characters or less (can be empty),
* unless empty, must begin and end with an alphanumeric character (`[a-z0-9A-Z]`),
* could contain dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between.

For example, here's a manifest for a Pod that has two labels `environment: production` and `app: nginx`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: label-demo
  labels:
    environment: production
    app: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
```

## Label selectors[](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors)

Unlike [names and UIDs](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/), labels do not provide uniqueness. In general, we expect many objects to carry the same label(s).

Via a label selector, the client/user can identify a set of objects. The label selector is the core grouping primitive in Kubernetes.

The API currently supports two types of selectors: equality-based and set-based. A label selector can be made of multiple requirements which are comma-separated. In the case of multiple requirements, all must be satisfied so the comma separator acts as a logical AND (`&&`) operator.

The semantics of empty or non-specified selectors are dependent on the context, and API types that use selectors should document the validity and meaning of them.

#### Note:For some API types, such as ReplicaSets, the label selectors of two instances must not overlap within a namespace, or the controller can see that as conflicting instructions and fail to determine how many replicas should be present.

---



# Source: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Overview](https://kubernetes.io/docs/concepts/overview/)
4. [Objects In Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/)
5. Namespaces

# Namespaces

In Kubernetes, namespaces provide a mechanism for isolating groups of resources within a single cluster. Names of resources need to be unique within a namespace, but not across namespaces. Namespace-based scoping is applicable only for namespaced [objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects) (e.g. Deployments, Services, etc.) and not for cluster-wide objects (e.g. StorageClass, Nodes, PersistentVolumes, etc.).

## When to Use Multiple Namespaces[](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/#when-to-use-multiple-namespaces)

Namespaces are intended for use in environments with many users spread across multiple teams, or projects. For clusters with a few to tens of users, you should not need to create or think about namespaces at all. Start using namespaces when you need the features they provide.

Namespaces provide a scope for names. Names of resources need to be unique within a namespace, but not across namespaces. Namespaces cannot be nested inside one another and each Kubernetes resource can only be in one namespace.

Namespaces are a way to divide cluster resources between multiple users (via [resource quota](https://kubernetes.io/docs/concepts/policy/resource-quotas/)).

It is not necessary to use multiple namespaces to separate slightly different resources, such as different versions of the same software: use [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels) to distinguish resources within the same namespace.

#### Note:For a production cluster, consider not using the `default` namespace. Instead, make other namespaces and use those.

## Initial namespaces[](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/#initial-namespaces)

Kubernetes starts with four initial namespaces:`default`Kubernetes includes this namespace so that you can start using your new cluster without first creating a namespace.`kube-node-lease`This namespace holds [Lease](https://kubernetes.io/docs/concepts/architecture/leases/) objects associated with each node. Node leases allow the kubelet to send [heartbeats](https://kubernetes.io/docs/concepts/architecture/nodes/#node-heartbeats) so that the control plane can detect node failure.`kube-public`This namespace is readable by all clients (including those not authenticated). This namespace is mostly reserved for cluster usage, in case that some resources should be visible and readable publicly throughout the whole cluster. The public aspect of this namespace is only a convention, not a requirement.`kube-system`The namespace for objects created by the Kubernetes system.

## Working with Namespaces[](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/#working-with-namespaces)

Creation and deletion of namespaces are described in the [Admin Guide documentation for namespaces](https://kubernetes.io/docs/tasks/administer-cluster/namespaces/).

#### Note:Avoid creating namespaces with the prefix `kube-`, since it is reserved for Kubernetes system namespaces.

### Viewing namespaces[](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/#viewing-namespaces)

You can list the current namespaces in a cluster using:
```yaml
kubectl get namespace
```

---



# Source: https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Overview](https://kubernetes.io/docs/concepts/overview/)
4. [Objects In Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/)
5. Annotations

# Annotations

You can use Kubernetes annotations to attach arbitrary non-identifying metadata to [objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects). Clients such as tools and libraries can retrieve this metadata.

## Attaching metadata to objects[](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/#attaching-metadata-to-objects)

You can use either labels or annotations to attach metadata to Kubernetes objects. Labels can be used to select objects and to find collections of objects that satisfy certain conditions. In contrast, annotations are not used to identify and select objects. The metadata in an annotation can be small or large, structured or unstructured, and can include characters not permitted by labels. It is possible to use labels as well as annotations in the metadata of the same object.

Annotations, like labels, are key/value maps:
```yaml
"metadata": {
  "annotations": {
    "key1" : "value1",
    "key2" : "value2"
  }
}
```

#### Note:The keys and the values in the map must be strings. In other words, you cannot use numeric, boolean, list or other types for either the keys or the values.

Here are some examples of information that could be recorded in annotations:
* 

Fields managed by a declarative configuration layer. Attaching these fields as annotations distinguishes them from default values set by clients or servers, and from auto-generated fields and fields set by auto-sizing or auto-scaling systems.
* 

Build, release, or image information like timestamps, release IDs, git branch, PR numbers, image hashes, and registry address.
* 

Pointers to logging, monitoring, analytics, or audit repositories.
* 

Client library or tool information that can be used for debugging purposes: for example, name, version, and build information.
* 

User or tool/system provenance information, such as URLs of related objects from other ecosystem components.
* 

Lightweight rollout tool metadata: for example, config or checkpoints.
* 

Phone or pager numbers of persons responsible, or directory entries that specify where that information can be found, such as a team web site.
* 

Directives from the end-user to the implementations to modify behavior or engage non-standard features.

Instead of using annotations, you could store this type of information in an external database or directory, but that would make it much harder to produce shared client libraries and tools for deployment, management, introspection, and the like.

## Syntax and character set[](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/#syntax-and-character-set)

Annotations are key/value pairs. Valid annotation keys have two segments: an optional prefix and name, separated by a slash (`/`). The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (`.`), not longer than 253 characters in total, followed by a slash (`/`).

If the prefix is omitted, the annotation Key is presumed to be private to the user. Automated system components (e.g. `kube-scheduler`, `kube-controller-manager`, `kube-apiserver`, `kubectl`, or other third-party automation) which add annotations to end-user objects must specify a prefix.

The `kubernetes.io/` and `k8s.io/` prefixes are reserved for Kubernetes core components.

For example, here's a manifest for a Pod that has the annotation `imageregistry: https://hub.docker.com/` :
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: annotations-demo
  annotations:
    imageregistry: "https://hub.docker.com/"
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
```

---



# Source: https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/

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



# Source: https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Overview](https://kubernetes.io/docs/concepts/overview/)
4. [Objects In Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/)
5. Finalizers

# Finalizers

Finalizers are namespaced keys that tell Kubernetes to wait until specific conditions are met before it fully deletes [resources](https://kubernetes.io/docs/reference/using-api/api-concepts/#standard-api-terminology) that are marked for deletion. Finalizers alert [controllers](https://kubernetes.io/docs/concepts/architecture/controller/) to clean up resources the deleted object owned.

When you tell Kubernetes to delete an object that has finalizers specified for it, the Kubernetes API marks the object for deletion by populating `.metadata.deletionTimestamp`, and returns a `202` status code (HTTP "Accepted"). The target object remains in a terminating state while the control plane, or other components, take the actions defined by the finalizers. After these actions are complete, the controller removes the relevant finalizers from the target object. When the `metadata.finalizers` field is empty, Kubernetes considers the deletion complete and deletes the object.

You can use finalizers to control [garbage collection](https://kubernetes.io/docs/concepts/architecture/garbage-collection/) of resources. For example, you can define a finalizer to clean up related [API resources](https://kubernetes.io/docs/reference/using-api/api-concepts/#standard-api-terminology) or infrastructure before the controller deletes the object being finalized.

You can use finalizers to control [garbage collection](https://kubernetes.io/docs/concepts/architecture/garbage-collection/) of [objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects) by alerting [controllers](https://kubernetes.io/docs/concepts/architecture/controller/) to perform specific cleanup tasks before deleting the target resource.

Finalizers don't usually specify the code to execute. Instead, they are typically lists of keys on a specific resource similar to annotations. Kubernetes specifies some finalizers automatically, but you can also specify your own.

## How finalizers work[](https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/#how-finalizers-work)

When you create a resource using a manifest file, you can specify finalizers in the `metadata.finalizers` field. When you attempt to delete the resource, the API server handling the delete request notices the values in the `finalizers` field and does the following:
* Modifies the object to add a `metadata.deletionTimestamp` field with the time you started the deletion.
* Prevents the object from being removed until all items are removed from its `metadata.finalizers` field
* Returns a `202` status code (HTTP "Accepted")

The controller managing that finalizer notices the update to the object setting the `metadata.deletionTimestamp`, indicating deletion of the object has been requested. The controller then attempts to satisfy the requirements of the finalizers specified for that resource. Each time a finalizer condition is satisfied, the controller removes that key from the resource's `finalizers` field. When the `finalizers` field is emptied, an object with a `deletionTimestamp` field set is automatically deleted. You can also use finalizers to prevent deletion of unmanaged resources.

A common example of a finalizer is `kubernetes.io/pv-protection`, which prevents accidental deletion of `PersistentVolume` objects. When a `PersistentVolume` object is in use by a Pod, Kubernetes adds the `pv-protection` finalizer. If you try to delete the `PersistentVolume`, it enters a `Terminating` status, but the controller can't delete it because the finalizer exists. When the Pod stops using the `PersistentVolume`, Kubernetes clears the `pv-protection` finalizer, and the controller deletes the volume.

#### Note:
* 

When you `DELETE` an object, Kubernetes adds the deletion timestamp for that object and then immediately starts to restrict changes to the `.metadata.finalizers` field for the object that is now pending deletion. You can remove existing finalizers (deleting an entry from the `finalizers` list) but you cannot add a new finalizer. You also cannot modify the `deletionTimestamp` for an object once it is set.
* 

After the deletion is requested, you can not resurrect this object. The only way is to delete it and make a new similar object.

#### Note:Custom finalizer names must be publicly qualified finalizer names, such as `example.com/finalizer-name`. Kubernetes enforces this format; the API server rejects writes to objects where the change does not use qualified finalizer names for any custom finalizer.

## Owner references, labels, and finalizers[](https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/#owners-labels-finalizers)

Like [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels), [owner references](https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/) describe the relationships between objects in Kubernetes, but are used for a different purpose. When a [controller](https://kubernetes.io/docs/concepts/architecture/controller/) manages objects like Pods, it uses labels to track changes to groups of related objects. For example, when a [Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/) creates one or more Pods, the Job controller applies labels to those pods and tracks changes to any Pods in the cluster with the same label.

The Job controller also adds owner references to those Pods, pointing at the Job that created the Pods. If you delete the Job while these Pods are running, Kubernetes uses the owner references (not labels) to determine which Pods in the cluster need cleanup.

Kubernetes also processes finalizers when it identifies owner references on a resource targeted for deletion.

In some situations, finalizers can block the deletion of dependent objects, which can cause the targeted owner object to remain for longer than expected without being fully deleted. In these situations, you should check finalizers and owner references on the target owner and dependent objects to troubleshoot the cause.

#### Note:In cases where objects are stuck in a deleting state, avoid manually removing finalizers to allow deletion to continue. Finalizers are usually added to resources for a reason, so forcefully removing them can lead to issues in your cluster. This should only be done when the purpose of the finalizer is understood and is accomplished in another way (for example, manually cleaning up some dependent object).

---



# Source: https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Overview](https://kubernetes.io/docs/concepts/overview/)
4. [Objects In Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/)
5. Owners and Dependents

# Owners and Dependents

In Kubernetes, some [objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects) are owners of other objects. For example, a [ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/) is the owner of a set of Pods. These owned objects are dependents of their owner.

Ownership is different from the [labels and selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) mechanism that some resources also use. For example, consider a Service that creates `EndpointSlice` objects. The Service uses [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels) to allow the control plane to determine which `EndpointSlice` objects are used for that Service. In addition to the labels, each `EndpointSlice` that is managed on behalf of a Service has an owner reference. Owner references help different parts of Kubernetes avoid interfering with objects they don’t control.

## Owner references in object specifications[](https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/#owner-references-in-object-specifications)

Dependent objects have a `metadata.ownerReferences` field that references their owner object. A valid owner reference consists of the object name and a [UID](https://kubernetes.io/docs/concepts/overview/working-with-objects/names) within the same [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces) as the dependent object. Kubernetes sets the value of this field automatically for objects that are dependents of other objects like ReplicaSets, DaemonSets, Deployments, Jobs and CronJobs, and ReplicationControllers. You can also configure these relationships manually by changing the value of this field. However, you usually don't need to and can allow Kubernetes to automatically manage the relationships.

Dependent objects also have an `ownerReferences.blockOwnerDeletion` field that takes a boolean value and controls whether specific dependents can block garbage collection from deleting their owner object. Kubernetes automatically sets this field to `true` if a [controller](https://kubernetes.io/docs/concepts/architecture/controller/) (for example, the Deployment controller) sets the value of the `metadata.ownerReferences` field. You can also set the value of the `blockOwnerDeletion` field manually to control which dependents block garbage collection.

A Kubernetes admission controller controls user access to change this field for dependent resources, based on the delete permissions of the owner. This control prevents unauthorized users from delaying owner object deletion.

#### Note:

Cross-namespace owner references are disallowed by design. Namespaced dependents can specify cluster-scoped or namespaced owners. A namespaced owner must exist in the same namespace as the dependent. If it does not, the owner reference is treated as absent, and the dependent is subject to deletion once all owners are verified absent.

Cluster-scoped dependents can only specify cluster-scoped owners. In v1.20+, if a cluster-scoped dependent specifies a namespaced kind as an owner, it is treated as having an unresolvable owner reference, and is not able to be garbage collected.

In v1.20+, if the garbage collector detects an invalid cross-namespace `ownerReference`, or a cluster-scoped dependent with an `ownerReference` referencing a namespaced kind, a warning Event with a reason of `OwnerRefInvalidNamespace` and an `involvedObject` of the invalid dependent is reported. You can check for that kind of Event by running `kubectl get events -A --field-selector=reason=OwnerRefInvalidNamespace`.

## Ownership and finalizers[](https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/#ownership-and-finalizers)

When you tell Kubernetes to delete a resource, the API server allows the managing controller to process any [finalizer rules](https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/) for the resource. [Finalizers](https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/) prevent accidental deletion of resources your cluster may still need to function correctly. For example, if you try to delete a [PersistentVolume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) that is still in use by a Pod, the deletion does not happen immediately because the `PersistentVolume` has the `kubernetes.io/pv-protection` finalizer on it. Instead, the [volume](https://kubernetes.io/docs/concepts/storage/volumes/) remains in the `Terminating` status until Kubernetes clears the finalizer, which only happens after the `PersistentVolume` is no longer bound to a Pod.

Kubernetes also adds finalizers to an owner resource when you use either [foreground or orphan cascading deletion](https://kubernetes.io/docs/concepts/architecture/garbage-collection/#cascading-deletion). In foreground deletion, it adds the `foreground` finalizer so that the controller must delete dependent resources that also have `ownerReferences.blockOwnerDeletion=true` before it deletes the owner. If you specify an orphan deletion policy, Kubernetes adds the `orphan` finalizer so that the controller ignores dependent resources after it deletes the owner object.

## What's next[](https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/#what-s-next)
* Learn more about [Kubernetes finalizers](https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/).
* Learn about [garbage collection](https://kubernetes.io/docs/concepts/architecture/garbage-collection/).
* Read the API reference for [object metadata](https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/#System).

## Feedback

Was this page helpful?Yes No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes). Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to [report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io) or [suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).const yes=document.querySelector(".feedback--yes"),no=document.querySelector(".feedback--no");document.querySelectorAll(".feedback--link").forEach(e=>{e.href=e.href+window.location.pathname});const sendFeedback=e=>{typeof gtag=="function"?gtag("event","page_helpful",{event_category:"Helpful",event_label:window.location.pathname,value:e}):console.log("gtag not available; skipping analytics event")},disableButtons=()=>{yes.disabled=!0,yes.classList.add("feedback--button__disabled"),no.disabled=!0,no.classList.add("feedback--button__disabled")};yes.addEventListener("click",()=>{sendFeedback(100),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")}),no.addEventListener("click",()=>{sendFeedback(0),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")})Last modified January 08, 2022 at 6:09 PM PST: [Reorganize Working with Kubernetes Objects section (634c17f61c)](https://github.com/kubernetes/website/commit/634c17f61cb92f40eb0e2122f44f0a5e5242b93e)

---



# Source: https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Overview](https://kubernetes.io/docs/concepts/overview/)
4. [Objects In Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/)
5. Recommended Labels

# Recommended Labels

You can visualize and manage Kubernetes objects with more tools than kubectl and the dashboard. A common set of labels allows tools to work interoperably, describing objects in a common manner that all tools can understand.

In addition to supporting tooling, the recommended labels describe applications in a way that can be queried.

The metadata is organized around the concept of an application. Kubernetes is not a platform as a service (PaaS) and doesn't have or enforce a formal notion of an application. Instead, applications are informal and described with metadata. The definition of what an application contains is loose.

#### Note:These are recommended labels. They make it easier to manage applications but aren't required for any core tooling.

Shared labels and annotations share a common prefix: `app.kubernetes.io`. Labels without a prefix are private to users. The shared prefix ensures that shared labels do not interfere with custom user labels.

## Labels[](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/#labels)

In order to take full advantage of using these labels, they should be applied on every resource object.``````````[](https://semver.org/spec/v1.0.0.html)``````````````

| Key | Description | Example | Type || --- | --- | --- | --- || app.kubernetes.io/name | The name of the application | mysql | string || app.kubernetes.io/instance | A unique name identifying the instance of an application | mysql-abcxyz | string || app.kubernetes.io/version | The current version of the application (e.g., a SemVer 1.0, revision hash, etc.) | 5.7.21 | string || app.kubernetes.io/component | The component within the architecture | database | string || app.kubernetes.io/part-of | The name of a higher level application this one is part of | wordpress | string || app.kubernetes.io/managed-by | The tool being used to manage the operation of an application | Helm | string |

To illustrate these labels in action, consider the following [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) object:
```yaml
# This is an excerpt
apiVersion: apps/v1
kind: StatefulSet
metadata:
  labels:
    app.kubernetes.io/name: mysql
    app.kubernetes.io/instance: mysql-abcxyz
    app.kubernetes.io/version: "5.7.21"
    app.kubernetes.io/component: database
    app.kubernetes.io/part-of: wordpress
    app.kubernetes.io/managed-by: Helm
```

## Applications And Instances Of Applications[](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/#applications-and-instances-of-applications)

An application can be installed one or more times into a Kubernetes cluster and, in some cases, the same namespace. For example, WordPress can be installed more than once where different websites are different installations of WordPress.

The name of an application and the instance name are recorded separately. For example, WordPress has a `app.kubernetes.io/name` of `wordpress` while it has an instance name, represented as `app.kubernetes.io/instance` with a value of `wordpress-abcxyz`. This enables the application and instance of the application to be identifiable. Every instance of an application must have a unique name.

## Examples[](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/#examples)

To illustrate different ways to use these labels the following examples have varying complexity.

### A Simple Stateless Service[](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/#a-simple-stateless-service)

Consider the case for a simple stateless service deployed using `Deployment` and `Service` objects. The following two snippets represent how the labels could be used in their simplest form.

The `Deployment` is used to oversee the pods running the application itself.
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app.kubernetes.io/name: myservice
    app.kubernetes.io/instance: myservice-abcxyz
...
```

---



# Source: https://kubernetes.io/docs/concepts/overview/working-with-objects/storage-version/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Overview](https://kubernetes.io/docs/concepts/overview/)
4. [Objects In Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/)
5. Storage Versions

# Storage Versions

The Kubernetes API server stores objects, relying on an etcd-compatible backing store (often, the backing storage is etcd itself). Each object is serialized using a particular version of that API type; for example, the v1 representation of a ConfigMap. Kubernetes uses the term storage version to describe how an object is stored in your cluster.

The Kubernetes API also relies on automatic conversion; for example, if you have a HorizontalPodAutoscaler, then you can interact with that HorizontalPodAutoscaler using any mix of the v1 and v2 versions of the HorizontalPodAutoscaler API. Kubernetes is responsible for converting each API call so that clients do not see what version is actually serialized.

For cluster administrators, object storage version is an important concept to understand since it is what links the API representation of the object to the actual encoding in the storage backend. This can be important for when the underlying binary encodings of the object matter, such as for encryption at rest, or API deprecation.

The same API may have multiple storage versions that the API Server can then convert to an object schema. A single object that is part of that resource must only have one storage version at any time. This means that the API Server is aware of the binary encodings of the objects and is able to convert between all the stored versions to the API Representation of the object dynamically.

The version of an object is separate from the storage version entirely. For example, a `v1alpha1` and `v1beta1` API Object for the same Resource will be encoded the same in storage as long as the storage version has not been updated between the two objects.

## Storage version to resource mapping[](https://kubernetes.io/docs/concepts/overview/working-with-objects/storage-version/#storage-version-to-resource-mapping)

Every resource will have 1 active storage version at any point in time, meaning that any write to an object will store the object at that storage version. The storage version can be updated however, making it so that objects can be stored at differing versions. One object will only be stored at one storage version at any time.

Reads from the API Server will convert the stored data to the API representation of the object. This makes it so that old storage versions can sit indefinitely as long as no updates occur to the object. Writes, on the other hand, will convert the stored object to the new representation upon update.

## Storage versions for custom resources[](https://kubernetes.io/docs/concepts/overview/working-with-objects/storage-version/#CustomResourceDefinition-storage-version)

[Custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#storage) are defined dynamically, and as such differ from built in Kubernetes types with their storage version. Builtin objects generally have their storage encoding defined separately from their API types, where the stored object acts as a hub and the specific version of the resource does not matter apart from being a field in the object schema.

However, for custom resources, a certain version of the resource must be set as the storage version. The schema defined by that specific version of the custom resource will be used as the encoding of the resource in the storage layer. See the [advanced CRD featureset](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#advanced-features-and-flexibility) for more detailed information on the API setup and versioning.

For example see this CustomResourceDefinition for crontabs:
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: crontabs.example.com
spec:
  group: example.com
  # list of versions supported by this CustomResourceDefinition
  versions:
  - name: v1beta1
    # Each version can be enabled/disabled by Served flag.
    served: true
    # One and only one version must be marked as the storage version.
    storage: true
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
          time:
            type: string
  conversion:
    strategy: None
  scope: Namespaced
  names:
    plural: crontabs
    singular: crontab
    kind: CronTab
    shortNames:
    - ct
```

The `v1beta1` API definition is used as the storage version, meaning that any updates or creation of `crontabs` will be stored with the object schema of the `v1beta1` api. In this case it actually would mean that the `v1` API object would never be able to store the `time` field since it is not part of the storage definition. This schema is used in the storage layer as the binary encoding of the object itself. Trying to set two versions as the stored version at the same time is considered invalid, since that would mean that two data schemes would be considered valid ways to store the objects at the same time.

Upon modification of the version that is used for storage, that version of the API will be used to store any new or update CRs. Watching or getting the object will have the object be in use but will just convert the object from the old storage version and not affect the object. Only updating or creating will have an effect and use the newly defined storage version.

## How storage versions are relevant to encryption at rest[](https://kubernetes.io/docs/concepts/overview/working-with-objects/storage-version/#how-storage-versions-are-relevant-to-encryption-at-rest)

There are tools to [encrypt the at rest storage](https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/) of a cluster, especially for cluster secrets. This adds an additional layer of protection for data exfiltration since the actual stored data in the cluster is encrypted. This means that the API Server is actually decrypting the data as it retrieves them from storage. The APIServer must have the key for that storage version in order to decode the object properly.

The storage version in this case is more than just the binary encoding of the object. As long as what is stored can be somehow converted into the API object, it can be used as a storage version.

## Migrating to a different storage version[](https://kubernetes.io/docs/concepts/overview/working-with-objects/storage-version/#migrating-to-a-different-storage-version)

Multiple storage versions for a single resource can pose problems for cluster administrators. A cluster administrator may not remove old versions of an API for CRDs which may be unsupported until they are sure that all objects are no longer using the storage version associated with it. With a large number of objects and an opaque view into which ones are new and which ones still are backed by old storage versions, it makes it difficult to tell when a version can be safely removed. If a version is removed prematurely, it can mean being unable to read the object entirely.

Another important issue is the use of encryption keys as defined in the section above. Since a resource must be actively in use to update the storage version, when a key rotation is done, both the old encryption key and the new encryption key must remain in use until the administrator is sure all objects have been written to at least once. This poses both security risks and usability issues, since a key cannot be fully removed from use until then.

See [storage version migration](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/storage-version-migration/) on examples of how to run a migration to ensure that all objects are using a newer storage version without manual intervention.

## Feedback

Was this page helpful?Yes No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes). Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to [report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io) or [suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).const yes=document.querySelector(".feedback--yes"),no=document.querySelector(".feedback--no");document.querySelectorAll(".feedback--link").forEach(e=>{e.href=e.href+window.location.pathname});const sendFeedback=e=>{typeof gtag=="function"?gtag("event","page_helpful",{event_category:"Helpful",event_label:window.location.pathname,value:e}):console.log("gtag not available; skipping analytics event")},disableButtons=()=>{yes.disabled=!0,yes.classList.add("feedback--button__disabled"),no.disabled=!0,no.classList.add("feedback--button__disabled")};yes.addEventListener("click",()=>{sendFeedback(100),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")}),no.addEventListener("click",()=>{sendFeedback(0),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")})Last modified April 05, 2026 at 2:45 PM PST: [Fix typos in docs: limtations, storege, Althought (89a9a2d607)](https://github.com/kubernetes/website/commit/89a9a2d6077234fcde8874abf865048c7722dff0)

---



# Source: https://kubernetes.io/docs/concepts/overview/kubernetes-api/

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



# Source: https://kubernetes.io/docs/concepts/overview/kubectl/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Overview](https://kubernetes.io/docs/concepts/overview/)
4. The kubectl command-line tool

# The kubectl command-line toolkubectl is the primary command-line tool for communicating with a Kubernetes cluster. This page provides an overview of kubectl and its role in the Kubernetes ecosystem.

Kubernetes provides a command line tool for communicating with a Kubernetes cluster's [control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane), using the Kubernetes API.

The `kubectl` tool communicates with your cluster through the [Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/). For configuration, `kubectl` looks for a file named `config` in the `$HOME/.kube` directory. You can specify other [kubeconfig](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/) files by setting the `KUBECONFIG` environment variable or by setting the [`--kubeconfig`](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/) flag.

## Role of kubectl[](https://kubernetes.io/docs/concepts/overview/kubectl/#role-of-kubectl)

The `kubectl` tool is the primary interface for creating, inspecting, updating, and deleting Kubernetes objects. It complements the [Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/) that run inside your cluster and the [Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/) that those components implement. Whether you run `kubectl` from your laptop or from a Pod inside the cluster, it sends requests to the API server. Other clients, such as [client libraries](https://kubernetes.io/docs/reference/using-api/client-libraries/) and web dashboards like [Headlamp](https://headlamp.dev/), also communicate through the same API.

## How kubectl works[](https://kubernetes.io/docs/concepts/overview/kubectl/#how-kubectl-works)

The `kubectl` tool connects to the API server and authenticates using the cluster, user, and context defined in your [kubeconfig](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/) file. When you run `kubectl` from outside a cluster, it uses the kubeconfig file to find the API server address and credentials. When `kubectl` runs inside a Pod (for example, in a CI/CD pipeline), it can use in-cluster authentication based on the ServiceAccount token mounted in the Pod.

When you run a command, `kubectl` translates your intent into one or more HTTP requests to the [Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/). The API server validates each request, applies it to the cluster state stored in [etcd](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/), and returns the result. This means every `kubectl` action, whether creating a Deployment or reading logs, follows the same API-driven path.

Because your kubeconfig can define multiple clusters, users, and contexts, you can use `kubectl` to switch between clusters without reconfiguring your environment. Run `kubectl config use-context` to change the active context.

## What you can do with kubectl[](https://kubernetes.io/docs/concepts/overview/kubectl/#what-you-can-do-with-kubectl)

The `kubectl` tool supports many operations, which fall into these broad categories:
* Manage resources – Create, update, and delete objects such as Pods, Deployments, and Services. Use `kubectl apply` for declarative management from configuration files.
* Inspect cluster state – List and describe objects, view events, and check resource usage.
* Debug – View logs from containers, execute commands inside a running container, or port-forward to a Pod.
* Cluster operations – Drain nodes for maintenance, cordon nodes to prevent new workloads, and manage cluster configuration.
* Script and automate – Format output as JSON, YAML, or custom columns using [JSONPath](https://kubernetes.io/docs/reference/kubectl/jsonpath/) for use in scripts and pipelines.

For syntax, command reference, and examples, see the [kubectl reference documentation](https://kubernetes.io/docs/reference/kubectl/).

## Declarative vs imperative[](https://kubernetes.io/docs/concepts/overview/kubectl/#declarative-vs-imperative)

For production workloads, prefer [declarative object management](https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/) using `kubectl apply` with version-controlled configuration files. Declarative management helps you track changes, collaborate, and integrate with GitOps workflows. Imperative commands (such as `kubectl create` or `kubectl run`) are useful for development and experimentation, but are harder to reproduce and audit.

## Extending kubectl with plugins[](https://kubernetes.io/docs/concepts/overview/kubectl/#extending-kubectl-with-plugins)

You can extend `kubectl` with [plugins](https://kubernetes.io/docs/tasks/extend-kubectl/kubectl-plugins/) that add new sub-commands. Plugins are standalone binaries that follow the `kubectl-<plugin-name>` naming convention. The Kubernetes community maintains many plugins, and you can manage them with the [Krew](https://krew.sigs.k8s.io/) plugin manager.

## Version compatibility[](https://kubernetes.io/docs/concepts/overview/kubectl/#version-compatibility)

The `kubectl` tool supports a version skew of plus-or-minus one minor version relative to the cluster's control plane. For example, `kubectl` v1.32 works with control planes at v1.31, v1.32, and v1.33. Using a compatible version avoids unexpected behavior. See the [version skew policy](https://kubernetes.io/releases/version-skew-policy/) for details.

## What's next[](https://kubernetes.io/docs/concepts/overview/kubectl/#what-s-next)
* Read the [kubectl reference](https://kubernetes.io/docs/reference/kubectl/) for syntax and command details.
* [Install kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl) on your machine.
* Learn about [The Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/) that `kubectl` uses.
* Review [Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/) that make up a cluster.
* Explore [Object Management](https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/) and declarative configuration.
* Check the [version skew policy](https://kubernetes.io/releases/version-skew-policy/) for supported version combinations.

## Feedback

Was this page helpful?Yes No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes). Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to [report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io) or [suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).const yes=document.querySelector(".feedback--yes"),no=document.querySelector(".feedback--no");document.querySelectorAll(".feedback--link").forEach(e=>{e.href=e.href+window.location.pathname});const sendFeedback=e=>{typeof gtag=="function"?gtag("event","page_helpful",{event_category:"Helpful",event_label:window.location.pathname,value:e}):console.log("gtag not available; skipping analytics event")},disableButtons=()=>{yes.disabled=!0,yes.classList.add("feedback--button__disabled"),no.disabled=!0,no.classList.add("feedback--button__disabled")};yes.addEventListener("click",()=>{sendFeedback(100),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")}),no.addEventListener("click",()=>{sendFeedback(0),disableButtons(),document.querySelector(".feedback--response").classList.remove("feedback--response__hidden")})Last modified March 01, 2026 at 6:10 PM PST: [cross-link from related pages and remove thirdparty shortcode (ab6b7f2067)](https://github.com/kubernetes/website/commit/ab6b7f2067b467fbb66fd4c12a7fa96d0c1301f4)

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



# Source (Sub-link): https://kubernetes.io/docs/concepts/overview/working-with-objects/labels

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Overview](https://kubernetes.io/docs/concepts/overview/)
4. [Objects In Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/)
5. Labels and Selectors

# Labels and Selectors

Labels are key/value pairs that are attached to [objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects) such as Pods. Labels are intended to be used to specify identifying attributes of objects that are meaningful and relevant to users, but do not directly imply semantics to the core system. Labels can be used to organize and to select subsets of objects. Labels can be attached to objects at creation time and subsequently added and modified at any time. Each object can have a set of key/value labels defined. Each Key must be unique for a given object.
```yaml
"metadata": {
  "labels": {
    "key1" : "value1",
    "key2" : "value2"
  }
}
```

Labels allow for efficient queries and watches and are ideal for use in UIs and CLIs. Non-identifying information should be recorded using [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).

## Motivation[](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels#motivation)

Labels enable users to map their own organizational structures onto system objects in a loosely coupled fashion, without requiring clients to store these mappings.

Service deployments and batch processing pipelines are often multi-dimensional entities (e.g., multiple partitions or deployments, multiple release tracks, multiple tiers, multiple micro-services per tier). Management often requires cross-cutting operations, which breaks encapsulation of strictly hierarchical representations, especially rigid hierarchies determined by the infrastructure rather than by users.

Example labels:
* `"release" : "stable"`, `"release" : "canary"`
* `"environment" : "dev"`, `"environment" : "qa"`, `"environment" : "production"`
* `"tier" : "frontend"`, `"tier" : "backend"`, `"tier" : "cache"`
* `"partition" : "customerA"`, `"partition" : "customerB"`
* `"track" : "daily"`, `"track" : "weekly"`

These are examples of [commonly used labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/); you are free to develop your own conventions. Keep in mind that label Key must be unique for a given object.

## Syntax and character set[](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels#syntax-and-character-set)

Labels are key/value pairs. Valid label keys have two segments: an optional prefix and name, separated by a slash (`/`). The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (`.`), not longer than 253 characters in total, followed by a slash (`/`).

If the prefix is omitted, the label Key is presumed to be private to the user. Automated system components (e.g. `kube-scheduler`, `kube-controller-manager`, `kube-apiserver`, `kubectl`, or other third-party automation) which add labels to end-user objects must specify a prefix.

The `kubernetes.io/` and `k8s.io/` prefixes are [reserved](https://kubernetes.io/docs/reference/labels-annotations-taints/) for Kubernetes core components.

Valid label value:
* must be 63 characters or less (can be empty),
* unless empty, must begin and end with an alphanumeric character (`[a-z0-9A-Z]`),
* could contain dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between.

For example, here's a manifest for a Pod that has two labels `environment: production` and `app: nginx`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: label-demo
  labels:
    environment: production
    app: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
```

## Label selectors[](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels#label-selectors)

Unlike [names and UIDs](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/), labels do not provide uniqueness. In general, we expect many objects to carry the same label(s).

Via a label selector, the client/user can identify a set of objects. The label selector is the core grouping primitive in Kubernetes.

The API currently supports two types of selectors: equality-based and set-based. A label selector can be made of multiple requirements which are comma-separated. In the case of multiple requirements, all must be satisfied so the comma separator acts as a logical AND (`&&`) operator.

The semantics of empty or non-specified selectors are dependent on the context, and API types that use selectors should document the validity and meaning of them.

#### Note:For some API types, such as ReplicaSets, the label selectors of two instances must not overlap within a namespace, or the controller can see that as conflicting instructions and fail to determine how many replicas should be present.

---



# Source (Sub-link): https://kubernetes.io/docs/concepts/overview/working-with-objects/names

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Overview](https://kubernetes.io/docs/concepts/overview/)
4. [Objects In Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/)
5. Object Names and IDs

# Object Names and IDs

Each [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects) in your cluster has a [Name](https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names) that is unique for that type of resource. Every Kubernetes object also has a [UID](https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids) that is unique across your whole cluster.

For example, you can only have one Pod named `myapp-1234` within the same [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/), but you can have one Pod and one Deployment that are each named `myapp-1234`.

For non-unique user-provided attributes, Kubernetes provides [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) and [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).

## Names[](https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names)

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

### DNS Subdomain Names[](https://kubernetes.io/docs/concepts/overview/working-with-objects/names#dns-subdomain-names)

Most resource types require a name that can be used as a DNS subdomain name as defined in [RFC 1123](https://tools.ietf.org/html/rfc1123). This means the name must:
* contain no more than 253 characters
* contain only lowercase alphanumeric characters, '-' or '.'
* start with an alphanumeric character
* end with an alphanumeric character

### RFC 1123 Label Names[](https://kubernetes.io/docs/concepts/overview/working-with-objects/names#dns-label-names)

Some resource types require their names to follow the DNS label standard as defined in [RFC 1123](https://tools.ietf.org/html/rfc1123). This means the name must:
* contain at most 63 characters
* contain only lowercase alphanumeric characters or '-'
* start with an alphabetic character
* end with an alphanumeric character

#### Note:When the `RelaxedServiceNameValidation` feature gate is enabled, Service object names are allowed to start with a digit.

### RFC 1035 Label Names[](https://kubernetes.io/docs/concepts/overview/working-with-objects/names#rfc-1035-label-names)

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



# Source (Sub-link): https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/

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



# Source (Sub-link): https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/

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

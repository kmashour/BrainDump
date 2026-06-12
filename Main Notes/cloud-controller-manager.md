---
obsidianUIMode: preview
class: landing-note
tier: main-note
domains:
  - "kubernetes"
role: control-plane
related_concepts:
  - "[[kube-apiserver]]"
  - "[[kube-controller-manager]]"
  - "[[node]]"
reference_guides:
  - "[[Reference Notes/0-2_cluster_architecture_and_components.md]]"
tags:
  - kubernetes/component
  - status/completed
against: []

---

# cloud-controller-manager

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Control Plane > **cloud-controller-manager**

---

## 🎯 Purpose (Why it is used)
The `cloud-controller-manager` (CCM) embeds cloud-provider-specific control logic. It decouples the core Kubernetes system from the underlying cloud provider's APIs, allowing cloud vendors to develop and release integrations independently from the core Kubernetes release cycle.

---

## ⚙️ Functionality (What it is doing)
1. **Cloud Node Tracking:** Queries the cloud provider to check if a worker node VM has been deleted/terminated in the cloud console. If so, it removes the Node object from the cluster.
2. **Cloud Load Balancing:** Watches for Kubernetes Services of type `LoadBalancer` and interacts with cloud APIs to provision, update, or tear down physical cloud load balancers.
3. **Cloud Route Management:** Configures routing tables and network interfaces in the cloud provider's VPC/network infrastructure to enable Pod-to-Pod communication across different nodes.

---

## 🏛️ Architectural Context (How it fits in the architecture)
The `cloud-controller-manager` is an optional, pluggable Control Plane component:
* **In-Tree vs. Out-of-Tree:** Previously, cloud code was compiled "in-tree" inside the `kube-controller-manager`. In modern clusters, the CCM runs "out-of-tree" as a separate deployment or daemonset.
* **External Integration:** It acts as a bridge, reading from the `kube-apiserver` and sending API requests outward to the cloud provider (e.g., AWS, GCP, Azure, OpenStack) API endpoints.

---

## 🧩 Problem Solver (What problem it solves)
* **Code Bloat & Security:** Prevents compilation of proprietary cloud provider SDKs inside core Kubernetes binaries, reducing binary size and security attack surfaces.
* **Release Decoupling:** Allows cloud providers to fix bugs and add features to load balancer controllers without waiting for a new core Kubernetes minor release.
* **Manual Cloud Provisioning:** Automates the management of cloud resources (like subnets, routing tables, and public IPs) in response to standard Kubernetes manifest applications.

---

## 🟢 Operational Impact (What will happen with it operating)
* **Automated External Load Balancers:** Creating a Service of type `LoadBalancer` automatically provisions an external cloud load balancer and updates the Service's `.status.loadBalancer.ingress` with a public IP or DNS name.
* **Clean Node Lifecycles:** When a cloud instance is deleted (e.g., auto-scaled down), the Kubernetes node list is updated immediately.
* **Dynamic Cloud Routes:** Cloud network routing tables are updated to direct Pod subnet traffic to the correct VM nodes.

---

## 🔴 Failure Impact (What will happen without it)
* **Broken Load Balancers:** Creating or updating Services of type `LoadBalancer` will hang indefinitely with `<pending>` external IPs. Stale load balancers will not be deleted, incurring unnecessary cloud costs.
* **Orphaned Node Records:** If a cloud VM node is deleted, the cluster will permanently show that node as `NotReady` rather than clean it up, preventing scheduled workloads from being rescheduled promptly.
* **Routing Failures:** If node IP addresses change, the underlying VPC routes will become stale, cutting off Pod-to-Pod communications.
---

---

This note covers the architectural migration from in-tree to out-of-tree cloud providers, configuration flags, and the low-level functions of cloud-controller-manager (CCM) loops.

---

## 🏗️ 1. In-Tree vs. Out-of-Tree Architecture
In early Kubernetes versions, cloud-provider integration was compiled directly into the core `kube-controller-manager` binary ("in-tree"). This presented several issues:
1. **Security:** The core control plane required full credentials for cloud APIs.
2. **Maintenance:** Every minor patch or feature update to a cloud provider's API required recompiling Kubernetes core.
3. **Bloat:** The binary contained AWS, GCP, Azure, and OpenStack drivers simultaneously.

### The Modern Out-of-Tree Model
In modern Kubernetes, all cloud logic is moved to external binaries ("out-of-tree") maintained by the respective cloud vendors. To enable this, the following configuration is applied:
* The core components (`kube-apiserver`, `kube-controller-manager`, and `kubelet` on worker nodes) are launched with the flag:
  ```bash
  --cloud-provider=external
  ```
* This flag tells the control plane to hold off on initializing node metadata and configuring load balancers until the external `cloud-controller-manager` daemon is running and takes responsibility.

---

## ⚙️ 2. Core CCM Loops Deep Dive
The CCM executes three primary controller loops:

### A. Cloud Node Controller
* **Metadata Initialization:** When a node registers with the `--cloud-provider=external` flag, the Cloud Node Controller queries the cloud provider's API to fetch node details:
  * Availability Zone and Region labels (e.g., `topology.kubernetes.io/zone`).
  * Instance type (e.g., `node.kubernetes.io/instance-type`).
  * Node IP addresses (Internal/External).
* **Cleanup:** Periodically checks if instances registered as nodes have been deleted in the cloud provider's catalog. If an instance is missing from the cloud API, the controller deletes the Node object from the cluster.

### B. Route Controller
* Configures network routing rules within the cloud provider's VPC so that Pod-to-Pod traffic can route successfully across node boundaries.
* This is only used in clusters running without an overlay network (like Calico in BGP mode or flannel in host-gw mode) on cloud infrastructures that support route tables.

### C. Service Controller
* Listens for Services of `type: LoadBalancer`.
* Communicates with cloud APIs (e.g., AWS IAM/EC2, GCP Compute) to provision a physical balancer routing traffic to the NodePorts of the worker nodes.
* Assigns the resulting public IP or DNS name to the Service's status.

---

## 🔑 3. Cloud Access & Credentials
Because the CCM must create VMs, routes, and load balancers, it runs with high-privilege credentials:
* **IAM Roles for Service Accounts (IRSA/KMS):** On cloud environments (like AWS EKS or GCP GKE), the CCM is assigned an IAM role that permits it to interact with EC2, VPC, and ELB resources.
* **Credentials Secret:** On self-hosted cloud installations, cloud credentials (such as an OpenStack clouds.yaml or AWS credentials file) are mounted into the CCM Pod via a Secret.

*Read more in [0-2_cluster_architecture_and_components.md](../Reference%20Notes/0-2_cluster_architecture_and_components.md#2-control-plane-core-components-deep-dive).*

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **cloud-controller-manager**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
WHERE class = "deeper-dive" AND contains(parent_concept, this.file.link)
SORT file.name ASC
```

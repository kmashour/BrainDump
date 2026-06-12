---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[cloud-controller-manager]]"
sub_concepts:
  - "[[In-tree vs Out-of-tree Migration]]"
  - "[[Cloud Provider External Flags]]"
  - "[[Cloud Node Controller]]"
  - "[[Cloud Service Controller]]"
  - "[[Cloud Route Controller]]"
use_cases:
  - "[[IAM role assignments for CCM]]"
external_links:
  - "[Mumshad CKA Course](https://kodekloud.com)"
  - "[Kubernetes Official Docs](https://kubernetes.io/docs/concepts/architecture/cloud-controller-manager/)"
sub_type: core-concept
source_type: udemy
tags:
  - kubernetes/deep-dive
---
# cloud-controller-manager deeper

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[cloud-controller-manager]] > **deeper dive**

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

## 🔍 Sub-Concepts & Use Cases
This table automatically displays all deeper notes, use cases, and configurations associated with **cloud-controller-manager-deeper**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), "cloud-controller-manager-deeper")
SORT file.name ASC
```

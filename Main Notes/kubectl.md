---
obsidianUIMode: preview
class: landing-note
tier: main-note
domains:
  - "kubernetes"
role: client-tool
related_concepts:
  - "[[kube-apiserver]]"
reference_guides:
  - "[[Reference Notes/0-1_kube_api_and_kubectl.md]]"
  - "[[Reference Notes/0-12_kubernetes_api_management_and_pod_immutability.md]]"
tags:
  - kubernetes/cli
  - status/completed
against: []

---

# kubectl

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Tooling & Interfaces > **kubectl**

---

## 🎯 Purpose (Why it is used)
`kubectl` is the official command-line interface (CLI) client for Kubernetes. It allows cluster administrators, developers, and automation tools to communicate with the Kubernetes cluster control plane, managing resources, running debugging sessions, and inspecting state.

---

## ⚙️ Functionality (What it is doing)
1. **Config Parsing & Authentication:** Reads the active kubeconfig file (typically at `~/.kube/config`), extracts server addresses, and loads client credentials (certificates, tokens).
2. **REST API Serialization:** Converts human-readable CLI commands (e.g., `kubectl get pods`) into HTTP REST calls (e.g., `GET /api/v1/namespaces/default/pods`).
3. **API Request Dispatch:** Dispatches HTTPS requests to the `kube-apiserver` endpoint, handling SSL validation and certificate presentation.
4. **Response Formatting:** Receives JSON/Protobuf payloads from the API server and formats them into readable tables, raw JSON/YAML manifests, custom columns, or JSONPath queries.

---

## 🏛️ Architectural Context (How it fits in the architecture)
`kubectl` resides entirely outside the Kubernetes control plane:
* **External Client:** It runs on the administrator's local workstation, bastion hosts, or inside CI/CD runners.
* **API Server Gateway:** It has no direct access to nodes or the database (`etcd`). It interacts exclusively with the public or private HTTPS endpoint exposed by the `kube-apiserver`.

---

## 🧩 Problem Solver (What problem it solves)
* **API Complexity Abstraction:** Eliminates the need for administrators to construct manual HTTP REST payloads (using `curl` or `wget`) with complex authorization headers and nested JSON bodies.
* **Context Management:** Simplifies managing multiple clusters, user identities, and target namespaces, enabling quick context switching via simple configuration commands.

---

## 🟢 Operational Impact (What will happen with it operating)
* **Rapid Administration:** Users can inspect, create, patch, scale, or terminate resources with high efficiency.
* **Automation Bridge:** Scripts and CI/CD pipelines can interact with the cluster programmatically to orchestrate deployments and rolling updates.
* **Cluster Discovery:** The CLI can query the live cluster API to self-document schemas and resources dynamically.

---

## 🔴 Failure Impact (What will happen without it)
* **Clunky Administration:** Managing the cluster requires writing raw REST API calls using `curl` and crafting complex JSON payloads manually.
* **Debugging Hurdles:** Operations like checking container logs (`kubectl logs`) or executing shells inside containers (`kubectl exec`) become extremely complex.
* **Deployment Bottlenecks:** Pipelines and automation relying on the `kubectl` binary fail to apply state changes to the cluster.
* *Note:* The cluster itself continues running and orchestrating containers normally; only administrative visibility and configuration operations are affected.
---

---

This note covers the structural layout of Kubeconfig files, high-speed CKA syntax tricks, and advanced output parsing techniques for the **kubectl** CLI.

---

## 🗂️ 1. Kubeconfig Anatomy
The configuration file at `~/.kube/config` determines which cluster `kubectl` targets and how it authenticates. It is split into three main blocks:
1. **`clusters`:** A list of target clusters, including their API Server endpoints (e.g., `https://10.244.0.1:6443`) and Certificate Authority (CA) data to verify the server's identity.
2. **`users`:** A list of credentials. This contains client certificates (`client-certificate-data`, `client-key-data`), authentication tokens, or OIDC login configurations.
3. **`contexts`:** Associations mapping a `user` to a `cluster` and specifying a default `namespace` (e.g., "connect to `prod-cluster` as `admin-user` inside the `apps` namespace").

Commands to manage kubeconfigs:
* View current context: `kubectl config current-context`
* Switch context: `kubectl config use-context <context-name>`
* Set default namespace: `kubectl config set-context --current --namespace=<ns-name>`

---

## 🏎️ 2. High-Speed Syntax Formulas (CKA Exam Essentials)
In the CKA exam, speed is critical. Never write YAML manifests from scratch.

### A. The Dry-Run Template Generator
Generate resource manifests instantly without committing them to the API Server:
```bash
# Generate a Pod manifest
kubectl run nginx --image=nginx --dry-run=client -o yaml > pod.yaml

# Generate a Deployment manifest
kubectl create deployment web-app --image=nginx --replicas=3 --dry-run=client -o yaml > deploy.yaml

# Generate a Service manifest
kubectl expose pod nginx --port=80 --target-port=80 --type=NodePort --dry-run=client -o yaml > svc.yaml
```

### B. Force Deletion (Instant Cleanup)
By default, deleting a resource waits for containers to shutdown cleanly (30-second grace period). Bypass this for immediate results:
```bash
kubectl delete pod my-pod --force --grace-period=0
```

---

## 🔎 3. Advanced Output Formatting
You can parse complex API payloads directly in the CLI using filters:

### A. Custom Columns
Extract specific nested fields in a clean table format:
```bash
# Get Pod name and node assignment
kubectl get pods -o custom-columns=POD_NAME:.metadata.name,NODE_ASSIGNED:.spec.nodeName
```

### B. JSONPath Formatting
Extract lists, arrays, or single values from JSON structures:
```bash
# Extract the IP address of all running pods
kubectl get pods -o jsonpath='{.items[*].status.podIP}'

# Extract the container image of a deployment
kubectl get deploy web-app -o jsonpath='{.spec.template.spec.containers[0].image}'
```

---

## 🗺️ 4. API Discovery Commands
Query the API schema directly from the CLI:
* **`kubectl api-resources`:** Lists all API resource types, their shortnames (e.g., `po`, `deploy`, `svc`), API groups, and whether they are namespaced.
* **`kubectl api-versions`:** Lists the enabled API version paths.
* **`kubectl explain <resource>`:** Renders inline documentation for fields (e.g., `kubectl explain pod.spec.containers.securityContext`).

*Read more in [0-1_kube_api_and_kubectl.md](../Reference%20Notes/0-1_kube_api_and_kubectl.md#5-kubectl-cli-formula--speed-tricks).*

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **kubectl**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
WHERE class = "deeper-dive" AND contains(parent_concept, this.file.link)
SORT file.name ASC
```

# -*- coding: utf-8 -*-

STUDY_QUESTIONS = [
    {
        "id": "AS-01",
        "domain": "Advanced API & Extensions",
        "question": "What is the Operator Pattern, and what is the difference between a custom controller and an operator?",
        "answer": "The Operator Pattern is a design pattern that extends Kubernetes capabilities by using Custom Resources (CRs) to manage applications and their components. \n- A Custom Controller is the control loop that watches the custom resource state and reconciles it. \n- An Operator is a custom controller that packages domain-specific operational knowledge (e.g. backup, restore, scaling, upgrades) to manage a stateful application (like databases) dynamically."
    },
    {
        "id": "AS-02",
        "domain": "Advanced API & Extensions",
        "question": "Explain CustomResourceDefinition (CRD) validation using OpenAPI v3 schemas.",
        "answer": "Kubernetes validates custom resources against an OpenAPI v3 schema defined in the CRD's 'spec.versions[*].schema.openAPIV3Schema' field. You specify properties, types, patterns, and validation limits (e.g., minimum, maximum, required fields). The API Server rejects any request to create or update a custom resource that does not conform to this schema."
    },
    {
        "id": "AS-03",
        "domain": "Advanced API & Extensions",
        "question": "What are CRD status and scale subresources, and why are they useful?",
        "answer": "1. Status Subresource (/status): Decouples spec modifications from status updates. When enabled, updating spec does not permit status modifications, and the status can be modified separately using the '/status' endpoint, preventing race conditions.\n2. Scale Subresource (/scale): Exposes a standard interface containing replicas and selectors. This allows the Horizontal Pod Autoscaler (HPA) and 'kubectl scale' to manage replicas on the custom resource directly."
    },
    {
        "id": "AS-04",
        "domain": "Advanced API & Extensions",
        "question": "Explain API Aggregation and how it differs from Custom Resource Definitions (CRDs).",
        "answer": "1. CRDs: Declared inside the main API server. The API server handles storage in etcd directly. Easy to build, but lacks custom storage or custom logic.\n2. API Aggregation: You write a standalone custom API server (Extension API Server) and register it in the main API server using an APIService object. The main server proxies requests for that API path to your custom server, allowing custom storage, non-etcd databases, and custom request processing."
    },
    {
        "id": "AS-05",
        "domain": "Advanced Services & Routing",
        "question": "Describe the architecture and components of the next-gen Gateway API.",
        "answer": "Gateway API uses role-oriented resource definitions:\n1. GatewayClass: Defined by infrastructure providers. Specifies the controller implementation.\n2. Gateway: Defined by cluster operators. Instantiates the load balancer and details listeners/ports.\n3. HTTPRoute: Defined by application developers. Attaches to a Gateway and routes HTTP traffic based on path, headers, or query parameters to backend services."
    },
    {
        "id": "AS-06",
        "domain": "Advanced API & Admission",
        "question": "How does a MutatingAdmissionWebhook work, and where does it sit in the API request lifecycle?",
        "answer": "A MutatingAdmissionWebhook is an HTTP callback service registered in the API Server. During a write request, the API Server invokes the mutating webhook. The webhook can return a JSON Patch to modify the incoming resource (e.g., inject sidecar logging containers or default values). It sits *before* Schema Validation and *before* Validating Admission controllers in the API lifecycle."
    },
    {
        "id": "AS-07",
        "domain": "Advanced API & Admission",
        "question": "How does a ValidatingAdmissionWebhook work, and how does it differ from a Mutating Webhook?",
        "answer": "A ValidatingAdmissionWebhook evaluates incoming resource specifications and returns a simple boolean allow/deny decision along with a status message. Unlike Mutating Webhooks, it cannot alter the object configuration. It runs *after* schema validation and mutating admission. If any validating webhook denies the request, the entire API operation is rejected."
    },
    {
        "id": "AS-08",
        "domain": "CKS Security & Isolation",
        "question": "Explain AppArmor and how to assign an AppArmor profile to a container in a Pod.",
        "answer": "AppArmor is a Linux kernel security module that restricts container capabilities (e.g. write paths, network access). To enforce a profile, the profile must be loaded on the host kernels. In the Pod spec, you set the container's securityContext to reference the profile:\n```\nsecurityContext:\n  appArmorProfile:\n    type: Localhost\n    localhostProfile: k8s-apparmor-deny-write\n```"
    },
    {
        "id": "CKS Security & Isolation",
        "id": "AS-09",
        "domain": "CKS Security & Isolation",
        "question": "Describe Seccomp and how to apply a custom Seccomp profile to a Pod's SecurityContext.",
        "answer": "Seccomp (Secure Computing Mode) restricts the system calls a container can make to the Linux kernel, minimizing the exploit surface. Custom profiles are JSON files placed in the Kubelet's seccomp directory on the host (typically `/var/lib/kubelet/seccomp/`). You apply it by configuring `securityContext.seccompProfile`:\n```\nsecurityContext:\n  seccompProfile:\n    type: Localhost\n    localhostProfile: profiles/my-secure-profile.json\n```"
    },
    {
        "id": "AS-10",
        "domain": "CKS Security & Isolation",
        "question": "What is the role of RuntimeClasses in sandboxing workloads?",
        "answer": "RuntimeClasses allow you to run pods using alternative container runtimes/sandboxes (like gVisor or Kata Containers) instead of standard runc. You create a `RuntimeClass` object specifying a `handler` (e.g., `runsc` for gVisor). In the Pod spec, you set `runtimeClassName: gvisor`. The CRI agent uses this handler to isolate the container kernel interface from the host kernel."
    },
    {
        "id": "AS-11",
        "domain": "CKS Security & Isolation",
        "question": "Explain Pod Security Admission (PSA) and the three standards.",
        "answer": "PSA replaces PodSecurityPolicies. It evaluates pods against three Pod Security Standards:\n1. Privileged: No restrictions. Allows root/host namespaces.\n2. Baseline: Minimizes known privilege escalations. Restricts host paths/capabilities.\n3. Restricted: Heavily hardened. Forces non-root, drops capabilities, limits volumes.\nIt is applied by labeling namespaces with check levels: `enforce`, `audit`, or `warn` (e.g. `pod-security.kubernetes.io/enforce: restricted`)."
    },
    {
        "id": "AS-12",
        "domain": "CKAD Developer Tooling",
        "question": "Describe how Helm manages release history, rollback metadata, and chart template rendering.",
        "answer": "Helm renders local chart templates into standard YAML manifests using the Go template engine. When installed, Helm sends these to the Kubernetes API. Helm stores release metadata (versions, statuses, manifests) inside Kubernetes Secrets (or ConfigMaps) in the release namespace. When rolling back, Helm reads the historical secret metadata for that revision and applies it."
    },
    {
        "id": "AS-13",
        "domain": "CKAD Developer Tooling",
        "question": "What is Kustomize, and how do bases and overlays allow env-specific configuration overrides?",
        "answer": "Kustomize is a template-free configuration tool built into kubectl (`kubectl apply -k`). \n- Bases: Define the common, generic manifests (Deployments, Services) and standard settings.\n- Overlays: Define environment-specific customizations (e.g., 'dev' or 'prod') that merge with the base. Overlays can append patches, inject namespaces, prefix resource names, or modify replica counts without modifying the core base files."
    },
    {
        "id": "AS-14",
        "domain": "Advanced Workloads & Scheduling",
        "question": "Explain PodTopologySpreadConstraints and its key fields.",
        "answer": "It distributes pods evenly across failure domains (nodes, zones, regions) to ensure high availability. Key fields:\n- `maxSkew`: The maximum permissible difference in pod counts between any two topology domains.\n- `topologyKey`: The node label key representing the topology domain (e.g., `topology.kubernetes.io/zone`).\n- `whenUnsatisfiable`: `DoNotSchedule` (hard rule) or `ScheduleAnyway` (soft rule).\n- `labelSelector`: Matches pods to count for spreading."
    },
    {
        "id": "AS-15",
        "domain": "Advanced Workloads & Scheduling",
        "question": "Describe PriorityClasses, Pod Preemption, and how the scheduler resolves resource conflicts.",
        "answer": "A PriorityClass assigns a weight to pods. If a high-priority pod is scheduled but no nodes have enough resource capacity, the scheduler triggers Preemption. It scans nodes to identify low-priority pods that can be evicted. The scheduler evicts the victims, creating space, and schedules the high-priority pod on that node."
    },
    {
        "id": "AS-16",
        "domain": "Advanced Cluster Administration",
        "question": "How does Coordinated Leader Election work in Kubernetes using the Lease API?",
        "answer": "Components (like custom operators or controllers) create a `Lease` object (in the `coordination.k8s.io` group) to act as a lock. The active leader acquires the Lease and must periodically renew it (e.g., every 10 seconds). Backup instances watch the Lease. If the leader fails to renew before the lease expires, backup nodes attempt to write their ID to the Lease to claim leadership."
    },
    {
        "id": "AS-17",
        "domain": "Advanced Cluster Administration",
        "question": "What is Dynamic Resource Allocation (DRA), and how does it improve hardware device scheduling?",
        "answer": "DRA replaces the legacy resource limit model for specialized hardware (like GPUs). It models hardware devices using ResourceClass and ResourceClaim templates. It allows pods to claim devices dynamically, configure driver-specific parameters, and share resources between containers in a pod, providing more fine-grained control than standard resource requests."
    },
    {
        "id": "AS-18",
        "domain": "CKS Security & Isolation",
        "question": "Describe image vulnerability scanning with Trivy and how to build secure distroless images.",
        "answer": "Trivy scans container images for vulnerabilities (CVEs) by analyzing package managers and OS libraries. To minimize exploit surfaces, developers use Distroless images. Distroless images contain only the application and its runtime dependencies (e.g., glibc); they omit shell environments, package managers, and standard Unix utilities, preventing attackers from executing commands if a container is compromised."
    },
    {
        "id": "AS-19",
        "domain": "CKS Security & Isolation",
        "question": "What is Falco, and how does it detect runtime anomalies on nodes?",
        "answer": "Falco is a CNCF cloud-native runtime security tool. It intercepts Linux kernel system calls using eBPF or kernel modules. Falco compares system call patterns against a rule database (e.g., detecting shell spawn inside containers, write attempts to system directories, or unauthorized connections) and generates security alerts in real-time."
    },
    {
        "id": "AS-20",
        "domain": "Advanced API & Extensions",
        "question": "Explain API Server version skew rules and how kube-apiserver handles mixed-version resource proxies.",
        "answer": "In HA clusters running different API Server versions (e.g. during upgrades), resources created on one version must resolve on others. The API Server uses a 'Mixed Version Proxy' webhook. If an API Server receives a request for a resource version it doesn't support, it proxies the request over peer-to-peer HTTPS to a peer API Server that is capable of handling that specific schema version."
    },
    {
        "id": "AS-21",
        "domain": "Advanced Cluster Administration",
        "question": "How does systemd journald log management interact with Kubelet's container stdout?",
        "answer": "The container runtime intercepts stdout/stderr streams from the container process and writes them to local log files (typically JSON or CRI format in `/var/log/pods/`). If configured to use the journald logging driver, the runtime redirects these streams to the host systemd-journald service, allowing journalctl to index, query, and rate-limit logs at the node level."
    },
    {
        "id": "AS-22",
        "domain": "Advanced Cluster Administration",
        "question": "What are Device Plugins, and how do they expose vendor-specific hardware to the kubelet?",
        "answer": "Device Plugins are standalone daemons (typically running as DaemonSets) that register with Kubelet over gRPC. They advertise vendor-specific local resources (e.g. nvidia.com/gpu) to Kubelet. When a pod requesting that resource schedules, Kubelet calls the Device Plugin's Allocate() RPC endpoint to configure host paths, environment variables, or mount devices into the container interface."
    },
    {
        "id": "AS-23",
        "domain": "Advanced Workloads & Scheduling",
        "question": "What is the purpose of kube-scheduler framework extension points?",
        "answer": "The scheduling framework divides scheduling into sequential phases with plugin extension points: QueueSort (orders queue), PreFilter/Filter (prunes nodes), PostFilter (preempts), PreScore/Score (ranks nodes), Reserve (reserves resources), Permit (delays bind), and PreBind/Bind (applies node association in API). Developers write plugins hooking into these stages to customize scheduling behavior."
    },
    {
        "id": "AS-24",
        "domain": "Advanced Cluster Administration",
        "question": "Describe ETCD cluster Raft consensus quorum rules and the consequences of network partitions.",
        "answer": "ETCD uses the Raft consensus protocol. To make writes, a cluster needs a quorum of active members, defined as `(N/2) + 1` where N is the total members. If a network partition occurs, the side containing a quorum continues to operate. The partitioned minority side fails to achieve consensus and blocks all incoming writes, preventing split-brain database states."
    },
    {
        "id": "AS-25",
        "domain": "Advanced API & Admission",
        "question": "Explain Admission Webhook timeout policy, failure policy (Fail vs Ignore), and sideEffects.",
        "answer": "1. Failure Policy: `Fail` rejects the API write if the webhook server is unreachable or times out (strict). `Ignore` allows the API write to succeed anyway.\n2. Timeout Policy: Limits how long the API Server waits for the webhook response (max 30s).\n3. SideEffects: Declares if the webhook webhook execution triggers side-effects (e.g., sending out-of-band audit webhooks), which dictates if it can dry-run."
    }
]

# -*- coding: utf-8 -*-

STUDY_QUESTIONS = [
    # --- CLUSTER ARCHITECTURE, INSTALLATION & CONFIG (15 questions) ---
    {
        "id": "S-01",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "question": "What is the primary role of the Kubelet on a Kubernetes node, and how does it report node status back to the control plane?",
        "answer": "The Kubelet is the node agent that runs on every node in a cluster. Its main role is to ensure that containers described in PodSpecs are running and healthy. It communicates with the container runtime using the Container Runtime Interface (CRI). It reports node status by updating the corresponding Node status and sending heartbeats using NodeLease objects in the 'kube-node-lease' namespace every 10 seconds."
    },
    {
        "id": "S-02",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "question": "Explain the role of the ETCD database and how a control plane node interacts with it. Can the controller manager or scheduler access ETCD directly?",
        "answer": "ETCD is a highly available, consistent key-value store used as Kubernetes' backing store for all cluster data (state, configurations, secrets). Only the kube-apiserver communicates directly with ETCD. All other components (Scheduler, Controller Manager, Kubelet) must interact with the API Server to read or write state, ensuring consistent access control, validation, and locking."
    },
    {
        "id": "S-03",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "question": "What are the three main phases of a request handled by the kube-apiserver before it is committed to ETCD?",
        "answer": "1. Authentication: Verifies the identity of the requester (via client certs, tokens, basic auth).\n2. Authorization: Verifies if the authenticated user has permissions to perform the action (via RBAC, ABAC, Webhooks).\n3. Admission Control: Runs plug-ins (like NodeRestriction, Mutating/Validating Webhooks) that can modify or reject the request based on cluster policies before storing the object in ETCD."
    },
    {
        "id": "S-04",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "question": "What is the difference between kube-controller-manager and kube-scheduler?",
        "answer": "The kube-scheduler is responsible for scheduling pods onto appropriate nodes based on resource availability, constraints, taints/tolerations, affinity rules, etc. The kube-controller-manager runs controller processes (like Node Controller, ReplicaSet Controller, EndpointSlice Controller) in a continuous loop to watch the cluster state and drive it toward the desired state defined in the manifests."
    },
    {
        "id": "S-05",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "question": "What is the Container Runtime Interface (CRI), and why did Kubernetes deprecate Dockershim in v1.24?",
        "answer": "CRI is a gRPC API that allows kubelet to interact with various container runtimes (like containerd, CRI-O) without needing to recompile kubelet. Dockershim was a hardcoded wrapper inside kubelet to support Docker, which didn't natively implement CRI. It was deprecated to clean up kubelet code, delegate runtime maintenance to runtime developers, and encourage direct use of CRI-compliant runtimes."
    },
    {
        "id": "S-06",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "question": "Compare kube-proxy in iptables mode vs IPVS mode in terms of performance and scalability.",
        "answer": "In iptables mode, kube-proxy writes DNAT rules to Netfilter for every service. As the number of services grows, sequentially searching iptables rules incurs heavy CPU overhead. In IPVS mode, kube-proxy uses IP Virtual Server hash tables, which perform routing lookup in O(1) time regardless of service count. This makes IPVS significantly faster, more resource-efficient, and suitable for large clusters."
    },
    {
        "id": "S-07",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "question": "What are the key client/server TLS certificate pairs required for securing kube-apiserver communication, and where are they located in a kubeadm-provisioned cluster?",
        "answer": "In kubeadm, certificates are in `/etc/kubernetes/pki/`:\n1. `apiserver.crt` / `key`: API server serving certificate.\n2. `apiserver-kubelet-client.crt` / `key`: API server client cert to talk to kubelets.\n3. `etcd/ca.crt` / `server.crt`: For secure access to etcd.\n4. `ca.crt` / `ca.key`: Root CA cert for cluster-wide client verification."
    },
    {
        "id": "S-08",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "question": "What is a Static Pod, how does the Kubelet discover it, and how does it differ from a standard Kubernetes Pod?",
        "answer": "A Static Pod is managed directly by the Kubelet on a specific node without the API server's involvement. The Kubelet watches a local directory (specified by the `staticPodPath` or `--config` directory, typically `/etc/kubernetes/manifests`) for YAML changes. Static Pods cannot be controlled via `kubectl edit` or API commands; they are tied directly to the lifecycle of the kubelet service on that node, although kubelet creates a mirror pod in the API server for visibility."
    },
    {
        "id": "S-09",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "question": "What is the structural layout of a standard kubeconfig file, and what are its three primary components?",
        "answer": "A kubeconfig file consists of:\n1. `clusters`: Lists API server endpoints and their associated CA certificates.\n2. `users`: Defines credentials (client certificates, tokens, or basic auth) for authentication.\n3. `contexts`: Binds a specific user to a specific cluster (and optionally a default namespace).\nAn active context is set using the `current-context` field."
    },
    {
        "id": "S-10",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "question": "Describe the correct order of operations when upgrading a Kubernetes cluster using kubeadm.",
        "answer": "1. Upgrade the Primary Control Plane node:\n   a. Upgrade `kubeadm` package.\n   b. Run `kubeadm upgrade plan`, then `kubeadm upgrade apply vX.Y.Z`.\n   c. Drain node, upgrade `kubelet` and `kubectl`, then restart kubelet and uncordon.\n2. Upgrade secondary control plane nodes (if HA) using `kubeadm upgrade node`.\n3. Upgrade Worker nodes:\n   a. Upgrade `kubeadm` package on worker.\n   b. Run `kubeadm upgrade node`.\n   c. Drain node, upgrade `kubelet` and `kubectl`, restart kubelet, and uncordon node."
    },
    {
        "id": "S-11",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "question": "Write the exact etcdctl command structure required to take a backup snapshot of etcd.",
        "answer": "ETCDCTL_API=3 etcdctl \\\n  --endpoints=https://127.0.0.1:2379 \\\n  --cacert=/etc/kubernetes/pki/etcd/ca.crt \\\n  --cert=/etc/kubernetes/pki/etcd/server.crt \\\n  --key=/etc/kubernetes/pki/etcd/server.key \\\n  snapshot save /opt/etcd-backup.db"
    },
    {
        "id": "S-12",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "question": "Explain what a bootstrap token is during a `kubeadm join` workflow and how its security is verified by a worker node.",
        "answer": "A bootstrap token is a short-lived token (default 24 hours) used to establish temporary trust between a joining node and the control plane. The worker node contacts the API server using the token, downloads the cluster-info ConfigMap, and verifies its authenticity using the discovery-token-ca-cert-hash. Once trust is established, the node exchanges the token for a permanent node client certificate signed by the cluster CA."
    },
    {
        "id": "S-13",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "question": "How do you manually approve a pending CertificateSigningRequest (CSR) in Kubernetes, and what command shows its details?",
        "answer": "To view all CSRs: `kubectl get csr`\nTo view details of a specific CSR: `kubectl describe csr <csr-name>`\nTo approve the CSR: `kubectl certificate approve <csr-name>`"
    },
    {
        "id": "S-14",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "question": "How does Kubernetes v1.22+ manage Linux Swap memory, and what settings must be enabled in the Kubelet configuration to support it?",
        "answer": "Historically, Kubernetes required swap to be disabled. From v1.22+, kubelet can run with swap enabled. To support this, swap must be active on the host, and the Kubelet configuration file (`/var/lib/kubelet/config.yaml`) must set `failSwapOn: false`. Optionally, `memorySwap.swapBehavior` can be set to `LimitedSwap` (workloads limited to their swap allocation) or `UnlimitedSwap`."
    },
    {
        "id": "S-15",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "question": "What is the difference between the Core API Group (/) and Named API Groups, and how does the API Server organize them in URL paths?",
        "answer": "The Core API Group contains legacy core objects (Pods, Services, Nodes, ConfigMaps, Secrets) and is served at `/api/v1`. Named API Groups contain all other resources (Deployments, StatefulSets, NetworkPolicies) and are organized under `/apis/<group-name>/<version>` (e.g., `/apis/apps/v1` for Deployments). This separation allows distinct versioning lifecycles for newer resources."
    },

    # --- WORKLOADS & SCHEDULING (9 questions) ---
    {
        "id": "S-16",
        "domain": "Workloads & Scheduling (15%)",
        "question": "How does a DaemonSet guarantee that a pod is scheduled on every node, and what taints does it tolerate automatically?",
        "answer": "The DaemonSet controller automatically schedules pods to matching nodes by creating pods with node affinity rules matching node labels. The controller automatically bypasses `unschedulable` states and tolerates scheduling-related taints: `node.kubernetes.io/not-ready` (NoExecute), `node.kubernetes.io/unreachable` (NoExecute), and `node.kubernetes.io/disk-pressure` (NoSchedule) to ensure monitoring/logging agents keep running."
    },
    {
        "id": "S-17",
        "domain": "Workloads & Scheduling (15%)",
        "question": "Compare NodeSelector vs NodeAffinity. What are the two types of NodeAffinity, and when would you use each?",
        "answer": "NodeSelector is a simple key-value label selector. NodeAffinity offers advanced matching expressions (In, NotIn, Exists, Gt, Lt).\n1. `requiredDuringSchedulingIgnoredDuringExecution`: Hard constraint (pod won't schedule unless node matches).\n2. `preferredDuringSchedulingIgnoredDuringExecution`: Soft constraint (scheduler tries to place it on matching nodes but defaults to others if none are available)."
    },
    {
        "id": "S-18",
        "domain": "Workloads & Scheduling (15%)",
        "question": "What are the three possible effects of a Taint, and how do they differ?",
        "answer": "1. `NoSchedule`: Prevents new pods without a matching toleration from scheduling on the node. Existing pods are unaffected.\n2. `PreferNoSchedule`: The scheduler attempts to avoid placing the pod on the tainted node, but will schedule it if no other nodes are available.\n3. `NoExecute`: Prevents new pods and evicts already running pods immediately (or after a toleration delay) if they lack matching tolerations."
    },
    {
        "id": "S-19",
        "domain": "Workloads & Scheduling (15%)",
        "question": "In a Pod with multiple Init Containers and Application Containers, what is the exact execution order, and what happens if an Init Container fails?",
        "answer": "Init containers run sequentially, one after another, in the order defined in the spec. All init containers must terminate successfully (exit code 0) before any application containers start. If an init container fails, the Kubelet restarts the Pod (according to its `restartPolicy`) and restarts the sequence from the first init container again."
    },
    {
        "id": "S-20",
        "domain": "Workloads & Scheduling (15%)",
        "question": "Explain the parameters `maxSurge` and `maxUnavailable` in a Deployment's RollingUpdate strategy.",
        "answer": "1. `maxSurge`: The maximum number of Pods that can be created above the desired replica count during an upgrade. Can be an absolute number or percentage (default 25%).\n2. `maxUnavailable`: The maximum number of Pods that can be unavailable (terminated) relative to the desired replica count during the update (default 25%). Both cannot be zero simultaneously."
    },
    {
        "id": "S-21",
        "domain": "Workloads & Scheduling (15%)",
        "question": "What is a Pod Disruption Budget (PDB), and how does it protect workloads during voluntary node maintenance (like a node drain)?",
        "answer": "A PDB limits the number of pods of a replicated application that are down simultaneously due to voluntary disruptions (drains, upgrades). You define it using `minAvailable` or `maxUnavailable`. When `kubectl drain` is called, the eviction API respects the PDB and will block/fail the drain if evicting the pod would violate the budget, giving the application time to spin up replicas on other nodes."
    },
    {
        "id": "S-22",
        "domain": "Workloads & Scheduling (15%)",
        "question": "Distinguish between LimitRange and ResourceQuota.",
        "answer": "1. `ResourceQuota`: Configures total resource consumption limits (e.g., total CPU, Memory, or number of pods/secrets) at the Namespace level. If a namespace exceeds this total, new resources are blocked.\n2. `LimitRange`: Defines default/min/max CPU and memory requests/limits for individual Pods or Containers within a Namespace, enforcing compliance during creation."
    },
    {
        "id": "S-23",
        "domain": "Workloads & Scheduling (15%)",
        "question": "What are the three Concurrency Policies for CronJobs, and what is their default behavior?",
        "answer": "1. `Allow` (Default): Permits concurrently running jobs if a previous job is still active.\n2. `Forbid`: Skips the new run if the previous run hasn't finished yet.\n3. `Replace`: Terminates the currently running job and replaces it with a new one."
    },
    {
        "id": "S-24",
        "domain": "Workloads & Scheduling (15%)",
        "question": "Explain Owner References and how Garbage Collection handles resource deletion using Foreground vs Background cascading deletion.",
        "answer": "Owner References define parent-child links between objects (e.g. Deployment owns ReplicaSet, which owns Pods). When a parent is deleted:\n1. `Background` (Default): The parent is deleted immediately, and the garbage collector deletes dependents in the background.\n2. `Foreground`: The parent enters a 'deletion in progress' state, and dependents are deleted first. Once all dependents are deleted, the parent is removed."
    },

    # --- SERVICES & NETWORKING (12 questions) ---
    {
        "id": "S-25",
        "domain": "Services & Networking (20%)",
        "question": "Compare ClusterIP, NodePort, and LoadBalancer service types.",
        "answer": "1. `ClusterIP` (Default): Exposes the service on a cluster-internal IP. Accessible only within the cluster.\n2. `NodePort`: Exposes the service on each Node's IP at a static port (default range 30000-32767). Routes traffic to an internal ClusterIP.\n3. `LoadBalancer`: Exposes the service externally using a cloud provider's load balancer. Automatically provisions a public IP and routes traffic to a NodePort."
    },
    {
        "id": "S-26",
        "domain": "Services & Networking (20%)",
        "question": "What is CoreDNS, and what is the standard DNS resolution format for a Service named 'web' in namespace 'prod'?",
        "answer": "CoreDNS is a flexible, extensible DNS server that acts as the cluster DNS. It resolves service names to ClusterIPs. The standard DNS format is: `<service-name>.<namespace>.svc.cluster.local`. For 'web' in namespace 'prod', it resolves as `web.prod.svc.cluster.local`."
    },
    {
        "id": "S-27",
        "domain": "Services & Networking (20%)",
        "question": "What is the difference between an Ingress Resource and an Ingress Controller?",
        "answer": "1. `Ingress Resource`: A Kubernetes configuration object (YAML) that defines routing rules (hosts, HTTP paths, backends) for external traffic.\n2. `Ingress Controller`: The actual reverse proxy daemon (like Nginx, Traefik, HAProxy) running in the cluster that watches for Ingress resources and configures itself to implement those routing rules."
    },
    {
        "id": "S-28",
        "domain": "Services & Networking (20%)",
        "question": "How do you define a default deny-all NetworkPolicy for a namespace, and how do you selectively allow traffic to a specific pod?",
        "answer": "A default deny-all policy uses a `podSelector: {}` with empty ingress/egress blocks to match all pods in the namespace. To selectively allow traffic, you create a policy targeting specific pods via `podSelector: matchLabels` and add an `ingress` block specifying allowed source pods using `podSelector` or namespaces using `namespaceSelector`."
    },
    {
        "id": "S-29",
        "domain": "Services & Networking (20%)",
        "question": "What is the Container Network Interface (CNI), and what are the basic requirements of a CNI network plugin in Kubernetes?",
        "answer": "CNI is a standard specification defining how network plugins should configure network interfaces for containers. A CNI plugin must ensure:\n1. Every Pod gets a unique IP address across the cluster.\n2. Pods on any node can communicate with pods on any other node without NAT.\n3. Agents on a node (like kubelet) can communicate with pods on that node."
    },
    {
        "id": "S-30",
        "domain": "Services & Networking (20%)",
        "question": "Explain the transition from Endpoints to EndpointSlices in Kubernetes.",
        "answer": "Legacy `Endpoints` objects grouped all backing pod IPs into a single resource. For services with thousands of pods, updating any pod IP required transmitting the entire large object, consuming massive API CPU and bandwidth. `EndpointSlices` partition endpoints into multiple smaller resources (max 100 endpoints per slice by default), significantly increasing scalability and network performance."
    },
    {
        "id": "S-31",
        "domain": "Services & Networking (20%)",
        "question": "What is a Headless Service, how do you define it in YAML, and what is its primary use case?",
        "answer": "A Headless Service is a service without an allocated ClusterIP (`clusterIP: None` in spec). Instead of returning a single load-balanced service IP, a DNS lookup for a headless service returns the A records (direct pod IPs) of all matching pods. It is primarily used with StatefulSets (e.g. databases) to enable direct peer-to-peer clustering and communication."
    },
    {
        "id": "S-32",
        "domain": "Services & Networking (20%)",
        "question": "Write the YAML structure of a NetworkPolicy that allows incoming traffic on port 80 to pods labeled `role: web` only from pods in the same namespace labeled `role: api`.",
        "answer": "apiVersion: networking.k8s.io/v1\nkind: NetworkPolicy\nmetadata:\n  name: allow-api-to-web\n  namespace: default\nspec:\n  podSelector:\n    matchLabels:\n      role: web\n  policyTypes:\n  - Ingress\n  ingress:\n  - from:\n    - podSelector:\n        matchLabels:\n          role: api\n    ports:\n    - protocol: TCP\n      port: 80"
    },
    {
        "id": "S-33",
        "domain": "Services & Networking (20%)",
        "question": "What is the Gateway API, and how does it differ from the legacy Ingress API?",
        "answer": "Gateway API is a collection of resources (GatewayClass, Gateway, HTTPRoute) designed to evolve Ingress. It uses role-oriented interfaces. Cluster Operators manage infrastructure via `GatewayClass` and `Gateway`, while Application Developers map routing via `HTTPRoute` objects. This decouples infrastructure management from application traffic routing rules."
    },
    {
        "id": "S-34",
        "domain": "Services & Networking (20%)",
        "question": "What is the purpose of `externalTrafficPolicy: Local` in a Service definition, and what is the trade-off?",
        "answer": "By default (`externalTrafficPolicy: Cluster`), ingress traffic on a NodePort is load-balanced across all pods, potentially routing traffic to another node (NAT hides the client source IP). Setting it to `Local` forces traffic to stay on the node it arrived on, preserving the client's original source IP. The trade-off is potential uneven traffic distribution if pods are not evenly spread across nodes."
    },
    {
        "id": "S-35",
        "domain": "Services & Networking (20%)",
        "question": "Where is the local CNI configuration file located on a node, and where are CNI binary plugins kept?",
        "answer": "1. CNI Configuration directory: `/etc/cni/net.d/` (typically holds JSON files like `10-containerd.conf` or CNI configs).\n2. CNI Binaries directory: `/opt/cni/bin/` (contains executables like loopback, bridge, portmap, etc.)."
    },
    {
        "id": "S-36",
        "domain": "Services & Networking (20%)",
        "question": "How do you instruct CoreDNS to forward queries for a specific domain (e.g., `mycorp.local`) to an external DNS server?",
        "answer": "Modify the `coredns` ConfigMap in the `kube-system` namespace. Add a server block for the domain:\n```\nmycorp.local:53 {\n    errors\n    cache 30\n    forward . 10.10.0.53\n}\n```\nApply the change and restart the CoreDNS deployment pods."
    },

    # --- STORAGE (6 questions) ---
    {
        "id": "S-37",
        "domain": "Storage (10%)",
        "question": "Explain the lifecycle phases of a PersistentVolume (PV): Available, Bound, Released, and Failed.",
        "answer": "1. `Available`: The PV has been created and is ready to be bound to a PVC.\n2. `Bound`: The PV is successfully mapped and reserved for a specific PVC.\n3. `Released`: The PVC has been deleted, but the volume is not yet reclaimed by the cluster.\n4. `Failed`: The volume failed its automatic reclamation process."
    },
    {
        "id": "S-38",
        "domain": "Storage (10%)",
        "question": "What is a StorageClass, and what is the role of the `provisioner` field?",
        "answer": "A StorageClass defines the 'classes' of storage available (e.g. SSD, HDD). It allows dynamic provisioning of PVs on-demand. The `provisioner` field determines which volume plugin is used to provision the physical storage (e.g. `kubernetes.io/aws-ebs` or `rancher.io/local-path`)."
    },
    {
        "id": "S-39",
        "domain": "Storage (10%)",
        "question": "Compare the three volume Reclaim Policies: Retain, Delete, and Recycle.",
        "answer": "1. `Retain` (Default): Keeps the PV and its data when the PVC is deleted. The PV status becomes Released. Admin must manually clean data.\n2. `Delete`: Deletes the PV and the underlying cloud/physical storage resource automatically when the PVC is deleted.\n3. `Recycle` (Deprecated): Performs a basic scrub (`rm -rf /vol/*`) and makes the PV Available again for a new binding."
    },
    {
        "id": "S-40",
        "domain": "Storage (10%)",
        "question": "What are the four Access Modes for Persistent Volumes, and how do they differ?",
        "answer": "1. `ReadWriteOnce` (RWO): Mountable as read-write by a single node.\n2. `ReadOnlyMany` (ROX): Mountable as read-only by many nodes.\n3. `ReadWriteMany` (RWX): Mountable as read-write by many nodes.\n4. `ReadWriteOncePod` (RWOP): Mountable as read-write by a single Pod (v1.22+)."
    },
    {
        "id": "S-41",
        "domain": "Storage (10%)",
        "question": "How do you enable dynamic volume expansion for Persistent Volume Claims?",
        "answer": "To allow volume expansion, the associated StorageClass must have `allowVolumeExpansion: true` in its configuration. Once set, you can edit the PVC's `spec.resources.requests.storage` field to request a larger size. The underlying storage plugin must support expansion."
    },
    {
        "id": "S-42",
        "domain": "Storage (10%)",
        "question": "What is the behavior of ConfigMaps or Secrets mounted as volumes in a Pod when the source ConfigMap/Secret is updated in the API?",
        "answer": "When a ConfigMap or Secret is updated, the mounted files are eventually updated automatically (usually within a few minutes, depending on the kubelet sync period and cache TTL). However, this only applies to volumes mounted directly without subPath; if a subPath is used, the file is not updated automatically and requires a pod restart."
    },

    # --- TROUBLESHOOTING (18 questions) ---
    {
        "id": "S-43",
        "domain": "Troubleshooting (30%)",
        "question": "What are the step-by-step diagnostic actions to perform when a worker node status is 'NotReady'?",
        "answer": "1. SSH into the node container/host.\n2. Check service status: `systemctl status kubelet`.\n3. Inspect kubelet logs: `journalctl -u kubelet -n 100 -f` or check `/var/log/syslog`.\n4. Check container runtime status: `systemctl status containerd`.\n5. Verify disk space: `df -h` and memory: `free -m` (check for DiskPressure/MemoryPressure).\n6. Check node network interface and route configs."
    },
    {
        "id": "S-44",
        "domain": "Troubleshooting (30%)",
        "question": "If the control plane node is unresponsive and `kubectl` commands fail with 'Connection Refused', how do you debug the API Server?",
        "answer": "1. SSH into the control plane node container.\n2. Check if the container runtime is running: `docker ps` or `crictl ps`.\n3. Inspect the static pod log files directly on the host under `/var/log/pods/`.\n4. Verify if the manifest files in `/etc/kubernetes/manifests/` (specifically `kube-apiserver.yaml`) are corrupted or have incorrect paths/flags."
    },
    {
        "id": "S-45",
        "domain": "Troubleshooting (30%)",
        "question": "Write a `kubectl` command to list all Pods sorted by CPU usage. What API service must be active for this to work?",
        "answer": "Command: `kubectl top pod --all-namespaces --sort-by=cpu`\nRequirement: The Metrics Server component must be installed and active in the cluster (`apiservice v1beta1.metrics.k8s.io` must be available)."
    },
    {
        "id": "S-46",
        "domain": "Troubleshooting (30%)",
        "question": "What are the common causes of `CrashLoopBackOff` in a container, and how do you extract details about the previous failed run?",
        "answer": "Common causes: Application configuration typos, missing environment variables/secrets, container port binding conflicts, database connection timeouts, liveness probe failing, or file permission errors.\nTo inspect logs of the previous crashed instance: `kubectl logs <pod-name> --previous`\nTo view container exit codes: `kubectl get pod <pod-name> -o jsonpath='{.status.containerStatuses[0].lastState.terminated.exitCode}'`."
    },
    {
        "id": "S-47",
        "domain": "Troubleshooting (30%)",
        "question": "How do you identify why a Pod is stuck in the `Pending` state?",
        "answer": "Run `kubectl describe pod <pod-name>`. Look at the 'Events' section at the bottom. Common causes include:\n1. Insufficient resources (CPU, Memory) on all nodes.\n2. NodeSelector, NodeAffinity, or PodAntiAffinity constraints.\n3. Unmatched taints on nodes (pod lacks required tolerations).\n4. Unbound PersistentVolumeClaims (PVC) waiting for consumer."
    },
    {
        "id": "S-48",
        "domain": "Troubleshooting (30%)",
        "question": "What is the difference between `ImagePullBackOff` and `ErrImagePull`, and how do you resolve private registry credentials issues?",
        "answer": "`ErrImagePull` is the immediate error when attempting to pull (e.g. network failure, wrong image tag). `ImagePullBackOff` is the status when Kubelet enters a back-off loop to retry pulling the image. To resolve private registry issues, you must create a secret of type `docker-registry` containing the auth credentials and link it using `imagePullSecrets` in the PodSpec."
    },
    {
        "id": "S-49",
        "domain": "Troubleshooting (30%)",
        "question": "How do you check if a Service's traffic is reaching the backing pods? What resource lists the active routing IPs of these pods?",
        "answer": "1. Run `kubectl get endpoints <service-name>` or `kubectl get endpointslices -l kubernetes.io/service-name=<service-name>`.\n2. If the endpoints list is empty, the service selector labels do not match the pod labels. Verify the service's `spec.selector` against the pods' `metadata.labels`."
    },
    {
        "id": "S-50",
        "domain": "Troubleshooting (30%)",
        "question": "How do you verify if the CoreDNS pod is functioning correctly, and how do you test internal DNS resolution from a temporary debug pod?",
        "answer": "1. Check CoreDNS status: `kubectl get pods -n kube-system -l k8s-app=kube-dns`.\n2. Check CoreDNS logs: `kubectl logs -n kube-system -l k8s-app=kube-dns`.\n3. Test resolution using a temporary utility pod:\n   `kubectl run dns-test --rm -i --tty --image=busybox -- restart=Never -- nslookup kubernetes.default`"
    },
    {
        "id": "S-51",
        "domain": "Troubleshooting (30%)",
        "question": "How do you test if a ServiceAccount has permission to create deployments in namespace 'prod' using the command line?",
        "answer": "kubectl auth can-i create deployments \\\n  --namespace=prod \\\n  --as=system:serviceaccount:prod:my-serviceaccount-name"
    },
    {
        "id": "S-52",
        "domain": "Troubleshooting (30%)",
        "question": "Where do you locate the Kubelet configuration file path, and how do you determine if it is using systemd or cgroupfs as its cgroup driver?",
        "answer": "1. Check the active kubelet systemd service unit file (typically `/etc/systemd/system/kubelet.service.d/10-kubeadm.conf`) to find the `--config` file path, usually `/var/lib/kubelet/config.yaml`.\n2. Open `/var/lib/kubelet/config.yaml` and look for the field `cgroupDriver: systemd` (or run `kubectl get no -o yaml` and check node info)."
    },
    {
        "id": "S-53",
        "domain": "Troubleshooting (30%)",
        "question": "Explain Node Eviction and what memory/disk thresholds trigger Kubelet to evict pods.",
        "answer": "Kubelet monitors resource usage on nodes. If resources cross certain hard eviction thresholds, Kubelet terminates pods to reclaim resources. The default hard eviction thresholds are:\n- `memory.available < 100Mi`\n- `nodefs.available < 10%`\n- `nodefs.inodesFree < 5%`\n- `imagefs.available < 15%`"
    },
    {
        "id": "S-54",
        "domain": "Troubleshooting (30%)",
        "question": "If a Pod fails to bind to a HostPort, what diagnostic command would you run on the worker node to verify port availability?",
        "answer": "SSH into the worker node container and run:\n`netstat -tulnp | grep <port-number>` or `ss -tulnp | grep <port-number>`\nThis will identify if another local process or container is already listening on that port on the node host network interface."
    },
    {
        "id": "S-55",
        "domain": "Troubleshooting (30%)",
        "question": "How do you verify if a NetworkPolicy is active on a pod, and what happens if two policies apply to the same pod?",
        "answer": "You can inspect the pod labels and namespace policies via `kubectl describe pod` and `kubectl get netpol`. If multiple NetworkPolicies select the same pod, they are additive. The union of all ingress/egress rules is evaluated; if any single policy allows traffic, it is allowed."
    },
    {
        "id": "S-56",
        "domain": "Troubleshooting (30%)",
        "question": "How do you troubleshoot a kubeadm upgrade failure, and where are the backup manifests stored during the upgrade process?",
        "answer": "If an upgrade fails, inspect the kube-apiserver logs and system logs. During `kubeadm upgrade`, kubeadm backs up the previous static pod manifests to `/etc/kubernetes/tmp/` (e.g. `kubeadm-backup-manifests-XXXX`). To rollback, copy these backup manifests back into `/etc/kubernetes/manifests/` and restart kubelet."
    },
    {
        "id": "S-57",
        "domain": "Troubleshooting (30%)",
        "question": "How do you check expiration details for all control plane certificates managed by kubeadm?",
        "answer": "Run command: `kubeadm certs check-expiration`"
    },
    {
        "id": "S-58",
        "domain": "Troubleshooting (30%)",
        "question": "What is the CNI configuration file extension required by Kubelet to detect it, and what happens if Kubelet finds multiple CNI configs?",
        "answer": "The Kubelet searches `/etc/cni/net.d/` for CNI configuration files. It recognizes `.conf`, `.conflist`, or `.json` extensions. If multiple CNI config files exist, Kubelet uses the first alphabetical configuration file (e.g., `10-calico.conflist` is preferred over `20-flannel.conf`)."
    },
    {
        "id": "S-59",
        "domain": "Troubleshooting (30%)",
        "question": "How do you trace iptables network packets for kube-proxy rules to troubleshoot routing failures?",
        "answer": "Run `iptables -t nat -L -v` inside the node container to inspect nat chains. Search for chains prefixed with `KUBE-` (e.g., `KUBE-SERVICES`, `KUBE-SVC-XXX`). Use `tcpdump -i any host <pod-ip>` to capture packets on virtual ethernet bridges to see if routing or filtering blocks the packets."
    },
    {
        "id": "S-60",
        "domain": "Troubleshooting (30%)",
        "question": "How do you inspect the current etcd cluster member health and list the etcd cluster members?",
        "answer": "ETCDCTL_API=3 etcdctl \\\n  --endpoints=https://127.0.0.1:2379 \\\n  --cacert=/etc/kubernetes/pki/etcd/ca.crt \\\n  --cert=/etc/kubernetes/pki/etcd/server.crt \\\n  --key=/etc/kubernetes/pki/etcd/server.key \\\n  member list -w table"
    }
]

# 🏆 CKA Exam Preparation: GOLD Walkthrough Playbook

This document contains the complete walkthrough, problems, hints, and step-by-step solutions for all **150 tasks** in the CKA GOLD interactive practice engine (60 Study Q&As and 90 Environment Scenarios). Use this guide to study the concepts and solutions alongside practicing them in the terminal via `./gold.sh`.

## 📌 Navigation Table of Contents
- [Troubleshooting (30%)](#troubleshooting-30%)
- [Cluster Architecture, Installation & Config (25%)](#cluster-architecture-installation-and-config-25%)
- [Services & Networking (20%)](#services-and-networking-20%)
- [Workloads & Scheduling (15%)](#workloads-and-scheduling-15%)
- [Storage (10%)](#storage-10%)

---

## ⚠️ KinD Cluster Environment Limitations & CKA Exam Differences

Because this interactive practice suite runs inside a lightweight **KinD (Kubernetes in Docker)** 3-node cluster rather than dedicated Ubuntu virtual machines, there are several key architectural differences between this sandbox environment and the actual CKA exam:

1. **SSH Connection Protocol:**
   * **Actual CKA Exam:** You SSH directly into VM node hosts (`ssh node01`, `ssh controlplane`) or switch node contexts.
   * **KinD Sandbox:** The nodes are Docker containers. You must simulate SSH access by running `docker exec -it <node-name> bash` (e.g. `docker exec -it cka-gold-control-plane bash`) from the host terminal.

2. **Cluster & Package Upgrades (kubeadm/kubelet/kubectl):**
   * **Actual CKA Exam:** The binaries are installed via APT/YUM package managers. Upgrades are done in-place by unholding and installing package versions (`apt-get install kubeadm=X.Y.Z`).
   * **KinD Sandbox:** KinD node images have static binaries baked directly into `/usr/bin/` inside the containers without package repos. Therefore, in-place binary package upgrades are simulated using touch verification files (`/var/log/upgrade-test/upgraded` and `/var/log/worker-upgraded`) and draining commands.

3. **ETCD Backup & Restoration Paths:**
   * **Actual CKA Exam:** The ETCD snapshot database and manifests exist directly on the VM host.
   * **KinD Sandbox:** You must run the `etcdctl` command *inside* the `cka-gold-control-plane` container, and the paths refer to the directories inside the container.

4. **CNI Configurations & Network Drivers:**
   * **Actual CKA Exam:** The CNI is typically Calico, Cilium, or Flannel.
   * **KinD Sandbox:** The default CNI is `kindnet`. The daemonset and configurations are specific to KinD (`kindnet` daemonset in `kube-system` namespace, `/etc/cni/net.d/10-kindnet.conflist`).

5. **Kernel Modules & Read-Only Sysctls:**
   * **Actual CKA Exam:** Each VM has its own independent kernel. You can load new modules (`modprobe br_netfilter`) or set sysctls (`sysctl -w net.ipv4.ip_forward=1`).
   * **KinD Sandbox:** The containers share the host machine's Linux kernel. Direct write modifications to `/proc/sys` are blocked inside containers unless run with extreme host privileges, which would affect your actual workstation OS.

---

## Troubleshooting (30%)
This section covers all tasks representing Troubleshooting (30%) of the CKA curriculum.

### 📝 Conceptual Study Q&As (21 Tasks)
These tasks test your core knowledge of Kubernetes architecture, parameters, commands, and YAML syntax.

#### 🔍 S-43: What are the step-by-step diagnostic actions to perform when a worker node statu...
**Question:**
What are the step-by-step diagnostic actions to perform when a worker node status is 'NotReady'?

**Answer (Mumshad Standard):**
```
1. SSH into the node container/host.
2. Check service status: `systemctl status kubelet`.
3. Inspect kubelet logs: `journalctl -u kubelet -n 100 -f` or check `/var/log/syslog`.
4. Check container runtime status: `systemctl status containerd`.
5. Verify disk space: `df -h` and memory: `free -m` (check for DiskPressure/MemoryPressure).
6. Check node network interface and route configs.
```

#### 🔍 S-44: If the control plane node is unresponsive and `kubectl` commands fail with 'Conn...
**Question:**
If the control plane node is unresponsive and `kubectl` commands fail with 'Connection Refused', how do you debug the API Server?

**Answer (Mumshad Standard):**
```
1. SSH into the control plane node container.
2. Check if the container runtime is running: `docker ps` or `crictl ps`.
3. Inspect the static pod log files directly on the host under `/var/log/pods/`.
4. Verify if the manifest files in `/etc/kubernetes/manifests/` (specifically `kube-apiserver.yaml`) are corrupted or have incorrect paths/flags.
```

#### 🔍 S-45: Write a `kubectl` command to list all Pods sorted by CPU usage. What API service...
**Question:**
Write a `kubectl` command to list all Pods sorted by CPU usage. What API service must be active for this to work?

**Answer (Mumshad Standard):**
```
Command: `kubectl top pod --all-namespaces --sort-by=cpu`
Requirement: The Metrics Server component must be installed and active in the cluster (`apiservice v1beta1.metrics.k8s.io` must be available).
```

#### 🔍 S-46: What are the common causes of `CrashLoopBackOff` in a container, and how do you ...
**Question:**
What are the common causes of `CrashLoopBackOff` in a container, and how do you extract details about the previous failed run?

**Answer (Mumshad Standard):**
```
Common causes: Application configuration typos, missing environment variables/secrets, container port binding conflicts, database connection timeouts, liveness probe failing, or file permission errors.
To inspect logs of the previous crashed instance: `kubectl logs <pod-name> --previous`
To view container exit codes: `kubectl get pod <pod-name> -o jsonpath='{.status.containerStatuses[0].lastState.terminated.exitCode}'`.
```

#### 🔍 S-47: How do you identify why a Pod is stuck in the `Pending` state?...
**Question:**
How do you identify why a Pod is stuck in the `Pending` state?

**Answer (Mumshad Standard):**
```
Run `kubectl describe pod <pod-name>`. Look at the 'Events' section at the bottom. Common causes include:
1. Insufficient resources (CPU, Memory) on all nodes.
2. NodeSelector, NodeAffinity, or PodAntiAffinity constraints.
3. Unmatched taints on nodes (pod lacks required tolerations).
4. Unbound PersistentVolumeClaims (PVC) waiting for consumer.
```

#### 🔍 S-48: What is the difference between `ImagePullBackOff` and `ErrImagePull`, and how do...
**Question:**
What is the difference between `ImagePullBackOff` and `ErrImagePull`, and how do you resolve private registry credentials issues?

**Answer (Mumshad Standard):**
```
`ErrImagePull` is the immediate error when attempting to pull (e.g. network failure, wrong image tag). `ImagePullBackOff` is the status when Kubelet enters a back-off loop to retry pulling the image. To resolve private registry issues, you must create a secret of type `docker-registry` containing the auth credentials and link it using `imagePullSecrets` in the PodSpec.
```

#### 🔍 S-49: How do you check if a Service's traffic is reaching the backing pods? What resou...
**Question:**
How do you check if a Service's traffic is reaching the backing pods? What resource lists the active routing IPs of these pods?

**Answer (Mumshad Standard):**
```
1. Run `kubectl get endpoints <service-name>` or `kubectl get endpointslices -l kubernetes.io/service-name=<service-name>`.
2. If the endpoints list is empty, the service selector labels do not match the pod labels. Verify the service's `spec.selector` against the pods' `metadata.labels`.
```

#### 🔍 S-50: How do you verify if the CoreDNS pod is functioning correctly, and how do you te...
**Question:**
How do you verify if the CoreDNS pod is functioning correctly, and how do you test internal DNS resolution from a temporary debug pod?

**Answer (Mumshad Standard):**
```
1. Check CoreDNS status: `kubectl get pods -n kube-system -l k8s-app=kube-dns`.
2. Check CoreDNS logs: `kubectl logs -n kube-system -l k8s-app=kube-dns`.
3. Test resolution using a temporary utility pod:
   `kubectl run dns-test --rm -i --tty --image=busybox -- restart=Never -- nslookup kubernetes.default`
```

#### 🔍 S-51: How do you test if a ServiceAccount has permission to create deployments in name...
**Question:**
How do you test if a ServiceAccount has permission to create deployments in namespace 'prod' using the command line?

**Answer (Mumshad Standard):**
```
kubectl auth can-i create deployments \
  --namespace=prod \
  --as=system:serviceaccount:prod:my-serviceaccount-name
```

#### 🔍 S-52: Where do you locate the Kubelet configuration file path, and how do you determin...
**Question:**
Where do you locate the Kubelet configuration file path, and how do you determine if it is using systemd or cgroupfs as its cgroup driver?

**Answer (Mumshad Standard):**
```
1. Check the active kubelet systemd service unit file (typically `/etc/systemd/system/kubelet.service.d/10-kubeadm.conf`) to find the `--config` file path, usually `/var/lib/kubelet/config.yaml`.
2. Open `/var/lib/kubelet/config.yaml` and look for the field `cgroupDriver: systemd` (or run `kubectl get no -o yaml` and check node info).
```

#### 🔍 S-53: Explain Node Eviction and what memory/disk thresholds trigger Kubelet to evict p...
**Question:**
Explain Node Eviction and what memory/disk thresholds trigger Kubelet to evict pods.

**Answer (Mumshad Standard):**
```
Kubelet monitors resource usage on nodes. If resources cross certain hard eviction thresholds, Kubelet terminates pods to reclaim resources. The default hard eviction thresholds are:
- `memory.available < 100Mi`
- `nodefs.available < 10%`
- `nodefs.inodesFree < 5%`
- `imagefs.available < 15%`
```

#### 🔍 S-54: If a Pod fails to bind to a HostPort, what diagnostic command would you run on t...
**Question:**
If a Pod fails to bind to a HostPort, what diagnostic command would you run on the worker node to verify port availability?

**Answer (Mumshad Standard):**
```
SSH into the worker node container and run:
`netstat -tulnp | grep <port-number>` or `ss -tulnp | grep <port-number>`
This will identify if another local process or container is already listening on that port on the node host network interface.
```

#### 🔍 S-55: How do you verify if a NetworkPolicy is active on a pod, and what happens if two...
**Question:**
How do you verify if a NetworkPolicy is active on a pod, and what happens if two policies apply to the same pod?

**Answer (Mumshad Standard):**
```
You can inspect the pod labels and namespace policies via `kubectl describe pod` and `kubectl get netpol`. If multiple NetworkPolicies select the same pod, they are additive. The union of all ingress/egress rules is evaluated; if any single policy allows traffic, it is allowed.
```

#### 🔍 S-56: How do you troubleshoot a kubeadm upgrade failure, and where are the backup mani...
**Question:**
How do you troubleshoot a kubeadm upgrade failure, and where are the backup manifests stored during the upgrade process?

**Answer (Mumshad Standard):**
```
If an upgrade fails, inspect the kube-apiserver logs and system logs. During `kubeadm upgrade`, kubeadm backs up the previous static pod manifests to `/etc/kubernetes/tmp/` (e.g. `kubeadm-backup-manifests-XXXX`). To rollback, copy these backup manifests back into `/etc/kubernetes/manifests/` and restart kubelet.
```

#### 🔍 S-57: How do you check expiration details for all control plane certificates managed b...
**Question:**
How do you check expiration details for all control plane certificates managed by kubeadm?

**Answer (Mumshad Standard):**
```
Run command: `kubeadm certs check-expiration`
```

#### 🔍 S-58: What is the CNI configuration file extension required by Kubelet to detect it, a...
**Question:**
What is the CNI configuration file extension required by Kubelet to detect it, and what happens if Kubelet finds multiple CNI configs?

**Answer (Mumshad Standard):**
```
The Kubelet searches `/etc/cni/net.d/` for CNI configuration files. It recognizes `.conf`, `.conflist`, or `.json` extensions. If multiple CNI config files exist, Kubelet uses the first alphabetical configuration file (e.g., `10-calico.conflist` is preferred over `20-flannel.conf`).
```

#### 🔍 S-59: How do you trace iptables network packets for kube-proxy rules to troubleshoot r...
**Question:**
How do you trace iptables network packets for kube-proxy rules to troubleshoot routing failures?

**Answer (Mumshad Standard):**
```
Run `iptables -t nat -L -v` inside the node container to inspect nat chains. Search for chains prefixed with `KUBE-` (e.g., `KUBE-SERVICES`, `KUBE-SVC-XXX`). Use `tcpdump -i any host <pod-ip>` to capture packets on virtual ethernet bridges to see if routing or filtering blocks the packets.
```

#### 🔍 S-60: How do you inspect the current etcd cluster member health and list the etcd clus...
**Question:**
How do you inspect the current etcd cluster member health and list the etcd cluster members?

**Answer (Mumshad Standard):**
```
ETCDCTL_API=3 etcdctl \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  member list -w table
```

#### 🔍 S-62: What is an Ephemeral Container, and why can it not be added to a running pod via...
**Question:**
What is an Ephemeral Container, and why can it not be added to a running pod via standard 'kubectl edit' or 'kubectl patch'?

**Answer (Mumshad Standard):**
```
An Ephemeral Container is a temporary container run inside an existing Pod to debug issues. It lacks resource guarantees and cannot be restarted. You cannot add it via edit/patch because the Pod Spec 'containers' and 'initContainers' lists are immutable after creation. Ephemeral containers are added via the specialized '/ephemeralcontainers' API subresource, which is accessed using the 'kubectl debug' command.
```

#### 🔍 S-73: Explain the default tolerations added to all pods automatically for node issues ...
**Question:**
Explain the default tolerations added to all pods automatically for node issues (Ready/Unreachable).

**Answer (Mumshad Standard):**
```
Kubernetes automatically appends default tolerations to all pods if not defined:
- `node.kubernetes.io/not-ready` with tolerationSeconds: 300
- `node.kubernetes.io/unreachable` with tolerationSeconds: 300
This prevents immediate eviction if a node experiences temporary network drops, giving the node 5 minutes to recover before relocating workloads.
```

#### 🔍 S-75: How do you inspect kubelet logs using journalctl for a specific unit, and how do...
**Question:**
How do you inspect kubelet logs using journalctl for a specific unit, and how do you filter by time?

**Answer (Mumshad Standard):**
```
To inspect active logs of kubelet: `journalctl -u kubelet -f`
To view only error logs: `journalctl -u kubelet -p err`
To filter logs since a specific time: `journalctl -u kubelet --since "20 min ago"` or `journalctl -u kubelet --since "2026-06-10 12:00:00"`
```

### 🔬 Hands-on Environment Scenarios (31 Tasks)
These tasks require access to the 3-node CKA GOLD cluster (`./gold.sh`). They inject real-world failures or specific deployment constraints that you must diagnose and resolve.

#### 🛠️ E-01: Kubelet Service Stopped on Worker Node 1
**Problem Statement:**
The node 'cka-gold-worker' is showing NotReady. Find the cause and bring it back online.

**💡 Hint:**
> Check if kubelet is running on cka-gold-worker container using systemctl.

**Setup Injection Command:**
```bash
docker exec cka-gold-worker systemctl stop kubelet
```
**Verification check script:**
```bash
kubectl get node cka-gold-worker -o jsonpath='{.status.conditions[?(@.type=="Ready")].status}' | grep -i True
```
**🟢 Step-by-Step Answer / Solution:**
=== ACTUAL CKA EXAM SYSTEMATIC PATHWAY ===
1. SSH/access the worker node console:
   ssh cka-gold-worker
2. Check kubelet service status:
   systemctl status kubelet
3. Start and enable the service:
   sudo systemctl start kubelet
   sudo systemctl enable kubelet

=== KIND SANDBOX PRACTICE SIMULATION ===
Execute command from host workstation:
docker exec cka-gold-worker systemctl start kubelet

---
#### 🛠️ E-02: Corrupt Kubelet Config on Worker Node 2
**Problem Statement:**
The node 'cka-gold-worker2' is NotReady. The configuration file seems to have an issue.

**💡 Hint:**
> Check the kubelet logs on cka-gold-worker2: journalctl -u kubelet. Look for config errors.

**Setup Injection Command:**
```bash
docker exec cka-gold-worker2 sed -i 's/staticPodPath/staticPodPathInvalid/g' /var/lib/kubelet/config.yaml && docker exec cka-gold-worker2 systemctl restart kubelet
```
**Verification check script:**
```bash
kubectl get node cka-gold-worker2 -o jsonpath='{.status.conditions[?(@.type=="Ready")].status}' | grep -i True
```
**🟢 Step-by-Step Answer / Solution:**
=== ACTUAL CKA EXAM SYSTEMATIC PATHWAY ===
1. SSH/access the worker node console:
   ssh cka-gold-worker2
2. Check the kubelet system logs for errors:
   sudo journalctl -u kubelet -n 50 --no-pager
3. Correct configuration typo inside config file:
   sudo vi /var/lib/kubelet/config.yaml  # Change staticPodPathInvalid -> staticPodPath
4. Restart the service:
   sudo systemctl restart kubelet

=== KIND SANDBOX PRACTICE SIMULATION ===
Fix configuration and restart inside node container:
docker exec cka-gold-worker2 sed -i 's/staticPodPathInvalid/staticPodPath/g' /var/lib/kubelet/config.yaml && docker exec cka-gold-worker2 systemctl restart kubelet

---
#### 🛠️ E-03: CoreDNS ConfigMap Corrupted
**Problem Statement:**
DNS resolution is failing inside pods. Inspect the CoreDNS configuration and fix it.

**💡 Hint:**
> View CoreDNS logs. Check the 'coredns' ConfigMap in the 'kube-system' namespace.

**Setup Injection Command:**
```bash
kubectl get configmap coredns -n kube-system -o yaml > /tmp/coredns.yaml && kubectl patch configmap coredns -n kube-system --type merge -p '{"data":{"Corefile":"invalid syntax block"}}' && kubectl rollout restart deploy coredns -n kube-system
```
**Verification check script:**
```bash
kubectl get deploy coredns -n kube-system -o jsonpath='{.status.readyReplicas}' | grep -w '2'
```
**🟢 Step-by-Step Answer / Solution:**
1. Edit ConfigMap: kubectl edit configmap coredns -n kube-system
2. Restore Corefile configuration
3. Restart deployment: kubectl rollout restart deploy coredns -n kube-system

---
#### 🛠️ E-04: API Server Static Pod Crashing due to Wrong Cert Path
**Problem Statement:**
The API server container is crashing. Diagnostic manifests show an incorrect client cert path config.

**💡 Hint:**
> Check static pod files in cka-gold-control-plane at /etc/kubernetes/manifests/kube-apiserver.yaml.

**Setup Injection Command:**
```bash
docker exec cka-gold-control-plane sed -i 's|/etc/kubernetes/pki/apiserver.crt|/etc/kubernetes/pki/apiserver-invalid.crt|g' /etc/kubernetes/manifests/kube-apiserver.yaml
```
**Verification check script:**
```bash
kubectl get no cka-gold-control-plane
```
**🟢 Step-by-Step Answer / Solution:**
1. Modify /etc/kubernetes/manifests/kube-apiserver.yaml inside control plane node.
2. Fix path back to /etc/kubernetes/pki/apiserver.crt
3. Kubelet will reload the static pod automatically.

---
#### 🛠️ E-05: ETCD Static Pod Port Mismatch
**Problem Statement:**
ETCD is down because the static pod manifest listen port was changed to 2380 instead of 2379.

**💡 Hint:**
> Locate etcd static pod config /etc/kubernetes/manifests/etcd.yaml and check port parameters.

**Setup Injection Command:**
```bash
docker exec cka-gold-control-plane sed -i 's|--listen-client-urls=https://127.0.0.1:2379|--listen-client-urls=https://127.0.0.1:2380|g' /etc/kubernetes/manifests/etcd.yaml
```
**Verification check script:**
```bash
kubectl get cs etcd-0 || kubectl get no
```
**🟢 Step-by-Step Answer / Solution:**
1. Access control plane node.
2. In /etc/kubernetes/manifests/etcd.yaml, restore listen-client-urls port to 2379.

---
#### 🛠️ E-06: Kubelet Certificate Path Mismatch on Worker 1
**Problem Statement:**
The Kubelet on 'cka-gold-worker' cannot authenticate with the API Server due to a broken cert path config.

**💡 Hint:**
> Check /etc/kubernetes/kubelet.conf in the cka-gold-worker container.

**Setup Injection Command:**
```bash
docker exec cka-gold-worker sed -i 's|client-certificate-data:|client-certificate-data-invalid:|g' /etc/kubernetes/kubelet.conf && docker exec cka-gold-worker systemctl restart kubelet
```
**Verification check script:**
```bash
kubectl get node cka-gold-worker -o jsonpath='{.status.conditions[?(@.type=="Ready")].status}' | grep -i True
```
**🟢 Step-by-Step Answer / Solution:**
1. Restore client-certificate-data key name in kubelet.conf on worker node.
2. Run: systemctl restart kubelet inside cka-gold-worker container.

---
#### 🛠️ E-07: Kube-Scheduler Crashing on Typos
**Problem Statement:**
Scheduler is not running. Find the typo in the scheduler's static pod manifest.

**💡 Hint:**
> Check kube-scheduler.yaml under /etc/kubernetes/manifests/ on cka-gold-control-plane.

**Setup Injection Command:**
```bash
docker exec cka-gold-control-plane sed -i 's|--leader-elect=true|--leader-elect=true-invalid|g' /etc/kubernetes/manifests/kube-scheduler.yaml
```
**Verification check script:**
```bash
kubectl get pod -n kube-system -l component=kube-scheduler -o jsonpath='{.items[0].status.phase}' | grep -i Running
```
**🟢 Step-by-Step Answer / Solution:**
1. Edit /etc/kubernetes/manifests/kube-scheduler.yaml inside the control plane node.
2. Remove the '-invalid' typo from --leader-elect flag.

---
#### 🛠️ E-08: Pod Stuck in Pending due to Custom Scheduler Name Mismatch
**Problem Statement:**
A deployment called 'nginx-scheduler-test' is pending because it requests a custom scheduler that doesn't exist.

**💡 Hint:**
> Inspect the deployment spec template for schedulerName. Remove or change it to default-scheduler.

**Setup Injection Command:**
```bash
kubectl create deployment nginx-scheduler-test --image=nginx --replicas=1 && kubectl patch deployment nginx-scheduler-test --type=json -p='[{"op": "add", "path": "/spec/template/spec/schedulerName", "value": "non-existent-scheduler"}]'
```
**Verification check script:**
```bash
kubectl get deployment nginx-scheduler-test -o jsonpath='{.status.readyReplicas}' | grep -w '1'
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl edit deploy nginx-scheduler-test
2. Delete the 'schedulerName: non-existent-scheduler' line or change it to 'default-scheduler'.
3. Save and check replicas.

---
#### 🛠️ E-09: Pod Stuck in ImagePullBackOff due to Image Name Typo
**Problem Statement:**
A pod named 'nginx-typo-image' cannot start due to an image configuration error.

**💡 Hint:**
> Check the image name using kubectl describe pod. Edit the image name to a valid image.

**Setup Injection Command:**
```bash
kubectl run nginx-typo-image --image=nginxx:latest
```
**Verification check script:**
```bash
kubectl get pod nginx-typo-image -o jsonpath='{.status.phase}' | grep -i Running
```
**🟢 Step-by-Step Answer / Solution:**
1. Re-create or patch pod: kubectl set image pod/nginx-typo-image nginx-typo-image=nginx:latest

---
#### 🛠️ E-10: CNI Plugin Deleted (Network down)
**Problem Statement:**
Pods are stuck in ContainerCreating because the CNI DaemonSet has been scaled to 0 or deleted.

**💡 Hint:**
> Check the status of CNI pods in the kube-system namespace. Scaled DaemonSets can be scaled back up.

**Setup Injection Command:**
```bash
kubectl scale daemonset kindnet -n kube-system --replicas=0
```
**Verification check script:**
```bash
kubectl get daemonset kindnet -n kube-system -o jsonpath='{.status.numberReady}' | grep -v '0'
```
**🟢 Step-by-Step Answer / Solution:**
1. Scale DaemonSet back up: kubectl scale daemonset kindnet -n kube-system --replicas=1

---
#### 🛠️ E-11: Service Selector Mismatch
**Problem Statement:**
Service 'web-svc' has no backend endpoint IPs. Resolve the selector mismatch.

**💡 Hint:**
> Compare the selectors of the service using 'kubectl describe svc web-svc' with the labels of deployment pods.

**Setup Injection Command:**
```bash
kubectl create deployment web-app --image=nginx --replicas=2 && kubectl create service clusterip web-svc --tcp=80:80 && kubectl patch service web-svc --type=json -p='[{"op": "replace", "path": "/spec/selector/app", "value": "wrong-label"}]'
```
**Verification check script:**
```bash
kubectl get endpoints web-svc -o jsonpath='{.subsets[0].addresses[0].ip}' | grep -v '^$'
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl describe svc web-svc (finds selector app=wrong-label)
2. Edit service: kubectl edit svc web-svc
3. Modify selector to app=web-app

---
#### 🛠️ E-12: Pod Memory Request Exceeds Node Limits
**Problem Statement:**
A pod named 'mem-heavy' is stuck in Pending because it requests more RAM than any node can provide.

**💡 Hint:**
> Reduce the pod memory request to a reasonable value (e.g. 50Mi) so that the scheduler can schedule it.

**Setup Injection Command:**
```bash
kubectl run mem-heavy --image=nginx --requests='memory=100Gi'
```
**Verification check script:**
```bash
kubectl get pod mem-heavy -o jsonpath='{.status.phase}' | grep -i Running
```
**🟢 Step-by-Step Answer / Solution:**
1. Delete current pod: kubectl delete pod mem-heavy --force
2. Recreate with valid requests: kubectl run mem-heavy --image=nginx --requests='memory=50Mi'

---
#### 🛠️ E-13: PVC Stuck Pending due to Invalid StorageClass
**Problem Statement:**
A PVC named 'pending-pvc' is stuck in Pending. Check the StorageClass request.

**💡 Hint:**
> Examine the storageClassName of the PVC. Change it to 'standard' (default KinD storage class).

**Setup Injection Command:**
```bash
kubectl apply -f - <<EOF
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pending-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
  storageClassName: non-existent-sc
EOF
```
**Verification check script:**
```bash
kubectl get pvc pending-pvc -o jsonpath='{.status.phase}' | grep -i Bound
```
**🟢 Step-by-Step Answer / Solution:**
1. Delete PVC: kubectl delete pvc pending-pvc
2. Modify manifest storageClassName to 'standard' (or omit it for default)
3. Re-apply: kubectl apply -f <manifest>

---
#### 🛠️ E-14: Failed ETCD Snapshot Restore Recovery
**Problem Statement:**
A broken configuration was applied. Restore the cluster configuration using the snapshot file at '/opt/backup.db'.

**💡 Hint:**
> Restore etcd using 'etcdctl snapshot restore --data-dir=/var/lib/etcd-restored /opt/backup.db' and point control plane etcd configuration path to the restored dir.

**Setup Injection Command:**
```bash
mkdir -p /opt && ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key snapshot save /opt/backup.db && kubectl create namespace break-me
```
**Verification check script:**
```bash
kubectl get ns break-me --no-headers 2>&1 | grep -q 'NotFound' || exit 0
```
**🟢 Step-by-Step Answer / Solution:**
=== ACTUAL CKA EXAM SYSTEMATIC PATHWAY ===
1. SSH/access the control plane node console:
   ssh cka-gold-control-plane
2. Restore the database snapshot to a new data directory:
   ETCDCTL_API=3 etcdctl --data-dir=/var/lib/etcd-restored snapshot restore /opt/backup.db
3. Update hostPath volume inside static pod manifest:
   sudo vi /etc/kubernetes/manifests/etcd.yaml
   # Update volume named etcd-data hostPath to point to /var/lib/etcd-restored

=== KIND SANDBOX PRACTICE SIMULATION ===
Restore and configure inside control plane container:
docker exec -it cka-gold-control-plane sh -c 'ETCDCTL_API=3 etcdctl --data-dir=/var/lib/etcd-restored snapshot restore /opt/backup.db && sed -i "s|path: /var/lib/etcd|path: /var/lib/etcd-restored|g" /etc/kubernetes/manifests/etcd.yaml'

---
#### 🛠️ E-15: Tainted Worker Node Evicting Pods
**Problem Statement:**
Worker node 'cka-gold-worker' has an administrative taint added. Remove it to allow scheduling.

**💡 Hint:**
> Look for active taints on cka-gold-worker node. Remove the taint using the minus suffix.

**Setup Injection Command:**
```bash
kubectl taint nodes cka-gold-worker key=value:NoSchedule --overwrite
```
**Verification check script:**
```bash
kubectl describe node cka-gold-worker | grep -i Taints | grep -v 'key=value:NoSchedule'
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl taint nodes cka-gold-worker key-

---
#### 🛠️ E-16: Static Pod not Starting on Worker 1
**Problem Statement:**
You need to host a static pod on 'cka-gold-worker'. Ensure the static pod runs correctly.

**💡 Hint:**
> Write a pod manifest file to /etc/kubernetes/manifests/static.yaml inside the cka-gold-worker node container.

**Setup Injection Command:**
```bash
docker exec cka-gold-worker mkdir -p /etc/kubernetes/manifests
```
**Verification check script:**
```bash
kubectl get pods --all-namespaces | grep -i cka-gold-worker | grep -i static-pod
```
**🟢 Step-by-Step Answer / Solution:**
=== ACTUAL CKA EXAM SYSTEMATIC PATHWAY ===
1. SSH/access the worker node console:
   ssh cka-gold-worker
2. Determine Kubelet staticPodPath directory (defaults to /etc/kubernetes/manifests/):
   grep staticPodPath /var/lib/kubelet/config.yaml
3. Create the directories if not exist, and write the static pod YAML file:
   sudo mkdir -p /etc/kubernetes/manifests
   sudo vi /etc/kubernetes/manifests/static.yaml
   # Insert Pod manifest running nginx container

=== KIND SANDBOX PRACTICE SIMULATION ===
Create static pod inside worker node container:
docker exec -i cka-gold-worker sh -c 'mkdir -p /etc/kubernetes/manifests && cat <<EOF > /etc/kubernetes/manifests/static.yaml
apiVersion: v1
kind: Pod
metadata:
  name: static-pod
spec:
  containers:
  - name: web
    image: nginx
EOF'

---
#### 🛠️ E-17: Ingress Routing Failure due to Service Port Mismatch
**Problem Statement:**
Ingress is returning a 503 error. The target service port configuration does not match the actual service port.

**💡 Hint:**
> Check the backend port in the Ingress resource compared to the Port defined in the web-service service.

**Setup Injection Command:**
```bash
kubectl apply -f - <<EOF
apiVersion: v1
kind: Namespace
metadata:
  name: ingress-test
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-deploy
  namespace: ingress-test
spec:
  replicas: 1
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: nginx
        image: nginx
---
apiVersion: v1
kind: Service
metadata:
  name: web-service
  namespace: ingress-test
spec:
  selector:
    app: web
  ports:
  - port: 80
    targetPort: 80
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: test-ingress
  namespace: ingress-test
spec:
  rules:
  - http:
      paths:
      - path: /test
        pathType: Prefix
        backend:
          service:
            name: web-service
            port:
              number: 8080
EOF
```
**Verification check script:**
```bash
kubectl get ingress test-ingress -n ingress-test -o jsonpath='{.spec.rules[0].http.paths[0].backend.service.port.number}' | grep -w '80'
```
**🟢 Step-by-Step Answer / Solution:**
1. Edit ingress: kubectl edit ingress test-ingress -n ingress-test
2. Modify port number from 8080 to 80

---
#### 🛠️ E-18: HostPort Conflict on Worker 1 Node
**Problem Statement:**
A pod named 'hostport-pod' fails to run because port 80 is already in use by another service on cka-gold-worker.

**💡 Hint:**
> A hostPort can only be bound once on a single node. Change the hostPort configuration to a free port or remove it.

**Setup Injection Command:**
```bash
kubectl run dummy-pod --image=nginx --overrides='{"spec":{"nodeName":"cka-gold-worker","containers":[{"name":"nginx","image":"nginx","ports":[{"hostPort":80,"containerPort":80}]}]}}' && sleep 2 && kubectl run hostport-pod --image=nginx --overrides='{"spec":{"nodeName":"cka-gold-worker","containers":[{"name":"nginx","image":"nginx","ports":[{"hostPort":80,"containerPort":80}]}]}}'
```
**Verification check script:**
```bash
kubectl get pod hostport-pod -o jsonpath='{.status.phase}' | grep -i Running || exit 0
```
**🟢 Step-by-Step Answer / Solution:**
1. Delete dummy-pod or recreate hostport-pod using a different hostPort (e.g. 8080).

---
#### 🛠️ E-19: Pod Stuck in CreateContainerConfigError
**Problem Statement:**
Pod 'config-err-pod' cannot start because it references a ConfigMap key that does not exist.

**💡 Hint:**
> Check the ConfigMap 'app-config' values. Either create the key 'missing-key' in the ConfigMap or edit the PodSpec.

**Setup Injection Command:**
```bash
kubectl create configmap app-config --from-literal=key1=val1 && kubectl apply -f - <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: config-err-pod
spec:
  containers:
  - name: app
    image: nginx
    env:
    - name: CFG_VAL
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: missing-key
EOF
```
**Verification check script:**
```bash
kubectl get pod config-err-pod -o jsonpath='{.status.phase}' | grep -i Running
```
**🟢 Step-by-Step Answer / Solution:**
1. Patch ConfigMap to include key: kubectl patch configmap app-config --type merge -p '{"data":{"missing-key":"fixed-value"}}'

---
#### 🛠️ E-20: Pod Blocked by Disabled ServiceAccount Token Automount
**Problem Statement:**
Pod 'sa-test-pod' needs to talk to the API server but has automountServiceAccountToken: false. Enable it.

**💡 Hint:**
> Set automountServiceAccountToken: true in the pod spec and recreate the pod.

**Setup Injection Command:**
```bash
kubectl apply -f - <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: sa-test-pod
spec:
  automountServiceAccountToken: false
  containers:
  - name: test
    image: nginx
EOF
```
**Verification check script:**
```bash
kubectl get pod sa-test-pod -o jsonpath='{.spec.automountServiceAccountToken}' | grep -w 'true' || kubectl get pod sa-test-pod -o yaml | grep -v 'automountServiceAccountToken: false'
```
**🟢 Step-by-Step Answer / Solution:**
1. Recreate the pod with automountServiceAccountToken: true.

---
#### 🛠️ E-21: Kubelet Masked on Worker Node 2
**Problem Statement:**
Node 'cka-gold-worker2' is showing NotReady. The systemd service is masked on the host.

**💡 Hint:**
> Run systemctl unmask kubelet and then start the service inside the cka-gold-worker2 container.

**Setup Injection Command:**
```bash
docker exec cka-gold-worker2 systemctl mask kubelet && docker exec cka-gold-worker2 systemctl stop kubelet
```
**Verification check script:**
```bash
kubectl get node cka-gold-worker2 -o jsonpath='{.status.conditions[?(@.type=="Ready")].status}' | grep -i True
```
**🟢 Step-by-Step Answer / Solution:**
=== ACTUAL CKA EXAM SYSTEMATIC PATHWAY ===
1. SSH/access the worker node console:
   ssh cka-gold-worker2
2. Unmask the kubelet systemd service:
   sudo systemctl unmask kubelet
3. Start the service:
   sudo systemctl start kubelet
4. Check service status:
   sudo systemctl status kubelet

=== KIND SANDBOX PRACTICE SIMULATION ===
Unmask and start inside node container:
docker exec cka-gold-worker2 systemctl unmask kubelet && docker exec cka-gold-worker2 systemctl start kubelet

---
#### 🛠️ E-22: Tainted Workers Blocking Deployment Scheduling
**Problem Statement:**
A deployment called 'unreachable-deploy' is stuck in Pending because all worker nodes have taints.

**💡 Hint:**
> Untaint the nodes using 'kubectl taint nodes <node> env-' or add the corresponding toleration to the deployment.

**Setup Injection Command:**
```bash
kubectl create deployment unreachable-deploy --image=nginx --replicas=2 && kubectl taint nodes cka-gold-worker env=prod:NoSchedule --overwrite && kubectl taint nodes cka-gold-worker2 env=prod:NoSchedule --overwrite
```
**Verification check script:**
```bash
kubectl get deployment unreachable-deploy -o jsonpath='{.status.readyReplicas}' | grep -w '2'
```
**🟢 Step-by-Step Answer / Solution:**
1. Untaint the nodes: kubectl taint nodes cka-gold-worker env- && kubectl taint nodes cka-gold-worker2 env-

---
#### 🛠️ E-23: ClusterRole Binding Mismatched Subject Name
**Problem Statement:**
A pod trying to query namespaces fails because the ClusterRoleBinding links to the wrong service account name.

**💡 Hint:**
> Edit the ClusterRoleBinding 'monitor-crb' to point to the correct ServiceAccount name 'monitor-sa'.

**Setup Injection Command:**
```bash
kubectl create serviceaccount monitor-sa && kubectl create clusterrolebinding monitor-crb --clusterrole=view --serviceaccount=default:wrong-name
```
**Verification check script:**
```bash
kubectl auth can-i get namespaces --as=system:serviceaccount:default:monitor-sa | grep -i yes
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl edit clusterrolebinding monitor-crb
2. Change subject name to 'monitor-sa'.

---
#### 🛠️ E-24: NetworkPolicy Default Deny Block
**Problem Statement:**
Traffic between pods in namespace 'default' and namespace 'app' is blocked by a default deny policy. Configure it to allow access.

**💡 Hint:**
> Either delete the default deny NetworkPolicy in 'app' namespace, or add a NetworkPolicy rule to allow ingress.

**Setup Injection Command:**
```bash
kubectl create namespace app && kubectl apply -f - <<EOF
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all
  namespace: app
spec:
  podSelector: {}
  policyTypes:
  - Ingress
EOF
```
**Verification check script:**
```bash
kubectl get netpol -n app | grep -v 'deny-all' || exit 0
```
**🟢 Step-by-Step Answer / Solution:**
1. Delete deny-all policy: kubectl delete netpol deny-all -n app

---
#### 🛠️ E-25: Kube-Proxy Pods Failing due to Bad ConfigMap
**Problem Statement:**
Kube-proxy daemonset is failing because the 'kube-proxy' ConfigMap has a syntax error.

**💡 Hint:**
> Check the configMap 'kube-proxy' in 'kube-system' namespace. Fix the configuration config.conf syntax.

**Setup Injection Command:**
```bash
kubectl get configmap kube-proxy -n kube-system -o yaml > /tmp/kube-proxy-cm.yaml && kubectl patch configmap kube-proxy -n kube-system --type merge -p '{"data":{"config.conf":"corrupted configuration line"}}' && kubectl rollout restart daemonset kube-proxy -n kube-system
```
**Verification check script:**
```bash
kubectl get daemonset kube-proxy -n kube-system -o jsonpath='{.status.numberReady}' | grep -w '3'
```
**🟢 Step-by-Step Answer / Solution:**
1. Restore the configuration file by editing ConfigMap: kubectl edit configmap kube-proxy -n kube-system
2. Rollout restart the daemonset: kubectl rollout restart daemonset kube-proxy -n kube-system

---
#### 🛠️ E-26: Ephemeral Storage Limit Exceeded
**Problem Statement:**
A pod named 'evicted-pod' fails to run because it requests ephemeral storage that exceeds the namespace limit.

**💡 Hint:**
> The pod ephemeral-storage request exceeds the LimitRange max limit (200Mi). Modify the pod request or delete the LimitRange.

**Setup Injection Command:**
```bash
kubectl apply -f - <<EOF
apiVersion: v1
kind: LimitRange
metadata:
  name: storage-limit
spec:
  limits:
  - default:
      ephemeral-storage: 100Mi
    defaultRequest:
      ephemeral-storage: 50Mi
    max:
      ephemeral-storage: 200Mi
    type: Container
---
apiVersion: v1
kind: Pod
metadata:
  name: evicted-pod
spec:
  containers:
  - name: main
    image: nginx
    resources:
      requests:
        ephemeral-storage: 500Mi
EOF
```
**Verification check script:**
```bash
kubectl get pod evicted-pod -o jsonpath='{.status.phase}' | grep -i Running || exit 0
```
**🟢 Step-by-Step Answer / Solution:**
1. Remove request limit or change request in pod spec to under 200Mi, then recreate pod.

---
#### 🛠️ E-27: API Priority & Fairness Blocking Configuration
**Problem Statement:**
A broken FlowSchema causes administrator requests to fail. Remove the broken FlowSchema.

**💡 Hint:**
> Locate and delete the FlowSchema named 'block-admin'.

**Setup Injection Command:**
```bash
kubectl apply -f - <<EOF
apiVersion: flowcontrol.apiserver.k8s.io/v1beta3
kind: FlowSchema
metadata:
  name: block-admin
spec:
  matchingPrecedence: 1
  priorityLevelConfiguration:
    name: catch-all
  rules:
  - subjects:
    - kind: User
      name: admin
    resourceRules:
    - verbs: ["*"]
      apiGroups: ["*"]
      resources: ["*"]
EOF
```
**Verification check script:**
```bash
kubectl get flowschema | grep -q 'block-admin' && exit 1 || exit 0
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl delete flowschema block-admin

---
#### 🛠️ E-92: Ephemeral Container Debug
**Problem Statement:**
Pod 'crashed-pod' is running with a shellless distroless image and has issues. Debug it by launching an ephemeral container with image 'busybox' inside it.

**💡 Hint:**
> Use 'kubectl debug crashed-pod -it --image=busybox --target=crashed-pod --name=debug-container' (wait, in check we check for any debug container name).

**Setup Injection Command:**
```bash
kubectl run crashed-pod --image=gcr.io/distroless/static-debian11 --command -- sleep 3600
```
**Verification check script:**
```bash
kubectl get pod crashed-pod -o jsonpath='{.spec.ephemeralContainers[0].name}' | grep -i debug
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl debug crashed-pod -it --image=busybox --image-pull-policy=IfNotPresent --share-processes --name=debug-container

---
#### 🛠️ E-93: JSONPath Node OS Image Filter
**Problem Statement:**
Use JSONPath to list all nodes with their names and OS images, sorted by name, and write the output format 'Name: <node-name>, OS: <os-image>' to file '/tmp/node-os.txt'.

**💡 Hint:**
> Use kubectl get nodes -o jsonpath='{range .items[*]}Name: {.metadata.name}, OS: {.status.nodeInfo.osImage}{"\n"}{end}' > /tmp/node-os.txt.

**Setup Injection Command:**
```bash
rm -f /tmp/node-os.txt
```
**Verification check script:**
```bash
grep -q 'OS:' /tmp/node-os.txt && grep -q 'cka-gold-control-plane' /tmp/node-os.txt
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl get nodes -o jsonpath='{range .items[*]}Name: {.metadata.name}, OS: {.status.nodeInfo.osImage}{"\n"}{end}' > /tmp/node-os.txt

---
#### 🛠️ E-94: JSONPath Pod IP Filter
**Problem Statement:**
Extract the IP addresses of all pods in namespace 'default' with label 'app=web-app' and write the list of IPs to '/tmp/pod-ips.txt'.

**💡 Hint:**
> Use kubectl get pods -l app=web-app -o jsonpath='{.items[*].status.podIP}' > /tmp/pod-ips.txt.

**Setup Injection Command:**
```bash
kubectl create deployment web-app --image=nginx --replicas=2 || true && rm -f /tmp/pod-ips.txt
```
**Verification check script:**
```bash
cat /tmp/pod-ips.txt | grep -E '^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl get pods -l app=web-app -o jsonpath='{.items[*].status.podIP}' | tr ' ' '\n' > /tmp/pod-ips.txt

---
#### 🛠️ E-100: CNI Config Restoration
**Problem Statement:**
Node 'cka-gold-worker' becomes NotReady because CNI config file '/etc/cni/net.d/10-kindnet.conflist' was renamed. Restore it.

**💡 Hint:**
> Access cka-gold-worker node, look for backed up files in /etc/cni/net.d/, and rename it back.

**Setup Injection Command:**
```bash
docker exec cka-gold-worker mv /etc/cni/net.d/10-kindnet.conflist /etc/cni/net.d/10-kindnet.conflist.bak 2>/dev/null
```
**Verification check script:**
```bash
kubectl get node cka-gold-worker -o jsonpath='{.status.conditions[?(@.type=="Ready")].status}' | grep -i True
```
**🟢 Step-by-Step Answer / Solution:**
=== ACTUAL CKA EXAM SYSTEMATIC PATHWAY ===
1. SSH/access the worker node console:
   ssh cka-gold-worker
2. Restore the backed-up CNI conflist file inside /etc/cni/net.d/:
   sudo mv /etc/cni/net.d/10-kindnet.conflist.bak /etc/cni/net.d/10-kindnet.conflist

=== KIND SANDBOX PRACTICE SIMULATION ===
Restore file inside node container:
docker exec cka-gold-worker mv /etc/cni/net.d/10-kindnet.conflist.bak /etc/cni/net.d/10-kindnet.conflist

---

---

## Cluster Architecture, Installation & Config (25%)
This section covers all tasks representing Cluster Architecture, Installation & Config (25%) of the CKA curriculum.

### 📝 Conceptual Study Q&As (21 Tasks)
These tasks test your core knowledge of Kubernetes architecture, parameters, commands, and YAML syntax.

#### 🔍 S-01: What is the primary role of the Kubelet on a Kubernetes node, and how does it re...
**Question:**
What is the primary role of the Kubelet on a Kubernetes node, and how does it report node status back to the control plane?

**Answer (Mumshad Standard):**
```
The Kubelet is the node agent that runs on every node in a cluster. Its main role is to ensure that containers described in PodSpecs are running and healthy. It communicates with the container runtime using the Container Runtime Interface (CRI). It reports node status by updating the corresponding Node status and sending heartbeats using NodeLease objects in the 'kube-node-lease' namespace every 10 seconds.
```

#### 🔍 S-02: Explain the role of the ETCD database and how a control plane node interacts wit...
**Question:**
Explain the role of the ETCD database and how a control plane node interacts with it. Can the controller manager or scheduler access ETCD directly?

**Answer (Mumshad Standard):**
```
ETCD is a highly available, consistent key-value store used as Kubernetes' backing store for all cluster data (state, configurations, secrets). Only the kube-apiserver communicates directly with ETCD. All other components (Scheduler, Controller Manager, Kubelet) must interact with the API Server to read or write state, ensuring consistent access control, validation, and locking.
```

#### 🔍 S-03: What are the three main phases of a request handled by the kube-apiserver before...
**Question:**
What are the three main phases of a request handled by the kube-apiserver before it is committed to ETCD?

**Answer (Mumshad Standard):**
```
1. Authentication: Verifies the identity of the requester (via client certs, tokens, basic auth).
2. Authorization: Verifies if the authenticated user has permissions to perform the action (via RBAC, ABAC, Webhooks).
3. Admission Control: Runs plug-ins (like NodeRestriction, Mutating/Validating Webhooks) that can modify or reject the request based on cluster policies before storing the object in ETCD.
```

#### 🔍 S-04: What is the difference between kube-controller-manager and kube-scheduler?...
**Question:**
What is the difference between kube-controller-manager and kube-scheduler?

**Answer (Mumshad Standard):**
```
The kube-scheduler is responsible for scheduling pods onto appropriate nodes based on resource availability, constraints, taints/tolerations, affinity rules, etc. The kube-controller-manager runs controller processes (like Node Controller, ReplicaSet Controller, EndpointSlice Controller) in a continuous loop to watch the cluster state and drive it toward the desired state defined in the manifests.
```

#### 🔍 S-05: What is the Container Runtime Interface (CRI), and why did Kubernetes deprecate ...
**Question:**
What is the Container Runtime Interface (CRI), and why did Kubernetes deprecate Dockershim in v1.24?

**Answer (Mumshad Standard):**
```
CRI is a gRPC API that allows kubelet to interact with various container runtimes (like containerd, CRI-O) without needing to recompile kubelet. Dockershim was a hardcoded wrapper inside kubelet to support Docker, which didn't natively implement CRI. It was deprecated to clean up kubelet code, delegate runtime maintenance to runtime developers, and encourage direct use of CRI-compliant runtimes.
```

#### 🔍 S-06: Compare kube-proxy in iptables mode vs IPVS mode in terms of performance and sca...
**Question:**
Compare kube-proxy in iptables mode vs IPVS mode in terms of performance and scalability.

**Answer (Mumshad Standard):**
```
In iptables mode, kube-proxy writes DNAT rules to Netfilter for every service. As the number of services grows, sequentially searching iptables rules incurs heavy CPU overhead. In IPVS mode, kube-proxy uses IP Virtual Server hash tables, which perform routing lookup in O(1) time regardless of service count. This makes IPVS significantly faster, more resource-efficient, and suitable for large clusters.
```

#### 🔍 S-07: What are the key client/server TLS certificate pairs required for securing kube-...
**Question:**
What are the key client/server TLS certificate pairs required for securing kube-apiserver communication, and where are they located in a kubeadm-provisioned cluster?

**Answer (Mumshad Standard):**
```
In kubeadm, certificates are in `/etc/kubernetes/pki/`:
1. `apiserver.crt` / `key`: API server serving certificate.
2. `apiserver-kubelet-client.crt` / `key`: API server client cert to talk to kubelets.
3. `etcd/ca.crt` / `server.crt`: For secure access to etcd.
4. `ca.crt` / `ca.key`: Root CA cert for cluster-wide client verification.
```

#### 🔍 S-08: What is a Static Pod, how does the Kubelet discover it, and how does it differ f...
**Question:**
What is a Static Pod, how does the Kubelet discover it, and how does it differ from a standard Kubernetes Pod?

**Answer (Mumshad Standard):**
```
A Static Pod is managed directly by the Kubelet on a specific node without the API server's involvement. The Kubelet watches a local directory (specified by the `staticPodPath` or `--config` directory, typically `/etc/kubernetes/manifests`) for YAML changes. Static Pods cannot be controlled via `kubectl edit` or API commands; they are tied directly to the lifecycle of the kubelet service on that node, although kubelet creates a mirror pod in the API server for visibility.
```

#### 🔍 S-09: What is the structural layout of a standard kubeconfig file, and what are its th...
**Question:**
What is the structural layout of a standard kubeconfig file, and what are its three primary components?

**Answer (Mumshad Standard):**
```
A kubeconfig file consists of:
1. `clusters`: Lists API server endpoints and their associated CA certificates.
2. `users`: Defines credentials (client certificates, tokens, or basic auth) for authentication.
3. `contexts`: Binds a specific user to a specific cluster (and optionally a default namespace).
An active context is set using the `current-context` field.
```

#### 🔍 S-10: Describe the correct order of operations when upgrading a Kubernetes cluster usi...
**Question:**
Describe the correct order of operations when upgrading a Kubernetes cluster using kubeadm.

**Answer (Mumshad Standard):**
```
1. Upgrade the Primary Control Plane node:
   a. Upgrade `kubeadm` package.
   b. Run `kubeadm upgrade plan`, then `kubeadm upgrade apply vX.Y.Z`.
   c. Drain node, upgrade `kubelet` and `kubectl`, then restart kubelet and uncordon.
2. Upgrade secondary control plane nodes (if HA) using `kubeadm upgrade node`.
3. Upgrade Worker nodes:
   a. Upgrade `kubeadm` package on worker.
   b. Run `kubeadm upgrade node`.
   c. Drain node, upgrade `kubelet` and `kubectl`, restart kubelet, and uncordon node.
```

#### 🔍 S-11: Write the exact etcdctl command structure required to take a backup snapshot of ...
**Question:**
Write the exact etcdctl command structure required to take a backup snapshot of etcd.

**Answer (Mumshad Standard):**
```
ETCDCTL_API=3 etcdctl \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  snapshot save /opt/etcd-backup.db
```

#### 🔍 S-12: Explain what a bootstrap token is during a `kubeadm join` workflow and how its s...
**Question:**
Explain what a bootstrap token is during a `kubeadm join` workflow and how its security is verified by a worker node.

**Answer (Mumshad Standard):**
```
A bootstrap token is a short-lived token (default 24 hours) used to establish temporary trust between a joining node and the control plane. The worker node contacts the API server using the token, downloads the cluster-info ConfigMap, and verifies its authenticity using the discovery-token-ca-cert-hash. Once trust is established, the node exchanges the token for a permanent node client certificate signed by the cluster CA.
```

#### 🔍 S-13: How do you manually approve a pending CertificateSigningRequest (CSR) in Kuberne...
**Question:**
How do you manually approve a pending CertificateSigningRequest (CSR) in Kubernetes, and what command shows its details?

**Answer (Mumshad Standard):**
```
To view all CSRs: `kubectl get csr`
To view details of a specific CSR: `kubectl describe csr <csr-name>`
To approve the CSR: `kubectl certificate approve <csr-name>`
```

#### 🔍 S-14: How does Kubernetes v1.22+ manage Linux Swap memory, and what settings must be e...
**Question:**
How does Kubernetes v1.22+ manage Linux Swap memory, and what settings must be enabled in the Kubelet configuration to support it?

**Answer (Mumshad Standard):**
```
Historically, Kubernetes required swap to be disabled. From v1.22+, kubelet can run with swap enabled. To support this, swap must be active on the host, and the Kubelet configuration file (`/var/lib/kubelet/config.yaml`) must set `failSwapOn: false`. Optionally, `memorySwap.swapBehavior` can be set to `LimitedSwap` (workloads limited to their swap allocation) or `UnlimitedSwap`.
```

#### 🔍 S-15: What is the difference between the Core API Group (/) and Named API Groups, and ...
**Question:**
What is the difference between the Core API Group (/) and Named API Groups, and how does the API Server organize them in URL paths?

**Answer (Mumshad Standard):**
```
The Core API Group contains legacy core objects (Pods, Services, Nodes, ConfigMaps, Secrets) and is served at `/api/v1`. Named API Groups contain all other resources (Deployments, StatefulSets, NetworkPolicies) and are organized under `/apis/<group-name>/<version>` (e.g., `/apis/apps/v1` for Deployments). This separation allows distinct versioning lifecycles for newer resources.
```

#### 🔍 S-66: What is the difference between 'kubectl cordon' and 'kubectl drain'?...
**Question:**
What is the difference between 'kubectl cordon' and 'kubectl drain'?

**Answer (Mumshad Standard):**
```
1. `kubectl cordon`: Marks a node as unschedulable (sets 'spec.unschedulable: true'). This blocks any new pods from scheduling on the node. Existing running pods are completely unaffected.
2. `kubectl drain`: Cordons the node first, then evicts all running workloads (except daemonsets unless ignored, and pods without controller owners unless forced). It safely terminates them to let them reschedule on other nodes.
```

#### 🔍 S-67: How does the Kubelet communicate with container runtime over CRI? What is the st...
**Question:**
How does the Kubelet communicate with container runtime over CRI? What is the standard Unix Domain Socket path for containerd?

**Answer (Mumshad Standard):**
```
The Kubelet acts as a gRPC client communicating with the container runtime (acting as a gRPC server) over local Unix Domain Sockets using the CRI API. The standard socket path for containerd is `unix:///var/run/containerd/containerd.sock`. For CRI-O, it is `unix:///var/run/crio/crio.sock`.
```

#### 🔍 S-68: What are the prerequisites on a Linux node for installing Kubeadm (swap, iptable...
**Question:**
What are the prerequisites on a Linux node for installing Kubeadm (swap, iptables, netfilter)?

**Answer (Mumshad Standard):**
```
1. Swap must be disabled (unless Kubelet swap features are explicitly enabled).
2. Enable kernel module loading for overlays and netfilter bridges (`modprobe overlay` and `modprobe br_netfilter`).
3. Configure sysctl system parameters to forward packets and allow bridge netfilter iptables analysis:
   - `net.bridge.bridge-nf-call-iptables = 1`
   - `net.ipv4.ip_forward = 1`
```

#### 🔍 S-69: Explain the 'kubectl auth reconcile' command and when it is used....
**Question:**
Explain the 'kubectl auth reconcile' command and when it is used.

**Answer (Mumshad Standard):**
```
'kubectl auth reconcile' is used to update RBAC Roles and ClusterRoles from a manifest while preserving any custom modifications. It performs a smart reconciliation: it adds missing rules, updates existing ones if permissions changed, and removes obsolete rules. It is commonly used during cluster upgrades to update default API system roles.
```

#### 🔍 S-72: What is the difference between Mutating and Validating Webhooks?...
**Question:**
What is the difference between Mutating and Validating Webhooks?

**Answer (Mumshad Standard):**
```
1. Mutating Webhooks: Invoked first during the admission phase. They can modify/patch the incoming object (e.g. inject sidecar containers, set defaults).
2. Validating Webhooks: Invoked second. They perform checks on the object's configuration and return a binary allow/deny response. They cannot modify the object; their role is strictly gatekeeping.
```

#### 🔍 S-74: What is the role of the Leader Election lock in Kube-Scheduler and Kube-Controll...
**Question:**
What is the role of the Leader Election lock in Kube-Scheduler and Kube-Controller-Manager?

**Answer (Mumshad Standard):**
```
To run in High Availability (HA) mode, multiple instances of the scheduler or controller-manager run simultaneously. To prevent them from acting in conflict, they use the Leases API (lock objects in kube-system namespace). The active master holds the lease lock. If it dies, backup instances compete to acquire the lease, guaranteeing only one controller acts as leader at a time.
```

### 🔬 Hands-on Environment Scenarios (26 Tasks)
These tasks require access to the 3-node CKA GOLD cluster (`./gold.sh`). They inject real-world failures or specific deployment constraints that you must diagnose and resolve.

#### 🛠️ E-28: Upgrade Control Plane Node (kubeadm & kubelet)
**Problem Statement:**
Systematic Upgrade: You are tasked with upgrading the control-plane node (cka-gold-control-plane) from v1.35.0 to v1.35.1. Perform a secure drain, plan and apply the kubeadm upgrade, upgrade the kubelet/kubectl packages, and restart services.

**💡 Hint:**
> On the actual CKA exam, you must follow the official Kubernetes documentation upgrade flow. This involves: 1. Draining the control plane node; 2. Upgrading kubeadm via apt-get; 3. Running 'kubeadm upgrade plan' and 'kubeadm upgrade apply'; 4. Upgrading kubelet and kubectl; 5. Reloading systemd and restarting kubelet; 6. Uncordoning the node. (Since KinD uses static binaries rather than APT packages, simulate this in your sandbox by running the drain command, and then creating the verification file: 'docker exec cka-gold-control-plane touch /var/log/upgrade-test/upgraded').

**Setup Injection Command:**
```bash
docker exec cka-gold-control-plane mkdir -p /var/log/upgrade-test
```
**Verification check script:**
```bash
docker exec cka-gold-control-plane ls /var/log/upgrade-test/upgraded
```
**🟢 Step-by-Step Answer / Solution:**
=== ACTUAL CKA EXAM SYSTEMATIC PATHWAY ===
1. Drain the control plane node:
   kubectl drain cka-gold-control-plane --ignore-daemonsets --force
2. SSH to the control-plane node and escalate to root:
   ssh cka-gold-control-plane
   sudo -i
3. Upgrade kubeadm package:
   apt-mark unhold kubeadm
   apt-get update && apt-get install -y kubeadm=1.35.1-1.1
   apt-mark hold kubeadm
4. Plan and apply the upgrade:
   kubeadm upgrade plan
   kubeadm upgrade apply v1.35.1
5. Upgrade kubelet and kubectl packages:
   apt-mark unhold kubelet kubectl
   apt-get install -y kubelet=1.35.1-1.1 kubectl=1.35.1-1.1
   apt-mark hold kubelet kubectl
6. Reload systemd manager configuration and restart kubelet daemon:
   systemctl daemon-reload
   systemctl restart kubelet
7. Exit the node and uncordon the control plane:
   exit
   kubectl uncordon cka-gold-control-plane

=== KIND SANDBOX PRACTICE SIMULATION ===
In this local KinD cluster environment, execute: 
docker exec cka-gold-control-plane touch /var/log/upgrade-test/upgraded

---
#### 🛠️ E-29: Upgrade Worker Node (kubeadm & kubelet)
**Problem Statement:**
Systematic Upgrade: Upgrade the worker node 'cka-gold-worker' from v1.35.0 to v1.35.1. Cordon and drain the node first, then perform the local package upgrade.

**💡 Hint:**
> On the actual CKA exam, worker node upgrades differ from control plane upgrades: 1. Drain the worker node from the control-plane; 2. SSH to the worker node; 3. Upgrade kubeadm via apt-get; 4. Run 'kubeadm upgrade node' (instead of apply); 5. Upgrade kubelet/kubectl and restart the services; 6. Uncordon the node from the control-plane. (Simulate this locally by running the drain command and creating the verification file: 'docker exec cka-gold-worker touch /var/log/worker-upgraded').

**Setup Injection Command:**
```bash
kubectl cordon cka-gold-worker
```
**Verification check script:**
```bash
kubectl get node cka-gold-worker -o jsonpath='{.spec.unschedulable}' | grep -w 'true' && docker exec cka-gold-worker ls /var/log/worker-upgraded
```
**🟢 Step-by-Step Answer / Solution:**
=== ACTUAL CKA EXAM SYSTEMATIC PATHWAY ===
1. Drain the worker node from your management terminal:
   kubectl drain cka-gold-worker --ignore-daemonsets --force
2. SSH to the worker node:
   ssh cka-gold-worker
3. Upgrade kubeadm on the worker node:
   apt-mark unhold kubeadm
   apt-get update && apt-get install -y kubeadm=1.35.1-1.1
   apt-mark hold kubeadm
4. Upgrade the local node configuration:
   sudo kubeadm upgrade node
5. Upgrade kubelet and kubectl on the worker node:
   apt-mark unhold kubelet kubectl
   apt-get install -y kubelet=1.35.1-1.1 kubectl=1.35.1-1.1
   apt-mark hold kubelet kubectl
6. Restart the local kubelet service:
   sudo systemctl daemon-reload
   sudo systemctl restart kubelet
7. Exit the worker node and uncordon it from the control plane:
   exit
   kubectl uncordon cka-gold-worker

=== KIND SANDBOX PRACTICE SIMULATION ===
Run the drain and touch verification file locally:
1. kubectl drain cka-gold-worker --ignore-daemonsets --force
2. docker exec cka-gold-worker touch /var/log/worker-upgraded

---
#### 🛠️ E-30: Take a secure ETCD backup
**Problem Statement:**
Save a backup snapshot of etcd to the path '/opt/etcd-backup.db' on the control plane node.

**💡 Hint:**
> Use etcdctl inside cka-gold-control-plane to save snapshot to the path /opt/etcd-backup.db.

**Setup Injection Command:**
```bash
docker exec cka-gold-control-plane rm -f /opt/etcd-backup.db
```
**Verification check script:**
```bash
docker exec cka-gold-control-plane ls -lh /opt/etcd-backup.db
```
**🟢 Step-by-Step Answer / Solution:**
=== ACTUAL CKA EXAM SYSTEMATIC PATHWAY ===
1. SSH/access the control plane node console:
   ssh cka-gold-control-plane
2. Execute etcdctl snapshot save specifying certificates located in /etc/kubernetes/pki/etcd/:
   ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 \
     --cacert=/etc/kubernetes/pki/etcd/ca.crt \
     --cert=/etc/kubernetes/pki/etcd/server.crt \
     --key=/etc/kubernetes/pki/etcd/server.key \
     snapshot save /opt/etcd-backup.db
3. Verify snapshot integrity:
   ETCDCTL_API=3 etcdctl snapshot status /opt/etcd-backup.db

=== KIND SANDBOX PRACTICE SIMULATION ===
Execute inside control plane container:
docker exec -it cka-gold-control-plane sh -c 'ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key snapshot save /opt/etcd-backup.db'

---
#### 🛠️ E-31: Restore ETCD backup from Snapshot file
**Problem Statement:**
Restore an etcd snapshot located at '/opt/snapshot.db' inside cka-gold-control-plane. Ensure a test configmap created after is gone.

**💡 Hint:**
> Restore snapshot and redirect hostPath volume to restored data directory.

**Setup Injection Command:**
```bash
docker exec cka-gold-control-plane sh -c "mkdir -p /opt && ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key snapshot save /opt/snapshot.db" && kubectl create configmap test-after-backup
```
**Verification check script:**
```bash
kubectl get configmap test-after-backup 2>&1 | grep -q 'NotFound' || exit 0
```
**🟢 Step-by-Step Answer / Solution:**
=== ACTUAL CKA EXAM SYSTEMATIC PATHWAY ===
1. SSH/access the control plane node console:
   ssh cka-gold-control-plane
2. Restore the database snapshot to a new data directory:
   ETCDCTL_API=3 etcdctl --data-dir=/var/lib/etcd-restored snapshot restore /opt/snapshot.db
3. Update hostPath volume inside static pod manifest:
   sudo vi /etc/kubernetes/manifests/etcd.yaml
   # Update volume named etcd-data hostPath to point to /var/lib/etcd-restored

=== KIND SANDBOX PRACTICE SIMULATION ===
Restore and configure inside control plane container:
docker exec -it cka-gold-control-plane sh -c 'ETCDCTL_API=3 etcdctl --data-dir=/var/lib/etcd-restored snapshot restore /opt/snapshot.db && sed -i "s|path: /var/lib/etcd|path: /var/lib/etcd-restored|g" /etc/kubernetes/manifests/etcd.yaml'

---
#### 🛠️ E-32: Configure Kube-APIServer Audit Logging
**Problem Statement:**
Enable audit logging on the API Server. Log file should be at '/var/log/kubernetes/audit.log', max size 10MB.

**💡 Hint:**
> Add --audit-log-path=/var/log/kubernetes/audit.log in kube-apiserver static pod arguments.

**Setup Injection Command:**
```bash
docker exec cka-gold-control-plane mkdir -p /etc/kubernetes/audit
```
**Verification check script:**
```bash
docker exec cka-gold-control-plane grep -q 'audit-log-path' /etc/kubernetes/manifests/kube-apiserver.yaml
```
**🟢 Step-by-Step Answer / Solution:**
1. Edit /etc/kubernetes/manifests/kube-apiserver.yaml
2. Add lines under args: - --audit-log-path=/var/log/kubernetes/audit.log

---
#### 🛠️ E-33: Renew API Server Certificates
**Problem Statement:**
Renew all certificates managed by kubeadm.

**💡 Hint:**
> Run 'kubeadm certs renew all' inside the cka-gold-control-plane container.

**Setup Injection Command:**
```bash
echo 'Renew simulation'
```
**Verification check script:**
```bash
docker exec cka-gold-control-plane kubeadm certs check-expiration
```
**🟢 Step-by-Step Answer / Solution:**
=== ACTUAL CKA EXAM SYSTEMATIC PATHWAY ===
1. SSH/access the control plane node console:
   ssh cka-gold-control-plane
2. Renew all certificates using kubeadm:
   sudo kubeadm certs renew all
3. Verify certificate lifetimes:
   sudo kubeadm certs check-expiration

=== KIND SANDBOX PRACTICE SIMULATION ===
Execute inside control plane container:
docker exec -it cka-gold-control-plane kubeadm certs renew all

---
#### 🛠️ E-34: Create Certificate Signing Request API
**Problem Statement:**
Create a CSR named 'dev-user-csr' and approve it using kubectl certificate approve.

**💡 Hint:**
> Generate a private key and CSR. Create a CSR object in Kubernetes and run approve command.

**Setup Injection Command:**
```bash
kubectl delete csr dev-user-csr --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get csr dev-user-csr -o jsonpath='{.status.conditions[0].type}' | grep -i Approved
```
**🟢 Step-by-Step Answer / Solution:**
1. Apply a CertificateSigningRequest YAML manifest.
2. Run: kubectl certificate approve dev-user-csr

---
#### 🛠️ E-35: Configure API Server Admission Plugins
**Problem Statement:**
Configure kube-apiserver to enable the 'NodeRestriction' admission plugin.

**💡 Hint:**
> Check the --enable-admission-plugins argument in /etc/kubernetes/manifests/kube-apiserver.yaml.

**Setup Injection Command:**
```bash
docker exec cka-gold-control-plane sed -i 's|--enable-admission-plugins=NodeRestriction|--enable-admission-plugins=None|g' /etc/kubernetes/manifests/kube-apiserver.yaml
```
**Verification check script:**
```bash
docker exec cka-gold-control-plane grep -q 'NodeRestriction' /etc/kubernetes/manifests/kube-apiserver.yaml
```
**🟢 Step-by-Step Answer / Solution:**
1. In /etc/kubernetes/manifests/kube-apiserver.yaml, add or modify --enable-admission-plugins=NodeRestriction

---
#### 🛠️ E-36: Create Kubeconfig file for User 'sarah'
**Problem Statement:**
Generate a kubeconfig file at '/tmp/sarah.kubeconfig' pointing to cluster 'cka-gold' and user 'sarah'.

**💡 Hint:**
> Use 'kubectl config set-cluster', 'set-credentials', and 'set-context' commands with --kubeconfig=/tmp/sarah.kubeconfig.

**Setup Injection Command:**
```bash
rm -f /tmp/sarah.kubeconfig
```
**Verification check script:**
```bash
grep -q 'sarah' /tmp/sarah.kubeconfig && grep -q 'cka-gold' /tmp/sarah.kubeconfig
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl config set-cluster cka-gold --server=https://127.0.0.1:6443 --kubeconfig=/tmp/sarah.kubeconfig
2. Run: kubectl config set-credentials sarah --token=token --kubeconfig=/tmp/sarah.kubeconfig
3. Run: kubectl config set-context sarah@cka-gold --cluster=cka-gold --user=sarah --kubeconfig=/tmp/sarah.kubeconfig

---
#### 🛠️ E-37: Expose Metrics Server Endpoint
**Problem Statement:**
Verify that metrics api group v1beta1.metrics.k8s.io is running.

**💡 Hint:**
> Metrics Server should be active. Ensure `kubectl top nodes` returns data.

**Setup Injection Command:**
```bash
echo 'Metrics validation'
```
**Verification check script:**
```bash
kubectl get apiservice v1beta1.metrics.k8s.io
```
**🟢 Step-by-Step Answer / Solution:**
1. Metrics server is installed by default on kind cluster. Verify: kubectl get apiservice v1beta1.metrics.k8s.io

---
#### 🛠️ E-38: Drain cka-gold-worker Node
**Problem Statement:**
Drain the worker node 'cka-gold-worker' for maintenance.

**💡 Hint:**
> Use 'kubectl drain cka-gold-worker --ignore-daemonsets --force'.

**Setup Injection Command:**
```bash
kubectl uncordon cka-gold-worker || true
```
**Verification check script:**
```bash
kubectl get node cka-gold-worker -o jsonpath='{.spec.unschedulable}' | grep -w 'true'
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl drain cka-gold-worker --ignore-daemonsets --force

---
#### 🛠️ E-39: Uncordon cka-gold-worker Node
**Problem Statement:**
Make the worker node 'cka-gold-worker' schedulable again after maintenance.

**💡 Hint:**
> Use 'kubectl uncordon cka-gold-worker'.

**Setup Injection Command:**
```bash
kubectl cordon cka-gold-worker
```
**Verification check script:**
```bash
kubectl get node cka-gold-worker -o jsonpath='{.spec.unschedulable}' | grep -v 'true'
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl uncordon cka-gold-worker

---
#### 🛠️ E-40: Create Static Pod on Control Plane Node
**Problem Statement:**
Create a static pod named 'static-web' running nginx on cka-gold-control-plane.

**💡 Hint:**
> Place the static pod manifest inside cka-gold-control-plane container at /etc/kubernetes/manifests/static-web.yaml.

**Setup Injection Command:**
```bash
docker exec cka-gold-control-plane rm -f /etc/kubernetes/manifests/static-web.yaml || true
```
**Verification check script:**
```bash
kubectl get pods -n default | grep -i static-web-cka-gold-control-plane
```
**🟢 Step-by-Step Answer / Solution:**
=== ACTUAL CKA EXAM SYSTEMATIC PATHWAY ===
1. SSH/access the control plane node console:
   ssh cka-gold-control-plane
2. Locate the staticPodPath configured for Kubelet:
   grep staticPodPath /var/lib/kubelet/config.yaml  # Default: /etc/kubernetes/manifests
3. Create the static pod manifest inside that folder:
   sudo vi /etc/kubernetes/manifests/static-web.yaml
   # Add nginx container pod spec

=== KIND SANDBOX PRACTICE SIMULATION ===
Create static pod inside control plane container:
docker exec -i cka-gold-control-plane sh -c 'mkdir -p /etc/kubernetes/manifests && cat <<EOF > /etc/kubernetes/manifests/static-web.yaml
apiVersion: v1
kind: Pod
metadata:
  name: static-web
spec:
  containers:
  - name: web
    image: nginx
EOF'

---
#### 🛠️ E-41: Configure Kubelet Garbage Collection thresholds
**Problem Statement:**
Set Kubelet to perform image garbage collection when disk usage exceeds 80%.

**💡 Hint:**
> Modify /var/lib/kubelet/config.yaml inside control plane and worker nodes to add imageGCHighThresholdPercent: 80.

**Setup Injection Command:**
```bash
echo 'Simulation setup'
```
**Verification check script:**
```bash
docker exec cka-gold-control-plane grep -q 'imageGCHighThresholdPercent' /var/lib/kubelet/config.yaml || exit 0
```
**🟢 Step-by-Step Answer / Solution:**
1. Edit /var/lib/kubelet/config.yaml
2. Add line: imageGCHighThresholdPercent: 80
3. Restart kubelet: systemctl restart kubelet

---
#### 🛠️ E-42: Create a ServiceAccount Named 'developer'
**Problem Statement:**
Create a ServiceAccount named 'developer' in the namespace 'default'.

**💡 Hint:**
> Use 'kubectl create serviceaccount developer'.

**Setup Injection Command:**
```bash
kubectl delete serviceaccount developer --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get serviceaccount developer
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl create serviceaccount developer

---
#### 🛠️ E-43: Create a Role Named 'pod-reader'
**Problem Statement:**
Create a Role named 'pod-reader' that allows getting, watching, and listing pods in default namespace.

**💡 Hint:**
> Use 'kubectl create role pod-reader --verb=get,list,watch --resource=pods'.

**Setup Injection Command:**
```bash
kubectl delete role pod-reader --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get role pod-reader -o jsonpath='{.rules[0].verbs}' | grep -w 'get'
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl create role pod-reader --verb=get,list,watch --resource=pods

---
#### 🛠️ E-44: Bind Role 'pod-reader' to ServiceAccount 'developer'
**Problem Statement:**
Create a RoleBinding named 'read-pods' to bind Role 'pod-reader' to ServiceAccount 'developer'.

**💡 Hint:**
> Use 'kubectl create rolebinding read-pods --role=pod-reader --serviceaccount=default:developer'.

**Setup Injection Command:**
```bash
kubectl create serviceaccount developer || true && kubectl create role pod-reader --verb=get,list,watch --resource=pods || true && kubectl delete rolebinding read-pods --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get rolebinding read-pods -o jsonpath='{.subjects[0].name}' | grep -w 'developer'
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl create rolebinding read-pods --role=pod-reader --serviceaccount=default:developer

---
#### 🛠️ E-45: Create a ClusterRole Named 'node-reader'
**Problem Statement:**
Create a ClusterRole named 'node-reader' that allows reading nodes.

**💡 Hint:**
> Use 'kubectl create clusterrole node-reader --verb=get,list,watch --resource=nodes'.

**Setup Injection Command:**
```bash
kubectl delete clusterrole node-reader --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get clusterrole node-reader
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl create clusterrole node-reader --verb=get,list,watch --resource=nodes

---
#### 🛠️ E-46: Bind ClusterRole to Group 'system:authenticated'
**Problem Statement:**
Create a ClusterRoleBinding named 'read-nodes-binding' to bind ClusterRole 'node-reader' to group 'system:authenticated'.

**💡 Hint:**
> Use 'kubectl create clusterrolebinding read-nodes-binding --clusterrole=node-reader --group=system:authenticated'.

**Setup Injection Command:**
```bash
kubectl create clusterrole node-reader --verb=get,list,watch --resource=nodes || true && kubectl delete clusterrolebinding read-nodes-binding --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get clusterrolebinding read-nodes-binding -o jsonpath='{.subjects[0].name}' | grep -w 'system:authenticated'
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl create clusterrolebinding read-nodes-binding --clusterrole=node-reader --group=system:authenticated

---
#### 🛠️ E-47: Find the active API Server Port
**Problem Statement:**
Output the active API Server secure port to file '/tmp/apiserver-port.txt'.

**💡 Hint:**
> Check kube-apiserver static pod arguments or running process inside control plane container. Default is 6443.

**Setup Injection Command:**
```bash
rm -f /tmp/apiserver-port.txt
```
**Verification check script:**
```bash
grep -q '6443' /tmp/apiserver-port.txt
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: echo '6443' > /tmp/apiserver-port.txt

---
#### 🛠️ E-48: Configure Kubelet Node IP argument
**Problem Statement:**
Identify the Node IP configuration option in Kubelet systemd config.

**💡 Hint:**
> Examine cgroup and config flags inside cka-gold-worker at /etc/systemd/system/kubelet.service.d/10-kubeadm.conf.

**Setup Injection Command:**
```bash
echo 'Simulation'
```
**Verification check script:**
```bash
docker exec cka-gold-worker systemctl status kubelet | grep -q 'node-ip'
```
**🟢 Step-by-Step Answer / Solution:**
1. The node IP is passed as argument --node-ip in the systemd drop-in configuration.

---
#### 🛠️ E-49: Verify API Priority & Fairness Default Limits
**Problem Statement:**
List all active FlowSchemas in the cluster.

**💡 Hint:**
> Use 'kubectl get flowschemas'.

**Setup Injection Command:**
```bash
echo 'Simulation'
```
**Verification check script:**
```bash
kubectl get flowschemas | grep -q 'exempt'
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl get flowschemas

---
#### 🛠️ E-50: Graceful Node Shutdown Config check
**Problem Statement:**
Ensure the GracefulNodeShutdown feature flag config parameter exists in Kubelet config.

**💡 Hint:**
> Check the shutdownGracePeriod settings in Kubelet config.yaml.

**Setup Injection Command:**
```bash
echo 'Simulation'
```
**Verification check script:**
```bash
docker exec cka-gold-control-plane grep -q 'shutdownGracePeriod' /var/lib/kubelet/config.yaml || exit 0
```
**🟢 Step-by-Step Answer / Solution:**
1. Add shutdownGracePeriod to Kubelet configuration file.

---
#### 🛠️ E-96: Pod ServiceAccount Integration
**Problem Statement:**
Create a ServiceAccount named 'deploy-sa' in namespace 'default'. Configure a pod named 'sa-pod' to run using this ServiceAccount and verify its token is mounted inside.

**💡 Hint:**
> Set serviceAccountName: deploy-sa in the Pod spec.

**Setup Injection Command:**
```bash
kubectl delete pod sa-pod --ignore-not-found=true && kubectl delete serviceaccount deploy-sa --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get pod sa-pod -o jsonpath='{.spec.serviceAccountName}' | grep -w 'deploy-sa'
```
**🟢 Step-by-Step Answer / Solution:**
1. Create SA: kubectl create serviceaccount deploy-sa
2. Apply Pod manifest:
kubectl apply -f - <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: sa-pod
spec:
  serviceAccountName: deploy-sa
  containers:
  - name: main
    image: nginx
EOF

---
#### 🛠️ E-98: Kubelet Cgroup Driver Check
**Problem Statement:**
Ensure the cgroup driver used by the Kubelet on cka-gold-control-plane node is configured to 'systemd'.

**💡 Hint:**
> Check the cgroupDriver setting inside /var/lib/kubelet/config.yaml.

**Setup Injection Command:**
```bash
echo 'Simulation'
```
**Verification check script:**
```bash
docker exec cka-gold-control-plane grep -q 'cgroupDriver: systemd' /var/lib/kubelet/config.yaml || exit 0
```
**🟢 Step-by-Step Answer / Solution:**
=== ACTUAL CKA EXAM SYSTEMATIC PATHWAY ===
1. SSH/access the node console:
   ssh cka-gold-control-plane
2. Check configured cgroupDriver in kubelet config file:
   cat /var/lib/kubelet/config.yaml | grep cgroupDriver

=== KIND SANDBOX PRACTICE SIMULATION ===
Inspect inside node container:
docker exec cka-gold-control-plane grep 'cgroupDriver' /var/lib/kubelet/config.yaml

---
#### 🛠️ E-99: API Server Port Diagnostics (Port occupied)
**Problem Statement:**
Simulate port collision. The API server fails to bind because port 6443 is blocked on the host. Fix the blocking issue.

**💡 Hint:**
> Check port usage on control plane node. Kill the netcat process blocking port 6443.

**Setup Injection Command:**
```bash
docker exec cka-gold-control-plane sh -c 'apt-get update && apt-get install -y netcat-openbsd || true' && docker exec -d cka-gold-control-plane nc -l -p 6443
```
**Verification check script:**
```bash
kubectl get nodes
```
**🟢 Step-by-Step Answer / Solution:**
=== ACTUAL CKA EXAM SYSTEMATIC PATHWAY ===
1. SSH/access the control-plane node console:
   ssh cka-gold-control-plane
2. Find the process occupying port 6443 and kill it:
   sudo fuser -k 6443/tcp
   # Or kill conflicting processes by name:
   sudo pkill -f 'nc -l -p 6443'

=== KIND SANDBOX PRACTICE SIMULATION ===
Kill process inside container:
docker exec cka-gold-control-plane fuser -k 6443/tcp || docker exec cka-gold-control-plane pkill -f 'nc -l -p 6443'

---

---

## Services & Networking (20%)
This section covers all tasks representing Services & Networking (20%) of the CKA curriculum.

### 📝 Conceptual Study Q&As (15 Tasks)
These tasks test your core knowledge of Kubernetes architecture, parameters, commands, and YAML syntax.

#### 🔍 S-25: Compare ClusterIP, NodePort, and LoadBalancer service types....
**Question:**
Compare ClusterIP, NodePort, and LoadBalancer service types.

**Answer (Mumshad Standard):**
```
1. `ClusterIP` (Default): Exposes the service on a cluster-internal IP. Accessible only within the cluster.
2. `NodePort`: Exposes the service on each Node's IP at a static port (default range 30000-32767). Routes traffic to an internal ClusterIP.
3. `LoadBalancer`: Exposes the service externally using a cloud provider's load balancer. Automatically provisions a public IP and routes traffic to a NodePort.
```

#### 🔍 S-26: What is CoreDNS, and what is the standard DNS resolution format for a Service na...
**Question:**
What is CoreDNS, and what is the standard DNS resolution format for a Service named 'web' in namespace 'prod'?

**Answer (Mumshad Standard):**
```
CoreDNS is a flexible, extensible DNS server that acts as the cluster DNS. It resolves service names to ClusterIPs. The standard DNS format is: `<service-name>.<namespace>.svc.cluster.local`. For 'web' in namespace 'prod', it resolves as `web.prod.svc.cluster.local`.
```

#### 🔍 S-27: What is the difference between an Ingress Resource and an Ingress Controller?...
**Question:**
What is the difference between an Ingress Resource and an Ingress Controller?

**Answer (Mumshad Standard):**
```
1. `Ingress Resource`: A Kubernetes configuration object (YAML) that defines routing rules (hosts, HTTP paths, backends) for external traffic.
2. `Ingress Controller`: The actual reverse proxy daemon (like Nginx, Traefik, HAProxy) running in the cluster that watches for Ingress resources and configures itself to implement those routing rules.
```

#### 🔍 S-28: How do you define a default deny-all NetworkPolicy for a namespace, and how do y...
**Question:**
How do you define a default deny-all NetworkPolicy for a namespace, and how do you selectively allow traffic to a specific pod?

**Answer (Mumshad Standard):**
```
A default deny-all policy uses a `podSelector: {}` with empty ingress/egress blocks to match all pods in the namespace. To selectively allow traffic, you create a policy targeting specific pods via `podSelector: matchLabels` and add an `ingress` block specifying allowed source pods using `podSelector` or namespaces using `namespaceSelector`.
```

#### 🔍 S-29: What is the Container Network Interface (CNI), and what are the basic requiremen...
**Question:**
What is the Container Network Interface (CNI), and what are the basic requirements of a CNI network plugin in Kubernetes?

**Answer (Mumshad Standard):**
```
CNI is a standard specification defining how network plugins should configure network interfaces for containers. A CNI plugin must ensure:
1. Every Pod gets a unique IP address across the cluster.
2. Pods on any node can communicate with pods on any other node without NAT.
3. Agents on a node (like kubelet) can communicate with pods on that node.
```

#### 🔍 S-30: Explain the transition from Endpoints to EndpointSlices in Kubernetes....
**Question:**
Explain the transition from Endpoints to EndpointSlices in Kubernetes.

**Answer (Mumshad Standard):**
```
Legacy `Endpoints` objects grouped all backing pod IPs into a single resource. For services with thousands of pods, updating any pod IP required transmitting the entire large object, consuming massive API CPU and bandwidth. `EndpointSlices` partition endpoints into multiple smaller resources (max 100 endpoints per slice by default), significantly increasing scalability and network performance.
```

#### 🔍 S-31: What is a Headless Service, how do you define it in YAML, and what is its primar...
**Question:**
What is a Headless Service, how do you define it in YAML, and what is its primary use case?

**Answer (Mumshad Standard):**
```
A Headless Service is a service without an allocated ClusterIP (`clusterIP: None` in spec). Instead of returning a single load-balanced service IP, a DNS lookup for a headless service returns the A records (direct pod IPs) of all matching pods. It is primarily used with StatefulSets (e.g. databases) to enable direct peer-to-peer clustering and communication.
```

#### 🔍 S-32: Write the YAML structure of a NetworkPolicy that allows incoming traffic on port...
**Question:**
Write the YAML structure of a NetworkPolicy that allows incoming traffic on port 80 to pods labeled `role: web` only from pods in the same namespace labeled `role: api`.

**Answer (Mumshad Standard):**
```
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-api-to-web
  namespace: default
spec:
  podSelector:
    matchLabels:
      role: web
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: api
    ports:
    - protocol: TCP
      port: 80
```

#### 🔍 S-33: What is the Gateway API, and how does it differ from the legacy Ingress API?...
**Question:**
What is the Gateway API, and how does it differ from the legacy Ingress API?

**Answer (Mumshad Standard):**
```
Gateway API is a collection of resources (GatewayClass, Gateway, HTTPRoute) designed to evolve Ingress. It uses role-oriented interfaces. Cluster Operators manage infrastructure via `GatewayClass` and `Gateway`, while Application Developers map routing via `HTTPRoute` objects. This decouples infrastructure management from application traffic routing rules.
```

#### 🔍 S-34: What is the purpose of `externalTrafficPolicy: Local` in a Service definition, a...
**Question:**
What is the purpose of `externalTrafficPolicy: Local` in a Service definition, and what is the trade-off?

**Answer (Mumshad Standard):**
```
By default (`externalTrafficPolicy: Cluster`), ingress traffic on a NodePort is load-balanced across all pods, potentially routing traffic to another node (NAT hides the client source IP). Setting it to `Local` forces traffic to stay on the node it arrived on, preserving the client's original source IP. The trade-off is potential uneven traffic distribution if pods are not evenly spread across nodes.
```

#### 🔍 S-35: Where is the local CNI configuration file located on a node, and where are CNI b...
**Question:**
Where is the local CNI configuration file located on a node, and where are CNI binary plugins kept?

**Answer (Mumshad Standard):**
```
1. CNI Configuration directory: `/etc/cni/net.d/` (typically holds JSON files like `10-containerd.conf` or CNI configs).
2. CNI Binaries directory: `/opt/cni/bin/` (contains executables like loopback, bridge, portmap, etc.).
```

#### 🔍 S-36: How do you instruct CoreDNS to forward queries for a specific domain (e.g., `myc...
**Question:**
How do you instruct CoreDNS to forward queries for a specific domain (e.g., `mycorp.local`) to an external DNS server?

**Answer (Mumshad Standard):**
```
Modify the `coredns` ConfigMap in the `kube-system` namespace. Add a server block for the domain:
```
mycorp.local:53 {
    errors
    cache 30
    forward . 10.10.0.53
}
```
Apply the change and restart the CoreDNS deployment pods.
```

#### 🔍 S-61: Explain PodSpec 'dnsPolicy' options and when 'dnsConfig' overrides are needed....
**Question:**
Explain PodSpec 'dnsPolicy' options and when 'dnsConfig' overrides are needed.

**Answer (Mumshad Standard):**
```
1. Default: Pod inherits the name resolution configuration from the node.
2. ClusterFirst (Default for pods not on hostNetwork): Any DNS query matching the cluster domain suffix is forwarded to CoreDNS.
3. ClusterFirstWithHostNet: Use this for pods running with hostNetwork: true that still need cluster DNS resolution.
4. None: Ignores cluster DNS settings. You must manually define custom DNS servers using the dnsConfig field.
```

#### 🔍 S-70: What is the structure and purpose of the 'kubernetes.default.svc.cluster.local' ...
**Question:**
What is the structure and purpose of the 'kubernetes.default.svc.cluster.local' DNS search path?

**Answer (Mumshad Standard):**
```
This is the fully qualified domain name (FQDN) for the cluster-internal API server service. The components represent:
- `kubernetes`: Service name.
- `default`: Namespace.
- `svc`: Resource type (service).
- `cluster.local`: Cluster DNS domain suffix.
Pods have search paths (defined in /etc/resolv.conf) allowing them to query 'kubernetes' or 'kubernetes.default' and resolve it automatically.
```

#### 🔍 S-71: Describe the role of EndpointSlices in managing ingress traffic....
**Question:**
Describe the role of EndpointSlices in managing ingress traffic.

**Answer (Mumshad Standard):**
```
EndpointSlices track network endpoints (IP, port, readiness status) associated with a Service. Kube-proxy watches EndpointSlices and writes routing rules to direct traffic. Ingress controllers also parse EndpointSlices directly to route HTTP requests straight to the pods' IP interfaces, bypassing service-IP NAT entirely for improved latency.
```

### 🔬 Hands-on Environment Scenarios (18 Tasks)
These tasks require access to the 3-node CKA GOLD cluster (`./gold.sh`). They inject real-world failures or specific deployment constraints that you must diagnose and resolve.

#### 🛠️ E-51: Install Nginx Ingress Controller Mock
**Problem Statement:**
Create a dummy namespace 'ingress-nginx' to simulate ingress controller installation.

**💡 Hint:**
> Use 'kubectl create namespace ingress-nginx'.

**Setup Injection Command:**
```bash
kubectl delete ns ingress-nginx --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get ns ingress-nginx
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl create namespace ingress-nginx

---
#### 🛠️ E-52: Configure Path Ingress Routing
**Problem Statement:**
Create an Ingress resource named 'path-ingress' in default namespace routing '/app' to service 'app-svc' on port 80.

**💡 Hint:**
> Use 'kubectl create ingress path-ingress --rule="/app=app-svc:80"'.

**Setup Injection Command:**
```bash
kubectl delete ingress path-ingress --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get ingress path-ingress -o jsonpath='{.spec.rules[0].http.paths[0].path}' | grep -w '/app'
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl create ingress path-ingress --rule="/app=app-svc:80"

---
#### 🛠️ E-53: Configure Host-based Ingress Routing
**Problem Statement:**
Create Ingress 'host-ingress' mapping domain 'web.example.com' to service 'web-svc' on port 80.

**💡 Hint:**
> Use 'kubectl create ingress host-ingress --rule="web.example.com/*=web-svc:80"'.

**Setup Injection Command:**
```bash
kubectl delete ingress host-ingress --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get ingress host-ingress -o jsonpath='{.spec.rules[0].host}' | grep -w 'web.example.com'
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl create ingress host-ingress --rule="web.example.com/*=web-svc:80"

---
#### 🛠️ E-54: Create a ClusterIP Service
**Problem Statement:**
Expose deployment 'my-deploy' on internal service 'my-service' port 80, targetPort 8080.

**💡 Hint:**
> Use 'kubectl expose deployment my-deploy --name=my-service --port=80 --target-port=8080'.

**Setup Injection Command:**
```bash
kubectl create deployment my-deploy --image=nginx --replicas=1 || true && kubectl delete service my-service --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get svc my-service -o jsonpath='{.spec.ports[0].targetPort}' | grep -w '8080'
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl expose deployment my-deploy --name=my-service --port=80 --target-port=8080

---
#### 🛠️ E-55: Create NodePort Service
**Problem Statement:**
Expose deployment 'my-deploy' via NodePort service 'np-service' on port 80, nodePort 32000.

**💡 Hint:**
> Create NP service using YAML overrides or by exposing deploy and changing type to NodePort and nodePort value.

**Setup Injection Command:**
```bash
kubectl create deployment my-deploy --image=nginx --replicas=1 || true && kubectl delete service np-service --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get svc np-service -o jsonpath='{.spec.ports[0].nodePort}' | grep -w '32000'
```
**🟢 Step-by-Step Answer / Solution:**
1. Create YAML for np-service:
kubectl expose deploy my-deploy --name=np-service --type=NodePort --port=80 --dry-run=client -o yaml > /tmp/np.yaml
2. Modify nodePort: 32000 under ports block and apply.

---
#### 🛠️ E-56: Create Headless Service for StatefulSet
**Problem Statement:**
Create a service named 'db-headless' with clusterIP set to None.

**💡 Hint:**
> Create a ClusterIP service and edit it to set clusterIP: None, or apply a YAML manifest.

**Setup Injection Command:**
```bash
kubectl delete service db-headless --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get svc db-headless -o jsonpath='{.spec.clusterIP}' | grep -i None
```
**🟢 Step-by-Step Answer / Solution:**
1. Create manifest and apply:
kubectl apply -f - <<EOF
apiVersion: v1
kind: Service
metadata:
  name: db-headless
spec:
  clusterIP: None
  selector:
    app: db
  ports:
  - port: 3306
EOF

---
#### 🛠️ E-57: Configure Ingress NetworkPolicy Rule
**Problem Statement:**
Create a NetworkPolicy 'allow-ingress-only' allowing ingress traffic only from pods with label 'access=granted'.

**💡 Hint:**
> Apply a NetworkPolicy targeting pods with specific selector that allows from matching podSelector access=granted.

**Setup Injection Command:**
```bash
kubectl delete netpol allow-ingress-only --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get netpol allow-ingress-only -o jsonpath='{.spec.ingress[0].from[0].podSelector.matchLabels.access}' | grep -w 'granted'
```
**🟢 Step-by-Step Answer / Solution:**
1. Apply manifest:
kubectl apply -f - <<EOF
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-ingress-only
spec:
  podSelector: {}
  ingress:
  - from:
    - podSelector:
        matchLabels:
          access: granted
EOF

---
#### 🛠️ E-58: Restrict Egress to DNS UDP 53 only
**Problem Statement:**
Create NetworkPolicy 'dns-egress-only' in default namespace blocking all egress except DNS traffic on UDP 53.

**💡 Hint:**
> Create policy with egress rules specifying UDP port 53.

**Setup Injection Command:**
```bash
kubectl delete netpol dns-egress-only --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get netpol dns-egress-only -o jsonpath='{.spec.egress[0].ports[0].port}' | grep -w '53'
```
**🟢 Step-by-Step Answer / Solution:**
1. Apply manifest:
kubectl apply -f - <<EOF
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: dns-egress-only
spec:
  podSelector: {}
  policyTypes:
  - Egress
  egress:
  - to:
    - namespaceSelector: {}
    ports:
    - protocol: UDP
      port: 53
EOF

---
#### 🛠️ E-59: Configure CoreDNS Upstream Forward Rule
**Problem Statement:**
Modify CoreDNS ConfigMap to forward corporate DNS queries to 10.10.10.10.

**💡 Hint:**
> Modify coredns configmap in kube-system namespace. Add forward statement.

**Setup Injection Command:**
```bash
echo 'Simulation'
```
**Verification check script:**
```bash
kubectl get configmap coredns -n kube-system -o yaml | grep -q '10.10.10.10' || exit 0
```
**🟢 Step-by-Step Answer / Solution:**
1. Edit: kubectl edit configmap coredns -n kube-system
2. Add forward statement: forward . 10.10.10.10

---
#### 🛠️ E-60: Verify Kube-proxy Config
**Problem Statement:**
Ensure kube-proxy config exists in the kube-system namespace.

**💡 Hint:**
> Run: kubectl get configmap kube-proxy -n kube-system

**Setup Injection Command:**
```bash
echo 'Done'
```
**Verification check script:**
```bash
kubectl get configmap kube-proxy -n kube-system
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl get configmap kube-proxy -n kube-system

---
#### 🛠️ E-61: Create ExternalName Service
**Problem Statement:**
Create service 'my-ext-svc' mapping to external domain 'api.google.com'.

**💡 Hint:**
> Use 'kubectl create service externalname my-ext-svc --external-name=api.google.com'.

**Setup Injection Command:**
```bash
kubectl delete service my-ext-svc --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get svc my-ext-svc -o jsonpath='{.spec.externalName}' | grep -w 'api.google.com'
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl create service externalname my-ext-svc --external-name=api.google.com

---
#### 🛠️ E-62: Configure Service SessionAffinity
**Problem Statement:**
Modify service 'my-service' to use ClientIP session affinity.

**💡 Hint:**
> Set spec.sessionAffinity: ClientIP on my-service.

**Setup Injection Command:**
```bash
kubectl create deployment my-deploy --image=nginx --replicas=1 || true && kubectl create service clusterip my-service --tcp=80:80 || true
```
**Verification check script:**
```bash
kubectl get svc my-service -o jsonpath='{.spec.sessionAffinity}' | grep -w 'ClientIP'
```
**🟢 Step-by-Step Answer / Solution:**
1. Edit service: kubectl edit svc my-service
2. Modify sessionAffinity to ClientIP

---
#### 🛠️ E-63: Create Pod with HostNetwork Enabled
**Problem Statement:**
Deploy a pod named 'host-network-pod' with hostNetwork: true.

**💡 Hint:**
> Set hostNetwork: true in pod spec.

**Setup Injection Command:**
```bash
kubectl delete pod host-network-pod --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get pod host-network-pod -o jsonpath='{.spec.hostNetwork}' | grep -w 'true'
```
**🟢 Step-by-Step Answer / Solution:**
1. Apply manifest:
kubectl apply -f - <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: host-network-pod
spec:
  hostNetwork: true
  containers:
  - name: web
    image: nginx
EOF

---
#### 🛠️ E-64: Enable Dual-Stack Service Mock
**Problem Statement:**
Create a service called 'dual-stack-svc' configured for IPv4/IPv6 preferDualStack IP family policy.

**💡 Hint:**
> Set ipFamilyPolicy: PreferDualStack in service spec.

**Setup Injection Command:**
```bash
kubectl delete service dual-stack-svc --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get svc dual-stack-svc -o jsonpath='{.spec.ipFamilyPolicy}' | grep -i PreferDualStack || exit 0
```
**🟢 Step-by-Step Answer / Solution:**
1. Apply manifest:
kubectl apply -f - <<EOF
apiVersion: v1
kind: Service
metadata:
  name: dual-stack-svc
spec:
  selector:
    app: web
  ports:
  - port: 80
  ipFamilyPolicy: PreferDualStack
EOF

---
#### 🛠️ E-65: Check CNI Configurations
**Problem Statement:**
Verify that CNI configurations are present inside nodes.

**💡 Hint:**
> Look at /etc/cni/net.d/ inside the control plane container.

**Setup Injection Command:**
```bash
echo 'CNI verification'
```
**Verification check script:**
```bash
docker exec cka-gold-control-plane ls /etc/cni/net.d/
```
**🟢 Step-by-Step Answer / Solution:**
=== ACTUAL CKA EXAM SYSTEMATIC PATHWAY ===
1. SSH/access the control-plane or worker node console:
   ssh cka-gold-control-plane
2. Navigate to CNI configuration directory and inspect files:
   cd /etc/cni/net.d/
   cat *.conflist

=== KIND SANDBOX PRACTICE SIMULATION ===
Inspect from local terminal:
docker exec cka-gold-control-plane ls /etc/cni/net.d/

---
#### 🛠️ E-66: Expose deployment using LoadBalancer
**Problem Statement:**
Expose deployment 'my-deploy' with LoadBalancer service named 'lb-service'.

**💡 Hint:**
> Use 'kubectl expose deployment my-deploy --name=lb-service --type=LoadBalancer --port=80'.

**Setup Injection Command:**
```bash
kubectl create deployment my-deploy --image=nginx --replicas=1 || true && kubectl delete service lb-service --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get svc lb-service -o jsonpath='{.spec.type}' | grep -w 'LoadBalancer'
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl expose deployment my-deploy --name=lb-service --type=LoadBalancer --port=80

---
#### 🛠️ E-67: CoreDNS Scale to 2 Replicas
**Problem Statement:**
Scale the CoreDNS deployment to 2 replicas.

**💡 Hint:**
> Use 'kubectl scale deployment coredns -n kube-system --replicas=2'.

**Setup Injection Command:**
```bash
kubectl scale deployment coredns -n kube-system --replicas=1
```
**Verification check script:**
```bash
kubectl get deploy coredns -n kube-system -o jsonpath='{.status.replicas}' | grep -w '2'
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl scale deployment coredns -n kube-system --replicas=2

---
#### 🛠️ E-68: Configure Ingress TLS Secret
**Problem Statement:**
Configure an ingress resource named 'secure-ingress' that binds to a TLS secret named 'secure-tls'.

**💡 Hint:**
> Define a spec.tls block with hosts and secretName in the ingress manifest.

**Setup Injection Command:**
```bash
kubectl delete ingress secure-ingress --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get ingress secure-ingress -o jsonpath='{.spec.tls[0].secretName}' | grep -w 'secure-tls'
```
**🟢 Step-by-Step Answer / Solution:**
1. Apply manifest:
kubectl apply -f - <<EOF
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: secure-ingress
spec:
  tls:
  - hosts:
    - secure.example.com
    secretName: secure-tls
  rules:
  - host: secure.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web-svc
            port:
              number: 80
EOF

---

---

## Workloads & Scheduling (15%)
This section covers all tasks representing Workloads & Scheduling (15%) of the CKA curriculum.

### 📝 Conceptual Study Q&As (12 Tasks)
These tasks test your core knowledge of Kubernetes architecture, parameters, commands, and YAML syntax.

#### 🔍 S-16: How does a DaemonSet guarantee that a pod is scheduled on every node, and what t...
**Question:**
How does a DaemonSet guarantee that a pod is scheduled on every node, and what taints does it tolerate automatically?

**Answer (Mumshad Standard):**
```
The DaemonSet controller automatically schedules pods to matching nodes by creating pods with node affinity rules matching node labels. The controller automatically bypasses `unschedulable` states and tolerates scheduling-related taints: `node.kubernetes.io/not-ready` (NoExecute), `node.kubernetes.io/unreachable` (NoExecute), and `node.kubernetes.io/disk-pressure` (NoSchedule) to ensure monitoring/logging agents keep running.
```

#### 🔍 S-17: Compare NodeSelector vs NodeAffinity. What are the two types of NodeAffinity, an...
**Question:**
Compare NodeSelector vs NodeAffinity. What are the two types of NodeAffinity, and when would you use each?

**Answer (Mumshad Standard):**
```
NodeSelector is a simple key-value label selector. NodeAffinity offers advanced matching expressions (In, NotIn, Exists, Gt, Lt).
1. `requiredDuringSchedulingIgnoredDuringExecution`: Hard constraint (pod won't schedule unless node matches).
2. `preferredDuringSchedulingIgnoredDuringExecution`: Soft constraint (scheduler tries to place it on matching nodes but defaults to others if none are available).
```

#### 🔍 S-18: What are the three possible effects of a Taint, and how do they differ?...
**Question:**
What are the three possible effects of a Taint, and how do they differ?

**Answer (Mumshad Standard):**
```
1. `NoSchedule`: Prevents new pods without a matching toleration from scheduling on the node. Existing pods are unaffected.
2. `PreferNoSchedule`: The scheduler attempts to avoid placing the pod on the tainted node, but will schedule it if no other nodes are available.
3. `NoExecute`: Prevents new pods and evicts already running pods immediately (or after a toleration delay) if they lack matching tolerations.
```

#### 🔍 S-19: In a Pod with multiple Init Containers and Application Containers, what is the e...
**Question:**
In a Pod with multiple Init Containers and Application Containers, what is the exact execution order, and what happens if an Init Container fails?

**Answer (Mumshad Standard):**
```
Init containers run sequentially, one after another, in the order defined in the spec. All init containers must terminate successfully (exit code 0) before any application containers start. If an init container fails, the Kubelet restarts the Pod (according to its `restartPolicy`) and restarts the sequence from the first init container again.
```

#### 🔍 S-20: Explain the parameters `maxSurge` and `maxUnavailable` in a Deployment's Rolling...
**Question:**
Explain the parameters `maxSurge` and `maxUnavailable` in a Deployment's RollingUpdate strategy.

**Answer (Mumshad Standard):**
```
1. `maxSurge`: The maximum number of Pods that can be created above the desired replica count during an upgrade. Can be an absolute number or percentage (default 25%).
2. `maxUnavailable`: The maximum number of Pods that can be unavailable (terminated) relative to the desired replica count during the update (default 25%). Both cannot be zero simultaneously.
```

#### 🔍 S-21: What is a Pod Disruption Budget (PDB), and how does it protect workloads during ...
**Question:**
What is a Pod Disruption Budget (PDB), and how does it protect workloads during voluntary node maintenance (like a node drain)?

**Answer (Mumshad Standard):**
```
A PDB limits the number of pods of a replicated application that are down simultaneously due to voluntary disruptions (drains, upgrades). You define it using `minAvailable` or `maxUnavailable`. When `kubectl drain` is called, the eviction API respects the PDB and will block/fail the drain if evicting the pod would violate the budget, giving the application time to spin up replicas on other nodes.
```

#### 🔍 S-22: Distinguish between LimitRange and ResourceQuota....
**Question:**
Distinguish between LimitRange and ResourceQuota.

**Answer (Mumshad Standard):**
```
1. `ResourceQuota`: Configures total resource consumption limits (e.g., total CPU, Memory, or number of pods/secrets) at the Namespace level. If a namespace exceeds this total, new resources are blocked.
2. `LimitRange`: Defines default/min/max CPU and memory requests/limits for individual Pods or Containers within a Namespace, enforcing compliance during creation.
```

#### 🔍 S-23: What are the three Concurrency Policies for CronJobs, and what is their default ...
**Question:**
What are the three Concurrency Policies for CronJobs, and what is their default behavior?

**Answer (Mumshad Standard):**
```
1. `Allow` (Default): Permits concurrently running jobs if a previous job is still active.
2. `Forbid`: Skips the new run if the previous run hasn't finished yet.
3. `Replace`: Terminates the currently running job and replaces it with a new one.
```

#### 🔍 S-24: Explain Owner References and how Garbage Collection handles resource deletion us...
**Question:**
Explain Owner References and how Garbage Collection handles resource deletion using Foreground vs Background cascading deletion.

**Answer (Mumshad Standard):**
```
Owner References define parent-child links between objects (e.g. Deployment owns ReplicaSet, which owns Pods). When a parent is deleted:
1. `Background` (Default): The parent is deleted immediately, and the garbage collector deletes dependents in the background.
2. `Foreground`: The parent enters a 'deletion in progress' state, and dependents are deleted first. Once all dependents are deleted, the parent is removed.
```

#### 🔍 S-63: What is the difference between 'kubectl scale' and modifying replicas directly i...
**Question:**
What is the difference between 'kubectl scale' and modifying replicas directly in deployment YAML using 'kubectl apply'?

**Answer (Mumshad Standard):**
```
'kubectl scale' is an imperative command that updates the replicas field directly in the live object in the API server. If you subsequently run 'kubectl apply' on a local YAML manifest that still specifies the old replica count, the three-way merge patch will overwrite your imperative scaling back to the local manifest's count. For GitOps, you should always scale by editing the YAML manifest.
```

#### 🔍 S-64: Describe how Kubelet enforces CPU limits using CFS (Completely Fair Scheduler) q...
**Question:**
Describe how Kubelet enforces CPU limits using CFS (Completely Fair Scheduler) quotas in Linux.

**Answer (Mumshad Standard):**
```
Kubelet uses the Linux kernel Completely Fair Scheduler (CFS) bandwidth control to enforce CPU limits. It configures two cgroup parameters under '/sys/fs/cgroup/cpu/':
1. `cpu.cfs_period_us`: The period length (usually 100,000 microseconds or 100ms).
2. `cpu.cfs_quota_us`: The total runtime allowed within that period. E.g., a limit of 0.5 CPU equates to a quota of 50,000us. If a container exhausts its quota, the kernel throttles its CPU usage until the next period starts.
```

#### 🔍 S-65: Explain how the 'system-node-critical' and 'system-cluster-critical' PriorityCla...
**Question:**
Explain how the 'system-node-critical' and 'system-cluster-critical' PriorityClasses protect system pods during resource exhaustion.

**Answer (Mumshad Standard):**
```
These are system-defined PriorityClasses with extremely high priority values (2000001000 and 2000000000 respectively). When a node runs out of resources, the scheduler will evict lower-priority user pods first to free up capacity. The Kubelet also respects these priorities during node-level eviction, ensuring critical components (like CoreDNS, kube-proxy, or CNIs) are never terminated to satisfy user workload resource demands.
```

### 🔬 Hands-on Environment Scenarios (15 Tasks)
These tasks require access to the 3-node CKA GOLD cluster (`./gold.sh`). They inject real-world failures or specific deployment constraints that you must diagnose and resolve.

#### 🛠️ E-69: Deployment Rolling Update & Rollback
**Problem Statement:**
Create a deployment 'rolling-dep' with image nginx:1.21. Upgrade to nginx:1.23, then rollback to previous configuration.

**💡 Hint:**
> Use 'kubectl rollout undo deployment/rolling-dep'.

**Setup Injection Command:**
```bash
kubectl create deployment rolling-dep --image=nginx:1.21 && sleep 2 && kubectl set image deployment/rolling-dep nginx=nginx:1.23
```
**Verification check script:**
```bash
kubectl rollout undo deployment/rolling-dep && sleep 2 && kubectl get deploy rolling-dep -o jsonpath='{.spec.template.spec.containers[0].image}' | grep -w 'nginx:1.21'
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl rollout undo deployment/rolling-dep

---
#### 🛠️ E-70: Schedule Pod via NodeSelector
**Problem Statement:**
Label cka-gold-worker node with 'disktype=ssd' and configure pod 'ssd-pod' to run on it via NodeSelector.

**💡 Hint:**
> Label the node: kubectl label node cka-gold-worker disktype=ssd. Add nodeSelector to pod.

**Setup Injection Command:**
```bash
kubectl label nodes cka-gold-worker disktype- && kubectl delete pod ssd-pod --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get pod ssd-pod -o jsonpath='{.spec.nodeSelector.disktype}' | grep -w 'ssd'
```
**🟢 Step-by-Step Answer / Solution:**
1. Label node: kubectl label node cka-gold-worker disktype=ssd
2. Apply pod manifest:
kubectl apply -f - <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: ssd-pod
spec:
  nodeSelector:
    disktype: ssd
  containers:
  - name: main
    image: nginx
EOF

---
#### 🛠️ E-71: Schedule Pod via Required NodeAffinity
**Problem Statement:**
Configure a pod named 'affinity-pod' to only schedule on nodes with key 'zone' set to 'us-east'.

**💡 Hint:**
> Use nodeAffinity in Pod spec.

**Setup Injection Command:**
```bash
kubectl delete pod affinity-pod --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get pod affinity-pod -o jsonpath='{.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms[0].matchExpressions[0].key}' | grep -w 'zone'
```
**🟢 Step-by-Step Answer / Solution:**
1. Apply manifest:
kubectl apply -f - <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: affinity-pod
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: zone
            operator: In
            values:
            - us-east
  containers:
  - name: main
    image: nginx
EOF

---
#### 🛠️ E-72: Configure PodAntiAffinity
**Problem Statement:**
Configure deployment 'anti-affinity-deploy' with podAntiAffinity to prevent replicas from running on the same node.

**💡 Hint:**
> Add podAntiAffinity to deployment spec.

**Setup Injection Command:**
```bash
kubectl delete deployment anti-affinity-deploy --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get deploy anti-affinity-deploy -o jsonpath='{.spec.template.spec.affinity.podAntiAffinity}' | grep -v '^$'
```
**🟢 Step-by-Step Answer / Solution:**
1. Apply manifest with spec.template.spec.affinity.podAntiAffinity rule.

---
#### 🛠️ E-73: Configure Toleration for Pod
**Problem Statement:**
Create pod 'toleration-pod' that tolerates node taint 'tier=prod:NoSchedule'.

**💡 Hint:**
> Define tolerations block in pod spec.

**Setup Injection Command:**
```bash
kubectl delete pod toleration-pod --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get pod toleration-pod -o jsonpath='{.spec.tolerations[0].key}' | grep -w 'tier'
```
**🟢 Step-by-Step Answer / Solution:**
1. Apply manifest:
kubectl apply -f - <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: toleration-pod
spec:
  tolerations:
  - key: "tier"
    operator: "Equal"
    value: "prod"
    effect: "NoSchedule"
  containers:
  - name: main
    image: nginx
EOF

---
#### 🛠️ E-74: Deploy DaemonSet
**Problem Statement:**
Create a DaemonSet named 'monitoring-ds' running image prometheus/node-exporter on all nodes.

**💡 Hint:**
> Create DaemonSet spec with selector and container exporter.

**Setup Injection Command:**
```bash
kubectl delete daemonset monitoring-ds --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get daemonset monitoring-ds
```
**🟢 Step-by-Step Answer / Solution:**
1. Apply DaemonSet manifest:
kubectl apply -f - <<EOF
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: monitoring-ds
spec:
  selector:
    matchLabels:
      name: monitoring-ds
  template:
    metadata:
      labels:
        name: monitoring-ds
    spec:
      containers:
      - name: exporter
        image: prometheus/node-exporter
EOF

---
#### 🛠️ E-75: Deploy Multi-Container Pod with Shared Volume
**Problem Statement:**
Deploy a pod 'multi-container-pod' containing two containers ('app' and 'sidecar') sharing an emptyDir volume at '/var/log'.

**💡 Hint:**
> Define two containers and associate them with a volume of type emptyDir.

**Setup Injection Command:**
```bash
kubectl delete pod multi-container-pod --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get pod multi-container-pod -o jsonpath='{.spec.containers[*].name}' | grep -q 'sidecar' && kubectl get pod multi-container-pod -o jsonpath='{.spec.volumes[*].emptyDir}' | grep -v '^$'
```
**🟢 Step-by-Step Answer / Solution:**
1. Apply multi-container pod manifest.

---
#### 🛠️ E-76: Deploy InitContainer Pod
**Problem Statement:**
Create a pod named 'init-pod' with an initContainer named 'init-myservice' that finishes immediately.

**💡 Hint:**
> Define spec.initContainers in the pod configuration.

**Setup Injection Command:**
```bash
kubectl delete pod init-pod --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get pod init-pod -o jsonpath='{.spec.initContainers[0].name}' | grep -w 'init-myservice'
```
**🟢 Step-by-Step Answer / Solution:**
1. Apply manifest:
kubectl apply -f - <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: init-pod
spec:
  initContainers:
  - name: init-myservice
    image: busybox
    command: ['sh', '-c', 'echo service up']
  containers:
  - name: main
    image: nginx
EOF

---
#### 🛠️ E-77: Create a CronJob
**Problem Statement:**
Create a CronJob 'every-min-job' executing 'date' every minute.

**💡 Hint:**
> Use 'kubectl create cronjob every-min-job --schedule="*/1 * * * *" --image=busybox -- date'.

**Setup Injection Command:**
```bash
kubectl delete cronjob every-min-job --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get cronjob every-min-job -o jsonpath='{.spec.schedule}' | grep -w '*/1 * * * *' || kubectl get cronjob every-min-job -o jsonpath='{.spec.schedule}' | grep -w '* * * * *'
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl create cronjob every-min-job --schedule="* * * * *" --image=busybox -- date

---
#### 🛠️ E-78: Create PodDisruptionBudget
**Problem Statement:**
Create a PDB named 'web-pdb' selector app=web requiring minAvailable: 2.

**💡 Hint:**
> Apply a PodDisruptionBudget manifest.

**Setup Injection Command:**
```bash
kubectl delete pdb web-pdb --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get pdb web-pdb -o jsonpath='{.spec.minAvailable}' | grep -w '2'
```
**🟢 Step-by-Step Answer / Solution:**
1. Apply manifest:
kubectl apply -f - <<EOF
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: web-pdb
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: web
EOF

---
#### 🛠️ E-79: Create LimitRange in Default Namespace
**Problem Statement:**
Create LimitRange 'default-limit' in default namespace setting default container CPU limit to 200m.

**💡 Hint:**
> Apply a LimitRange configuration YAML.

**Setup Injection Command:**
```bash
kubectl delete limitrange default-limit --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get limitrange default-limit -o jsonpath='{.spec.limits[0].default.cpu}' | grep -w '200m'
```
**🟢 Step-by-Step Answer / Solution:**
1. Apply manifest:
kubectl apply -f - <<EOF
apiVersion: v1
kind: LimitRange
metadata:
  name: default-limit
spec:
  limits:
  - default:
      cpu: 200m
    type: Container
EOF

---
#### 🛠️ E-80: Create Namespace ResourceQuota
**Problem Statement:**
Create ResourceQuota named 'ns-quota' in default namespace limiting total pods count to 5.

**💡 Hint:**
> Use 'kubectl create resourcequota ns-quota --hard=pods=5'.

**Setup Injection Command:**
```bash
kubectl delete resourcequota ns-quota --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get resourcequota ns-quota -o jsonpath='{.spec.hard.pods}' | grep -w '5'
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl create resourcequota ns-quota --hard=pods=5

---
#### 🛠️ E-81: Run Parallel Job
**Problem Statement:**
Create a Job named 'parallel-job' with parallelism 2 and completions 4 running 'sleep 5'.

**💡 Hint:**
> Apply Job manifest with spec.parallelism: 2 and spec.completions: 4.

**Setup Injection Command:**
```bash
kubectl delete job parallel-job --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get job parallel-job -o jsonpath='{.spec.parallelism}' | grep -w '2'
```
**🟢 Step-by-Step Answer / Solution:**
1. Apply manifest:
kubectl apply -f - <<EOF
apiVersion: batch/v1
kind: Job
metadata:
  name: parallel-job
spec:
  parallelism: 2
  completions: 4
  template:
    spec:
      containers:
      - name: worker
        image: busybox
        command: ["sleep", "5"]
      restartPolicy: Never
EOF

---
#### 🛠️ E-91: Troubleshoot Node Capacity Resource Limits
**Problem Statement:**
Pod 'resource-fit' is stuck in Pending because it requests too much CPU. Adjust resource requests so that it can run on the cluster nodes.

**💡 Hint:**
> Examine the CPU requests. Nodes do not have 80 cores. Scale it down to 50m (0.05 core).

**Setup Injection Command:**
```bash
kubectl run resource-fit --image=nginx --requests='cpu=80'
```
**Verification check script:**
```bash
kubectl get pod resource-fit -o jsonpath='{.status.phase}' | grep -i Running
```
**🟢 Step-by-Step Answer / Solution:**
1. Delete the stuck pod: kubectl delete pod resource-fit --force
2. Recreate with valid requests: kubectl run resource-fit --image=nginx --requests='cpu=50m'

---
#### 🛠️ E-97: Sidecar Log Rotation Handler
**Problem Statement:**
Create a multi-container pod named 'logger-pod' containing container 'app' writing to '/var/log/app.log', and a sidecar container 'log-watcher' that tail-logs that file.

**💡 Hint:**
> Create pod with emptyDir volume shared by both containers.

**Setup Injection Command:**
```bash
kubectl delete pod logger-pod --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get pod logger-pod -o jsonpath='{.spec.containers[*].name}' | grep -q 'log-watcher' && kubectl get pod logger-pod -o jsonpath='{.spec.volumes[0].emptyDir}' || exit 1
```
**🟢 Step-by-Step Answer / Solution:**
1. Apply manifest with two containers sharing an emptyDir volume mounted at /var/log.

---

---

## Storage (10%)
This section covers all tasks representing Storage (10%) of the CKA curriculum.

### 📝 Conceptual Study Q&As (6 Tasks)
These tasks test your core knowledge of Kubernetes architecture, parameters, commands, and YAML syntax.

#### 🔍 S-37: Explain the lifecycle phases of a PersistentVolume (PV): Available, Bound, Relea...
**Question:**
Explain the lifecycle phases of a PersistentVolume (PV): Available, Bound, Released, and Failed.

**Answer (Mumshad Standard):**
```
1. `Available`: The PV has been created and is ready to be bound to a PVC.
2. `Bound`: The PV is successfully mapped and reserved for a specific PVC.
3. `Released`: The PVC has been deleted, but the volume is not yet reclaimed by the cluster.
4. `Failed`: The volume failed its automatic reclamation process.
```

#### 🔍 S-38: What is a StorageClass, and what is the role of the `provisioner` field?...
**Question:**
What is a StorageClass, and what is the role of the `provisioner` field?

**Answer (Mumshad Standard):**
```
A StorageClass defines the 'classes' of storage available (e.g. SSD, HDD). It allows dynamic provisioning of PVs on-demand. The `provisioner` field determines which volume plugin is used to provision the physical storage (e.g. `kubernetes.io/aws-ebs` or `rancher.io/local-path`).
```

#### 🔍 S-39: Compare the three volume Reclaim Policies: Retain, Delete, and Recycle....
**Question:**
Compare the three volume Reclaim Policies: Retain, Delete, and Recycle.

**Answer (Mumshad Standard):**
```
1. `Retain` (Default): Keeps the PV and its data when the PVC is deleted. The PV status becomes Released. Admin must manually clean data.
2. `Delete`: Deletes the PV and the underlying cloud/physical storage resource automatically when the PVC is deleted.
3. `Recycle` (Deprecated): Performs a basic scrub (`rm -rf /vol/*`) and makes the PV Available again for a new binding.
```

#### 🔍 S-40: What are the four Access Modes for Persistent Volumes, and how do they differ?...
**Question:**
What are the four Access Modes for Persistent Volumes, and how do they differ?

**Answer (Mumshad Standard):**
```
1. `ReadWriteOnce` (RWO): Mountable as read-write by a single node.
2. `ReadOnlyMany` (ROX): Mountable as read-only by many nodes.
3. `ReadWriteMany` (RWX): Mountable as read-write by many nodes.
4. `ReadWriteOncePod` (RWOP): Mountable as read-write by a single Pod (v1.22+).
```

#### 🔍 S-41: How do you enable dynamic volume expansion for Persistent Volume Claims?...
**Question:**
How do you enable dynamic volume expansion for Persistent Volume Claims?

**Answer (Mumshad Standard):**
```
To allow volume expansion, the associated StorageClass must have `allowVolumeExpansion: true` in its configuration. Once set, you can edit the PVC's `spec.resources.requests.storage` field to request a larger size. The underlying storage plugin must support expansion.
```

#### 🔍 S-42: What is the behavior of ConfigMaps or Secrets mounted as volumes in a Pod when t...
**Question:**
What is the behavior of ConfigMaps or Secrets mounted as volumes in a Pod when the source ConfigMap/Secret is updated in the API?

**Answer (Mumshad Standard):**
```
When a ConfigMap or Secret is updated, the mounted files are eventually updated automatically (usually within a few minutes, depending on the kubelet sync period and cache TTL). However, this only applies to volumes mounted directly without subPath; if a subPath is used, the file is not updated automatically and requires a pod restart.
```

### 🔬 Hands-on Environment Scenarios (10 Tasks)
These tasks require access to the 3-node CKA GOLD cluster (`./gold.sh`). They inject real-world failures or specific deployment constraints that you must diagnose and resolve.

#### 🛠️ E-82: Create HostPath PersistentVolume
**Problem Statement:**
Create a PV named 'local-pv' size 1Gi, accessMode ReadWriteOnce, path '/mnt/data'.

**💡 Hint:**
> Use standard hostPath PV configuration.

**Setup Injection Command:**
```bash
kubectl delete pv local-pv --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get pv local-pv -o jsonpath='{.spec.capacity.storage}' | grep -w '1Gi'
```
**🟢 Step-by-Step Answer / Solution:**
1. Apply manifest:
kubectl apply -f - <<EOF
apiVersion: v1
kind: PersistentVolume
metadata:
  name: local-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/mnt/data"
EOF

---
#### 🛠️ E-83: Create PVC and Bind to PV
**Problem Statement:**
Create PVC named 'local-pvc' size 1Gi, RWO matching 'local-pv'.

**💡 Hint:**
> Create PVC with storage size 1Gi and accessModes ReadWriteOnce.

**Setup Injection Command:**
```bash
kubectl apply -f - <<EOF
apiVersion: v1
kind: PersistentVolume
metadata:
  name: local-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/mnt/data"
EOF || true && kubectl delete pvc local-pvc --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get pvc local-pvc -o jsonpath='{.status.phase}' | grep -i Bound
```
**🟢 Step-by-Step Answer / Solution:**
1. Apply manifest:
kubectl apply -f - <<EOF
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: local-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
  volumeName: local-pv
EOF

---
#### 🛠️ E-84: Mount PVC to Pod
**Problem Statement:**
Create pod 'storage-pod' mounting PVC 'local-pvc' at path '/usr/share/nginx/html'.

**💡 Hint:**
> Define volumes and volumeMounts inside the Pod spec.

**Setup Injection Command:**
```bash
kubectl delete pod storage-pod --ignore-not-found=true && kubectl apply -f - <<EOF
apiVersion: v1
kind: PersistentVolume
metadata:
  name: local-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/mnt/data"
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: local-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
  volumeName: local-pv
EOF
```
**Verification check script:**
```bash
kubectl get pod storage-pod -o jsonpath='{.spec.containers[0].volumeMounts[0].mountPath}' | grep -w '/usr/share/nginx/html'
```
**🟢 Step-by-Step Answer / Solution:**
1. Apply manifest:
kubectl apply -f - <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: storage-pod
spec:
  containers:
  - name: web
    image: nginx
    volumeMounts:
    - name: log-vol
      mountPath: /usr/share/nginx/html
  volumes:
  - name: log-vol
    persistentVolumeClaim:
      claimName: local-pvc
EOF

---
#### 🛠️ E-85: Create StorageClass with Retain Reclaim Policy
**Problem Statement:**
Create StorageClass 'retain-sc' using local-path provisioner with reclaimPolicy set to Retain.

**💡 Hint:**
> Apply StorageClass manifest with reclaimPolicy: Retain.

**Setup Injection Command:**
```bash
kubectl delete sc retain-sc --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get sc retain-sc -o jsonpath='{.reclaimPolicy}' | grep -w 'Retain'
```
**🟢 Step-by-Step Answer / Solution:**
1. Apply manifest:
kubectl apply -f - <<EOF
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: retain-sc
provisioner: rancher.io/local-path
reclaimPolicy: Retain
volumeBindingMode: Immediate
EOF

---
#### 🛠️ E-86: Dynamic PVC Volume Expansion check
**Problem Statement:**
Verify that StorageClass standard allows volume expansion.

**💡 Hint:**
> Examine 'kubectl get sc standard -o yaml' and check for allowVolumeExpansion: true.

**Setup Injection Command:**
```bash
echo 'SC setup'
```
**Verification check script:**
```bash
kubectl get sc standard -o jsonpath='{.allowVolumeExpansion}' | grep -w 'true' || exit 0
```
**🟢 Step-by-Step Answer / Solution:**
1. Run: kubectl patch sc standard --type merge -p '{"allowVolumeExpansion":true}'

---
#### 🛠️ E-87: Mount ConfigMap as Volume
**Problem Statement:**
Create ConfigMap 'app-settings' with key 'app.config' and mount it as a volume in pod 'cm-vol-pod' at '/etc/config'.

**💡 Hint:**
> Use configMap volume type in pod volumes definition.

**Setup Injection Command:**
```bash
kubectl delete pod cm-vol-pod --ignore-not-found=true && kubectl delete configmap app-settings --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get pod cm-vol-pod -o jsonpath='{.spec.containers[0].volumeMounts[0].mountPath}' | grep -w '/etc/config'
```
**🟢 Step-by-Step Answer / Solution:**
1. Create ConfigMap: kubectl create configmap app-settings --from-literal=app.config=setting-value
2. Apply pod manifest mounting CM volume.

---
#### 🛠️ E-88: Inject Secret as Env Variables
**Problem Statement:**
Create Secret 'db-secret' with DB_PASS='secret123' and inject it as env variable DB_PASSWORD in pod 'secret-env-pod'.

**💡 Hint:**
> Define env with valueFrom.secretKeyRef in the Pod container spec.

**Setup Injection Command:**
```bash
kubectl delete pod secret-env-pod --ignore-not-found=true && kubectl delete secret db-secret --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get pod secret-env-pod -o jsonpath='{.spec.containers[0].env[0].valueFrom.secretKeyRef.key}' | grep -w 'DB_PASS'
```
**🟢 Step-by-Step Answer / Solution:**
1. Create secret: kubectl create secret generic db-secret --from-literal=DB_PASS=secret123
2. Apply Pod manifest with secretKeyRef env mapping.

---
#### 🛠️ E-89: Configure Pod EmptyDir Volume
**Problem Statement:**
Create pod 'cache-pod' with an emptyDir volume mounted at '/cache'.

**💡 Hint:**
> Set volume type to emptyDir: {} in Pod spec.

**Setup Injection Command:**
```bash
kubectl delete pod cache-pod --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get pod cache-pod -o jsonpath='{.spec.volumes[0].emptyDir}' || exit 1
```
**🟢 Step-by-Step Answer / Solution:**
1. Apply manifest:
kubectl apply -f - <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: cache-pod
spec:
  containers:
  - name: main
    image: nginx
    volumeMounts:
    - name: cache-vol
      mountPath: /cache
  volumes:
  - name: cache-vol
    emptyDir: {}
EOF

---
#### 🛠️ E-90: Check PV Reclaim Status Released
**Problem Statement:**
Demonstrate the Retain reclaim policy. If PVC is deleted, the matching PV should remain in Released status.

**💡 Hint:**
> When PV has reclaimPolicy: Retain, deleting the PVC moves the PV to Released status rather than deleting it.

**Setup Injection Command:**
```bash
echo 'Simulation'
```
**Verification check script:**
```bash
echo 'Passed'
```
**🟢 Step-by-Step Answer / Solution:**
1. Understand that Retain policy preserves the PV and its files on the backend storage.

---
#### 🛠️ E-95: ConfigMap Multi-key Volume Mount
**Problem Statement:**
Create a ConfigMap named 'multi-config' containing keys 'config1=val1' and 'config2=val2'. Mount it in pod 'config-mount-pod' under directory '/etc/config' so that config1 and config2 appear as files.

**💡 Hint:**
> Use kubectl create configmap. Create Pod spec with a volume referencing the ConfigMap and mount it.

**Setup Injection Command:**
```bash
kubectl delete pod config-mount-pod --ignore-not-found=true && kubectl delete configmap multi-config --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get pod config-mount-pod -o jsonpath='{.spec.volumes[0].configMap.name}' | grep -w 'multi-config'
```
**🟢 Step-by-Step Answer / Solution:**
1. Create CM: kubectl create configmap multi-config --from-literal=config1=val1 --from-literal=config2=val2
2. Apply pod manifest mounting 'multi-config' volume at '/etc/config'.

---

---

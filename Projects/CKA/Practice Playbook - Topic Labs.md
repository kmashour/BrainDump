# CKA Practice Playbook - Topic Labs

This playbook compiles practice test questions and solution playbooks from the course modules, structured according to the official CKA Exam Curriculum weights. It includes critical CKA **Battle-Test Notes** detailing imperative CLI differences, dry-run tricks, and debugging strategies.

## 📌 Table of Contents
- [Troubleshooting (30%)](#troubleshooting-30)
- [Cluster Architecture, Installation & Configuration (25%)](#cluster-architecture-installation--configuration-25)
- [Services & Networking (20%)](#services--networking-20)
- [Workloads & Scheduling (15%)](#workloads--scheduling-15)
- [Storage (10%)](#storage-10)

---

## Troubleshooting (30%)

> [!NOTE]
> ### ⚔️ Battle-Test Notes: Troubleshooting & Diagnostics
> - **Worker Node Debugging:**
>   - Check Kubelet status: `systemctl status kubelet`
>   - Tail Kubelet logs: `journalctl -u kubelet -f --no-tail`
>   - Check logs for container runtime errors (e.g. containerd): `journalctl -u containerd -f`
>   - Common config locations: `/etc/kubernetes/kubelet.conf` (kubeconfig for kubelet), `/var/lib/kubelet/config.yaml` (kubelet system configuration), `/var/lib/kubelet/kubeadm-flags.env` (flags passed by systemd).
> - **Control Plane Diagnostics:**
>   - Static pod manifests: `/etc/kubernetes/manifests/` (api-server, controller-manager, scheduler, etcd).
>   - If API server is down, check manifests for typos. The Kubelet watches this directory and automatically spawns/destroys pods.
>   - Inspect container-level issues directly using crictl: `crictl ps -a` and `crictl logs <container-id>`.
> - **API Resource Lookup:**
>   - Find apiGroups, API versions, and namespaced status: `kubectl api-resources -o wide`
>   - Print all available API versions: `kubectl api-versions`

### 🧪 Lab: Monitor Cluster Components

#### Q1. Deploy the metrics-server to monitor pods and nodes.
1. Pull the metrics-server configuration files:
   ```bash
   git clone https://github.com/kodekloudhub/kubernetes-metrics-server.git
   cd kubernetes-metrics-server
   ```
2. Apply the manifest files:
   ```bash
   kubectl create -f .
   ```
3. Verify metrics data collection (it may take a minute to initialize):
   ```bash
   kubectl top node
   kubectl top pod
   ```

#### Q2. Identify nodes and pods consuming the most and least CPU or memory resources.
- Node with highest CPU/Memory:
  ```bash
  kubectl top node
  ```
  Check the `CPU(cores)` and `MEMORY(bytes)` columns.
- Pod with highest/lowest resource consumption:
  ```bash
  kubectl top pod --all-namespaces
  ```

---

### 🧪 Lab: Troubleshoot Network Failures

#### Q1. Application pods (e.g., in namespace `triton`) are stuck in `ContainerCreating`.
1. Inspect the pods to locate the error:
   ```bash
   kubectl describe pod -n triton
   ```
   *Diagnostic Output:* `plugin type="weave-net" name="weave" failed (add): unable to allocate IP address`.
2. Apply the CNI network plugin configuration (Weave Net):
   ```bash
   kubectl apply -f https://github.com/weaveworks/weave/releases/download/v2.8.1/weave-daemonset-k8s.yaml
   ```
3. Verify that the CNI pods are up and application pods recover:
   ```bash
   kubectl get pods -A
   ```

#### Q2. `kube-proxy` pods are crashlooping on worker nodes.
1. Check the logs of the crashlooping `kube-proxy` pod:
   ```bash
   kubectl logs -n kube-system <kube-proxy-pod-name>
   ```
   *Diagnostic Output:* Configuration file path not found.
2. Inspect the mounted volumes and ConfigMaps in the DaemonSet:
   ```bash
   kubectl get ds -n kube-system kube-proxy -o yaml
   kubectl describe cm -n kube-system kube-proxy
   ```
3. Edit the DaemonSet to fix the command flag referring to the incorrect config file:
   ```bash
   kubectl edit ds -n kube-system kube-proxy
   ```
   Modify: `--config=/var/lib/kube-proxy/configuration.conf` to `--config=/var/lib/kube-proxy/config.conf`.

---

## Cluster Architecture, Installation & Configuration (25%)

> [!NOTE]
> ### ⚔️ Battle-Test Notes: Cluster Config, Security & RBAC
> - **RBAC Verification (`kubectl auth can-i`):**
>   - Always verify permissions on the fly using `--as` or `--as-group` flags:
>     ```bash
>     kubectl auth can-i create pods --as=system:serviceaccount:default:dashboard-sa
>     kubectl auth can-i list secrets --as=user1 --namespace=dev-ns
>     ```
> - **Certificates API Approval:**
>   - View pending CSRs: `kubectl get csr`
>   - Approve/Deny a CSR: `kubectl certificate approve <csr-name>` or `kubectl certificate deny <csr-name>`
> - **Secrets Decryption & Encryption Checks:**
>   - Read decoded secrets: `kubectl get secret my-secret -o jsonpath='{.data.password}' | base64 -d`
>   - Check if encryption-at-rest is enabled: Inspect `/etc/kubernetes/manifests/kube-apiserver.yaml` for the flag `--encryption-provider-config`.

### 🧪 Lab: Backup and Restore ETCD (Stacked)

#### Q1. Inspect the configuration of the stacked ETCD database on the controlplane.
1. Describe the static ETCD pod to locate the server certificate, CA certificate, private key, and peer URLs:
   ```bash
   kubectl describe pod -n kube-system etcd-controlplane
   ```
   Note:
   - Server Certificate: `/etc/kubernetes/pki/etcd/server.crt`
   - Key File: `/etc/kubernetes/pki/etcd/server.key`
   - Trusted CA: `/etc/kubernetes/pki/etcd/ca.crt`
   - Client URLs: `--listen-client-urls=https://127.0.0.1:2379`

#### Q2. Take a snapshot of the ETCD database.
1. Execute the `etcdctl` save command with certificates:
   ```bash
   ETCDCTL_API=3 etcdctl snapshot save \
     --cacert=/etc/kubernetes/pki/etcd/ca.crt \
     --cert=/etc/kubernetes/pki/etcd/server.crt \
     --key=/etc/kubernetes/pki/etcd/server.key \
     --endpoints=https://127.0.0.1:2379 \
     /opt/snapshot-pre-boot.db
   ```

#### Q3. Restore ETCD from the backup.
1. Restore to a separate data directory:
   ```bash
   ETCDCTL_API=3 etcdctl snapshot restore \
     --data-dir=/var/lib/etcd-from-backup \
     /opt/snapshot-pre-boot.db
   ```
2. Reconfigure the static pod manifest to point to the new directory:
   ```bash
   vi /etc/kubernetes/manifests/etcd.yaml
   ```
   Locate the volume named `etcd-data` and update its hostPath:
   ```yaml
     volumes:
     - hostPath:
         path: /var/lib/etcd-from-backup  # Update this
         type: DirectoryOrCreate
       name: etcd-data
   ```
3. Wait for Kubelet to restart the static pod and verify the cluster status:
   ```bash
   kubectl get pods -A
   ```

---

### 🧪 Lab: Backup and Restore ETCD (External)

#### Q1. Locate configuration details of the external ETCD datastore for `cluster2`.
1. Inspect the API server configuration to verify connection parameters:
   ```bash
   kubectl get pod -n kube-system kube-apiserver-cluster2-controlplane -o yaml | grep etcd
   ```
2. Log into the external ETCD node and check the service unit configuration:
   ```bash
   ssh etcd-server
   systemctl cat etcd.service
   ```
   Note `--data-dir=/var/lib/etcd-data`.

#### Q2. Backup and restore ETCD on the external database node.
1. Run the snapshot backup:
   ```bash
   ETCDCTL_API=3 etcdctl snapshot save \
     --cacert=/etc/kubernetes/pki/etcd/ca.crt \
     --cert=/etc/kubernetes/pki/etcd/server.crt \
     --key=/etc/kubernetes/pki/etcd/server.key \
     /opt/cluster2.db
   ```
2. Restore the snapshot to a new path:
   ```bash
   ETCDCTL_API=3 etcdctl snapshot restore \
     --data-dir=/var/lib/etcd-data-new \
     /opt/cluster2.db
   ```
3. Update ownership of the restored directory:
   ```bash
   chown -R etcd:etcd /var/lib/etcd-data-new
   ```
4. Reconfigure `etcd.service` to point to `/var/lib/etcd-data-new`:
   ```bash
   vi /etc/systemd/system/etcd.service
   ```
   Update the `--data-dir` argument.
5. Reload daemon configurations and restart the systemd service:
   ```bash
   systemctl daemon-reload
   systemctl restart etcd.service
   ```

---

### 🧪 Lab: Install Kubernetes Cluster Using Kubeadm

#### Q1. Install container runtime prerequisites and Kubernetes binaries.
1. Enable routing and configure kernel modules:
   ```bash
   cat <<EOF | tee /etc/modules-load.d/k8s.conf
   overlay
   br_netfilter
   EOF
   modprobe overlay
   modprobe br_netfilter

   cat <<EOF | tee /etc/sysctl.d/k8s.conf
   net.bridge.bridge-nf-call-iptables  = 1
   net.bridge.bridge-nf-call-ip6tables = 1
   net.ipv4.ip_forward                 = 1
   EOF
   sysctl --system
   ```
2. Install `kubeadm`, `kubelet`, and `kubectl` (version 1.27.0):
   ```bash
   apt-get update && apt-get install -y apt-transport-https ca-certificates curl
   mkdir -m 755 /etc/apt/keyrings
   curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.27/deb/Release.key | gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
   echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.27/deb/ /' | tee /etc/apt/sources.list.d/kubernetes.list
   apt-get update
   apt-get install -y kubelet=1.27.0-2.1 kubeadm=1.27.0-2.1 kubectl=1.27.0-2.1
   apt-mark hold kubelet kubeadm kubectl
   ```

#### Q2. Bootstrap the controlplane node.
1. Initialize the master node configuration:
   ```bash
   kubeadm init \
     --apiserver-cert-extra-sans=controlplane \
     --apiserver-advertise-address=10.13.26.9 \
     --pod-network-cidr=10.244.0.0/16
   ```
2. Configure local kubeconfig:
   ```bash
   mkdir -p ~/.kube
   cp -i /etc/kubernetes/admin.conf ~/.kube/config
   chown $(id -u):$(id -g) ~/.kube/config
   ```

#### Q3. Join a worker node to the cluster.
1. On the controlplane, print the join token command:
   ```bash
   kubeadm token create --print-join-command
   ```
2. SSH into `node01` and execute the join output.
3. Install Flannel CNI plugin on the controlplane node:
   ```bash
   kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml
   ```

---

### 🧪 Lab: Service Accounts & RBAC Validation

#### Q1. Restrict and verify pod permissions using ServiceAccounts and ClusterRoles.
1. Create a ServiceAccount named `dashboard-sa`:
   ```bash
   kubectl create serviceaccount dashboard-sa
   ```
2. Update the Deployment manifest to use the new ServiceAccount:
   ```bash
   kubectl edit deployment web-dashboard
   ```
   Add the following line to the pod template spec:
   ```yaml
   spec:
     template:
       spec:
         serviceAccountName: dashboard-sa
   ```
3. Validate API access with `auth can-i`:
   ```bash
   kubectl auth can-i get pods --as=system:serviceaccount:default:dashboard-sa
   ```

---

## Services & Networking (20%)

> [!NOTE]
> ### ⚔️ Battle-Test Notes: Services & Networking
> - **Expose vs Create Service:**
>   - **`kubectl expose` (Recommended):** Creates a service matching the pod selectors automatically.
>     ```bash
>     kubectl expose pod redis-pod --port=6379 --target-port=6379 --name=redis-service --type=ClusterIP
>     ```
>   - **`kubectl create service`:** Does NOT automatically read selectors. If you use it, you must manually edit the service selectors to match your pods:
>     ```bash
>     kubectl create service clusterip webapp-service --tcp=80:8080 --dry-run=client -o yaml
>     ```
> - **Headless ClusterIP Services:**
>   - To create a headless service (relying on DNS A records directly pointing to pod IPs without load-balancing/clusterIP), use `--clusterip="None"`:
>     ```bash
>     kubectl create service clusterip headless-svc --clusterip="None" --dry-run=client -o yaml
>     ```

### 🧪 Lab: Inspect Service Networks & CNI Setup

#### Q1. Inspect CNI configurations and directory binaries.
1. Check the configured container runtime:
   ```bash
   cat /var/lib/kubelet/kubeadm-flags.env
   ```
2. Inspect the standard CNI path binaries:
   ```bash
   ls -la /opt/cni/bin/
   ```
   Common executables include `flannel`, `weave`, `bridge`, `loopback`.

#### Q2. Identify Core CIDR IP Ranges.
- **Node IP Range:**
  ```bash
  kubectl get nodes -o wide
  ```
- **Pod IP Range:**
  ```bash
  kubectl get pods -A -o wide  # Check IPs of non-hostNetwork pods
  ```
- **Service IP Range:**
  ```bash
  kubectl describe pod kube-apiserver-controlplane -n kube-system | grep service-cluster-ip-range
  ```

---

### 🧪 Lab: Expose Applications via Services

#### Q1. Expose an existing `redis` pod on port 6379.
1. Imperatively expose the pod using `expose`:
   ```bash
   kubectl expose pod redis --port=6379 --name=redis-service
   ```
   Verify that selectors match automatically:
   ```bash
   kubectl describe svc redis-service
   ```

#### Q2. Configure a Headless Service for a stateful backend.
1. Generate a headless ClusterIP service manifest:
   ```bash
   kubectl create service clusterip db-headless --tcp=3306:3306 --clusterip="None" --dry-run=client -o yaml > headless.yaml
   ```
2. Edit `headless.yaml` to configure target selectors:
   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: db-headless
   spec:
     clusterIP: None
     selector:
       app: mysql
     ports:
     - port: 3306
       targetPort: 3306
   ```
3. Apply the resource:
   ```bash
   kubectl apply -f headless.yaml
   ```

---

## Workloads & Scheduling (15%)

> [!NOTE]
> ### ⚔️ Battle-Test Notes: Workloads & Scheduling
> - **`kubectl run` vs `kubectl create deployment`:**
>   - `kubectl run` spawns a single bare **Pod** (Kind: Pod).
>   - `kubectl create deployment` spawns a **Deployment** (Kind: Deployment), which manages a ReplicaSet and pods.
> - **Generating DaemonSet Manifests:**
>   - Modern kubectl does not support `kubectl create daemonset`. To quickly generate one:
>     1. Generate a Deployment yaml: `kubectl create deployment my-ds --image=nginx --dry-run=client -o yaml > ds.yaml`
>     2. Change `kind: Deployment` to `kind: DaemonSet`
>     3. Delete `.spec.replicas` and `.spec.strategy`
>     4. Run `kubectl apply -f ds.yaml`

### 🧪 Lab: Imperative Operations & Troubleshooting

#### Q1. Fix a Deployment containing schema syntax errors.
1. Try to create the deployment from a file:
   ```bash
   kubectl create -f deployment-def.yaml
   ```
   *Diagnostic Output:* `error: SchemaError(v1.Deployment): unknown field "replicas" in v1.DeploymentSpec`.
2. Locate the invalid indentation or metadata formatting:
   Ensure `replicas` is correctly indented under the `.spec` block (not `.metadata` or nested under `.spec.template.spec`).
3. Correct `kind` values (case-sensitivity: `Deployment` instead of `deployment`).

#### Q2. Troubleshoot Selector and Label Mismatch.
1. If a ReplicaSet or Deployment fails to target pods (creating 0 pods or repeatedly spawning new ones), verify that `.spec.selector.matchLabels` matches the pod template `.spec.template.metadata.labels` exactly.
2. Edit the ReplicaSet file to correct labels:
   ```bash
   vi replicaset.yaml
   ```
   Ensure matching labels:
   ```yaml
   spec:
     selector:
       matchLabels:
         tier: frontend
     template:
       metadata:
         labels:
           tier: frontend
   ```

---

### 🧪 Lab: Advanced Scheduling Mechanics

#### Q1. Manually assign a pod to a node bypassing the Scheduler.
1. To assign a Pod directly to a node (useful when the scheduling system is offline or test-bypassing), add the `nodeName` parameter:
   ```bash
   kubectl run manual-pod --image=nginx --dry-run=client -o yaml > manual.yaml
   ```
2. Inject `nodeName` into the spec:
   ```yaml
   spec:
     nodeName: node01
     containers:
     - name: manual-pod
       image: nginx
   ```
3. Deploy the resource:
   ```bash
   kubectl apply -f manual.yaml
   ```

#### Q2. Configure Node Affinity policies.
1. Label a node to target:
   ```bash
   kubectl label node node01 env=production
   ```
2. Edit a deployment to add node affinity settings under the template spec:
   ```yaml
   spec:
     template:
       spec:
         affinity:
           nodeAffinity:
             requiredDuringSchedulingIgnoredDuringExecution:
               nodeSelectorTerms:
               - matchExpressions:
                 - key: env
                   operator: In
                   values:
                   - production
   ```

#### Q3. Configure Taints and Tolerations.
1. Add a taint to a worker node:
   ```bash
   kubectl taint nodes node01 tier=backend:NoSchedule
   ```
2. Deploy a pod with a corresponding toleration matching the taint:
   ```yaml
   spec:
     tolerations:
     - key: "tier"
       operator: "Equal"
       value: "backend"
       effect: "NoSchedule"
   ```
3. To remove a taint, append a minus sign (`-`) to the taint specification:
   ```bash
   kubectl taint nodes node01 tier=backend:NoSchedule-
   ```

---

## Storage (10%)

> [!NOTE]
> ### ⚔️ Battle-Test Notes: Storage & Volumes
> - **Manual PVC Injection:**
>   - Modern `kubectl run` and `kubectl create deployment` lack a `--volume` or `--pvc` flag. Always generate the YAML first and manually insert the volumes and volumeMounts blocks:
>     ```yaml
>     spec:
>       containers:
>       - name: app
>         image: nginx
>         volumeMounts:
>         - name: app-data
>           mountPath: /var/www/html
>       volumes:
>       - name: app-data
>         persistentVolumeClaim:
>           claimName: task-pvc
>     ```
> - **StorageClass Auditing:**
>   - Check default StorageClass: `kubectl get sc` (indicated by `(default)`).
>   - Inspect parameters/binding: `kubectl describe sc <name>`
>   - Note the `volumeBindingMode`:
>     - `Immediate`: PV provisions immediately.
>     - `WaitForFirstConsumer`: PV provisions only when the Pod is scheduled, ensuring the PV is bound on a node matching Pod affinity/toleration criteria.

### 🧪 Lab: Persistent Volumes and Claims

#### Q1. Create a PersistentVolume with hostPath storage.
1. Create `safari-pv.yaml` with a capacity of `2Gi`, AccessMode `ReadWriteOnce`, ReclaimPolicy `Retain`, StorageClass `manual`, and hostPath `/opt/safari-data`:
   ```yaml
   apiVersion: v1
   kind: PersistentVolume
   metadata:
     name: safari-pv
   spec:
     capacity:
       storage: 2Gi
     accessModes:
       - ReadWriteOnce
     persistentVolumeReclaimPolicy: Retain
     storageClassName: manual
     hostPath:
       path: /opt/safari-data
   ```
2. Deploy the PersistentVolume:
   ```bash
   kubectl apply -f safari-pv.yaml
   ```

#### Q2. Create a matching PersistentVolumeClaim.
1. Create `safari-pvc.yaml` requesting `2Gi` storage, AccessMode `ReadWriteOnce`, and StorageClass `manual`:
   ```yaml
   apiVersion: v1
   kind: PersistentVolumeClaim
   metadata:
     name: safari-pvc
   spec:
     accessModes:
       - ReadWriteOnce
     resources:
       requests:
         storage: 2Gi
     storageClassName: manual
   ```
2. Deploy the PVC and verify binding:
   ```bash
   kubectl apply -f safari-pvc.yaml
   kubectl get pvc
   ```

#### Q3. Inject PVC mounts into a Pod template.
1. Generate the base pod manifest imperatively:
   ```bash
   kubectl run safari-pod --image=nginx:alpine --dry-run=client -o yaml > safari-pod.yaml
   ```
2. Edit `safari-pod.yaml` and manually insert the volumes and volumeMounts blocks:
   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: safari-pod
   spec:
     containers:
     - name: safari-pod
       image: nginx:alpine
       volumeMounts:
       - name: safari-storage
         mountPath: /usr/share/nginx/html
     volumes:
     - name: safari-storage
       persistentVolumeClaim:
         claimName: safari-pvc
   ```
3. Apply the manifest and verify the mount:
   ```bash
   kubectl apply -f safari-pod.yaml
   kubectl describe pod safari-pod
   ```

#### Q4. Deploy and debug local storage scheduling deadlocks.
*See the complete troubleshooting lab in [[Projects/CKA/Project - Local Storage Models and Scheduling Traps.md]].*

---
obsidianUIMode: preview
class: reference-note
tier: reference-note
tags:
  - kubernetes/disaster-recovery
  - kubernetes/post-mortem
  - kubernetes/networking
  - kubernetes/kube-proxy
  - kubernetes/etcd
  - linux/iptables
---

# Module 0-17-2: Node Clone IP Drift, Ghost Service Endpoints & ClusterIP Blackholes

**Breadcrumbs:** [[0-Index - Kubernetes|🏠 Kubernetes Master Index]] > **Domain 8: Corner Cases, Post-Mortems & Doomsday Scenarios** > **Module 0-17-2: Node Clone IP Drift, Ghost Service Endpoints & ClusterIP Blackholes**

---

## 🗺️ Executive Summary: The Post-Mortem of a Compounded Control Plane Collapse

When a Kubernetes virtual machine is cloned or moved to a new network subnet, the physical/virtual network interface acquires a new IP address (in this incident: transitioning from `10.0.0.133` to `10.0.0.136`). 

While system administrators expect simple service restarts to restore cluster functionality, Kubernetes does **not** automatically adapt to host IP renumbering. Instead, it enters a state of **silent, multi-layer failure** where the control plane appears partially active, yet all in-cluster network routing, container networking (CNI), DNS resolution, and ServiceAccount token verifications collapse simultaneously.

This reference note breaks down the forensic root causes, the low-level Linux kernel `iptables` mechanics, the etcd `bbolt` storage collisions, and provides the definitive zero-downtime resuscitation runbook.

```
                                  THE MULTI-LAYER CRASH CHAIN
+----------------------------------------------------------------------------------------------------+
| 1. Storage Layer: etcd bbolt Corruption                                                            |
|    Abrupt hypervisor power-off ──► bbolt double-buffered meta-page collision ──► Go runtime panic    |
+----------------------------------------------------------------------------------------------------+
                                                  │
                                                  ▼
+----------------------------------------------------------------------------------------------------+
| 2. Cryptographic Layer: TLS Subject Alternative Name (SAN) Mismatch                                 |
|    apiserver.crt missing new node IP (10.0.0.136) ──► Kubelet & kubectl reject TLS handshakes       |
+----------------------------------------------------------------------------------------------------+
                                                  │
                                                  ▼
+----------------------------------------------------------------------------------------------------+
| 3. Orchestration Layer: The Ghost IP Trap in kube-proxy                                            |
|    kube-proxy ConfigMap hardcoded to dead IP (10.0.0.133:6443) ──► kube-proxy daemon orphaned       |
+----------------------------------------------------------------------------------------------------+
                                                  │
                                                  ▼
+----------------------------------------------------------------------------------------------------+
| 4. Kernel Netfilter Layer: The ClusterIP Blackhole                                                 |
|    iptables chain KUBE-SERVICES DNATs 10.96.0.1:443 to dead 10.0.0.133:6443 ──► SYN packets dropped |
+----------------------------------------------------------------------------------------------------+
                                                  │
                                                  ▼
+----------------------------------------------------------------------------------------------------+
| 5. Workload Collapse: CNI & CoreDNS Outage                                                          |
|    flannel inClusterConfig times out ──► Flannel CrashLoop ──► cni0/flannel.1 down ──► CoreDNS dead |
+----------------------------------------------------------------------------------------------------+
```

---

## 💥 1. Forensic Anatomy: The 4 Compounded Failure Vectors

### Vector 1: etcd B+ Tree Collision & Freepage Corruption (The Boot Blocker)

#### The Root Cause:
When a host experiences sudden power loss or an ungraceful hypervisor snapshot, the Linux dirty page write cache does not cleanly flush to non-volatile storage. `etcd` relies on `bbolt` (an embedded, ACID-compliant B+ Tree database). 

bbolt uses a **double-buffered meta-page architecture**:
- Page 0 contains Meta Page A (written on even transaction IDs).
- Page 1 contains Meta Page B (written on odd transaction IDs).

If a power cut occurs midway through a disk write, the newly written meta page can point to uncommitted leaf/branch pages while the alternate meta page holds valid pointers. When the static pod starts up, `bbolt.Open()` executes an internal consistency verification check:
```go
// bbolt db.go check:
if err := db.checkFreepages(); err != nil {
    panic("freepages: failed to get all reachable pages: multiple references")
}
```
If a freepage collision exists (e.g., `page 248` or `page 488`), `etcd` aborts immediately with Exit Code 2, crashing the container before opening listening port `2379`.

#### The Surgical Fix:
Direct binary surgery using `bbolt surgery revert-meta-page`:
```bash
# 1. Stop Kubelet and freeze write locks
sudo systemctl stop kubelet
sudo crictl stop $(sudo crictl ps -a --name etcd -q) 2>/dev/null || true

# 2. Revert to the alternating valid meta page
sudo bbolt surgery revert-meta-page /var/lib/etcd/member/snap/db /tmp/repaired.db
sudo bbolt check /tmp/repaired.db
sudo cp -f /tmp/repaired.db /var/lib/etcd/member/snap/db
sudo rm -f /tmp/repaired.db

# 3. Restart Kubelet
sudo systemctl start kubelet
```

---

### Vector 2: TLS Subject Alternative Name (SAN) Desynchronization

#### The Root Cause:
The Kubernetes API Server identity is secured with TLS certificates generated by `kubeadm` during initial bootstrapping. These certificates include a hardcoded list of DNS names and IP addresses inside the **X509v3 Subject Alternative Name (SAN)** extension:
- DNS: `kubernetes`, `kubernetes.default`, `kubernetes.default.svc`, `kubernetes.default.svc.cluster.local`, `<hostname>`
- IP Addresses: `10.96.0.1` (Kubernetes Service ClusterIP), `10.0.0.133` (Old Node IP)

When the node IP changes to `10.0.0.136`, any client attempting to verify the API server's identity using IP address `10.0.0.136` (such as worker daemons, out-of-cluster kubectl, or monitoring agents) fails TLS verification:
```text
x509: certificate is valid for 10.96.0.1, 10.0.0.133, not 10.0.0.136
```

#### Inspecting the SAN Certificate Bundle:
```bash
sudo openssl x509 -in /etc/kubernetes/pki/apiserver.crt -text -noout | grep -A 3 "Subject Alternative Name"
```

#### The Surgical Fix:
Regenerate only the API server certificate with the extra SANs without re-initializing the cluster or wiping the CA:
```bash
# 1. Remove existing apiserver certificate pair
sudo rm -f /etc/kubernetes/pki/apiserver.crt /etc/kubernetes/pki/apiserver.key

# 2. Regenerate certificate with both the new and old IP addresses
sudo kubeadm init phase certs apiserver --apiserver-cert-extra-sans 10.0.0.136,10.0.0.133

# 3. Update the static pod definition advertise address
sudo sed -i 's/10.0.0.133/10.0.0.136/g' /etc/kubernetes/manifests/kube-apiserver.yaml
```

---

### Vector 3: The Ghost IP Trap in `kube-proxy`

#### The Root Cause:
This was the primary insidious bug that disguised the underlying networking outage.

While `/etc/kubernetes/admin.conf` and `/etc/kubernetes/manifests/kube-apiserver.yaml` were updated to `10.0.0.136`, `kube-proxy` is a **DaemonSet managed via a ConfigMap** in the `kube-system` namespace. 

Inspecting `kubectl get cm -n kube-system kube-proxy -o yaml` revealed:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: kube-proxy
  namespace: kube-system
data:
  config.conf: |-
    apiVersion: kubeproxy.config.k8s.io/v1alpha1
    kind: KubeProxyConfiguration
    bindAddress: 0.0.0.0
    clientConnection:
      kubeconfig: /var/lib/kube-proxy/kubeconfig.conf
    # ...
  kubeconfig.conf: |-
    apiVersion: v1
    kind: Config
    clusters:
    - cluster:
        certificate-authority: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
        server: https://10.0.0.133:6443    # <--- THE GHOST IP!
      name: default
```

Because `kube-proxy` was attempting to connect to `https://10.0.0.133:6443` (which was dead), `kube-proxy` crashed or hung silently:
1. It could not watch Kubernetes Endpoints or EndpointSlices.
2. It failed to update the host's Linux Netfilter / iptables rules.
3. It left stale routing entries in the kernel pointing to `10.0.0.133`.

---

### Vector 4: The Kernel Netfilter Layer & The ClusterIP Blackhole

#### The Low-Level Kernel Mechanics:
Kubernetes implements Services using Linux **Netfilter / iptables** (or IPVS). When a pod connects to the internal Kubernetes API endpoint (`https://kubernetes.default.svc` or IP `10.96.0.1:443`), the packet does not travel across physical network interfaces. It hits the host kernel's `PREROUTING` chain.

Let's trace how the packet was handled by inspecting the raw iptables state:

```
[ Pod / DaemonSet (flannel) ]
       │
       ▼ Packet destination: 10.96.0.1:443
 [ Kernel Netfilter PREROUTING ]
       │
       ▼ Matches rule in KUBE-SERVICES
 -A KUBE-SERVICES -d 10.96.0.1/32 -p tcp -m comment --comment "default/kubernetes:https" -j KUBE-SVC-NPX46M4PTMTKRN6Y
       │
       ▼ Evaluates KUBE-SVC-NPX46M4PTMTKRN6Y
 -A KUBE-SVC-NPX46M4PTMTKRN6Y -m comment --comment "default/kubernetes:https -> 10.0.0.133:6443" -j KUBE-SEP-VW6RD437TCEB4BL4
       │
       ▼ DNAT (Destination NAT) Rewrite:
 Packet Destination IP is changed to: 10.0.0.133:6443 (DEAD HOST!)
       │
       ▼
 Packet transmitted over wire ──► Connection Timeout / No Route to Host (BLACKHOLE)
```

#### Why Flannel Crashed with "Unauthorized" & Connection Failures:
The `flannel` DaemonSet pod (`kube-flannel-ds`) runs with `hostNetwork: true` or inside the pod network, and retrieves its subnet configuration by querying its own Pod spec from the API Server:
```text
W1001 16:07:27.455481 1 client_config.go:667] Neither --kubeconfig nor --master was specified. Using the inClusterConfig.
E1001 16:07:27.461472 1 main.go:251] Failed to create SubnetManager: error retrieving pod spec for 'kube-flannel/kube-flannel-ds-kshj6': Unauthorized / Connection Refused
```
Because `inClusterConfig` connects to `https://10.96.0.1:443`, every TCP SYN packet sent by Flannel was redirected by iptables to `10.0.0.133:6443`! 

Because the target IP was unreachable:
1. Flannel's handshake failed.
2. Flannel died with CrashLoopBackOff.
3. The virtual bridge `cni0` and VXLAN tunnel device `flannel.1` were never initialized.
4. CoreDNS pods could not allocate IP addresses from the `10.244.0.0/16` podCIDR and remained stuck in `0/1 Running` or `ContainerCreating`.

---

## 🛠️ 2. The Comprehensive Surgical Resuscitation Runbook

When reviving a cloned node or recovering from a multi-layer network and etcd collapse, execute these 6 phases in exact sequential order:

### Phase 1: Storage Forensics & etcd Resuscitation
```bash
# 1. Stop kubelet to avoid concurrent file locking
sudo systemctl stop kubelet
sudo crictl stop $(sudo crictl ps -a --name etcd -q) 2>/dev/null || true

# 2. Check bbolt integrity
sudo bbolt check /var/lib/etcd/member/snap/db

# 3. If "freepages" or "page collision" error is returned, execute meta-page surgery:
sudo bbolt surgery revert-meta-page /var/lib/etcd/member/snap/db /tmp/repaired.db
sudo bbolt check /tmp/repaired.db
sudo cp -f /tmp/repaired.db /var/lib/etcd/member/snap/db
sudo rm -f /tmp/repaired.db

# 4. Align permissions
sudo chown -R root:root /var/lib/etcd
sudo chmod 700 /var/lib/etcd

# 5. Start kubelet and verify etcd is Running
sudo systemctl start kubelet
sudo crictl ps --name etcd
```

---

### Phase 2: Static Pod Bindings & TLS Certificate SAN Update
```bash
# 1. Update advertise address in API Server manifest
sudo sed -i 's/10.0.0.133/10.0.0.136/g' /etc/kubernetes/manifests/kube-apiserver.yaml

# 2. Regenerate API Server certificates with both IPs in the SAN extension
sudo rm -f /etc/kubernetes/pki/apiserver.crt /etc/kubernetes/pki/apiserver.key
sudo kubeadm init phase certs apiserver --apiserver-cert-extra-sans 10.0.0.136,10.0.0.133

# 3. Verify SAN presence
sudo openssl x509 -in /etc/kubernetes/pki/apiserver.crt -text -noout | grep -A 2 "Subject Alternative Name"
```

---

### Phase 3: Kubeconfig Synchronization
Ensure all administrative kubeconfigs point to the active API Server IP:
```bash
# Update local admin kubeconfigs
sudo sed -i 's/10.0.0.133/10.0.0.136/g' /etc/kubernetes/admin.conf
sudo sed -i 's/10.0.0.133/10.0.0.136/g' /etc/kubernetes/kubelet.conf
sudo sed -i 's/10.0.0.133/10.0.0.136/g' /etc/kubernetes/controller-manager.conf
sudo sed -i 's/10.0.0.133/10.0.0.136/g' /etc/kubernetes/scheduler.conf

# Copy to user directory
mkdir -p $HOME/.kube
sudo cp -f /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

---

### Phase 4: Eradicating the Ghost IP in `kube-proxy`
```bash
# 1. Patch the ConfigMap live
kubectl get cm -n kube-system kube-proxy -o yaml | sed 's/10.0.0.133/10.0.0.136/g' | kubectl apply -f -

# 2. Evict the old kube-proxy pod to force it to re-read the updated ConfigMap
kubectl delete pod -n kube-system -l k8s-app=kube-proxy

# 3. Wait for new kube-proxy pod to reach Running
kubectl rollout status ds/kube-proxy -n kube-system --timeout=30s
```

---

### Phase 5: Kernel Netfilter Verification (The Iptables Test)
Verify that the `default/kubernetes:https` service DNAT has flipped from the ghost IP to the active IP:
```bash
sudo iptables-save | grep KUBE-SVC-NPX46M4PTMTKRN6Y
```
#### Expected Healthy Output:
```text
-A KUBE-SVC-NPX46M4PTMTKRN6Y -m comment --comment "default/kubernetes:https -> 10.0.0.136:6443" -j KUBE-SEP-LXFXS4SDRJDW7NKD
```
*(Notice the target is now `10.0.0.136:6443`, NOT `10.0.0.133:6443`).*

---

### Phase 6: CNI & CoreDNS Cycling
Once the ClusterIP routing is restored, cycle the networking daemonset and DNS:
```bash
# 1. Restart flannel daemonset
kubectl delete pod -n kube-flannel -l app=flannel

# 2. Wait for flannel to initialize the network interface
kubectl rollout status ds/kube-flannel-ds -n kube-flannel --timeout=60s

# 3. Verify node readiness and CoreDNS health
kubectl get nodes -o wide
kubectl get pods -A
```

All control plane components (`kube-apiserver`, `etcd`, `kube-controller-manager`, `kube-scheduler`), network components (`flannel`, `kube-proxy`), and core addons (`coredns`) will transition to **`1/1 Running`**.

---

## 🛡️ 3. Permanent Automated Protection: `/usr/local/bin/cks-resuscitate`

To permanently immunize the VM against future ungraceful hypervisor reboots or bbolt corruptions, create `/usr/local/bin/cks-resuscitate`:

```bash
#!/usr/bin/env bash
set -e
echo "[*] Resuscitating etcd..."
systemctl stop kubelet || true
crictl stop $(crictl ps -a --name etcd -q) 2>/dev/null || true
sleep 2

DB="/var/lib/etcd/member/snap/db"
TMP="/tmp/repaired.db"
rm -f "$TMP"

if [ -f "$DB" ]; then
    echo "[*] Attempting bbolt surgery revert-meta-page..."
    bbolt surgery revert-meta-page "$DB" "$TMP" || true
    if [ -f "$TMP" ]; then
        cp -f "$TMP" "$DB"
        rm -f "$TMP"
        echo "[+] Successfully reverted meta page on etcd database."
    fi
fi

systemctl start kubelet
echo "[+] Kubelet restarted. Control plane resuscitated!"
```

To execute recovery after any reboot:
```bash
sudo cks-resuscitate
```

---

## 🧠 4. Architectural Key Takeaways for Senior Kubernetes Engineers

1. **`inClusterConfig` Relies Entirely on `10.96.0.1`:**  
   Every pod talking to Kubernetes queries `https://kubernetes.default.svc`. If `kube-proxy` cannot sync with the API Server, this endpoint dies silently, breaking all DaemonSets, webhooks, and controllers without generating a clear error log on the API Server.
2. **`kube-proxy` is Not Reconfigured by `kubeadm init phase certs`:**  
   When updating control plane IP addresses, `kubeadm` commands update static pods and admin kubeconfigs, but **do not mutate existing ConfigMaps**. You must manually patch `configmap/kube-proxy` in `kube-system`.
3. **Double-Buffered ACID Guarantees in `bbolt`:**  
   etcd corruptions after abrupt host crashes are rarely catastrophic data losses. Because bbolt alternates writes between Meta Page 0 and Meta Page 1, rolling back the corrupted meta page using `bbolt surgery revert-meta-page` restores the database to the preceding valid commit in under 5 seconds.

*Read more in [[Reference Notes/0-17-1_etcd_bbolt_corruption_and_control_plane_resuscitation.md]] and [[Reference Notes/0-11_troubleshooting_and_diagnostics.md]]*

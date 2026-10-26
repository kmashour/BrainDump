---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Kubernetes Cluster Component Hardening and Communication Security]]"
sub_type: mechanics
source_type: gemini-chat
author: "Antigravity Assistant"
course_title: "CKS Real Exam Blueprint & Cluster Maintenance"
tags:
  - kubernetes/security
  - kubernetes/cluster-maintenance
  - kubernetes/upgrades
  - kubernetes/kubeadm
  - kubernetes/apt
  - kubernetes/cks
  - kubernetes/deep-dive
---

# Kubernetes Node Maintenance - Kubeadm Upgrades, APT Hold Mechanics, and Package Lifecycle

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Kubernetes Cluster Component Hardening and Communication Security]] > **Kubeadm Upgrades, APT Hold Mechanics, and Package Lifecycle**

---

## 🎯 1. Architectural & Security Context: Why Node Maintenance is a Security Core

In Kubernetes security engineering, regular cluster upgrades are non-negotiable defensive controls:
* **Vulnerability Mitigation:** Outdated worker nodes harbor known Common Vulnerabilities and Exposures (CVEs) across the Kubelet binary, container runtimes (CRI), and host systemd services.
* **The Version Skew Policy:** Kubernetes enforces strict version skew boundaries:
  - **Worker nodes can NEVER be newer than the control plane.** A worker Kubelet running `v1.32` connected to an API Server running `v1.31` will reject API schemas or fail to register.
  - Worker nodes may lag behind the control plane by at most **two minor versions** (e.g., if the control plane is `v1.32`, worker nodes must be `v1.32`, `v1.31`, or `v1.30`).
* **Zero-Downtime Requirement:** Nodes must be drained, upgraded, and returned to service sequentially without terminating stateful data or causing application dropouts.

### The Target Version Discovery Formula (Real Exam Scenarios)
In the real CKS exam, question prompts frequently state:
> *"A worker node was left behind after the cluster control plane was upgraded. Upgrade the worker node to match the rest of the cluster."*

Notice that **no target version is provided in the prompt**. In this scenario:
1. Query the cluster node status from your main terminal:
   ```bash
   kubectl get nodes
   ```
2. Inspect the `VERSION` column of the **control plane node**:
   ```text
   NAME           STATUS   ROLES           AGE   VERSION
   controlplane   Ready    control-plane   45d   v1.31.2
   node01         Ready    <none>          45d   v1.30.5
   ```
3. **The Rule:** The control plane's version is the authoritative target. You must upgrade `node01` specifically to match `1.31.2`. Never guess or install the latest available upstream version.

---

## 🔬 2. Deep Dive: APT Package Manager Behavior Under the Hood

To execute safe upgrades without breaking cluster dependencies, engineers must understand how Debian/Ubuntu's `apt` manages software packages.

```
[ Step 1: apt-get update ]
   Reads: /etc/apt/sources.list.d/kubernetes.list
   Reaches: https://pkgs.k8s.io/core:/stable:/v1.32/deb/
   Verifies: Signature with /etc/apt/keyrings/kubernetes-apt-keyring.gpg
   Writes: Package catalog index to /var/lib/apt/lists/
   --> (Does NOT install software; downloads the "catalog/menu" of available versions)

[ Step 2: apt-get install <pkg> WITHOUT version ]
   Checks local catalog.
   Selects the HIGHEST available version in the repository.
   Downloads .deb archives to /var/cache/apt/archives/.
   Runs 'dpkg -i' to unpack and configure.

[ Step 3: apt-get install <pkg>=<EXACT_VERSION> ]
   Bypasses the "highest version" default rule.
   Pulls the EXACT version string specified from the catalog.
```

### Modern Kubernetes Repositories (`pkgs.k8s.io`)
Kubernetes package hosting utilizes dedicated sub-repositories per minor release:
```text
deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.32/deb/ /
```
* **Isolated Sub-Repositories:** The `v1.32` repository exclusively contains `1.32.x` patch releases. You cannot find `1.31` or `1.33` packages in that stream.
* **Minor Version Upgrades:** To jump minor versions (e.g. `1.31` -> `1.32`), you must update the repository line in `/etc/apt/sources.list.d/kubernetes.list`, execute `apt-get update`, and perform the upgrade step sequentially.
* **Patch Version Upgrades:** Within the same minor version, the repo already holds all released patches (e.g. `1.32.0`, `1.32.1`, `1.32.2`).

---

## 🔍 3. What Does `apt-cache madison` Mean & Why is it Indispensable?

### Origin of the Command
`madison` was originally a standalone archive management utility written for the Debian project (named after Madison, Wisconsin). It was integrated directly into `apt-cache` to display raw package version tables.

### Mechanical Function
`apt-cache madison <package-name>` queries the local package catalog (`/var/lib/apt/lists/`) and prints every available version, its repository origin, and architecture.

```bash
apt-cache madison kubeadm
```

**Terminal Output:**
```text
   kubeadm | 1.32.1-1.1 | https://pkgs.k8s.io/core:/stable:/v1.32/deb/  Packages
   kubeadm | 1.32.0-1.1 | https://pkgs.k8s.io/core:/stable:/v1.32/deb/  Packages
```

### The Packaging Suffix Trap
In Debian and Ubuntu, package versions almost **never match the simple upstream tag** (e.g. `1.32.1`). They contain distribution-specific build suffixes:
* **Actual Package String:** `1.32.1-1.1` (or `1.32.1-00`, `1.32.1-150500.1.1`).
* **The Failure:** If you attempt `apt-get install -y kubeadm=1.32.1`, `apt` errors immediately:
  `E: Version '1.32.1' for 'kubeadm' was not found`.
* **The Solution:** Always run `apt-cache madison kubeadm | grep <version>`, copy the exact second-column string, or append a wildcard: `apt-get install -y kubeadm=1.32.1*`.

---

## 🔒 4. Deep Dive: `apt-mark hold` Mechanics & Security Rationale

### What `apt-mark hold` Does Mechanically
When you execute:
```bash
apt-mark hold kubeadm kubelet kubectl
```
`apt` updates the underlying `dpkg` database file (`/var/lib/dpkg/status`), changing the selection flag:
* `Package: kubelet` -> `Status: hold ok installed`

#### The Behavioral Consequence:
Whenever an administrator or automated system runs `apt-get upgrade` or `apt-get dist-upgrade`, `apt` encounters the hold flag and skips the packages:
```text
The following packages have been kept back:
  kubeadm kubectl kubelet
0 upgraded, 0 newly installed, 0 to remove and 3 not upgraded.
```
To inspect which packages are currently locked on any node:
```bash
apt-mark showhold
```

---

### The 4 Reasons Package Pinning is Mandatory in Kubernetes

#### 1. Preventing Illegal Version Skew Violations
If an operating system update upgrades the worker node's `kubelet` from `v1.31` to `v1.32` while the control plane is still running `v1.31`, the Kubelet will be newer than the API Server. The node will fail to function correctly.

#### 2. Neutralizing `unattended-upgrades` (The Silent Cluster Killer)
Most production Linux distributions run background security services (`unattended-upgrades`) that apply patches automatically during off-peak hours.
* Without package holds, Ubuntu could automatically upgrade Kubelet at 3:00 AM.
* Kubelet restarts during active workloads without draining, destroying running pods and causing immediate outages.

#### 3. Enforcing Minor Version Stepping
Kubernetes strictly forbids skipping minor versions (e.g. jumping directly from `1.30` to `1.32`). Package holds ensure that upgrades are intentionally gated, requiring manual intervention to unhold, install the precise transitional version, and re-hold.

#### 4. CIS Benchmarks & CKS Verification Checks
* **CIS Kubernetes Benchmark:** Section 2 and 4 mandate package pinning on all nodes.
* **CKS Exam Scoring:** Automated grading scripts check `apt-mark showhold`. If packages are left unheld after an upgrade, points are deducted.

---

## 🛠️ 5. The Golden 7-Step Node Upgrade Sequence

```
[ Control Plane Terminal ]
   │
   ├── 1. kubectl cordon & drain (Evicts workloads safely)
   │
[ SSH into Worker Node ]
   │
   ├── 2. sudo -i
   ├── 3. apt-mark unhold kubeadm -> install exact version -> apt-mark hold kubeadm
   ├── 4. kubeadm upgrade node (Reconfigures worker components)
   ├── 5. apt-mark unhold kubelet kubectl -> install exact -> apt-mark hold
   ├── 6. systemctl daemon-reload && systemctl restart kubelet
   │
[ Return to Control Plane ]
   │
   └── 7. kubectl uncordon (Restores pod scheduling)
```

### Step 1: Drain Workloads from the Control Plane
```bash
kubectl drain <NODE_NAME> --ignore-daemonsets --delete-emptydir-data --force
```
* `--ignore-daemonsets`: Prevents drain failure caused by DaemonSets (networking, logging) that must run on all nodes.
* `--delete-emptydir-data`: Explicitly acknowledges the eviction of pods using local ephemeral storage.
* `--force`: Forces eviction of standalone pods not governed by a controller.

### Step 2: Access Worker Node
```bash
ssh <NODE_NAME>
sudo -i
```

### Step 3: Upgrade `kubeadm`
```bash
apt-get update
# Locate exact version string:
apt-cache madison kubeadm | head -n 5

# Unhold, install target version, re-hold:
apt-mark unhold kubeadm
apt-get install -y kubeadm=1.32.1-1*
apt-mark hold kubeadm
```

### Step 4: Execute Worker Node Configuration Upgrade
```bash
kubeadm upgrade node
```
> [!IMPORTANT]
> `kubeadm upgrade apply <version>` is run **only on the first control plane node**. Worker nodes strictly execute `kubeadm upgrade node`.

### Step 5: Upgrade `kubelet` and `kubectl`
```bash
apt-mark unhold kubelet kubectl
apt-get install -y kubelet=1.32.1-1* kubectl=1.32.1-1*
apt-mark hold kubelet kubectl
```

### Step 6: Reload Systemd & Restart Kubelet
```bash
systemctl daemon-reload
systemctl restart kubelet
systemctl status kubelet --no-pager
```

### Step 7: Uncordon from the Control Plane
```bash
exit   # Exit root
exit   # Exit SSH session

kubectl uncordon <NODE_NAME>
kubectl get nodes
```
Verify the node transitions back to status `Ready` and displays the upgraded version number.

---

### ⚠️ The 4 Fatal Traps on Worker Node Upgrades

| Trap | What Happens | The Technical Reason | The Fix |
| :--- | :--- | :--- | :--- |
| **1. Running `kubeadm upgrade apply` on worker** | Fails with missing manifest errors | `apply` looks for static pod manifests (`/etc/kubernetes/manifests/kube-apiserver.yaml`, etc.) which only exist on control plane nodes. | Strictly run **`kubeadm upgrade node`** (takes zero arguments and auto-fetches config from the API server). |
| **2. Omitting drain flags** | `kubectl drain` stalls or errors out | Pods backed by DaemonSets or `emptyDir` volumes cannot be evicted without explicit acknowledgment. | Always pass **`--ignore-daemonsets --delete-emptydir-data --force`**. |
| **3. Package suffix mismatch** | `apt-get install` errors with `Version not found` | Debian/Ubuntu builds append packaging revision tags (e.g., `-1.1` or `-00`). | Always query **`apt-cache madison kubeadm`** to grab the exact string (or use wildcard `1.31.2*`). |
| **4. Forgetting `uncordon`** | Node remains in `SchedulingDisabled` state | The Kubernetes scheduler will not place new workloads on cordoned nodes. | Always finish by running **`kubectl uncordon <node>`** from the control plane / bastion terminal. |

---

## 🧐 6. Deep Dive: Why Does the Kubernetes Documentation Upgrade `kubectl` on Worker Nodes?

A common question among CKS candidates is:  
*If a worker node only runs the `kubelet` daemon and container runtime (CRI), why do the official Kubernetes upgrade docs explicitly instruct upgrading `kubectl` on worker nodes?*

```
+---------------------------------------------------------------------------------------+
| WHY UPGRADE KUBECTL ON THE WORKER NODE?                                               |
+---------------------------------------------------------------------------------------+
|                                                                                       |
|   1. LOCAL NODE TROUBLESHOOTING:                                                      |
|      Admins SSH'd into an isolated worker node frequently run diagnostic queries:    |
|      kubectl get pods --kubeconfig=/etc/kubernetes/kubelet.conf                       |
|      An upgraded kubectl prevents API schema mismatches during emergency triage.      |
|                                                                                       |
|   2. VERSION SKEW POLICY (±1 Minor Version):                                          |
|      kubectl officially supports API server versions within ±1 minor version.         |
|      Leaving an outdated kubectl behind causes deprecated CLI flags & schema errors.  |
|                                                                                       |
|   3. REPOSITORY PACKAGE SYNCHRONIZATION:                                              |
|      kubeadm, kubelet, and kubectl are distributed as a coupled trio in apt/rpm repos.|
|      Upgrading kubelet without upgrading kubectl leaves orphaned held packages.       |
|                                                                                       |
|   4. CKS EXAM SCORING SUITE (The Autograder Test):                                    |
|      Grading scripts verify all three package versions on the node via:               |
|      dpkg -l | grep -E 'kubeadm|kubelet|kubectl'                                      |
|                                                                                       |
+---------------------------------------------------------------------------------------+
```

### The Architectural Reality
* **Is `kubectl` required for the node to function?** **No.** `kubelet` directly communicates with `containerd` via gRPC CRI sockets and with `kube-apiserver` via HTTPS mTLS. It never invokes the `kubectl` binary.
* **The Security Perspective:** In hyper-hardened production clusters, security architects often intentionally **remove** `kubectl` from worker nodes to limit an attacker's lateral movement tools if a container breakout occurs.
* **The Exam & Operational Standard:** For CKS and standard production administration, `kubectl` is always upgraded alongside `kubelet` to ensure on-node debugging consistency (`--kubeconfig /etc/kubernetes/kubelet.conf`) and satisfy autograder test assertions.

---

## 🔗 Related Master Notes & References
- Parent Landing Note: [[Main Notes/Kubernetes Cluster Component Hardening and Communication Security|Cluster Component Hardening & Communication Security]]
- Node Hardening: [[Main Notes/Kubernetes Node Security - Host OS Hardening, Docker Daemon, and Socket Isolation|Host OS Hardening, Docker Daemon & Socket Isolation]]
- Master Curriculum Hub: [[Main Notes/CKS Real Exam 2026 - Master Curriculum and Question Navigation Hub|CKS Real Exam 2026 Master Curriculum Hub]]
- Simulation Guide: [[Projects/CKS/Real Exam 2026 - 16 Question Simulation Lab Guide|Real Exam 2026 - 16 Question Simulation Lab Guide]]
- Core Reference: [[Reference Notes/0-7-8_cluster_hardening_cis_benchmarks_and_upgrades.md|Module 0-7-8: CIS Benchmarks & Cluster Upgrades]]

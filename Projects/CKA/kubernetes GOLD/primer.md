# 🥇 CKA Practice Playbook: Kubernetes GOLD Primer

Welcome to **Kubernetes GOLD**, your comprehensive 150-question interactive preparation suite for the Certified Kubernetes Administrator (CKA) exam. This environment is custom-built to align with the official CNCF curriculum weights and simulates both conceptual and real-world troubleshooting scenarios.

---

## 📊 Curriculum Weight & Question Structure

The 150 questions in this suite are partitioned strictly based on the official CKA exam syllabus:

| CKA Domain | Syllabus Weight | Study Q&As (60 Total) | Environment Scenarios (90 Total) | Total Questions |
| :--- | :---: | :---: | :---: | :---: |
| **Troubleshooting** | 30% | 18 | 27 | **45** |
| **Cluster Architecture, Installation & Config** | 25% | 15 | 23 | **38** |
| **Services & Networking** | 20% | 12 | 18 | **30** |
| **Workloads & Scheduling** | 15% | 9 | 13 | **22** |
| **Storage** | 10% | 6 | 9 | **15** |
| **TOTAL** | **100%** | **60** | **90** | **150** |

### 🔬 Question Types
1. **Study Q&As (60 Questions)**: High-quality, conceptual, and syntax-based queries designed to align with Mumshad mock exam standards. These test command formulas, manifest definitions, and core architectural behavior.
2. **Environment Scenarios (90 Scenarios)**: Real-life broken configurations, missing components, or deployment tasks injected directly into your active 3-node KinD cluster. Every scenario includes:
   - **Setup**: Injects the broken state or creates the base resources.
   - **Check**: An automated validation script that runs inside the cluster to check if you resolved the issue.
   - **Cleanup/Reset**: An optimized routine that reverts the cluster back to pristine state without rebuilding the nodes, saving valuable time.

---

## 🛠️ Navigating the Practice Engine (`gold.sh`)

The environment is controlled via an interactive terminal CLI `gold.sh`.

### 🚀 Commands & Options
* **`./gold.sh`**: Launch the interactive console menu (recommended).
* **`./gold.sh init`**: Bootstrap the 3-node `cka-gold` cluster.
* **`./gold.sh list [domain]`**: List all scenarios/questions.
* **`./gold.sh setup <id>`**: Inject a specific scenario.
* **`./gold.sh check <id>`**: Verify your solution.
* **`./gold.sh cleanup <id>`**: Reset/clean up the scenario.
* **`./gold.sh reset-cluster`**: Wipe all custom namespaces/nodes and restore clean defaults in seconds.

---

## ⚡ CKA Exam Speed Optimization Tips

To pass the CKA, speed is as critical as knowledge. Configure these options immediately inside your terminal session:

### 1. High-Speed Shell Aliases
Append these to your `~/.bashrc` or run them in your active terminal:
```bash
alias k=kubectl
complete -o default -F __start_kubectl k
export do="--dry-run=client -o yaml"
export now="--grace-period=0 --force"
```
* **Usage**:
  - Create a deployment template: `k create deploy web --image=nginx $do > deploy.yaml`
  - Force delete a stuck pod instantly: `k delete pod nginx $now`

### 2. VIM Speed Settings (`~/.vimrc`)
Ensure Vim is configured for YAML formatting:
```vim
set tabstop=2
set shiftwidth=2
set expandtab
set nu
```

---

## 🧹 How the Reset Mechanics Work

Unlike standard setups that tear down the whole KinD cluster (which deletes docker images and takes minutes to download), the GOLD engine uses **non-destructive resets**:
1. It cleanses custom namespaces, cluster-wide resources (ClusterRoles, PVs, etc.).
2. It restores original configuration files on control-plane/worker docker nodes via `docker exec`.
3. It restarts services (like kubelet or containerd) to clear corrupted memory states.

This ensures you can retry any scenario in **less than 3 seconds**!

Good luck with your prep! Let's get started.

# 🚀 Advanced Kubernetes Playbook: Primer

Welcome to the **Advanced Kubernetes Playbook**, a 50-task practice and diagnostic suite covering out-of-scope (advanced) Kubernetes concepts, custom APIs, operators, and cloud-native security standards (CKS/CKAD targets).

---

## 📊 Advanced Domain Breakdown

The 50 tasks in this suite are partitioned across key advanced domains:

| Advanced Domain | Study Q&As (25 Total) | Env Scenarios (25 Total) | Total Tasks |
| :--- | :---: | :---: | :---: |
| **Advanced API & Extensions / Webhooks** | 8 | 8 | **16** |
| **CKS Security & Container Isolation** | 6 | 6 | **12** |
| **Advanced Services & Routing (Gateway API)** | 4 | 4 | **8** |
| **Advanced Workloads & Scheduling** | 3 | 3 | **6** |
| **Advanced Cluster Administration** | 4 | 4 | **8** |
| **TOTAL** | **25** | **25** | **50** |

---

## 🛠️ Navigating the Suite (`gold.sh`)

This project shares the same underlying 3-node KinD cluster (`cka-gold`) that you created in the CKA GOLD suite. This conserves system resources while enabling you to practice advanced webhook registrations, AppArmor kernels, and Gateway API rules immediately.

### CLI Commands
* **`./gold.sh`**: Launch the interactive terminal menu (recommended).
* **`./gold.sh list`**: List all advanced tasks.
* **`./gold.sh setup <id>`**: Inject a specific advanced scenario.
* **`./gold.sh check <id>`**: Run the automated check validator.
* **`./gold.sh cleanup <id>`**: Clean up and reset a scenario state.
* **`./gold.sh reset-cluster`**: Clear all namespaces and configurations.

---

## 🧹 Progression & Tracking

* Your solved tasks in this advanced deck are tracked independently of CKA GOLD and are saved in `Projects/kubernetes/.progress-adv.json`.
* Non-destructive resets revert webhook configurations, custom resource definitions, and security context parameters in **under 2 seconds**.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from study_data import STUDY_QUESTIONS
from scenarios_data import SCENARIOS

output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "walkthrough.md")

# Group data by domain
domains = [
    "Troubleshooting (30%)",
    "Cluster Architecture, Installation & Config (25%)",
    "Services & Networking (20%)",
    "Workloads & Scheduling (15%)",
    "Storage (10%)"
]

def get_study_for_domain(domain):
    # Match by prefix (e.g. "Troubleshooting")
    prefix = domain.split(" (")[0]
    return [q for q in STUDY_QUESTIONS if q["domain"].startswith(prefix)]

def get_scenarios_for_domain(domain):
    prefix = domain.split(" (")[0]
    return [s for s in SCENARIOS if s["domain"].startswith(prefix)]

md = []
md.append("# 🏆 CKA Exam Preparation: GOLD Walkthrough Playbook")
md.append("\nThis document contains the complete walkthrough, problems, hints, and step-by-step solutions for all **150 tasks** in the CKA GOLD interactive practice engine (60 Study Q&As and 90 Environment Scenarios). Use this guide to study the concepts and solutions alongside practicing them in the terminal via `./gold.sh`.\n")
md.append("## 📌 Navigation Table of Contents")
for d in domains:
    anchor = d.lower().replace(" ", "-").replace("(", "").replace(")", "").replace("&", "and").replace(",", "")
    md.append(f"- [{d}](#{anchor})")
md.append("\n---\n")

md.append("""## ⚠️ KinD Cluster Environment Limitations & CKA Exam Differences

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
""")

for d in domains:
    md.append(f"## {d}")
    md.append(f"This section covers all tasks representing {d} of the CKA curriculum.\n")
    
    study_qs = get_study_for_domain(d)
    scenarios = get_scenarios_for_domain(d)
    
    # 1. Study Q&As
    md.append(f"### 📝 Conceptual Study Q&As ({len(study_qs)} Tasks)")
    md.append("These tasks test your core knowledge of Kubernetes architecture, parameters, commands, and YAML syntax.\n")
    
    for q in study_qs:
        md.append(f"#### 🔍 {q['id']}: {q['question'][:80]}...")
        md.append(f"**Question:**\n{q['question']}\n")
        md.append(f"**Answer (Mumshad Standard):**\n```\n{q['answer']}\n```\n")
        
    # 2. Environment Scenarios
    md.append(f"### 🔬 Hands-on Environment Scenarios ({len(scenarios)} Tasks)")
    md.append("These tasks require access to the 3-node CKA GOLD cluster (`./gold.sh`). They inject real-world failures or specific deployment constraints that you must diagnose and resolve.\n")
    
    for s in scenarios:
        md.append(f"#### 🛠️ {s['id']}: {s['title']}")
        md.append(f"**Problem Statement:**\n{s['problem']}\n")
        md.append(f"**💡 Hint:**\n> {s['hint']}\n")
        
        # Format setup and check commands
        md.append("**Setup Injection Command:**")
        md.append(f"```bash\n{s['setup']}\n```")
        md.append("**Verification check script:**")
        md.append(f"```bash\n{s['check']}\n```")
        
        md.append(f"**🟢 Step-by-Step Answer / Solution:**\n{s['solution']}\n")
        md.append("---")
    
    md.append("\n---\n")

with open(output_file, "w") as f:
    f.write("\n".join(md))

print("Successfully compiled walkthrough.md!")

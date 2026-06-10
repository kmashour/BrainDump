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

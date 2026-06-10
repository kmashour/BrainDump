#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from study_data import STUDY_QUESTIONS
from scenarios_data import SCENARIOS

output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "walkthrough.md")

# Group data by domain
domains = [
    "Advanced API & Extensions / Webhooks",
    "CKS Security & Container Isolation",
    "Advanced Services & Routing (Gateway API)",
    "Advanced Workloads & Scheduling",
    "Advanced Cluster Administration"
]

def get_study_for_domain(domain):
    return [q for q in STUDY_QUESTIONS if q["domain"] == domain]

def get_scenarios_for_domain(domain):
    return [s for s in SCENARIOS if s["domain"] == domain]

md = []
md.append("# 🚀 Advanced Kubernetes Playbook: Walkthrough Playbook")
md.append("\nThis document contains the complete walkthrough, problems, hints, and step-by-step solutions for all **50 tasks** in the Advanced Kubernetes interactive practice engine (25 Study Q&As and 25 Environment Scenarios). Use this guide to study advanced operator paradigms, admission webhooks, and CKS security standards alongside practicing them via `./gold.sh`.\n")
md.append("## 📌 Navigation Table of Contents")
for d in domains:
    anchor = d.lower().replace(" ", "-").replace("(", "").replace(")", "").replace("&", "and").replace("/", "-").replace(",", "")
    md.append(f"- [{d}](#{anchor})")
md.append("\n---\n")

for d in domains:
    md.append(f"## {d}")
    md.append(f"This section covers all tasks representing {d}.\n")
    
    study_qs = get_study_for_domain(d)
    scenarios = get_scenarios_for_domain(d)
    
    # 1. Study Q&As
    md.append(f"### 📝 Conceptual Study Q&As ({len(study_qs)} Tasks)")
    md.append("These tasks test your core knowledge of advanced patterns, structures, and systems details.\n")
    
    for q in study_qs:
        md.append(f"#### 🔍 {q['id']}: {q['question'][:80]}...")
        md.append(f"**Question:**\n{q['question']}\n")
        md.append(f"**Answer:**\n```\n{q['answer']}\n```\n")
        
    # 2. Environment Scenarios
    md.append(f"### 🔬 Hands-on Environment Scenarios ({len(scenarios)} Tasks)")
    md.append("These tasks require access to the shared KinD cluster (`./gold.sh`). They inject advanced challenges that you must diagnose and resolve.\n")
    
    for s in scenarios:
        md.append(f"#### 🛠️ {s['id']}: {s['title']}")
        md.append(f"**Problem Statement:**\n{s['problem']}\n")
        md.append(f"**💡 Hint:**\n> {s['hint']}\n")
        
        md.append("**Setup Injection Command:**")
        md.append(f"```bash\n{s['setup']}\n```")
        md.append("**Verification check script:**")
        md.append(f"```bash\n{s['check']}\n```")
        
        md.append(f"**🟢 Step-by-Step Solution:**\n{s['solution']}\n")
        md.append("---")
    
    md.append("\n---\n")

with open(output_file, "w") as f:
    f.write("\n".join(md))

print("Successfully compiled advanced walkthrough.md!")

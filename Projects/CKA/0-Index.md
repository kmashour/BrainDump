---
obsidianUIMode: preview
class: index-note
tier: project-note
project: "CKA Exam"
tags:
  - kubernetes/exam-index
  - obsidian/moc
---

# 🎓 CKA Exam Preparation MOC

This project workspace focuses strictly on passing the CKA (Certified Kubernetes Administrator) exam. It contains terminal setup instructions, high-speed aliases, vim settings, and topic-by-topic checklists based on the reference notes.

---

## 🛠️ Environment & Speed Setup
* **[[Vim and Terminal Setup]]** - Autocompletions, aliases, and VIM defaults for high-speed YAML editing.
---

## 🏆 Kubernetes GOLD Practice Suite
* **[[kubernetes-CKA-Gold/primer|GOLD Playbook Primer]]** - A primer on navigating the 175 curriculum-weighted CKA questions.
* **[[kubernetes-CKA-Gold/walkthrough|GOLD Walkthrough Playbook]]** - Complete reference walkthrough for all 175 CKA GOLD tasks (75 study Q&As + 100 scenarios).
* **Interactive CLI Practice Engine**: Run `kubernetes-CKA-Gold/gold.sh` in your terminal to access the suite!

---

## 🚀 Advanced Kubernetes Playbook (Out-of-Scope Concepts)
* **[[../kubernetes/primer|Advanced Playbook Primer]]** - Guide to the advanced suite covering CKS, CKAD, and custom operator designs.
* **[[../kubernetes/walkthrough|Advanced Walkthrough Playbook]]** - Complete reference walkthrough for all 50 advanced tasks (25 study Q&As + 25 scenarios).
* **Interactive CLI Practice Engine**: Run `kubernetes/gold.sh` in your terminal to access the advanced suite!

---

## 📝 Topic Exam Checklists
These checklists focus on what is tested in the exam, common pitfalls, and quick command formulas.

```dataview
TABLE topics AS "Exam Topics", status AS "Prep Status"
FROM "Projects/CKA"
WHERE class = "exam-checklist"
SORT file.name ASC
```

---

## 🏆 Mock Exam Reviews
Analysis of Lightning Labs, Mock Exams, and recovery strategies for common failure loops.

```dataview
TABLE score AS "Score", failed_questions AS "Focus Areas"
FROM "Projects/CKA"
WHERE class = "mock-review"
SORT file.name ASC
```

---

## 💡 CKA Battle-Test FAQ: Knowledge Ingestion Pipeline

### Q: Where are the practice tests ingested?
* **Source Location:** Raw practice tests, mock exams, lightning labs, and tips are located in the `inflow/docs/` directory. They are structured into modules:
  * `inflow/docs/14-Lightning-Labs/`
  * `inflow/docs/15-Mock-Exams/`
  * `inflow/docs/16-Ultimate-Mocks/`
  * `inflow/docs/17-tips-and-tricks/`
* **Target Playbook:** The ingestion pipeline automatically compiles these scattered markdown files, scenario requirements, diagnostic steps, CLI solutions, and YAML manifests into a single, cohesive, high-fidelity playbook: [Practice Playbook - Lightning Labs and Mock Exams.md](file:///home/karim/Desktop/BrainDump/Projects/CKA/Practice%20Playbook%20-%20Lightning%20Labs%20and%20Mock%20Exams.md).
* **Topic Labs:** Other topic-specific lab exercises are processed and deduplicated into [Practice Playbook - Topic Labs.md](file:///home/karim/Desktop/BrainDump/Projects/CKA/Practice%20Playbook%20-%20Topic%20Labs.md).

### Q: Can this BrainDump work as RAG for the AI assistant?
* **Yes.** This repository functions as a structured "Second Brain" or Retrieval-Augmented Generation (RAG) knowledge base.
* **How it works:** Because the Antigravity AI coding assistant can search, index, and read all files inside this workspace, the structured layouts, reference sheets, exam checklists, commands, and diagrams are loaded into the agent's context window.
* **Benefits:** This grounding prevents LLM hallucinations, ensuring that code generation, terminal configurations, and troubleshooting steps match the specific, battle-tested Kubernetes setups, versions, and configurations defined in this vault.

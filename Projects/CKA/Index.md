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

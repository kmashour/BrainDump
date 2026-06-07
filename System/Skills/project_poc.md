# SKILL: Project-Based Verification PoC Compilation

This skill guides the creation of standalone implementation projects to demonstrate system design and CKA concepts without cluttering main reference guides.

---

## 📋 Execution Steps
1. **Decouple PoCs:** Do not put massive configuration sheets and terminal commands directly inside core reference notes.
2. **Project Creation:** Create a standalone project file inside `Projects/` using the `project_note.md` template.
3. **Reference Linking:**
   - Link the project back to the core concept notes using wiki links in the frontmatter `concepts_referenced`.
   - In the core reference or landing notes, replace large command blocks with inline links pointing to the project note (e.g. `*See complete implementation in [[Projects/Path/Project_File.md]]*`).
4. **Verifiable Quality:** Include Nginx blocks, Terraform/Ansible scripts, and curl checking scripts that are completely correct and runnable.

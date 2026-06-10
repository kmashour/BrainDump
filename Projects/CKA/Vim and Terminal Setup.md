---
obsidianUIMode: preview
class: exam-guide
tier: project-note
project: "CKA Exam"
tags:
  - kubernetes/exam-setup
  - terminal/vim
---

# Vim and Terminal Setup

**Breadcrumbs:** [[Projects/CKA/0-Index|🏠 Index]] > [[Projects/CKA/Index|🎓 CKA Exam MOC]] > **Vim and Terminal Setup**

---

## 🏎️ 1. High-Speed Bash Configuration (Do this first!)
At the very start of the CKA exam, configure your terminal to enable fast autocomplete, short aliases, and dry-run templates. Run these commands immediately:

```bash
# 1. Enable kubectl auto-completion
source <(kubectl completion bash)

# 2. Setup shorthand 'k' alias and bind autocomplete to it
alias k=kubectl
complete -o default -F __start_kubectl k

# 3. Define shorthand helper variables for dry-runs and deletions
export do="--dry-run=client -o yaml"
export now="--force --grace-period=0"
```

### Verification
Test your terminal setup:
```bash
# Autocomplete check: Type 'k get' and hit Tab twice to see resources.
k get 

# Generate a deployment manifest instantly
k create deploy web-server --image=nginx $do > web-deploy.yaml

# Delete a pod instantly (zero grace period)
k delete pod nginx $now
```

---

## 📝 2. Vim Customization (`~/.vimrc`)
YAML is highly indentation-sensitive. Configure VIM to use 2-space tab indentations and avoid TAB character injections which break Kubernetes YAML specifications.

Create or update your `~/.vimrc` with these lines:
```vim
set tabstop=2 
shiftwidth=2 
expandtab
set nu
set ai
```

### Property Descriptions
* `tabstop=2`: Renders TAB characters as 2 spaces.
* `shiftwidth=2`: Inserts 2 spaces when using auto-indentation or block shifts.
* `expandtab`: Converts TAB key presses into physical spaces (critical for YAML!).
* `nu` (number): Shows line numbers on the left sidebar.
* `ai` (autoindent): Copies the indentation of the previous line when hitting Enter.

---

## 🖥️ 3. Remote Browser Desktop & SSH Hopping Setup
As of the latest exam environments, the exam is strictly administered via a remote Ubuntu desktop inside a browser tab. Standard OS shortcuts may not work or can cause issues:
* **Copy-Paste Shortcuts:** Use `Ctrl+Shift+C` to copy and `Ctrl+Shift+V` to paste within the remote Linux terminal.
* **Avoid `Ctrl + W`:** Do NOT use `Ctrl + W` to delete a word in the terminal—this will close your browser tab! Instead, use `Ctrl+Alt+Backspace` or navigate using `Alt+B` (move back a word) and `Alt+F` (move forward a word).
* **SSH Node Hopping:** Most tasks require you to SSH into a specific control plane or worker node. Always verify your shell prompt before running commands.
* **Privilege Elevation:** Elevate immediately after hopping. Many tasks require root access; use `sudo -i` once logged in to prevent permission denied errors when modifying system files (e.g., `/etc/kubernetes/manifests/kube-apiserver.yaml`).

---

## 💡 4. High-Speed VIM Tricks for YAML Editing
* **Multi-Line Indentation:**
  1. Press `Esc` to enter command mode.
  2. Press `Shift + V` to enter Visual Line Mode and select the target lines.
  3. Type `>` to shift the entire block right by 2 spaces, or `<` to shift left.
* **Block Deletion / Visual Block Mode:**
  1. Press `Esc` and move your cursor to the start of the block.
  2. Press `Ctrl + V` to enter Visual Block Mode.
  3. Select the target block area using arrow keys, then press `d` to delete.
* **Undo / Redo:**
  - Press `u` to undo the last edit.
  - Press `Ctrl + R` to redo.

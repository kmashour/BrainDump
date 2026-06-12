---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kubectl]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/tasks/extend-kubectl/kubectl-plugins/"
author: "Kubernetes Documentation"
course_title: "Certified Kubernetes Administrator (CKA)"
tags:
  - kubernetes/kubectl
  - kubernetes/deep-dive
  - kubernetes/cli
---

# kubectl - Plugins

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[kubectl]] > **Plugins**

---

## 🎯 Purpose (Why it is used)
A **kubectl plugin** allows developers and cluster administrators to write custom scripts or binary programs that extend the standard command-line capabilities of the `kubectl` tool without compiling them into the core binary. This is highly useful for automating repetitive tasks (like diagnosing network failures or listing resource custom formats) and integrating custom scripts natively as subcommands.

---

## ⚙️ Functionality (What it is doing)

### 1. Naming and Discovery
Kubernetes matches plugins based on file naming conventions in your local shell's environment path:
- **Naming Prefix:** A plugin must be an executable whose filename starts with the prefix `kubectl-` (e.g. `kubectl-foo`).
- **Subcommand Mapping:** Hyphens in the filename translate to subcommands in `kubectl`. For example, `kubectl-foo-bar` is executed via:
  ```bash
  kubectl foo bar
  ```
- **PATH Resolution:** When you run a subcommand that `kubectl` does not natively support, it scans all folders in your local `$PATH` environment variable for an executable matching `kubectl-<subcommand>`. If found, it runs the executable, forwarding all flags and arguments.

### 2. Verification and Troubleshooting
To verify that plugins are correctly located, executable, and free from namespace collisions (e.g. duplicate plugin names in different PATH folders):
```bash
kubectl plugin list
```
*Note: Any duplicates or binaries without executable permissions (`+x`) will be shown as warnings.*

---

## 🏎️ CKA Exam Setup and Verification (Bash Example)

### Step 1: Create a shell script plugin
Write a script named `kubectl-ping-all` that lists all pods and pings their IP:
```bash
cat << 'EOF' > kubectl-ping-all
#!/bin/bash
echo "Scanning Pod IPs in current namespace..."
kubectl get pods -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.podIP}{"\n"}{end}'
EOF
```

### Step 2: Make it executable and place it in the PATH
```bash
chmod +x kubectl-ping-all
sudo mv kubectl-ping-all /usr/local/bin/
```

### Step 3: Run the plugin
```bash
kubectl ping-all
```

---

*Read more in [0-1_kube_api_and_kubectl.md](../Reference%20Notes/0-1_kube_api_and_kubectl.md#9-extending-kubectl-with-plugins)*

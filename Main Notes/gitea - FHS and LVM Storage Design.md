---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[gitea]]"
sub_type: architecture
source_type: documentation
source_url: "https://docs.gitea.com/administration/dir-to-var-symlink"
author: "Linux Filesystem Standard"
course_title: "RHCSA Storage Architecture"
tags:
  - git/gitea
  - storage/lvm
---

# gitea - FHS and LVM Storage Design

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[gitea]] > **FHS and LVM Storage Design**

---

## 📑 FHS and LVM Storage Design

Deploying version control systems on Red Hat Enterprise Linux requires managing storage limits to avoid filling the operating system's root disk.

### 1. Partition Architecture
* **System Root (`/var`):** 50GB allocated to the system disk. High write loads (like multi-GB repositories) can easily exhaust this space and crash the OS.
* **Large Partition (`/app`):** 400GB of LVM storage on `/dev/sdb1`.

### 2. Symlink Abstraction
We maintain FHS standards by placing physical directories on `/app` and pointing the standard paths to them via symbolic links:

```text
/var/lib/gitea  ───(Symbolic Link)───>  /app/gitea (400GB LVM Partition)
```

```bash
# Setup physical storage
sudo mkdir -p /app/gitea/{custom,data,log}
sudo ln -s /app/gitea /var/lib/gitea
```

---

## 📁 Directory Traversal (FACL)

Because the `/app` root directory is owned by `root:root` with permissions like `700`, unprivileged services like the `git` user cannot enter it. 

Instead of changing permissions for `/app` or recursively exposing other sub-folders, we grant the `git` user traversal rights (the `x` execute permission) using a **File Access Control List (FACL)**:

```bash
# Grant traversal permission specifically to git user
sudo setfacl -m u:git:x /app
```

*Read more in [gitea_installation_and_workflows.md](../Reference%20Notes/gitea_installation_and_workflows.md#3-filesystem-hierarchy-standard-fhs-and-storage-design)*

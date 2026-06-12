---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[configmap]]"
sub_type: core-concept
source_type: udemy
author: "Mumshad Mannambeth"
course_title: "Certified Kubernetes Administrator (CKA)"
against: []
tags:
  - kubernetes/configmap
  - kubernetes/deep-dive
---

# configmap - Injection and Volume Mounts

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[configmap]] > **Injection and Volume Mounts**

---

## 📑 ConfigMap Injection Mechanics

Kubernetes supports multiple ways to inject ConfigMap values into running Pod containers:

### 1. Environment Variables
You can inject individual keys or bulk load all keys from a ConfigMap as environment variables.
*   **Individual Keys (`valueFrom`):**
    ```yaml
    env:
    - name: DATABASE_URL
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: db_url
    ```
*   **Bulk Ingestion (`envFrom`):** Loads all keys in the ConfigMap as environment variables where the keys become environment variable names.
    ```yaml
    envFrom:
    - configMapRef:
        name: app-config
    ```

### 2. Volume Mounts
ConfigMaps can be mounted as volumes, rendering each key as a separate file inside a directory.
```yaml
spec:
  containers:
  - name: app
    image: nginx
    volumeMounts:
    - name: config-vol
      mountPath: /etc/config
  volumes:
  - name: config-vol
    configMap:
      name: app-config
```

---

## ⚙️ The Symlink and inotify Sync Mechanics

When a ConfigMap is mounted as a volume, the Kubelet ensures that updates to the ConfigMap in the API server are periodically projected into the container filesystem without rebuilding the Pod.

### Atomic Sync Workflow
Rather than writing to files directly (which could cause applications to read partial/corrupted data during a sync), Kubelet uses a layered symlink structure:
1.  **Timestamped Directories:** Kubelet downloads the new ConfigMap data into a new subdirectory named with a timestamp (e.g., `..2026_06_05_13_00_00.123456789`).
2.  **Symmetric Link Update:** It links all keys inside that subdirectory.
3.  **Atomic Symlink Swap:** It atomically updates a symbolic link named `..data` to point to the new timestamped directory.
4.  **Key Symlinks:** The user-facing files (e.g., `/etc/config/app.properties`) are actually symlinks pointing to `..data/app.properties`.

### Linux `inotify` Integration
Because the user-facing files are symlinks to a symlink, modifying the ConfigMap triggers directory-level `inotify` write events. Applications designed to reload configs dynamically must watch the **parent directory** rather than the individual file to detect the symlink swap.

---

## ⚠️ The `subPath` Eviction Pitfall

If you mount a ConfigMap file using `subPath` to avoid overwriting existing files in the directory (e.g., placing `nginx.conf` directly into `/etc/nginx/` without wiping out other files), **dynamic updates are disabled**.
*   **Why:** `subPath` uses a Linux bind-mount that locks the target file's physical **inode** at container startup. When the Kubelet updates the ConfigMap, it swaps the symlink targets, but the bind-mount inside the container remains locked to the old physical inode. The container will never see the updates.
*   **Mitigation:** Avoid `subPath` for files that require hot-reloading. Instead, mount the volume to a separate folder and use a symbolic link or a sidecar container to copy/update configuration files.

*Read more in [0-13_scheduling_logging_and_lifecycle.md](../Reference%20Notes/0-13_scheduling_logging_and_lifecycle.md#c-configmaps-decoupled-configuration)*

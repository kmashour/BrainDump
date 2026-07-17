---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[docker]]"
sub_type: use-case
source_type: udemy
source_url: "https://www.udemy.com"
author: "Udemy Instructor"
course_title: "Docker and Containerization"
against: []
tags:
  - docker/storage
  - docker/deep-dive
---

# docker - Volumes and Bind Mounts

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[docker]] > **Volumes and Bind Mounts**

---

## 📑 Persistent Storage & Host Security

Containers are ephemeral by design. To preserve application state, you must map storage out of the container's write layer.

### Storage Mount Types:
1.  **Named Volumes (Recommended for DBs):** Managed entirely by Docker inside protected host system paths. Provides superior filesystem performance.
2.  **Bind Mounts:** Maps a direct path on the host system to the container. Essential for code hot-reloading in dev.
3.  **Anonymous Volumes:** Auto-generated unique hash name by Docker, used for transient caches.

*Read more in [2-3_docker_volumes_and_storage.md](../Reference%20Notes/2-3_docker_volumes_and_storage.md#1-storage-mount-primitives)*

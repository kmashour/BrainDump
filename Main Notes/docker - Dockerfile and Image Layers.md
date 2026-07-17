---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[docker]]"
sub_type: core-concept
source_type: udemy
source_url: "https://www.udemy.com"
author: "Udemy Instructor"
course_title: "Docker and Containerization"
against: []
tags:
  - docker/dockerfile
  - docker/deep-dive
---

# docker - Dockerfile and Image Layers

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[docker]] > **Dockerfile and Image Layers**

---

## 📑 Docker Image Layers & Optimization

Docker images are structured as a read-only stack of layers, where each Dockerfile instruction that modifies the filesystem (like `RUN`, `COPY`, `ADD`) creates a new layer.

### Core Architecture & Cache Optimization:
*   **Read-Only Base Layers:** Every instruction is a delta change from the previous layer.
*   **Layer Cache:** During builds, Docker checks if the instruction string and the file hash (for `COPY`/`ADD`) match the cache. If they match, the layer is reused. If the cache is broken, all subsequent layers are forced to rebuild.
*   **Optimization Rule:** Always structure Dockerfiles to copy package managers and dependencies first, run package installs, and copy source code last.

*Read more in [2-2_dockerfile_primer_and_image_building.md](../Reference%20Notes/2-2_dockerfile_primer_and_image_building.md#2-docker-layer-caching--build-optimization)*

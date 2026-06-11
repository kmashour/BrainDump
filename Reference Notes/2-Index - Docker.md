---
obsidianUIMode: preview
class: index-note
tier: reference-note
tags:
  - docker/reference-index
  - obsidian/moc
---

# 🐳 Docker Reference MOC

**Breadcrumbs:** [[--Index--|🏠 Index]] > **Docker Reference MOC**

---

## 🏛️ Reference Modules & Frameworks

This index contains our Docker container virtualization study modules, starting from container mechanics to multi-stage builds and GitHub Actions pipelines.

- 🐋 **[Module 2-1: Docker Fundamentals & Container Mechanics](2-1_docker_fundamentals_and_containers.md)**
  * Docker Engine architecture, Client-Daemon REST communication, Container vs. VM virtualization, lifecycle commands, and container process immutability.
- 🏗️ **[Module 2-2: Dockerfile Primer & Image Building](2-2_dockerfile_primer_and_image_building.md)**
  * Dockerfile instructions, layer caching strategies, ENTRYPOINT vs. CMD parameters, image versioning tags, and image registry operations (build, commit, push).
- 💾 **[Module 2-3: Docker Volumes & Storage Mechanics](2-3_docker_volumes_and_storage.md)**
  * Persistent storage mechanisms: Anonymous Volumes, Named Volumes, and Bind Mounts, including CLI syntax (`-v` vs. `--mount`) and lifecycle scoping.
- 🔌 **[Module 2-4: Docker Networking & Multi-Container Compose](2-4_docker_networking_and_compose.md)**
  * Network drivers (Bridge, Host, None, Overlay), port-mapping primitives, and multi-container orchestration using Docker Compose configurations.
- 🚀 **[Module 2-5: Advanced Docker & CI/CD Pipelines](2-5_advanced_docker_and_github_actions.md)**
  * Layer reduction via multi-stage builds, target build stages, and automating image building and publishing workflows inside GitHub Actions.

---

## 🛠️ Verification Projects
Hands-on deployment scripts and playground setups:
- 🚀 **[Project: Secure Load-Balanced Web API](../Projects/Systems%20Design/Project%20-%20Secure%20Load-Balanced%20Web%20API.md)**

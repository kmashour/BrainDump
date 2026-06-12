---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[docker]]"
sub_type: use-case
source_type: book
source_url: "https://nigelpoulton.com/books"
author: "Nigel Poulton"
course_title: "Docker Deep Dive"
tags:
  - docker/multistage
  - docker/cicd
  - docker/deep-dive
---

# docker - Multi-Stage Builds and GH Actions

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[docker]] > **Multi-Stage Builds and GH Actions**

---

## 📑 Multi-Stage Docker Builds

Multi-stage builds utilize multiple `FROM` instructions in a single Dockerfile, allowing you to discard intermediate build environments (heavy SDKs, package managers, and compilers) and keep only the compile outputs in the final runtime container:

*   **Stage Inheritance:** A stage can build directly from a previous stage declared in the same Dockerfile.
*   **Artifact Copying:** Copying files across different base images using `COPY --from=<stage_name>`. This drops all build context and leaves only the final application binary or static files.
*   **Targeting Stages:** You can compile specific environments (e.g. `dev`, `test`, `prod`) using `docker build --target <stage_name>`.

---

## 📑 GitHub Actions Integration

Automated container registries (Docker Hub, GHCR, etc.) are populated via CI/CD workflows. A standard GitHub Actions pipeline executes the following steps:

1.  **Repository Checkout:** `actions/checkout@v3` clones the code.
2.  **Authentication:** `docker/login-action@v2` logs in to the target registry using environment secrets.
3.  **Docker Buildx Setup:** `docker/setup-buildx-action@v2` configures Buildx multi-platform builders.
4.  **Build and Push:** `docker/build-push-action@v4` builds the Dockerfile, applying `--target` and metadata labels, and pushes the final image.

*Read more in [2-5_advanced_docker_and_github_actions.md](../Reference%20Notes/2-5_advanced_docker_and_github_actions.md#1-multi-stage-docker-builds)*

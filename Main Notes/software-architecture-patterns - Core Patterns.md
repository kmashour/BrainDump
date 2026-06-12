---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[software-architecture-patterns]]"
sub_type: core-concept
source_type: documentation
author: "Level Up Coding"
course_title: "Architecture Patterns Playbook"
against: []
tags:
  - system-design/architecture
  - system-design/deep-dive
---

# Software Architecture Patterns - Core Patterns

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[software-architecture-patterns]] > **Core Patterns**

---

## 📑 The 10 Core Architectural Patterns

Here is a summary of the 10 software architecture patterns studied in this playbook:

### 1. Monolithic Architecture
- **Concept:** A single, unified codebase and execution process where all modules share a database.
- **Key Feature:** All communication is handled via fast, in-process function calls.
- **Best Use Case:** Small teams, early-stage MVPs, low-to-moderate traffic volumes.

### 2. Modular Monolith
- **Concept:** Single-deployment application structured internally as decoupled, domain-aligned modules.
- **Key Feature:** Modules have strict interface boundaries and own their data schemas within a shared database.
- **Best Use Case:** Middle-stage growth where codebase discipline is required without operational microservice overhead.

### 3. Microservices
- **Concept:** A suite of independently deployable, small services communicating over network APIs (REST, gRPC).
- **Key Feature:** Each service has its own repository, CI/CD pipeline, and private database.
- **Best Use Case:** Large engineering organizations with autonomous squads and high scalability needs.

### 4. Event-Driven Architecture (EDA)
- **Concept:** Asynchronous communication where services react to events published to a central broker.
- **Key Feature:** Complete decoupling of producer and consumer execution cycles.
- **Best Use Case:** Asynchronous pipelines, high-throughput systems, and eventual consistency models.

### 5. Serverless Architecture
- **Concept:** Ephemeral container functions (FaaS) executed on-demand and managed by cloud providers.
- **Key Feature:** Scalability matches execution request volume directly, scaling to zero when idle.
- **Best Use Case:** Unpredictable, bursty workloads, back-end background jobs, and quick prototyping.

### 6. Domain-Driven Design (DDD)
- **Concept:** Software design approach structuring code directly around business domain bounded contexts.
- **Key Feature:** Ubiquitous language mapping domain entities, aggregates, and value objects in code.
- **Best Use Case:** Systems with complex, nested business logic and long-term evolutionary life.

### 7. Clean Architecture (Ports and Adapters)
- **Concept:** Concentric architecture separating business logic from frameworks, databases, and UI.
- **Key Feature:** Core business rules (entities/use cases) are isolated and rely on interfaces (ports).
- **Best Use Case:** long-lived codebases requiring automated testing and framework independence.

### 8. Strangler Fig Pattern
- **Concept:** Intercept-and-route migration pattern to replace legacy systems incrementally.
- **Key Feature:** A routing proxy redirects API traffic slice-by-slice from the legacy monolith to new services.
- **Best Use Case:** Legacy migrations where "big bang" rewrites are too high-risk to perform.

### 9. Backend-For-Frontend (BFF)
- **Concept:** Dedicated backend services built specifically for the needs of individual client platforms.
- **Key Feature:** Downstream microservice API response aggregation and data formatting tailored to client channel constraints.
- **Best Use Case:** Applications with diverse client platforms (e.g. mobile vs web vs voice).

### 10. Command Query Responsibility Segregation (CQRS)
- **Concept:** separation of data read models (queries) from write models (commands).
- **Key Feature:** Read models are denormalized (e.g. Elasticsearch/Redis) and synchronized asynchronously via events.
- **Best Use Case:** High read-to-write ratios requiring ultra-fast, complex query execution.

---

## 📑 Comparison Matrix of Deployment and Data Models

| Pattern | Deployment Packaging | Database Boundary | Inter-component Communication | Primary Benefit |
| :--- | :--- | :--- | :--- | :--- |
| **Monolith** | Single runtime process | Single Shared DB | In-process calls (Local) | Simplicity & Low latency |
| **Modular Monolith** | Single runtime process | Separated logical schemas | In-process public interfaces | Boundary isolation, no network overhead |
| **Microservices** | Multiple containers / VMs | Private Database per service | Distributed Network RPCs | Squad autonomy & Selective scaling |
| **Serverless (FaaS)** | Ephemeral containers | Managed Cloud Databases | Event-driven triggers | Zero idle cost & Auto-scaling |
| **CQRS** | Can be decoupled services | Separate Write and Read DBs | Async message broker syncing | Extreme query performance |

*Read more in [[Reference Notes/1-7_software_architecture_patterns.md]]*

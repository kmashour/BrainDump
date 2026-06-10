---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[api-protocols]]"
sub_type: core-concept
source_type: documentation
source_url: "https://www.youtube.com/watch?v=C842vFY5kRo"
author: "Hayk Simonyan"
course_title: "System Design Course"
tags:
  - system-design/api
  - system-design/deep-dive
---

# API Protocols - REST vs GraphQL

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[api-protocols]] > **REST vs GraphQL**

---

## 📑 REST (Representational State Transfer)

REST is an architectural style designed around resources represented by network URLs. Clients make requests using HTTP verbs to manage these resources.

### Characteristics:
- **Resource-Centric:** Each resource has its own specific URL (e.g., `GET /users`, `GET /users/1/posts`).
- **Stateless:** Each request must carry all authentication and configuration details. No server session state is preserved.
- **Idempotency:** 
  - `GET`, `PUT`, `DELETE` are idempotent (repeated requests yield the same state).
  - `POST` and `PATCH` are non-idempotent (repeated requests can create multiple objects or yield differing modifications).
- **Caching:** Highly cacheable via standard HTTP caching headers (`Cache-Control`, `ETag`).

---

## 📑 GraphQL

GraphQL is an API query language and runtime developed by Facebook, structured around a single HTTP endpoint (typically `POST /graphql`).

### Characteristics:
- **Single Endpoint:** All operations are dispatched to a single controller endpoint.
- **Client-Specified Selection:** The client payload specifies the exact JSON fields to return:
  ```graphql
  query {
    user(id: "1") {
      name
      orders {
        total
      }
    }
  }
  ```
- **Eliminates Over-Fetching / Under-Fetching:** 
  - *Over-fetching:* REST endpoint returns 50 user fields when only the `name` is needed. GraphQL solves this by only selecting `name`.
  - *Under-fetching:* REST requires calling `/users/1` then `/users/1/orders` (two roundtrips). GraphQL resolves this with nested fields in one roundtrip.
- **Schema Validation:** Strictly typed schema defined using Schema Definition Language (SDL), serving as self-documenting code.

---

## 📑 Comparison Matrix

| Feature | RESTful APIs | GraphQL |
| :--- | :--- | :--- |
| **Endpoint Design** | Multiple endpoints (nouns-based URLs) | Single endpoint (typically `POST /graphql`) |
| **Data Fetching** | Fixed server-defined payloads | Flexible client-defined query payloads |
| **Versioning** | Path/header-based (e.g. `/v1/`, `/v2/`) | Single evolutionary schema (deprecated fields) |
| **Caching** | Built-in HTTP level caching | Complex client-side caching (e.g., Apollo Client) |
| **Payload Size** | Larger (contains unused database fields) | Minimal (contains only requested fields) |

*Read more in [[Reference Notes/1-5_api_protocols_and_grpc.md#1-core-api-paradigms]]*

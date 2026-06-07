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

# API Protocols - gRPC and Protobuf

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[api-protocols]] > **gRPC and Protobuf**

---

## 📑 gRPC & HTTP/2 Foundation

gRPC (Google Remote Procedure Call) is a modern, open-source RPC framework that replaces REST for internal microservice communication. It requires **HTTP/2** as its transport layer, which unlocks key performance improvements:

### 1. Multiplexing
Unlike HTTP/1.1 (where each request-response cycle blocks a TCP connection), HTTP/2 allows sending multiple bidirectional streams concurrently over a single TCP connection. This eliminates the head-of-line blocking issue.

### 2. HPACK Header Compression
HPACK compresses headers by maintaining a dynamic lookup index between client and server, reducing byte transmission size.

### 3. Bidirectional Streaming
gRPC natively supports four communication methods:
- **Unary:** Simple request-response.
- **Server Streaming:** Client sends one request, server streams multiple responses (e.g. log streams).
- **Client Streaming:** Client streams multiple requests, server sends one response (e.g. file uploads).
- **Bidirectional Streaming:** Both client and server send streams concurrently.

---

## 📑 Protocol Buffers (Protobuf)

gRPC uses **Protocol Buffers** as its serialization format instead of JSON:
- **Binary Encoding:** Protobuf compresses messages into small binary payloads. It strips string keys and replaces them with numeric field tags (`1`, `2`, `3`), resulting in a $60\% - 80\%$ payload size reduction compared to JSON.
- **Schema Contracts:** Interface contracts are defined in `.proto` files:
  ```protobuf
  syntax = "proto3";
  
  message UserRequest {
    int32 id = 1;
  }
  
  message UserResponse {
    string name = 1;
    string email = 2;
  }
  
  service UserService {
    rpc GetUser (UserRequest) returns (UserResponse);
  }
  ```
- **Generated Stubs:** Code generators convert the schema directly into client stubs and server boilerplate skeletons, ensuring immediate cross-language compatibility (Go, Java, Python, Node, etc.).

*Read more in [System Design Fundamentals](../Reference%20Notes/17_system_design_fundamentals.md#c-grpc-protocol-buffers-http2-multiplexing)*

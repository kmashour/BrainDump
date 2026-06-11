---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "infra"
  - "networking"
related_concepts:
  - "[[api-protocols]]"
against:
  - "[[api-protocols]]"
reference_guides:
  - "[[Reference Notes/1-8_distributed_communication_and_queues.md]]"
tags:
  - system-design/communication
  - status/completed
---

# Distributed Communication & Queues

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **Distributed Communication & Queues**

---

## 🎯 Purpose (Why it is used)
Distributed Communication & Queues provide the architectural foundation for asynchronous, event-driven interactions in scale-out systems. By routing messages through intermediate brokers, services can communicate without blocking, decoupling producers and consumers in both time and network address space.

---

## ⚙️ Functionality (What it is doing)
- **Message Buffering:** Temporarily stores messages in broker queues or commit logs during consumer slow-downs or offline periods.
- **Asynchronous Execution:** Allows producers to fire-and-forget events, freeing execution threads immediately.
- **Load Balancing (Competing Consumers):** Spreads message processing workloads evenly across multiple competing worker instances.
- **Event Broadcasting (Pub/Sub):** Replicates and delivers a single event to multiple independent subscriber systems.
- **Ordered Log Storage (Streaming):** Persists events in sequential commit logs, allowing replayability and event streaming.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Asynchronous brokers sit between independent microservices. Producers write messages to the broker, which handles persistence, routing, and delivery to consumers. Caching tiers (like Redis) or database layers are typically placed at consumer boundaries to store the processed state.

---

## 🧩 Problem Solver (What problem it solves)
- **Tight Coupling:** Solves compile-time and runtime dependencies between services.
- **Cascading Outages:** Prevents thread pools on upstream services from being exhausted when downstream services experience latency spikes or crashes.
- **Traffic Spikes:** Acts as a shock absorber/buffer, preventing database and app nodes from collapsing under sudden request surges.

---

## 🟢 Operational Impact (What will happen with it operating)
Systems achieve higher resilience, better hardware utilization, and elastic scalability. Features like billing, email dispatch, and reports processing are offloaded to background workers, keeping user-facing APIs snappy.

---

## 🔴 Failure Impact (What will happen without it)
Without asynchronous communication, all service calls must be synchronous. A crash or delay in a single deep dependency (e.g., email gateway) blocks caller threads all the way up to the API Gateway, causing system-wide timeouts (`504 Gateway Timeout`), thread starvation, and application crashes.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Distributed Communication & Queues**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[distributed-communication]]
SORT file.name ASC
```

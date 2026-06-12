---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[caching]]"
sub_type: core-concept
source_type: documentation
source_url: "https://www.youtube.com/watch?v=C842vFY5kRo"
author: "Hayk Simonyan"
course_title: "System Design Course"
against: []
tags:
  - system-design/caching
  - system-design/deep-dive
---

# Caching - Strategies and Eviction Policies

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[caching]] > **Strategies and Eviction Policies**

---

## 📑 Caching Write-Read Patterns

Developers implement specific caching patterns to balance latency, transaction safety, and eventual consistency:

### 1. Cache-Aside (Lazy Loading)
- **Mechanics:** The application queries the cache first.
  - *Cache Hit:* Data is returned immediately.
  - *Cache Miss:* The application queries the database, writes the result to the cache, and returns it.
- **Trade-offs:** 
  - **Pros:** Cache only contains requested data; server crashes don't bring down writes.
  - **Cons:** Cache miss penalty (double latency hop on first read); potential for stale data if database updates occur outside the cache TTL cycle.

### 2. Write-Through
- **Mechanics:** The application writes data to the cache. The cache synchronously writes it to the database before confirming success to the application.
- **Trade-offs:**
  - **Pros:** No stale data; high consistency.
  - **Cons:** High write latency (double write penalty).

### 3. Write-Behind (Write-Back)
- **Mechanics:** The application writes to the cache, which acknowledges the write instantly. An asynchronous process subsequently batches and writes updates to the database.
- **Trade-offs:**
  - **Pros:** High write throughput; near-zero write latency.
  - **Cons:** Risk of data loss if the cache server crashes before data is persisted to the database.

---

## 📑 Cache Eviction Policies

When cache memory fills up, the system evicts keys using specific policies:
- **LRU (Least Recently Used):** Tracks access timestamps and evicts keys that haven't been queried for the longest duration.
- **LFU (Least Frequently Used):** Tracks hit counters and evicts keys with the lowest query frequency.
- **FIFO (First In First Out):** Discards keys in the order they were inserted, regardless of access patterns.

---

## 📑 Critical Caching Pitfalls

- **Cache Avalanche:** Occurs when many keys expire concurrently, or the cache tier crashes, causing all request traffic to overwhelm the database. *Defenses:* Randomize TTLs (Jitter) and configure HA cache clusters.
- **Cache Stampede (Thundering Herd):** Multiple application threads concurrently execute database queries on a cache miss for the same key. *Defenses:* Implement Mutex Locking so only the first thread queries the database while others wait for the cache to update.
- **Cache Penetration:** Requests query keys that do not exist in either cache or database (e.g. scanner exploits). *Defenses:* Cache null results with a short TTL, or use **Bloom Filters** to quickly reject non-existent keys at the gateway.

*Read more in [Caching & CDNs](../Reference%20Notes/1-4_caching_and_content_delivery_networks.md#1-caching-topologies--write-strategies)*

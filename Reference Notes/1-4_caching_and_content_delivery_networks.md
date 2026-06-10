---
domains:
  - "database"
  - "networking"
  - "infra"
---

# Module 1-4: Caching & Content Delivery Networks (CDNs)

This module covers the core concepts of caching, write patterns (Cache-Aside, Write-Through, Write-Behind), eviction policies, cache stampede mitigations, and Content Delivery Network (CDN) edge routing.

---

## 🗺️ Cognitive Map: How to Think About Caching & CDNs

```mermaid
graph TD
    subgraph cache_flow["Caching & CDN Architecture"]
        Client["Client Request"] --> DNS["DNS Anycast Routing"]
        DNS --> CDN{"CDN Edge Cache?"}
        CDN -- "Hit" --> Client
        CDN -- "Miss" --> Origin["Origin Load Balancer"]
        Origin --> App["Application Server"]
        App --> Cache{"Cache Tier (RAM)?"}
        Cache -- "Hit" --> App
        Cache -- "Miss" --> DB["Database Server"]
    end
```

---

## 1. Caching Topologies & Write Strategies

Caching stores hot, transient data in high-speed memory (RAM) to avoid expensive database read operations and reduce latency.

### A. Caching Read-Write Patterns
1. **Cache-Aside (Lazy Loading):**
   - *Flow:* The application queries the cache first. On a *Cache Hit*, data is returned immediately. On a *Cache Miss*, the application fetches the data from the database, writes it to the cache, and returns it to the client.
   - *Trade-off:* Cache only contains requested data, but misses incur a double-hop latency penalty, and data can become stale if updated directly in the DB.
2. **Write-Through:**
   - *Flow:* The application writes data to the cache, and the cache immediately writes it synchronously to the database in the same transaction.
   - *Trade-off:* Data is never stale, but write latency is high due to synchronous double-writing.
3. **Write-Behind (Write-Back):**
   - *Flow:* The application writes to the cache, which acknowledges immediately. An asynchronous background process batches and writes updates to the database.
   - *Trade-off:* Extremely fast write speeds and high write throughput, but data loss is possible if the cache server crashes before database synchronization completes.

```mermaid
sequenceDiagram
    autonumber
    Client->>Application: HTTP GET /resource/1
    Application->>Cache: Check key: resource_1
    alt Cache Hit
        Cache-->>Application: Return Cached Data
        Application-->>Client: HTTP 200 OK (Cache HIT)
    else Cache Miss
        Cache-->>Application: Key Not Found
        Application->>Database: SELECT * FROM resources WHERE id = 1
        Database-->>Application: Return DB Record
        Application->>Cache: SET key: resource_1 with TTL
        Application-->>Client: HTTP 200 OK (Cache MISS)
    end
```

### B. Cache Eviction Policies
When the cache reaches memory capacity, items are evicted based on policies:
- **Least Recently Used (LRU):** Discards items that haven't been accessed for the longest time.
- **Least Frequently Used (LFU):** Discards items with the lowest access count.
- **First In First Out (FIFO):** Discards items in the order they were inserted.

---

## 2. Caching Failure Patterns

* **Cache Avalanche:** Occurs when many keys expire at once, or the cache tier crashes, causing a massive surge of concurrent queries to hit the database, leading to outages. *Mitigations:* Add random time variables (Jitter) to TTLs, and use high-availability cache clusters.
* **Cache Stampede (Thundering Herd):** Occurs when multiple application threads concurrently execute database queries on a cache miss for the exact same key. *Mitigations:* Use mutex locks so only one request queries the database for a cache miss while others wait for the cache to update.
* **Cache Penetration:** Occurs when clients query keys that do not exist in either cache or database (e.g. scanner attacks). *Mitigations:* Cache empty/null results with a short TTL, or intercept queries with a **Bloom Filter** at the gateway level.

---

## 3. Content Delivery Networks (CDNs)

A CDN is a distributed network of edge proxy servers that cache and serve static content (images, JS/CSS, HTML) geographically close to users.
- **Pull CDNs:** The edge server pulls static files from the origin server on the first cache miss, caches it for subsequent users, and returns it.
- **Push CDNs:** The origin server pushes new assets to the CDN edge nodes manually when files are uploaded or updated.
- **Anycast Routing:** CDNs share a single IP address across all edge locations. BGP routing automatically forwards client packets to the nearest physical edge server, minimizing network hops.

---

## 🛠️ Hands-on Verification Project

To verify and inspect the cache control headers and CDN revalidation triggers, refer to the client verification commands:
- [[Projects/Systems Design/Project - Secure Load-Balanced Web API.md#1-verification-of-caching-and-cdn-headers|Caching and CDN header checks]]

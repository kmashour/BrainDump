---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[api-security]]"
sub_type: core-concept
source_type: documentation
source_url: "https://www.youtube.com/watch?v=C842vFY5kRo"
author: "Hayk Simonyan"
course_title: "System Design Course"
against: []
tags:
  - system-design/security
  - system-design/deep-dive
---

# API Security - Defenses

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[api-security]] > **Defenses**

---

## 📑 Core API Defense Shields

To build secure production architectures, requests must pass through several layers of security defense:

### 1. Rate Limiting
- **Mechanism:** Imposes a limit on the number of requests a client can make in a specified time window (e.g., 100 requests per minute).
- **Levels:** Implemented at the user account, IP address, endpoint, or global cluster level.
- **Protection:** Prevents Denial of Service (DoS) attacks, brute-force login attempts, and API scraping.

### 2. CORS (Cross-Origin Resource Sharing)
- **Mechanism:** A browser-side security specification. The server returns HTTP headers (e.g., `Access-Control-Allow-Origin: https://app.demo.com`) defining which frontend domains are allowed to read the API responses.
- **Protection:** Prevents rogue websites from reading authenticated API data via client browsers.

### 3. Input Parameterization (Injection Defense)
- **Mechanism:** Ensures that user input is never concatenated directly into SQL or NoSQL database commands. Instead, developers use prepared statements (parameterization) or ORM models.
- **Protection:** Defends against SQL/NoSQL injections where attackers try to read or delete database tables by injecting logical statements.

### 4. Firewalls (WAF)
- **Mechanism:** Web Application Firewalls inspect incoming L7 traffic at the network edge, matching payloads against known malicious signatures (e.g., checking for shell commands, SQL verbs, or strange User-Agents).
- **Protection:** Shields application servers from direct exploit attempts and generic automated web attacks.

### 5. Private Networks & VPNs
- **Mechanism:** Moves critical APIs, administration panels, and database nodes completely off the public internet, routing access through a virtual private network (VPN).
- **Protection:** Guarantees that internal services are physically unreachable by external hosts.

### 6. CSRF (Cross-Site Request Forgery) Tokens
- **Mechanism:** Pairs cookie authentication with a cryptographically secure, random, one-time token that must be sent in request headers for all state-changing operations (POST/PUT/DELETE).
- **Protection:** Prevents malicious pages from tricking a user's browser into executing authenticated transactions (e.g., money transfers).

### 7. XSS (Cross-Site Scripting) Sanitization
- **Mechanism:** Sanitizes and HTML-encodes all user-provided strings before saving them to the database or outputting them to a browser.
- **Protection:** Prevents attackers from injecting JavaScript payloads (e.g., in a comment field) that execute in the browsers of other users who view the content.

*Read more in [[Reference Notes/1-6_access_control_and_api_security.md#2. Infrastructure & API Hardening]]*

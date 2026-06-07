---
domains:
  - "security"
---

# Module 22: Access Control & API Security

This module covers identity verification and security hardening at the application and network layers, detailing authentication models, authorization frameworks, and common defense-in-depth mitigation strategies.

---

## 🗺️ Cognitive Map: How to Think About Security Guards

```mermaid
graph TD
    subgraph security_pipeline["Request Shield Pipeline"]
        Client["Incoming Client Request"] --> Shield1["Rate Limiter (Volume check)"]
        Shield1 --> Shield2["WAF / Firewall (Malicious pattern check)"]
        Shield2 --> Shield3["CORS Validator (Origin check)"]
        Shield3 --> AuthN["Authentication (AAA - Who are you?)"]
        AuthN --> AuthR["Authorization (RBAC/ABAC - What can you do?)"]
        AuthR --> API["Secure Backend Service"]
    end
```

---

## 1. Access Management: AAA Foundation

Security systems rely on the AAA framework:
* **Authentication (AuthN):** Verification of identity (proves *who* the entity is).
- **Authorization (AuthR):** Verification of permissions (proves *what* the entity can do).
- **Accounting (Auditing):** Tracking and logging actions performed by authenticated users.

### A. Authentication Paradigms
- **Basic Authentication:** Credentials sent as Base64-encoded strings (`username:password`) in the `Authorization` header. Insecure without TLS encryption.
- **Digest Authentication:** Uses challenge-response hashing (MD5) to avoid transmitting credentials in plain text.
- **API Keys:** Unique identifier strings issued to consumers. Lightweight but requires database/caching lookups to invalidate selectively.
- **Session-Based Authentication:** Stateful. The server verifies credentials, generates a session record in a memory store (e.g. Redis), and returns a session ID in a browser cookie. The server must check the session database on every request.
- **Token-Based Authentication (JWT):** Stateless. The server returns a signed JSON Web Token (JWT). The client includes it in the `Authorization: Bearer <token>` header. The server verifies the token signature cryptographically using a public/private key or shared secret, eliminating database lookups.
  - *Access vs. Refresh Tokens:* Short-lived access tokens (e.g. 15 minutes) reduce leak window. Long-lived refresh tokens (stored in secure `HttpOnly` cookies) are checked against a stateful store to renew access tokens.

```mermaid
graph TD
    subgraph client_zone["Client App"]
        Client["Client App"]
    end

    subgraph auth_zone["Identity Provider (Auth Server)"]
        AuthServer["Auth Server"]
        DB_Session["Session/Token Store"]
        AuthServer <-->|"Check/Invalidate Refresh Tokens"| DB_Session
    end

    subgraph resource_zone["Resource Provider (API Server)"]
        APIServer["API Server"]
    end

    %% Flow 1: Authentication
    Client -->|"Step 1: POST /login (Credentials)"| AuthServer
    AuthServer -->|"Step 2: Returns Access Token (Short-lived, memory) and Refresh Token (Long-lived, HttpOnly Cookie)"| Client

    %% Flow 2: Accessing Resource
    Client -->|"Step 3: GET /resource with Bearer Access Token"| APIServer
    APIServer -->|"Step 4: Stateless Validation (Verify signature locally using public key, no DB call)"| APIServer
    APIServer -->|"Step 5: Returns Resource"| Client

    %% Flow 3: Refreshing Token
    Client -->|"Step 6: POST /refresh with HttpOnly Refresh Token"| AuthServer
    AuthServer -->|"Step 7: Stateful Verification (Check token store/database validity)"| AuthServer
    AuthServer -->|"Step 8: Returns new Access Token"| Client
```

### B. Authorization Models
- **Role-Based Access Control (RBAC):** Permissions are bound to logical roles (e.g. `admin`, `editor`, `reader`), and users are assigned to roles. Highly audit-friendly.
- **Attribute-Based Access Control (ABAC):** Evaluates attributes of the subject, resource, and context (e.g. "Department = Finance", "Resource = Secret", "Time = Working Hours"). Extremely flexible but complex to implement.
- **Access Control Lists (ACL):** Associates individual permissions directly with specific resources (e.g. file read/write permissions mapped per user ID).

### C. OAuth 2.0 & OpenID Connect (OIDC)
- **OAuth 2.0:** A delegated authorization framework. Allows third-party client applications to access API scopes on a user's behalf without credentials sharing (trades authorization codes for access tokens).
- **OpenID Connect (OIDC):** An identity verification layer built on top of OAuth 2.0. Adds an `id_token` (JWT format containing user profile info) to verify user authentication.

```mermaid
graph TD
    User["End User"]
    Client["Client App (Relying Party)"]
    AuthServer["Identity and Auth Server (OpenID Provider)"]

    %% Flow steps
    User -->|"1. Initiates login"| Client
    Client -->|"2. Redirects to Auth Server"| User
    User -->|"3. Authenticates and grants consent"| AuthServer
    AuthServer -->|"4. Redirects with Authorization Code"| Client
    Client -->|"5. Token Exchange: Send Auth Code and Client Secret"| AuthServer
    AuthServer -->|"6. Returns Access Token and ID Token (JWT)"| Client
```

---

## 2. Infrastructure & API Hardening

1. **Rate Limiting:** Protects systems from brute-force and Denial of Service (DDoS) requests by capping request count per client IP or session (e.g. using Token Bucket or Leaky Bucket algorithms).
2. **CORS (Cross-Origin Resource Sharing):** A browser-enforced security mechanism restricting which external origins can query your API. Enforced via HTTP handshake headers (`Access-Control-Allow-Origin`).
3. **Injection Defenses:** Prevents SQL/NoSQL Injection by separating database queries from parameter data using Parameterized Queries or ORM mapping.
4. **Firewalls & WAFs:** Web Application Firewalls inspect HTTP headers, payloads, and cookies to block known attack vectors (e.g. SQLi strings, XSS payloads).
5. **VPNs & Network Segregation:** Isolates internal admin APIs behind virtual private networks, blocking public-internet routing.
6. **CSRF (Cross-Site Request Forgery):** Prevents session hijack commands by verifying custom CSRF tokens sent in headers alongside cookies.
7. **XSS (Cross-Site Scripting):** Sanitizes user-generated inputs to prevent malicious scripts from executing in client browsers, and protects sensitive cookies via `HttpOnly` flags.

---

## 🛠️ Hands-on Verification Project

To verify and inspect the complete, production-grade hands-on configuration files for security hardening (Nginx rate limits, CORS response headers, parameterized backend SQL queries, JWT parsing), refer to:
- [[Projects/Systems Design/Project - Secure Load-Balanced Web API.md#1-nginx-load-balancer-and-gateway-configuration-nginxconf|Nginx rate limiting and CORS configuration]]
- [[Projects/Systems Design/Project - Secure Load-Balanced Web API.md#2-secure-api-web-server-python---fastapi|SQL Parameterization and JWT verify token verification logic]]


### (6 Minutes) | How JWTs Work, the Advantages, the Tradeoffs, Where They Shine, and When Not to Use Them

![](https://substackcdn.com/image/fetch/$s_!yLV0!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faa58aa08-bd21-454c-9e82-1d7ba2fedfaa_1292x266.png)

---

## Does Your Resume Pass the ATS Filter?

##### Presented by Kickresume

![](https://substackcdn.com/image/fetch/$s_!Z7ex!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F958d0d06-1234-4d40-a55c-bb92ac3a666d_1079x892.png)

Most resumes get filtered out by applicant tracking systems (ATS) before they reach a human. If you **want more interviews**, your resume needs to **pass the first test**. And that’s exactly what [Kickresume](https://lucode.co/ats-resume-checker-z7nl) ‘s **ATS Resume Checker** is built for.

☑ An instant ATS score ☑ A breakdown of missing keywords ☑ Formatting issues flagged ☑ Structural flaws identified ☑ Real-time suggestions to improve your chances

---

## JWT Clearly Explained

Your API needs to know who’s making the request without checking a central session store each time.

JSON Web Tokens (JWTs) make that possible.

They’re compact, signed packages of identity and permissions that any service can verify locally.

Each token carries its own proof, removing the need for shared session storage. But it also introduces new challenges around revocation, expiration, and security.

## From Centralized Sessions to Stateless Tokens

Before JWTs, most authentication revolved around **server-side sessions**. When a user logged in, the server created a record in memory or a database and sent back a small session ID, usually stored in a cookie. Every request sent that ID, and the server looked it up to recall the user.

![](https://substackcdn.com/image/fetch/$s_!yK7L!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F51821148-262a-45af-8543-24812b0b9877_2000x1339.png)

This model worked well for early web apps, where one server handled all requests. But as systems grew more complex, it started to break down:

- **Shared state** → Multiple servers needed access to the same session store, adding caching layers or sticky sessions.
- **Cross-service access** → Each service had to reach into the central session store to verify users, creating tight coupling.
- **Global latency** → Every request depended on a lookup, even for simple identity checks.

JWTs solved these problems by moving identity data into a **self-contained, signed token**.

Each service can verify it locally with a shared secret or public key; no lookups, no coordination, just stateless authentication that scales naturally.

## How JWTs Work

A **JSON Web Token (JWT)** is a small, encoded string that carries a user’s identity and permissions in a way that any service can verify without contacting a central database.

A JWT is made up of **three parts**, separated by dots:

`header.payload.signature`

- **Header** → Describes the token type (`JWT`) and the signing algorithm (e.g. `HS256` or `RS256`).
- **Payload** → Contains the **claims**, which are pieces of information about the user or entity. These include both standardized fields and custom ones.
- **Signature** → **Proof of authenticity**. The server signs the encoded header and payload using a secret (HMAC) or private key (RSA/ECDSA). When a service verifies the token, it recomputes the signature; if it matches, the token is valid and untampered.

### The Workflow

1. **Login** → The client authenticates with valid credentials.
2. **Issue** → The server issues a JWT containing identity and claims, signed with its key.
3. **Store** → The client saves the token (commonly in a secure cookie or memory).
4. **Send** → Each API call includes the token, usually as `Authorization: Bearer <token>`.
5. **Verify** → The receiving service validates the signature and claims (`exp`, `iss`, `aud`).
6. **Authorize** → If valid, the service trusts the identity and grants access.

![](https://substackcdn.com/image/fetch/$s_!3P2H!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3da5cd50-8928-4910-9dae-00eda340e56b_2000x1797.png)

JWTs enable **stateless authentication**, which means there is no shared session store or database lookup required. Any service with the signing key (or public key) can verify a token locally.

Importantly, JWTs are **signed, not encrypted**.

Anyone with the token can read its contents, but only someone with the signing key can alter them. This design makes JWTs fast and verifiable, but unsuitable for storing sensitive data.

Each token carries everything needed to prove who the user is and what they’re allowed to do.

## The Key Advantages

- **Stateless by design →** Each token carries its own claims, so servers don’t track sessions. Any instance can verify a token locally, making horizontal scaling effortless.
- **Fast to verify →** Checking a cryptographic signature is faster than querying a session table or cache, reducing latency and backend load.
- **Cross-domain and SSO friendly →** JWTs aren’t tied to a single domain, so they fit naturally into Single Sign-On (SSO) and multi-service systems that share the same identity provider.
- **Compact and portable →** Tokens are small, URL-safe, and JSON-based, so they travel easily in headers or URLs across browsers, devices, and third-party clients.
- **Trust built in →** Each token is signed, allowing any service that trusts the issuer to validate it without a network call.
- **Universal support →** JWTs follow an open standard (RFC 7519) with libraries available in nearly every stack.

## The Tradeoffs

- **No built-in session control →** Once issued, a JWT stays valid until it expires. You can’t revoke it server-side without adding a blacklist or shortening its lifetime.
- **No sliding sessions →** Because tokens are stateless, they can’t auto-extend like traditional sessions. To keep users logged in, you need a refresh token system.
- **Bigger payloads →** JWTs are often hundreds of bytes, not a short ID. Sending them with every request increases bandwidth use and can hit header size limits if claims are verbose.
- **Payload is readable →** Anyone with the token can decode its contents. While the signature prevents tampering, it doesn’t hide data. It’s important to never include secrets or personal information without an extra encryption layer.
- **Risk of impersonation →** If an attacker steals a valid token, they can use it to impersonate the user until it expires. Storing tokens securely (HTTP-only cookies, short TTLs, and HTTPS) helps contain the risk.
- **Outdated roles or access →** If a user’s permissions change, old tokens still reflect the previous state until they expire or are reissued.
- **Implementation pitfalls →** Common mistakes include skipping signature checks, using weak algorithms, or failing to validate claims like `exp` and `iss`. Small misconfigurations can open large security holes.

## When JWTs Shine

JWTs work best in systems that need to scale, span multiple services, or support many kinds of clients.

They’re not a default choice; but when used in the right context, they simplify authentication without slowing things down.

Here are the best use cases for JWTs:

- **Distributed backends →** In a microservice or serverless architecture, each service can verify the same token locally using a shared key.
- **APIs and mobile apps →** JWTs travel well in HTTP headers and don’t depend on cookies, making them ideal for mobile, IoT, or third-party integrations that need to authenticate outside a browser.
- **Single Sign-On (SSO) →** JWTs power most modern SSO systems (like OpenID Connect). A single identity provider can issue tokens that multiple services trust, enabling seamless logins across domains.
- **Service-to-service authentication →** Backend systems can issue and validate JWTs to authenticate calls between internal services.
- **High-throughput APIs →** For APIs handling thousands of requests per second, verifying a JWT signature is faster and cheaper than querying a database for every session lookup.

## When Not to Use JWTs

JWTs aren’t a one-size-fits-all solution. In some systems, their stateless nature creates more problems than it solves.

Here’s when you’re better off with traditional sessions or other approaches:

- **You need instant logout or revocation** → JWTs can’t be invalidated before their expiry without extra systems like blacklists or key rotation, making server sessions safer for apps that require instant logout.
- **User permissions change frequently** → A JWT’s claims are fixed when it’s issued. If a user’s role or access level changes, old tokens still carry outdated permissions until they expire. In fast-changing environments, that lag can create security gaps.
- **You handle sensitive data in the token** → Anyone who gets the token can read its payload, so they’re unsuitable for confidential or personal data unless you add an extra encryption layer (JWE).
- **You don’t need distributed scale** → For small or single-server apps, using JWTs adds unnecessary complexity. A simple session ID stored in an HTTP-only cookie is easier to implement and revoke.

## Recap

JWTs replace server-stored sessions with self-contained, signed tokens that any service can verify locally.

They’re fast, scalable, and ideal for distributed systems where services must trust the same identity without constant lookups.

But they come with tradeoffs which make them risky for apps that need fine-grained control or immediate session invalidation.

![](https://substackcdn.com/image/fetch/$s_!UzRv!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72135251-48a9-4359-a3d0-f1450bed1175_2000x1474.png)

JWTs aren’t better or worse than server sessions; they serve different needs.

The best choice depends on whether your system values **stateless scale or centralized control** more.

---

Subscribe to get simple-to-understand, visual, and engaging system design articles straight to your inbox:
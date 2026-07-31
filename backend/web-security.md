# Web & application security

Senior loops probe *"how do you secure a web app,"* and for regulated / FinTech work
(PII, payments, RBI/PCI) it's central, not a footnote. This guide is organized around
the **OWASP Top 10:2025** plus the authentication, injection, and browser-security
topics interviewers push hardest on. It spans backend, frontend, and infra — security
is cross-cutting.

## OWASP Top 10:2025 — the current list

Released January 2026 (first revision since 2021). Know the categories and the notable
changes — interviewers who follow security will expect the 2025 framing:

1. **A01 Broken Access Control** — #1 for four editions running, and now **absorbs
   SSRF**. Enforce authorization **server-side on every request**, deny by default, and
   watch **IDOR** (object-level authz: check the caller actually owns the object).
2. **A02 Security Misconfiguration** — rose to #2. Default credentials, open cloud
   buckets, debug endpoints in prod, missing security headers, over-permissive
   IaC/cloud settings.
3. **A03 Software Supply Chain Failures** — new/broadened (was "Vulnerable & Outdated
   Components"). Pin and scan dependencies, verify integrity, maintain an SBOM, use
   lockfiles, secure the CI/CD pipeline.
4. **A04 Cryptographic Failures** — weak or missing encryption. TLS everywhere; strong,
   salted password hashing; don't roll your own crypto.
5. **A05 Injection** — SQL / NoSQL / command / XSS. Parameterize, validate, encode.
6. **A06 Insecure Design** — threat-model early; security as a design property, not a
   patch.
7. **A07 Authentication Failures** — weak credential and session handling (see below).
8. **A08 Software or Data Integrity Failures** — unverified updates, insecure
   deserialization, unsigned CI/CD artifacts.
9. **A09 Security Logging and Alerting Failures** — you can't respond to what you can't
   see; log security events and alert.
10. **A10 Mishandling of Exceptional Conditions** — **new**: errors handled badly —
    leaking stack traces/secrets, or failing *open* instead of *closed*.

Authoritative source: `owasp.org/Top10/2025`.

## Authentication vs authorization

- **AuthN** = who you are; **AuthZ** = what you're allowed to do. Broken authorization
  is the #1 risk, so treat it as first-class.
- **Sessions vs tokens:**
  - **Server sessions** (a cookie holds an opaque session id; state lives server-side):
    easy to **revoke** (delete it), simple, but stateful.
  - **JWT** (self-contained, signed): stateless and scalable, but **revocation is
    hard** — a valid token works until it expires. Mitigate with **short-lived access
    tokens + refresh tokens** (and a refresh-token denylist).
  - **Token storage:** prefer an **`httpOnly`, `Secure`, `SameSite` cookie** (JS can't
    read it → not stealable via XSS) over `localStorage` (readable by any script → XSS
    can exfiltrate it).
- **OAuth2 / OIDC:** delegated authorization; use the **Authorization Code flow with
  PKCE** for web and mobile. OIDC layers identity (an `id_token`) on top. Don't
  hand-roll federated auth.
- **Passwords:** hash with **bcrypt / argon2** (salted, deliberately slow); never
  encrypt or store plaintext. Add **MFA**.
- **Access model:** RBAC (roles) vs ABAC (attributes/policies) — pick per needs.

## Injection

- **SQL injection:** use **parameterized queries / an ORM**; never string-concatenate
  user input into SQL. Run the app's DB user with **least privilege**. (In FinTech,
  parameterize everything and encrypt PII columns.)
- Also **NoSQL injection**, **command injection**, and **LDAP injection** — same root
  cause (untrusted input reaching an interpreter), same fix (validate + parameterize).

## XSS (cross-site scripting)

- **Types:** stored (persisted then served), reflected (echoed from the request),
  DOM-based (client-side sink).
- **Defense:** contextual **output encoding**; rely on framework auto-escaping (React
  escapes by default — `dangerouslySetInnerHTML` is the deliberate escape hatch);
  **sanitize** any HTML you must render (DOMPurify); and add a **Content-Security-Policy**
  as defense-in-depth so injected scripts won't execute.

## CSRF (cross-site request forgery)

An attacker's page makes the victim's browser send a state-changing request that rides
along the victim's cookies. **Defenses:** **`SameSite=Lax`/`Strict` cookies** (the
primary modern defense), anti-CSRF tokens, and checking `Origin`/`Referer`. Note:
APIs authenticated by a **token in a header** (not an ambient cookie) aren't
CSRF-vulnerable.

## CORS (commonly misunderstood)

CORS is a **browser relaxation of the same-origin policy** — it grants a cross-origin
site permission to *read* your responses. It is **not** a server-side access control.
`Access-Control-Allow-Origin: *` protects nothing on its own; your real authorization
still has to be enforced server-side. Never reflect an arbitrary `Origin` back *with*
`Allow-Credentials: true`.

## Secrets & transport

- Keep secrets in **environment variables / a secret manager** (Vault, cloud KMS) —
  never in code or git. (This repo learned that the hard way — a credential in a
  committed `.env` is exactly the failure mode; rotate immediately on exposure.)
- **TLS/HTTPS everywhere**, HSTS to force it, modern cipher suites.

## Security headers

`Content-Security-Policy` (mitigate XSS), `Strict-Transport-Security` (HSTS),
`X-Content-Type-Options: nosniff`, `X-Frame-Options` / `frame-ancestors` (clickjacking),
and a sensible `Referrer-Policy`.

## Other must-knows

- **Rate limiting / brute-force protection** on auth and expensive endpoints (see
  [`../system-design/high-level/rate-limiter.md`](../system-design/high-level/rate-limiter.md)).
- **IDOR / broken object-level authorization** — verify ownership on *every* object
  access, don't trust an id in the URL.
- **SSRF** (now under A01) — validate/allowlist any server-side outbound URL so an
  attacker can't pivot to internal services or cloud metadata endpoints.
- **PII handling** — encrypt at rest and in transit, minimize what you store, and keep
  **audit trails** (table stakes in regulated domains).

## Secure-design principles

Least privilege, **defense in depth**, **fail secure** (deny on error, never fail
open), **validate on the server** (client-side validation is UX, not security), don't
roll your own crypto, and minimize the attack surface.

## Trade-offs / what interviewers probe

- **Sessions vs JWT** — instant revocation vs stateless scalability (short TTL +
  refresh tokens is the usual compromise).
- **Cookie vs `localStorage`** token storage — XSS exposure vs CSRF surface (cookie +
  `SameSite` + CSRF token is generally safest).
- **Security vs UX** — MFA friction, session length, step-up auth for sensitive
  actions.
- **Where to enforce authorization** — always server-side, on every request; the client
  is never trusted.

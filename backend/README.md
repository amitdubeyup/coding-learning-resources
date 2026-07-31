# Backend

Server-side engineering: runtimes, APIs, and the concerns that show up once code
faces real traffic.

## Modules
- **[`nodejs/`](nodejs/)** — the rebuilt Node.js module:
  - [`nodejs/README.md`](nodejs/README.md) — runtime model + the event loop
  - [`nodejs/async-streams-events.md`](nodejs/async-streams-events.md)
  - [`nodejs/apis-and-express.md`](nodejs/apis-and-express.md)
  - [`nodejs/production.md`](nodejs/production.md) — scaling, security, error handling, testing
  - `nodejs/nodejs-legacy/` — original 400-question set (reference)
- **[`python-web/`](python-web/)** — Python web frameworks: [`python-web/fastapi.md`](python-web/fastapi.md) (Pydantic v2) and [`python-web/django.md`](python-web/django.md).
- **[`web-security.md`](web-security.md)** — web & application security: OWASP Top 10:2025, auth (sessions / JWT / OAuth2-OIDC), injection, XSS / CSRF / CORS, secrets, security headers.

Runnable reference apps live in [`../projects/`](../projects/).

## The backend interview arc
Most backend questions ladder up the same way: the **language runtime** (how async
works — `nodejs/README.md` or `../languages/python.md`) → **API design**
(`nodejs/apis-and-express.md`) → the **data layer** ([`../data/`](../data/)) →
**scale & reliability** (`nodejs/production.md`, [`../system-design/`](../system-design/),
[`../devops/`](../devops/)) → and **securing it** ([`web-security.md`](web-security.md)).
Being able to walk that ladder is what "senior backend"
means in an interview.

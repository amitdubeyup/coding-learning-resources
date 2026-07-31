# Backend

Server-side engineering: runtimes, APIs, and the concerns that show up once code
faces real traffic.

## Modules
- **[`nodejs/`](nodejs/)** — the rebuilt Node.js module:
  - [`nodejs/README.md`](nodejs/README.md) — runtime model + the event loop
  - [`nodejs/async-streams-events.md`](nodejs/async-streams-events.md)
  - [`nodejs/apis-and-express.md`](nodejs/apis-and-express.md)
  - [`nodejs/production.md`](nodejs/production.md) — scaling, security, error handling, testing
  - `nodejs/nodejs-legacy/` — original 400-question set (reference, pending review)

*Pending relocation:* Python web frameworks (FastAPI/Django notes) will land here as
`python-web/`, and the runnable reference apps will move to top-level
[`../projects/`](../projects/).

## The backend interview arc
Most backend questions ladder up the same way: the **language runtime** (how async
works — `nodejs/README.md` or `../languages/python.md`) → **API design**
(`nodejs/apis-and-express.md`) → the **data layer** ([`../data/`](../data/)) →
**scale & reliability** (`nodejs/production.md`, [`../system-design/`](../system-design/),
[`../devops/`](../devops/)). Being able to walk that ladder is what "senior backend"
means in an interview.

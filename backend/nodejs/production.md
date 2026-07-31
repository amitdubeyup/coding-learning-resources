# Node.js in production

Scaling, performance, security, error handling, and testing — the "how does this
survive real traffic?" topics that senior Node interviews focus on.

## Using all your CPU cores

Node runs your JS on one thread, so a single process uses one core. To use all cores:
- **Cluster module / multiple processes** behind a load balancer — fork one worker
  per core; each handles requests independently. A process manager (PM2) or the
  platform (Kubernetes) typically runs multiple instances.
- **Worker threads** for CPU-bound tasks *within* a process (image processing, heavy
  computation) so they don't block the event loop.

Rule of thumb: horizontal scaling (more stateless instances) for throughput; worker
threads for in-process CPU work. Keep the app **stateless** so any instance can serve
any request (session/state in Redis or a DB).

## Performance

- **Don't block the event loop** — the golden rule. Move CPU work off the main thread.
- **Cache** hot reads (in-memory for a single instance, Redis for shared).
- **Stream** large payloads instead of buffering (see `async-streams-events.md`).
- **Connection pooling** for databases; reuse connections, don't open per request.
- **Profile** with `--prof`, clinic.js, or flame graphs before optimizing; measure the
  hot path.
- Set **timeouts** on outbound calls so a slow dependency doesn't pile up requests.

## Error handling strategy

- **Operational errors** (bad input, network failure, 404) — expected; handle and
  respond gracefully.
- **Programmer errors** (bugs, undefined access) — let them crash; a process manager
  restarts a clean process. Don't try to `catch` your way out of a corrupted state.
- Use `try/catch` around `await`, forward Express errors via `next(err)`, and add
  process-level `uncaughtException` / `unhandledRejection` handlers **for logging and
  graceful shutdown**, not to keep running in an unknown state.
- **Graceful shutdown:** on SIGTERM, stop accepting new connections, finish in-flight
  requests, close DB pools, then exit — critical for zero-downtime deploys in K8s.

## Security essentials (OWASP-aware)

- **Validate & sanitize all input** (see `apis-and-express.md`) — prevents injection.
- **Parameterized queries / ORM** — never build SQL by string concatenation.
- **Hash passwords** with bcrypt/argon2; never store plaintext.
- **HTTPS everywhere**; set security headers (helmet); secure, httpOnly, sameSite
  cookies.
- **Rate limiting** to blunt brute-force and DoS.
- **Manage secrets via environment/secret store**, never in code (this repo's leaked
  DB credential is the cautionary example — see `../../SECURITY.md`).
- **Keep dependencies patched** (`npm audit`); the supply chain is a real attack
  surface.
- Don't leak stack traces / internal details in error responses.

## Testing

- **Unit** (Jest/Vitest/node:test) for pure logic; **integration** (supertest) for API
  routes; **e2e** for critical flows.
- Mock external services at the boundary; use a test database, not production.
- Test error paths and edge cases, not just the happy path — interviewers probe this.

## Common questions

- **Use all CPU cores in Node?** Cluster/multiple processes + load balancing; worker
  threads for CPU tasks.
- **Make a Node app scalable?** Stateless instances, horizontal scaling, caching,
  connection pooling, don't block the loop.
- **uncaughtException — keep running?** No — log, shut down gracefully, let the manager
  restart a clean process.
- **Graceful shutdown — why?** Finish in-flight work and close resources for
  zero-downtime deploys.
- **Top Node security practices?** Validate input, parameterized queries, hash
  passwords, HTTPS + headers, rate limit, secrets outside code, patch deps.

*Deep legacy Q&A: [`nodejs-legacy/`](nodejs-legacy/).*

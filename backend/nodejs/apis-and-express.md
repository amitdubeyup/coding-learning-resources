# APIs & Express

Building HTTP services is what most Node roles are actually about. Interviews test
middleware, REST design, auth, and validation.

## HTTP in Node & why frameworks

Node's built-in `http` module can serve requests, but you get no routing, body
parsing, or middleware. **Express** (and modern alternatives like Fastify) add these
ergonomically. Fastify is worth naming as the faster, schema-first alternative.

## The middleware model (Express's core concept)

Middleware are functions `(req, res, next)` that run in order for each request. Each
either responds or calls `next()` to pass control on.

```js
const express = require("express");
const app = express();

app.use(express.json());                 // parse JSON bodies
app.use((req, _res, next) => {           // logging middleware
  console.log(`${req.method} ${req.url}`);
  next();
});

app.get("/users/:id", async (req, res, next) => {
  try {
    const user = await getUser(req.params.id);
    if (!user) return res.status(404).json({ error: "Not found" });
    res.json(user);
  } catch (err) {
    next(err);                           // forward to the error handler
  }
});

// Error-handling middleware has FOUR args — Express identifies it by arity
app.use((err, _req, res, _next) => {
  res.status(err.status || 500).json({ error: "Internal error" });
});
```

The interview must-knows: middleware runs in registration order; `next()` passes
control (and `next(err)` jumps to error handlers); an error handler is the one with
**four** parameters.

## REST API design

- **Resources as nouns**, HTTP verbs for actions: `GET /users`, `POST /users`,
  `GET /users/:id`, `PUT/PATCH /users/:id`, `DELETE /users/:id`.
- **Status codes:** 200 OK, 201 Created, 204 No Content, 400 Bad Request, 401
  Unauthorized, 403 Forbidden, 404 Not Found, 409 Conflict, 422 Unprocessable, 500
  Server Error. Using the right code is a seniority signal.
- **Idempotency:** GET/PUT/DELETE are idempotent; POST is not. Matters for retries.
- **Versioning** (`/v1/…`), pagination, filtering, and consistent error shapes.
- **PUT vs PATCH:** full replace vs partial update.

## Authentication & authorization

- **Stateless (JWT):** signed token holds claims; server verifies the signature — no
  session store, scales horizontally. Trade-off: hard to revoke before expiry, so keep
  access tokens short-lived and use refresh tokens.
- **Stateful (sessions):** session id in a cookie, state in a store (Redis). Easy to
  revoke; needs shared session storage across instances.
- **AuthN vs AuthZ:** who you are vs what you're allowed to do. Implement authZ as
  middleware that checks roles/permissions.
- Always hash passwords (bcrypt/argon2), use HTTPS, set secure/httpOnly cookies.

## Validation

Never trust client input. Validate and coerce request data at the boundary with a
schema (e.g. Zod/Joi) and reject with 400/422 on failure. This prevents a huge class
of bugs and injection issues.

## Common questions

- **What is middleware?** Ordered `(req,res,next)` functions that process a request;
  the backbone of Express.
- **How does Express know a function is an error handler?** It has four parameters.
- **JWT vs sessions?** Stateless/scalable/hard-to-revoke vs stateful/revocable/needs
  a store.
- **Which status code for X?** Match the semantic (201 create, 404 missing, 401 vs
  403, 409 conflict).
- **Handle async errors in Express?** `try/catch` + `next(err)` (or an async wrapper);
  unhandled async errors won't reach the error middleware on their own in older Express.
- **PUT vs PATCH?** Full replace vs partial update.

*Deep legacy Q&A: [`nodejs-legacy/`](nodejs-legacy/).*

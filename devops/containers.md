# Containers: Docker & Kubernetes

Containerization is the backbone of modern deployment. Interviews test whether you
understand *why* containers exist, how images work, and how orchestration keeps them
running at scale.

---

# Docker

## What a container actually is

A container is an isolated process on the host, using Linux **namespaces** (isolation
of PID, network, mounts) and **cgroups** (resource limits). It is **not** a VM — there's
no guest OS; containers share the host kernel, which is why they're lightweight and
start in milliseconds.

- **Image** = an immutable, layered template (your app + deps + runtime).
- **Container** = a running instance of an image.
- **Registry** = where images are stored/shared (Docker Hub, ECR, GHCR).

## Images & layers

Each Dockerfile instruction creates a **layer**; layers are cached and shared between
images. Order matters for cache efficiency:

```dockerfile
# Copy dependency manifests first so `npm ci` is cached until they change
COPY package*.json ./
RUN npm ci
# App code changes often — copy it last
COPY . .
```

If you copy source before installing deps, every code change busts the dependency
cache and reinstalls everything. This ordering question is common.

## Multi-stage builds (the key best practice)

Build in a heavy image, ship only the artifact in a tiny runtime image:

```dockerfile
FROM node:20 AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-slim AS runtime
WORKDIR /app
COPY --from=build /app/dist ./dist
COPY --from=build /app/node_modules ./node_modules
USER node                      # don't run as root
CMD ["node", "dist/server.js"]
```

Benefits: smaller images, no build tools in production, smaller attack surface.

## Best practices interviewers listen for

- Use a **specific base tag** (`node:20-slim`), not `latest`.
- **Minimal base images** (slim/alpine/distroless) for size and security.
- **Don't run as root**; use `USER`.
- **`.dockerignore`** to keep secrets/junk out of the build context.
- **One process per container**; make containers **stateless** — state goes to
  volumes or external services.
- **`CMD` vs `ENTRYPOINT`:** ENTRYPOINT sets the executable, CMD sets default args.

## Compose

`docker-compose.yml` defines multi-container local stacks (app + db + cache) with one
`docker compose up`. Great for dev; production uses an orchestrator.

---

# Kubernetes

## Why orchestration exists

Running one container is easy. Running hundreds across many machines — with
self-healing, rolling updates, scaling, and service discovery — is what Kubernetes
automates. The core idea is **declarative desired state**: you declare what you want;
the control loop continuously reconciles reality toward it.

## The objects you must know

- **Pod** — the smallest unit; one (or a few tightly-coupled) containers sharing
  network/storage. Pods are ephemeral and disposable.
- **Deployment** — manages a **ReplicaSet** of identical pods; handles rolling updates
  and rollbacks. What you deploy stateless apps with.
- **Service** — a stable virtual IP/DNS name that load-balances across a changing set
  of pods (since pod IPs churn). Types: ClusterIP, NodePort, LoadBalancer.
- **Ingress** — HTTP(S) routing/TLS into the cluster (host/path rules).
- **ConfigMap / Secret** — inject config and sensitive values (Secrets are base64, not
  encrypted at rest by default — enable encryption).
- **StatefulSet** — for stateful apps needing stable identity/storage (databases).
- **Namespace** — logical partitioning of a cluster.

## Self-healing & health

- **Liveness probe** — restart the container if it's stuck.
- **Readiness probe** — remove the pod from the Service until it's ready to serve.
  Getting these two confused (and taking traffic before ready) is a classic bug.
- The scheduler reschedules pods off failed nodes automatically.

## Scaling

- **HPA (Horizontal Pod Autoscaler)** scales replica count on CPU/memory/custom
  metrics.
- Set **resource requests/limits** so the scheduler can place pods and the HPA has
  signal.

## Common questions

- **Container vs VM?** Shared kernel + process isolation vs full guest OS — containers
  are lighter and faster but less isolated.
- **Why is image ordering important?** Layer caching — put rarely-changing steps first.
- **Reduce image size?** Multi-stage builds + slim/distroless base + fewer layers.
- **Pod vs Deployment?** A Pod is one running unit; a Deployment declaratively manages
  many identical Pods with rollouts.
- **Liveness vs readiness?** Restart-if-broken vs ready-to-receive-traffic.
- **How does a Service find pods?** Label selectors + kube-proxy load-balancing; the
  Service IP is stable while pod IPs change.

*Deep legacy Q&A: [`docker-legacy-qa.md`](docker-legacy-qa.md) ·
[`kubernetes-legacy-qa.md`](kubernetes-legacy-qa.md).*

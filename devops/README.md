# DevOps & Cloud

How software ships and stays healthy in production: containers, orchestration, cloud,
CI/CD, and the reliability practices that tie them together.

## Guides
- [`containers.md`](containers.md) — Docker (images, layers, multi-stage) & Kubernetes
  (pods, deployments, services, scaling, probes).
- [`aws.md`](aws.md) — the service map, compute choices, S3, IAM, VPC, HA, Well-Architected.
- [`ci-cd.md`](ci-cd.md) — pipelines, GitHub Actions, deployment strategies, IaC, Git workflows.

Deep legacy Q&A preserved as `*-legacy-qa.md` alongside each.

## Cross-cutting concepts (asked everywhere)

**The 12-factor app** — the checklist for cloud-native services: config in the
environment (not code), stateless processes, treat backing services as attached
resources, build/release/run separation, disposability, logs as event streams. Half
of "how would you make this production-ready?" is just reciting and applying these.

**Observability — the three pillars:**
- **Metrics** — numeric time series (latency, error rate, throughput, saturation);
  the "four golden signals" of SRE.
- **Logs** — structured, centralized event records.
- **Traces** — follow one request across services to find where latency/errors live.
Answer "how do you debug a slow distributed system?" with: dashboards → traces to
localize → logs for detail.

**Reliability (SRE):** define **SLIs** (what you measure), **SLOs** (targets), and
**error budgets** (allowed failure) — they turn "is it reliable enough?" into a number
that governs how fast you ship. Add health checks, autoscaling, graceful degradation,
retries with backoff, and circuit breakers.

**Deployment safety:** IaC for reproducibility, canary/blue-green for safe rollout,
automated rollback on SLO breach, and secret management (never in the repo — see
[`../SECURITY.md`](../SECURITY.md)).

## How to use
For a cloud/DevOps design question, structure the answer as: containerize
(`containers.md`) → run it (K8s or a cloud compute choice in `aws.md`) → ship it
(`ci-cd.md`) → observe & keep it reliable (this page). Walking that arc signals real
production experience.

## Cross-references
- System design at scale: [`../system-design/`](../system-design/).
- Data-layer scaling & caching: [`../data/`](../data/).

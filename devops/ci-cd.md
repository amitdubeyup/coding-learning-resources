# CI/CD & Git

How code goes from commit to production, safely and repeatably. Interviews test your
pipeline design, deployment strategies, and Git workflow judgment.

## CI vs CD

- **Continuous Integration** — every push is automatically built and tested, so
  integration problems surface early. Keep the main branch always green.
- **Continuous Delivery** — every green build is *release-ready*; deploying is a
  button press.
- **Continuous Deployment** — every green build is deployed to production
  automatically (no manual gate).

## Anatomy of a pipeline

```
commit → lint → unit tests → build artifact → integration tests
       → security scan → deploy to staging → smoke tests → deploy to prod
```

Principles: **fail fast** (cheap checks first), build the artifact **once** and
promote the same one through environments (never rebuild per environment), and keep
pipelines **reproducible** (pinned tool/dependency versions).

## GitHub Actions (concrete example)

```yaml
name: CI
on:
  push: { branches: [main] }
  pull_request: { branches: [main] }
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: "20" }
      - run: npm ci
      - run: npm test
```

Know the vocabulary: **workflow → jobs → steps**; jobs run in parallel by default,
steps run in order; **secrets** are injected via the encrypted secrets store (never
hard-coded). This repo's own `.github/workflows/ci.yml` adds a **gitleaks** secret
scan — a scan you should include in any real pipeline.

## Deployment strategies (a favorite topic)

| Strategy | How | Trade-off |
|---|---|---|
| **Rolling** | replace instances gradually | simple; mixed versions briefly |
| **Blue-green** | run old (blue) + new (green), flip traffic | instant rollback; needs 2x capacity |
| **Canary** | send a small % to the new version, watch metrics, ramp | safest; needs good monitoring/automation |
| **Recreate** | stop old, start new | downtime; only for non-critical |

Senior answer: pick based on rollback needs, cost, and monitoring maturity — canary if
you have solid metrics, blue-green when you need instant rollback and can afford the
capacity.

## Infrastructure as Code (IaC)

Define infrastructure declaratively (Terraform, CloudFormation, Pulumi) and version
it in git. Benefits: reproducible environments, peer-reviewable changes, and no
click-ops drift. Terraform's `plan`/`apply` (preview then execute) mirrors the
"see the diff before you change prod" discipline.

## Git workflow judgment

- **Trunk-based** (short-lived branches merged to main frequently, behind feature
  flags) suits CI/CD and is increasingly the default.
- **Git flow** (long-lived develop/release branches) suits scheduled releases but adds
  merge overhead.
- **`merge` vs `rebase`:** merge preserves history (safe on shared branches); rebase
  gives a linear history (use only on your own un-pushed branches). Never rebase
  shared/public history.
- **Resolve a conflict:** understand both changes, edit to the intended result, test,
  then commit — don't blindly accept "theirs/mine."

## Common questions

- **CI vs CD?** Auto build+test on every change vs auto-releasable/auto-deployed.
- **Blue-green vs canary?** Instant full flip w/ rollback vs gradual %-based rollout
  with monitoring.
- **Why build the artifact once?** Guarantees prod runs exactly what you tested;
  rebuilding risks environment drift.
- **Store secrets in a pipeline?** Encrypted secret store / vault + least-privilege,
  never in the repo — and scan for leaks in CI.
- **merge vs rebase?** History-preserving vs linear; never rebase shared branches.

*Deep legacy Q&A: [`cicd-legacy-qa.md`](cicd-legacy-qa.md).*

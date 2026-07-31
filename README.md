# 🎯 Engineering Interview Prep

A structured, verified knowledge base for cracking senior-level software & AI
engineering interviews at top-tier companies worldwide — DSA, system design,
languages, backend/frontend, data, DevOps, AI/ML, and behavioral rounds.

> **Quality bar:** accurate, current, runnable, honest. Every file must meet the
> standard in [`CONTRIBUTING.md`](CONTRIBUTING.md).

## How to use this repo

1. **Start with the three universal gates:** [`dsa/`](dsa/),
   [`system-design/`](system-design/), and [`behavioral/`](behavioral/) — they decide
   most senior offers regardless of role.
2. **Learn patterns, not problems.** `dsa/` teaches the ~15 patterns behind the
   hundreds of LeetCode variants.
3. **Then go deep on your stack** via the language/framework folders below.
4. **Practice out loud** — senior interviews score how you reason about trade-offs.

## Layout

| Area | Folder | Focus |
|------|--------|-------|
| Algorithms | [`dsa/`](dsa/) | 15 patterns, complexity, curated problem sets |
| System design | [`system-design/`](system-design/) | high-level, low-level (OS), multi-tenancy |
| Languages | [`languages/`](languages/) | Python, JavaScript, TypeScript |
| Backend | [`backend/`](backend/) | Node.js, Python web (FastAPI/Django) |
| Frontend | [`frontend/`](frontend/) | React, Angular, Vue, HTML/CSS, GraphQL |
| Data | [`data/`](data/) | SQL, indexing, NoSQL, CAP, caching |
| DevOps | [`devops/`](devops/) | containers, AWS, CI/CD, observability |
| AI/ML | [`ai-ml/`](ai-ml/) | LLMs, RAG, agents, evaluation, MLOps |
| Behavioral | [`behavioral/`](behavioral/) | STAR method, competency map, story bank |
| Projects | [`projects/`](projects/) | runnable reference apps (Django, FastAPI) |

Each folder has a `README.md` index. Files ending in `-legacy-qa.md` are the original
long-form Q&A, kept for reference and pending a final line-by-line review.

## 🔴 Security notice — action required

Live credentials were previously committed to this repo. The code is fixed (secrets
now come from the environment), but the secrets remain in **git history**. Complete
[`SECURITY.md`](SECURITY.md) — rotate the DB password and Django `SECRET_KEY`, and
purge history — **before pushing anywhere.**

## 🧹 Final housekeeping (run once)

Empty folders remain from the reorg (I couldn't delete them directly). Sweep macOS
files and remove the empties:

```bash
find . -name .DS_Store -delete
rmdir ai angular database fastapi javascript multi-tenant-architecture \
      program reactjs vuejs django full-stack python
```

There's also a quarantine folder at `~/Learning/_learning-code-quarantine/`
(old databases, build artifacts, `helper.txt`, and two personal scripts that were
not yours) — inspect and `rm -rf` when satisfied.

## Status

Restructured and rewritten to the quality bar: **DSA, AI-ML, behavioral, frontend
(React/Angular/Vue), languages (Python/JS/TS), data, DevOps, Node.js**, plus all
security/code/CI hardening. Remaining polish: a version pass over the
`*-legacy-qa.md` deep-dives and the Pydantic-v1 bits in the FastAPI notes.

## License

MIT — see [`LICENSE`](LICENSE).

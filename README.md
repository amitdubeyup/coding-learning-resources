# 🎯 Engineering Interview Prep

A structured, verified knowledge base for cracking senior-level software & AI
engineering interviews at top-tier companies worldwide — DSA, system design,
languages, backend/frontend, data, DevOps, AI/ML, and behavioral rounds.

> **Quality bar:** accurate, current, runnable, honest — every file earns its place.

## How to use this repo

Two ways in: **targeted** — jump straight to your weak area via the folder `README.md`
indexes below; or **systematic** — follow the **Study plan** section below in order.
Either way, two rules decide senior outcomes: **learn patterns, not problems** (`dsa/`
teaches the ~15 patterns behind hundreds of LeetCode variants), and **practice out
loud** — you're scored on how you reason about trade-offs, not just the final answer.

## Layout

| Area | Folder | Focus |
|------|--------|-------|
| Algorithms | [`dsa/`](dsa/) | 15 patterns, complexity, sorting & trees/graphs, curated problem sets |
| System design | [`system-design/`](system-design/) | HLD fundamentals + 10 worked designs, LLD/OOD round, OS internals, multi-tenancy |
| Languages | [`languages/`](languages/) | Python, JavaScript, TypeScript |
| Backend | [`backend/`](backend/) | Node.js, Python web (FastAPI/Django), web security |
| Frontend | [`frontend/`](frontend/) | React (19 + compiler), Angular, Vue, HTML/CSS, GraphQL, frontend system design |
| Data | [`data/`](data/) | SQL, indexing, NoSQL, CAP, caching |
| DevOps | [`devops/`](devops/) | containers, AWS, CI/CD, observability |
| AI/ML | [`ai-ml/`](ai-ml/) | LLM foundations, RAG, agents, GenAI system design, evaluation, classical ML |
| Behavioral | [`behavioral/`](behavioral/) | STAR method, competency map, story bank |
| Projects | [`projects/`](projects/) | runnable reference apps (Django, FastAPI) |

Each folder has a `README.md` index. Files ending in `-legacy-qa.md` are the original
long-form Q&A, kept as supplementary reference beside the rewritten guides.

## Study plan — read in this order

Concepts build in layers, so this order means each topic rests on the one before it. A
focused full pass is roughly **6–8 weeks part-time** — but the *ordering* matters more
than the calendar. Compress or expand each phase to your timeline.

**Phase 0 · Orient (½ hour).** Read this page, then skim every folder's `README.md` to
build a mental map. Don't read the content yet — just learn what lives where.

**Phase 1 · The universal gates (weeks 1–3).** These decide most senior offers, whatever
the role:
- **DSA** — [`dsa/`](dsa/) README (patterns + complexity) →
  [`sorting.md`](dsa/sorting.md) → [`trees-and-graphs.md`](dsa/trees-and-graphs.md).
  Then *drill the patterns on a judge* (LeetCode/NeetCode) daily — this repo builds
  recognition; reps build the skill.
- **System design** — [`system-design/`](system-design/) README →
  [`fundamentals.md`](system-design/fundamentals.md) (building blocks, estimation, the
  framework) → [`low-level-design.md`](system-design/low-level-design.md) (the OOD
  round) → then one design from [`high-level/`](system-design/high-level/) per sitting.
  **Re-derive each design yourself before reading the solution.**
- **Behavioral** — [`behavioral/`](behavioral/) README, and **start your story bank
  now** — it compounds and can't be crammed the night before.

**Phase 2 · Your stack depth (weeks 3–5).** Pick what the role uses:
- **Language** — your primary in [`languages/`](languages/) (Python / JS / TS).
- **Backend / Frontend** — the module for your stack: [`backend/`](backend/) →
  [`web-security.md`](backend/web-security.md), and/or [`frontend/`](frontend/) →
  [`system-design.md`](frontend/system-design.md).
- **Data** — [`data/`](data/) (SQL → indexing → NoSQL/CAP); it underpins both backend
  and system design.

**Phase 3 · AI/ML specialization (weeks 5–6).** For AI-focused roles:
[`ai-ml/`](ai-ml/) README → [`foundations.md`](ai-ml/foundations.md) (the depth anchor)
→ [`rag.md`](ai-ml/rag.md) → [`agents.md`](ai-ml/agents.md) →
[`genai-system-design.md`](ai-ml/genai-system-design.md) (apply it) →
[`evaluation-and-safety.md`](ai-ml/evaluation-and-safety.md) →
[`classical-ml.md`](ai-ml/classical-ml.md) if the role touches DS/ML.

**Phase 4 · Integrate & rehearse (ongoing).** Use [`devops/`](devops/) as supporting
context, then spend the back half on **timed mock interviews, out loud** (coding +
design + behavioral) — the highest-leverage activity, and the one the repo can't do for
you. Before each design mock, re-read the **"Trade-offs to voice"** at the end of each
design file — that's your senior signal.

### Make it stick (how to read, not just what)
- **Re-derive, don't reread** — solve or design it yourself first, then compare to the
  guide.
- **Active recall** — after a section, close it and explain the idea out loud or on a
  whiteboard.
- **Run the code** — type out and execute the runnable snippets (DSA, the ML-coding
  round, [`projects/`](projects/)); reading code is not knowing it.
- **Spaced repetition** — revisit patterns and frameworks on a 1-day / 1-week / 1-month
  cadence.
- **Teach it** — if you can explain a topic simply to someone else, you own it.
- **Track your fumbles** — keep a running list of what you got wrong and target it next.

## Status

**Rewritten to the quality bar (deep, current, senior-focused):**
- **DSA** — 15-pattern guide, plus `sorting` and `trees-and-graphs` with a senior
  "what's actually tested" lens.
- **System design** — HLD fundamentals primer, the LLD/OOD round, an OS-internals
  index, and **all 10 high-level worked designs** rewritten to reasoning-driven depth.
- **AI/ML** — LLM foundations (transformers, RoPE, scaling, LoRA/QLoRA, reasoning
  models) plus RAG, agents, GenAI system-design worked examples, and evaluation.
- **Frontend** — React on the React 19 + compiler baseline; Angular, Vue, HTML/CSS.
- **Languages** — Python, JavaScript, TypeScript.
- **Also:** data, DevOps, Node.js, behavioral, and all security/code/CI hardening.
- **Senior add-ons:** frontend system design, classical ML + the ML-coding round, and
  web & application security (OWASP Top 10:2025).

**Remaining (supplementary, lower priority):** the `*-legacy-qa.md` deep-dives (kept
as reference) and the `os-internals/` OS topic files (index reframed; topics not
individually rewritten).

## License

MIT — see [`LICENSE`](LICENSE).

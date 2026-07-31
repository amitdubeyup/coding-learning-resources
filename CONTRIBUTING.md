# Contributing & content standards

This repo aims to be good enough that a diligent reader can prepare for and pass
senior-level interviews at top-tier companies worldwide. Every file must earn
its place against that bar.

## The quality bar (non-negotiable)

1. **Accurate.** Every technical claim must be correct and current. If you can't
   verify it, don't publish it. AI-drafted content must be reviewed by a human
   before it lands.
2. **Runnable.** Every code snippet should actually run on the stated version.
   Prefer complete, minimal examples over pseudo-code.
3. **Complexity-aware.** Algorithm answers state time/space complexity and why.
4. **Honest, not inflated.** No "200 questions" that are really 200 titles. If a
   problem isn't solved and explained, it's a link, not a claim.
5. **No secrets, no PII.** Never commit credentials or a real person's identity,
   employer, or project details. Behavioral answers are neutral templates.
6. **Trade-offs first.** Senior interviews reward "it depends, here's the
   trade-off," so lead with those, not memorized definitions.

## File & folder conventions

- One topic per file. If a file passes ~1,500 lines / ~60 KB, split it by topic.
- `kebab-case.md` filenames. No `SCREAMING.md`, no numeric splits (`1-50.md`).
- Every topic folder has a `README.md` that is an index + study path.
- Fenced code blocks always specify a language.

## Repository layout (target)

```
languages/    python, javascript, typescript
frontend/     react, angular, vue, html-css, graphql
backend/      nodejs, python-web (fastapi/django)
data/         sql, postgresql, mongodb, redis
system-design/ high-level, low-level
dsa/          patterns, problems, sorting, trees-graphs
devops/       aws, kubernetes, docker, github-actions
ai-ml/        llms, rag, agents, mlops, evaluation
behavioral/   neutral STAR templates
projects/     runnable code, separated from notes
```

## AI prompt templates

These generate first drafts only. Output is **not** publishable until a human
verifies it against the quality bar above.

### Generate new content
> As a technical interview coach, generate interview Q&A for **[TOPIC]** for
> senior/staff roles. 40–80 questions tagged `[Basic] / [Intermediate] /
> [Advanced] / [Scenario]`, grouped by theme. Each answer: concise explanation →
> runnable example on the current stable version → trade-offs / pitfalls → "what
> the interviewer is really testing." State complexity for anything algorithmic.
> Flag any claim you are not confident is current so a human can verify it.

### Update existing content
> Review and modernize the **[TOPIC]** document below. Preserve non-duplicate
> questions. Update code to current stable versions, replace deprecated APIs,
> merge duplicates, fix structure, and add commonly-asked missing questions.
> Return the complete updated document plus a change summary. Mark every version
> claim you could not verify.

### Validate without changing
> Assess the **[TOPIC]** document below for accuracy, currency, completeness,
> and duplication. Score each 1–10, list issues with line references, and rank
> fixes High/Medium/Low. Do not rewrite — assess only.

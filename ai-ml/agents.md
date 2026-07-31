# LLM Agents

An **agent** is an LLM that decides *actions* in a loop: it can call tools,
observe results, and iterate toward a goal — instead of answering in one shot.

## The core loop

```
Goal → LLM reasons → picks a tool + args → tool runs → observation
        ▲                                                    │
        └───────────────── repeat until done ────────────────┘
```

The simplest robust pattern is **ReAct** (Reason + Act): the model alternates a
short "thought" with an action, sees the observation, and continues.

```python
def run_agent(goal, tools, llm, max_steps=8):
    history = []
    for _ in range(max_steps):
        decision = llm.decide(goal, tools, history)   # -> {tool, args} | {final}
        if "final" in decision:
            return decision["final"]
        result = tools[decision["tool"]](**decision["args"])
        history.append((decision, result))
    return "Stopped: step limit reached."             # ALWAYS bound the loop
```

Two lines that keep it safe in interviews and prod: a **step cap** and an explicit
**termination path**. Unbounded agent loops are the #1 way agents burn money.

## Tool use / function calling

Tools are how agents affect the world (search, DB query, code exec, API calls).
- Define each tool with a **clear name, description, and typed schema** — the
  model chooses tools based on those descriptions, so write them well.
- **Validate arguments** before executing; never `eval` model output.
- Return **structured, unambiguous** observations; fold errors back as
  observations so the agent can recover instead of crashing.
- Principle of least privilege: sandbox code execution, scope API keys, and
  gate destructive actions behind confirmation.

## Memory

- **Short-term:** the conversation/scratchpad in the context window. Bounded, so
  **summarize or trim** older turns as it fills.
- **Long-term:** persist facts/preferences in a store (often a vector DB) and
  retrieve them when relevant — RAG applied to memory.
- Interview trap: "just keep appending to context" fails — you hit token limits,
  cost, and "lost in the middle." Have a memory strategy.

## Planning patterns

- **ReAct:** interleave reasoning and acting. Great default.
- **Plan-and-execute:** make a full plan first, then execute steps — better for
  long multi-step tasks; re-plan when steps fail.
- **Reflection / self-critique:** the agent reviews its own output and retries —
  improves quality at the cost of more calls.

## Multi-agent — and when NOT to

Specialized agents (planner, researcher, coder, reviewer) coordinated by an
orchestrator can help with genuinely separable sub-tasks. But be ready to argue
the **cost**: more latency, more tokens, more failure surface, harder debugging.
A senior answer is "one well-instrumented agent with good tools usually beats a
multi-agent swarm — reach for multiple agents only when responsibilities are
truly distinct."

## Why agents fail in production (know these cold)

| Failure | Cause | Mitigation |
|---|---|---|
| Infinite / expensive loops | no termination or bad observations | step cap, clear tool outputs, budget guard |
| Wrong tool / bad args | vague tool schemas | precise descriptions + typed schemas + validation |
| Compounding errors | one bad step poisons the rest | checkpoints, self-check steps, re-planning |
| Prompt injection via tool output | untrusted content treated as instructions | isolate/label tool data, don't grant it authority |
| Non-determinism / hard to debug | free-form reasoning | trace every step; constrain with structured output |

## Evaluating agents

Score the **trajectory**, not just the final answer: did it pick the right tools,
in a sensible order, with valid args, and terminate correctly? Use task-completion
rate on a fixed benchmark, plus per-step tracing. Details in
[`evaluation-and-safety.md`](evaluation-and-safety.md).

## What interviewers are really testing

That you treat an agent as a **distributed system with a stochastic component** —
you think about bounds, validation, observability, cost, and blast radius — not
that you can name the trendiest framework.

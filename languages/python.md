# Python for interviews

Python interviews test whether you understand the language's *model* — how names,
objects, and the runtime actually work — not just syntax. This is the high-signal set.

## The data model

- **Everything is an object**, and variables are **names bound to objects**, not
  boxes holding values. `a = b` makes `a` point at the same object as `b`.
- **Mutable vs immutable:** `list`, `dict`, `set`, and most custom objects are
  mutable; `int`, `float`, `str`, `tuple`, `frozenset`, `bytes` are immutable.
  This drives the two classic gotchas below.
- **`is` vs `==`:** `is` compares identity (same object); `==` compares value. Use
  `is` only for `None`/singletons.

**Mutable default argument** — the #1 Python gotcha:
```python
def add(item, bucket=[]):      # BUG: the list is created ONCE, at def time
    bucket.append(item); return bucket
# Fix:
def add(item, bucket=None):
    bucket = [] if bucket is None else bucket
    ...
```

**Shared references** — `b = a` on a list means mutating `b` mutates `a`. Use
`a.copy()` / `copy.deepcopy()` when you need independence.

## Concurrency & the GIL (guaranteed question)

- The **GIL** (in CPython) lets only one thread execute Python bytecode at a time.
  So **threads don't give CPU parallelism** — but they *do* help I/O-bound work,
  because the GIL is released during blocking I/O.
- **CPU-bound → `multiprocessing`** (separate processes, real parallelism).
  **I/O-bound → threads or `asyncio`.**
- **`asyncio`** is single-threaded cooperative concurrency: `async def` coroutines
  `await` at suspension points so one thread juggles thousands of I/O waits. It does
  **not** speed up CPU work and a blocking call inside a coroutine stalls the whole
  loop.
- Worth knowing: recent CPython has an experimental **free-threaded (no-GIL) build**;
  mention it as the direction of travel, but the GIL model above is still the answer.

## Generators & iterators

- An **iterator** implements `__next__`; an **iterable** implements `__iter__`.
- **Generators** (`yield`) produce values lazily — constant memory over huge/infinite
  sequences, which is the whole point in interviews.
```python
def read_large(path):
    with open(path) as f:
        for line in f:        # streams; doesn't load the file into memory
            yield line.strip()
```
Generator *expressions* `(x*x for x in it)` are the lazy cousins of list comprehensions.

## Decorators & context managers

- A **decorator** wraps a function to add behavior (logging, caching, timing, auth).
  Use `functools.wraps` to preserve the wrapped function's metadata.
```python
from functools import wraps
def timed(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        # ...time it...
        return fn(*args, **kwargs)
    return inner
```
- **Context managers** (`with`) guarantee setup/teardown (files, locks, connections)
  even on exceptions — via `__enter__`/`__exit__` or `@contextlib.contextmanager`.

## Memory management

- CPython uses **reference counting** plus a **cyclic garbage collector** for
  reference cycles. An object is freed when its refcount hits zero.
- `__slots__` removes the per-instance `__dict__` to cut memory for many small objects.
- Be able to explain why holding references (e.g. in a cache/list) prevents collection.

## Typing (modern Python)

- Type hints are optional and not enforced at runtime; a checker (mypy/pyright)
  enforces them statically.
- Modern syntax: `list[int]`, `dict[str, int]`, `str | None` (not `Optional[str]`),
  `X | Y` unions. Use `TypedDict`, `Protocol` (structural typing), and `dataclass`
  for typed records.

## Pythonic performance

- Prefer built-ins and comprehensions (they run in C) over manual loops.
- `set`/`dict` membership is O(1); `list` membership is O(n) — a common speedup.
- Use `collections` (`defaultdict`, `Counter`, `deque`) and `functools.lru_cache`.
- Profile before optimizing (`cProfile`), same as any language.

## Common questions

- **`list` vs `tuple`?** Mutable vs immutable; tuples are hashable (usable as dict
  keys) and signal fixed structure.
- **Shallow vs deep copy?** Shallow copies the container but shares nested objects;
  deep copies everything recursively.
- **`*args` / `**kwargs`?** Capture arbitrary positional / keyword arguments.
- **How does `async` differ from threads?** Cooperative single-thread concurrency vs
  preemptive OS threads; async excels at high-concurrency I/O with less overhead.
- **When multiprocessing over threading?** CPU-bound work, to sidestep the GIL.

*Full legacy Q&A preserved in [`python-legacy-qa.md`](python-legacy-qa.md).*

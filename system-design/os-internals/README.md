# Operating Systems & CS fundamentals

> **Naming note:** this folder was previously called "low-level design," but its
> content is **operating-systems / computer-science fundamentals** — not the
> object-oriented **Low-Level Design (LLD)** round. The real LLD/OOD material lives in
> [`../low-level-design.md`](../low-level-design.md). These topics still come up
> (especially in systems-heavy roles and for reasoning about concurrency, memory, and
> I/O in any design), so they're worth knowing — just don't confuse the two.

## Topics
1. [OS fundamentals](os-fundamentals.md) — kernel/user space, system calls, architecture
2. [Process management](process-management.md) — PCB, scheduling, context switches
3. [Concurrency](concurrency.md) — threads, mutexes/semaphores, deadlock, lock-free
4. [Memory management](memory-management.md) — virtual memory, paging, page faults
5. [File systems](file-systems.md) — structure, journaling, allocation
6. [Networking](networking.md) — TCP/IP, the stack, flow/congestion control
7. [I/O systems](io-systems.md) — blocking vs non-blocking vs async, DMA, interrupts
8. [System calls](system-calls.md) — entry points, interrupt handling, overhead
9. [Device management](device-management.md) — drivers, char/block devices
10. [Security](security.md) — auth, cryptography, hardening

## The questions that actually recur

- **Process vs thread** — separate address space vs shared memory; what a context
  switch costs; when to use each.
- **Virtual memory** — page tables, page faults, TLB, page-replacement (LRU/clock),
  and why it gives isolation + more-than-physical RAM.
- **Concurrency** — race conditions, mutex vs semaphore, deadlock (the four Coffman
  conditions + prevention/avoidance/detection), and why lock-free is hard (memory
  ordering).
- **Deadlock** — mutual exclusion, hold-and-wait, no preemption, circular wait; break
  any one to prevent it.
- **TCP vs UDP** — reliable/ordered/connection-oriented vs fast/best-effort; when each
  wins. Know the handshake and flow/congestion control at a high level.
- **How a system call works** — user→kernel trap, mode switch, validation, return; why
  it's more expensive than a function call.
- **Blocking vs non-blocking vs async I/O** — the model behind Node's event loop and
  high-concurrency servers (cross-ref [`../../backend/nodejs/`](../../backend/nodejs/)).

## Why this still matters for design
Concurrency, memory, caching, and I/O reasoning underpin every high-level design —
knowing what a context switch, a page fault, or a blocking syscall *costs* is what lets
you justify an architecture. See [`../fundamentals.md`](../fundamentals.md).

## References
- *Operating System Concepts* (Silberschatz) · *Modern Operating Systems* (Tanenbaum)
- MIT OpenCourseWare 6.828 (Operating System Engineering)

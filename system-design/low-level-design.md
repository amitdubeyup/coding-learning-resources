# Low-Level Design (LLD / OOD)

The **object-oriented design** round: turn a fuzzy requirement ("design a parking lot,"
"design an elevator system," "design a ride-share matcher") into a clean set of
classes, relationships, and interfaces. It tests whether you can model a domain, apply
**SOLID** and the right **design patterns**, and reason about extensibility and
concurrency — distinct from the distributed-systems HLD round in
[`fundamentals.md`](fundamentals.md).

## Contents
- [The OOD interview process](#the-ood-interview-process)
- [OOP pillars (quick)](#oop-pillars-quick)
- [SOLID](#solid)
- [Design patterns that actually come up](#design-patterns-that-actually-come-up)
- [Worked example: parking lot](#worked-example-parking-lot)
- [Concurrency in LLD](#concurrency-in-lld)
- [Common questions & pitfalls](#common-questions--pitfalls)

---

## The OOD interview process

A repeatable method — narrate it as you go:
1. **Clarify requirements & scope.** Functional features + constraints. Agree what's
   in/out (e.g. "single lot, multiple floors, three vehicle sizes, hourly pricing").
2. **Identify the core entities.** The nouns become classes: `ParkingLot`, `Floor`,
   `Spot`, `Vehicle`, `Ticket`, `Payment`.
3. **Define relationships & cardinality.** Composition vs association vs inheritance;
   "a Floor *has* many Spots," "a Car *is a* Vehicle."
4. **Design interfaces & key methods.** What each class exposes; keep responsibilities
   focused.
5. **Apply patterns where they earn their place.** Strategy for pricing, Factory for
   creating spot/vehicle types, Singleton for the lot, Observer for display boards —
   *name the pattern and the reason*, don't pattern-stuff.
6. **Handle edge cases & extensibility.** "How would you add electric-charging spots
   or surge pricing?" — your design should absorb it without rewrites (Open/Closed).
7. **Concurrency, if relevant.** Two cars racing for the last spot → guard the
   allocation.

The signal interviewers want: clean responsibilities, an abstraction that flexes to
new requirements, and *justified* pattern use.

## OOP pillars (quick)

- **Encapsulation** — hide internal state behind methods; expose intent, not fields.
- **Abstraction** — program to interfaces/roles, not concrete classes.
- **Inheritance** — model true "is-a" relationships; **prefer composition over
  inheritance** when in doubt (more flexible, avoids fragile hierarchies).
- **Polymorphism** — one interface, many implementations chosen at runtime (the basis
  of Strategy, and of extensibility generally).

## SOLID

The five principles, each with the *why*:
- **S — Single Responsibility.** A class has one reason to change. Split "does too
  much" classes (e.g. separate `Payment` from `Ticket`).
- **O — Open/Closed.** Open for extension, closed for modification. Add a new pricing
  scheme by adding a class, not editing a `switch`.
- **L — Liskov Substitution.** A subtype must be usable anywhere its base is, without
  surprises. The classic violation: `Square extends Rectangle` breaking `setWidth`.
- **I — Interface Segregation.** Many small, focused interfaces beat one fat one — no
  class should be forced to implement methods it doesn't use.
- **D — Dependency Inversion.** Depend on abstractions, not concretions. High-level
  policy shouldn't import low-level detail; inject the interface (this is what enables
  testing/mocking — cross-ref the FastAPI/Angular DI notes).

SOLID is *the* LLD vocabulary — interviewers listen for you naming these as you justify
choices.

## Design patterns that actually come up

You don't need all 23 GoF patterns; know these and **when** to use each:

**Creational**
- **Factory** — centralize object creation when the concrete type varies (create the
  right `Spot`/`Vehicle` subtype from input).
- **Builder** — construct complex objects step by step (a request/config with many
  optional fields).
- **Singleton** — one shared instance (a registry/config). Use sparingly — it's global
  state and hurts testability; often DI is better.

**Structural**
- **Adapter** — make an incompatible interface fit (wrap a third-party API).
- **Decorator** — add behavior at runtime without subclassing (add logging/caching to
  a component; also the mental model for React HOCs and middleware).
- **Facade** — a simple front over a complex subsystem.

**Behavioral**
- **Strategy** — swap interchangeable algorithms behind one interface (pricing rules,
  sorting, payment methods). The single most useful LLD pattern for Open/Closed.
- **Observer** — subscribers react to a subject's changes (event listeners, display
  boards, pub/sub). 
- **State** — behavior changes with internal state via state objects (order lifecycle,
  a vending machine).
- **Command** — encapsulate an action as an object (undo/redo, task queues).

The senior move: reach for a pattern to solve a *named* problem (extensibility,
decoupling), never to show off. "I'd use Strategy so new pricing schemes are additive"
beats reciting definitions.

## Worked example: parking lot

A compact model showing the method:

- **Entities:** `ParkingLot` (Singleton — one per site) *has* many `Floor`s; each
  `Floor` *has* many `ParkingSpot`s. `Vehicle` is abstract → `Car`/`Bike`/`Truck`.
  `ParkingSpot` has a size and an occupancy state.
- **Assignment:** a `SpotAssignmentStrategy` (Strategy) picks a spot for a vehicle —
  nearest, or by size fit — swappable without touching the lot.
- **Pricing:** a `PricingStrategy` (Strategy) computes fees — hourly, flat, or surge —
  added by writing a new class (Open/Closed).
- **Creation:** a `SpotFactory` / `VehicleFactory` builds the right subtype.
- **Display:** availability boards are `Observer`s of the lot; they update when spots
  change.
- **Flow:** vehicle enters → strategy assigns a spot → `Ticket` issued → on exit,
  pricing strategy computes fee → `Payment` processed → spot freed → observers notified.

Notice: adding electric-charging spots or a new pricing model means *new classes*, not
edits to existing ones. That's the design working.

## Concurrency in LLD

Many LLD problems have a race at the "allocate a shared resource" step (last parking
spot, last movie seat, elevator dispatch). Be ready to:
- Guard the critical section (lock around spot allocation), or use an atomic
  compare-and-set / optimistic check, so two requests can't grab the same resource.
- Keep locks narrow (lock the spot/seat, not the whole lot) to preserve throughput.
- Mention idempotency for retried bookings.

## Common questions & pitfalls

- **Inheritance vs composition?** Prefer composition — it's more flexible and avoids
  deep, fragile hierarchies; use inheritance only for genuine "is-a."
- **Where would you use Strategy vs State?** Strategy = interchangeable algorithms
  chosen by the caller; State = behavior that changes as the object's own state
  transitions.
- **Why is Singleton controversial?** Hidden global state, hard to test, concurrency
  pitfalls — often replaced by DI.
- **How do you make this extensible?** Point to Open/Closed + Strategy/Factory: new
  behavior arrives as new classes.
- **Pitfalls:** over-engineering (patterns with no problem), god classes (violating
  SRP), leaking implementation details (breaking encapsulation), and ignoring the
  concurrency in the resource-allocation step.

## References
- *Design Patterns* (Gang of Four) · *Head First Design Patterns* (approachable)
- *Clean Code* / *Clean Architecture* (Robert C. Martin) — SOLID in depth
- *Refactoring* (Fowler) · refactoring.guru (patterns, with diagrams)

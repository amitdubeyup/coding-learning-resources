# Python web frameworks

Interview notes for Python's two dominant web frameworks.

- [`fastapi.md`](fastapi.md) — FastAPI: async, Pydantic validation, dependency
  injection, performance, testing, deployment.
- [`django.md`](django.md) — Django: MTV, the ORM (QuerySets, `select_related` /
  `prefetch_related`, N+1), views, DRF, security, deployment.

> **Currency note:** the FastAPI notes contain some **Pydantic v1** syntax
> (`@validator`, `root_validator`, `class Config: orm_mode`). Pydantic v2 uses
> `@field_validator`, `@model_validator`, and `model_config = ConfigDict(...)`.
> Flagged for a version pass — the working example of the v2 style is in
> [`../../projects/fastapi-user-management/`](../../projects/fastapi-user-management/).

## Runnable references
Working apps live in [`../../projects/`](../../projects/):
FastAPI (`fastapi-school-management`, `fastapi-user-management`) and Django
(`django-tennis-club`). Read the notes here, then see the patterns applied there.

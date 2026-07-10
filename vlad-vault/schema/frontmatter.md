---
type: reference
status: active
sensitivity: normal
scope: all
axis: vault
updated: 2026-06-11
tags: [schema, frontmatter, metadata, rag, lint]
---

# Frontmatter schema

Minimum contract for files that should be visible to agents or retrieval.

## Required for indexed vault files

```yaml
---
type: reference | decision | idea | plan | method | model | corpus | tech-profile | run-retro | backlog | edge | index
status: idea | proposed | accepted | active | superseded | archived
sensitivity: normal | private
scope: personal | work | all
tags: [hook1, hook2]
updated: YYYY-MM-DD
---
```

Use `date` instead of `updated` for dated artifacts whose identity is the event
date: decisions, diary entries, run retros. A file may carry both when useful.

## Status enum

- `idea` — rough seed, not yet shaped enough to depend on.
- `proposed` — coherent proposal, still awaiting a decision.
- `accepted` — decision taken; may be historical or not the current operating canon.
- `active` — current operating canon or current live index.
- `superseded` — replaced by a newer object; keep for provenance.
- `archived` — retained record, not part of current retrieval by default.

Do not use local-language status values in frontmatter. Put human wording in the
body if needed.

## Sensitivity

- `normal` — safe for the local namespace and non-public work use.
- `private` — may be indexed locally, but never leaves to a public remote or
  public artifact.

The egress wall is the invariant. `private` does not forbid local cross-corpus
edges or local cross-scope retrieval.

## Scope

- `personal` — personal corpora, reflection, people, timeline, private edges.
- `work` — project-facing work knowledge.
- `all` — cross-domain canon, orchestration, engine/method contracts.

`scope` says who/what the object is for. It is not a privacy label; use
`sensitivity` for that.

## Trust

`trust: primary | derived` belongs to data/content objects only, not operational
docs. Use it for corpora, extracted artifacts, personal syntheses, and edge
endpoint metadata. Do not add `trust` to `principles`, `preferences`,
`schema`, `agentics/method`, or other operational contracts.

## Optional disambiguators

```yaml
axis: vault | agentic | engine | cross
layer: base | meta | hybrid   # only with axis: agentic
related:
  - path/or/wiki-link
```

Use these only when they reduce ambiguity.

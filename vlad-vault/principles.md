---
type: reference
status: active
sensitivity: normal
scope: all
tags: [principles, conventions, vault, deltas]
updated: 2026-06-04
---

# Principles (vault conventions — base-of-bases)

This is the **base** for vault conventions across the namespace. Project vaults
(`music-vault`, `study-vault`, `content-factory-vault`, …) state only their
**deltas** against this file. Structure & entry points are in [[vlad-vault/vault-template|vault-template]];
this file holds the object-level writing rules.

**Core conventions (the base):**
one file = one object · names are search hooks · links via [[brackets]] · flat
structure · required frontmatter · no secrets in files (pointers only) · English by
default. Terms are canon in [[vlad-vault/glossary|glossary]] (level / stream / flow / meta-layer / zone /
engine).

## Refinements & vlad-level deltas

- **Language.** English by default, like the base (files exist for
  retrieval; English is what we read for search). Verbatim personal
  content quoted from Russian sources may stay Russian inside a file;
  the wrapper around it stays English.
- **Sensitivity.** Frontmatter may carry `sensitivity: normal | private`.
  `private` objects and personal corpora are **never** pushed to a
  public remote (this repo is local-only for now anyway).
- **Corpora.** The personal source (`vlad-life/`) is **not** copied into
  this vault. It lives by path and carries `trust: primary`; here we keep
  only notes *about* corpora (see `corpora/` — reserved until an engine
  exists).
- **`trust` is a property of DATA, not operational docs.** `trust:
  primary | derived` is carried by content objects (corpora, syntheses).
  Operational/infrastructure objects — `decisions/`, `agentics/method/`,
  `principles`, `preferences` — are curated canon and carry **no** `trust`
  field. The test stays: *"is this a piece of knowledge I'm storing, or a
  rule for how the system runs?"* Only the former gets `trust`.
- **`scope` field (formalised).** Every object may declare `scope:
  personal | work | all` — who reads/uses it. `all` = cross-domain canon
  (method, glossary); `personal` = private corpora/notes; `work` =
  project-facing. Used as a metadata filter; was practiced, now written.
- **`axis` / `layer` tagging (where it disambiguates).** Architecture / method /
  decision docs may declare which vocabulary they sit on (canon: [[vlad-vault/glossary|glossary]]):
  `axis: vault | agentic | engine | cross`. For `axis: agentic` add `layer: base |
  meta | hybrid` — *base* = product-making (streams/orchestrator), *meta* =
  meta-layer (improving the conveyor), *hybrid* = both. Apply only where it
  clarifies (cross/hybrid/meta docs benefit most); **don't** force it on pure
  content (tech-profiles, corpora) or files already obvious by folder.
- **Size cap is for reference objects, not write-ups.** The base 120-line
  soft cap applies to **single-concept reference** files. `decisions/`,
  `agentics/method/`, `tech/` profiles, and `type: model` docs legitimately
  run longer (they carry reasoning, not one lookup) — kept honest by strong
  internal structure (headers, tables), not by line count. No `research/`
  zone in this vault — that base rule is **retired here** (this vault is
  method + decisions + tech synthesis, not a research archive).

## Frontmatter

The current machine-facing contract lives in [[vlad-vault/schema/frontmatter|schema/frontmatter]]. This file
states the vault principle; schema states the fields and enums agents should
lint/index against.

Minimum for indexed vault files:

```yaml
---
type: corpus | person | note | ...
status: idea | proposed | accepted | active | superseded | archived
sensitivity: normal | private
scope: personal | work | all
tags: [hook1, hook2]
---
```

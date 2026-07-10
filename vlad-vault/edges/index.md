---
type: index
status: active
sensitivity: normal
scope: all
axis: vault
updated: 2026-07-10
tags: [edges, cross-domain, links, knowledge-graph]
related:
  - ../schema/frontmatter
---

# edges/

Durable cross-domain edges.

An edge is a small markdown object that materializes a connection between two
objects when a plain `[[wikilink]]` is not enough: cross-vault links, private
endpoints, mixed `scope`, or a relation that needs provenance.

## Why this exists

The namespace goal is LLM-independent storage. A query-time synthesis disappears
with the session; an edge file survives engine rebuilds and can be indexed,
reviewed, accepted, superseded, or archived.

## File shape

```yaml
---
type: edge
status: proposed | accepted | active | superseded | archived
sensitivity: normal | private
scope: personal | work | all
date: YYYY-MM-DD
from: path-or-wikilink
to: path-or-wikilink
relation: echoes | grounds | contradicts | refines | motivates | implements
tags: [edge, cross-domain]
---
```

Body: one sentence for the connection; why it matters; endpoint provenance;
what a future agent should do with it.

## Placement

All cross-domain edges live here, including private personal edges
(`sensitivity: private` — allowed locally, forbidden for public egress).

## Current edges

_(пусто)_

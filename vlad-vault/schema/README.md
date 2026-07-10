---
type: index
status: active
sensitivity: normal
scope: all
axis: vault
updated: 2026-06-06
tags: [schema, frontmatter, contracts, rag]
---

# schema/

Machine-facing contracts for `vlad-vault`.

This folder is not canon in the "final truth" sense. It is the current contract
that lets humans, agents, linters, and the RAG engine interpret files the same
way. When practice changes, update the schema first, then migrate files.

## Contracts

- [[vlad-vault/schema/frontmatter|Frontmatter schema]] — required fields, status enum,
  and metadata semantics for retrieval.

## Rule

Rules may stay alive and revisable, but every operational rule that affects
retrieval should leave a machine-readable trace: field, enum, source entry,
edge, or link convention.

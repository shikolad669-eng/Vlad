---
type: reference
status: active
sensitivity: private
scope: work
date: 2026-06-26
updated: 2026-06-26
tags: [secrets-map, pointers]
related:
  - HOME
  - ../../vlad-vault/secrets-map
---

# Secrets map — content-factory

Pointers only, never values. No secrets live in tracked files (skandar base rule).

- None yet (concept stage, nothing provisioned).
- When the pipeline is built: API keys (voice clone, lip-sync, video gen, scheduler) →
  per-project `.env` under each code project, never here. Global access map:
  `[[../../vlad-vault/secrets-map]]`.

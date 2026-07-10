---
type: reference
status: active
sensitivity: normal
scope: work
axis: vault
date: 2026-07-10
updated: 2026-07-10
tags: [home, map, drafting]
related:
  - principles
  - status
  - ../../vlad-vault/vault-template
---

# drafting-vault

Knowledge base of the drafting domain. Semantic map — start here. Door is
`../CLAUDE.md`. Conforms to [[vlad-vault/vault-template|vlad-vault/vault-template]].

## What this is

Черчение Влада: чертежи деталей и узлов, проекты, спецификации, версии, уроки о
том, как чертить. Тяжёлые файлы (DWG/STEP/PDF) живут в [[drafting/cad/README|cad/]]
(вне git); vault держит карточки-указатели. Инструмент/формат фиксируется в
[[drafting/drafting-vault/status|status]] при наполнении.

## Mandatory

- [[drafting/drafting-vault/status|status]] — hot current state (read every session).
- [[drafting/drafting-vault/principles|principles]] — conventions (vlad base + deltas; `market/` дропнут — не бизнес).
- **plans/** — [[drafting/drafting-vault/plans/README|планы]] (проект/партия чертежей/цель).
- **tasks/** — [[drafting/drafting-vault/tasks/README|per-cycle run-data]].

## Zones

- **drawings/** — [[drafting/drafting-vault/drawings/README|каталог чертежей]]: один файл = один чертёж/деталь (карточка → `cad/`).
- decisions/ · lessons/ — grow by need ([[drafting/drafting-vault/decisions/README|decisions/README]] · [[drafting/drafting-vault/lessons/README|lessons/README]]).

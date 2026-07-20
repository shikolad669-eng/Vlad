---
type: reference
status: active
sensitivity: normal
scope: work
axis: vault
date: 2026-07-20
updated: 2026-07-20
tags: [home, map, discord-custom]
related:
  - principles
  - status
  - ../../vlad-vault/vault-template
---

# discord-custom-vault

Knowledge base of the Discord-custom business. Semantic map — start here, follow
links by topic. Door is `../CLAUDE.md`. Conforms to
[[vlad-vault/vault-template|vlad-vault/vault-template]].

## What this is

«Discord custom» как бизнес: заказная сборка и оформление Discord-серверов под
клиента — структура каналов, роли и права, боты и автоматизация, брендинг
(иконки, баннеры, эмодзи), модерация, интеграции. Vault держит знание (оффер,
клиенты, процессы, прецеденты); тяжёлая графика — в `../assets/` (вне git),
здесь карточки-указатели.

## Mandatory

- [[discord-custom/discord-custom-vault/status|status]] — hot current state (read every session).
- [[discord-custom/discord-custom-vault/principles|principles]] — conventions (vlad base + deltas).
- **market/** — [[discord-custom/discord-custom-vault/market/README|рынок и спрос]] (где клиенты,
  конкуренты, цены, референсы) — заполняется по мере разведки.
- **plans/** — [[discord-custom/discord-custom-vault/plans/README|планы бизнеса]].
- **tasks/** — [[discord-custom/discord-custom-vault/tasks/README|per-cycle run-data]] (spec → plan → build → review → record).

## Client business

- **positioning.md** — [[discord-custom/discord-custom-vault/positioning|внешнее предложение]] (что продаём, пакеты, кому).
- **clients/** — [[discord-custom/discord-custom-vault/clients/README|заказы и клиенты]] (один файл = один клиент/заказ).

## Shared

- decisions/ · lessons/ · systems/ · tools/ — grow by need
  ([[discord-custom/discord-custom-vault/decisions/README|decisions/README]] · [[discord-custom/discord-custom-vault/lessons/README|lessons/README]] · [[discord-custom/discord-custom-vault/systems/README|systems/README]] ·
  [[discord-custom/discord-custom-vault/tools/README|tools/README]]).

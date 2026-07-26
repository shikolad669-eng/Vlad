---
type: reference
status: active
sensitivity: normal
scope: work
axis: vault
date: 2026-07-27
updated: 2026-07-27
tags: [home, map, ai-agents, бизнес]
related:
  - principles
  - status
  - ../../vlad-vault/vault-template
---

# ai-agents-vault

Knowledge base of the AI-agents business. Semantic map — start here, follow links
by topic. Door is `../CLAUDE.md`. Conforms to
[[vlad-vault/vault-template|vlad-vault/vault-template]].

## What this is

Продаём бизнесам не «ИИ», а **решение конкретной боли** (пропущенные сообщения =
потерянные записи, рутина менеджеров, дорогая поддержка). ИИ-агент — инструмент.
Два потока денег:

```
Разовое внедрение (setup fee)      →  оплатило запуск
Ежемесячная подписка (обслуживание) →  строит актив
```

Принципы бизнеса: одна ниша + один тип агента на старте; продавать результат
(сэкономленные часы, закрытые лиды), а не технологию; обслуживание — отдельный
продукт, а не гарантия.

## Mandatory

- [[ai-agents/ai-agents-vault/status|status]] — hot current state (read every session).
- [[ai-agents/ai-agents-vault/principles|principles]] — conventions (vlad base + deltas).
- **market/** — [[ai-agents/ai-agents-vault/market/README|рынок и лиды]].
- **plans/** — [[ai-agents/ai-agents-vault/plans/README|планы]].
- **tasks/** — [[ai-agents/ai-agents-vault/tasks/README|per-cycle run-data]] (spec → plan → build → review → record).

## Оффер (что продаём)

- [[ai-agents/ai-agents-vault/systems/products|Продукты и услуги]] — что именно продаём.
- [[ai-agents/ai-agents-vault/systems/pricing|Ценообразование]] — сколько берём и за что.
- [[ai-agents/ai-agents-vault/systems/subscription|Обслуживание и подписка]] — ретеншен, главный поток.

## Как это работает

- [[ai-agents/ai-agents-vault/systems/sales-funnel|Воронка продаж]] — как находим и закрываем.
- [[ai-agents/ai-agents-vault/systems/delivery|Процесс внедрения]] — как делаем агента под ключ.
- [[ai-agents/ai-agents-vault/systems/tech-stack|Технологический стек]] — на чём строим.
- [[ai-agents/ai-agents-vault/systems/unit-economics|Финмодель]] — экономика, точки прибыли.

## Клиенты

- [[ai-agents/ai-agents-vault/clients/README|clients/]] — сделки (один файл = один клиент).
  Живой: [[ai-agents/ai-agents-vault/clients/tatyana|Татьяна]] — внедрение сдано и оплачено.

## Рынок

- [[ai-agents/ai-agents-vault/market/niches|Клиенты и ниши]] — кому продаём, с чего начать.
- [[ai-agents/ai-agents-vault/market/leads-salons|Лиды: салоны и барбершопы Караганды]] (30).
- [[ai-agents/ai-agents-vault/market/leads-schools|Лиды: онлайн-школы и курсы Караганды]] (50).
- `market/leads/` — карточки лидов (`salons/`, `schools/`).

## Планы

- [[ai-agents/ai-agents-vault/plans/launch-90-days|План запуска — 90 дней]].

## Термины

- [[ai-agents/ai-agents-vault/glossary|glossary]] — понятия работы с ИИ-агентом
  (агентный цикл, контекст, tool use, RAG, MCP, гардрейлы) с толкованием «что это
  на практике». Термины по самим моделям — в
  [[ai-agents/ai-agents-vault/tools/llm/glossary|tools/llm/glossary]].

## Tools

- [[ai-agents/ai-agents-vault/tools/llm/README|tools/llm/ — LLM Wiki]]: провайдеры, сравнение,
  как выбрать модель, глоссарий. Питает [[ai-agents/ai-agents-vault/systems/tech-stack|техстек]];
  кросс-доменный справочник — указатель в [[vlad-vault/tech/README|vlad-vault/tech]].

## Shared

- decisions/ · lessons/ — grow by need
  ([[ai-agents/ai-agents-vault/decisions/README|decisions/README]] ·
  [[ai-agents/ai-agents-vault/lessons/README|lessons/README]]).
- [[ai-agents/ai-agents-vault/secrets-map|secrets-map]] — где живут доступы (без значений).

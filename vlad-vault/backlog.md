---
title: Backlog — реестр задач уровня vlad (кратко здесь, решается ниже)
type: registry
status: active
sensitivity: normal
scope: all
axis: vault
date: 2026-07-10
updated: 2026-07-10
tags: [backlog, registry, tasks]
related:
  - inbox/README
  - backlog-review-protocol
  - HOME
---

# Backlog — реестр задач уровня vlad

**Все живые пункты одной строкой**: суть · исполнитель (домен/агент) · указатель
вниз на полный контекст. Захват — через [[vlad-vault/inbox/README|inbox/]]; разбор — по
[[vlad-vault/backlog-review-protocol|backlog-review-protocol]].

Гигиена строки (унаследовано из базы):
- Указатели — **полные пути**, не сокращения: холодный агент не должен знать
  раскладку наизусть.
- Без счётчиков файлов в строках — они протухают; фиксируй инвариант, цифра
  живёт в `git status`.
- Строка, называющая файл, называет существующий файл.

## Live

- **Зафиксировать деньги по сделке Татьяны** (сумма setup fee + подписка/мес) ·
  `ai-agents` · [[ai-agents/ai-agents-vault/clients/tatyana|ai-agents/ai-agents-vault/clients/tatyana]]
  → оттуда в [[ai-agents/ai-agents-vault/systems/unit-economics|unit-economics]].
  Без факта MRR домена не считается.
- **Оформить подписку на обслуживание Татьяне** (состав, цена, дата первого
  платежа) · `ai-agents` · [[ai-agents/ai-agents-vault/systems/subscription|ai-agents/ai-agents-vault/systems/subscription]].
- **Начать касания по базе Караганды** (80 лидов, ни одного контакта) ·
  `ai-agents` · [[ai-agents/ai-agents-vault/market/README|ai-agents/ai-agents-vault/market/]].
- **Удалить исходный волт «Влад бизнес»** после проверки домена Владом ·
  уровень `vlad` · [[vlad-vault/meta-map|vlad-vault/meta-map]] → «Вне карты».

## Done

- 2026-07-27 — волт «Влад бизнес» слит в неймспейс доменом `ai-agents/` ·
  [[vlad-vault/entry-points|entry-points]] → «Реестр приведения к канону».

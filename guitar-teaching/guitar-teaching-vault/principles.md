---
type: reference
status: active
sensitivity: normal
scope: work
date: 2026-07-30
updated: 2026-07-30
tags: [principles, conventions, deltas]
related:
  - ../../vlad-vault/principles
  - ../../vlad-vault/vault-template
---

# Principles — guitar-teaching (deltas)

Follows the **vlad base**: [[vlad-vault/principles|vlad-vault/principles]] (object rules) +
[[vlad-vault/vault-template|vlad-vault/vault-template]] (structure & entry points). Only deltas
here.

## Deltas

- **Client + education business.** Зоны `clients/` (один файл = один ученик) и
  `curriculum/` (программа/курс) — по опциям vault-template «if a client
  business» и «if an education business».
- **`curriculum/` ≠ `lessons/`.** Омоним: `lessons/` в базовом шаблоне —
  операционные уроки самого домена («триггер → правило → почему»), не уроки
  гитары. Программа/материалы урока живут в `curriculum/`.
- **Ученик ≠ лид.** Карточка в `market/leads/` — контакт без первого урока;
  переезжает в `clients/` после первого реального занятия.
- **Language.** English for infra/canon; Russian for живые заметки, программу,
  учеников и всё, что Влад читает как преподаватель.
- **Наружу — через витрину.** Промо, отзывы и разборы уроков публикует
  `danny-content/` по своей routing-table; домен готовит материал, не постит
  сам.

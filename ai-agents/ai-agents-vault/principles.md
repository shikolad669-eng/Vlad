---
type: reference
status: active
sensitivity: normal
scope: work
date: 2026-07-27
updated: 2026-07-27
tags: [principles, conventions, deltas]
related:
  - ../../vlad-vault/principles
  - ../../vlad-vault/vault-template
---

# Principles — ai-agents (deltas)

Follows the **vlad base**: [[vlad-vault/principles|vlad-vault/principles]] (object rules) +
[[vlad-vault/vault-template|vlad-vault/vault-template]] (structure & entry points). Only deltas
here.

## Deltas

- **Client business.** Зоны `clients/` (один файл = один клиент/сделка) и
  `market/leads/` (холодная база: `salons/`, `schools/`) — по опции vault-template
  «if a client business».
- **`positioning.md` не заводим.** Внешний оффер уже разложен по объектам:
  [[ai-agents/ai-agents-vault/systems/products|products]] (что продаём) +
  [[ai-agents/ai-agents-vault/systems/pricing|pricing]] (за сколько) +
  [[ai-agents/ai-agents-vault/market/niches|niches]] (кому). Отдельная страница-оффер
  дублировала бы их и разошлась.
- **Лид ≠ клиент.** Карточка в `market/leads/` — гипотеза из 2ГИС (боль
  предполагаемая, контакта нет). Переезжает в `clients/` только после первого
  реального разговора; статус ведётся в поле `статус` карточки и в таблице
  соответствующего индекса `market/leads-*.md`.
- **Деньги — только по факту.** В карточку клиента пишем оплаченные суммы, а не
  прайсовые. Не знаем — пишем «уточнить», не подставляем цифру из пакета
  ([[ai-agents/ai-agents-vault/systems/pricing|pricing]] — прайс, не факт).
- **Naming.** Канон-файлы (структура, системы, планы) — английский kebab-case;
  карточки лидов сохраняют имя бизнеса как есть (`Ручки Ножки.md`) — по нему
  клиент ищется глазами и по нему же ведётся 2ГИС.
- **Language.** English for infra/canon; Russian for живые заметки, оффер,
  клиентов и всё, что Влад читает как владелец бизнеса.
- **Наружу — через витрину.** Кейсы, отзывы и промо услуги публикует
  `danny-content/` по своей routing-table; домен готовит материал, не постит сам.
- **Наследие волта.** Домен рождён 2026-07-27 слиянием отдельного Obsidian-волта
  «Влад бизнес» в неймспейс. Frontmatter старых карточек лидов оставлен как был
  (`tags`, `статус`, `источник`) — переписывать 80 карточек ради схемы дороже,
  чем польза; новые объекты пишутся по базе.

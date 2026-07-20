---
type: reference
status: active
sensitivity: normal
scope: work
date: 2026-07-20
updated: 2026-07-20
tags: [principles, conventions, deltas]
related:
  - ../../vlad-vault/principles
  - ../../vlad-vault/vault-template
---

# Principles — discord-custom (deltas)

Follows the **vlad base**: [[vlad-vault/principles|vlad-vault/principles]] (object rules) +
[[vlad-vault/vault-template|vlad-vault/vault-template]] (structure & entry points). Only deltas
here.

## Deltas

- **Client business.** Держим зоны `clients/` (один файл = клиент/заказ) и
  `positioning.md` (внешний оффер) — по опции vault-template «if a client business».
- **Assets by pointer.** Тяжёлая графика (иконки, баннеры, эмодзи, GIF, макеты)
  живёт в `../assets/` (вне git); vault держит карточку-указатель (что это, чей
  заказ, где лежит, статус). Файл без карточки = потерянный файл.
- **Secrets — только указатели.** Токены ботов, доступы к Discord-аккаунту
  бизнеса и площадкам заказов НИКОГДА в трекаемых файлах — в `~/vlad/secrets/`
  / `.env`, здесь только `secrets-map.md`. Discord bot-token утёк = сервер
  угнан, поэтому граница жёсткая.
- **Language.** English for infra/canon; Russian for живые заметки о заказах,
  оффер и всё, что Влад читает как владелец бизнеса.
- **Наружу — через витрину.** Кейсы/промо/посты об услуге публикует
  `danny-content/` по своей routing-table; домен готовит материал, не постит сам.

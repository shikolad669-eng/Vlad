---
type: reference
status: active
sensitivity: normal
scope: work
date: 2026-07-24
updated: 2026-07-24
tags: [principles, conventions, deltas]
related:
  - ../../vlad-vault/principles
  - ../../vlad-vault/vault-template
---

# Principles — phyto (deltas)

Follows the **vlad base**: [[vlad-vault/principles|vlad-vault/principles]] +
[[vlad-vault/vault-template|vlad-vault/vault-template]]. Only deltas here.

## Deltas

- **`market/` остаётся** — phyto это бизнес (B2B-опт фитопродукции), template's
  mandatory `market/` в силе.
- **`systems/` — ядро вики.** Бизнес-модель, каналы, поставщик, оптовый оффер:
  один файл = один компонент (что это + зачем, не реализация).
- **`catalog/` zone added** — карта ассортимента (категории + репрезентативные
  срезы). Данные `derived`: **источник правды — живой [travnik.kz](https://www.travnik.kz/)**,
  vault держит снимок с датой. Цены/наличие в vault — не канон, а слепок.
- **`sources.md`** — провенанс: откуда снят каждый факт (сайт/инста/поиск + дата).
  Обязателен, потому что данные derived, а не от Влада.
- **Trust.** Всё наполнение = `derived` (снято с публичных витрин), не `primary`.
  Факты «от Влада» (реальные условия опта, реквизиты) помечаются явно при вводе.
- **Секреты** (реквизиты юрлица, доступы к CRM/маркетплейсам, договоры) — только
  в `~/vlad/secrets/`, здесь указатели ([[phyto/phyto-vault/secrets-map|secrets-map]]).
- **Language.** Контент — русский (язык бизнеса и клиента в РК); infra
  (frontmatter, имена файлов, зоны) — English (base rule).
- **Дисклеймер.** Продукция «не является лекарственным средством» — этот статус
  несётся во всех клиентских формулировках, вики его не теряет.

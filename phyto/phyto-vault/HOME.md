---
type: reference
status: active
sensitivity: normal
scope: work
axis: vault
date: 2026-07-24
updated: 2026-07-24
tags: [home, map, phyto, wiki]
related:
  - principles
  - status
  - sources
  - ../../vlad-vault/vault-template
---

# phyto-vault — LLM-вики оптового фитобизнеса

Knowledge base домена phyto. Semantic map — start here. Door is `../CLAUDE.md`.
Conforms to [[vlad-vault/vault-template|vlad-vault/vault-template]].

## What this is

**LLM-вики** оптового (B2B) бизнеса фитопродукции. Витрина — сайт
[travnik.kz](https://www.travnik.kz/) + Instagram [@sibir.kz](https://www.instagram.com/sibir.kz/).
Цель вики: чтобы агент/человек за один заход понял бизнес и мог представлять
его, отвечать оптовику и клиенту, вести каталог. Данные `derived` — источник
правды — живой сайт; см. [[phyto/phyto-vault/sources|sources]].

## В одном абзаце

Эксклюзивный дистрибьютор фитопродукции **фитоцентра Гордеева** по Казахстану.
Центральный склад — Караганда (Гапеева 9/2), отгрузка розницы и опта по всей РК.
Позиционирование — «научная фитотерапия, прямые поставки со склада».
~780 SKU / 19 категорий. Опт — аптекам, ЗОЖ-магазинам, маркетплейс-продавцам,
фитокабинетам; прайс по запросу, полный пакет сертификатов и бух. документов.

## Mandatory

- [[phyto/phyto-vault/status|status]] — hot current state (read every session).
- [[phyto/phyto-vault/principles|principles]] — conventions (vlad base + deltas).
- [[phyto/phyto-vault/sources|sources]] — провенанс данных (derived).
- **market/** — [[phyto/phyto-vault/market/overview|рынок, позиционирование, аудитория]].
- **plans/** — [[phyto/phyto-vault/plans/README|планы/горизонт]].
- **tasks/** — [[phyto/phyto-vault/tasks/README|per-cycle run-data]].

## Systems — ядро бизнеса

- [[phyto/phyto-vault/systems/business-model|business-model]] — цепочка
  поставщик → дистрибьютор → B2B-опт; как зарабатывает.
- [[phyto/phyto-vault/systems/wholesale-offer|wholesale-offer]] — оптовый оффер:
  кому, что, условия, документы.
- [[phyto/phyto-vault/systems/lead-gen|lead-gen]] — алгоритм поиска оптовых
  клиентов (сегменты, источники, скоринг, выход в [[phyto/phyto-vault/market/wholesale-leads|wholesale-leads]]).
- [[phyto/phyto-vault/systems/promotion|promotion]] — алгоритмы продвижения
  бизнеса: Instagram, Threads, маркетплейсы, локалка, WhatsApp, сайт, B2B-магнит.
- [[phyto/phyto-vault/systems/automation-claude-code|automation-claude-code]] —
  автоматизация процессов через ИИ (Claude Code): движок над викой, апрув Влада.
- [[phyto/phyto-vault/systems/supplier-gordeev|supplier-gordeev]] — поставщик
  (фитоцентр Гордеева, РФ).
- [[phyto/phyto-vault/systems/channels|channels]] — каналы: сайт, Instagram,
  WhatsApp; контакты.

## Catalog

- [[phyto/phyto-vault/catalog/products-detailed|products-detailed]] — **полный
  список 780 товаров со всеми полями** (состав, применение, штрихкод, ссылки).
- [[phyto/phyto-vault/catalog/full-catalog|full-catalog]] — компактный список
  (имя/фасовка/цена). Сводка: [[phyto/phyto-vault/catalog/categories|categories]].
- Машинные данные: `products.csv`, `products.json`. Вход:
  [[phyto/phyto-vault/catalog/README|catalog/README]].

## Zones (grow by need)

- decisions/ · lessons/ — [[phyto/phyto-vault/decisions/README|decisions]] ·
  [[phyto/phyto-vault/lessons/README|lessons]].

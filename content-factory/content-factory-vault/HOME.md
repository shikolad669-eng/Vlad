---
type: reference
status: active
sensitivity: private
scope: work
axis: vault
date: 2026-06-26
updated: 2026-07-06
tags: [home, map, content-factory, smm, ai-pipeline]
related:
  - principles
  - status
  - positioning
  - ../../vlad-vault/vault-template
  - ../../vlad-vault/ideas/2026-06-26-team-and-ventures-synergy
---

# content-factory-vault

Knowledge base of the content-factory venture. Semantic map — start here, follow links by
topic. Door is `../CLAUDE.md`. Conforms to
[[vlad-vault/vault-template|vlad-vault/vault-template]].

> **Перепрофилирование 2026-07-04:** рабочая роль завода = **цех** (процессы контента
> Скандара, станки, intake, автопостинг) → [[content-factory/content-factory-vault/decisions/2026-07-04-factory-as-workshop|decisions/2026-07-04-factory-as-workshop]].
> Shared-венчур ниже — запаркованная ветка концепта. Спек контент-единицы:
> [[content-factory/content-factory-vault/content-bundle-spec|content-bundle-spec]].

> Cross-domain strategy (team synergy, three engines, asset separation, two ICPs) lives up
> in `~/skandar/skandar-vault/ideas/2026-06-26-team-and-ventures-synergy.md` (машина Скандара). Here =
> business-local brain.

## What this is
AI-pipeline content / SMM service for local businesses (restaurants, brands), sold on
**Adil's** distribution and face. The differentiator is not "another SMM agency" — it is
**"content from the guy doing 300–560K views"** plus a per-client knowledge base so the AI
output is grounded, not generic slop.

## Mandatory
- [[content-factory/content-factory-vault/status|status]] — hot current state (read every session).
- [[content-factory/content-factory-vault/principles|principles]] — conventions (skandar base + deltas).
- **market/** — [[content-factory/content-factory-vault/market/overview|market/overview]] (demand = Adil's dropped inbound; competitors = SMM agencies).
- **plans/** — [[content-factory/content-factory-vault/plans/vision|plans/vision]] (concept; MVP deferred; demand-first discipline).

## Offer
- [[content-factory/content-factory-vault/positioning|positioning]] — the pricing ladder (Adil-personal → factory → pure-AI), the moat, the
  two-tier downsell of Adil's face.

## People (roles)
- **Adil** — face + sales (the whole sales function). Record:
  [[content-factory/content-factory-vault/ideas/2026-06-23-adil-aigul-first-engagement|ideas/2026-06-23-adil-aigul-first-engagement]].
- **Build** — Vlad (candidate) / or another. Record:
  `~/skandar/skandar-vault/people/vlad.md` (машина Скандара).
- **Skandar** — system + process + business judgment.

## Pipelines (агентский конвейер: как агент собирает)
- [[content-factory/content-factory-vault/pipelines/HOME|pipelines/HOME]] — **агентские видео/контент-пайплайны** (зеркало skandar `agentics/`):
  стримы, контракт ручное/авто, 4 код-гейта, show-then-fix чекпоинт, субагенты.
  Content-type [[content-factory/content-factory-vault/pipelines/content-type/talking-head|pipelines/content-type/talking-head]] заполнен (разговорное видео → рил + пост);
  остальные типы — слоты. Шов: `pipelines/` = конвейер (agentic), `processes/video-station`
  = ремесло (цифры), `video-pipeline/` (корень завода) = код. Создано 2026-07-06.
- **Экспортная роль завода (2026-07-06, сверху):** завод собирает и поддерживает
  **пайплайн-пакеты** — раздаточные версии станков для чужого агента (каркас +
  нейтральный демо-стиль + агентский setup-плейбук с чек-пойнтами + тестовый пример;
  фирменный стиль Макси не раздаётся). Заказчик — академия (воркшопы + платный TG);
  вопросы из канала = intake сырья для патчей. Роли:
  `../../vlad-vault/decisions/2026-07-06-pipelines-product-roles.md`;
  идея: `../../vlad-vault/ideas/2026-07-06-pipelines-as-product.md`.
  Пока — роль на будущее, ничего не собираем без брифа.

## Processes (цех: ремесло — константы и ffmpeg-команды)
- [[content-factory/content-factory-vault/processes/video-station|processes/video-station]] — видео-станция, канон: 4 трека (генеративный /
  говорящая голова / трекинг-VFX / нарезка длинного), общий монтажный слой
  (нормы, сабы, обложки, звук, экспорт), интерфейс станции. Дистиллят из
  run-data витрин (2026-07-04). **Пороги гейтов живут здесь; конвейер их зовёт из
  [[content-factory/content-factory-vault/pipelines/HOME|pipelines/HOME]].**

## Research
- [[content-factory/content-factory-vault/research/2026-07-04-agentic-montage-frameworks|research/2026-07-04-agentic-montage-frameworks]] — агентские монтажные каркасы
  (декларативная сборка, авто-каты, рендер-API): что брать в станцию, что нет.

## Tools
- [[content-factory/content-factory-vault/tools/telegram-channel-bot|tools/telegram-channel-bot]] — first pipeline base (test scaffold): AI drafts
  channel posts in-voice, owner approves with one tap, bot publishes. The
  content-factory loop on the smallest real surface.

## Shared
- decisions/ · lessons/ · systems/ · tools/ · processes/ · research/ — grow by need.

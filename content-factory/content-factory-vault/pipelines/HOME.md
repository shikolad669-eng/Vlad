---
type: reference
status: active
sensitivity: private
scope: work
axis: agentic
date: 2026-07-06
updated: 2026-07-06
tags: [pipelines, video, agentic, method, content-type, home, index]
related:
  - method/streams
  - content-type/talking-head
  - ../processes/video-station
  - ../content-bundle-spec
  - ../../../vlad-vault/agentics/HOME
  - ../../../vlad-vault/decisions/2026-07-04-pipeline-canon-placement
---

# Pipelines — агентские видео/контент-пайплайны цеха

Как агент (**Денни**-orchestrator) собирает контент по шагам — **зеркало skandar-уровневого
`agentics/`**, но для видео/постов вместо dev. Живёт в заводе: цех — единственный исполнитель
видео-станции (ADR `~/skandar/skandar-vault/decisions/2026-07-04-pipeline-canon-placement.md` (машина Скандара)).
Тот же слот, что `agentics/` наверху: там cross-project *как строим софт*; здесь *как собираем видео/пост*.

## Шов (read first) — конвейер vs ремесло vs код

Три разных знания, намеренно раздельно — **не дублировать, иначе дрейф** (грабля byte-sync из agentics):

- **Конвейер (здесь, `pipelines/`)** — агентская механика: стримы, контракт ручное/авто, гейты,
  review-чекпоинт, субагенты, I/O content-type. Ось **agentic**.
- **Ремесло ([[content-factory/content-factory-vault/processes/video-station|processes/video-station]])** — константы и ffmpeg-команды: тонмап-цепочки, LUFS,
  crf, цвета, шрифты, грабли жанра. Продукт цеха.
- **Код (`video-pipeline/` в корне завода)** — исполняемые модули (инструменты стримов).

Правило: `pipelines/` **называет** гейт → `video-station` даёт **порог/цифру** → `video-pipeline`
его **исполняет**. Один источник на факт.

## Термины (глоссарий, не выдумка)

Ось agentic канонизирована в глоссарии (`../../../vlad-vault/glossary.md`):
**stream** (дорожка) · **flow** (путь одного видео) · **orchestrator** (Денни, гонит одно видео) ·
**meta-layer** (сессия улучшения конвейера). «Станок/станция» — off-glossary, ретайрено в
неформальное; в коде — «инструмент стрима».

## Method (canon)

- [[content-factory/content-factory-vault/pipelines/method/streams|method/streams]] — 5 стримов, контракт ручное/авто, 4 код-гейта, show-then-fix чекпоинт,
  политика субагентов.
- [[content-factory/content-factory-vault/pipelines/method/run-schema|method/run-schema]] — что Денни пишет после прогона (`run.md` в бандл + строка в runs/):
  гейты, **residual чекпоинта** (сигнал улучшения), грабли, дельты. Петля улучшения конвейера.

## Content-type (один на тип `вход × цель`)

- [[content-factory/content-factory-vault/pipelines/content-type/talking-head|content-type/talking-head]] — **ЗАПОЛНЕН**: разговорное видео → рил (обложка + сабы + инфографика +
  сжат) + пост ≤5 тегов.
- Слоты (0 прогонов, вне скоупа): [[content-factory/content-factory-vault/pipelines/content-type/generative|content-type/generative]] (трек A · Veo) · [[content-factory/content-factory-vault/pipelines/content-type/vfx-track|content-type/vfx-track]]
  (трек C) · [[content-factory/content-factory-vault/pipelines/content-type/long-cut|content-type/long-cut]] (трек D · нарезка) · [[content-factory/content-factory-vault/pipelines/content-type/carousel|content-type/carousel]] · [[content-factory/content-factory-vault/pipelines/content-type/post-only|content-type/post-only]].

## Runs

- [[content-factory/content-factory-vault/pipelines/runs/README|runs/README]] — ретро прогонов. Run-data роликов живёт в бандлах витрин (primary), сюда —
  только дистиллят. Зеркало agentics/runs.

## Lessons

- [[content-factory/content-factory-vault/pipelines/lessons/README|lessons/README]] — грабли, ставшие код-гейтами: контраст-структурный · рендерер-общий ·
  тонмап-первым · аудио-экспорт-стерео. rule + trigger.

## Open threads

- Декларативная сборка (один CUTS-JSON → таймлайн+сабы+окна) — пилот v3 в академии, не в content-type.
- ASS-из-whisper обобщённый — не сделан.
- SFX-слой — приоритет №1 ремесла, 0 прогонов.
- Агентная параллель (moment-selection веером по клипам) вырастает в `long-cut`/VO — слот.

## Promotion trigger

Второй исполнитель станка (напр. команда Адиля гоняет у себя) → канон поднимается на уровень,
видящий обоих (зеркало ADR pipeline-canon-placement). До тех пор — здесь, секцией завода.

---

See also: [[content-factory/content-factory-vault/HOME|HOME]] · [[content-factory/content-factory-vault/processes/video-station|processes/video-station]] · [[vlad-vault/agentics/README|vlad-vault/agentics]].

---
type: method
status: active
sensitivity: private
scope: work
axis: agentic
date: 2026-07-06
updated: 2026-07-06
tags: [method, run, retro, schema, feedback, improvement, analysis]
related:
  - ../HOME
  - ../runs/README
  - ../lessons/README
  - ../../processes/video-station
  - ../../../../vlad-vault/agentics/method/lessons-schema
---

# Method — run-schema (что Денни пишет после прогона)

Дом run-данных для **улучшения и анализа конвейера** (зеркало
`~/skandar/skandar-vault/agentics/method/lessons-schema.md` (машина Скандара)). Без этой записи прогон
ничему не учит — meta-layer нечего читать.

## Куда пишется (два места, разный род)

1. **Полный record — в бандл витрины** (`trust: primary`, у Денни):
   `~/vlad/danny-content/posts/<YYYY-MM-DD-slug>/run.md`. Пишет **Денни** сразу после прогона.
   Живёт с роликом; не копируется наверх целиком.
2. **Регистрация — строка в [[content-factory/content-factory-vault/pipelines/runs/README|runs/README]]** (карта прогонов). Денни добавляет одну строку
   (чтобы карта не устаревала — та же дисциплина, что «обновить README» в post-workflow).
3. **Дистиллят — в `pipelines/runs/<slug>.md`** лифтит **meta-layer** (аналитическая сессия), не
   Денни. Только cross-run-релевантная дельта.

## Что в `run.md` (фикс. поля)

```yaml
type: run
content-type: talking-head        # какой заполненный тип гоняли
date: YYYY-MM-DD
slug: <slug>
surface: [ig-@skandar1104]
status: done
```

- **Вход/цель** — видео (path, primary), тезисы, бриф, поверхность.
- **Стримы — что реально шло** — по стриму (prep/visual/subs/audio/cover/assembly): auto/manual,
  время, отклонения от рецепта.
- **Гейты (числа, не «на глаз»)** — contrast-floor (значение + pass/fail) · L/R RMS (равны?) ·
  длительность (совпала со сборкой?).
- **★ Residual чекпоинта — ГЛАВНЫЙ сигнал улучшения.** Что Скандар правил на show-then-fix по трём
  выходам: **пост · название кавера · текст инфографики** — сколько правок и какие. Это видео-аналог
  vibecode-tail: **сжимается от прогона к прогону → конвейер улучшается**; растёт → авто-драфты
  деградируют. Мерить, не забывать.
- **Грабли** — известная сработала (гейт поймал?) / **новая** (→ строка в [[content-factory/content-factory-vault/pipelines/lessons/README|lessons/README]] +
  дельта в [[content-factory/content-factory-vault/processes/video-station|processes/video-station]]).
- **Дельты** — в код (`video-pipeline/`), в ремесло (video-station), в канон (pipelines). Что
  предложено поднять.
- **Carried / TODO** — что осталось на следующий прогон.

## Петля (как это улучшает конвейер)

```
прогон → run.md в бандле (Денни) → строка в runs/README (Денни)
                                        │
             meta-layer (аналитическая сессия, offline, cross-run)
                                        ▼
   residual-тренд · новые грабли → lessons/ (гейт) · дельты → video-station (порог) / video-pipeline (код)
```

Meta-layer работает **поперёк прогонов, offline** — не лезет в один прогон (как в agentics). Денни
пишет данные; улучшает конвейер meta-layer.

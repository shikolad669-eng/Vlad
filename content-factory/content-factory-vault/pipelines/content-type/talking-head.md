---
type: content-type
status: active
sensitivity: private
scope: work
axis: agentic
date: 2026-07-06
updated: 2026-07-06
tags: [content-type, talking-head, video, reel, plates, subs, pipeline]
related:
  - ../HOME
  - ../method/streams
  - ../../processes/video-station
  - ../../content-bundle-spec
---

# Content-type — разговорное видео (talking-head + инфографика)

Первый заполненный content-type. Трек B + «плашки над головой». Механика — [[content-factory/content-factory-vault/pipelines/method/streams|method/streams]];
ремесленные пороги/цифры — [[content-factory/content-factory-vault/processes/video-station|processes/video-station]] («Трек B» + «Инфографика-плашки над
головой»); код — `video-pipeline/`.

## Контракт I/O

- **Вход:** разговорное видео (raw HLG) · тезисы для плашек (Скандар: какие мысли) · бриф на текст.
- **Выход:** `<slug>.mp4` (сжат, сабы, инфографика) · `<slug>-cover.jpg` · `post.md` (подпись ≤5 тегов).
  Имя — **по контексту видео** (slug бандла), не фиксированное.
- **Маршрут (Денни routing):** вход разговорный × цель IG `@skandar1104` → этот content-type.

## DAG (◆ = код-гейт)

```
ВХОД:  raw-видео (HLG)  +  тезисы для плашек (Скандар)  +  бриф на текст
   │
[prep] transcribe(raw) ─────────────→ words.json
   │
   ├──────────── ПАРАЛЛЕЛЬНО сразу после transcribe ────────────┐
   │         │            │                 │                    │
 [audio]  [subs]      [cover]         [text-meta]        [visual] ▼ (ждёт тезисы Скандара)
 clean+   gen_subs    cover(frame)    draft caption      ┌ render_plates ─┐
 stereo   (words)     тонмап          +теги (бриф)       ├ head_track(win)┤→ contrast ◆
 ◆−16/L=R └→subs.ass  └→cover.jpg     └→post-draft       └────────────────┘   └─x/y─┐
 └→voice                              (Скандар финал)                              │
      └───────────┴───────────────────────┬──────────────────────────────────────┘
                                           ▼
                          [assembly] build  ← БАРЬЕР (нужны visual x/y + subs + audio)
                          ◆ тонмап ПЕРВЫМ → плашки(x/y) → сабы → фейды
                                           ▼
                          [export] ◆ стерео / −16 LUFS / crf22+maxrate
                                           ▼
                          [qa] gates: длительность · L/R RMS равны · контраст-floor
                                           ▼
                          [review] show-then-fix (пост · название кавера · текст инфографики)
                                           ▼
ВЫХОД:  <slug>.mp4  +  <slug>-cover.jpg  +  post.md (≤5 тегов)   →  status: ready
```

## Стримы по шагам

1. **prep · transcribe** (mlx-whisper, word-timestamps) → `words.json`. [авто]
2. **[Скандар] тезисы** — какие мысли → плашки + грубые окна (нужен `words.json`). [ручное; черновик
   plate-copy агента → финал Скандар]
3. **visual · head_track** (`head_track.py`: MediaPipe Tasks IMAGE, crown + ярчайший кадр окна) →
   `win_measures.json`. [авто] ∥ ш.4
4. **visual · render_plates** (`plate.py`, стиль maksi, accent `#5f9bff` под энкод) → PNG.
   **◆ рендерер-общий.** [авто] ∥ ш.3
5. **visual · contrast** (`contrast.py`) → placement x/y + pass/fail. **◆ контраст-структурный**;
   x/y **идёт в build** (wired, не руками). [авто]
6. **subs** (`subs.py`, сырой режим `cuts=None` → тайминги прямо из words.json; MarginV нижняя треть,
   не пересекать плашки) → `subs.ass`. [авто] ∥ visual
7. **audio** (`clean.py`, профиль «шумная улица/селфи»: петличка → highpass → arnndn → afftdn →
   loudnorm) → стерео-мастер. **◆ аудио-экспорт-стерео.** [авто] ∥ visual/subs
8. **cover** (`cover.py`, тонмап HLG→SDR + плашка в грид-safe зоне) → `<slug>-cover.jpg`.
   [авто; название — черновик → Скандар] ∥ всё
9. **text-meta** (субагент) → каркас подписи + честные **≤5 тегов**. [черновик → Скандар] ∥ всё
10. **assembly · build** (`talking_head.py`): **◆ тонмап первым** → плашки (x/y из ш.5) → сабы →
    фейды. **БАРЬЕР** (нужны 5 + 6 + 7). [авто]
11. **export** **◆ стерео / −16 LUFS / TP −1 + crf22 + maxrate**. [авто]
12. **qa** гейты: длительность (рассинхрон concat — тихий брак) · L/R RMS равны · контраст-floor. [авто]
13. **review-чекпоинт (show-then-fix):** показать Скандару рил + кавер + подпись; правки по 3
    контентным выходам → пере-гон только дешёвых задетых шагов → `status: ready`.
14. **record** — Денни пишет `run.md` в бандл по [[content-factory/content-factory-vault/pipelines/method/run-schema|method/run-schema]] (гейты, residual правок
    чекпоинта, грабли, дельты) + строка в [[content-factory/content-factory-vault/pipelines/runs/README|runs/README]]. Без записи прогон ничему не учит. [Денни]

## Ручное / авто (сводка)

- **Авто:** 1, 3, 4, 5, 6, 7, 8, 10, 11, 12.
- **Ручное (Скандар):** тезисы (2) · выбор кадров/дублей · музыка · финал 3 контентных выходов.
- **Show-then-fix:** пост · название кавера · текст инфографики (13).

## Субагенты

Денни (orchestrator) + **text-meta** (9, параллельно) + опц. **plate-copy** (2) + опц. **verify/QA**
(12–13). Остальное — скрипты (параллельные subprocess, не LLM).

## Бандл

`~/vlad/danny-content/posts/YYYY-MM-DD-<slug>/` по [[content-factory/content-factory-vault/content-bundle-spec|content-bundle-spec]]:
`post.md` (source, подпись одним блоком) · `<slug>.mp4` · `<slug>-cover.jpg` · `work/`
(воспроизводимость: скрипты + промежуточные) · `run.md` (run-данные по [[content-factory/content-factory-vault/pipelines/method/run-schema|method/run-schema]]).
Статус `draft → ready → posted`; постинг — по команде Скандара.

---

See also: [[content-factory/content-factory-vault/pipelines/method/streams|method/streams]] · [[content-factory/content-factory-vault/processes/video-station|processes/video-station]] · [[content-factory/content-factory-vault/content-bundle-spec|content-bundle-spec]].

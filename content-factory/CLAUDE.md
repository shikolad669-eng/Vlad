# content-factory — цех контент-производства (door)

You are in `~/vlad/content-factory/` — **завод = цех**: процессы создания
контента (как делаем видео, как делаем дизайн), станки, приём сырья (intake) и
автопостинг.

Цех — **не витрина**: смыслом, голосом и routing владеет витрина
(`~/vlad/danny-content/` — Денни, личный бренд). Цех — подрядчик: бриф/сырьё на
входе, ассет в бандл витрины на выходе. Единый стандарт контент-единицы —
`content-factory-vault/content-bundle-spec.md`.

A domain peer to `music` and `study`; born 2026-07-10 as a **mirror of
Skandar's `~/maksi-content-factory/`** (его машина): vault скопирован целиком —
процессы, станки-канон, позиционирование венчура. **Канон живого венчура — у
Скандара**; расхождения снимаются на синк-сессиях. Ссылки на `~/maksi-studio/…`
и `~/skandar-academy/…` внутри vault — внешние указатели в его неймспейс.

Имя агента этого уровня — **Завод** (реестр имён:
`~/vlad/vlad-vault/glossary.md` → «Имена агентов»). Агент завода — мета-уровень
автоматизации конвейера: улучшает и крутит процессы, голоса не имеет, в витрины
не пишет.

> **Invariant (all levels):** NEVER `AskUserQuestion` / popup choice dialogs —
> questions always in plain text.

Read first (the brain is the vault):
- `content-factory-vault/HOME.md` — map of the knowledge.
- `content-factory-vault/status.md` — current state, read every session.
- `content-factory-vault/principles.md` — conventions (base + deltas).

## Stage

**Mirror born 2026-07-10.** Знание завода скопировано; код станков
(`video-pipeline/`) и TG-инструменты **не** перенесены (решение 2026-07-10:
«не всё сразу») — заберутся при первом реальном прогоне. См. status.

## Inside

- `content-factory-vault/` — the knowledge base (see HOME).
- `intake/` — приём сырья: `inbox/` (сброс) → `raw/` (записи Влада, primary) +
  `gen/` (ИИ-генерации, derived) + `ref/` (чужие референсы, study-only).
  Содержимое вне git. См. `intake/README.md`.
- (pipeline code / tools будут добавлены как проекты, каждый со своим CLAUDE.md.)

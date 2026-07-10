---
type: reference
status: active
sensitivity: normal
scope: all
axis: vault
date: 2026-07-10
updated: 2026-07-10
tags: [danny-content, publishing, platforms, format, markdown]
related:
  - HOME
  - routing-table
  - ../vlad-life/HOME.md
---

# Publishing model — hub-and-spoke

How a finished piece reaches platforms. Метод унаследован из базы Скандара
(его решение 2026-06-26); набор каналов Влада — открыт, заполняется в
`../vlad-vault/surfaces.md`.

## The principle — one source, many renders

**Markdown is the canonical source of truth; every platform is a disposable
render.** Same philosophy as the namespace itself (data primary,
engine/format disposable). Do **not** try to "unify into one format that works
everywhere" — that is the lowest-common-denominator trap. Instead: one MD →
adapt per platform, each getting the format **and the role** that fits it.

## The spokes (hub-and-spoke, not a mesh)

| Channel | Role | Format |
|---|---|---|
| **Canonical source** | truth, archive | **Markdown** (lives here in `danny-content/`) |
| _(каналы Влада)_ | — | заводятся строкой в `../vlad-vault/surfaces.md`, затем сюда |

Известно на старте: TG-канал «Vlad music» (`t.me/htopnot`) — статус to-verify
в реестре поверхностей. Музыкальные площадки (стриминги) — отдельный род
поверхности, решается при первом релизе.

## The manual pipeline (no automation yet)

1. Finish **one canonical MD** here in `danny-content/`.
2. The agent emits **ready-to-paste variants** per platform. Reformatting is
   the cheap part the tool does — the human only pastes.
3. Paste manually.

Automation (bot poster, auto-fan-out) is **deferred** — это роль завода
(`../content-factory/`), заработает когда дойдут руки; TG-инструменты не
перенесены (решение 2026-07-10).

## Content bank (recycle source)

Content is **not** the bottleneck. Recycle from:

- `../vlad-life/texts/` — свои тексты и песни, `trust: primary`.
- `drafts/` — заготовки.
- `../music/` — материал музыкального домена (треки, истории записей,
  выступления).

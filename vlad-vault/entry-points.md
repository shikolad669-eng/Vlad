---
type: reference
status: active
sensitivity: normal
scope: all
axis: vault
updated: 2026-07-25
tags: [entry-points, navigation, map, claude-md, home-md, convention, namespace]
related:
  - HOME
  - principles
  - vault-template
  - ../CLAUDE.md
---

# Entry-point map — двери и карты неймспейса

Навигация сверху вниз: с уровня `vlad` пройти к двери любого домена.

## Канон (в голове держать так)

**`CLAUDE.md` = дверь. `HOME.md` = карта. Цепочка: `CLAUDE.md → HOME.md → знание`.**

- **Дверь.** Харнесс **авто-грузит** её из cwd вверх по родителям. Обязательна в
  каждой папке-cwd: корень домена + каждый код-репо. Тонкая, стабильная: «где ты,
  как действовать, что читать первым». Имя зависит от харнесса: `CLAUDE.md`
  (Claude Code) / `AGENTS.md` (Codex) — папка под несколько тулов несёт оба как
  синхронные твины.
- **`HOME.md` — карта.** Харнесс её **не грузит** — на неё указывает дверь. Одна
  на корень vault. Семантическая навигация по темам.
- **`README.md` — человеку.** Опционально. Никогда не несёт нагрузку для агента —
  маршрутизация в нём = баг (прецедент базы: «cosmomap door bug»).
- **`status.md` / `principles.md`** — не входы, но дверь/карта должны на них
  указывать в project-vault (горячее состояние + правила).
- **Проекция (`danny-content/`, `public/`)** — дверь + карта есть, **vault нет**:
  не источник, а выход. Отсутствие `-vault/` = признак проекции ([[vlad-vault/glossary|glossary]]).

Легенда: `[door]` CLAUDE.md · `[map]` HOME.md · `[hot]` status.md ·
`[rules]` principles.md · `[human]` README.md · ✓ ок · ✗ пробел

## Карта

```
~/vlad/  ◄══ верхний уровень (один репозиторий)
├─ CLAUDE.md                       [door] ✓  карта неймспейса
├─ vlad-vault/HOME.md              [map]  ✓  + principles [rules] ✓ + preferences ✓
│                                            + vault-template ✓ (база-баз) + entry-points (этот файл)
├─ vlad-life/CLAUDE.md             [door] ✓  + HOME.md [map] ✓ + principles ✓   (primary; дневник вне git)
├─ music/CLAUDE.md                 [door] ✓
│   └─ music-vault/HOME.md         [map]  ✓  + status ✓ + principles ✓
├─ study/CLAUDE.md                 [door] ✓
│   └─ study-vault/HOME.md         [map]  ✓  + status ✓ + principles ✓
├─ drafting/CLAUDE.md              [door] ✓  (+ cad/ тяжёлые файлы, вне git)
│   └─ drafting-vault/HOME.md      [map]  ✓  + status ✓ + principles ✓
├─ phyto/CLAUDE.md                 [door] ✓  (бизнес: опт фитопродукции, LLM-вики)
│   └─ phyto-vault/HOME.md         [map]  ✓  + status ✓ + principles ✓ + sources ✓ + catalog/
├─ discord-custom/CLAUDE.md        [door] ✓  (бизнес; + assets/ вне git)
│   └─ discord-custom-vault/HOME.md [map] ✓  + status ✓ + principles ✓ + clients/ + positioning
├─ content-factory/CLAUDE.md       [door] ✓  (цех; зеркало завода Скандара)
│   └─ content-factory-vault/HOME.md [map] ✓ + status ✓ + principles ✓
├─ danny-content/CLAUDE.md         [door] ✓  + HOME.md [map] ✓   (проекция, агент Денни)
├─ public/CLAUDE.md                [door] ✓  + HOME.md [map] ✓   (проекция, безагентная)
├─ documents/                      [human]    README (приёмник, вне git)
└─ secrets/                        [human]    README (вне git; NEVER commit)
```

## Реестр приведения к канону

- [x] 2026-07-10 — неймспейс рождён по `vault-template` целиком (все двери и
  карты созданы одним прогоном; зеркало структуры неймспейса Скандара).
- [x] 2026-07-10 — добавлен домен `drafting/` (чертежи) по `vault-template`:
  дверь + vault (дельта: `market/` дропнут, зона `drawings/`, тяжёлые файлы в
  `cad/` вне git). Зеркало на стороне Скандара — при синхронизации.
- [x] 2026-07-20 — добавлен домен `discord-custom/` (бизнес: заказная
  кастомизация Discord) по `vault-template`: дверь + vault (дельта: клиентский
  бизнес → зоны `clients/` + `positioning.md`; тяжёлая графика в `assets/` вне
  git). Зеркало на стороне Скандара — при синхронизации, если он заведёт его.
- [x] 2026-07-24 — добавлен домен `phyto/` (бизнес: оптовая фитопродукция) по
  `vault-template`: дверь + vault (дельта: `catalog/` — датированный снимок
  витрины; `lessons/` вместо `drawings/`). Внесён в мета-карту 2026-07-25.
- [ ] `Влад бизнес` (ИИ-агенты для бизнеса + клиентские базы Караганды) — вне
  неймспейса, дверей и карт нет. Завести доменом по `vault-template`.
  Инвентарь: [[vlad-vault/meta-map|meta-map]] → «Вне карты».
- [ ] `AGENTS.md`-твины дверей — не созданы; завести, если появится второй
  харнесс (Codex и т.п.).

## Почему это и есть учебный пример

«Дверь, которую видит машина» (`CLAUDE.md` авто-грузится) vs «карта, на которую
указывают» (`HOME.md`) — разница между **системой** (агент входит холодным и
сразу знает, что делать) и **разговором** (агент гадает).

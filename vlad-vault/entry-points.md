---
type: reference
status: active
sensitivity: normal
scope: all
axis: vault
updated: 2026-07-10
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
  не источник, а выход. Отсутствие `-vault/` = признак проекции ([[glossary]]).

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
- [ ] `AGENTS.md`-твины дверей — не созданы; завести, если появится второй
  харнесс (Codex и т.п.).

## Почему это и есть учебный пример

«Дверь, которую видит машина» (`CLAUDE.md` авто-грузится) vs «карта, на которую
указывают» (`HOME.md`) — разница между **системой** (агент входит холодным и
сразу знает, что делать) и **разговором** (агент гадает).

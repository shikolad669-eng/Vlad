---
title: Secrets map — где живут доступы (без значений)
updated: 2026-07-10
type: reference
status: active
sensitivity: normal
scope: all
tags: [secrets, security, access]
---

# Secrets map

Указатели, **без значений**. Машина доверенная → секреты plain md, но
NEVER sync / NEVER commit / NEVER index. Контракт: `~/vlad/secrets/README.md`.

## Глобальный личный уровень — `~/vlad/secrets/`

Доступы, которыми владеет Влад (не проект). Вне git через `.gitignore`
(+ рекомендован глобальный excludesfile).

- _(пусто — файлы появляются по мере надобности: passwords.md, tokens.md)_

## Per-project уровень

Доступы проекта — в его `.env` / `.secrets/`, никогда в трекаемых файлах.

- _(пусто — появятся с первыми код-проектами)_

## Защита

- `.gitignore` корня: `secrets/*`, `*.env`, `*.key`, `id_*`.
- Рекомендация: глобальный git excludesfile `~/.config/git/ignore`
  (`core.excludesfile`) с теми же паттернами — защита в любом будущем репо.

## Долги

_(пусто)_

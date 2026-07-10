---
title: Meta-map — обзорная карта неймспейса одной страницей
type: reference
status: active
sensitivity: normal
scope: all
date: 2026-07-10
updated: 2026-07-10
tags: [meta-map, namespace, agents, projections, audit]
related:
  - HOME
  - ../CLAUDE.md
  - glossary
  - entry-points
  - surfaces
---

# Meta-map — обзорная карта неймспейса

Одна страница «всё сразу»: уровни, агенты, проекции. **Не канон**: при
расхождении правы `../CLAUDE.md`, [[vlad-vault/glossary|glossary]], decisions. Горячие статусы здесь
не живут — они в `status.md` доменов. Обновлять при изменении структуры;
аудит-снимки датировать внизу.

## Схема

```
~/vlad — верхний уровень · top-оркестратор (мета · навигатор · диспатч; пишет вниз во все уровни)
├─ vlad-vault       meta-vault: канон, решения, glossary, surfaces, people, edges
├─ danny-content    проекция «личный бренд», агент Денни (read все домены, write поверхности)
├─ public           проекция «наружу», безагентная (артефакты строятся в доменах)
├─ documents/       приёмник документов (вне git)
└─ secrets/         доступы (вне git)

личное (primary)                       работа (свой scope + свой агент)
vlad-life   primary  дневник/тексты    music            (без имени)  + media/ вне git
                                       study            (без имени)
                                       content-factory  Завод  (цех, не витрина)

потоки:
intake (цех) ─станки─► Денни ─бандлы по bundle-spec─► поверхности   (реестр: surfaces.md)
музыка (media/) ─материал─► danny-content ─► поверхности
```

## Домены

| Домен | Роль | trust | Агент | Дверь |
|---|---|---|---|---|
| `~/vlad/vlad-vault` | meta-vault: знание о неймспейсе | — | — | `HOME.md` |
| `~/vlad/vlad-life` | живой первоисточник | primary | — (источник, не проект) | `CLAUDE.md` |
| `~/vlad/music` | музыка: треки, выступления, релизы | work | без имени | `CLAUDE.md` |
| `~/vlad/study` | учёба | work | без имени | `CLAUDE.md` |
| `~/vlad/content-factory` | цех: процессы, станки, intake | work | Завод | `CLAUDE.md` |
| `~/vlad/danny-content` | проекция «личный бренд» | projection | Денни | `CLAUDE.md` |
| `~/vlad/public` | проекция «наружу» | projection | — | `CLAUDE.md` |

## Роды агентов

- **Оркестратор** (без имени) — governance/навигатор/диспатч, продукт не
  производит; cwd `~/vlad/`.
- **Уровневые** (Завод; music/study без имён) — исходная работа в домене;
  cwd = домен.
- **Проекции** (Денни) — read поперёк, write только на поверхности.
- **Рекордер** (чат-Клод) — пишет primary под диктовку в `vlad-life/diary/`;
  устав: [[vlad-vault/recorder-charter|recorder-charter]].

## Вне карты (на машине, но не в неймспейсе)

_(пусто — заполняется по факту: что живёт на машине Влада вне `~/vlad/`)_

## Аудит-снимки

- **2026-07-10** — рождение неймспейса: структура-зеркало неймспейса Скандара
  (метод скопирован, история нет; TG-инструменты и RAG-движок отложены).

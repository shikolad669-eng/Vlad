---
type: reference
status: active
sensitivity: normal
scope: all
tags: [home, index, vault, map]
updated: 2026-07-25
---

# vlad-vault

meta-vault верхнего level'а: vault *о самом неймспейсе* — связи **вниз** ко всем
доменам. Семантическая карта — начинать отсюда. Конвенции — [[vlad-vault/principles|principles]].
Растёт по мере надобности, один файл = один объект.

> Карта неймспейса и роли — `../CLAUDE.md`. Структура рождена 2026-07-10 как
> зеркало неймспейса Скандара (идентичная структура — условие частого синка).

---

## Домены (связи вниз)

Личное (`trust` указан):

- **`../vlad-life/`** — живой первоисточник: дневник, тексты. `primary`.
  Содержимое дневника вне git.

Работа (домены-пиры):

- **`../music/`** — музыка: треки, демки, выступления, релизы. Дверь + `music-vault/`
  + `media/` (файлы вне git).
- **`../study/`** — учёба. Дверь + `study-vault/`.
- **`../drafting/`** — чертежи: детали, узлы, спеки. Дверь + `drafting-vault/`
  + `cad/` (тяжёлые DWG/STEP/PDF вне git).
- **`../phyto/`** — **бизнес**: оптовая фитопродукция, эксклюзивная дистрибуция
  трав Гордеева по РК. Дверь + `phyto-vault/` (LLM-вики: `systems/`, `market/`,
  `catalog/`). Канон домена живёт здесь — `phyto-sale` лишь выгрузка
  ([[vlad-vault/meta-map|meta-map]] → «Вне карты»).
- **`../discord-custom/`** — **бизнес**: заказная кастомизация Discord. Дверь +
  `discord-custom-vault/` (`clients/`, `positioning.md`) + `assets/` вне git.
- **`../ai-agents/`** — **бизнес**: ИИ-агенты для бизнеса под ключ (внедрение +
  подписка). Дверь + `ai-agents-vault/` (`systems/`, `clients/`, `market/leads/`
  — 80 лидов Караганды, `tools/llm/` — LLM-вики). Домен рождён 2026-07-27
  слиянием волта «Влад бизнес» в неймспейс.
- **`../content-factory/`** — **цех** контента (агент Завод): процессы, станки,
  intake сырья, автопостинг. Зеркало завода Скандара; канон живого венчура — у него.

Проекции (выходы поперёк доменов):

- **`../danny-content/`** — личный бренд (агент **Денни** — исполнитель полного
  цикла). Карта: `../danny-content/HOME.md`. Канон поверхностей: [[vlad-vault/surfaces|surfaces]].
- **`../public/`** — внешние готовые артефакты. Карта: `../public/HOME.md`.

## Corpora

- [[vlad-vault/corpora/README|corpora/]] — зарезервировано: заметки о корпусах появятся,
  когда подключится движок (RAG отложен).

## Tech (cross-project memory)

- [[vlad-vault/tech/README|tech/]] — tech-профили проектов (стек, архитектура,
  переиспользуемые блоки). Пусто — появятся с первыми проектами.

## Agentics (метод агентской разработки)

- [[vlad-vault/agentics/README|agentics/]] — метод + прогоны. Канон метода живёт у Скандара
  (`~/skandar/skandar-vault/agentics/` — referenced, not copied); здесь копятся
  прогоны и ретро этого неймспейса.
- [[vlad-vault/workflow-streams|workflow-streams]] — **горизонтальная ось воркфлоу**: streams + мета-слой.
  Термины — [[vlad-vault/glossary|glossary]] (читать первым).

## Decisions

- [[vlad-vault/decisions/README|decisions/]] — датированные прецеденты `YYYY-MM-DD-*`.
  Пусто — первое решение уровня запишется сюда.

## Backlog + inbox (задачи: кратко на мете, решаются ниже)

- [[vlad-vault/inbox/README|inbox/]] — одна дверь захвата: кидай что угодно, zero ceremony.
- [[vlad-vault/backlog|Backlog]] — **реестр**: все живые пункты одной строкой (суть ·
  исполнитель · указатель вниз).
- [[vlad-vault/backlog-review-protocol|Review-протокол]] — «сессия: бэклог»: разбор inbox →
  проход реестра → свод.

## Plans

- [[vlad-vault/plans/README|plans/]] — полка стратегических сборок (не календарные
  обязательства; обязательства ведёт [[vlad-vault/backlog|backlog]] — правило унаследовано из базы).

## Ideas (будущие улучшения, открытые вопросы)

- [[vlad-vault/ideas/README|ideas/]] — forward-looking предложения мета-уровня, отдельно от
  устоявшихся decisions. Пусто.

## For Vlad (личный уровень развития)

- [[vlad-vault/for-vlad/README|for-vlad/]] — новые слова/концепты для расширения семантики
  Влада как пользователя-человека. Агент кладёт сам или по просьбе; разбирает
  Влад выделенной сессией.

## People

- [[vlad-vault/people/README|people/]] — реестр идентичностей: карточка на человека из ≥2
  доменов. Пусто.

## Meta

- [[vlad-vault/meta-map|Meta-map]] — обзорная карта неймспейса одной страницей.
- [[vlad-vault/glossary|Glossary]] — канон терминов: две оси (level vs stream/flow) + RU-алиасы.
- [[vlad-vault/field-radar|Field radar]] — реестр внешних источников (статьи/репо/референсы).
- [[vlad-vault/meta-philosophy/README|Meta-philosophy]] — зона методологии мышления
  (мета-мета). Пусто — родится из первых мета-сессий.
- [[vlad-vault/vault-template|Vault template]] — база-баз: «папка = точка входа», контракт
  дверь/карта, скелет project-vault. Новые домены рождаются отсюда.
- [[vlad-vault/entry-points|Entry-point map]] — двери (`CLAUDE.md`) и карты (`HOME.md`)
  всего неймспейса.
- [[vlad-vault/schema/README|Schema]] — machine-facing контракты frontmatter.
- [[vlad-vault/edges/index|Edges]] — долговечные кросс-доменные связи.
- [[vlad-vault/preferences|Preferences]] — принципы уровня vlad (оркестратор) + инвариант.
- [[vlad-vault/recorder-charter|Recorder charter]] — устав рекордера (чат-Клод → дневник).
- [[vlad-vault/secrets-map|Secrets map]] — где живут доступы (без значений).
- [[vlad-vault/surfaces|Surfaces]] — реестр поверхностей (каналы наружу).
- [[vlad-vault/principles|Principles]] — правила vault'а.

---

См. также: карта неймспейса `../CLAUDE.md`.

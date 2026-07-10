---
type: reference
status: active
sensitivity: normal
scope: all
updated: 2026-07-07
tags: [glossary, terminology, agentics, vault, axes, harness]
axis: cross
---

# Glossary — keep the two axes apart

One word = one concept. The two axes were historically both called "уровни/слои";
this file is the single source of truth that keeps them distinct.

## The two axes (+ two auxiliary vocabularies)

- **Vault axis (vertical)** — where knowledge lives + ownership/trust (namespace). Term: **level**.
- **Agentic axis (horizontal)** — how work flows through phases of responsibility. Terms:
  **stream / flow / meta-layer / orchestrator**.

Three more vocabularies sit beside the axes; they must NOT reuse "level/layer" either:
- **zone** — knowledge-curation tiers (canon / precedent / journal / lessons).
- **engine** — the retrieval/RAG substrate (`memory-layer`).
- **harness** — the runtime client that executes agents (Claude Code / Codex / chat-Claude / SDK):
  loads doors by cwd, supplies tools, skills, permissions, memory. Replaceable; data must outlive it.

Five non-overlapping vocabularies total. "layer" is reserved for **meta-layer** only.

## Three evaluation axes of one object (do not conflate)

Any object is rated on three independent axes; «высокий» on one says nothing
about the others:

- **trust** — кто написал/проверил: `primary` / `derived`. Ось доверия.
- **важность** — место в смысловой иерархии: derived по trust может быть
  смысловым верхом неймспейса (правило унаследовано из базы Скандара).
- **публичность** — surface/sensitivity: приватный корень ↔ публичная крона.

## Terms

| Term | Axis | Definition | Do NOT call it |
|---|---|---|---|
| **level** | vault | A tier of the namespace/trust hierarchy: `vlad` on top, domains below, `trust: primary/derived`. Answers *where knowledge lives & who owns it*. | layer, stream, stage |
| **vault** | vault | The curated wiki-map folder of one domain (`<domain>-vault`). Container, one per domain. By genre it is an LLM-**wiki** (hand-curated, navigable), not a RAG corpus. **English only — never transliterate/decline** (see RU aliases). | engine, corpus, level, ~~волт~~/~~вольт~~ |
| **meta-vault** | vault | The single cross-domain vault at the top level (`vlad-vault`): content is *about the namespace itself* — domain tech-profiles, cross-domain agentics, down-links to every domain. "meta" in the precise reflexive sense (a plane over all domains), the vault-axis twin of **meta-layer**. | super-vault, level, корневой (those name only hierarchy, not the *about-the-whole* function) |
| **проекция (projection)** | vault | A cross-domain **output**: draws on many levels, owns no source, lives at the super-vault level with its **own door**, writes **outward** to surfaces (`danny-content`→IG/TG, `public`→decks/sites). The outward element of the vault axis — *level* points in (source), *projection* points out (published). Has **no `-vault/`** (owns no curated knowledge): door + map + specs + output. Produced by the **projection-agent** role. See `decisions/2026-06-30-agent-architecture`. | level (source), meta-vault (about-the-whole, *inward*), surface (the channel, not the projection), vault (a projection has none) |
| **stream** | agentic | A structural lane of responsibility (design, build, deploy, QA…). Persistent, parallel-capable, can split / merge / be optional. Replaces "department". Answers *where in the conveyor*. | level, department, layer |
| **flow** | agentic | The trajectory of **one** work-item (one feature) through the streams. Transient, per-item. One stream serves many flows. Answers *how an item moves*. | stream (it is not the lane) |
| **meta-layer** | agentic | The supervisory layer **above** the streams. Improves the *workflow itself* (context-splitting, parallelism, retrieval requirements) across many runs — not the product. The only legal use of "layer". | orchestrator |
| **orchestrator** | agentic | The conductor that drives the streams to ship **one product**. Lives inside the product axis. Cares about output quality, not the conveyor. | meta-layer |
| **engine (движок)** | — | The retrieval/RAG substrate (`memory-layer`: Chroma, hybrid search). Namespace-wide infrastructure, versioned in git, no trust label. Meta states the *demand*; the engine *supplies*. | meta-layer, stream |
| **zone** | knowledge | A curation tier of the knowledge base, each with its own semantics: **canon / precedent / journal / lessons**. Maps to folders. Answers *how distilled / how trusted a piece of knowledge is*. | layer, level |
| **harness (харнесс)** | — | The runtime client executing an agent session: resolves cwd → auto-loads the door chain (`CLAUDE.md` up the parents), supplies tools / permissions / skills / auto-memory; enforces its own safety gates (autonomy edge in run-data). Interchangeable & disposable: Claude Code, Codex (door = `AGENTS.md`), chat-Claude (recorder lives there), Agent SDK. `~/.claude/` is harness **cache**, not truth; data must survive any harness (LLM-independence). The **agent** is the charter/role (markdown); the harness *executes* it; the **engine** retrieves. Door contract: [[vlad-vault/entry-points|entry-points]], [[vlad-vault/vault-template|vault-template]]; cwd-model: `~/skandar/skandar-vault/decisions/2026-06-30-agent-architecture.md`. | agent, engine, model, level |

## `meta-` is a cross-axis prefix (not reserved)

Only the noun **`layer`** is reserved (→ `meta-layer` only), so tiers/lanes never get called
"layer". The qualifier **`meta-`** is *not* reserved: it means "the spanning, about-the-whole-field
element of its axis." Same meaning, applied per axis:

- agentic axis → **meta-layer** (a plane over all streams: improves the workflow itself)
- vault axis → **meta-vault** (a vault over all domains: knowledge about the namespace itself)

Never write bare `meta` as a term — always `meta-layer` or `meta-vault`, so the axis is explicit.
`super-vault` (English only) names hierarchy ("on top"); **meta-vault** names
the function ("about the whole"), which is the property that actually distinguishes `vlad-vault`.

## Why these words (geometry)

The shape of each word matches the shape of the thing — and explains why "layer" is reserved:

- **stream** = a *lane* — one of many vertical tracks. Local, structural.
- **flow** = a *line* — the trajectory of one item. Single.
- **level** = a *tier* of the vault hierarchy. Local to a domain.
- **meta-layer** = a *plane laid over and across all streams and all flows at once*. **Global.**
- **projection** = a *casting* of many domains onto an external surface — a shadow/map of the whole, **outside** the vault. (Direction, not span: *level* faces in, *projection* faces out.)

"layer" is the only term with **spanning, global** semantics — a plane over the whole field, not a
lane or a line. That is exactly why it is reserved for the meta and nothing else: the meta is the
one thing that covers everything below.

## Anchor sentence

> **Levels** — where knowledge lives (vault). **Stream** — a lane of work (structure, *where*).
> **Flow** — one feature's path through streams (*how it moves*). **Meta-layer** — what improves
> the conveyor. **Orchestrator** — who conducts streams to ship the product.

## Имена агентов (по уровням)

Короткие имена, чтобы ссылаться на агентов уровней в разговоре и файлах.
Имя = агент уровня, не сам уровень. Рабочие имена унаследованы из неймспейса
Скандара (2026-07-10): совпадающие роли зовутся одинаково, чтобы при синке двух
неймспейсов не переводить термины.

| Имя | Уровень | Статус имени |
|---|---|---|
| *(без имени)* | `~/vlad/` — top-оркестратор (мета-уровень) | не присвоено (2026-07-10) |
| **Денни** | `~/vlad/danny-content/` — личный агент-исполнитель контента, пишет только за Влада; имя в честь Danny Worsnop | рабочее, унаследовано 2026-07-10 |
| **Завод** | `~/vlad/content-factory/` — цех: процессы/станки/intake/автопостинг | рабочее, унаследовано 2026-07-10 |
| *(без имени)* | `~/vlad/music/` | не присвоено |
| *(без имени)* | `~/vlad/study/` | не присвоено |

## RU aliases (canonical English on the left)

The owner may write the term in Russian / transliterated; it maps 1:1 to the English canon:

- `уровень` → **level**
- **vault / meta-vault / super-vault — English only.** Не транслитерировать и не склонять:
  пиши `vault` как несклоняемое боррослово («в vault», «конвенции vault», «по всем vault»).
  Ретайрнуто: ~~волт~~ / ~~вольт~~ / ~~мета-волт~~ / ~~суперволт~~ (читается как «вольт» = напряжение). Правило 2026-07-06.
- `вики` → **wiki** (жанр vault; не контейнер)
- `стрим` → **stream**
- `флоу` → **flow**
- `метаслой` / `мета-слой` → **meta-layer**
- `оркестратор` → **orchestrator**
- `движок` → **engine**
- `зона` → **zone**
- `проекция` → **projection**
- `харнесс` → **harness** (склоняется свободно; это НЕ агент и НЕ движок)

⚠️ **Do NOT use «поток» as a term** — in Russian it means *both* stream and flow, so it is
ambiguous. Always write the transliteration: `стрим` (stream) or `флоу` (flow).

## Spelling / pitfalls

- «поток» is ambiguous in Russian (= stream *and* flow) — never use it as a term; write `стрим` / `флоу`.
- English `stream` (not "steam" = пар).
- the noun "layer" is reserved for **meta-layer** only. The prefix "meta-" is NOT reserved —
  it is cross-axis (`meta-layer` agentic, `meta-vault` vault). Never write bare "meta" as a term.
- "вики" (genre: hand-curated LLM-wiki) ≠ **vault** (container folder) ≠ "корпус"/engine (RAG substrate).
- retired: «супер-вики» / «суперволт» as the name for `vlad-vault` → use **meta-vault**.
- retired transliteration: `волт` / `вольт` / `мета-волт` → always English **vault** / **meta-vault** (indeclinable). «вольт» reads as voltage.
- Drop "semantic" from "semantic levels" — it differentiates nothing.

See also: [[vlad-vault/workflow-streams|workflow-streams]] (the model + how the axes connect).

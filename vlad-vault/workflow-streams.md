---
type: model
status: active
sensitivity: normal
scope: all
created: 2026-06-04
updated: 2026-06-07
tags: [workflow, streams, meta, agentics, method, glossary, terminology]
axis: cross
note: >
  Graduated from seed (2026-06-04). Was recorded mid-flight closing cosmomap Experiment 3;
  developed in a dedicated skandar session into the model + glossary below. The terminology
  collision flagged in the seed is resolved here (level / stream / flow / meta-layer).
---

# Streams, the meta-layer, and how they relate to vault levels

Two **orthogonal axes** that were both historically called "уровни/слои". This file is the
canon that keeps them distinct and records how they connect.

- **Vault axis (vertical) — *levels*.** Namespace / trust hierarchy: `skandar` on top, domains
  below, `trust: primary/derived`. About **where knowledge lives and who owns it.** Canon:
  `decisions/2026-06-02-namespace-systematization`, map: `../CLAUDE.md`.
- **Agentic axis (horizontal) — *streams + meta-layer*.** How work flows through phases of
  responsibility. About **how work gets done.** This file.

## Glossary

The canonical term definitions live in their own object → **[[vlad-vault/glossary|glossary]]** (level / stream / flow /
meta-layer / orchestrator / engine, with RU aliases). Read it first; this file uses those terms.

**Stream vs flow** are perpendicular, not two sizes of one thing. A stream is a lane (container,
long-lived, *where*); a flow is one item's trajectory through lanes (transient, *how it moves*).
**One stream serves many flows** over time. "stream бигger / flow smaller" only in the
container-vs-item sense.

## The model

Work moves left→right through **sequential streams**, with a **meta-layer above** that watches them
across runs and continuously improves them.

```
        ┌─────────────────────────────────────────────────────────┐
 META-  │  analyses the WORKFLOW itself (not the product) — how to   │   ← improves the machinery
 LAYER  │  split context between agents, where to parallelise,       │     across many runs
        │  what retrieval the streams need. Cares 0 about the product│
        └─────────────────────────────────────────────────────────┘
                 ▲ reads run-data                   ▲ reads run-data
        ┌──────────────────────┐        ┌──────────────────────────┐
        │  STREAM: projection   │  ───►  │  STREAM: implementation   │   ← streams (configurable;
        │  & design (manual)    │  hand- │  & deploy (agentic)       │     at least these two)
        └──────────────────────┘  off   └──────────────────────────┘
              ▲ orchestrator conducts the streams to ship ONE product ▲
```

**The stream set is configurable**, not fixed. Examples of valid shapes:
- merge implementation+deploy (current default), **or** split deploy into its own stream;
- add a QA / business-review stream, **or** skip it;
- projection vs design as one stream or two; a research/spike stream when warranted.

Which shape a project uses depends on its profile (risk, prod-edge, multi-repo…). See
"Who chooses the stream shape" below.

- **Stream — projection & design (проектирование и дизайн).** Manual / human ("vibecoder"):
  decide *what* to build and *why*. Output = the product spec, acceptance oracles, and design hand-off
  into the next stream.
- **Stream — implementation & deploy (имплементация и деплой).** Agentic pipeline: spec → plan
  (including reuse/solution discovery when applicable) → technical architecture approval when required
  → build → verify → review → deploy → vibecode closure. This is the **agentic-dev method**
  (`agentics/HOME`).
- **Meta-layer (above).** Analyses run-data and improves the *workflow* and the *hand-off format*
  between streams. Itself improvable. See "Orchestrator vs meta-layer" below.

One **flow** = one spec being implemented through the streams. The flow always ends with a
**vibecode closure**: a terminal session that fixes residual implementation bugs against the current
spec, or records `0` bugs. If the closure discovers that the spec or approved technical architecture
was wrong/incomplete, that is a `spec_gap` / architecture gap and routes back to the design stream or
Architect; it is not counted as an implementation residual.

## How the two axes connect (substrate ↔ process)

They are **perpendicular**, in a *substrate ↔ process* relation:

- **Vault levels = the substrate** (static): where things are stored, with ownership/trust.
- **Agentic streams = the process** (dynamic): the conveyor that walks over that substrate.

Three concrete connection points:

1. **Launched from the top level.** The orchestrator lives at the `skandar` level — the only level
   that sees all domains. The agentic process *starts* from the top of the vertical. Not a
   coincidence: only the all-seeing level can conduct.
2. **Streams read/write specific levels.** Each stream consumes/produces artifacts that land at
   specific vault levels (spec → project, `trust: primary`; runs → project; method canon →
   `vlad-vault/agentics`). The process slides along the substrate without breaking it.
3. **Meta mirrors `primary → derived`.** The meta-layer takes run-data from projects (process
   first-source, `primary`) and distills it into method/lessons (`derived`, curated in
   `vlad-vault`). **Exact same arrow** as a personal corpus (`source → reflection`).
   The agentic meta-layer is a distillation engine over runs.

One line: **the agentic axis is a producer/consumer over the vault axis.** Vault = warehouse with
ownership borders; agentic = conveyor walking the warehouse. Different words because one is *place*,
the other *movement*.

## Orchestrator vs meta-layer (two different "above" things)

Easy to conflate; keep apart by **target function**:

- **Orchestrator** — *inside* the product axis. Conducts the streams to ship **the product** (no
  bugs). Sees one run, one product. Metric = quality of the **output**.
- **Meta-layer** — *above & orthogonal*. **Does not care about the product.** Optimises the
  *conditions of AI work*: how to split context between agents, where to parallelise, what
  retrieval the streams need. Sees **many runs at once**. Metric = quality of the **conveyor**.

The orchestrator optimises *this* product; the meta optimises *the ability to produce any* product.

⚠️ **The meta must not reach into a single run** ("for cosmomap today do X"). The moment it
configures one run, it *became* the orchestrator and the distinction is lost. Meta works offline,
over run-data, across many runs. It puts a rule on the shelf; the orchestrator takes it down.

## Retrieval / RAG is engine work, not meta work

The seed asked "will the meta choose the RAG implementation?" — **no.** This rides the seam already
wired into the vault: three рода — `primary` / `derived` / **движок**. RAG (Chroma, hybrid search,
BM25+vectors) is **движок** — lives in `../memory-layer`, no trust label, versioned in git.

Why the meta does **not** own the implementation:
1. **Category.** "What context agent B needs" is a workflow property (meta). "How the index/search
   is built" is engine internals. Merging them repeats the exact error the trust axis prevents.
2. **Scope.** The engine (`memory-layer`) serves the **whole namespace** — personal RAG over
   `reflection` **and** agentic dev. Its scope is *wider* than agentic. The meta only sees agentic
   runs; it can't own something bigger than itself.

**Demand vs supply resolution:**
- **Meta (demand):** "retrieval between agents is now the bottleneck; agents need hybrid search over
  zone-canon at recall X." A **requirement / spec**.
- **Движок (supply):** picks & builds Chroma+BM25, tunes, reconciles requirements from *all*
  consumers.

So the meta *formulates the need* for retrieval and hands it down to the engine — exactly like the
design stream hands a spec to implementation. Producer→consumer again.

Nice recursion: the engine is itself a software project → built **by the same streams through the
same conveyor** → the improved engine then serves the next agentic run.

## Who chooses the stream shape (split deploy or not?)

Both orchestrator and meta — but **different halves**, split along **policy vs instance**:

Test: *"is this decision about THIS product, or about ALL future products?"*
- "cosmomap's deploy is risky (payments, prod) — isolate it here" → this product → **orchestrator**.
- "splitting deploy generally cuts errors when there's a prod-edge — here's the criterion" → across
  runs → **meta**.

Three things, don't merge:
1. **The menu of shapes + selection criterion** (policy) → **meta**. Only it sees many runs and can
   notice "split deploy helps under condition X". Writes the playbook.
2. **The choice of shape for this run** (instance) → **orchestrator** (at project start, in practice
   the **human** in the design stream), reading meta's playbook + project profile.
3. **Evidence the choice was good/bad** → run-data → feeds back to meta.

Same `primary → derived` arrow: orchestrator chose (run fact, `primary`) → meta distilled into a
rule (`derived`, canon). Stream topology is just another lesson class.

**Bootstrap reality (now).** The meta playbook is nearly empty (2–3 runs). So **today the shape is
chosen by the orchestrator/human by judgment**, and each such call is exactly the run-data that
bootstraps the playbook. Structurally the *rule* belongs to meta; until the rule exists, the
*act* is carried ad-hoc by the orchestrator/human and becomes the raw material for the rule.

The instance is physically recorded in `agentics/method/project-instance` (the project's "execution-unit
list"); the template & criterion *behind* that list is what the meta improves.

## Meta-layer success metric — the residual & the vibecode tail

The first concrete metric for the meta-layer (observed 2026-06-04).

The agentic pipeline ships with a **residual** of human-visible defects — UI tweaks, visual
correctness, "is this even it". This is the **machine-inexpressible** error class
(`agentics/method/errors`): the automated nets (Verifier, QA) *structurally* can't see it — not
mis-tuned, just inexpressible as checks. It is the pipeline's natural tail, not a failure.

**Two ways to close the tail — and the crossover:**
- another agent run — expensive, non-deterministic, and **still blind** to the visual class;
- a short **human vibecode session** — cheap, tuned exactly to that class.

Below some residual size the vibecode pass **strictly wins**. So the vibecode tail is the
**designed terminal net**, not a defeat — and the same human who designed it (design stream /
vibecoder) closes the visual tail. The loop closes on one person.

**The existence of a short vibecode session is a positive signal** — it proves the residual fell
below the "re-run an agent" threshold. The target is **not zero residual**; it is *"the residual
stays in the cheap-human-pass zone and never grows back toward needing another agent loop."*

**Metric:** residual size = the **scope of the follow-up vibecode session** (fix count / time /
diff). Track the trend across runs; shrinking = the workflow is improving. This is the measurable
proxy for the invisible "oracle quality" Experiment 3 surfaced.

**Residual is also a data-feed, not just a number.** Each vibecode fix = something the net missed →
a candidate lesson, or a candidate **executable** check (the executability-down lever,
`agentics/method/context`). The meta-layer *harvests* the vibecode session, it doesn't only measure it.

**Browser-automation net is deferred on purpose.** Auto-checking visually (open Chrome, assert) is
how part of this residual becomes executable — but it's overhead now; it pays off only at volume
(same "deferred until volume" logic as the process-reviewer in
`decisions/agent-knowledge-architecture`). The meta-layer owns the **trigger** for when to
introduce it.

## Meta-layer finding — parallelism is governed by ownership seams, not change size

Second concrete meta finding (observed 2026-06-04). The meta-layer's answer to "how to
parallelise."

**Empirical:** a human can run a landing page in parallel with an agentic run, freely — but must
**not** introduce *any* other change, even small ones, into the zone the agent owns.

**The rule — and the right reason.** Safe parallelism is along **ownership seams**, not bounded by
size. The landing is safe because it is a **disjoint execution unit** (`agentics/method/project-instance`
— cosmomap's `apps/landing` is its own unit), **not** because it is small. A "small" edit inside the
agent's owned unit is the dangerous case, precisely because smallness tempts you past the seam
discipline:
- the agent plans & verifies against a **baseline snapshot**; a concurrent edit (even one line)
  invalidates its read context (planned against X, now X′);
- its checks are **global, not local** — an edit "off to the side" can turn its build red and the
  agent chases a ghost it didn't create;
- merge conflict + muddied review attribution ("agent or me?").

**Size does not bound blast radius** → the criterion is *"inside someone else's seam or not"*, never
*"small or big."*

This is **single-writer** (`agentics/method/constitution`) extended from agent-vs-agent to
**human-vs-agent**, plus "cut along real seams / low coupling" (`agentics/method/context`) applied to
*who touches what during a run*. Operating form: for the run's duration the agent **exclusively owns
its execution units**; a parallel human takes a **disjoint unit**; everything inside the agent's zone
is frozen until hand-off, regardless of size. Candidate to graduate into the constitution / a lesson.

## Why recorded (evidence)

cosmomap **Experiment 3** ran a feature through the implementation stream and shipped it; the
post-mortem showed the hand-off (a single thin spec) was too thin and that quality lived in oracles
the automated net couldn't see. That *is* meta-layer work — which surfaced the need for this layer
to exist explicitly. First worked example + framed questions:
`~/cosmomap/cosmomap-vault/meta/experiment-3-systemic-view.md` (project-local meta instance) and
`~/cosmomap/cosmomap-vault/meta/README.md`.

## Where things live

- **Implementation-stream method (canon):** `agentics/method/` · runs: `agentics/runs/` · lessons:
  `agentics/lessons/`.
- **Meta-layer:** portable canon → cross-domain, lives under `agentics/meta/`,
  reading `agentics/runs/`, improving `agentics/method/`). Project-local meta instances → each
  project vault (e.g. `cosmomap-vault/meta/`), mirroring how the method has portable canon +
  per-project instance.
- **Engine (RAG/движок):** `../memory-layer` — separate род, namespace-wide, demand-fed by meta.

## Terminology cleanup — done (2026-06-04)

The vault-wide rename is complete (canon: [[vlad-vault/glossary|glossary]]). Propagated: `context.md` (streams, not
"semantic layers"), `errors.md`, `HOME.md`, `decisions/2026-06-02-namespace-systematization`,
`skandar/CLAUDE.md` (dropped "семантические" from levels), `decisions/agent-knowledge-architecture`
(knowledge **zones**, not "semantic layers"). A third structural vocabulary surfaced — knowledge
**zones** (canon/precedent/journal/lessons) — now a glossary term.

## Open threads

1. **flow granularity** — `flow` = per-item trajectory (adopted here). Alternative reading (a small
   *structural* sub-block inside a stream) left open; a one-word swap if chosen.
2. **How many streams by default** — 2 for now; the set is explicitly open (research/spike,
   deploy-split, QA stream are candidates) without renaming "stream".

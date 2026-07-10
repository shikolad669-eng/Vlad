---
type: reference
status: active
sensitivity: normal
scope: all
axis: vault
updated: 2026-06-20
tags: [template, vault, entry-points, convention, project, base]
related:
  - HOME
  - principles
  - entry-points
  - ../CLAUDE.md
---

# Vault template — folder as entry point + project-vault skeleton

The **base-of-bases** for how a domain folder and its vault are laid out. Domains
(`music`, `study`, `content-factory`, …) conform to this and record only
their **deltas** in their own `principles.md`. Object-level writing rules live in
[[principles]]; this file is **structure + entry-point contract**.

## The model — the folder is the entry point

A domain folder is **not** just its vault. It holds a vault (knowledge base) **plus**
code projects, docs, agentic files, blog, presentations — anything. When an agent
opens the folder as cwd it must, first try: know what this place is, find the vault,
and find every project inside.

```
<domain>/                    ← THE entry point (the folder you open as cwd)
  CLAUDE.md        [door]     ← auto-loaded by the harness. The manifest.
  README.md        [human]    ← optional, humans only, never load-bearing
  <project-1>/ CLAUDE.md      ← each code repo has its own door
  <project-2>/ …
  docs/ blog/ presentations/  ← other contents — listed in the door
  <domain>-vault/             ← the knowledge base
    HOME.md        [map]      ← semantic navigation of the knowledge
    status.md      [hot]      ← current state, read every session
    principles.md  [rules]    ← "follows skandar base + these deltas"
    market/ plans/ tasks/ …   ← canonical zones (below)
```

## Entry-point contract

**Chain: `[door]` → `HOME.md` (map) → knowledge.** One role per file; the **door's
filename is harness-specific**.

- **The door.** The harness **auto-loads** it from cwd up the parent chain; nothing
  else is auto-loaded. Its filename depends on the tool: **`CLAUDE.md`** (Claude Code),
  **`AGENTS.md`** (Codex / others). A folder used by more than one tool carries **both
  as content-synced twins** (only the tool-name wording differs) — this is correct for
  the LLM-independent goal, *not* a duplicate to delete. Required at every openable cwd:
  every domain root **and** every code repo. The door is a **manifest**: (a) what this
  place is, (b) route to the vault first (`HOME.md` + `status.md`), (c) **enumerate the
  projects / zones inside** so agents find everything first try. Thin and stable. Model
  to copy: `~/vlad/content-factory/CLAUDE.md`.
- **`HOME.md` — the map.** Reached *via* the door (never auto-loaded). Exactly one per
  vault root. Semantic navigation by topic. Do **not** duplicate it at the workspace
  root — the map lives in the vault.
- **`README.md` — humans.** Optional. Never put agent routing only in README — the
  harness does not open it (the "cosmomap door bug" precedent from the skandar base, see [[entry-points]]).
- A folder that is only a knowledge vault (no code) still gets a `CLAUDE.md` door if it
  can be opened as cwd; it may be a one-line redirect into `HOME.md`.

## Project-vault skeleton

`<domain>-vault/`. **Mandatory** spine + **shared** body + **optional** by business
type. Each zone is one-file-per-object per [[principles]].

**Mandatory**
- `HOME.md` [map], `status.md` [hot], `principles.md` [rules], `secrets-map.md` (pointers).
- `market/` — `overview.md` + `competitors/` (one file per competitor).
- `plans/` — open roadmaps + horizon (`vision` / `now`); differential, rebuilt from state.
- `tasks/` — per-cycle agentic run-data (`spec → plan → build → review → record`).

**Shared body**
- `systems/` — own components (what each is + why, not implementation).
- `decisions/` — dated precedents `YYYY-MM-DD-*` (incl. negative "rejected X").
- `lessons/` — operational rules (trigger → rule → why).
- `tools/`, `people/` — reference cards.
- `_archive/` — terminal; no live links from canon.

**Optional by business type**
- `clients/` — if a client business.
- `analytics/` — quantified prod analysis.
- `research/` — long write-ups with TL;DR.
- `positioning.md` — if there is an outward offer.
- `curriculum/` — if an education business.

## status.md contract — blockers visible from the top

`status.md` is the **hot-state**, read every session. The recording rule (added
2026-06-26): **blockers must be visible to a high-level agent without drilling into
side-docs.**

- **Carry a `Blockers` / not-done surface, led with — never buried.** State plainly what is
  **not** done and what is **gated and on what**. A `docs/*.md` that holds the real blocker
  is invisible to a planning agent that reads the door + `status.md` only. (Same failure as
  the door-bug precedent: the truth existed, in a file the machine doesn't auto-open.)
- **"Deployed / works" ≠ done — the demo view hides the last mile.** A status that leads with
  success makes a high-level read confidently wrong on the final step. Always pair *what
  works* with *what's blocked*.
- **Propagate cross-domain blockers UP.** A blocker that gates a higher-level priority is
  copied into the **hot-state the higher level actually reads** (e.g. a domain project blocker
  → the doc the top level actually reads), with the **specific** blocker, not a
  vague "gate". The top agent must hit it from its normal read.
- **Why it matters (the principle):** planning is **two-altitude** — the top owns priority,
  the project owns the real blockers; correctness comes from the *data* being right (honest
  hot-state), and a sub-agent is then an optimisation for depth, not a correctness crutch.
  (Rule inherited from the skandar base, worked example 2026-06-26 lives there.)

## Base + deltas

This template + [[principles]] are the **base**. A project vault's `principles.md`
opens with *"follows skandar base + these deltas"* and lists only what it changes
(e.g. study drops `market/` — not a business; music keeps it). New projects are
**born from this template**, so they are correct on day one rather than retrofitted.

## Conformance

Live status of every door/map across the namespace → [[entry-points]].

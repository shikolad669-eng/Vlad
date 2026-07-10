---
type: reference
status: active
sensitivity: private
scope: work
axis: vault
date: 2026-06-29
updated: 2026-06-29
tags: [tool, telegram, bot, mvp, pipeline, base]
related:
  - ../status
  - ../positioning
  - ../plans/vision
---

# telegram-channel-bot — first pipeline base

First concrete touch of the content-factory loop, built as a **test scaffold**
(2026-06-29). The venture stays concept-stage; this is a proof base, not the
production pipeline.

## The idea (good)
AI runs a Telegram channel through a bot: the owner feeds raw info (a thought, a
fact, a fragment), the AI turns it into a finished post **in the channel's
voice**, the owner approves with one tap, the bot publishes. **Draft → approve,
never autopost.**

Why it holds up as an idea:
- It's the content-factory thesis on the smallest real surface — *AI output
  grounded in a per-client voice + a human approval gate*, not generic slop.
- The approval tap is also the voice-training loop (Rewrite button = feedback).
- Per-channel persona file = the "per-client knowledge base" differentiator in
  embryo. One bot, swap the persona, serve N channels/clients.
- Removes the real bottleneck for media presence — consistency of output — while
  leaving authorship/judgement with the human.

## The base (good)
A working MVP exists: `~/maksi-studio/tg-channel-bot/` (own README + persona.md).
Placed in maksi-studio as a test project; if it graduates it becomes its own
project under this venture.

- **Stack:** Python 3.12 · httpx long-polling (no webhook, no deploy needed) ·
  Anthropic SDK · single-file `bot.py`. Voice lives in `persona.md`, re-read on
  every request (edit live, no restart).
- **Works, verified live:** DM raw text → Claude draft → inline buttons
  [✅ Publish · 🔄 Rewrite · ❌ Cancel] → posts to the channel. Plus `post.py`
  for one-shot posting "from here". Test post landed in channel **Vlad music**
  (`t.me/htopnot`); admin rights + posting confirmed. Channel id captured via
  forward-detection in the bot.
- **Config:** `OWNER_ID` (lock bot to owner) and `CHANNEL_ID` optional; with no
  channel set it falls back to posting in DM for dry runs.

Why it's good as a base:
- Minimal deps, transparent single file, swappable persona, approval gate baked
  in — easy to extend without rework.
- Clean extension path: voice/photo intake → autopost rubrics → scheduling →
  response analytics → multi-channel (per-client) → Railway deploy as a service.

## Pointers
- Code: `~/maksi-studio/tg-channel-bot/` (README, `bot.py`, `persona.md`, `post.py`).
- Secrets: `~/maksi-studio/.secrets/tg-channel-bot.env` — bot token + reused
  `ANTHROPIC_API_KEY`. Values off-file (pointer only).
- Bot: @Karagandamusicbot. Test channel surface: `t.me/htopnot` (Vlad music).

## Next (deferred — concept discipline)
- Fill `persona.md` with 5–20 real sample posts so the voice is a person's, not
  neutral. Without this it's grounded-but-generic.
- Voice-message / photo intake; autopost rubrics; scheduling; response analytics.
- Decide if this graduates from test scaffold to a venture project (own CLAUDE.md).

---
type: reference
status: active
sensitivity: normal
scope: work
axis: vault
date: 2026-07-27
updated: 2026-07-27
tags: [secrets, map, pointers]
---

# Secrets map — ai-agents

**Только указатели, никогда значения.** Ключи и доступы живут в `~/vlad/secrets/`
и `.env` (вне git). Канон уровня: [[vlad-vault/secrets-map|vlad-vault/secrets-map]].

| Что | Где лежит | Статус |
|---|---|---|
| API-ключи LLM-провайдеров (см. [[ai-agents/ai-agents-vault/tools/llm/README|LLM Wiki]]) | `~/vlad/secrets/` | не заведены |
| Доступы к каналам клиента (WhatsApp/Instagram/Telegram) | у клиента, на нашей стороне — `.env` внедрения | не заведены |
| Хостинг агента / платформа сборки | `~/vlad/secrets/` | не заведены |

> Доступ клиента к его каналам — чужая собственность: берём минимально
> необходимое, фиксируем в карточке клиента **что** выдано, не **чем** входим.

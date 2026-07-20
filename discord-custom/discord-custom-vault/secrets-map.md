---
type: reference
status: active
sensitivity: normal
scope: work
date: 2026-07-20
updated: 2026-07-20
tags: [secrets-map, pointers]
related:
  - HOME
  - ../../vlad-vault/secrets-map
---

# Secrets map — discord-custom

Pointers only, never values (vlad base rule).

- **mod-bot token** → `discord-custom/bots/mod-bot/.env` (ключ `DISCORD_TOKEN`,
  вне git). Бот в Developer Portal — **WarBot**, App ID `1528717047297474580`
  (публичный, не секрет). Сам токен ещё не вставлен. Токен утёк = сервер угнан.
  См. [[discord-custom/discord-custom-vault/systems/mod-bot|systems/mod-bot]].
- Прочие доступы (Discord-аккаунт бизнеса, площадки поиска заказов, платёжки) —
  при появлении в `.env`/`~/vlad/secrets/`, здесь только указатели. Global map:
  [[vlad-vault/secrets-map|vlad-vault/secrets-map]].

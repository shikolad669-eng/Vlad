---
type: reference
status: active
sensitivity: normal
scope: work
date: 2026-07-20
updated: 2026-07-20
tags: [systems, bot, moderation, python, discord-py]
related:
  - README
  - discord-server-template
  - ../status
  - ../secrets-map
---

# mod-bot — бот ручной модерации (карточка-указатель)

**Первый бот стека.** Ручная модерация слэш-командами (модератор вызывает сам,
без автофильтров). Закрывает слой №4 «Модерация» из
[[discord-custom/discord-custom-vault/systems/discord-server-template|шаблона сервера]].

- **Код (движок):** `../../bots/mod-bot/` (в git). Точка входа `bot.py`,
  логика — `cogs/moderation.py`. README с установкой рядом.
- **Стек:** Python 3.11+ / discord.py 2.x. Выбран как **базовый стек ботов**
  домена (был открытый вопрос в [[discord-custom/discord-custom-vault/status|status]]).
- **Команды:** `/kick`, `/ban`, `/unban`, `/timeout`, `/untimeout`, `/warn`,
  `/warnings`, `/clearwarnings`, `/purge`, `/slowmode`, `/help`.
- **Гарантии:** проверка иерархии ролей, права Discord на каждой команде, лог в
  канал + ЛС участнику, предупреждения в `data/warnings.json` (вне git).
- **Секреты:** токен только в `bots/mod-bot/.env` (вне git). Указатель —
  [[discord-custom/discord-custom-vault/secrets-map|secrets-map]].

## Статус (2026-07-20)

- ✅ Python 3.14 стоит, venv + зависимости (discord.py 2.7.1) — в `bots/mod-bot/.venv/`.
- ✅ Код проверен: синтаксис + дымовой тест (11 команд в дереве, парсер длительности).
- ✅ Приложение-бот в Developer Portal: **WarBot**, Application ID
  `1528717047297474580`. **Server Members Intent** включён (Presence / Message
  Content — выкл, не нужны).
- ⏳ **Пригласить на сервер:** ссылка готова (client_id + perms `1099511720982`,
  scope `bot applications.commands`) — Влад авторизует (десктоп-приложение
  Discord перехватывает OAuth; клик «Авторизовать» + возможная капча — за Владом).
- ⏳ **Токен:** `bot`-страница → «Сбросить токен» → вставить в `bots/mod-bot/.env`
  (файл создан, строка `DISCORD_TOKEN=` пустая). Токен — только руками Влада.
- ⏳ **Запуск:** после токена — `./.venv/Scripts/python.exe bot.py` (сделает агент).

## Переиспользование под заказы

База под клиентские сервера: свой токен/бот на заказ, при необходимости — свой
`MOD_LOG_CHANNEL_ID`. Расширяется новыми cog'ами (тикеты, приветствия,
reaction-roles) без переписывания ядра.

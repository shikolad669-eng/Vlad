---
type: status
status: active
sensitivity: normal
scope: work
date: 2026-07-20
updated: 2026-07-20
tags: [status, hot]
---

<!-- updated 2026-07-20: 1-й кейс — сборка «Сервера Менделеев» по образцу ARUKU (структура + правила готовы) -->

# status — discord-custom

Hot state. Read at session start; keep small and current.
**Blockers must be visible here, never buried in side-docs** (base rule).

## Focus

- Ядро домена: **кастомизация Discord-серверов под заказ** (структура каналов,
  роли/права, боты, брендинг, модерация). Оффер: [[discord-custom/discord-custom-vault/positioning|positioning]].
- **Активный кейс: «Сервер Менделеев»** (сервер Влада, реплика ARUKU). Структура
  (7 категорий, ~35 каналов) + правила — **готовы**. Продолжение — ниже.
  Лог: [[discord-custom/discord-custom-vault/tasks/mendeleev-server/log|tasks/mendeleev-server/log]] ·
  переиспользуемый шаблон: [[discord-custom/discord-custom-vault/systems/discord-server-template|systems/discord-server-template]].

## Blockers / not done

- **«Сервер Менделеев» — следующие шаги** (Влад хотел «всё как на ARUKU»):
  - **роли** (цветные + reaction-roles «уютные/игровые») — нужен стек ботов;
  - **права** приватных каналов (CLOSE, Приватная, Любовная — сейчас открыты);
  - **баннеры-картинки** шапок каналов (нужны готовые изображения → `../assets/`).
- Оффер не сформулирован: состав услуг, пакеты и цены (`positioning.md` — пусто).
- Рынок не разведан: где искать клиентов, конкуренты, вилка цен (`market/` — пусто).
- Базовый стек ботов выбран: **Python/discord.py**, первый бот —
  [[discord-custom/discord-custom-vault/systems/mod-bot|mod-bot]] (ручная модерация,
  код готов). **Не запущен:** нет Python в системе + не заведён бот/токен в
  Developer Portal. Reaction-roles — отдельным cog'ом позже.
- Доступы (Discord-аккаунт бизнеса, боты, площадки заказов) не заведены —
  указатели появятся в `secrets-map.md`. Пока работаем в Chrome Влада.

## Pointers

- Карта: [[discord-custom/discord-custom-vault/HOME|HOME]] · правила: [[discord-custom/discord-custom-vault/principles|principles]].

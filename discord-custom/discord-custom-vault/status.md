---
type: status
status: active
sensitivity: normal
scope: work
date: 2026-07-20
updated: 2026-07-20
tags: [status, hot]
---

<!-- updated 2026-07-20 (сессия 2): сервер переименован в Backrooms, штабные роли Owner/Admin/Moder готовы -->

# status — discord-custom

Hot state. Read at session start; keep small and current.
**Blockers must be visible here, never buried in side-docs** (base rule).

## Focus

- Ядро домена: **кастомизация Discord-серверов под заказ** (структура каналов,
  роли/права, боты, брендинг, модерация). Оффер: [[discord-custom/discord-custom-vault/positioning|positioning]].
- **Активный кейс: сервер «Backrooms»** (экс-«Сервер Менделеев», сервер Влада,
  реплика ARUKU + свой бренд «Beckroom»: казачий имперский арт). Структура
  (7 категорий, ~35 каналов) + правила + штабные роли (Owner/Admin/Moder) —
  **готовы**. Продолжение — ниже.
  Лог: [[discord-custom/discord-custom-vault/tasks/mendeleev-server/log|tasks/mendeleev-server/log]] ·
  переиспользуемый шаблон: [[discord-custom/discord-custom-vault/systems/discord-server-template|systems/discord-server-template]].

## Blockers / not done

- **«Backrooms» — следующие шаги** (детали в логе кейса):
  - роль **Стажёр** досохранить (mute), **Content-maker** создать;
  - **аватарка сервера** (кроп орла с баннера; ChatGPT из браузера заблокирован);
  - баннер-файл из Downloads → `../assets/` + карточка;
  - reaction-roles «уютные/игровые» — нужен стек ботов;
  - **права** приватных каналов (CLOSE, Приватная, Любовная — сейчас открыты).
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

---
type: status
status: active
sensitivity: normal
scope: work
date: 2026-07-10
updated: 2026-07-25
tags: [status, hot]
---

# status — phyto

Hot state. Read at session start; keep small and current.
**Blockers must be visible here, never buried** (base rule).

## Focus

- Природа домена зафиксирована: phyto — **оптовый (B2B) + розничный бизнес
  фитопродукции**. Роль — эксклюзивный дистрибьютор трав Гордеева по РК,
  склад — Караганда. Витрина: [travnik.kz](https://www.travnik.kz/) +
  Instagram [@sibir.kz](https://www.instagram.com/sibir.kz/).
- Строится **LLM-вики** бизнеса. По состоянию на 2026-07-25 собран каркас +
  каталог + процессы (lead-gen, promotion, automation).

## Что построено (2026-07-24 … 25)

- **Бизнес-ядро** `systems/`: [[phyto/phyto-vault/systems/business-model|business-model]],
  [[phyto/phyto-vault/systems/wholesale-offer|wholesale-offer]],
  [[phyto/phyto-vault/systems/supplier-gordeev|supplier-gordeev]],
  [[phyto/phyto-vault/systems/channels|channels]].
- **Каталог** `catalog/`: все **780 SKU / 19 категорий** сняты из RSC-потока сайта
  → [[phyto/phyto-vault/catalog/products-detailed|products-detailed]] (все поля) +
  [[phyto/phyto-vault/catalog/full-catalog|full-catalog]] (имя/фасовка/цена) +
  машинные `products.csv` / `products.json` + [[phyto/phyto-vault/catalog/categories|categories]].
- **Рынок** `market/`: [[phyto/phyto-vault/market/overview|overview]] +
  [[phyto/phyto-vault/market/wholesale-leads|wholesale-leads]] (10 оптовых лидов РК).
- **Процессы-алгоритмы** `systems/`: [[phyto/phyto-vault/systems/lead-gen|lead-gen]]
  (поиск клиентов), [[phyto/phyto-vault/systems/promotion|promotion]] (7 алгоритмов
  продвижения, вкл. Threads), [[phyto/phyto-vault/systems/automation-claude-code|automation-claude-code]]
  (автоматизация через ИИ).

## Blockers / not done (нужен ввод Влада)

- **Данные каталога — `derived`, снимок 2026-07-24.** Источник правды — живой сайт;
  цены устаревают. Покрытие полей: состав 293, применение 442, штрихкод 671 из 780.
- **Условия опта не заведены:** MOQ, скидочные тиры, маржа, оплата/возвраты —
  на сайте только «прайс по запросу».
- **Структура каналов** (Kaspi/Flip/розничный отдел) — записана со слов Влада, но
  не детализирована: магазины/ссылки, кто ведёт отдел, ценовые контуры. Открытые
  вопросы — [[phyto/phyto-vault/systems/channels|channels]].
- **Лиды (10) неквалифицированы:** нет прямых контактов/ЛПР, не проверены на
  конкуренцию/текущего поставщика.
- **Юрлицо/ИП, реквизиты, договор эксклюзива** — не заведены (→ `~/vlad/secrets/`).
- **Instagram-метрики** — не сняты (login-wall). Threads — ещё не запущен.
- Автоматизация — на Фазе 1 (черновики), доступы (Meta/Kaspi/Sheets) не подключены.

## Next (кандидаты, по выбору Влада)

- Прогнать lead-gen на новую пачку (напр. только Караганда / Kaspi-селлеры) или
  пробить контакты по текущей десятке.
- Собрать Фазу-1 автоматизации: слэш-команда `/content` — черновики постов Threads.
- Дать оптовую наценку → сгенерировать прайс под сегмент.

## Pointers

- Карта: [[phyto/phyto-vault/HOME|HOME]] · правила: [[phyto/phyto-vault/principles|principles]] ·
  источники: [[phyto/phyto-vault/sources|sources]].

---
type: reference
status: active
sensitivity: normal
scope: work
date: 2026-07-24
updated: 2026-07-24
tags: [sources, provenance, derived]
related:
  - HOME
  - principles
---

# Sources — провенанс данных

Всё наполнение вики v1 — `derived` (снято с публичных источников), **не от
Влада**. Источник правды по ассортименту/ценам — живой сайт. Снимок: 2026-07-24.

## Источники

- **[travnik.kz](https://www.travnik.kz/)** — главная: позиционирование, товары,
  контакты, доставка. → business-model, market, channels, catalog.
- **[travnik.kz/optovikam](https://www.travnik.kz/optovikam)** — оптовые
  сегменты, benefits, «прайс по запросу», документы. → wholesale-offer.
- **[travnik.kz/catalog](https://www.travnik.kz/catalog)** — **все 780 SKU /
  19 категорий**, сняты 2026-07-24 из Next.js RSC-потока (`fetch('/catalog',
  {headers:{RSC:'1'}})` → массив `products` со всеми полями). → catalog/.
  Картинки товаров — Firebase Storage (`travnik-5cc55`); часть `sourceUrl`
  ведёт на flip.kz (перепродажа/референс). Цены — розничные, снимок.
- **[Instagram @sibir.kz](https://www.instagram.com/sibir.kz/)** — имя/тематика
  («ФИТО АПТЕКА | ТРАВЫ ГОРДЕЕВА | ЖЕНСКОЕ ЗДОРОВЬЕ | КАРАГАНДА»). Частично
  (login-wall): без метрик и bio-контактов. → channels, market.
- **Веб-поиск «фитоцентр Гордеева»** — профиль поставщика (Гордеев М.В., >20 лет,
  200+ сборов, Башкирия/Алтай, точки Уфа/Стерлитамак/Москва). → supplier-gordeev.
  Референсы: travogor.ru, travoshop.ru (связь с этим бизнесом не подтверждена).
- **Веб-поиск оптовых лидов РК** (2ГИС, Satu, сайты, 2026-07-24) → wholesale-leads.
- **Веб-поиск Threads 2026** (маркетинг/реклама + аудитория РК, 2026-07-25):
  ~320 млн MAU глобально, РК ~1,85 млн (обогнал X); Threads Ads запущены глобально
  21.01.2026, CPM на 30–40% ниже IG; алгоритм: ответы>лайки, founder-led.
  → promotion (Алгоритм 7).

## Не покрыто / требует Влада

- Реальные оптовые условия: MOQ, тиры, маржа, оплата, возвраты.
- Юрлицо/ИП, реквизиты, договор эксклюзива с Гордеевым (→ `secrets/`).
- Полная оцифровка каталога; метрики Instagram; конкуренты.

> Правило: при вводе фактов **от Влада** помечать их (не derived) — меняет trust
> строки с «слепок витрины» на «подтверждено владельцем».

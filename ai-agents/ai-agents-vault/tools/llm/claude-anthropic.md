---
tags: [llm, вики, anthropic]
created: 2026-07-25
type: reference
scope: work
axis: vault
updated: 2026-07-27
---

# Claude (Anthropic)

Назад к [[ai-agents/ai-agents-vault/tools/llm/README|LLM Wiki]]

## Кратко
Семейство моделей от Anthropic. Сильны в рассуждении, работе с кодом, длинных документах и следовании инструкциям. Основной API — **Anthropic API** (Messages API).

## Линейка (семейство Claude 5 + Haiku 4.5)
| Модель | Позиционирование | Model ID |
|---|---|---|
| Opus 5 | Максимум качества/рассуждения | `claude-opus-5` |
| Sonnet 5 | Баланс качество/скорость/цена | `claude-sonnet-5` |
| Fable 5 | — | `claude-fable-5` |
| Haiku 4.5 | Быстрая и дешёвая | `claude-haiku-4-5-20251001` |

> [!info] Для приложений
> По умолчанию бери самые свежие и мощные модели Claude. Точные ID/цены/лимиты — сверяй через справочник `claude-api` или доки Anthropic.

## Параметры и фичи
- Контекст: ⚠️ уточнить по модели
- Цена (вход/выход за 1M токенов): ⚠️ уточнить
- Возможности: tool use (функции), MCP, prompt caching, streaming, vision.

## Когда выбирать
- Нужны качественные рассуждения и аккуратное следование инструкциям.
- Работа с кодом и агентами (см. [[ai-agents/ai-agents-vault/HOME|карта домена]]).
- Длинные документы.

## Ссылки
- ⚠️ Официальная документация Anthropic (добавить URL)

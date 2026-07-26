---
tags: [llm, вики, гайд]
created: 2026-07-25
type: reference
scope: work
axis: vault
updated: 2026-07-27
---

# Как выбрать модель

Назад к [[ai-agents/ai-agents-vault/tools/llm/README|LLM Wiki]]

## Алгоритм под задачу

1. **Сформулируй задачу и метрику качества** — что считаем «хорошим ответом».
2. **Собери 20–50 реальных примеров** и прогони через 2–3 кандидата.
3. **Сравни по осям** (см. [[ai-agents/ai-agents-vault/tools/llm/comparison|Сравнение моделей]]): качество → цена → латентность → приватность.
4. **Проверь бюджет**: цена × ожидаемый объём токенов/мес.
5. **Учти данные клиента**: если чувствительные — смотри self-hosting ([[ai-agents/ai-agents-vault/tools/llm/llama-meta|Llama (Meta)]]) или юрисдикцию.

## Быстрые эвристики

| Ситуация | Куда смотреть |
|---|---|
| Нужно лучшее качество/рассуждение | [[ai-agents/ai-agents-vault/tools/llm/claude-anthropic|Claude (Anthropic)]], топовые модели |
| Дёшево и массово (простые ответы) | лёгкие модели: Haiku, [[ai-agents/ai-agents-vault/tools/llm/mistral|Mistral]], [[ai-agents/ai-agents-vault/tools/llm/deepseek|DeepSeek]] |
| Приватность / on-premise | [[ai-agents/ai-agents-vault/tools/llm/llama-meta|Llama (Meta)]], open-weight |
| Очень длинный контекст | [[ai-agents/ai-agents-vault/tools/llm/gemini-google|Gemini (Google)]] |
| Рынок РФ / локальные требования | [[ai-agents/ai-agents-vault/tools/llm/other-models|Другие модели]] (Yandex, GigaChat) |

> [!tip] Главное правило
> **Не выбирай по бенчмаркам из интернета — выбирай по своим тестам.** Модель, которая лучше на чужих задачах, может проиграть на твоих.

## Связь с бизнесом
Для [[ai-agents/ai-agents-vault/systems/tech-stack|техстека агентов]]: на старте — сильная модель для качества, для дешёвых массовых диалогов — лёгкая. Расход токенов закладывай в [[ai-agents/ai-agents-vault/systems/pricing|Ценообразование]].

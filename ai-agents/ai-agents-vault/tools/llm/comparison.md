---
tags: [llm, вики, сравнение]
created: 2026-07-25
type: reference
scope: work
axis: vault
updated: 2026-07-27
---

# Сравнение моделей

Назад к [[ai-agents/ai-agents-vault/tools/llm/README|LLM Wiki]]

> [!warning] ⚠️ Все цифры — заполнять из официальных доков
> Таблица — каркас. Проставляй актуальные значения сам, не по памяти.

| Модель | Провайдер | Open-weight | Контекст | Цена (вх/вых /1M) | Сильная сторона |
|---|---|---|---|---|---|
| [[ai-agents/ai-agents-vault/tools/llm/claude-anthropic|Claude (Anthropic)]] | Anthropic | Нет | ⚠️ | ⚠️ | Рассуждение, код, инструкции |
| [[ai-agents/ai-agents-vault/tools/llm/gpt-openai|GPT (OpenAI)]] | OpenAI | Нет | ⚠️ | ⚠️ | Экосистема, мультимодальность |
| [[ai-agents/ai-agents-vault/tools/llm/gemini-google|Gemini (Google)]] | Google | Нет | ⚠️ | ⚠️ | Длинный контекст, мультимодальность |
| [[ai-agents/ai-agents-vault/tools/llm/llama-meta|Llama (Meta)]] | Meta | Да | ⚠️ | своя GPU | Self-hosting, приватность |
| [[ai-agents/ai-agents-vault/tools/llm/mistral|Mistral]] | Mistral | Частично | ⚠️ | ⚠️ | Цена/качество, EU |
| [[ai-agents/ai-agents-vault/tools/llm/deepseek|DeepSeek]] | DeepSeek | Частично | ⚠️ | ⚠️ | Низкая цена, reasoning |

## Оси сравнения (что реально важно)
- **Качество** на твоих задачах (тестируй на своих примерах!).
- **Цена** за токены и предсказуемость расходов.
- **Контекст** — сколько текста влезает за раз.
- **Приватность / юрисдикция** — где живут данные клиента.
- **Фичи** — tools, vision, caching, streaming.
- **Латентность** — скорость ответа (критично для [[ai-agents/ai-agents-vault/systems/products|агентов поддержки]]).

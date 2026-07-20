# mod-bot — бот ручной модерации

Первый бот стека `discord-custom`. Слэш-команды, модератор вызывает действия
сам (без автофильтров). Стек: **Python 3.11+ / discord.py 2.x**.

## Команды

| Команда | Что делает | Право Discord |
|---|---|---|
| `/kick` | выгнать участника | Kick Members |
| `/ban`, `/unban` | бан / разбан по ID | Ban Members |
| `/timeout`, `/untimeout` | мут на время (`10m`, `1h30m`, `2d`, макс 28 дн) / снять | Moderate Members |
| `/warn`, `/warnings`, `/clearwarnings` | предупреждения (копятся в `data/warnings.json`) | Moderate Members |
| `/purge` | удалить N последних сообщений (1–100, опц. одного автора) | Manage Messages |
| `/slowmode` | медленный режим канала (0 = выкл) | Manage Channels |
| `/help` | список команд | — |

Защита у каждого действия над участником: нельзя тронуть себя, бота, владельца
сервера и того, чья роль выше/равна твоей (и роли бота). Каждое действие пишется
в лог-канал (если задан) и участнику в ЛС.

## Установка

1. **Python 3.11+.** Проверь: `python --version`. Если нет — поставь с python.org
   (в этой системе сейчас не установлен).
2. Зависимости:
   ```
   pip install -r requirements.txt
   ```
3. Создай приложение и бота: <https://discord.com/developers/applications> →
   *New Application* → вкладка **Bot** → *Reset Token* (скопируй токен).
4. На вкладке **Bot** включи **Server Members Intent** (нужен для kick/ban/timeout
   и ЛС). *Message Content Intent* — НЕ нужен.
5. Скопируй `.env.example` → `.env`, впиши `DISCORD_TOKEN`. По желанию `GUILD_ID`
   (мгновенная регистрация команд на dev-сервере) и `MOD_LOG_CHANNEL_ID`.
6. Пригласи бота на сервер (OAuth2 → URL Generator → scopes `bot` +
   `applications.commands`, права: Kick/Ban/Moderate/Manage Messages/Manage
   Channels). **Роль бота подними выше ролей тех, кого он будет модерировать.**
7. Запуск:
   ```
   python bot.py
   ```

## Безопасность токена

`.env` в git не попадает (корневой `.gitignore`). Токен утёк = сервер угнан —
никогда не коммить и не пересылай его. Указатель на доступ — в
`../../discord-custom-vault/secrets-map.md`.

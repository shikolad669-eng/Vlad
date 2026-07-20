"""mod-bot — ручная модерация Discord-сервера (слэш-команды).

Первый бот стека discord-custom. Точка входа: загружает конфиг из .env,
поднимает клиент с нужными intents, подключает cog модерации и синкает
слэш-команды.

Запуск:  python bot.py   (сначала: pip install -r requirements.txt, заполнить .env)
"""

import logging
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s: %(message)s",
)
log = logging.getLogger("mod-bot")


class ModBot(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.members = True  # нужно для kick/ban/timeout по участнику и DM
        intents.message_content = False  # ручная модерация не читает содержимое
        super().__init__(command_prefix="!", intents=intents, help_command=None)

    async def setup_hook(self) -> None:
        # Загружаем cog(и).
        await self.load_extension("cogs.moderation")

        # Синхронизация слэш-команд.
        if GUILD_ID:
            guild = discord.Object(id=int(GUILD_ID))
            self.tree.copy_global_to(guild=guild)
            synced = await self.tree.sync(guild=guild)
            log.info("Синхронизировано %d команд для сервера %s.", len(synced), GUILD_ID)
        else:
            synced = await self.tree.sync()
            log.info("Синхронизировано %d глобальных команд (до часа на раскатку).", len(synced))

    async def on_ready(self) -> None:
        log.info("Вошёл как %s (id=%s). Серверов: %d.", self.user, self.user.id, len(self.guilds))
        await self.change_presence(activity=discord.Game(name="модерация · /help"))


def main() -> None:
    if not TOKEN:
        raise SystemExit(
            "DISCORD_TOKEN не задан. Скопируй .env.example → .env и впиши токен бота."
        )
    ModBot().run(TOKEN, log_handler=None)


if __name__ == "__main__":
    main()

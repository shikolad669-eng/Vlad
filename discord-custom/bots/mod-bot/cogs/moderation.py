"""Cog ручной модерации: kick / ban / unban / timeout / warn / purge / slowmode.

«Ручная» = модератор вызывает действие сам слэш-командой. Никаких автофильтров.

Общие гарантии для всех действий над участником:
  * нельзя тронуть себя, самого бота и владельца сервера;
  * нельзя тронуть того, чья высшая роль >= твоей (и >= роли бота);
  * действие пишется в лог-канал (если задан) и участнику в ЛС (best-effort).
"""

from __future__ import annotations

import datetime as dt
import json
import logging
import os
import re
from pathlib import Path

import discord
from discord import app_commands
from discord.ext import commands

log = logging.getLogger("mod-bot.moderation")

MOD_LOG_CHANNEL_ID = os.getenv("MOD_LOG_CHANNEL_ID")
WARN_FILE = Path(__file__).resolve().parent.parent / "data" / "warnings.json"

# Discord ограничивает timeout 28 сутками.
MAX_TIMEOUT = dt.timedelta(days=28)

COLOR = {
    "kick": discord.Color.orange(),
    "ban": discord.Color.red(),
    "unban": discord.Color.green(),
    "timeout": discord.Color.gold(),
    "untimeout": discord.Color.green(),
    "warn": discord.Color.yellow(),
    "purge": discord.Color.blurple(),
    "slowmode": discord.Color.blurple(),
}

_DURATION_RE = re.compile(r"(\d+)\s*([smhdw])", re.IGNORECASE)
_UNIT_SECONDS = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}


def parse_duration(text: str) -> dt.timedelta | None:
    """'10m', '1h30m', '2d' -> timedelta. None если не распарсилось."""
    matches = _DURATION_RE.findall(text or "")
    if not matches:
        return None
    total = sum(int(n) * _UNIT_SECONDS[u.lower()] for n, u in matches)
    return dt.timedelta(seconds=total) if total > 0 else None


# --------------------------- хранение предупреждений ---------------------------

def _load_warns() -> dict:
    if WARN_FILE.exists():
        try:
            return json.loads(WARN_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            log.warning("warnings.json повреждён — стартую с пустого.")
    return {}


def _save_warns(data: dict) -> None:
    WARN_FILE.parent.mkdir(parents=True, exist_ok=True)
    WARN_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


# ------------------------------------ cog ------------------------------------

class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.warns = _load_warns()

    # ---- вспомогательные ----

    def _key(self, guild_id: int, user_id: int) -> str:
        return f"{guild_id}:{user_id}"

    async def _log_action(
        self,
        interaction: discord.Interaction,
        action: str,
        target: discord.abc.User,
        reason: str,
        extra: str | None = None,
    ) -> None:
        embed = discord.Embed(
            title=f"Модерация · {action}",
            color=COLOR.get(action, discord.Color.greyple()),
            timestamp=dt.datetime.now(dt.timezone.utc),
        )
        embed.add_field(name="Участник", value=f"{target} (`{target.id}`)", inline=False)
        embed.add_field(name="Модератор", value=interaction.user.mention, inline=True)
        if extra:
            embed.add_field(name="Детали", value=extra, inline=True)
        embed.add_field(name="Причина", value=reason or "—", inline=False)

        if MOD_LOG_CHANNEL_ID:
            channel = interaction.guild.get_channel(int(MOD_LOG_CHANNEL_ID))
            if isinstance(channel, discord.TextChannel):
                try:
                    await channel.send(embed=embed)
                except discord.HTTPException:
                    log.warning("Не смог написать в лог-канал %s.", MOD_LOG_CHANNEL_ID)
        log.info("%s: %s -> %s (%s)", action, interaction.user, target, reason)

    async def _dm(self, member: discord.abc.User, guild_name: str, action: str, reason: str) -> None:
        try:
            await member.send(
                f"На сервере **{guild_name}** к тебе применено действие: **{action}**.\n"
                f"Причина: {reason or '—'}"
            )
        except (discord.Forbidden, discord.HTTPException):
            pass  # ЛС закрыты — не критично

    def _guard(
        self, interaction: discord.Interaction, member: discord.Member
    ) -> str | None:
        """Проверка иерархии. Возвращает текст ошибки или None если можно."""
        if member.id == interaction.user.id:
            return "Нельзя применить действие к самому себе."
        if member.id == self.bot.user.id:
            return "Я не могу модерировать сам себя."
        if member.id == interaction.guild.owner_id:
            return "Нельзя тронуть владельца сервера."
        author = interaction.user
        if isinstance(author, discord.Member) and author.id != interaction.guild.owner_id:
            if member.top_role >= author.top_role:
                return "У участника роль выше или равная твоей — не могу."
        me = interaction.guild.me
        if member.top_role >= me.top_role:
            return "Роль участника выше моей — подними роль бота в настройках сервера."
        return None

    # --------------------------------- команды ---------------------------------

    @app_commands.command(name="kick", description="Выгнать участника (сможет вернуться по инвайту).")
    @app_commands.describe(member="Кого выгнать", reason="Причина (попадёт в лог и в ЛС)")
    @app_commands.checks.has_permissions(kick_members=True)
    @app_commands.checks.bot_has_permissions(kick_members=True)
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: str = "—") -> None:
        if err := self._guard(interaction, member):
            return await interaction.response.send_message(err, ephemeral=True)
        await self._dm(member, interaction.guild.name, "кик", reason)
        await member.kick(reason=f"{interaction.user}: {reason}")
        await interaction.response.send_message(f"👢 {member} выгнан. Причина: {reason}")
        await self._log_action(interaction, "kick", member, reason)

    @app_commands.command(name="ban", description="Забанить участника.")
    @app_commands.describe(
        member="Кого забанить",
        reason="Причина",
        delete_days="Удалить сообщения за N последних дней (0–7)",
    )
    @app_commands.checks.has_permissions(ban_members=True)
    @app_commands.checks.bot_has_permissions(ban_members=True)
    async def ban(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        reason: str = "—",
        delete_days: app_commands.Range[int, 0, 7] = 0,
    ) -> None:
        if err := self._guard(interaction, member):
            return await interaction.response.send_message(err, ephemeral=True)
        await self._dm(member, interaction.guild.name, "бан", reason)
        await member.ban(
            reason=f"{interaction.user}: {reason}",
            delete_message_seconds=delete_days * 86400,
        )
        await interaction.response.send_message(f"🔨 {member} забанен. Причина: {reason}")
        await self._log_action(interaction, "ban", member, reason,
                               extra=f"чистка сообщений: {delete_days} дн.")

    @app_commands.command(name="unban", description="Разбанить по ID пользователя.")
    @app_commands.describe(user_id="ID пользователя (18–19 цифр)", reason="Причина")
    @app_commands.checks.has_permissions(ban_members=True)
    @app_commands.checks.bot_has_permissions(ban_members=True)
    async def unban(self, interaction: discord.Interaction, user_id: str, reason: str = "—") -> None:
        if not user_id.isdigit():
            return await interaction.response.send_message("ID — это только цифры.", ephemeral=True)
        try:
            user = await self.bot.fetch_user(int(user_id))
            await interaction.guild.unban(user, reason=f"{interaction.user}: {reason}")
        except discord.NotFound:
            return await interaction.response.send_message("Такого бана нет.", ephemeral=True)
        await interaction.response.send_message(f"♻️ {user} разбанен. Причина: {reason}")
        await self._log_action(interaction, "unban", user, reason)

    @app_commands.command(name="timeout", description="Тайм-аут (мут): участник молчит заданное время.")
    @app_commands.describe(
        member="Кому",
        duration="Длительность: 10m, 1h, 1h30m, 2d (макс 28 дней)",
        reason="Причина",
    )
    @app_commands.checks.has_permissions(moderate_members=True)
    @app_commands.checks.bot_has_permissions(moderate_members=True)
    async def timeout(
        self, interaction: discord.Interaction, member: discord.Member, duration: str, reason: str = "—"
    ) -> None:
        if err := self._guard(interaction, member):
            return await interaction.response.send_message(err, ephemeral=True)
        delta = parse_duration(duration)
        if delta is None:
            return await interaction.response.send_message(
                "Не понял длительность. Формат: `10m`, `1h`, `1h30m`, `2d`.", ephemeral=True
            )
        if delta > MAX_TIMEOUT:
            return await interaction.response.send_message("Максимум — 28 дней.", ephemeral=True)
        await member.timeout(delta, reason=f"{interaction.user}: {reason}")
        await self._dm(member, interaction.guild.name, f"тайм-аут на {duration}", reason)
        await interaction.response.send_message(f"🔇 {member} в тайм-ауте на {duration}. Причина: {reason}")
        await self._log_action(interaction, "timeout", member, reason, extra=f"длительность: {duration}")

    @app_commands.command(name="untimeout", description="Снять тайм-аут досрочно.")
    @app_commands.describe(member="Кому снять", reason="Причина")
    @app_commands.checks.has_permissions(moderate_members=True)
    @app_commands.checks.bot_has_permissions(moderate_members=True)
    async def untimeout(self, interaction: discord.Interaction, member: discord.Member, reason: str = "—") -> None:
        if member.timed_out_until is None:
            return await interaction.response.send_message("Участник не в тайм-ауте.", ephemeral=True)
        await member.timeout(None, reason=f"{interaction.user}: {reason}")
        await interaction.response.send_message(f"🔊 С {member} снят тайм-аут.")
        await self._log_action(interaction, "untimeout", member, reason)

    @app_commands.command(name="warn", description="Выдать предупреждение (копится в истории).")
    @app_commands.describe(member="Кому", reason="За что")
    @app_commands.checks.has_permissions(moderate_members=True)
    async def warn(self, interaction: discord.Interaction, member: discord.Member, reason: str) -> None:
        if err := self._guard(interaction, member):
            return await interaction.response.send_message(err, ephemeral=True)
        key = self._key(interaction.guild.id, member.id)
        entry = {
            "reason": reason,
            "moderator": str(interaction.user),
            "at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        }
        self.warns.setdefault(key, []).append(entry)
        _save_warns(self.warns)
        count = len(self.warns[key])
        await self._dm(member, interaction.guild.name, f"предупреждение (#{count})", reason)
        await interaction.response.send_message(f"⚠️ {member} получил предупреждение (#{count}). Причина: {reason}")
        await self._log_action(interaction, "warn", member, reason, extra=f"всего: {count}")

    @app_commands.command(name="warnings", description="Показать предупреждения участника.")
    @app_commands.describe(member="Чьи смотреть")
    @app_commands.checks.has_permissions(moderate_members=True)
    async def warnings(self, interaction: discord.Interaction, member: discord.Member) -> None:
        items = self.warns.get(self._key(interaction.guild.id, member.id), [])
        if not items:
            return await interaction.response.send_message(f"У {member} нет предупреждений.", ephemeral=True)
        embed = discord.Embed(
            title=f"Предупреждения · {member}",
            description=f"Всего: {len(items)}",
            color=discord.Color.yellow(),
        )
        for i, w in enumerate(items[-20:], 1):  # последние 20
            embed.add_field(
                name=f"#{i} · {w['at']}",
                value=f"{w['reason']} — _{w['moderator']}_",
                inline=False,
            )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="clearwarnings", description="Обнулить предупреждения участника.")
    @app_commands.describe(member="Кому обнулить")
    @app_commands.checks.has_permissions(moderate_members=True)
    async def clearwarnings(self, interaction: discord.Interaction, member: discord.Member) -> None:
        key = self._key(interaction.guild.id, member.id)
        if self.warns.pop(key, None) is None:
            return await interaction.response.send_message("У участника и так пусто.", ephemeral=True)
        _save_warns(self.warns)
        await interaction.response.send_message(f"🧹 Предупреждения {member} обнулены.")
        await self._log_action(interaction, "warn", member, "обнуление истории", extra="clearwarnings")

    @app_commands.command(name="purge", description="Удалить последние N сообщений в этом канале (1–100).")
    @app_commands.describe(amount="Сколько сообщений удалить", member="(опц.) только этого автора")
    @app_commands.checks.has_permissions(manage_messages=True)
    @app_commands.checks.bot_has_permissions(manage_messages=True)
    async def purge(
        self,
        interaction: discord.Interaction,
        amount: app_commands.Range[int, 1, 100],
        member: discord.Member | None = None,
    ) -> None:
        await interaction.response.defer(ephemeral=True)
        check = (lambda m: m.author.id == member.id) if member else None
        deleted = await interaction.channel.purge(limit=amount, check=check)
        who = f" от {member}" if member else ""
        await interaction.followup.send(f"🧽 Удалено {len(deleted)} сообщений{who}.", ephemeral=True)
        await self._log_action(interaction, "purge", interaction.user, "чистка канала",
                               extra=f"#{interaction.channel.name}: {len(deleted)} сообщ.{who}")

    @app_commands.command(name="slowmode", description="Медленный режим в канале (0 = выключить).")
    @app_commands.describe(seconds="Задержка между сообщениями, сек (0–21600)")
    @app_commands.checks.has_permissions(manage_channels=True)
    @app_commands.checks.bot_has_permissions(manage_channels=True)
    async def slowmode(
        self, interaction: discord.Interaction, seconds: app_commands.Range[int, 0, 21600]
    ) -> None:
        await interaction.channel.edit(slowmode_delay=seconds)
        state = "выключен" if seconds == 0 else f"{seconds} сек"
        await interaction.response.send_message(f"🐢 Медленный режим: {state}.")

    @app_commands.command(name="help", description="Список команд модерации.")
    async def help_cmd(self, interaction: discord.Interaction) -> None:
        embed = discord.Embed(title="mod-bot · команды", color=discord.Color.blurple())
        rows = [
            ("/kick", "выгнать участника"),
            ("/ban · /unban", "бан / разбан по ID"),
            ("/timeout · /untimeout", "мут на время / снять"),
            ("/warn · /warnings · /clearwarnings", "предупреждения"),
            ("/purge", "удалить N последних сообщений"),
            ("/slowmode", "медленный режим канала"),
        ]
        for name, desc in rows:
            embed.add_field(name=name, value=desc, inline=False)
        embed.set_footer(text="Каждая команда требует соответствующих прав Discord.")
        await interaction.response.send_message(embed=embed, ephemeral=True)

    # ------------------------------ обработка ошибок ------------------------------

    async def cog_app_command_error(
        self, interaction: discord.Interaction, error: app_commands.AppCommandError
    ) -> None:
        if isinstance(error, app_commands.MissingPermissions):
            msg = "У тебя нет нужных прав для этой команды."
        elif isinstance(error, app_commands.BotMissingPermissions):
            perms = ", ".join(error.missing_permissions)
            msg = f"У бота не хватает прав: {perms}. Проверь роль бота."
        else:
            log.exception("Ошибка команды: %s", error)
            msg = "Что-то пошло не так при выполнении команды."
        if interaction.response.is_done():
            await interaction.followup.send(msg, ephemeral=True)
        else:
            await interaction.response.send_message(msg, ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Moderation(bot))

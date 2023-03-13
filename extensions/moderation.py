import hikari
import lightbulb
from datetime import timedelta, timezone, datetime


mod = lightbulb.Plugin("mod")


@mod.command
@lightbulb.add_checks(
    lightbulb.has_guild_permissions(hikari.Permissions.MANAGE_MESSAGES),
    lightbulb.bot_has_guild_permissions(hikari.Permissions.MANAGE_MESSAGES)
)
@lightbulb.option("amount", "How many messages should I delete?", type = int, required = True)
@lightbulb.command("clear", "Delete some messages")
@lightbulb.implements(lightbulb.SlashCommand)
async def clear(ctx: lightbulb.Context):
    amount = ctx.options.amount
    channel = ctx.channel_id
    msgs = await ctx.bot.rest.fetch_messages(channel).limit(amount)
    await ctx.bot.rest.delete_messages(channel, msgs)




@mod.command
@lightbulb.add_checks(
    lightbulb.has_guild_permissions(hikari.Permissions.KICK_MEMBERS),
    lightbulb.bot_has_guild_permissions(hikari.Permissions.KICK_MEMBERS)
)
@lightbulb.option("user", "Who should I kick?", type = hikari.Member, required = True)
@lightbulb.option("reason", "Why would you like to kick this user?", type = str, required = False)
@lightbulb.command("kick", "Kick an user!")
@lightbulb.implements(lightbulb.SlashCommand)
async def kick(ctx: lightbulb.Context):
    embed = hikari.Embed(title = "Success!")
    embed.add_field(name = f"You kicked {ctx.options.user}", value = f"Reason: {ctx.options.reason}")
    embed.set_footer(text = f"Requested by: {ctx.author}", icon = ctx.author.avatar_url)
    gid = ctx.guild_id
    await ctx.bot.rest.kick_member(user = ctx.options.user, guild = gid)
    await ctx.respond(embed=embed)



@mod.command
@lightbulb.add_checks(
    lightbulb.has_guild_permissions(hikari.Permissions.BAN_MEMBERS),
    lightbulb.bot_has_guild_permissions(hikari.Permissions.BAN_MEMBERS)
)
@lightbulb.option("user", "Who should I ban?", type = hikari.Member, required = True)
@lightbulb.option("reason", "Why would you like to ban this user?", type = str, required = False)
@lightbulb.command("ban", "Ban an user!")
@lightbulb.implements(lightbulb.SlashCommand)
async def ban(ctx: lightbulb.Context):
    embed = hikari.Embed(title = "Ban successful!")
    embed.add_field(name = f"You banned {ctx.options.user}", value = f"Reason: {ctx.options.reason}")
    embed.set_footer(text = f"Requested by: {ctx.author}", icon = ctx.author.avatar_url)
    gid = ctx.guild_id
    await ctx.bot.rest.ban_member(user = ctx.options.user, guild = gid)
    await ctx.respond(embed=embed)


@mod.command
@lightbulb.add_checks(
    lightbulb.has_guild_permissions(hikari.Permissions.MODERATE_MEMBERS),
    lightbulb.bot_has_guild_permissions(hikari.Permissions.MODERATE_MEMBERS)
)
@lightbulb.option("days", "Duration of the timeout in days", type=int, default=0)
@lightbulb.option("hours", "Duration of the timeout in hours", type=int, default=0)
@lightbulb.option("minutes", "Duration of the timeout in minutes", type=int, default=0)
@lightbulb.option("seconds", "Duration of the timeout in seconds", type=int, default=0)
@lightbulb.option("member", "Which user should recieve the timeout?", type=hikari.Member, required=True)
@lightbulb.command("timeout", "Timeout a member!")
@lightbulb.implements(lightbulb.SlashCommand)
async def timeout(ctx: lightbulb.Context):
    member = ctx.options.member
    now = datetime.now(timezone.utc)
    then = now + timedelta(days=ctx.options.days, hours=ctx.options.hours, minutes=ctx.options.minutes, seconds=ctx.options.seconds)
    if (then - now).days > 28:
        await ctx.respond("You can't time someone out for more than 28 days", flags=hikari.MessageFlag.EPHEMERAL)
        return
    elif (then - now).days < 28:
        embed = hikari.Embed(title="Timeout successful!", description=f"{ctx.options.member} is now muted for {ctx.options.days} days, {ctx.options.minutes} minutes and {ctx.options.seconds} seconds")
        embed.set_footer(text = f"Requested by: {ctx.author}", icon = ctx.author.avatar_url)
        await ctx.bot.rest.edit_member(user=member, guild=ctx.guild_id, communication_disabled_until=then)
        await ctx.respond(embed=embed)


def load(bot):
    bot.add_plugin(mod)
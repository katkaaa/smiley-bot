import hikari
import lightbulb
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("token")
intents = hikari.Intents.ALL # Edit this based on what intents you have set in your developer portal
bot = lightbulb.BotApp(token = token, prefix="s!", intents=intents, help_class=None)

@bot.command
@lightbulb.command("help", "The epic help message")
@lightbulb.implements(lightbulb.SlashCommand)
async def help_message(ctx : lightbulb.Context):
    embed = hikari.Embed(title = "Here to help!")
    embed.add_field(name="Fun", value="`meme`\n`kitty`")
    embed.add_field(name="Misc", value="`ping`\n`apis`")
    embed.add_field(name="**Source code**", value="**Check out the source code on [Github!](https://github.com/katkaaa/smiley-bot)**")
    await ctx.respond(embed)


@bot.command
@lightbulb.command("ping", "Checks the bot's latency")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping_command(ctx: lightbulb.Context):
      embed = hikari.Embed(title = "Pong! :ping_pong:", description = f"{bot.heartbeat_latency * 1000:.0f}ms")
      await ctx.respond(embed=embed)


@bot.command
@lightbulb.command("apis", "I wonder what apis does this bot use!")
@lightbulb.implements(lightbulb.SlashCommand)
async def api_list(ctx: lightbulb.Context):
      embed = hikari.Embed(title="**API List**", description="Cat as a service - *https://cataas.com/* \nMeme API - *https://github.com/D3vd/Meme_Api*")
      await ctx.respond(embed=embed)


for filename in os.listdir("./extensions"):
    if filename.endswith(".py"):
        bot.load_extensions(f"extensions.{filename[:-3]}")

bot.run(activity = hikari.Activity(name = "/help", type = 3))
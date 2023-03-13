import hikari
import lightbulb
import aiohttp
import json

fun = lightbulb.Plugin("fun")

@fun.command
@lightbulb.command("kitty", "Awww 🥰 ")
@lightbulb.implements(lightbulb.SlashCommand)
async def kitty(ctx : lightbulb.Context):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://cataas.com/cat?json=true") as cat:
            jsonvalue = await cat.json()
            cat_img = jsonvalue["url"]
            embed = hikari.Embed(title="A kitty pic for you! <3").set_image(f"https://cataas.com/{cat_img}").set_footer(f"Powered by Cataas")
            await ctx.respond(embed=embed)

@fun.command
@lightbulb.command("meme", "The big funny")
@lightbulb.implements(lightbulb.SlashCommand)
async def meme(ctx : lightbulb.Context):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://meme-api.com/gimme/1") as meme:
            jsonvalue = await meme.json()
            image = jsonvalue["memes"][0]["url"]
            subreddit = jsonvalue["memes"][0]["subreddit"]
            author = jsonvalue["memes"][0]["author"]
            title = jsonvalue["memes"][0]["title"]
            embed = hikari.Embed(title = f"{title}").set_image(image).set_footer(text = f"r/{subreddit} - u/{author} | Powered by meme-api")
            await ctx.respond(embed = embed)


def load(bot):
    bot.add_plugin(fun)
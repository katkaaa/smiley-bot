# Smiley

Smiley is a multipurpose discord bot, written using hikari-lightbulb.
This is a rewrite of the old version, the old repo is now privated.

Invite Smiley into your server [here!](https://discord.com/api/oauth2/authorize?client_id=892396707608932353&permissions=1099511639046&scope=bot%20applications.commands)

Join the support server [here!](https://discord.gg/87WDjkd6J5)

## Commands

This bot only has a few commands, but I'm planning on adding more.

The help command for this bot:

-  `/help`

Fun commands:

-  `/kitty` - Sends an image of a kitty :3

-  `/meme` - The big funny 

Moderation commands:

-  `/clear` - Takes in the number of messages to delete

-  `/timeout` - Takes in the duration in days, hours, minutes and seconds.

-  `/kick` - Kicks an user

-  `/ban` - Bans an user

## How to use
 - Install the packages from requirements.txt (``pip install -R requirements.txt``)
 - Set up an .env with your token, edit the intents based on what you have checked out in your developer portal
 - In CMD type ``cd <the directory where you cloned this repo>``, then type ``py main.py`` to start the bot
 - You may want to add your own commands, so here's a very simple example (even though you could just take a look at one of the extensions):
 ```py
 import hikari
 import lightbulb

extension = lightbulb.Plugin("extension")

@extension.command
@lightbulb.command("command", "command description")
@lightbulb.implements(lightbulb.SlashCommand) # Or lightbulb.PrefixCommand for a prefix command
async def myCommand(ctx : lightbulb.Context):
	reply = "This is a text reply"
	embed = hikari.Embed(title="This is the title", description="This is the description")
	embed.add_field(name="OMG a new field", value="OMG a description too?")
	embed.set_footer(text="Even a footer!!!!!!")
	await ctx.respond(reply, embed=embed)

def load(bot):
	bot.add_plugin(extension)
```

## Issues
If you come across any issues, submit an issue.
When submitting an issue, make sure to provide:
 - The code causing said issue and the error
 - Python and Hikari-lightbulb versions
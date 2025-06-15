from dotenv import dotenv_values
import discord
from discord.ext import commands


config = dotenv_values(".env") 

intents = discord.Intents.default()	# request bot roots
intents.message_content = True
bot = commands.Bot(command_prefix = "%", intents = intents)

@bot.event
# when the bot active successfully
async def on_ready():
    print(f"currently username --> {bot.user}")

@bot.command()
# hello world
async def Hello(ctx):
    await ctx.send("Hello, world!")


bot.run(config['DISCORD-SERVER-TOKEN'])

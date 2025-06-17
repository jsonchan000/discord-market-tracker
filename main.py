from dotenv import dotenv_values, load_dotenv
import discord
from discord.ext import commands
import os

from modules.market import get_realtime_price_change 

load_dotenv()
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

@bot.command()
# get news 
async def GetNews(ctx):
    # await ctx.send("Fetching news...")
    # price = get_latest_price('AAPL')
    # await ctx.send(price)
    await ctx.send("📈 Fetching stock prices...")

    # Read symbols from .env
    symbols_str = os.getenv("MARKET_INFO_LIST", "")
    symbols = [s.strip() for s in symbols_str.split(",") if s.strip()]

    # Collect prices
    results = []
    for symbol in symbols:
        price_info = get_realtime_price_change(symbol)
        results.append(price_info)

    response = "\n".join(results)
    await ctx.send(response)



bot.run(config['DISCORD_SERVER_TOKEN'])

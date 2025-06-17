# import requests


# # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
# r = requests.get(url)
# data = r.json()

# print(data)

# import requests

# API_KEY = 'TEYBETLDC7EU7I3W'
# symbol = 'VOO'

# url = 'https://www.alphavantage.co/query'
# params = {
#     'function': 'TIME_SERIES_DAILY',
#     'symbol': symbol,
#     'apikey': API_KEY
# }

# response = requests.get(url, params=params)
# data = response.json()

# daily_data = data.get("Time Series (Daily)", {})
# if daily_data:
#     latest_date = sorted(daily_data.keys(), reverse=True)[0]
#     closing_price = daily_data[latest_date]['4. close']
#     print(f"VOO closing price on {latest_date} was ${closing_price}")
# else:
#     print("No data available")



from dotenv import dotenv_values,load_dotenv
import discord
from discord.ext import commands
import os

from modules.market import get_latest_price

load_dotenv()  # <--- 把 .env 的值載入到 os.environ

config = dotenv_values(".env") 

# Read symbols from .env
symbols_str = os.getenv("MARKET_INFO_LIST", "")
print(symbols_str)
symbols = [s.strip() for s in symbols_str.split(",") if s.strip()]

# Collect prices
results = []
for symbol in symbols:
    price_info = get_latest_price(symbol)
    results.append(price_info)

response = "\n".join(results)
print(response)
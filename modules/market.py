import yfinance as yf
from datetime import datetime


# def get_latest_price(symbol):
#     ticker = yf.Ticker(symbol)
#     data = ticker.history(period="1d", interval="1m")

#     if not data.empty:
#         latest_time = data.index[-1]
#         latest_price = data['Close'].iloc[-1]
#         return f"✅ Latest {symbol} price at {latest_time} is ${latest_price:.2f}"
#     else:
#         print("No data yet — market may not be open.")



def get_realtime_price_change(symbol):
    """
    Fetch the current and previous close price for a stock symbol,
    then calculate the absolute and percentage change.

    Args:
        symbol (str): The stock symbol (e.g., "AAPL").

    Returns:
        tuple: (current_price, price_change, percent_change) or None if error.
    """
    ticker = yf.Ticker(symbol)

    try:
        previous_close = ticker.info["previousClose"]
        current_price = ticker.info["regularMarketPrice"]

        if previous_close is None or current_price is None:
            return f"Data not available for {symbol}"

        daily_change_pct = ((current_price - previous_close) / previous_close) * 100

        return {
            "symbol": symbol.upper(),
            "current_price": round(current_price, 2),
            "daily_change_pct": round(daily_change_pct, 2),
        }
    except Exception as e:
        return f"Error retrieving data for {symbol}: {e}"

# # example usage
# msg = get_realtime_price_change("ETH-USD")
# print(msg)


def get_stock_news(symbol):
    """
    Fetch the latest news articles for a given stock symbol using yfinance.

    Args:
        symbol (str): The stock ticker symbol (e.g., "AAPL").

    Returns:
        list: A list of dictionaries, each containing:
            - title (str): Title of the news article.
            - publisher (str): Name of the news provider.
            - published_on (str): Publication datetime in 'YYYY-MM-DD HH:MM:SS' format.
            - link (str): URL to the full news article.
        Returns an empty list if no news is available or an error occurs.
    """
    ticker = yf.Ticker(symbol)
    news_list = ticker.news
    formatted_news = []

    for article in news_list:
        try:
            content = article["content"]

            title = content["title"]
            publisher = content["provider"]["displayName"]
            pub_date_str = content["pubDate"]
            link = content["canonicalUrl"]["url"]

            pub_datetime = datetime.fromisoformat(pub_date_str.replace("Z", "+00:00"))

            formatted_news.append({
                "title": title,
                "publisher": publisher,
                "published_on": pub_datetime.strftime('%Y-%m-%d %H:%M:%S'),
                "link": link
            })
        except (KeyError, TypeError):
            continue  # skip articles with missing fields

    return formatted_news

# # example usage
# news = get_stock_news("AAPL")
# for article in news:
#     print(f"Title: {article['title']}")
#     print(f"Publisher: {article['publisher']}")
#     print(f"Published on: {article['published_on']}")
#     print(f"Link: {article['link']}\n")
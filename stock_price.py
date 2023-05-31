import requests

def get_stock_price(symbol, api_key):
    # Retrieve the stock price for the given symbol using the provided API key
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    price = data["Global Quote"]["05. price"]
    return price

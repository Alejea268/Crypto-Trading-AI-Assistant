import requests

def fetch_crypto_price(crypto_pair="BTC/USD"):
    """
    Fetch the current price of a cryptocurrency pair using a public API.
    Default pair: BTC/USD.
    """
    try:
        # Using a public crypto API (CoinGecko in this case)
        url = f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP response
        data = response.json()
        
        # Extract and print the price
        price = data["bitcoin"]["usd"]
        print(f"The current price of {crypto_pair} is ${price}")
        return price
    except Exception as e:
        print(f"Error fetching price data: {e}")
        return None

def analyze_price_trend(price_history):
    """
    Analyze price trends based on historical data.
    Input: price_history (list of past prices)
    Output: A basic trend analysis
    """
    if len(price_history) < 2:
        print("Not enough data to analyze trends.")
        return

    if price_history[-1] > price_history[-2]:
        print("The price trend is UP.")
    elif price_history[-1] < price_history[-2]:
        print("The price trend is DOWN.")
    else:
        print("The price is STABLE.")

# Example usage
if __name__ == "__main__":
    price_history = []
    
    # Fetch current price and analyze
    for _ in range(3):  # Simulate fetching data at different times
        price = fetch_crypto_price()
        if price:
            price_history.append(price)
        analyze_price_trend(price_history)

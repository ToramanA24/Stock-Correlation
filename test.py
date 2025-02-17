import requests
import pandas as pd
import numpy as np

# Step 1: Fetch Data from API
def fetch_data(symbol, days=5):
    # Replace with the actual API and API key
    api_url = f"https://api.example.com/{symbol}?days={days}&apikey=YOUR_API_KEY"
    response = requests.get(api_url)
    data = response.json()
    return pd.DataFrame(data['prices'])  # Adjust based on API response structure

# Step 2: Calculate Correlation
def calculate_correlation(index_data, stock_data):
    combined_data = pd.concat([index_data, stock_data], axis=1).dropna()
    return combined_data.corr().iloc[0, 1]  # Correlation between the two columns

# Step 3: Find Top 3 Correlated Stocks
def find_top_correlated_stocks(index_symbol, stock_symbols):
    index_data = fetch_data(index_symbol)
    correlations = {}
    for stock in stock_symbols:
        stock_data = fetch_data(stock)
        correlations[stock] = calculate_correlation(index_data['close'], stock_data['close'])
    top_3 = sorted(correlations, key=correlations.get, reverse=True)[:3]
    return [(stock, correlations[stock]) for stock in top_3]

# Main Execution
if __name__ == "__main__":
    index_symbol = "BIST100"
    stock_symbols = ["STOCK1", "STOCK2", "STOCK3", "STOCK4", "STOCK5"]  # Add all stock symbols
    top_3_stocks = find_top_correlated_stocks(index_symbol, stock_symbols)
    print("Top 3 Correlated Stocks:")
    for stock, corr in top_3_stocks:
        print(f"{stock}: {corr:.2f}")
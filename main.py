import yfinance as yf
import pandas as pd
import numpy as np

# Step 1: Fetch Data using yfinance
def fetch_data(symbol, days=365):
    """
    Fetch historical stock data using yfinance.
    :param symbol: Stock ticker symbol (e.g., "AAPL").
    :param days: Number of past days to fetch data for.
    :return: DataFrame with historical stock data.
    """
    # Calculate the start date based on the number of days
    end_date = pd.Timestamp.today()
    start_date = end_date - pd.Timedelta(days=days)
    
    # Fetch data using yfinance
    data = yf.download(symbol, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
    
    # Ensure the 'close' column exists and return the DataFrame
    if 'Close' in data.columns:
        data = data.rename(columns={'Close': 'close'})  # Rename 'Close' to 'close' for consistency
    return data

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
    top_5 = sorted(correlations, key=correlations.get, reverse=True)[:5]
    return [(stock, correlations[stock]) for stock in top_5]

# Main Execution
if __name__ == "__main__":
    index_symbol = "XU100.IS"  # Example: BIST 100 index ticker on Yahoo Finance
    stock_symbols = ["TAVHL.IS",
                     "MGROS.IS",
                     "TURSG.IS",
                     "TTRAK.IS",
                     "KOZAL.IS",
                     "AGHOL.IS",
                     "ENJSA.IS",
                     "ISMEN.IS",
                     "MPARK.IS",
                     "CLEBI.IS",
                     "OTKAR.IS",
                     "EKGYO.IS",
                     "BRSAN.IS",
                     "BRYAT.IS",
                     "ANSGR.IS",
                     "CIMSA.IS",
                     "TABGD.IS",
                     "ULKER.IS",
                     "DOAS.IS",
                     "AKSA.IS",
                     "ANHYT.IS",
                     "PETKM.IS",
                     "SELEC.IS",
                     "AKSEN.IS",
                     "TKFEN.IS",
                     "DOHOL.IS",
                     "ALARK.IS",
                     "MAGEN.IS",
                     "TSKB.IS",
                     "KRDMD.IS",
                     "ENERY.IS",
                     "LIDER.IS",
                     "EGEEN.IS",
                     "KOZAA.IS",
                     "ECILC.IS",
                     "HEKTS.IS",
                     "KONYA.IS",
                     "MAVI.IS",
                     "PASEU.IS",
                     "KCAER.IS",
                     "EUPWR.IS",
                     "GESAN.IS",
                     "BTCIM.IS",
                     "SOKM.IS",
                     "SMRTG.IS",
                     "KONTR.IS",
                     "YEOTK.IS",
                     "MIATK.IS",
                     "BSOKE.IS",
                     "AKFYE.IS",
                     "NTHOL.IS",
                     "CWENE.IS",
                     "ALFAS.IS",
                     "VESTL.IS",
                     "ZOREN.IS",
                     "KLSER.IS",
                     "CVKMD.IS",
                     "SDTTR.IS",
                     "REEDR.IS",
                     "FENER.IS",
                     "TMSN.IS",
                     "AGROT.IS",
                     "BERA.IS",
                     "SKBNK.IS",
                     "CANTE.IS",
                     "KARSN.IS",
                     "TUKAS.IS",
                     "GOLTS.IS",
                     "ODAS.IS",
                     "TSPOR.IS",
                     "ARDYZ.IS",
                     "IEYHO.IS",
                     "ALTNY.IS",
                     ]  # Replace with your stock symbols
    top_5_stocks = find_top_correlated_stocks(index_symbol, stock_symbols)
    print("Top 5 Correlated Stocks:")
    for stock, corr in top_5_stocks:
        print(f"{stock}: {corr:.2f}")
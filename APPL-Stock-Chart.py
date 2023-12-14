import pandas as pd
import requests
import matplotlib.pyplot as plt
from datetime import datetime

def fetch_stock_data(symbol):
    # Fetching stock data from a public API
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey=YOUR_API_KEY&outputsize=compact'
    response = requests.get(url)
    data = response.json()

    # Converting data to a pandas DataFrame
    df = pd.DataFrame(data['Time Series (Daily)']).T
    df = df.rename(columns={
        '1. open': 'Open',
        '2. high': 'High',
        '3. low': 'Low',
        '4. close': 'Close',
        '5. volume': 'Volume'
    })
    df = df.apply(pd.to_numeric)
    df.index = pd.to_datetime(df.index)

    return df

def plot_moving_average(df, symbol, window=20):
    # Calculate the moving average
    df['Moving Average'] = df['Close'].rolling(window=window).mean()

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(df['Close'], label='Close Price')
    plt.plot(df['Moving Average'], label='Moving Average')
    plt.title(f'{symbol} Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.show()

# Fetch stock data
symbol = 'AAPL'  # Example stock symbol
df_stock = fetch_stock_data(symbol)

# Plot moving average
plot_moving_average(df_stock, symbol)

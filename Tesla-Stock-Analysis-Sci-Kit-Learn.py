import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import yfinance as yf

# Fetch historical stock data for Tesla (TSLA)
ticker = 'TSLA'
start_date = '2010-01-01'
end_date = '2025-12-01'  # Adjusted to a realistic end date
data = yf.download(ticker, start=start_date, end=end_date)

# Check if data was fetched successfully
if data.empty:
    raise ValueError("No data fetched. Check the ticker or date range.")

# Prepare the data
data.reset_index(inplace=True)           # Convert the index to a column (Date)
data['Date'] = pd.to_datetime(data['Date'])
# Create a numeric feature representing the number of days from the start date
data['Days'] = (data['Date'] - data['Date'].min()).dt.days
X = data[['Days']]
y = data['Close']

# Split the data into training and testing sets (80/20 split)
train_size = int(len(X) * 0.8)
X_train, X_test = X.iloc[:train_size], X.iloc[train_size:]
y_train, y_test = y.iloc[:train_size], y.iloc[train_size:]

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the stock price 12 months (365 days) from the last date in the dataset
future_days = 365
last_day = X['Days'].max()
future_day = np.array([[last_day + future_days]])
predicted_price = model.predict(future_day)

# Extract the scalar prediction from the array (in case it's 2D)
predicted_price_scalar = predicted_price.item()

# Calculate the prediction date
prediction_date = data['Date'].max() + pd.Timedelta(days=future_days)

print(f"Predicted Tesla stock price on {prediction_date.date()}: ${predicted_price_scalar:.2f}")

# Plot the results
plt.figure(figsize=(10, 6))
plt.scatter(data['Date'], y, color='blue', label='Actual Prices')
plt.plot(data['Date'], model.predict(X), color='red', label='Fitted Line')
# Mark the predicted date on the plot
plt.axvline(x=prediction_date, color='green', linestyle='--', label='Prediction Date')
plt.scatter(prediction_date, predicted_price_scalar, color='black', label='Predicted Price')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('Tesla Stock Price Prediction using Linear Regression')
plt.legend()
plt.xticks(rotation=45)
# Extend the x-axis to ensure the predicted date is visible
plt.xlim([data['Date'].min(), prediction_date + pd.Timedelta(days=30)])
plt.tight_layout()
plt.show()

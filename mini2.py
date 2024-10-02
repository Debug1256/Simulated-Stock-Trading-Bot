import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Simulated historical stock data (date, price)
# Let's create a dataset of 30 days of stock prices
start_date = datetime(2023, 1, 1)
historical_data = [
    (start_date + timedelta(days=i), round(np.random.uniform(100, 200), 2))
    for i in range(30)
]

# Parameters for the trading bot
N = 5  # Days to calculate average momentum
initial_cash = 1000  # Starting cash
shares_owned = 0  # Number of shares owned
portfolio_value_history = []  # To track portfolio value over time

# Trading simulation
for i in range(len(historical_data)):
    current_date, current_price = historical_data[i]

    # Calculate average price of the last N days
    if i >= N:
        last_n_prices = [price for _, price in historical_data[i-N:i]]
        average_price = np.mean(last_n_prices)
    else:
        average_price = current_price  # If not enough data, use current price

    # Calculate momentum
    momentum = current_price - average_price

    # Make trading decisions
    if momentum > 0 and shares_owned == 0:  # Buy condition
        shares_owned = initial_cash // current_price  # Buy as many shares as possible
        initial_cash -= shares_owned * current_price
        print(f"{current_date.date()}: Buying {shares_owned} shares at ${current_price}")
    elif momentum < 0 < shares_owned:  # Sell condition
        initial_cash += shares_owned * current_price  # Sell all shares
        print(f"{current_date.date()}: Selling {shares_owned} shares at ${current_price}")
        shares_owned = 0

    # Calculate current portfolio value
    current_portfolio_value = initial_cash + (shares_owned * current_price)
    portfolio_value_history.append(current_portfolio_value)

# Final evaluation
final_portfolio_value = initial_cash + (shares_owned * historical_data[-1][1])
print(f"\nFinal Portfolio Value: ${final_portfolio_value:.2f}")
print(f"Initial Cash: ${1000:.2f}")
print(f"Profit/Loss: ${final_portfolio_value - 1000:.2f}")

# Plotting portfolio value over time
plt.figure(figsize=(12, 6))
plt.plot([date for date, _ in historical_data], portfolio_value_history, label='Portfolio Value', marker='o')
plt.title('Portfolio Value Over Time')
plt.xlabel('Date')
plt.ylabel('Portfolio Value ($)')
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()


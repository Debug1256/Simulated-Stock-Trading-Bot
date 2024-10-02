#3 Modules (pandas)
#Question: Use the pandas library to load a CSV file containing historical trading data and calculate the daily percentage change of closing prices over a period of time.

import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('historical_data.csv')

# Display the first few rows of the DataFrame to understand the structure
print(df.head())

# Calculate the daily percentage change of the 'Close' column
df['Daily Percentage Change'] = df['Close'].pct_change() * 100

# Display the updated DataFrame with the percentage change column
print(df[['Date', 'Close', 'Daily Percentage Change']].head())

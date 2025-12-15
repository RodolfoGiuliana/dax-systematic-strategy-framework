# First, import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf  # Common library for downloading stock data

# Download DAX data
g = yf.download('^GDAXI', start='2010-01-01')  # Adjust date range as needed

# Calculate log returns and volatility
# Changed variable name from ^GDAXI to dax to avoid syntax error
dax = g  # Assign the downloaded data to a valid variable name
dax['Log_Ret'] = np.log(dax['Close'] / dax['Close'].shift(1))
dax['Volatility'] = dax['Log_Ret'].rolling(window=252).std() * np.sqrt(252)

# Plot the data
%matplotlib inline
dax[['Close', 'Volatility']].plot(subplots=True, color='blue',
                                  figsize=(8, 6), grid=True)
# tag: DAX
# title: Dax

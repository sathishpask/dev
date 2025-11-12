import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate a synthetic time series dataset with a clear seasonal component
np.random.seed(42)
date_today = pd.to_datetime('2023-01-01')
days = pd.date_range(date_today, date_today + pd.to_timedelta(364, unit='D'), freq='D')

# Creating a seasonal component (weekly cycle)
seasonal_component = np.sin(2 * np.pi * np.arange(len(days)) / 365 * 7)

# Generating synthetic data with trend and seasonal components
trend_component = np.cumsum(np.random.randn(len(days)))
values = trend_component + 10 * seasonal_component
df = pd.DataFrame({'Date': days, 'Value': values})

# Plot the original time series data
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Value'], label='Original Data')
plt.title('Original Time Series Data with Seasonal Component')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()

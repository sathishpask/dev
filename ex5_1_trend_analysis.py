import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate a synthetic time series dataset
np.random.seed(42)
date_today = pd.to_datetime('2023-01-01')
days = pd.date_range(date_today, date_today + pd.to_timedelta(364, unit='D'),
                     freq='D')
values = np.cumsum(np.random.randn(len(days)))
df = pd.DataFrame({'Date': days, 'Value': values})

# Plot the original time series data
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Value'], label='Original Data')
plt.title('Original Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()

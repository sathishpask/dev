import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Generate a synthetic time series dataset
np.random.seed(42)
date_today = datetime.now()
# Corrected date range generation
days = pd.date_range(date_today, date_today + timedelta(days=9), freq='D')
data = {'Date': days, 'Value': np.random.randint(10, 100, size=(len(days)))} 
df = pd.DataFrame(data)

# Display the dataset
print("Time Series Dataset (First 5 Rows):")
print(df.head())

# Visualize the time series data
plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='Value', data=df)
plt.title('Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()

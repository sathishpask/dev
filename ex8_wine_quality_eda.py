import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Wine Quality dataset (White Wine Quality)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
# CORRECTED: Wine dataset uses ';' as a separator
wine_data = pd.read_csv(url, sep=';') 

# Display the first few rows of the dataset
print("First Few Rows:")
print(wine_data.head())

# Summary statistics
print("\nSummary Statistics:")
print(wine_data.describe())

# Distribution of Wine Quality
plt.figure(figsize=(8, 5))
sns.countplot(x='quality', data=wine_data)
plt.title('Distribution of Wine Quality')
plt.show()

# Correlation heatmap
correlation_matrix = wine_data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

# Pairplot for selected features
# CORRECTED feature names to match the dataset columns
selected_features = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'quality']
sns.pairplot(wine_data[selected_features], hue='quality', markers=['o'])
plt.suptitle('Pairplot of Selected Features by Quality', y=1.02)
plt.show()

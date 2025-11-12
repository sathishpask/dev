import pandas as pd

# Load a sample dataset (e.g., Iris dataset)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
df = pd.read_csv(url, header=None, names=column_names)

# Display the first few rows of the dataset (from Ex 4.0 & 4.1)
print("First Few Rows of the Dataset:")
print(df.head())

# Display basic information about the dataset (from Ex 4.1)
print("\nDataset Information:")
print(df.info())

# Display summary statistics (from Ex 4.1)
print("\nSummary Statistics:")
print(df.describe())

# Display unique classes in the 'class' column (from Ex 4.1)
print("\nUnique Classes:")
print(df['class'].unique())

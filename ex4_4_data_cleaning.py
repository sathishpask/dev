import pandas as pd

# Sample data with missing values and duplicates
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Alice'], 
        'Age': [20, None, 21, 23, 22], 
        'Grade': [85, 92, 78, 95, 92]}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# 1. Handle Missing Values (Impute with mean for 'Age')
df['Age'].fillna(df['Age'].mean(), inplace=True)
print("\nDataFrame after Imputing Missing 'Age' with Mean:")
print(df)

# 2. Handle Duplicates (Drop duplicates)
df_cleaned = df.drop_duplicates(keep='first')
print("\nDataFrame after Dropping Duplicates:")
print(df_cleaned)

print("\nMissing Values (Final Check):")
print(df_cleaned.isnull().sum())

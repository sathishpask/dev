import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 
        'Age': [25, 30, 22], 
        'City': ['NewYork', 'SanFrancisco', 'Los Angeles']}
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Filter specific variables (columns)
selected_columns = ['Name', 'City']
filtered_df = df[selected_columns]

# Display the filtered DataFrame
print("\nFiltered DataFrame:")
print(filtered_df)

import pandas as pd

# Sample data
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 
        'Age': [20, 22, 21, 23], 
        'Grade': [85, 92, 78, 95]}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Applying a row filter (e.g., filter for people with Grade > 80)
grade_filter = df['Grade'] > 80
filtered_rows_df = df[grade_filter]

print("\nFiltered DataFrame (Grade > 80):")
print(filtered_rows_df)

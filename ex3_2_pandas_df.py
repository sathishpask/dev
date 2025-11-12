import pandas as pd

# Creating a Pandas DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'], 
        'Age': [25, 30, 22, 35, 28],
        'City': ['New York', 'SanFrancisco', 'LosAngeles', 'Chicago', 'Boston']}
df = pd.DataFrame(data)

# Displaying the DataFrame
print("Original DataFrame:")
print(df)

# Basic DataFrame operations
average_age = df['Age'].mean()
# Corrected syntax for filtering
youngest_person = df[df['Age'] == df['Age'].min()] 

# Displaying results of operations
print("\nAverage Age:", average_age)
print("\nYoungest Person:")
print(youngest_person)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# NOTE: This program assumes a file named 'college_students.csv' exists in the same directory.
# The contents of that CSV are provided in the manual's text block.
try:
    df = pd.read_csv('college_students.csv')
except FileNotFoundError:
    print("Error: 'college_students.csv' not found. Please create the file with the sample data.")
    # Fallback to create DataFrame directly from string for completeness
    import io
    csv_data = """Age,Gender,GPA,StudyHours,Grade
24,Female,2.76,24,A
21,Male,2.53,25,D
22,Male,3.24,14,D
24,Female,2.77,12,F
20,Female,3.05,21,B
22,Female,3.62,29,F
22,Female,3.58,13,B
24,Female,2.96,25,F
19,Female,3.31,16,C
20,Female,3.26,22,C
24,Female,3.45,19,C
20,Male,2.88,16,C
20,Female,3.38,23,A
22,Female,3.97,14,C
21,Male,3.23,12,D
20,Female,3.86,20,D
23,Male,3.15,20,A
22,Male,3.03,27,C
19,Female,3.47,24,C
21,Male,3.5,21,C
23,Male,3.8,18,F
23,Male,2.85,19,B
19,Male,3.25,21,F
21,Female,3.36,26,B
22,Male,3.65,15,C
18,Female,2.57,16,C
21,Male,3.99,23,F
19,Male,3.2,22,F
23,Male,2.92,17,B
22,Male,3.83,19,D
21,Female,3.62,18,B
18,Female,3.93,27,F
18,Male,3.0,11,F
20,Male,3.33,14,A
20,Female,3.36,14,F
24,Male,3.97,15,A
19,Male,2.61,28,D
21,Male,2.96,17,B
21,Female,2.79,25,B
24,Female,2.9,22,A
23,Female,3.23,10,B
23,Male,3.06,29,F
24,Male,3.09,26,C
23,Female,3.77,16,A
20,Female,3.9,22,B
21,Female,2.61,13,A
24,Female,2.81,13,A
21,Male,3.51,15,C
18,Female,3.04,28,F
20,Male,2.88,21,A
22,Female,2.94,16,B
20,Male,2.98,19,D
24,Female,3.77,28,A
22,Female,2.7,16,A
18,Female,3.56,12,C
24,Female,3.33,22,F
19,Male,2.94,22,D
21,Female,3.13,27,B
18,Male,2.88,29,D
21,Male,3.42,17,B
23,Male,2.62,18,F
19,Male,2.51,16,B
19,Female,3.44,10,C
18,Male,2.79,12,C
19,Male,2.61,22,C
22,Male,3.1,26,C
19,Female,2.58,10,D
21,Female,3.83,15,F
21,Female,2.54,15,B
24,Female,3.37,21,B
21,Male,3.16,22,C
24,Male,3.51,22,C
21,Female,2.99,24,A
22,Male,2.73,25,F
24,Male,3.97,20,D
20,Male,3.76,14,B
23,Female,3.79,13,A
18,Female,2.88,12,A
21,Male,2.56,28,B
19,Female,2.95,29,D
21,Female,3.31,27,A
19,Female,2.99,24,A
23,Female,3.74,18,F
23,Female,2.91,26,D
23,Male,3.95,23,A
19,Female,3.19,24,D
21,Male,3.76,10,B
23,Male,2.79,12,C
22,Female,3.12,25,A
24,Male,3.55,20,F
19,Male,2.71,21,B
19,Male,2.7,19,D
21,Female,3.95,25,B
19,Female,3.57,17,A
19,Male,2.56,15,D
23,Female,3.1,21,C
21,Female,3.15,17,B
23,Female,3.62,13,A
24,Female,2.88,17,F
24,Male,2.78,27,D
23,Male,2.62,14,B
24,Female,3.14,18,B
21,Female,3.53,13,C
18,Male,2.59,26,C
23,Male,3.87,18,F
22,Female,3.16,10,F
22,Male,2.86,29,A
19,Female,2.64,22,A
24,Female,2.77,25,F
22,Male,3.9,22,F
19,Male,3.46,23,D
18,Female,3.28,12,C
21,Female,3.49,15,A
21,Male,3.15,27,C
21,Female,3.6,28,C
22,Male,2.57,14,F
18,Female,3.35,24,D
22,Male,2.74,11,B
24,Male,2.68,19,D
22,Male,3.01,27,D
18,Female,2.64,22,C
18,Female,2.64,14,D
24,Male,2.97,10,A
18,Female,3.97,10,C
18,Male,2.76,27,A
21,Male,2.53,24,B
24,Female,3.65,26,C
20,Female,3.71,20,B
20,Male,3.02,26,C
18,Female,3.2,22,F
20,Female,3.47,10,D
20,Male,2.57,11,F
18,Male,3.92,18,B
20,Female,3.83,12,D
22,Male,2.89,10,C
19,Male,2.52,25,D
24,Female,3.9,15,A
19,Male,3.25,26,D
18,Male,3.31,14,A
21,Female,3.53,14,D
24,Female,3.42,15,A
18,Male,3.92,12,B
21,Male,3.92,14,F
19,Female,3.8,14,C
18,Female,3.45,19,D
24,Female,3.7,19,F
24,Female,3.52,28,C
23,Male,3.36,26,C
22,Female,2.69,23,A
20,Female,3.72,18,B
21,Male,3.73,23,B
23,Female,3.44,10,F
20,Male,3.73,28,B
20,Female,3.48,22,D
18,Female,2.81,22,B
20,Female,2.91,13,F
22,Male,2.82,10,B
24,Male,3.07,26,D
23,Female,2.56,17,A
20,Male,3.43,11,F
18,Male,3.0,17,A
22,Male,3.48,16,A
19,Male,3.08,11,A
24,Male,3.52,12,C
24,Male,3.01,27,C
23,Female,2.89,21,A
24,Female,3.24,10,F
20,Male,3.54,21,D
18,Female,3.02,14,D
24,Female,3.9,26,B
24,Female,2.56,25,F
19,Female,3.13,24,C
19,Male,3.95,24,A
21,Female,3.32,14,B
22,Female,3.14,23,D
20,Male,3.35,11,C
24,Male,3.36,20,C
24,Female,3.6,28,A
18,Female,2.69,16,D
21,Female,2.88,15,F
22,Female,3.37,11,C
21,Female,3.8,15,A
23,Female,3.34,27,F
22,Male,2.86,11,D
24,Female,3.52,27,C
24,Female,3.61,24,F
22,Male,2.86,28,F
24,Male,3.07,11,F
20,Male,3.3,29,C
22,Male,3.24,15,C
21,Female,3.08,10,B
22,Female,2.95,24,D
24,Female,2.65,19,A
20,Female,2.58,28,F
20,Female,3.94,26,B
23,Female,3.77,14,A
21,Male,3.03,13,B
19,Female,3.94,19,C
19,Male,3.52,26,F
22,Male,3.22,19,A"""
    df = pd.read_csv(io.StringIO(csv_data))


# Display the first few rows of the dataset
print("First Few Rows:")
print(df.head())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Univariate Analysis
# Histograms for numerical variables
df.plot(kind='hist', subplots=True, layout=(2, 2), figsize=(12, 10), bins=20,
        title='Histograms')
plt.show()

# Bar plot for categorical variables (e.g., Gender)
plt.figure(figsize=(7, 5))
df['Gender'].value_counts().plot(kind='bar', color=['skyblue', 'pink'])
plt.title('Distribution of Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()

# Bivariate Analysis
# Pairplot for numerical variables
sns.pairplot(df, hue='Gender', markers=['o', 's'], height=3)
plt.suptitle('Pair Plot of Numerical Variables by Gender', y=1.02)
plt.show()

# Correlation heatmap
correlation_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.2)
plt.title('Correlation Heatmap')
plt.show()

print("\n--- Summary ---")
print(f"Average GPA: {df['GPA'].mean():.2f}")

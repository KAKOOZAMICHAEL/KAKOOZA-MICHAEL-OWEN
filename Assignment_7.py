import pandas as pd
import numpy as np

# === SERIES EXERCISES ===
print("=== SERIES EXERCISES ===")

# 1. Compare elements of two Pandas Series
print("\n1. Compare two Series:")
series1 = pd.Series([4, 65, 436, 3, 9])
series2 = pd.Series([7, 0, 3, 897, 9])
print("Equal:", series1 == series2)
print("Greater than:", series1 > series2)
print("Less than:", series1 < series2)

# 2. Add, subtract, multiply, and divide two Pandas Series
print("\n2. Add, Subtract, Multiply, Divide two Series:")
series1 = pd.Series([2, 4, 6, 8, 14])
series2 = pd.Series([1, 3, 5, 7, 9])
print("Add:", series1 + series2)
print("Subtract:", series1 - series2)
print("Multiply:", series1 * series2)
print("Divide:", series1 / series2)

# 3. Convert a dictionary to a Pandas Series
print("\n3. Dictionary to Series:")
dictionary1 = {'Josh': 24, 'Sam': 36, 'Peace': 19, 'Charles': 65, 'Tom': 44}
series = pd.Series(dictionary1)
print(series)

# 4. Convert a Series to an array
print("\n4. Series to Array:")
series = pd.Series(['Love', 800, 'Joy', 789.9, 'Peace', True])
array = series.to_numpy()
print(array)

# === DATAFRAME EXERCISES ===
print("\n=== DATAFRAME EXERCISES ===")

# Load and clean DataFrame
file_path = 'AfricaCupofNationsMatches.csv'
df = pd.read_csv(file_path)

# Clean column names
df.columns = df.columns.str.strip()

# Remove duplicate column names if any (like 'Date' and 'Date ')
df = df.loc[:, ~df.columns.duplicated()]

# 1. DataFrame loaded
print("\n1. DataFrame loaded:")
print(df.head())

# 5. Replace non-most-frequent 'HomeTeamGoals' values with 'Other'
print("\n5. Most frequent value in HomeTeamGoals and replace others:")
most_frequent = df['HomeTeamGoals'].mode()[0]
df['HomeTeamGoals'] = df['HomeTeamGoals'].apply(lambda x: x if x == most_frequent else 'Other')
print(df['HomeTeamGoals'].head())

# 2. Get the first 7 rows
print("\n2. First 7 rows:")
print(df.head(7))

# 3. Select specific columns
print("\n3. Select specific columns:")
selected_columns = df[['HomeTeam', 'AwayTeam', 'HomeTeamGoals', 'AwayTeamGoals']]
print(selected_columns.head())

# 4. Select rows where Egypt appears
print("\n4. Rows where Egypt appears:")
egypt_rows = df[(df['HomeTeam'].str.strip() == 'Egypt') | (df['AwayTeam'].str.strip() == 'Egypt')]
print(egypt_rows)

# 5. Count rows and columns
print("\n5. Number of rows and columns:")
rows, cols = df.shape
print(f"Rows: {rows}, Columns: {cols}")

# 6. Select rows with missing Attendance
print("\n6. Rows with missing Attendance:")
missing_attendance = df[df['Attendance'].isna()]
print(missing_attendance)

# 7. Rows where HomeTeamGoals are between 3 and 6
print("\n7. Rows where HomeTeamGoals are between 3 and 6:")
df_original = pd.read_csv(file_path)
df_original.columns = df_original.columns.str.strip()
goals_3_to_6 = df_original[df_original['HomeTeamGoals'].between(3, 6)]
print(goals_3_to_6)

# 8. Change AwayTeamGoals in 3rd row to 10
print("\n8. Change AwayTeamGoals in 3rd row to 10:")
df.loc[2, 'AwayTeamGoals'] = 10
print(df.head())

# 9. Sort by HomeTeam (asc) and HomeTeamGoals (desc)
print("\n9. Sort by HomeTeam (asc) and HomeTeamGoals (desc):")
df = pd.read_csv(file_path)
df.columns = df.columns.str.strip()
sorted_df = df.sort_values(by=['HomeTeam', 'HomeTeamGoals'], ascending=[True, False])
print(sorted_df.head())

# 10. List of column headers
print("\n10. List of column headers:")
columns = list(df.columns)
print(columns)

# 11. Append a new column
print("\n11. Append a new column:")
df['NewColumn'] = 'DefaultValue'
print(df.head())

# 12. Add 2 rows
print("\n12. Add 2 rows:")
new_rows = pd.DataFrame({
    'Year': [2025, 2025],
    'Date': ['1-Jan', '2-Jan'],
    'HomeTeam': ['TeamA', 'TeamB'],
    'AwayTeam': ['TeamC', 'TeamD'],
    'HomeTeamGoals': [1, 2],
    'AwayTeamGoals': [0, 1],
    'Stage': ['Group', 'Group'],
    'SpecialWinConditions': [None, None],
    'Stadium': ['StadiumX', 'StadiumY'],
    'City': ['CityX', 'CityY'],
    'Attendance': [10000, 15000],
    'NewColumn': ['DefaultValue', 'DefaultValue']
})
df = pd.concat([df, new_rows], ignore_index=True)
print(df.tail())

# 13. Change Uganda to China in AwayTeam
print("\n13. Change Uganda to China in AwayTeam:")
df['AwayTeam'] = df['AwayTeam'].replace('Uganda', 'China')
print(df[df['AwayTeam'] == 'China'])

# 14. Reset index
print("\n14. Reset index:")
df = df.reset_index(drop=True)
print(df.tail())

# 15. Check if Stadium column exists
print("\n15. Check if Stadium column exists:")
print('Stadium' in df.columns)

# 16. Convert AwayTeamGoals to float
print("\n16. Convert AwayTeamGoals to float:")
df['AwayTeamGoals'] = df['AwayTeamGoals'].astype(float)
print(df.dtypes)

# 17. Remove last 10 rows
print("\n17. Remove last 10 rows:")
df = df.iloc[:-10]
print(df.tail())

# 18. Iterate over rows (clean output)
print("\n18. Iterate over rows:")
print(df.head(5).to_string(index=True))

# 19. Change column order
print("\n19. Change column order:")
new_order = ['AwayTeam', 'HomeTeam', 'AwayTeamGoals', 'HomeTeamGoals', 'Year', 'Date', 'Stage',
             'SpecialWinConditions', 'Stadium', 'City', 'Attendance', 'NewColumn']
df = df[new_order]
print(df.head())

# 20. Delete rows where HomeTeamGoals is 0
print("\n20. Delete rows where HomeTeamGoals is 0:")
df = df[df['HomeTeamGoals'] != 0]
print(df.head())

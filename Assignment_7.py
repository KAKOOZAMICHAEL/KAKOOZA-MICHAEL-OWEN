import pandas as pd
import numpy as np


print("=== AFRICA CUP OF NATIONS EXERCISE ===")


print("\n1. Compare two Series:")
series1 = pd.Series([4, 65, 436, 3, 9])
series2 = pd.Series([7, 0, 3, 897, 9])
print("Equal:", series1 == series2)
print("Greater than:", series1 > series2)
print("Less than:", series1 < series2)


print("\n2. Add, Subtract, Multiply, Divide two Series:")
series1 = pd.Series([2, 4, 6, 8, 14])
series2 = pd.Series([1, 3, 5, 7, 9])
print("Add:", series1 + series2)
print("Subtract:", series1 - series2)
print("Multiply:", series1 * series2)
print("Divide:", series1 / series2)


print("\n3. Dictionary to Series:")
dictionary1 = {'Josh': 24, 'Sam': 36, 'Peace': 19, 'Charles': 65, 'Tom': 44}
series = pd.Series(dictionary1)
print(series)


print("\n4. Series to Array:")
series = pd.Series(['Love', 800, 'Joy', 789.9, 'Peace', True])
array = series.to_numpy()
print(array)



file_path = 'AfricaCupofNationsMatches.csv'
df = pd.read_csv(file_path)


df.columns = df.columns.str.strip()


df = df.loc[:, ~df.columns.duplicated()]


print("\n1. DataFrame loaded:")
print(df.head())


print("\n5. Most frequent value in HomeTeamGoals and replace others:")
most_frequent = df['HomeTeamGoals'].mode()[0]
df['HomeTeamGoals'] = df['HomeTeamGoals'].apply(lambda x: x if x == most_frequent else 'Other')
print(df['HomeTeamGoals'].head())


print("\n2. First 7 rows:")
print(df.head(7))


print("\n3. Select specific columns:")
selected_columns = df[['HomeTeam', 'AwayTeam', 'HomeTeamGoals', 'AwayTeamGoals']]
print(selected_columns.head())


print("\n4. Rows where Egypt appears:")
egypt_rows = df[(df['HomeTeam'].str.strip() == 'Egypt') | (df['AwayTeam'].str.strip() == 'Egypt')]
print(egypt_rows)


print("\n5. Number of rows and columns:")
rows, cols = df.shape
print(f"Rows: {rows}, Columns: {cols}")

print("\n6. Rows with missing Attendance:")
missing_attendance = df[df['Attendance'].isna()]
print(missing_attendance)


print("\n7. Rows where HomeTeamGoals are between 3 and 6:")
df_original = pd.read_csv(file_path)
df_original.columns = df_original.columns.str.strip()
goals_3_to_6 = df_original[df_original['HomeTeamGoals'].between(3, 6)]
print(goals_3_to_6)


print("\n8. Change AwayTeamGoals in 3rd row to 10:")
df.loc[2, 'AwayTeamGoals'] = 10
print(df.head())


print("\n9. Sort by HomeTeam (ascinding order) and HomeTeamGoals (descending order):")
df = pd.read_csv(file_path)
df.columns = df.columns.str.strip()
sorted_df = df.sort_values(by=['HomeTeam', 'HomeTeamGoals'], ascending=[True, False])
print(sorted_df.head())



print("\n10. List of column headers:")
columns = list(df.columns)
print(columns)



print("\n11. Append a new column:")
df['NewColumn'] = 'DefaultValue'
print(df.head())



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


print("\n13. Change Uganda to China in AwayTeam:")
df['AwayTeam'] = df['AwayTeam'].replace('Uganda', 'China')
print(df[df['AwayTeam'] == 'China'])


print("\n14. Reset index:")
df = df.reset_index(drop=True)
print(df.tail())


print("\n15. Check if Stadium column exists:")
print('Stadium' in df.columns)


print("\n16. Convert AwayTeamGoals to float:")
df['AwayTeamGoals'] = df['AwayTeamGoals'].astype(float)
print(df.dtypes)


print("\n17. Remove last 10 rows:")
df = df.iloc[:-10]
print(df.tail())


print("\n18. Iterate over rows:")
print(df.head(5).to_string(index=True))


print("\n19. Change column order:")
new_order = ['AwayTeam', 'HomeTeam', 'AwayTeamGoals', 'HomeTeamGoals', 'Year', 'Date', 'Stage',
             'SpecialWinConditions', 'Stadium', 'City', 'Attendance', 'NewColumn']
df = df[new_order]
print(df.head())


print("\n20. Delete rows where HomeTeamGoals is 0:")
df = df[df['HomeTeamGoals'] != 0]
print(df.head())

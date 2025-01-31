# %%
import pandas as pd
import numpy as np

# %%
mlbdata = pd.read_csv('rawmlbpitching.csv')
kbodata = pd.read_csv('rawkbopitching.csv')

# %%
mlbdata.head()

# %%
kbodata.head()

# %%
print(mlbdata.describe())

# %%
print(kbodata.describe())

# %%
team_counts = kbodata.groupby('year')['team'].nunique()
kbodata['teams'] = kbodata['year'].map(team_counts)

# %%
# Grouping the KBO data by 'year' and aggregating all the columns
kbo_grouped_df = kbodata.groupby('year').agg({
    'average_age': 'mean',
    'runs_per_game': 'mean',
    'wins': 'sum',
    'losses': 'sum',
    'win_loss_percentage': 'mean',
    'ERA': 'mean',
    'run_average_9': 'mean',
    'games': 'sum',
    'games_started': 'sum',         
    'games_finished': 'sum',
    'complete_game': 'sum',
    'shutouts': 'sum',
    'saves': 'sum',
    'innings_pitched': 'sum',
    'hits': 'sum',
    'runs': 'sum',
    'earned_runs': 'sum',
    'home_runs': 'sum',
    'walks': 'sum',
    'intentional_walks': 'sum',
    'strikeouts': 'sum',
    'hit_batter': 'sum',
    'balks': 'sum',
    'wild_pitches': 'sum',
    'batters_faced': 'sum',
    'WHIP': 'mean',
    'hits_9': 'mean',
    'homeruns_9': 'mean',
    'walks_9': 'mean',
    'strikeouts_9': 'mean',
    'strikeout_walk': 'mean',
    'teams': 'max'  # Include the 'teams' column using 'max' to retain the unique count for each year
}).reset_index()

# Display the grouped data
print(kbo_grouped_df)

# %%
print("Column names in the MLB dataset:")
for column in mlbdata:
    print(column)

# %%
print("Column names in the KBO dataset:")
for column in kbo_grouped_df.columns:
    print(column)

# %%
kbo_grouped_df = kbo_grouped_df.drop(columns = ['wins', 'losses', 'win_loss_percentage', 'run_average_9', 'games', 'games_started'])
mlbdata = mlbdata.drop(columns = ['total_pitchers', 'games_played', 'shutouts_team', 'BA_bip', 'errors'])

# %%
mlb_columns_order = mlbdata.columns.tolist()

# Identify and add missing columns to KBO dataset with NaN values
for col in mlb_columns_order:
    if col not in kbo_grouped_df.columns:
        kbo_grouped_df[col] = np.nan

# Reorder the KBO dataset columns to match the MLB dataset column order
kbo_grouped_df = kbo_grouped_df[mlb_columns_order]

# Display the reordered datasets
print("Reordered KBO Data:")
print(kbo_grouped_df.head())
print("\nReordered MLB Data:")
print(mlbdata.head())

# %%
cleaned_mlb_data = mlbdata.sort_values(by='year', ascending=True).reset_index(drop = True)
cleaned_kbo_data = kbo_grouped_df.reset_index(drop = True)

# %%
cleaned_mlb_data.to_csv('cleaned_mlb_data.csv', index=False)
cleaned_kbo_data.to_csv('cleaned_kbo_data.csv', index=False)

# %%
from IPython.display import FileLink

display(FileLink('cleaned_mlb_data.csv'))
display(FileLink('cleaned_kbo_data.csv'))



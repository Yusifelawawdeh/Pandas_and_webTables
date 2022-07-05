import pandas as pd

df_premiere = pd.read_csv('https://www.football-data.co.uk/mmz4281/2122/E0.csv')

length = len(df_premiere)
print(length)
print(df_premiere)

df_premiere.rename(columns={'FTHG':'home_goals','FTAG':'away_goals'}, inplace=True)

print(df_premiere)
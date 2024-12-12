import pandas as pd

df = pd.read_csv('Fatur Rachman Huda - Negara.csv')
mean_population = df.groupby(['Negara'])['Populasi'].mean()

print(df)
print()
print(mean_population)

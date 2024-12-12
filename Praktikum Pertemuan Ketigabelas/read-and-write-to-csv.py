import pandas as pd

file_name = 'Fatur Rachman Huda - Negara.csv'
df = pd.read_csv(file_name)

mean_data = df.groupby(['Negara'])[['Luas', 'Populasi']].mean()
std_data = df.groupby(['Negara'])[['Luas', 'Populasi']].std()

print(df)
print("\nMean:\n", mean_data)
print("\nStandar Deviasi:\n", std_data)

mean_file = 'NegaraMean.csv'
std_file = 'NegaraStandarDeviasi.csv'

mean_data.to_csv(mean_file)
std_data.to_csv(std_file)

print(f"Hasil mean disimpan di {mean_file}")
print(f"Hasil standar deviasi disimpan di {std_file}")

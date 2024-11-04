# Leia um arquivo .csv (use pd.read_csv('arquivo.csv')) e exiba as cinco primeiras linhas.

import pandas as pd

df = pd.read_csv('arquivo.csv')

print(df.head())
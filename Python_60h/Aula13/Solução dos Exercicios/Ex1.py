# Crie uma Series que armazene cinco notas e exiba a média delas

import pandas as pd

notas = pd.Series([7.5, 8.0, 6.5, 9.0, 7.0])
media = notas.mean()

print("média: ", media)
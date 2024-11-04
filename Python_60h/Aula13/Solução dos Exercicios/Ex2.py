# Crie um DataFrame com informações de produtos (nome e preço) e exiba todos os dados.

import pandas as pd

prod = {'Produto': ['Heineken', 'Corona', 'Amstel'], 'Precos':[5.99, 6.99, 2.89]}

df = pd.DataFrame(prod)

print(df)
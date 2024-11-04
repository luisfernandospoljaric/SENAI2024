# Crie um DataFrame e aplique uma função para converter a coluna de preços em dólares para reais, usando um valor de conversão de 5.00.

import pandas as pd

dados = {'Produto':['Cuéca','Tenis','Calça'], 'Preco_Dolar':[10, 20, 30]}

df = pd.DataFrame(dados)
df['Preco_Total'] = df['Preco_Dolar'] * 5

print(df)
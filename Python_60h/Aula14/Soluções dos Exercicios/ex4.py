import pandas as pd

df_estoque = pd.read_excel("estoque.xlsx")

df_estoque['ValorTotal'] = df_estoque['Preco'] * df_estoque['Quantidade']

df_estoque.to_excel("estoque_atualizado.xlsx", index=False)

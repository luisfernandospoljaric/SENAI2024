import pandas as pd

df_vendas = pd.read_excel("vendas.xlsx")

df_vendas['Comissao'] = df_vendas['Comissao'].fillna(df_vendas['Comissao'].mean())

df_vendas.to_excel("vendas_comissao.xlsx", index=False)

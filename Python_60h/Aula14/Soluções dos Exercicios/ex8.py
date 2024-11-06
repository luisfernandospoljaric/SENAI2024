import pandas as pd

df_transacoes = pd.read_excel("transacoes.xlsx")

df_resumo = df_transacoes.groupby('Cliente')['Valor'].sum().reset_index()

df_resumo.to_excel("resumo_transacoes.xlsx", index=False)

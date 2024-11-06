import pandas as pd

df_funcionarios = pd.read_excel("funcionarios.xlsx")

df_vendas = df_funcionarios[df_funcionarios['Setor'] == 'Vendas'].copy()
df_vendas['Salario'] = df_vendas['Salario'] * 1.15

df_vendas.to_excel("vendas_atualizado.xlsx", index=False)

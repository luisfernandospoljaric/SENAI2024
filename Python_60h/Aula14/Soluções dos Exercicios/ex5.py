import pandas as pd

df_clientes = pd.read_excel("clientes.xlsx")

df_clientes_adultos = df_clientes[df_clientes['Idade'] >= 18]

df_clientes_adultos.to_excel("clientes_adultos.xlsx", index=False)

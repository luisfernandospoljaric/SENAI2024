import pandas as pd

df_notas = pd.read_excel("notas_alunos.xlsx")

df_notas['Situacao'] = df_notas['Media'].apply(lambda x: 'Aprovado' if x >= 7 else 'Reprovado')

df_notas.to_excel("notas_situacao.xlsx", index=False)

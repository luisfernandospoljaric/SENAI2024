# Use groupby para calcular a média de notas por idade de um conjunto de estudantes.

import pandas as pd

dados = {'Nome':['Lucas', 'Pedro', 'Zeca'], 'Idade':[22, 23, 24], 'Nota':[7.0, 8.5, 9.0]}
df = pd.DataFrame(dados)
media_idade = df.groupby('Idade')['Nota'].mean()

print(media_idade)
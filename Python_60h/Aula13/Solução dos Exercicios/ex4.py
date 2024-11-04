# Crie um DataFrame com informações de estudantes (nome, idade, nota) e exiba apenas os estudantes com nota acima de 7.

import pandas as pd

dados = {'Nome':['Pedro', 'Rodrigo', 'Pietra'], 'Idade':[22, 23, 21], 'Nota':[8.5, 6.0, 9.0]}
df = pd.DataFrame(dados)

aprovados = df[df['Nota']>7]

print("Aprovados ", aprovados)
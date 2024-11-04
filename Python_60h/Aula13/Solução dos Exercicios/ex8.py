# Utilize dados de um DataFrame que contenha informações de funcionários (nome, salário e departamento). Agrupe os dados por departamento e calcule o salário médio e o total de salários de cada departamento.

import pandas as pd

dados = {'Nome':['Natan', 'Ricardo', 'Davi', 'Pedro'], 'Salario':[8000, 9000, 18000, 7000], 'Departamento':['Dev', 'Tester', 'Dev', 'Tester']}

df = pd.DataFrame(dados)

result = df.groupby('Departamento')['Salario'].mean()

print(result)

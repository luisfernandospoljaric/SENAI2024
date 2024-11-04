import pandas as pd

# Carregar os dados da planilha Excel
df = pd.read_excel("C:/Users/luisf/Documents/GitHub/SENAI2024/Python_60h/Aula14/dados_exemplo.xlsx")

# Filtrar dados para idade maior que 30
df_filtrado = df[df['Idade'] > 30].copy()

# Aumentar o salário em 10% para os funcionários com idade maior que 30
df_filtrado.loc[:, 'Salario'] = df_filtrado['Salario'] * 1.1

# Remover a coluna 'Endereco'
df_filtrado = df_filtrado.drop(columns=['Endereco'])

# Preencher valores nulos na coluna 'Experiencia' com a média sem usar inplace=True
df_filtrado['Experiencia'] = df_filtrado['Experiencia'].fillna(df_filtrado['Experiencia'].mean())

# Salvar o DataFrame modificado de volta na mesma planilha Excel
df_filtrado.to_excel("C:/Users/luisf/Documents/GitHub/SENAI2024/Python_60h/Aula14/dados_exemplo_modificado.xlsx", index=False)

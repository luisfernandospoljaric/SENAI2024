import pandas as pd

df = pd.read_excel("produtos.xlsx")

print(df.head())


df_acima_50 = df[df['Preco'] > 50]


df_acima_50.to_excel("produtos_acima_50.xlsx", index=False)

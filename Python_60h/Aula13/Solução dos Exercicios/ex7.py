# Carregue um DataFrame com informações de vendas, incluindo colunas de produto, quantidade e preço_unitário. 
# Calcule o total de vendas (quantidade * preço_unitário) para cada produto e exiba os produtos que tiveram vendas totais acima de 100.

import pandas as pd

produtos = {'Produto':['p1', 'p2', 'p3'], 'Quantidade': [5, 20, 15], 'preço_unitario':[10, 5, 12]}
df = pd.DataFrame(produtos)
df['Total_Vendas'] = df['Quantidade']*df['preço_unitario']

vendas_mais_100 = df[df['Total_Vendas']>100]
print(vendas_mais_100)
# Aula06 - Segmentação de dados
A segmentação de dados no Power BI, conhecida em inglês como "Data Slicers", é uma ferramenta interativa que permite aos usuários filtrar dados em relatórios de forma visual e intuitiva. Segmentadores de dados facilitam a análise de diferentes subconjuntos de dados sem a necessidade de alterar permanentemente os relatórios ou gráficos.

## O que é um Segmentador de Dados?
Um segmentador de dados é um tipo de filtro visual que pode ser adicionado a um relatório no Power BI. Ele permite que os usuários selecionem um ou mais valores de um campo específico para filtrar os dados apresentados nos gráficos, tabelas e outras visualizações.

A segmentação de dados no Power BI é uma ferramenta essencial para criar relatórios interativos e dinâmicos. Ela permite que os usuários filtrem e explorem dados de maneira intuitiva, melhorando a capacidade de análise e tomada de decisão baseada em dados.

## Benefícios dos Segmentadores de Dados
- Interatividade: Melhora a interatividade do relatório, permitindo que os usuários explorem os dados de diferentes perspectivas.
- Facilidade de Uso: Segmentadores são intuitivos e fáceis de usar, mesmo para usuários sem experiência técnica.
- Análise Dinâmica: Permitem análises dinâmicas e rápidas, sem a necessidade de criar múltiplas versões do mesmo relatório para diferentes cenário

# DrillDown
Drill down em Power BI é uma funcionalidade que permite aos usuários explorar dados em níveis mais detalhados dentro de uma hierarquia. Isso é particularmente útil para análise de dados complexos, onde você pode começar com uma visão geral e, em seguida, aprofundar-se em dados mais específicos. Aqui está como funciona:

## Hierarquias de Dados
Primeiro, é importante ter hierarquias de dados configuradas. Uma hierarquia pode ser composta de diferentes níveis, como:

- Ano -> Trimestre -> Mês -> Dia
- Continente -> País -> Estado -> Cidade

## Exemplo Prático
Suponha que você tenha um gráfico de vendas por ano e deseja analisar as vendas trimestrais dentro de um ano específico:

Crie a hierarquia: Ano -> Trimestre -> Mês.
Adicione o gráfico: Insira um gráfico de colunas e coloque a hierarquia de datas no eixo X e as vendas no eixo Y.
Ative o Drill Down: Clique no ícone de drill down.
Perfure os dados: Clique em um ano específico (por exemplo, 2023). O gráfico agora mostrará os dados trimestrais para 2023.
Perfure ainda mais: Clique em um trimestre para ver os dados mensais.

## Benefícios do Drill Down
- Intuitividade: Facilita a navegação pelos dados de forma intuitiva, permitindo que usuários não técnicos façam análises detalhadas.

- Detalhamento Incremental: Permite começar com uma visão ampla e ir detalhando conforme necessário, sem sobrecarregar o usuário com todas as informações de uma vez.

- Análise Profunda: Ajuda a identificar padrões, tendências e outliers em diferentes níveis de detalhe.


# Publicações:
    Publicar seu projeto de Power BI envolve vários passos, dependendo de onde você deseja compartilhar o seu trabalho. Vou detalhar os principais métodos:

## Publicar no Power BI Service
1. Preparar o Relatório: Certifique-se de que o relatório esteja completo e sem erros no Power BI Desktop

2. Publicar:
- Abra o Power BI Desktop e carregue o relatório que você deseja publicar. 
- Clique em Publicar no canto superior direito.
- Selecione seu Workspace no Power BI Service (ou crie um novo).

3. Configurar as Credenciais de Fonte de Dados:
- Após a publicação, acesse o Power BI Service (app.powerbi.com).
- Vá para o Workspace onde o relatório foi publicado.
- Clique em Configurações do dataset associado ao relatório.
- Configure as credenciais da fonte de dados para garantir que a atualização de dados funcione corretamente.
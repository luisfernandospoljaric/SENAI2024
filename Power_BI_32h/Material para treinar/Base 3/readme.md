# 🛠️ Exercício Prático de Power BI

## 📋 Descrição do Exercício
Você é um analista de dados em uma loja de varejo e recebeu um conjunto de dados para analisar as vendas e o desempenho dos funcionários. Os dados estão divididos em dois arquivos: **"Vendas.xlsx"** e **"Funcionários.xlsx"**.

### Objetivo
- Importar, tratar e relacionar os dados no Power BI.
- Criar gráficos interativos para análises visuais.
- Aplicar filtros e criar medidas para uma análise mais completa.

---

## 📁 Fonte de Dados

### 1. **Vendas.xlsx**
Contém os dados de vendas realizadas pela loja.

| ID_Venda | Data_Venda  | ID_Funcionario | Produto  | Quantidade | Valor_Unitario |
|----------|-------------|----------------|----------|------------|----------------|
| 1        | 2024-01-15  | 101            | Cadeira  | 2          | 150.00         |
| 2        | 2024-01-20  | 102            | Mesa     | 1          | 300.00         |
| ...      | ...         | ...            | ...      | ...        | ...            |

[Baixar Vendas.xlsx](./Vendas.xlsx)

---

### 2. **Funcionários.xlsx**
Contém informações dos funcionários da loja.

| ID_Funcionario | Nome          | Departamento   | Data_Admissao |
|----------------|---------------|----------------|---------------|
| 101            | Carlos Silva  | Vendas         | 2020-05-10    |
| 102            | Ana Pereira   | Vendas         | 2021-08-15    |
| ...            | ...           | ...            | ...           |

[Baixar Funcionários.xlsx](./Funcionarios.xlsx)

---

## 🔧 Tarefas

### 1. **Importação dos Dados**
- Carregue os dois arquivos no Power BI.

### 2. **Tratamento de Dados**
- No arquivo **Vendas.xlsx**, crie uma coluna calculada chamada **Valor_Total**, que multiplica **Quantidade** pelo **Valor_Unitario**.
- Converta as colunas de data (**Data_Venda** e **Data_Admissao**) para o formato de data apropriado.
- Corrija possíveis inconsistências, como valores nulos ou duplicados. Certifique-se de que os IDs não estejam repetidos de forma indevida.

### 3. **Relacionamento**
- Crie um relacionamento entre as tabelas **Vendas** e **Funcionários** usando a coluna **ID_Funcionario** como chave primária.

### 4. **Visualizações e Gráficos**
Crie as seguintes visualizações no **relatório**:
- **Gráfico de Colunas**: Mostre o total de vendas por **Produto**.
- **Gráfico de Pizza**: Apresente a participação de vendas por **Departamento**.
- **Tabela Dinâmica**: Liste os **Funcionários**, junto com a quantidade total de vendas realizadas por cada um.
- **Série Temporal**: Mostre as vendas totais ao longo do tempo (**Data_Venda**).

### 5. **Análises Adicionais**
- Crie uma **medida DAX** para calcular o faturamento médio por venda.
- Adicione um **filtro** no painel que permita visualizar os dados por **Departamento**.

### 6. **Personalização**
- Adicione uma **segmentação de dados** para permitir que o usuário selecione intervalos de datas.
- Configure a página com cores e logotipo da empresa fictícia.

---

## 🎯 Objetivos do Exercício
- Aplicar técnicas de ETL (Extração, Transformação e Carregamento).
- Trabalhar com relacionamentos entre tabelas no Power BI.
- Criar gráficos interativos para visualização de dados.
- Desenvolver análises avançadas com medidas DAX.

---

## 📝 Notas
- Certifique-se de verificar os relacionamentos criados entre as tabelas.
- Lembre-se de salvar seu projeto no formato `.pbix` e exportar um relatório para apresentação, se necessário.

---

## 📥 Downloads
- [Vendas.xlsx](./Vendas.xlsx)
- [Funcionários.xlsx](./Funcionários.xlsx)

Boa sorte no exercício! 🚀

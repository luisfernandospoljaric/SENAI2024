# 📊 Exercício de Power BI - Contexto RH

## 📋 Descrição do Exercício
Você é um analista de Recursos Humanos e recebeu o desafio de criar um **dashboard** para acompanhar os indicadores de desempenho e treinamentos dos funcionários da empresa. O objetivo é identificar tendências, avaliar desempenhos e propor melhorias com base nos dados disponíveis.

---

## 📁 Bases de Dados

### 1. **Funcionários.xlsx**
Contém informações básicas dos colaboradores.

| ID_Funcionario | Nome           | Departamento      | Cargo                | Salario | Data_Admissao |
|----------------|----------------|-------------------|----------------------|---------|---------------|
| 101            | Carlos Silva   | TI                | Analista             | 4000    | 2020-05-10    |
| 102            | Ana Pereira    | TI                | Desenvolvedor        | 4500    | 2021-08-15    |
| 103            | João Costa     | Financeiro        | Analista Financeiro  | 5000    | 2019-11-20    |
| ...            | ...            | ...               | ...                  | ...     | ...           |

[Baixar Funcionários.xlsx](./Funcionarios.xlsx)

---

### 2. **Avaliacoes.xlsx**
Contém registros de avaliações de desempenho realizadas com os funcionários.

| ID_Funcionario | Data_Avaliacao | Nota_Desempenho | Feedback             |
|----------------|----------------|-----------------|----------------------|
| 101            | 2023-01-15     | 8               | Ótimo trabalho       |
| 102            | 2023-01-20     | 7               | Bom desempenho       |
| 103            | 2023-02-05     | 9               | Excelente            |
| ...            | ...            | ...             | ...                  |

[Baixar Avaliacoes.xlsx](./Avaliacoes.xlsx)

---

### 3. **Treinamentos.xlsx**
Contém informações sobre treinamentos concluídos pelos funcionários.

| ID_Funcionario | Treinamento             | Data_Conclusao | Custo |
|----------------|-------------------------|----------------|-------|
| 101            | Liderança               | 2023-06-15     | 1000  |
| 102            | Python Avançado         | 2023-07-20     | 1200  |
| 103            | Gestão Financeira       | 2023-08-05     | 800   |
| ...            | ...                     | ...            | ...   |

[Baixar Treinamentos.xlsx](./Treinamentos.xlsx)

---

## 🔧 Tarefas

### 1. **Importação dos Dados**
- Carregue os três arquivos no Power BI.

### 2. **Tratamento de Dados**
- No arquivo **Funcionários.xlsx**, crie uma coluna calculada chamada **Tempo_Empresa**, que calcula o número de anos entre a **Data_Admissao** e a data atual:
  ```DAX
  Tempo_Empresa = DATEDIFF([Data_Admissao], TODAY(), YEAR)
  ```

### Avaliacoes.xlsx
- Crie uma **Coluna Calculada** chamada `Resultado`, baseada na **Nota_Desempenho**:
  - **Aprovado**: Nota maior ou igual a 7.
  - **Em Desenvolvimento**: Nota menor que 7.
  ```DAX
  Resultado = IF([Nota_Desempenho] >= 7, "Aprovado", "Em Desenvolvimento")
  ``` 

### Relacionamento
- Relacione as tabelas utilizando a coluna ID_Funcionario como chave primária.


### Visualizações e Gráficos
- Gráfico de Colunas: Mostre o salário médio por Departamento.
- Gráfico de Pizza: Exiba a proporção de funcionários por Resultado das avaliações. 
- Tabela Dinâmica: Liste os Funcionários, com o Tempo_Empresa e o número de Treinamentos Concluídos.
- Linha do Tempo: Mostre o custo total de treinamentos ao longo do tempo.

### Medidas Avançadas DAX
- *** Custo total do treinamento ***
```DAX
Custo_Total_Treinamentos = SUM(Treinamentos[Custo])
``` 

- Elegibilidade para Promoção: Um funcionário é elegível para promoção se: 
- Nota de Desempenho ≥ 8.
- Treinamentos Concluídos ≥ 3.

```DAX
Elegivel_Promocao = IF(
  [Nota_Desempenho] >= 8 && COUNT(Treinamentos[ID_Funcionario]) >= 3,
  "Sim", 
  "Não"
)
```

## 🎯 Objetivos do Exercício
- Aplicar técnicas de ETL (Extração, Transformação e Carregamento) no Power BI.
- Utilizar fórmulas DAX com a função IF para criar lógicas de negócio.
- Construir dashboards interativos e gráficos relevantes para análise de RH.

## 📥 Downloads
- [Avaliacoes.xlsx](./Avaliacoes.xlsx)
- [Funcionários.xlsx](./Funcionários.xlsx)
- [Treinamentos.xlsx](./Treinamentos.xlsx)


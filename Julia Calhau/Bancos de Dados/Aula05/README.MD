# Aula Banco de dados - JOINs

## Criando o banco em sala de aula

CREATE DATABASE Loja;
USE Loja;

CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY,
    nome VARCHAR(50),
    cidade VARCHAR(50)
);

CREATE TABLE pedidos (
    id_pedido INT PRIMARY KEY,
    id_cliente INT,
    produto VARCHAR(50),
    valor DECIMAL(10, 2),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);


INSERT INTO clientes (id_cliente, nome, cidade) VALUES
(1, 'Maria', 'São Paulo'),
(2, 'Carlos', 'Rio de Janeiro'),
(3, 'Ana', 'Curitiba');

INSERT INTO pedidos (id_pedido, id_cliente, produto, valor) VALUES
(101, 1, 'Notebook', 3000.00),
(102, 1, 'Mouse', 50.00),
(103, 2, 'Teclado', 100.00),
(104, 4, 'Monitor', 700.00); -- Note que não existe cliente com id 4



# Exercicios:

## Crie o banco e faça os Insert:

CREATE DATABASE Livraria;
USE Livraria;

CREATE TABLE autores (
    id_autor INT PRIMARY KEY,
    nome VARCHAR(50)
);

CREATE TABLE livros (
    id_livro INT PRIMARY KEY,
    titulo VARCHAR(100),
    id_autor INT,
    preco DECIMAL(8, 2),
    FOREIGN KEY (id_autor) REFERENCES autores(id_autor)
);


INSERT INTO autores (id_autor, nome) VALUES
(1, 'J.K. Rowling'),
(2, 'George R.R. Martin'),
(3, 'J.R.R. Tolkien');

INSERT INTO livros (id_livro, titulo, id_autor, preco) VALUES
(101, 'Harry Potter', 1, 39.90),
(102, 'A Game of Thrones', 2, 49.90),
(103, 'The Hobbit', 3, 29.90),
(104, 'Fantastic Beasts', 1, 25.90);


1. Exibir todos os livros com seus respectivos autores.

SELECT livros.titulo, autores.nome
FROM livros
INNER JOIN autores ON livros.id_autor = autores.id_autor;


2. Exibir todos os autores, com ou sem livros.

SELECT autores.nome, livros.titulo
FROM autores
LEFT JOIN livros ON autores.id_autor = livros.id_autor;


3. Listar todos os livros e seus preços.

SELECT titulo, preco FROM livros;


4. Listar os livros mais caros que R$30,00.

SELECT titulo, preco
FROM livros
WHERE preco > 30.00;


5. Exibir os autores que têm livros cadastrados na tabela.

SELECT DISTINCT autores.nome
FROM autores
INNER JOIN livros ON autores.id_autor = livros.id_autor;


6. Exibir todos os autores e o total de livros que possuem.

SELECT autores.nome, COUNT(livros.id_livro) AS total_livros
FROM autores
LEFT JOIN livros ON autores.id_autor = livros.id_autor
GROUP BY autores.nome;


7. Exibir todos os livros cujo título contém a palavra "The".

SELECT titulo
FROM livros
WHERE titulo LIKE '%The%';


8. Calcular a média dos preços dos livros.

SELECT AVG(preco) AS media_preco FROM livros;



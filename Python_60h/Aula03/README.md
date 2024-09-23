# Aula03

# Algoritmos

Conjunto de passos lógicos e iterativos para resolução de um problema.

## Problema
Algo que possua uma solução porém não trivial.

## Exemplo de problema
- Escovar os dentes - Não é um problema (Possui solução trivial)
- Tocar a superfície do Sol - Não é um problema (Não possui solução)
- Trocar uma lâmpada - É um problema (Possui solução porém não trivial)

## Exemplo de algoritmo
### Problema: Trocar uma lâmpada (Portugol)
```portugol
0 - Início
1 - Pegar a escada e uma lâmpada nova
2 - Posicionar a escada
3 - Subir na escada
4 - Ajustar a lâmpada e fazer um teste, se acender ir para o passo 6, senão ir para o passo 5
5 - Trocar a lâmpada e ir para o passo 4.
6 - Descer da escada
7 - Guardar a escada e a lampada nova ou descartar a lâmpada queimada
8 - Fim
```

### Desafio: Pérolas e balança
Um joalheiro possui 9 pérolas e uma balançã do tipo prato de dois pratos. Todas as pérolas possuem o mesmo peso, exceto uma que é mais leve. Utilizando a balança, escreva um algoritmo que descura quantas pesagens no mínimo são necessárias para descobrir qual é a pérola mais leve?

## Conhecimentos:
- 1 Lógica e algoritmos
	- 1.1. Definição
	- 1.2. Estruturas
		- 1.2.1.Sequência
		- 1.2.2.Seleção
		- 1.2.3.Repetição



# EXERCICIOS

 1 - Faça um Programa que peça dois números e imprima o maior deles.

 Var
// Seção de Declarações das variáveis
 n1, n2, n3: inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
// Leitura dos números
    escreva("Digite o primeiro número: ")
    leia(n1)

    escreva("Digite o segundo número: ")
    leia(n2)

    escreva("Digite o terceiro número: ")
    leia(n3)

    se (n1 > n2) e (n1 > n3) então
       escreval("o numero maior eh: ", n1)
    senao
       se (n2 > n3) e (n2 > n1) então
          escreval("O maior numero eh: ",n2)
       senao
         se (n3>n1) e (n3>n2) então
            escreval("o maio numero eh: ",n3)
         senao
         fimse
    fimse
fimse


fimalgoritmo

2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

Var
// Seção de Declarações das variáveis 
numero : inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
Escreval ("Infome um neumro")
leia(numero)

se (numero > 0) entao
   escreval("O numero eh positivo")
senao
   escreval ("o numero eh negativo")
fimse


Fimalgoritmo

3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

Var
// Seção de Declarações das variáveis 
letra:caractere
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

escreval ("Informe F para feminino OU M para masculino")
leia(letra)

 se letra = "F" então
        escreva("F - Feminino")
    senao
        se letra = "M" então
            escreva("M - Masculino")
        senao
            escreva("Sexo Inválido")
        fimse
    fimse

Fimalgoritmo

4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

Var
// Seção de Declarações das variáveis 
letra: caractere

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
Escreval ("Informe uma letra")
leia (letra)

 se (letra = "A") ou (letra = "E") ou (letra = "I") ou (letra = "O") ou (letra = "U") então
        escreva("A letra ", letra, " é uma vogal.")
    senao
        se (letra >= "B") e (letra <= "Z") e (letra <> "A") e (letra <> "E") e (letra <> "I") e (letra <> "O") e (letra <> "U") então
            escreva("A letra ", letra, " é uma consoante.")
        senao
            escreva("Caractere inválido. Por favor, digite uma letra do alfabeto.")
        fimse
    fimse

Fimalgoritmo

5 - Faça um Programa que leia três números e mostre o maior deles.

Var
// Seção de Declarações das variáveis
 n1, n2, n3: inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
// Leitura dos números
    escreva("Digite o primeiro número: ")
    leia(n1)

    escreva("Digite o segundo número: ")
    leia(n2)

    escreva("Digite o terceiro número: ")
    leia(n3)

    se (n1 > n2) e (n1 > n3) então
       escreval("o numero maior eh: ", n1)
    senao
       se (n2 > n3) e (n2 > n1) então
          escreval("O maior numero eh: ",n2)
       senao
         se (n3>n1) e (n3>n2) então
            escreval("o maio numero eh: ",n3)
         senao
         fimse
    fimse
fimse


fimalgoritmo

6 - Faça um Programa que leia três números e mostre o maior e o menor deles.

var
    num1, num2, num3: inteiro
    maior, menor: inteiro
inicio
    // Leitura dos números
    escreva("Digite o primeiro número: ")
    leia(num1)

    escreva("Digite o segundo número: ")
    leia(num2)

    escreva("Digite o terceiro número: ")
    leia(num3)

    maior := num1
    menor := num1

    se (num2 > maior) entao
        maior := num2
    fimse

    se (num2 < menor) entao
        menor := num2
    fimse

    se (num3 > maior) entao
        maior := num3
    fimse

    se (num3 < menor) entao
        menor := num3
    fimse

    // Mostra o maior e o menor número
    escreva("O maior número é: ", maior, "\n")
    escreva("O menor número é: ", menor)
fimalgoritmo

7 - Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

var
    dia: inteiro
inicio
    // Leitura do número do dia
    escreva("Digite um número de 1 a 7: ")
    leia(dia)

    // Verifica e exibe o dia correspondente
    escolha dia
        caso 1
            escreva("Domingo")
        caso 2
            escreva("Segunda-feira")
        caso 3
            escreva("Terça-feira")
        caso 4
            escreva("Quarta-feira")
        caso 5
            escreva("Quinta-feira")
        caso 6
            escreva("Sexta-feira")
        caso 7
            escreva("Sábado")
        caso contrario:
            escreva("Valor inválido")
    fimescolha
fimalgoritmo


# Formulário para envio:

https://docs.google.com/forms/d/e/1FAIpQLSe5b-4Aa7qBUPC5GB5sSY84HEmId4PTVL83vRbz9dpRf1I7jA/viewform?usp=sf_link

numero = int(input("Digite um número: "))

if numero > 0:
    print(f"{numero} é positivo")
elif numero < 0:
    print(f"{numero} é negativo")
else:
    print("O número é zero")


##O f nos print refere-se a f-strings (formatted string literals), uma maneira moderna e eficiente de formatar strings em Python.
##Ao colocar um f antes das aspas, você pode inserir variáveis diretamente dentro de uma string, usando {} para indicar onde a variável será inserida. O Python substitui as chaves pela representação do valor da variável.
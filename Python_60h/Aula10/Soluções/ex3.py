lista = [1, 2, 3]
try:
    indice = int(input("Digite um índice (0-2): "))
    print(lista[indice])
except IndexError:
    print("Índice fora do intervalo da lista.")
import math

try:
    numero = float(input("Digite um número para calcular a raiz quadrada: "))
    if numero < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
    print(f"A raiz quadrada de {numero} é {math.sqrt(numero)}.")
except ValueError as e:
    print(e)
class DivisaoPorZero(Exception):
    pass

def dividir(a, b):
    if b == 0:
        raise DivisaoPorZero("Não é possível dividir por zero.")
    return a / b

try:
    num1 = float(input("Digite o numerador: "))
    num2 = float(input("Digite o denominador: "))
    resultado = dividir(num1, num2)
    print(f"O resultado da divisão é: {resultado}")
except DivisaoPorZero as e:
    print(e)
except ValueError:
    print("Por favor, digite apenas números válidos.")
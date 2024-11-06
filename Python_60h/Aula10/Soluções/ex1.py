try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 / num2
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
except ValueError:
    print("Por favor, digite apenas números.")
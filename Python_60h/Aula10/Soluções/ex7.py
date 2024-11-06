try:
    numeros = input("Digite uma lista de números separados por vírgula: ")
    lista_numeros = [float(num) for num in numeros.split(",")]
    media = sum(lista_numeros) / len(lista_numeros)
    print(f"A média é: {media}")
except ValueError:
    print("Por favor, digite apenas números válidos.")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
# numeros = list(range(1, 11))
# numeros = [num for num in numeros if num % 2 != 0]
# print(numeros)

# Criamos uma lista com os números de 1 a 10
numeros = list(range(1, 11))

# Criamos uma nova lista com apenas os números ímpares
numeros_impares = []
for numero in numeros:
    if numero % 2 != 0:
        numeros_impares.append(numero)

# Imprimimos a lista de números ímpares
print(numeros_impares)
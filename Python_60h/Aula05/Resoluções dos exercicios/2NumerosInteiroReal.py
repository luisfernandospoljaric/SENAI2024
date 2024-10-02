# Solicita os dois números inteiros e o número real
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = float(input("Digite um número real: "))

# Calcula o produto do dobro do primeiro com metade do segundo
resultado1 = (2 * numero1) * (numero2 / 2)

# Calcula a soma do triplo do primeiro com o terceiro
resultado2 = (3 * numero1) + numero3

# Calcula o terceiro número elevado ao cubo
resultado3 = numero3 ** 3

# Exibe os resultados
print("\nO produto do dobro do primeiro com metade do segundo é: {:.2f}".format(resultado1))
print("A soma do triplo do primeiro com o terceiro é: {:.2f}".format(resultado2))
print("O terceiro número elevado ao cubo é: {:.2f}".format(resultado3))

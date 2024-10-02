# Solicita a temperatura em Fahrenheit
fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

# Converte para Celsius
celsius = (5 * (fahrenheit - 32) / 9)

# Exibe a temperatura em Celsius
print("\nA temperatura em graus Celsius é: {:.2f}°C".format(celsius))

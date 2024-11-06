try:
    numero = int(input("Digite um número inteiro: "))
    print(f"O número digitado é: {numero}")
except ValueError:
    print("Isso não é um número inteiro válido.")
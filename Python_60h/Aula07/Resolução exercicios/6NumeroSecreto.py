numero_secreto = 7
while True:
    chute = int(input("Tente adivinhar o número (entre 1 e 10): "))
    if chute == numero_secreto:
        print("Você acertou!")
        break
    else:
        print("Tente novamente!")
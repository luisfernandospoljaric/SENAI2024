import random

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    tentativa = int(input("Tente adivinhar o número (entre 1 e 100): "))
    tentativas += 1

    if tentativa < numero_secreto:
        print("O número é maior!")
    elif tentativa > numero_secreto:
        print("O número é menor!")
    else:
        print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")
        break
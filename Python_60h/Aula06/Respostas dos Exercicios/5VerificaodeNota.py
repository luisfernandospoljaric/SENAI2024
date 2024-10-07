nota = float(input("Digite sua nota (0-100): "))

if 0 <= nota <= 100:
    if nota >= 60:
        print("Você foi aprovado")
    else:
        print("Você foi reprovado")
else:
    print("Nota inválida")

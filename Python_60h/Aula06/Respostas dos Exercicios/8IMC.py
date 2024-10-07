
peso = float(input("Informe o peso (em kg): "))
altura = float(input("Informe sua altura (em metros): "))

imc = peso / (altura * altura)

print(f"O seu IMC é: {imc:.2f}")

if imc < 16.9:
    print("Muito abaixo do peso!")
elif 17 <= imc <= 18.4:
    print("Abaixo do peso")
elif 18.5 <= imc <= 24.9:
    print("Peso Normal")
elif 25 <= imc <= 29.9:
    print("Acima do peso!")
elif 30 <= imc <= 34.9:
    print("Obesidade grau 1")
elif 35 <= imc <= 40:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")

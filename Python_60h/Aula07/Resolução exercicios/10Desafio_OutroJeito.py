
limite = int(input("Digite um número: "))

print(f"Números primos até {limite}:")

#Percorre todos os numeros até o digitado
for num in range(2, limite + 1):
    primo = True
    #Verifica se é primo
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(num)

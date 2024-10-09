contador = 0
for i in range(100, 1000):
    if i % 3 == 0 and i % 7 == 0:
        contador += 1
print(f"Há {contador} números divisíveis por 3 e 7 entre 100 e 999.")
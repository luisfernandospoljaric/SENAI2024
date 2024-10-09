"""numero = int(input("Digite um número: "))

def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(2, numero + 1):
    if eh_primo(i):
        print(i)
"""

limite = int(input("Digite um número: "))

print(f"Números primos até {limite}:")

for num in range(2, limite + 1):    
    primo = True
    
    for i in range(2, num):
        if num % i == 0:  
            primo = False  
            break
    
    if primo:
        print(num)
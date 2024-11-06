def verificar_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Exemplo de uso
print(verificar_primo(7))  # True
print(verificar_primo(10))  # False
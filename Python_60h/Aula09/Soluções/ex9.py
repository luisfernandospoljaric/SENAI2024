def maior_lista(lista):
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

# Exemplo de uso
print(maior_lista([3, 6, 2, 8, 4]))  # 8
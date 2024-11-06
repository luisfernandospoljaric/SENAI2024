dicionario = {"a": 1, "b": 2, "c": 3}
try:
    chave = input("Digite uma chave (a, b, c): ")
    print(f"O valor para a chave '{chave}' é {dicionario[chave]}.")
except KeyError:
    print("Chave não encontrada no dicionário.")
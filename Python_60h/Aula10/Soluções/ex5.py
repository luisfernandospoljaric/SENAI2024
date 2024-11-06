try:
    with open("arquivo.txt", "r") as file:
        conteudo = file.read()
        print(conteudo)
except FileNotFoundError:
    print("Arquivo não encontrado. Criando um novo arquivo.")
    with open("arquivo.txt", "w") as file:
        file.write("Arquivo criado devido a erro na leitura.")
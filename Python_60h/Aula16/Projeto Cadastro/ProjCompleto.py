# Antes de tudo instale a biblioteca:
# pip install pandas openpyxl

import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os

# Função para salvar os dados no Excel
def salvar_dados():
    nome = entry_nome.get()
    nascimento = entry_nascimento.get()
    idade = entry_idade.get()
    endereco = entry_endereco.get()

    if not nome or not nascimento or not idade or not endereco:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
        return

    # Criar um dicionário com os dados
    dados = {
        "Nome": [nome],
        "Data de Nascimento": [nascimento],
        "Idade": [idade],
        "Endereço": [endereco]
    }

    # Verificar se o arquivo já existe
    arquivo = "C:/Users/luisf/Desktop/Resolução de exercicios - Python/Teste Projeto Cadastro/cadastro_clientes.xlsx"
    if os.path.exists(arquivo):
        # Carregar o arquivo existente e adicionar os novos dados
        df_existente = pd.read_excel(arquivo)
        df_novo = pd.DataFrame(dados)
        df_combinado = pd.concat([df_existente, df_novo], ignore_index=True)
        df_combinado.to_excel(arquivo, index=False)
    else:
        # Criar um novo arquivo
        df = pd.DataFrame(dados)
        df.to_excel(arquivo, index=False)

    messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
    entry_nome.delete(0, tk.END)
    entry_nascimento.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)

# Criar a interface
janela = tk.Tk()
janela.title("Cadastro de Clientes")

tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Data de Nascimento:").grid(row=1, column=0, padx=10, pady=5)
entry_nascimento = tk.Entry(janela)
entry_nascimento.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Idade:").grid(row=2, column=0, padx=10, pady=5)
entry_idade = tk.Entry(janela)
entry_idade.grid(row=2, column=1, padx=10, pady=5)

tk.Label(janela, text="Endereço:").grid(row=3, column=0, padx=10, pady=5)
entry_endereco = tk.Entry(janela)
entry_endereco.grid(row=3, column=1, padx=10, pady=5)

btn_salvar = tk.Button(janela, text="Salvar", command=salvar_dados)
btn_salvar.grid(row=4, column=0, columnspan=2, pady=10)

janela.mainloop()

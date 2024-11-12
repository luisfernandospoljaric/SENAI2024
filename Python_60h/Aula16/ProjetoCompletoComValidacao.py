import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os
from datetime import datetime

def calcular_idade(data_nascimento):
    try:
        data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
        hoje = datetime.today()

        if data_nascimento > hoje:
            messagebox.showerror("Erro","Data maior que atual")
        else:
            idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
            entry_idade.delete(0, tk.END) #Limpa o campo de idade
            entry_idade.insert(0, str(idade)) #Insere a idade Calculada
    except ValueError:
        messagebox.showerror("Erro", "Data de nascimento inválida")

# Função para Salvar os dados no Excel
def salvar_arquivos():
    nome = entry_nome.get()
    nascimento = entry_nascimento.get()
    idade = entry_idade.get()
    endereco = entry_endereco.get()

    if not nome or not nascimento or not idade or not endereco:
        messagebox.showerror("Erro", "todos os campos devem ser preenchidos")
        return
    
    #Criar um dicionário de dados
    dados = {
        "Nome": [nome],
        "Data de Nascimento": [nascimento],
        "Idade": [idade],
        "Endereço": [endereco]
    }

    arquivo = "C:/Users/Professor/Desktop/AulasLuis/AulaPython/Aula16/cadastro_cliente.xlsx"
    if os.path.exists(arquivo):
        df_existente = pd.read_excel(arquivo)
        df_novo = pd.DataFrame(dados)
        df_combinado = pd.concat([df_existente, df_novo], ignore_index=True)
        df_combinado.to_excel(arquivo, index=False)
    else:
        #Criar um novo Arquivo;
        df = pd.DataFrame(dados)
        df.to_excel(arquivo, index=False)

    messagebox.showinfo("Sucesso", "Dados Salvos!")
    entry_nome.delete(0, tk.END)
    entry_nascimento.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)

#CRIAR UM LAYOUT (Interface)

janela = tk.Tk()
janela.title("Cadastro de Cliente")

tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Data de nascimento: (DD/MM/AAAA)").grid(row=1, column=0, padx=10, pady=5)
entry_nascimento = tk.Entry(janela)
entry_nascimento.grid(row=1, column=1, padx=10, pady=5)
entry_nascimento.bind("<FocusOut>", lambda event: calcular_idade(entry_nascimento.get()))

tk.Label(janela, text="Idade:").grid(row=2, column=0, padx=10, pady=5)
entry_idade = tk.Entry(janela)
entry_idade.grid(row=2, column=1, padx=10, pady=5)

tk.Label(janela, text="Endereço").grid(row=3, column=0, padx=10, pady=5)
entry_endereco = tk.Entry(janela)
entry_endereco.grid(row=3, column=1, padx=10, pady=5)

btn_Salvar = tk.Button(janela, text="Salvar", command=salvar_arquivos)
btn_Salvar.grid(row=4, column=0, columnspan=2, pady=10)

janela.mainloop()



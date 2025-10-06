import tkinter as tk 
import orm
from tkinter import messagebox

def adicionar_jogo():
    jogo = entry_jogo.get()
    ano = entry_ano.get()
    empresa = entry_empresa.get()
    preco = entry_preco.get()

    orm.adiciona_jogo(jogo, ano, empresa, preco)
    messagebox.showinfo('Tudo certo!', 'Jogo adicionado!')

def atualizar_jogo():
    id = entry_id.get()
    jogo = entry_jogo.get()
    ano = entry_ano.get()
    empresa = entry_empresa.get()
    preco = entry_preco.get()

    orm.atualiza_jogo(id, jogo, ano, empresa, preco)
    messagebox.showinfo('Tudo certo!', 'Jogo atualizado!')

def deletar_jogo():
    id = entry_id.get()

    orm.deleta_jogo(id)
    messagebox.showinfo('Tudo certo!', 'Jogo deletado!')



root = tk.Tk()
root.title('Gerenciador de jogos')

# Rótulos e inputs

label_id = tk.Label(root, text = 'ID:')
label_id.grid(row=0, column=0)
entry_id = tk.Entry(root, width=50)
entry_id.grid(row=0, column=1, padx=10, pady=5)

label_jogo = tk.Label(root, text = 'Jogo:')
label_jogo.grid(row=1, column=0)
entry_jogo = tk.Entry(root, width=50)
entry_jogo.grid(row=1, column=1, padx=10, pady=5)

label_ano = tk.Label(root, text = 'Ano:')
label_ano.grid(row=2, column=0)
entry_ano = tk.Entry(root, width=50)
entry_ano.grid(row=2, column=1, padx=10, pady=5)

label_empresa = tk.Label(root, text = 'Empresa:')
label_empresa.grid(row=3, column=0)
entry_empresa = tk.Entry(root, width=50)
entry_empresa.grid(row=3, column=1, padx=10, pady=5)

label_preco = tk.Label(root, text = 'Preço:')
label_preco.grid(row=4, column=0)
entry_preco = tk.Entry(root, width=50)
entry_preco.grid(row=4, column=1, padx=10, pady=5)

button_adicionar = tk.Button(root, text='Adicionar jogo', command=adicionar_jogo)
button_adicionar.grid(row=5, column=0, columnspan=2, pady=5, padx=10)

button_atualizar = tk.Button(root, text='Atualizar jogo', command=atualizar_jogo)
button_atualizar.grid(row=6, column=0, columnspan=2, pady=5, padx=10)

button_deletar = tk.Button(root, text='Deletar jogo', command=deletar_jogo)
button_deletar.grid(row=7, column=0, columnspan=2, pady=5, padx=10)


root.mainloop()
# O tkinter é usado para criar a interface das aplicações

import tkinter as tk 

# 1 - Criando a janela 

window = tk.Tk()
window.geometry('350x200') # Largura e altura da janela
window.title('Gerencia Frases')

# 2 - Frame ( equivalente a uma div )

frame = tk.Frame(window) # O frame está contido à janela
frame.pack(padx=10 , pady= 10 , fill='x', expand=True)

# 3 - Criando um label

label = tk.Label(frame, text='Olá, mundo!')
label.pack(fill='x' , expand=True)

# 4 - Input text

frase_lab = tk.Label(frame, pady=10, text='Frase')
frase_lab.pack(fill='x' , expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill='x', expand=True)

# 5 - Botão

# Altera o texto do label 

def click():
    label.config(text=frase_inp.get())

btn = tk.Button(frame, text='Enviar', command=click)
btn.pack()

window.mainloop()
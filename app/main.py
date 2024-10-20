import tkinter as tk #Importa a biblioteca Tkinter

# Cria a janela principal do app
app = tk.Tk()
app.title("Sala Branca") # Define o título da Janela
app.geometry("600x450") # Define tamanho da janela

# Função chamada quando o botão é clicado
def clicar():
    label.config(text="Você clicou no botão!")

# Adiciona um botão na janela
botao = tk.Button(app, text="Clique aqui!", command=clicar)
botao.pack(pady=20) #Organiza o botão e coloca uma margem no topo

# Adiciona um label (texto) na janela
label = tk.Label(app, text="Olá, Bem-vindo(a) a Sala Branca!")
label.pack(pady=10)

# Maantém a janela aberta até ser fechada
app.mainloop()
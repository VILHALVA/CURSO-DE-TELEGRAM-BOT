import telebot
import tkinter as tk
from tkinter import Scrollbar, Text, Entry, Button

TOKEN = "SEU_TOKEN_AQUI"
bot = telebot.TeleBot(TOKEN)

# Função para responder às mensagens do usuário
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    resposta = f"Bot: Você disse '{message.text}'"
    update_chat(resposta)

# Função para atualizar a janela de chat com a resposta do bot
def update_chat(message):
    chat_text.config(state=tk.NORMAL)  # Ativar a edição
    chat_text.insert(tk.END, message + "\n")
    chat_text.config(state=tk.DISABLED)  # Desativar a edição
    chat_text.see(tk.END)  # Rolagem automática para a última mensagem

# Função para enviar mensagem quando o botão "Enviar" é pressionado
def enviar_mensagem():
    mensagem = entrada_mensagem.get()
    entrada_mensagem.delete(0, tk.END)  # Limpar a entrada
    update_chat(f"Você: {mensagem}")
    bot.send_message(chat_id, mensagem)  # Enviar a mensagem para o bot

# Configurações da interface gráfica
root = tk.Tk()
root.title("Bot do Telegram")
root.geometry("400x500")

# Janela de chat
chat_text = Text(root, state=tk.DISABLED)
chat_text.pack(fill=tk.BOTH, expand=True)

# Barra de rolagem
scrollbar = Scrollbar(chat_text)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar.config(command=chat_text.yview)
chat_text.config(yscrollcommand=scrollbar.set)

# Entrada de mensagem
entrada_mensagem = Entry(root)
entrada_mensagem.pack(fill=tk.X, padx=10, pady=10)

# Botão de envio
botao_enviar = Button(root, text="Enviar", command=enviar_mensagem)
botao_enviar.pack()

# ID do chat/grupo em que o bot irá responder (substitua pelo seu)
chat_id = "ID_DO_CHAT_AQUI"

# Iniciar a interface gráfica
root.mainloop()

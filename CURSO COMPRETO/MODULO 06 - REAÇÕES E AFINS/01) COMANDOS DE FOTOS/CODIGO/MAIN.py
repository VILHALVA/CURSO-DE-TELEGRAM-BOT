import os
import telebot
from TOKEN import *

bot = telebot.TeleBot(TOKEN)

# Diretório onde as imagens estão armazenadas
MEDIA_DIR = "MIDIAS"

# Dicionário com os comandos e os nomes dos arquivos de imagem correspondentes
comandos_imagens = {
    "/alegria": "alegria.png",
    "/tristeza": "tristeza.png",
    "/raiva": "raiva.png"
}

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Olá! Envie um dos seguintes comandos para ver uma imagem: /alegria, /tristeza, /raiva")

@bot.message_handler(commands=['alegria', 'tristeza', 'raiva'])
def handle_command(message):
    command = message.text.split()[0]  # Obtém o comando digitado pelo usuário
    if command in comandos_imagens:
        file_name = comandos_imagens[command]
        file_path = os.path.join(MEDIA_DIR, file_name)
        if os.path.exists(file_path):
            photo = open(file_path, 'rb')
            bot.send_photo(message.chat.id, photo)
        else:
            bot.reply_to(message, "Desculpe, imagem não encontrada.")
    else:
        bot.reply_to(message, "Comando inválido. Por favor, use /alegria, /tristeza ou /raiva.")

bot.polling()

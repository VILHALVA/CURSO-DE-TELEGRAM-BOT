import telebot
import json
import os
from TOKEN import *

bot = telebot.TeleBot(TOKEN)

# Carrega as respostas do arquivo JSON
def load_responses():
    with open("WORD.json", "r", encoding="utf-8") as file:
        return json.load(file)

responses = load_responses()

# Função para verificar se a mensagem contém uma palavra-chave
def should_respond(message):
    for keyword in responses.keys():
        if keyword.lower() in message.text.lower():
            return True
    return False

# Manipulador de mensagens
@bot.message_handler(func=lambda message: should_respond(message))
def handle_message(message):
    for keyword, media_file in responses.items():
        if keyword.lower() in message.text.lower():
            # Verifica se o arquivo de mídia existe
            if os.path.exists(f"MIDIAS/{media_file}"):
                # Envia o STICKER
                bot.send_sticker(message.chat.id, open(f"MIDIAS/{media_file}", 'rb'))
            else:
                bot.reply_to(message, "Desculpe, não consegui encontrar o arquivo de mídia correspondente.")
            break

if __name__ == '__main__':
    bot.infinity_polling()

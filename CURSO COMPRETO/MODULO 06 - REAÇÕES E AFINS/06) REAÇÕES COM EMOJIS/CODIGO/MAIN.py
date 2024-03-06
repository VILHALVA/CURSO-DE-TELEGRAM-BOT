import telebot
import json
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
    for keyword, emoji in responses.items():
        if keyword.lower() in message.text.lower():
            # Envia o emoji correspondente
            bot.send_message(message.chat.id, emoji)
            break

if __name__ == '__main__':
    bot.infinity_polling()

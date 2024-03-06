import telebot
import json
import os
from TOKEN import *

bot = telebot.TeleBot(TOKEN)

def load_responses():
    with open("WORD.json", "r", encoding="utf-8") as file:
        return json.load(file)

responses = load_responses()

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    for keyword, filename in responses.items():
        if keyword.lower() in message.text.lower():
            send_image(message.chat.id, filename)
            break

def send_image(chat_id, filename):
    try:
        with open(os.path.join("MIDIAS", filename), "rb") as img:
            bot.send_photo(chat_id, img)
    except FileNotFoundError:
        print(f"Arquivo {filename} não encontrado.")

if __name__ == '__main__':
    print("Bot em execução...")
    bot.polling()

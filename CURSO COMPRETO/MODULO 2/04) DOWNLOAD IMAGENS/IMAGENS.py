import telebot
import requests
import os

TOKEN = "SEU_TOKEN"
bot = telebot.TeleBot(TOKEN)

UNSPLASH_ACCESS_KEY = "SUA_CHAVE_DO_UNSPLASH"
UNSPLASH_API_URL = "https://api.unsplash.com/photos/random"

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Olá! Envie uma descrição de uma imagem ou uma palavra-chave.")

@bot.message_handler(func=lambda message: True)
def search_image(message):
    query = message.text
    headers = {
        "Accept-Version": "v1",
        "Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"
    }
    params = {
        "query": query,
        "orientation": "landscape"
    }

    response = requests.get(UNSPLASH_API_URL, headers=headers, params=params)
    data = response.json()

    if response.status_code == 200 and data.get("urls"):
        image_url = data["urls"]["regular"]
        bot.send_photo(message.chat.id, image_url)
    else:
        bot.send_message(message.chat.id, "Não foi possível encontrar uma imagem correspondente.")

bot.polling()

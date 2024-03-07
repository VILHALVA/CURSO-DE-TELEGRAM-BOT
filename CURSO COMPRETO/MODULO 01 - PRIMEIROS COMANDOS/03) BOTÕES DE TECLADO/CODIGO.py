import telebot
from telebot import types

TOKEN = "TOKEN_AQUI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Opção 1")
    item2 = types.KeyboardButton("Opção 2")
    markup.add(item1, item2)
    
    bot.send_message(message.chat.id, "Escolha uma opção:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Opção 1":
        bot.send_message(message.chat.id, "Você selecionou a Opção 1.")
    elif message.text == "Opção 2":
        bot.send_message(message.chat.id, "Você selecionou a Opção 2.")
    else:
        bot.send_message(message.chat.id, "Por favor, escolha uma das opções.")

bot.polling()

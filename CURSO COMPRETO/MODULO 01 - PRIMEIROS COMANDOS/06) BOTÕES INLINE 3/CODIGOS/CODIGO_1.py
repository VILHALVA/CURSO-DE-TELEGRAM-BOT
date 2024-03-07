import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "TOKEN_AQUI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    markup = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton("GRUPO", url="https://t.me/GRUPOCN")
    button2 = InlineKeyboardButton("CANAL", url="https://t.me/CODIGOCN")
    markup.add(button1, button2)
    bot.send_message(message.chat.id, "Use os botões inline para acessar os links!", reply_markup=markup)

bot.polling()

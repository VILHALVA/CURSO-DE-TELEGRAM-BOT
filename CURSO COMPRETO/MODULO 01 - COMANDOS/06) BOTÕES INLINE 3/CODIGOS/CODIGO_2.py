import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "TOKEN_AQUI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("DIVULGAÇÃO", url="https://t.me/DIVULGACAO2023")
    button2 = InlineKeyboardButton("CODERS", url="https://t.me/CODIGOCN")
    button3 = InlineKeyboardButton("VILHALVA", url="https://t.me/VILHALVA100_CANAL")
    button4 = InlineKeyboardButton("GRUPO CN", url="https://t.me/GRUPOCN")
    button5 = InlineKeyboardButton("NEWS", url="https://t.me/CANALTECNEWS")
    
    markup.row(button1, button2)
    markup.row(button3)
    markup.add(button4, button5)
    
    bot.send_message(message.chat.id, "Use os botões inline para acessar os links!", reply_markup=markup)

bot.polling()

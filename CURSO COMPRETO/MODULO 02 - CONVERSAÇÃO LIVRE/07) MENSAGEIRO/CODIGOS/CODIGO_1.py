import telebot
TOKEN = "TOKEN DO BOT AQUI"
bot = telebot.TeleBot(TOKEN)

chat_id = "ID DO GRUPO AQUI"

bot.send_message(chat_id, '''TEXTO''')


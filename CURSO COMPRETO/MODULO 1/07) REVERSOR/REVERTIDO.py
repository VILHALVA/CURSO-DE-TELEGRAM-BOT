import telebot

TOKEN = "SEU_TOKEN_AQUI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def reverse_message(message):
    user_message = message.text
    reversed_message = user_message[::-1]
    bot.reply_to(message, reversed_message)

bot.polling()

import telebot
# Substitua pelo seu Token do bot
TOKEN = "SEU_TOKEN_AQUI"

# Lista de palavras proibidas
palavras_proibidas = ["palavra1", "palavra2", "palavra3"]

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: any(word in message.text.lower() for word in palavras_proibidas))
def delete_message(message):
    # Exclui a mensagem
    bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(message.chat.id, "Olá! Este é um bot moderador de palavras proibidas.")

if __name__ == '__main__':
    print("Bot iniciado!")
    bot.polling()

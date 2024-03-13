import telebot

TOKEN = "TOKEN_AQUI"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"])
def reagir_mensagem(mensagem):
    chat_id = mensagem.chat.id
    message_id = mensagem.message_id
    bot.set_message_reaction(chat_id, message_id, [telebot.types.ReactionTypeEmoji('❤️')])

bot.polling()

import telebot
from TOKEN import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['enquete'])
def enviar_enquete(message):
    # Verificar se a mensagem veio de um grupo
    if message.chat.type == 'group' or message.chat.type == 'supergroup':
        enquete_texto = "Qual é a sua cor favorita?"
        opcoes = ["Vermelho", "Verde", "Azul"]
        bot.send_poll(message.chat.id, enquete_texto, options=opcoes, is_anonymous=False)
    else:
        bot.reply_to(message, "Esse comando só pode ser usado em grupos!")

bot.polling()

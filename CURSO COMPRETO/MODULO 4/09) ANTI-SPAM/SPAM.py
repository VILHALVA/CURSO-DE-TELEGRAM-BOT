import telebot
import re

TOKEN = "SEU_TOKEN_AQUI"  # Substitua pelo token do seu bot
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def anti_spam(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    text = message.text

    # Verifica se a mensagem contém algum tipo de link
    if re.search(r'http[s]?://[^\s<>"]+|www\.[^\s<>"]+', text):
        # Remove a mensagem do usuário
        bot.delete_message(chat_id, message.message_id)
        # Bane o usuário por envio de spam (você pode personalizar essa mensagem)
        bot.kick_chat_member(chat_id, user_id)
        # Envie uma mensagem de aviso ao grupo (você pode personalizar essa mensagem)
        bot.send_message(chat_id, f"Usuário @{message.from_user.username} foi banido por enviar spam.")

if __name__ == '__main__':
    print("Bot Anti-Spam Iniciado!")
    bot.polling()

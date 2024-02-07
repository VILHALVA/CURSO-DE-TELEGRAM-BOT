import telebot
import time
from telebot import types

TOKEN = 'SEU_TOKEN_AQUI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: message.new_chat_members is not None)
def welcome_new_members(message):
    for member in message.new_chat_members:
        # Obtém informações sobre o membro recém-chegado
        member_name = member.first_name
        member_id = member.id
        group_name = message.chat.title
        
        # Cria uma mensagem de boas-vindas personalizada
        welcome_message = f"Bem-vindo(a) ao grupo {group_name}, {member_name} (ID: {member_id})!\n\n" \
                          "Confira nosso canal parceiro:"

        # Cria um botão inline com o link para o canal parceiro
        inline_button = types.InlineKeyboardMarkup()
        inline_button.add(types.InlineKeyboardButton(text="Canal Parceiro", url="https://t.me/canalparceiro"))

        # Envia a mensagem de boas-vindas com o botão inline
        sent_message = bot.send_message(message.chat.id, welcome_message, reply_markup=inline_button)

        # Programa a exclusão da mensagem de boas-vindas após 1 minuto
        time.sleep(60)
        bot.delete_message(message.chat.id, sent_message.message_id)

if __name__ == '__main__':
    bot.polling()

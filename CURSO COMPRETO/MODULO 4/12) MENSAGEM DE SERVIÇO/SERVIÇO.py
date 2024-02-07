import telebot
from telebot import types

TOKEN = 'SEU_TOKEN_AQUI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def delete_service_messages(message):
    # Verifica se a mensagem é um serviço (por exemplo, mensagem fixada ou alteração de título/foto)
    if message.content_type == 'new_chat_members' or message.content_type == 'left_chat_member' \
            or message.content_type == 'new_chat_title' or message.content_type == 'new_chat_photo' \
            or message.content_type == 'delete_chat_photo' or message.content_type == 'group_chat_created' \
            or message.content_type == 'supergroup_chat_created' or message.content_type == 'channel_chat_created' \
            or message.content_type == 'migrate_to_chat_id' or message.content_type == 'migrate_from_chat_id' \
            or message.content_type == 'pinned_message':
        # Apaga a mensagem de serviço
        bot.delete_message(message.chat.id, message.message_id)

if __name__ == '__main__':
    bot.polling()

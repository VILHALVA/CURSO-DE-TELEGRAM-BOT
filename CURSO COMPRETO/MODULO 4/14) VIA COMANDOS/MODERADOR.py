import telebot
from telebot import types

# Configurações do bot
TOKEN = 'SEU_TOKEN_AQUI'
bot = telebot.TeleBot(TOKEN)

# Lista de IDs de administradores do grupo
admins = [123456789, 987654321]  # Substitua pelos IDs reais dos administradores

# Comando /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Olá! Eu sou o bot moderador. Apenas administradores podem usar meus comandos.")

# Comando /ban
@bot.message_handler(commands=['ban'])
def ban_member(message):
    user_id = get_mentioned_user_id(message)
    if user_id:
        if is_admin(message.from_user.id):
            bot.ban_chat_member(message.chat.id, user_id)
        else:
            bot.reply_to(message, "Você não tem permissão para banir membros.")
    else:
        bot.delete_message(message.chat.id, message.message_id)

# Comando /warn
@bot.message_handler(commands=['warn'])
def warn_member(message):
    user_id = get_mentioned_user_id(message)
    if user_id:
        if is_admin(message.from_user.id):
            bot.send_message(message.chat.id, f"Usuário {user_id} foi advertido.")
        else:
            bot.reply_to(message, "Você não tem permissão para advertir membros.")
    else:
        bot.delete_message(message.chat.id, message.message_id)

# Comando /kick
@bot.message_handler(commands=['kick'])
def kick_member(message):
    user_id = get_mentioned_user_id(message)
    if user_id:
        if is_admin(message.from_user.id):
            bot.kick_chat_member(message.chat.id, user_id)
        else:
            bot.reply_to(message, "Você não tem permissão para expulsar membros.")
    else:
        bot.delete_message(message.chat.id, message.message_id)

# Comando /mute
@bot.message_handler(commands=['mute'])
def mute_member(message):
    user_id = get_mentioned_user_id(message)
    if user_id:
        if is_admin(message.from_user.id):
            bot.restrict_chat_member(message.chat.id, user_id, until_date=None, can_send_messages=False)
        else:
            bot.reply_to(message, "Você não tem permissão para silenciar membros.")
    else:
        bot.delete_message(message.chat.id, message.message_id)

# Comando /del
@bot.message_handler(commands=['del'])
def delete_message(message):
    if is_admin(message.from_user.id):
        user_id = get_mentioned_user_id(message)
        if user_id:
            bot.delete_message(message.chat.id, message.message_id)
        else:
            bot.reply_to(message, "Você precisa mencionar o usuário cuja mensagem deseja apagar.")
    else:
        bot.delete_message(message.chat.id, message.message_id)

# Verifica se o remetente da mensagem é um administrador
def is_admin(user_id):
    return user_id in admins

# Obtém o ID do usuário mencionado na mensagem
def get_mentioned_user_id(message):
    user_id = None
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    elif message.entities:
        for entity in message.entities:
            if entity.type == 'text_mention':
                user_id = entity.user.id
    return user_id

if __name__ == '__main__':
    bot.polling()

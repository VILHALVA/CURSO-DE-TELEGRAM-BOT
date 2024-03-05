from TOKEN import TOKEN
import telebot
from COMANDOS import COMANDOS

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    
    # Verifica se a mensagem veio de um chat em grupo ou canal
    if message.chat.type in ["group", "supergroup", "channel"]:
        group_name = None
        
        # Verifica se o usuário é um administrador do grupo
        chat_admins = bot.get_chat_administrators(message.chat.id)
        admin_ids = [admin.user.id for admin in chat_admins]
        if user_id in admin_ids:
            chat_info = bot.get_chat(message.chat.id)
            group_name = chat_info.title
        
            if group_name:
                COMANDOS(bot)
        else:
            bot.reply_to(message, "VOCÊ NÃO É ADM DESSE GRUPO!")
    else:
        bot.reply_to(message, "ERRO: ESSE COMANDO SÓ PODE SER USADO EM GRUPOS!")

@bot.message_handler(commands=['ban', 'mute', 'kick', 'warn'])
def not_admin(message):
    user_id = message.from_user.id
    
    # Verifica se a mensagem veio de um chat em grupo ou canal
    if message.chat.type in ["group", "supergroup", "channel"]:
        # Verifica se o usuário é um administrador do grupo
        chat_admins = bot.get_chat_administrators(message.chat.id)
        admin_ids = [admin.user.id for admin in chat_admins]
        if user_id not in admin_ids:
            bot.reply_to(message, "VOCÊ NÃO É ADM DESSE GRUPO!")
    else:
        bot.reply_to(message, "ERRO: ESSE COMANDO SÓ PODE SER USADO EM GRUPOS!")

bot.polling()

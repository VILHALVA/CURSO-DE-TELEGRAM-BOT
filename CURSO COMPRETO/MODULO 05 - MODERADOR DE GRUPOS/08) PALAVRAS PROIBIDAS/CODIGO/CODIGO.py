import telebot
import json
import re

TOKEN = "SEU_TOKEN"  # Substitua pelo token do seu bot
bot = telebot.TeleBot(TOKEN)

# Carregar as palavras proibidas e suas ações do arquivo JSON
with open("WORD.json", "r", encoding="utf-8") as file:
    banned_words = json.load(file)

# Função para verificar as palavras proibidas e executar ações
def check_banned_words(message):
    text = message.text.lower()
    for word, action in banned_words.items():
        if re.search(rf'\b{word}\b', text):
            return action
    return None

# Função para banir um usuário
def ban_user(chat_id, user_id):
    bot.kick_chat_member(chat_id, user_id)

# Função para silenciar um usuário
def silence_user(chat_id, user_id):
    bot.restrict_chat_member(chat_id, user_id, can_send_messages=False)

# Manipulador de mensagens para verificar palavras proibidas
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_name = message.from_user.username
    action = check_banned_words(message)
    if action:
        # Verifica se o usuário que envia a mensagem é um administrador do grupo
        chat_admins = bot.get_chat_administrators(chat_id)
        admin_ids = [admin.user.id for admin in chat_admins]
        if user_id in admin_ids:
            bot.reply_to(message, "Você é um administrador e não pode ser penalizado por isso.")
            return
        else:
            if action == "banir":
                ban_user(chat_id, user_id)
            elif action == "silenciar":
                silence_user(chat_id, user_id)
            # Remover a mensagem que contém a palavra proibida
            bot.delete_message(chat_id, message.message_id)
            # Enviar mensagem no grupo informando sobre a penalização
            bot.send_message(chat_id, f"O usuário @{user_name} foi penalizado por enviar uma mensagem com conteúdo proibido.")

# Iniciar o bot
bot.polling()

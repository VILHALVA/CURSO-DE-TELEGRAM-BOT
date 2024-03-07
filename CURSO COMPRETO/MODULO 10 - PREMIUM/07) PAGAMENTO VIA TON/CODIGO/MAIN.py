from DB_CONNECT import *
from TOKEN import TOKEN
import telebot
import mysql.connector

# Inicializa o bot
bot = telebot.TeleBot(TOKEN)

# Manipulador de comando '/start'
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    # Verifica se o usuário está registrado no banco de dados
    if is_user_registered(user_id):
        bot.reply_to(message, "Bem-vindo de volta! Você já está registrado.")
    else:
        # Se o usuário não estiver registrado, envia uma mensagem de pagamento
        bot.send_message(message.chat.id, "Por favor, realize o pagamento para se registrar.")

# Função para verificar se o usuário está registrado no banco de dados
def is_user_registered(user_id):
    query = "SELECT * FROM users WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    return cursor.fetchone() is not None

# Manipulador de mensagem de pagamento
@bot.message_handler(content_types=['successful_payment'])
def handle_payment(message):
    user_id = message.from_user.id

    # Registra o usuário no banco de dados
    if register_user(user_id):
        bot.send_message(message.chat.id, "Pagamento bem-sucedido! Você agora está registrado.")
    else:
        bot.send_message(message.chat.id, "Erro ao registrar usuário.")

# Função para registrar o usuário no banco de dados
def register_user(user_id):
    try:
        query = "INSERT INTO users (user_id) VALUES (%s)"
        cursor.execute(query, (user_id,))
        mysql_conn.commit()
        return True
    except mysql.connector.Error as err:
        print("Erro ao registrar usuário no MySQL:", err)
        return False

# Inicia o bot
bot.polling()

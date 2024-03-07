from DB_CONNECT import *
from TOKEN import TOKEN
from SEU_ID_ADM import *
import telebot
from flask import Flask, request
import mysql.connector
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Página inicial do Flask
@app.route('/')
def index():
    return 'Bot de Aprovação de ADM'

# Manipulador de comando '/start'
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    # Verifica se o usuário está registrado no banco de dados
    if is_user_approved(user_id):
        bot.send_message(message.chat.id, "Bem-vindo de volta! Você está aprovado pelo ADM.")
        # Adicione aqui a lógica para permitir o acesso a recursos específicos
    else:
        # Se o usuário não estiver aprovado, envia um botão inline para solicitar aprovação
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Solicitar Aprovação", url=f"https://t.me/NOME_DO_SEU_BOT?start=approve_{user_id}"))
        bot.send_message(message.chat.id, "Você precisa de aprovação para usar este bot. Clique no botão abaixo para solicitar aprovação:", reply_markup=markup)

# Função para verificar se o usuário está aprovado como ADM
def is_user_approved(user_id):
    query = "SELECT * FROM approved_users WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    return cursor.fetchone() is not None

# Manipulador de comando '/approve'
@bot.message_handler(commands=['approve'])
def approve(message):
    if message.from_user.id == SEU_ID_ADM:
        user_id = int(message.text.split('_')[-1])
        add_approved_user(user_id)
        bot.send_message(user_id, "Você foi aprovado pelo ADM e agora pode acessar o bot.")
        # COLOQUE A LOGICA DO SEU BOT!
    else:
        bot.reply_to(message, "Você não tem permissão para executar este comando.")

# Função para adicionar um usuário aprovado no banco de dados
def add_approved_user(user_id):
    try:
        query = "INSERT INTO approved_users (user_id) VALUES (%s)"
        cursor.execute(query, (user_id,))
        mysql_conn.commit()
    except mysql.connector.Error as err:
        print("Erro ao adicionar usuário aprovado no MySQL:", err)

# Inicia o bot
def start_bot():
    bot.polling()

# Inicia o Flask em segundo plano
if __name__ == '__main__':
    import threading
    threading.Thread(target=start_bot).start()
    app.run()

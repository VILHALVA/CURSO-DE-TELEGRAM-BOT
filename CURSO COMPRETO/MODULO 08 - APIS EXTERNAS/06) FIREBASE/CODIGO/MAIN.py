import requests
from telegram.ext import Updater, CommandHandler
import firebase_admin
from firebase_admin import credentials, firestore
from TOKEN import TOKEN
from FIREBASE_PROJECT import *
from FIREBASE_CREDENTIALS import *

# Inicializa o Firebase
cred = credentials.Certificate(FIREBASE_CREDENTIALS)
firebase_admin.initialize_app(cred)
db = firestore.client()

# Função para lidar com o comando /start
def start(bot, update):
    # Adiciona o usuário ao Firebase
    user_id = update.message.from_user.id
    user_data = {'username': update.message.from_user.username}
    db.collection('users').document(str(user_id)).set(user_data)

    # Envia uma mensagem de boas-vindas ao usuário
    update.message.reply_text('Bem-vindo! Você foi adicionado ao Firebase.')

def main():
    # Cria um Updater para receber atualizações do Telegram
    updater = Updater(TOKEN, use_context=True)

    # Obtém o despachante para registrar manipuladores de comando
    dp = updater.dispatcher

    # Registra um manipulador de comando para o comando /start
    dp.add_handler(CommandHandler("start", start))

    # Inicia o bot
    updater.start_polling()

    # Aguarda o bot receber comandos
    updater.idle()

if __name__ == '__main__':
    main()

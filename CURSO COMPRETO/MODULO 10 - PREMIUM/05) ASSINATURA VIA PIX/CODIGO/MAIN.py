from DB_CONNECT import *
from TOKEN import TOKEN
import telebot
import mysql.connector
from datetime import datetime, timedelta
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Preço da assinatura mensal em centavos
PRECO_ASSINATURA = 1000  # Exemplo: R$ 10,00

# Inicializa o bot
bot = telebot.TeleBot(TOKEN)

# Manipulador de comando '/start'
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    # Verifica se o usuário está registrado e tem uma assinatura válida
    if is_user_subscribed(user_id):
        bot.reply_to(message, "Bem-vindo de volta! Você pode usar este bot.")
    else:
        # Se o usuário não estiver registrado ou assinado, envia um botão inline para pagamento
        send_subscription_button(message)

# Função para verificar se o usuário está registrado e tem uma assinatura válida
def is_user_subscribed(user_id):
    query = "SELECT * FROM subscriptions WHERE user_id = %s AND expiration_date > NOW()"
    cursor.execute(query, (user_id,))
    return cursor.fetchone() is not None

# Função para enviar um botão inline para pagamento da assinatura mensal
def send_subscription_button(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton(f"Pagar Assinatura Mensal ({PRECO_ASSINATURA / 100:.2f} BRL)", callback_data='pay_subscription'))

    bot.send_message(message.chat.id, "Você ainda não é um usuário registrado ou sua assinatura expirou. Por favor, pague a assinatura mensal para acessar este bot:", reply_markup=markup)

# Manipulador de callback de botão inline
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'pay_subscription':
        # Aqui você pode implementar a integração com a API de pagamento para processar a assinatura mensal
        user_id = call.from_user.id
        if subscribe_user(user_id):
            bot.send_message(call.message.chat.id, "Assinatura mensal ativada com sucesso! Você agora pode usar este bot.")
            # COLOQUE A LÓGICA DO SEU BOT!
        else:
            bot.send_message(call.message.chat.id, "Ocorreu um erro ao processar a assinatura. Tente novamente mais tarde.")

# Função para registrar a assinatura mensal do usuário no banco de dados MySQL
def subscribe_user(user_id):
    try:
        # Calcula a data de expiração da assinatura (30 dias a partir de agora)
        expiration_date = datetime.now() + timedelta(days=30)
        
        # Insere a assinatura no banco de dados
        query = "INSERT INTO subscriptions (user_id, expiration_date) VALUES (%s, %s)"
        cursor.execute(query, (user_id, expiration_date))
        mysql_conn.commit()
        return True
    except mysql.connector.Error as err:
        print("Erro ao processar a assinatura:", err)
        return False

# Inicia o bot
bot.polling()

from DB_CONNECT import *
from TOKEN import TOKEN
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Inicializa o bot
bot = telebot.TeleBot(TOKEN)

# Manipulador de comando '/start'
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    # Verifica se o usuário está na tabela MySQL
    if is_user_registered(user_id):
        bot.reply_to(message, "Bem-vindo de volta! Você pode usar este bot.")
    else:
        # Se o usuário não estiver registrado, envia um botão inline para pagamento
        send_payment_button(message)

# Função para verificar se o usuário está na tabela MySQL
def is_user_registered(user_id):
    query = "SELECT * FROM users WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    return cursor.fetchone() is not None

# Função para enviar um botão inline para pagamento via PIX
def send_payment_button(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Pagar via PIX", callback_data='pay_pix'))

    bot.send_message(message.chat.id, "Você ainda não é um usuário registrado. Para acessar este bot, por favor, faça o pagamento via PIX:", reply_markup=markup)

# Manipulador de callback de botão inline
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'pay_pix':
        # Aqui você pode implementar a integração com a API de pagamento PIX
        # Se o pagamento for bem-sucedido, registre o usuário na tabela MySQL
        user_id = call.from_user.id
        if register_user(user_id):
            bot.send_message(call.message.chat.id, "Pagamento realizado com sucesso! Você agora pode usar este bot.")
        else:
            bot.send_message(call.message.chat.id, "Ocorreu um erro ao processar o pagamento. Tente novamente mais tarde.")

# Função para registrar o usuário na tabela MySQL
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

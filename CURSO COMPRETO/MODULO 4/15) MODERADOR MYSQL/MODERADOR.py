import telebot
import mysql.connector

# Configurações do bot
TOKEN = 'SEU_TOKEN_AQUI'
bot = telebot.TeleBot(TOKEN)

# Configurações do banco de dados MySQL
db_host = 'SEU_HOST_MYSQL'
db_user = 'SEU_USUARIO_MYSQL'
db_password = 'SUA_SENHA_MYSQL'
db_database = 'nome_do_banco'  # Substitua pelo nome do seu banco

# Conexão com o banco de dados
db_connection = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_database
)

# Cursor para executar consultas SQL
db_cursor = db_connection.cursor()

# Comando SQL para criar a tabela de configuração
create_table_query = '''
CREATE TABLE IF NOT EXISTS group_settings (
    group_id BIGINT PRIMARY KEY,
    admin_id BIGINT,
    action ENUM('ban', 'kick', 'mute', 'delete') DEFAULT 'delete'
)
'''

# Executa o comando SQL para criar a tabela
db_cursor.execute(create_table_query)
db_connection.commit()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Olá! Use o comando /settings para configurar a ação para links no grupo.")

@bot.message_handler(commands=['settings'])
def settings(message):
    # Verifica se o usuário é um administrador do grupo
    chat_member = bot.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status in ['administrator', 'creator']:
        # Envia o teclado de configuração
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('/ban', '/kick', '/mute', '/delete')
        bot.send_message(message.chat.id, "Escolha a ação para links no grupo:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Você precisa ser um administrador para configurar as ações.")

@bot.message_handler(commands=['ban', 'kick', 'mute', 'delete'])
def set_action(message):
    action = message.text[1:]  # Remove o "/" do comando
    user_id = message.from_user.id
    group_id = message.chat.id

    # Verifica se o usuário é um administrador do grupo
    chat_member = bot.get_chat_member(group_id, user_id)
    if chat_member.status in ['administrator', 'creator']:
        # Atualiza a ação na tabela de configuração
        update_query = '''
        INSERT INTO group_settings (group_id, admin_id, action)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE action = %s
        '''
        data = (group_id, user_id, action, action)
        db_cursor.execute(update_query, data)
        db_connection.commit()

        bot.send_message(group_id, f"Ação para links no grupo configurada para: {action}")
    else:
        bot.send_message(group_id, "Você precisa ser um administrador para configurar as ações.")

if __name__ == '__main__':
    bot.polling()

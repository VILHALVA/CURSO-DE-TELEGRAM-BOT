import mysql.connector
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Conexão ao banco de dados
connection = mysql.connector.connect(
    host="SUA_CONEXÃO",
    user="SEU_USUARIO",
    password="SUA_SENHA",
    database="upload"
)
cursor = connection.cursor()

# Inicialização do bot
TOKEN = "SEU_TOKEN"
bot = telebot.TeleBot(TOKEN)

# Função para obter os nomes dos arquivos do banco de dados
def get_filenames():
    cursor.execute("SELECT filename FROM media")
    filenames = [row[0] for row in cursor.fetchall()]
    return filenames

# Função para enviar os nomes dos arquivos como botões inline
@bot.message_handler(commands=["start"])
def start(message):
    filenames = get_filenames()
    markup = InlineKeyboardMarkup(row_width=1)
    for filename in filenames:
        markup.add(InlineKeyboardButton(filename, callback_data=filename))
    bot.send_message(message.chat.id, "Escolha um arquivo:", reply_markup=markup)

# Função para lidar com a resposta do botão inline
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    query = call.data
    bot.send_message(call.message.chat.id, f'Você selecionou: {query}')

# Inicialização do bot
if __name__ == "__main__":
    print("Bot em execução!")
    bot.polling()

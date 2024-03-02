import mysql.connector
import telebot

# Configurações do bot
TOKEN = "TOKEN_DO_BOT"
bot = telebot.TeleBot(TOKEN)

# Função para lidar com o comando /start
@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, 'Olá! Este bot está pronto para testar a conexão com o MySQL. Use o comando /test_mysql.')

# Função para lidar com o comando /test_mysql
@bot.message_handler(commands=["test_mysql"])
def test_mysql(message):
    # Configuração da conexão com o MySQL
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='upload'
        )
        
        # Verifica se a conexão foi bem sucedida
        if connection.is_connected():
            bot.reply_to(message, 'Conexão com o MySQL estabelecida com sucesso!')
        else:
            bot.reply_to(message, 'Erro ao conectar ao MySQL.')
    except Exception as e:
        bot.reply_to(message, f'Ocorreu um erro ao conectar ao MySQL: {e}')

if __name__ == '__main__':
    print("Bot em execução!")
    bot.polling()

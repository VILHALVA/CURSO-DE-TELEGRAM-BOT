import os
import telebot
import mysql.connector
from telebot.types import Message
from datetime import datetime

TOKEN = "SEU_TOKEN"

# Inicialização do bot
bot = telebot.TeleBot(TOKEN)

# Diretório para salvar os arquivos recebidos
SAVE_DIR = "./MIDIAS"

# Verifica se o diretório existe, se não, cria
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

# Conexão ao MySQL
mysql_connection = mysql.connector.connect(
    host="seu_host",
    user="seu_user",
    password="sua_senha",
    database="upload"
)
mysql_cursor = mysql_connection.cursor()

# Instruções de uso ao iniciar a conversa
@bot.message_handler(commands=["start"])
def start(message: Message):
    instructions = (
        "Olá! Eu sou um bot para receber e salvar diferentes tipos de arquivos.\n"
        "Você pode me enviar áudio, foto, vídeo ou livro em qualquer formato e eu vou salvá-lo para você.\n"
        "Basta enviar o arquivo desejado e eu cuidarei do resto!"
    )
    bot.reply_to(message, instructions)

# Função para salvar e enviar o arquivo recebido
@bot.message_handler(content_types=["audio", "photo", "video", "document"])
def save_media(message: Message):
    try:
        content_type = message.content_type
        file_id = (message.document.file_id if content_type == "document" else
                   message.audio.file_id if content_type == "audio" else
                   message.video.file_id if content_type == "video" else
                   message.photo[-1].file_id)
        file_info = bot.get_file(file_id)
        file_ext = file_info.file_path.split(".")[-1]
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        save_path = os.path.join(SAVE_DIR, f"{content_type}_{timestamp}.{file_ext}")
        downloaded_file = bot.download_file(file_info.file_path)
        with open(save_path, "wb") as file:
            file.write(downloaded_file)
        
        # Salvar no MySQL
        mysql_cursor.execute("INSERT INTO media (filename, directory, file_ext) VALUES (%s, %s, %s)", 
                             (f"{content_type}_{timestamp}.{file_ext}", SAVE_DIR, file_ext))
        mysql_connection.commit()
        
        bot.reply_to(message, f"Arquivo {content_type} salvo com sucesso!")
    except Exception as e:
        bot.reply_to(message, f"Ocorreu um erro ao salvar o arquivo: {str(e)}")

if __name__ == "__main__":
    print("Bot em execução!")
    bot.polling()

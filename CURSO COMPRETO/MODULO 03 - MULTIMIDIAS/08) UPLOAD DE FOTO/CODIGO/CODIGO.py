import telebot
import os

TOKEN = 'SEU_TOKEN_AQUI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['photo'])
def handle_photos(message):
    # Obtém o ID da conversa
    chat_id = message.chat.id
    
    # Verifica se a pasta "../FOTOS" existe, se não, cria a pasta
    if not os.path.exists("./FOTOS"):
        os.makedirs("./FOTOS")
    
    try:
        # Faz o download da foto
        file_id = message.photo[-1].file_id  # Escolhe a última foto enviada (maior resolução)
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        # Salva a foto no diretório "../FOTOS"
        file_path = os.path.join("./FOTOS", f"{file_id}.jpg")  # Salva como JPG
        with open(file_path, 'wb') as new_file:
            new_file.write(downloaded_file)
        
        # Envia feedback ao usuário
        bot.send_message(chat_id, "Foto recebida e salva com sucesso!")
    
    except Exception as e:
        # Envia mensagem de erro se ocorrer algum problema
        bot.send_message(chat_id, f"Ocorreu um erro ao processar a foto: {e}")

# Inicia o bot
bot.polling()

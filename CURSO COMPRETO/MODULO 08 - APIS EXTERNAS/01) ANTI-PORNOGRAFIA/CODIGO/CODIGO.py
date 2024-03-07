import telebot
import requests
from WEBPURIFY_API import *
from TOKEN import *

# Inicialização do bot

bot = telebot.TeleBot(TOKEN)

# Função para verificar e banir imagens pornográficas
def check_and_ban_porn(message):
    # Verifica se a mensagem contém uma foto
    if message.photo:
        # Obtém a URL da foto de maior resolução
        photo_url = bot.get_file_url(message.photo[-1].file_id)
        
        # Faz uma solicitação para a API da WebPurify para verificar se a imagem é pornográfica
        url = 'https://im-api1.webpurify.com/image/check'
        payload = {
            'imgurl': photo_url,
            'key': WEBPURIFY_API_KEY
        }
        response = requests.get(url, params=payload)
        result = response.json()
        
        # Se a imagem for considerada pornográfica, excluir a mensagem e banir o usuário
        if result['status'] == 'failed':
            bot.delete_message(message.chat.id, message.message_id)
            bot.kick_chat_member(message.chat.id, message.from_user.id)
            bot.send_message(message.chat.id, f"Usuário {message.from_user.id} foi banido por enviar conteúdo pornográfico.")

# Lidar com mensagens de texto
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    check_and_ban_porn(message)

# Lidar com mensagens de mídia
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    check_and_ban_porn(message)

# Executar o bot
bot.polling()

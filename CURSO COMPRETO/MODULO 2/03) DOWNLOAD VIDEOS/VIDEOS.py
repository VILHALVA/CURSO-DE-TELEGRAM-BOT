import telegram
import re
from pytube import YouTube
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Coloque aqui o token de acesso do seu bot
TOKEN = '5774876922:AAFHemJbJBIIX15DRs7ehpBtlvXj1WcT0xE'

# Criação do objeto updater e dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Função que lida com as mensagens recebidas
def handle_message(update, context):
    message = update.message.text
    # Extrai o link do YouTube da mensagem usando expressões regulares
    match = re.search("(?P<url>https?://[^\s]+)", message)
    if match is not None:
        url = match.group("url")
        try:
            # Baixa o vídeo do YouTube
            yt = YouTube(url)
            video = yt.streams.filter(adaptive=True).first()
            video.download()
            filename = video.default_filename
            # Envia o vídeo baixado de volta para o usuário
            with open(filename, 'rb') as f:
                context.bot.send_video(chat_id=update.message.chat_id, video=f)
        except Exception as e:
            # Em caso de erro, envia uma mensagem de erro para o usuário
            context.bot.send_message(chat_id=update.message.chat_id, text='Ocorreu um erro ao baixar o vídeo.')
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text='Por favor, envie um link do YouTube.')

# Criação do tratador de mensagens
message_handler = MessageHandler(Filters.text & (~Filters.command), handle_message)

# Adiciona o tratador de mensagens ao dispatcher
dispatcher.add_handler(message_handler)

# Inicia o bot
updater.start_polling()



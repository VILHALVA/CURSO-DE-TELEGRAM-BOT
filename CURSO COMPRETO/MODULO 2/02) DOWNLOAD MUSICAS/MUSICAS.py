import logging
import os
from telegram import Update, Audio
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from pytube import YouTube

# Configurando o logger para exibir informações relevantes
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

# Função para tratar o comando /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Olá! Envie o link do YouTube para eu baixar a música.')

# Função para tratar as mensagens com links do YouTube
def youtube_link(update: Update, context: CallbackContext) -> None:
    url = update.message.text
    logger.info(f'Recebido link do YouTube: {url}')

    try:
        # Baixando o vídeo do YouTube
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        filepath = f'{yt.title}.mp3'
        stream.download(output_path='.', filename=yt.title)

        # Enviando o arquivo de áudio para o usuário
        audio = open(filepath, 'rb')
        update.message.reply_audio(audio=audio)
        audio.close()

        # Removendo o arquivo temporário
        os.remove(filepath)

        logger.info(f'Áudio enviado com sucesso para {update.message.chat_id}')
    except Exception as e:
        logger.warning(f'Erro ao baixar e enviar o áudio: {e}')

# Configurando o token do bot e criando o objeto Updater
updater = Updater('seu_token_aqui', use_context=True)

# Registrando os handlers
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r'^https?:\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-]+)'), youtube_link))

# Iniciando o bot
updater.start_polling()
updater.idle()


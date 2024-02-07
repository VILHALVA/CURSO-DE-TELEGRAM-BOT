import os
import time
from googleapiclient.discovery import build
from telegram.ext import Updater

# Defina suas credenciais do Google e do Telegram
API_KEY = 'YOUR_YOUTUBE_API_KEY'
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
TELEGRAM_CHAT_ID = 'YOUR_TELEGRAM_CHAT_ID'

# Cria um objeto da API do YouTube
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Cria um objeto Updater do Telegram
updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Define uma função para enviar mensagens para o canal do Telegram
def send_message(msg):
    try:
        updater.bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=msg)
    except Exception as e:
        print('Erro ao enviar a mensagem: ', e)

# Define uma função para buscar os vídeos mais recentes dos canais inscritos
def check_new_videos():
    # Pega as informações da sua conta do YouTube
    channels_response = youtube.subscriptions().list(
        part='snippet',
        mine=True
    ).execute()

    # Itera pelos canais inscritos
    for channel in channels_response['items']:
        channel_id = channel['snippet']['resourceId']['channelId']
        channel_title = channel['snippet']['title']

        # Pega os vídeos mais recentes do canal
        videos_response = youtube.search().list(
            part='id,snippet',
            channelId=channel_id,
            maxResults=1,
            order='date'
        ).execute()

        # Verifica se há novos vídeos
        if videos_response['items']:
            video_id = videos_response['items'][0]['id']['videoId']
            video_title = videos_response['items'][0]['snippet']['title']
            video_url = f'https://www.youtube.com/watch?v={video_id}'

            # Envia a mensagem para o canal do Telegram
            msg = f'🔴 Novo vídeo do canal {channel_title}!\n\n{video_title}\n{video_url}'
            send_message(msg)

# Define uma função para verificar os vídeos a cada 10 minutos
def job():
    check_new_videos()
    time.sleep(600)

# Inicia o job
job()

# Inicia o bot do Telegram
updater.start_polling()


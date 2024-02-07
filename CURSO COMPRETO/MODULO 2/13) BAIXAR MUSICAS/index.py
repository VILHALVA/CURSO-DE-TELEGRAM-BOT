import os
import datetime
import telebot
from pytube import YouTube
from os import rename

caracteres = ['#', '.', "'", '"', '<', '>', ':','/', '\ ', '?', '*', '|']

TOKEN = 'TOKEN_AQUI'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def boas_vindas(mensagem):
    bot.reply_to(mensagem, 'Olá amigo, \nvocê pode fazer o download de musicas pelos comandos "/dm" e "/dv" das seguintes formas: \n\n '
                           '/dv <link> -------------> esta forma baixa video\n'
                           '/dm <link> -------------> esta forma para baixar musica \n\n'
                           'O BOT ainda esta em fase de desenvolvimento espero que gostem e que passem feedback ')




@bot.message_handler(commands=['dv'])
def baixar_video(mensagem):
    URL = str(mensagem.text)
    URL = URL[4:]           #coletando URL

    yt = YouTube(URL)
    video = yt.streams.filter(file_extension='mp4').first()
    video.download()  #baixando video
    nome_video = yt.title
    for letra in nome_video:
        if letra in caracteres:
            nome_video = nome_video.replace(letra, '')


    video = open(fr"D:\programasdogrolicos\Python\exercicios_praticos\telegram_bot\{nome_video}.mp4", 'rb')
    try:
        bot.send_video(mensagem.chat.id, video, supports_streaming=True)
    except:
        bot.reply_to(mensagem, 'houve algum problema, talvez nao seja possivel fazer o download')
    with open('pessoas_musicas.txt', 'a', encoding='UTF-8') as txt:
        txt.write(f'{yt.title}-VIDEO-{mensagem.chat.first_name}-{datetime.datetime.now()}\n')
    video.close()
    os.remove(f'{str(nome_video)}.mp4')

@bot.message_handler(commands=['dm'])
def baixar_musica(mensagem):
    URL = str(mensagem.text)
    URL = URL[4:]

    yt = YouTube(URL)
    audio = yt.streams.filter(only_audio=True).first()
    nome_video = str(yt.title)

    audio.download()
    for letra in nome_video:
        if letra in caracteres:
            nome_video = nome_video.replace(letra, '')


    arquivo = f"{str(nome_video)}.mp4"
    rename(arquivo, fr'{str(nome_video)}.mp3')
    arquivo = open(fr'{str(nome_video)}.mp3','rb' )
    try:
        bot.send_audio(mensagem.chat.id, arquivo)
    except:
        bot.reply_to(mensagem, 'houve algum problema, talvez nao seja possivel fazer o download')
    with open('pessoas_musicas.txt', 'a', encoding='UTF-8') as txt:
        txt.write(f'{nome_video}-AUDIO-{mensagem.chat.first_name}\n')
    arquivo.close()
    os.remove(f'{str(nome_video)}.mp3')







bot.polling()

from TOKEN import *
from telegram.ext import Updater, MessageHandler, Filters
import os
from moviepy.editor import VideoFileClip

# Função para converter vídeo para áudio MP3
def convert_video_to_audio(update, context):
    video_file = update.message.video.get_file()
    video_file_path = video_file.download('input_video.mp4') # Salvando o arquivo de vídeo localmente
    output_audio_path = 'output_audio.mp3'
    clip = VideoFileClip(video_file_path)
    clip.audio.write_audiofile(output_audio_path) # Conversão para MP3
    context.bot.send_audio(chat_id=update.effective_chat.id, audio=open(output_audio_path, 'rb')) # Enviar o áudio convertido

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.video & ~Filters.command, convert_video_to_audio))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

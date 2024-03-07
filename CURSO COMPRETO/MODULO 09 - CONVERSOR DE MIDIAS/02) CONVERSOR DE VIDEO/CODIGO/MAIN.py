import os
from telegram.ext import Updater, MessageHandler, Filters
from TOKEN import *

# Função para lidar com mensagens de vídeo
def convert_video_to_mp4(update, context):
    video_file = update.message.video.get_file()
    video_file_path = video_file.download('input_video') # Salvando o arquivo de vídeo localmente
    os.system("ffmpeg -i input_video -c:v copy -c:a aac -strict experimental output_video.mp4") # Conversão para MP4
    context.bot.send_video(chat_id=update.effective_chat.id, video=open('output_video.mp4', 'rb')) # Enviar o vídeo convertido

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.video & ~Filters.command, convert_video_to_mp4))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

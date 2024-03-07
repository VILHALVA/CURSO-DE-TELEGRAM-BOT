from TOKEN import *
import os
from io import BytesIO
from PIL import Image
from telegram.ext import Updater, MessageHandler, Filters

# Função para lidar com mensagens de foto
def convert_photo_to_png(update, context):
    photo_file = update.message.photo[-1].get_file()
    photo_file_path = photo_file.download('input_photo.jpg') # Salvando a foto localmente
    image = Image.open(photo_file_path)
    image.save('output_photo.png', 'PNG') # Convertendo a foto para PNG
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('output_photo.png', 'rb')) # Enviando a foto convertida

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.photo & ~Filters.command, convert_photo_to_png))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

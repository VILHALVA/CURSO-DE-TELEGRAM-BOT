from TOKEN import *
import os
from io import BytesIO
from PIL import Image
from telegram.ext import Updater, MessageHandler, Filters

# Função para lidar com mensagens de foto
def convert_photo_to_icon(update, context):
    photo_file = update.message.photo[-1].get_file()
    photo_file_path = photo_file.download('input_photo.jpg') # Salvando a foto localmente
    image = Image.open(photo_file_path)
    
    # Convertendo a foto para o formato de ícone (.ico)
    icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
    icon_frames = []
    for size in icon_sizes:
        resized_image = image.resize(size)
        icon_frames.append(resized_image)
    
    # Salvar todas as imagens redimensionadas em um arquivo .ico
    output_icon_path = 'output_icon.ico'
    icon_frames[0].save(output_icon_path, icon=Image.ICO, sizes=[image.size for image in icon_frames])
    
    context.bot.send_document(chat_id=update.effective_chat.id, document=open(output_icon_path, 'rb')) # Enviar o ícone convertido

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.photo & ~Filters.command, convert_photo_to_icon))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

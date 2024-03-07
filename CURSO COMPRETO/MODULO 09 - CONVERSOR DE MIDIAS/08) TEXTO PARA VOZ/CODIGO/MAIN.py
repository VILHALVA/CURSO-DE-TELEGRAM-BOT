from TOKEN import *
from telegram.ext import Updater, MessageHandler, Filters
from gtts import gTTS
import os

# Função para converter texto em voz MP3
def convert_text_to_speech(update, context):
    text = update.message.text
    tts = gTTS(text=text, lang='pt-br')  # 'pt-br' para português brasileiro, você pode alterar conforme necessário
    tts.save('output_audio.mp3')  # Salva o arquivo de áudio
    context.bot.send_audio(chat_id=update.effective_chat.id, audio=open('output_audio.mp3', 'rb')) # Enviar o áudio convertido

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, convert_text_to_speech))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

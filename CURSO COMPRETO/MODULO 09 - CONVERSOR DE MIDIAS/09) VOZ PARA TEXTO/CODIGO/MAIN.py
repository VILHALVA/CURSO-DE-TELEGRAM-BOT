from TOKEN import *
from telegram.ext import Updater, MessageHandler, Filters
from google.cloud import speech
import os

# Configurar as credenciais do Google Cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "caminho/para/seu/arquivo-de-credenciais.json"

# Função para converter áudio em texto
def convert_audio_to_text(update, context):
    voice_file = update.message.voice.get_file()
    voice_file_path = voice_file.download('input_audio.ogg') # Salvando o arquivo de áudio localmente

    # Inicializar o cliente de reconhecimento de fala
    client = speech.SpeechClient()

    # Carregar o áudio
    with open(voice_file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.OGG_OPUS,
        language_code="pt-BR"  # Especifica o idioma do áudio (Português do Brasil)
    )

    # Fazer a solicitação de reconhecimento de fala
    response = client.recognize(config=config, audio=audio)

    # Extrair e enviar o texto reconhecido
    for result in response.results:
        context.bot.send_message(chat_id=update.effective_chat.id, text=result.alternatives[0].transcript)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.voice & ~Filters.command, convert_audio_to_text))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

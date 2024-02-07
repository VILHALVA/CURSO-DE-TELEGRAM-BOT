import os
import telegram
from telegram.ext import Updater, MessageHandler, Filters
from google.cloud import texttospeech

# Configuração do bot
bot_token = 'TOKEN_AQUI'
bot = telegram.Bot(token=bot_token)

# Configuração do Google Cloud Text-to-Speech
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'CAMINHO_DO_ARQUIVO_DE_CREDENCIAIS_AQUI.json'
client = texttospeech.TextToSpeechClient()

# Função para converter texto em fala
def text_to_speech(text, voice_name):
    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(language_code='pt-BR', name=voice_name)
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    response = client.synthesize_speech(input=input_text, voice=voice, audio_config=audio_config)
    return response.audio_content

# Função para receber mensagens dos usuários
def handle_message(update, context):
    # Obtém o texto da mensagem enviada pelo usuário
    text = update.message.text
    # Converte o texto em fala com a voz do Ricardo
    audio_data = text_to_speech(text, 'pt-BR-Wavenet-B')
    # Envia o áudio como mensagem de voz para o usuário
    update.message.reply_voice(voice=audio_data)

# Criação do objeto Updater e do dispatcher
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

# Registra o handler para mensagens de texto
dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

# Inicia o bot
updater.start_polling()
updater.idle()


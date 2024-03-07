from io import BytesIO
from pydub import AudioSegment
from telegram.ext import Updater, MessageHandler, Filters
from TOKEN import *

# Função para converter o áudio para MP3
def convert_to_mp3(audio_data):
    # Carrega o áudio na memória
    audio = AudioSegment.from_file(BytesIO(audio_data))

    # Cria um buffer para armazenar o áudio convertido
    output_buffer = BytesIO()

    # Exporta o áudio para MP3 e salva no buffer
    audio.export(output_buffer, format="mp3")

    # Retorna os dados do áudio convertido
    return output_buffer.getvalue()

# Função para lidar com mensagens de áudio
def handle_audio(update, context):
    # Verifica se a mensagem contém um arquivo de áudio
    if update.message.audio:
        # Obtém os dados do arquivo de áudio
        audio_file = update.message.audio.get_file()

        # Baixa os dados do áudio
        audio_data = audio_file.download_as_bytearray()

        # Converte o áudio para MP3
        mp3_data = convert_to_mp3(audio_data)

        # Envia o áudio convertido de volta ao usuário
        context.bot.send_audio(chat_id=update.effective_chat.id, audio=BytesIO(mp3_data))

def main():
    # Crie um objeto Updater e passe seu token bot
    updater = Updater(TOKEN, use_context=True)

    # Obtenha o dispatcher para registrar manipuladores
    dp = updater.dispatcher

    # Adicione um manipulador para mensagens de áudio
    dp.add_handler(MessageHandler(Filters.audio, handle_audio))

    # Comece o bot
    updater.start_polling()

    # Aguarde o bot finalizar
    updater.idle()

if __name__ == '__main__':
    main()

import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "SEU_TOKEN_AQUI"

bot = telebot.TeleBot(TOKEN)

# Diretório onde os arquivos de mídia estão armazenados
MEDIA_DIRECTORY = "./MIDIAS"

@bot.message_handler(commands=["start"])
def start(message):
    markup = InlineKeyboardMarkup(row_width=2)
    audio_button = InlineKeyboardButton("ENVIAR ÁUDIO", callback_data="send_audio")
    markup.add(audio_button)
    bot.reply_to(message, "Clique no botão abaixo para enviar um áudio:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "send_audio":
        audio_file = os.path.join(MEDIA_DIRECTORY, "BoysBoys.mp3")
        send_media(call.message.chat.id, audio_file, "audio")

def send_media(chat_id, filename, media_type):
    try:
        with open(filename, "rb") as file:
            bot.send_chat_action(chat_id, "upload_" + media_type)
            bot.send_audio(chat_id, file)
    except Exception as e:
        bot.send_message(chat_id, f"Ocorreu um erro ao enviar o áudio: {str(e)}")

if __name__ == "__main__":
    print("Bot em execução!")
    bot.polling()

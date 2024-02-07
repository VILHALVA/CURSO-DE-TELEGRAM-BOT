import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "SEU_TOKEN_AQUI"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    markup = InlineKeyboardMarkup(row_width=2)
    
    video_button = InlineKeyboardButton("Enviar Vídeo", callback_data="send_video")
    photo_button = InlineKeyboardButton("Enviar Foto", callback_data="send_photo")
    music_button = InlineKeyboardButton("Enviar Música", callback_data="send_music")
    pdf_button = InlineKeyboardButton("Enviar PDF", callback_data="send_pdf")
    
    markup.add(video_button, photo_button, music_button, pdf_button)
    
    bot.reply_to(message, "Escolha uma opção:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "send_video":
        send_media(call.message.chat.id, "./MIDIAS/sol.mp4", "video")
    elif call.data == "send_photo":
        send_media(call.message.chat.id, "./MIDIAS/telegram.jpg", "photo")
    elif call.data == "send_music":
        send_media(call.message.chat.id, "./MIDIAS/BoysBoys.mp3", "audio")
    elif call.data == "send_pdf":
        send_media(call.message.chat.id, "./MIDIAS/Python.pdf", "document")

def send_media(chat_id, filename, media_type):
    file_path = os.path.join(os.path.dirname(__file__), filename)
    with open(file_path, "rb") as file:
        bot.send_chat_action(chat_id, "upload_" + media_type)
        bot.send_document(chat_id, file)

if __name__ == "__main__":
    print("Bot em execução!")
    bot.polling()

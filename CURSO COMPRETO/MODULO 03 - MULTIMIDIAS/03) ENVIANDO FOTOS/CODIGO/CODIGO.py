import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "SEU_TOKEN_AQUI"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    markup = InlineKeyboardMarkup(row_width=2)

    photo_button = InlineKeyboardButton("ENVIAR FOTO", callback_data="send_photo")
    
    markup.add(photo_button)
    
    bot.reply_to(message, "Clique no botão abaixo para me enviar uma foto:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "send_photo")
def callback_query(call):
    send_media(call.message.chat.id, "./MIDIAS/telegram.jpg", "photo")

def send_media(chat_id, filename, media_type):
    file_path = os.path.join(os.path.dirname(__file__), filename)
    with open(file_path, "rb") as file:
        bot.send_chat_action(chat_id, "upload_" + media_type)
        if media_type == "photo":
            bot.send_photo(chat_id, file)
        else:
            bot.send_document(chat_id, file)

if __name__ == "__main__":
    print("Bot em execução!")
    bot.polling()

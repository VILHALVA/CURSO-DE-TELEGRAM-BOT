import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "SEU_TOKEN_AQUI"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    markup = create_inline_keyboard([["ENVIAR VIDEO", "send_video"]])
    bot.reply_to(message, "CLIQUE NO BOTÃO INLINE PARA RECEBER O VÍDEO:", reply_markup=markup)

def create_inline_keyboard(buttons):
    markup = InlineKeyboardMarkup()
    row_width = 2
    for button_text, callback_data in buttons:
        markup.add(InlineKeyboardButton(button_text, callback_data=callback_data))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "send_video":
        send_media(call.message.chat.id, "./MIDIAS/sol.mp4", "video")

def send_media(chat_id, filename, media_type):
    file_path = os.path.join(os.path.dirname(__file__), filename)
    with open(file_path, "rb") as file:
        bot.send_chat_action(chat_id, "upload_" + media_type)
        if media_type == "video":
            bot.send_video(chat_id, file)

if __name__ == "__main__":
    print("Bot em execução!")
    bot.polling()

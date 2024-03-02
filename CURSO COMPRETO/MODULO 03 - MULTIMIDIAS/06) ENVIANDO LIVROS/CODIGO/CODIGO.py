import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "SEU_TOKEN_AQUI"

bot = telebot.TeleBot(TOKEN)

# Manipulador para o comando /start
@bot.message_handler(commands=["start"])
def start(message):
    markup = InlineKeyboardMarkup(row_width=2)
    pdf_button = InlineKeyboardButton("ENVIAR PDF", callback_data="send_pdf")
    markup.add(pdf_button)
    bot.reply_to(message, "CLIQUE NO BOTÃO ABAIXO PARA RECEBER O LIVRO:", reply_markup=markup)

# Manipulador para os botões inline
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "send_pdf":
        send_media(call.message.chat.id, "./MIDIAS/Python.pdf", "document")

# Função para enviar o documento
def send_media(chat_id, filename, media_type):
    file_path = os.path.join(os.path.dirname(__file__), filename)
    with open(file_path, "rb") as file:
        bot.send_chat_action(chat_id, "upload_" + media_type)
        sent_message = bot.send_document(chat_id, file)
        if sent_message:
            bot.send_message(chat_id, "Documento enviado com sucesso!")

# Execução do bot
if __name__ == "__main__":
    print("Bot em execução!")
    bot.polling()

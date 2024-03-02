import telebot
from TOKEN import *
from DB_CONNECTION import *
from ENVIAR import process_send_media
from APAGAR import delete_media, delete_media_record
from EDITAR import edit, edicao
from EXIBIR import display_media, send_media

# INICIALIZAÇÃO DO BOT:
bot = telebot.TeleBot(TOKEN)

# MENU PRINCIPAL:
@bot.message_handler(commands=["start"])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    send_button = telebot.types.InlineKeyboardButton("ENVIAR", callback_data="send")
    delete_button = telebot.types.InlineKeyboardButton("APAGAR", callback_data="delete")
    edit_button = telebot.types.InlineKeyboardButton("EDITAR", callback_data="edit")
    display_button = telebot.types.InlineKeyboardButton("EXIBIR", callback_data="display")
    markup.add(send_button, delete_button, edit_button, display_button)
    bot.reply_to(message, "Escolha uma opção:", reply_markup=markup)
    
# CALLBACKS-DATAS PARA LIDAR COM BOTÕES INLINES:
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "send":
        bot.send_message(call.message.chat.id, "Por favor, envie a mídia que deseja Salvar.")
        bot.register_next_step_handler(call.message, process_send_media)
    elif call.data == "delete":
        delete_media(call.message.chat.id)
    elif call.data.startswith("delete_"): 
        filename = call.data.split("_")[1] 
        delete_media_record(filename, call.message.chat.id, bot) 
    elif call.data == "edit":
        edit(call.message.chat.id)
    elif call.data.startswith("edit_"): 
        edicao(call.message.chat.id, bot, call.data) 
    elif call.data == "display":
        display_media(call.message.chat.id)
    elif call.data.startswith("send_media"):
        filename = call.data.split('_')[-1]
        send_media(call.message.chat.id, filename)  
        
# START BOT
if __name__ == "__main__":
    print("Bot em execução!")
    bot.polling()

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler

# Configuração do bot
bot_token = 'TOKEN_AQUI'
updater = Updater(bot_token, use_context=True)

# Função para lidar com a consulta do botão
def button_handler(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Você clicou no botão!")

# Função para enviar a mensagem com o botão inline
def send_inline_button(update, context):
    keyboard = [[InlineKeyboardButton("Clique aqui", callback_data='button_clicked')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Clique no botão abaixo:', reply_markup=reply_markup)

# Registro dos handlers
updater.dispatcher.add_handler(CallbackQueryHandler(button_handler))
updater.dispatcher.add_handler(CommandHandler('start', send_inline_button))

# Inicialização do bot
updater.start_polling()
updater.idle()


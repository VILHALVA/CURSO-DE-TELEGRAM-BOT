import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

# Configuração de logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Token do seu bot
TOKEN = 'SEU_TOKEN_AQUI'

# ID do canal onde o bot é administrador
CANAL_ID = "ID_CANAL"  # Substitua pelo ID do seu canal

# Função para verificar se o usuário é um membro do canal
def is_subscribed(update):
    user_id = update.message.from_user.id
    chat_member = update.message.bot.get_chat_member(CANAL_ID, user_id)
    return chat_member.status != 'left'

# Comando /start
def start(update, context):
    if is_subscribed(update):
        update.message.reply_text('Olá! Você é um membro inscrito no canal. Pode usar o bot premium.')
    else:
        keyboard = [
            [InlineKeyboardButton("Inscrever-se no Canal", url="https://t.me/seucanal")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Você não é um membro inscrito no canal. Este bot é apenas para membros.', reply_markup=reply_markup)

# Responder a qualquer mensagem
def reply_message(update, context):
    if is_subscribed(update):
        update.message.reply_text('Você é um membro inscrito no canal. Aqui está a resposta do bot premium.')
    else:
        keyboard = [
            [InlineKeyboardButton("Inscrever-se no Canal", url="https://t.me/seucanal")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Você não é um membro inscrito no canal. Este bot é apenas para membros.', reply_markup=reply_markup)

# Responder a pressionar o botão inline
def button(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Clique no link abaixo para se inscrever no canal:", reply_markup=None)
    update.message.bot.send_message(chat_id=query.message.chat_id, text="https://t.me/seucanal")

# Configuração do bot
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Comandos
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Resposta a mensagens
message_handler = MessageHandler(Filters.text & ~Filters.command, reply_message)
dispatcher.add_handler(message_handler)

# Botão inline
dispatcher.add_handler(CallbackQueryHandler(button))

# Iniciar o bot
updater.start_polling()
updater.idle()

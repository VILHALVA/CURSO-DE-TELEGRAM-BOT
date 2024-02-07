import logging
import pyporn
from telegram.ext import Updater, MessageHandler, Filters

# Configuração do bot
TOKEN = 'TOKEN_AQUI'
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Configuração do logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Função para lidar com as mensagens
def handle_message(update, context):
    # Obtém a mensagem e o chat em que ela foi enviada
    message = update.message
    chat = message.chat

    # Verifica se a mensagem contém pornografia
    if pyporn.contains_porn(message.text):
        # Remove a mensagem
        context.bot.delete_message(chat.id, message.message_id)
        # Bane o usuário
        context.bot.kick_chat_member(chat.id, message.from_user.id)

# Registra o manipulador de mensagens
dispatcher.add_handler(MessageHandler(Filters.text & Filters.group, handle_message))

# Inicia o bot
updater.start_polling()


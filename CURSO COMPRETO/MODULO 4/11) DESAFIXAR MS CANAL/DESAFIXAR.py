import logging
from telegram import Update, ChatPermissions
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Configure o token do seu bot aqui
TOKEN = 'SEU_TOKEN'

# Inicialização do bot
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Configuração de log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Função para desafixar (remover) mensagens do canal vinculado ao grupo
def desafixar_mensagem(update: Update, context: CallbackContext):
    # Verifica se a mensagem é proveniente de um canal vinculado
    if update.message.forward_from_chat and update.message.forward_from_chat.type == 'channel':
        # Obtém o ID do canal vinculado
        channel_id = update.message.forward_from_chat.id

        # Obtém o ID da mensagem a ser desafixada
        message_id = update.message.forward_from_message_id

        # Obtém o ID do chat (grupo) onde a mensagem foi recebida
        chat_id = update.message.chat_id

        try:
            # Desafixa (remove) a mensagem do canal vinculado
            context.bot.delete_message(chat_id=channel_id, message_id=message_id)

            # Notifica o grupo sobre a ação
            context.bot.send_message(chat_id=chat_id, text='Uma mensagem do canal vinculado foi removida.')

        except Exception as e:
            # Em caso de erro, registra no log
            logging.error(f'Erro ao desafixar mensagem: {str(e)}')

# Handler para o comando /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Bot Moderador iniciado.')

# Handler para mensagens recebidas
def mensagem_recebida(update: Update, context: CallbackContext):
    # Verifica se a mensagem é proveniente de um canal vinculado
    if update.message.forward_from_chat and update.message.forward_from_chat.type == 'channel':
        # Desafixa a mensagem do canal vinculado
        desafixar_mensagem(update, context)

# Adiciona os handlers
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.all & ~Filters.command, mensagem_recebida))

# Inicia o bot
updater.start_polling()
updater.idle()

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Obtém o token do bot do BotFather
token = 'YOUR_BOT_TOKEN'

# Cria um updater para o bot
updater = Updater(token=token)

# Lista para armazenar os IDs dos grupos e usuários
subscribers = set()

# Define um comando para iniciar o bot
def start(update, context):
    user_id = update.effective_user.id
    if user_id not in subscribers:
        subscribers.add(user_id)
        update.message.reply_text('Você foi inscrito para receber mensagens de recados!')

# Define um comando para enviar uma mensagem de recado
def send(update, context):
    if update.effective_user.id == YOUR_ADMIN_USER_ID:
        message = ' '.join(context.args)
        for subscriber_id in subscribers:
            context.bot.send_message(subscriber_id, message)
        update.message.reply_text('Mensagem enviada para todos os inscritos!')

# Registra os comandos
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('send', send))

# Inicia o bot
updater.start_polling()
updater.idle()

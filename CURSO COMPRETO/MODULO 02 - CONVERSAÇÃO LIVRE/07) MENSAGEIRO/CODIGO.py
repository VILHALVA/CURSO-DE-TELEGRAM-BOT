import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Substitua 'YOUR_BOT_TOKEN' pelo token do seu bot
token = 'SEU_TOKEN_AQUI'

updater = Updater(token=token)
subscribers = set()

def start(update, context):
    user_id = update.effective_user.id
    if user_id not in subscribers:
        subscribers.add(user_id)
        update.message.reply_text('Você foi inscrito para receber mensagens de recados!')

def send(update, context):
    # Substitua YOUR_ADMIN_USER_ID pelo ID do administrador
    if update.effective_user.id == YOUR_ADMIN_USER_ID:
        message = ' '.join(context.args)
        for subscriber_id in subscribers:
            context.bot.send_message(subscriber_id, message)
        update.message.reply_text('Mensagem enviada para todos os inscritos!')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('send', send))

updater.start_polling()
updater.idle()

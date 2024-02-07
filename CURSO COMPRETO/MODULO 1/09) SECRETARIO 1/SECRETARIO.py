import asyncio
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Obtém o token do bot do BotFather
token = 'YOUR_BOT_TOKEN'

# Cria um updater para o bot
updater = Updater(token=token)

# Define um manipulador de mensagens
def handle_message(update, context):
    # Obtém o texto da mensagem
    text = update.message.text

    # Obtém o nome e a foto de perfil do usuário
    user = update.effective_user
    name = user.full_name
    avatar = user.profile_photo

    # Envia a mensagem para o nosso privado
    updater.bot.send_message(chat_id=updater.bot.get_me().id, text=f'**{name}:** {text}')

# Registra os manipuladores de mensagens
updater.dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

# Inicia o bot
updater.start_polling()
updater.idle()

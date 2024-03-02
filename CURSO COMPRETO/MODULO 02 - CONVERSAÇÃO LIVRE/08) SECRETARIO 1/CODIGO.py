import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Obtém o token do bot do BotFather
token = 'SEU_TOKEN_AQUI'

# Cria um updater para o bot
updater = Updater(token=token)

# Mensagem de boas-vindas
def start(update, context):
    update.message.reply_text("Olá! Eu sou um bot de mensagens. Me envie uma mensagem e eu a encaminharei para o meu proprietário.")
    
# Define um manipulador de mensagens
def handle_message(update, context):
    try:
        # Obtém o texto da mensagem
        text = update.message.text

        # Obtém o nome e a foto de perfil do usuário
        user = update.effective_user
        name = user.full_name
        avatar = user.profile_photo

        # Envia a mensagem para o nosso privado
        context.bot.send_message(chat_id=updater.bot.get_me().id, text=f'**{name}:** {text}')
        update.message.reply_text("Sua mensagem foi encaminhada com sucesso para o proprietário do bot!")
    except Exception as e:
        logging.error(f"Ocorreu um erro ao lidar com a mensagem: {e}")

# Registra os manipuladores de mensagens
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# Inicia o bot
updater.start_polling()
updater.idle()

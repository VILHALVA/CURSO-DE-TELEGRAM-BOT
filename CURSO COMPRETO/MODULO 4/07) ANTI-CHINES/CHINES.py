import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Configurar o token do seu bot aqui
TOKEN = 'SEU_TOKEN_AQUI'

# Inicializar o bot
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Configurar o registro de mensagens
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Palavras ou frases ofensivas que você deseja detectar
palavras_ofensivas = ["chinês", "China", "outras_palavras_ofensivas"]

# Função para verificar mensagens ofensivas
def check_offensive(update: Update, context: CallbackContext):
    message = update.message
    text = message.text.lower()  # Converter o texto para minúsculas para correspondência insensível a maiúsculas e minúsculas

    # Verificar se a mensagem contém palavras ofensivas
    for palavra in palavras_ofensivas:
        if palavra in text:
            # Remover a mensagem
            message.delete()
            # Opcional: Banir o usuário (você precisa de permissões de administrador)
            # update.message.chat.kick_member(update.message.from_user.id)
            return

# Configurar um manipulador de mensagens
offensive_handler = MessageHandler(Filters.text & (~Filters.command), check_offensive)
dispatcher.add_handler(offensive_handler)

# Iniciar o bot
updater.start_polling()
updater.idle()

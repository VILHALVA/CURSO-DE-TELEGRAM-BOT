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

# Função para verificar mensagens em caixa alta
def check_caps(update: Update, context: CallbackContext):
    message = update.message
    text = message.text

    # Defina um limite para o número de letras em caixa alta permitidas
    limite_caps = 5  # Você pode personalizar isso

    # Verificar se a mensagem tem letras maiúsculas excessivas
    if sum(1 for c in text if c.isupper()) > limite_caps:
        # Remover a mensagem
        message.delete()
        # Opcional: Banir o usuário (você precisa de permissões de administrador)
        # update.message.chat.kick_member(update.message.from_user.id)

# Configurar um manipulador de mensagens
caps_handler = MessageHandler(Filters.text & (~Filters.command), check_caps)
dispatcher.add_handler(caps_handler)

# Iniciar o bot
updater.start_polling()
updater.idle()

import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

# Substitua pelo token do seu bot
TOKEN = "SEU_TOKEN_AQUI"

# Substitua pelo ID do seu grupo
GRUPO_ID = -123456789

# Inicialização do bot
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Configurar logging (opcional)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Função para remover mensagens com palavras árabes
def remove_arabic_words(update: Update, context: CallbackContext):
    message = update.message
    if any(word in message.text.lower() for word in ["árabes", "palavra", "que", "quer", "bloquear"]):
        # Remover a mensagem
        message.delete()
        # Banir o usuário
        context.bot.kick_chat_member(chat_id=GRUPO_ID, user_id=message.from_user.id)
        return
    return

# Configurar o handler para remover mensagens
remove_arabic_handler = MessageHandler(Filters.text, remove_arabic_words)
dispatcher.add_handler(remove_arabic_handler)

# Iniciar o bot
updater.start_polling()
updater.idle()

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Configurando o logger para ver possíveis erros
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Função para o comando /start
def start(update, context):
    update.message.reply_text('Olá! Eu sou um bot de exemplo. Como posso ajudar?')

# Função para lidar com mensagens de texto
def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    # Inicializando o Updater com o token do seu bot
    updater = Updater("TOKEN_DO_SEU_BOT", use_context=True)

    # Obtendo o despachante para registrar manipuladores
    dp = updater.dispatcher

    # Registrando manipuladores
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Iniciando o bot
    updater.start_polling()

    # Parando o bot de forma segura caso seja interrompido
    updater.idle()

if __name__ == '__main__':
    main()

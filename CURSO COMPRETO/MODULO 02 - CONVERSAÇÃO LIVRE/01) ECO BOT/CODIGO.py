from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main() -> None:
    updater = Updater("TOKEN_DO_SEU_BOT")  # Substitua "TOKEN_DO_SEU_BOT" pelo token do seu bot
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))  # Manipulador de mensagens para eco

    updater.start_polling()  # Inicia o bot
    updater.idle()

if __name__ == '__main__':
    main()

import random
import time
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler

# Define os estados da conversa
CAPTCHA, VERIFIED = range(2)

# Dicionário para armazenar os membros e seus status de verificação
members = {}

# Função para gerar um Captcha simples (números aleatórios)
def generate_captcha():
    return str(random.randint(1000, 9999))

# Função para iniciar a verificação
def start(update: Update, context: CallbackContext) -> int:
    user_id = update.message.from_user.id
    captcha = generate_captcha()
    members[user_id] = {"captcha": captcha, "verified": False, "timestamp": time.time()}
    update.message.reply_text(f"Olá! Para verificar que você é humano, digite o Captcha: {captcha}")
    return CAPTCHA

# Função para verificar o Captcha
def verify_captcha(update: Update, context: CallbackContext) -> int:
    user_id = update.message.from_user.id
    message_text = update.message.text
    if user_id in members and message_text == members[user_id]["captcha"]:
        members[user_id]["verified"] = True
        update.message.reply_text("Você foi verificado com sucesso! Bem-vindo ao grupo.")
        return ConversationHandler.END
    else:
        update.message.reply_text("Captcha incorreto. Tente novamente ou clique em 'Sair do Grupo'.")
        return CAPTCHA

# Função para verificar membros não verificados e removê-los após 3 minutos
def check_unverified_members(context: CallbackContext):
    current_time = time.time()
    for user_id, member in members.copy().items():
        if not member["verified"] and current_time - member["timestamp"] > 180:
            context.bot.kick_chat_member(context.job.context, user_id)
            del members[user_id]

def main():
    # Substitua com seu token do bot
    updater = Updater("SEU_TOKEN", use_context=True)
    dispatcher = updater.dispatcher

    # Crie um comando /start para iniciar a verificação
    start_handler = CommandHandler("start", start)
    dispatcher.add_handler(start_handler)

    # Use um ConversationHandler para gerenciar a conversa de verificação
    captcha_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.text & ~Filters.command, verify_captcha)],
        states={CAPTCHA: [MessageHandler(Filters.text & ~Filters.command, verify_captcha)]},
        fallbacks=[],
    )
    dispatcher.add_handler(captcha_handler)

    # Inicie um trabalho periódico para verificar membros não verificados
    updater.job_queue.run_repeating(check_unverified_members, interval=60, context=CHAT_ID)

    # Inicie o bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler, PollHandler, PollAnswerHandler
from telegram.ext.poll import Poll

# Configure o token do seu bot aqui
TOKEN = 'SEU_TOKEN_AQUI'

# Definindo estados para o ConversationHandler
ESCOLHENDO_PERGUNTA, DEFININDO_PERGUNTA, DEFININDO_RESPOSTAS, ENVIANDO_ENQUETE = range(4)

# Dicionário para armazenar perguntas e respostas
quiz_data = {}

# Função para iniciar a criação da enquete
def start(update: Update, context: CallbackContext) -> int:
    user = update.effective_user
    update.message.reply_html(
        fr'Olá, {user.mention_html()}!',
        reply_markup=ForceReply(selective=True),
    )
    return ESCOLHENDO_PERGUNTA

# Função para escolher a pergunta
def escolher_pergunta(update: Update, context: CallbackContext) -> int:
    user = update.effective_user
    quiz_data[user.id] = {'pergunta': update.message.text}
    update.message.reply_html(
        f'Ótimo, agora digite as opções de resposta (separadas por vírgula).',
        reply_markup=ForceReply(selective=True),
    )
    return DEFININDO_RESPOSTAS

# Função para definir as respostas
def definir_respostas(update: Update, context: CallbackContext) -> int:
    user = update.effective_user
    respostas = update.message.text.split(',')
    quiz_data[user.id]['respostas'] = [r.strip() for r in respostas]
    update.message.reply_html(
        f'A enquete está pronta! Você pode enviá-la para um grupo ou canal agora.',
        reply_markup=ForceReply(selective=True),
    )
    return ENVIANDO_ENQUETE

# Função para enviar a enquete
def enviar_enquete(update: Update, context: CallbackContext) -> int:
    user = update.effective_user
    pergunta = quiz_data[user.id]['pergunta']
    respostas = quiz_data[user.id]['respostas']

    enquete = context.bot.send_poll(
        update.effective_chat.id,
        question=pergunta,
        options=respostas,
        allows_multiple_answers=True,
    )
    
    # Limpa os dados do usuário
    del quiz_data[user.id]

    update.message.reply_html(f'Enquete enviada! Você pode acessá-la [aqui](https://t.me/{update.effective_chat.username}/{enquete.message_id}).')
    return ConversationHandler.END

# Função principal para iniciar o bot
def main() -> None:
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            ESCOLHENDO_PERGUNTA: [MessageHandler(Filters.text & ~Filters.command, escolher_pergunta)],
            DEFININDO_RESPOSTAS: [MessageHandler(Filters.text & ~Filters.command, definir_respostas)],
            ENVIANDO_ENQUETE: [MessageHandler(Filters.text & ~Filters.command, enviar_enquete)],
        },
        fallbacks=[],
    )

    dp.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

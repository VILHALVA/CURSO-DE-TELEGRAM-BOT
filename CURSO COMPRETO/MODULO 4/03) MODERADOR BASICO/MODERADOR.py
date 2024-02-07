import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Configuração do token do bot do Telegram
TOKEN = 'TOKEN_AQUI'

# Configuração do nível de log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Criação do objeto Updater, que irá receber as atualizações do bot do Telegram
updater = Updater(token=TOKEN, use_context=True)

# Criação do objeto Dispatcher, responsável por gerenciar as mensagens recebidas
dispatcher = updater.dispatcher

# Função que será executada quando o comando /start for enviado
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Olá! Eu sou o moderador do grupo. Como posso ajudar?')

# Função que será executada quando uma mensagem for enviada ao grupo
def handle_message(update, context):
    # Verifica se a mensagem contém algum conteúdo ofensivo (nesse exemplo, apenas a palavra "palavrão")
    if 'palavrão' in update.message.text.lower():
        context.bot.delete_message(chat_id=update.effective_chat.id,
                                   message_id=update.message.message_id)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"{update.message.from_user.name}, por favor, não use palavras ofensivas.")
        context.bot.kick_chat_member(chat_id=update.effective_chat.id,
                                     user_id=update.message.from_user.id)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"{update.message.from_user.name} disse: {update.message.text}")

# Adicionando os handlers de comando e mensagem
start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text & (~Filters.command), handle_message)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

# Função que será executada quando o bot receber um novo membro no grupo
def new_member(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"Bem-vindo(a) ao grupo, {update.message.new_chat_members[0].name}!")
new_member_handler = MessageHandler(Filters.status_update.new_chat_members, new_member)
dispatcher.add_handler(new_member_handler)

# Função que será executada quando o bot for removido do grupo
def bot_removed(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Fui removido do grupo. Até mais!")
bot_removed_handler = MessageHandler(Filters.status_update.left_chat_member, bot_removed)
dispatcher.add_handler(bot_removed_handler)

# Função que será executada quando um membro deixar o grupo
def member_left(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"Até mais, {update.message.left_chat_member.name}!")
member_left_handler = MessageHandler(Filters.status_update.left_chat_member, member_left)
dispatcher.add_handler(member_left_handler)

# Inicialização do bot
updater.start_polling()




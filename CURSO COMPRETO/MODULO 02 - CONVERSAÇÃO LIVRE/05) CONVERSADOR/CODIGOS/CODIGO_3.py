import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Define uma função que responde às mensagens do usuário
def reply_to_message(update, context):
    message = update.message.text
    response = generate_response(message)
    update.message.reply_text(response)

# Define uma função que gera a resposta do bot
def generate_response(message):
    if message.startswith('Oi') or message.startswith('Olá'):
        return 'Olá, como posso ajudá-lo?'
    elif message.startswith('Como você está?'):
        return 'Estou bem, obrigado!'
    elif message.startswith('O que você pode fazer?'):
        return 'Posso responder a perguntas simples e conversar com você.'
    elif message.startswith('Tchau'):
        return 'Até mais!'
    else:
        return 'Desculpe, eu não entendi. Você pode reformular a sua pergunta?'

# Configuração do logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Criação do objeto Updater e dispatcher
updater = Updater('TOKEN AQUI')
dispatcher = updater.dispatcher

# Criação dos handlers
start_handler = CommandHandler('start', reply_to_message)
message_handler = MessageHandler(Filters.text & (~Filters.command), reply_to_message)

# Adiciona os handlers ao dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

# Inicia o bot
updater.start_polling()


import os
import openai
import telegram
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

# Chave de API do OpenAI
openai.api_key = "<sua chave de API da OpenAI>"

# Chave do bot do Telegram
bot_token = "<sua chave do bot do Telegram>"

# Função para lidar com comandos
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Olá! Eu sou o ChatGPT. Como posso ajudar?")

# Função para lidar com mensagens de texto
def reply(update, context):
    # Recupera a mensagem do usuário
    message = update.message.text
    
    # Gera uma resposta utilizando o modelo de linguagem GPT-3
    response = openai.Completion.create(
        engine="davinci",
        prompt=message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    # Envia a resposta para o usuário
    context.bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)

# Cria um objeto do tipo Updater com a chave do bot do Telegram
updater = Updater(token=bot_token, use_context=True)

# Cria um objeto do tipo Dispatcher a partir do Updater
dispatcher = updater.dispatcher

# Cria um objeto do tipo CommandHandler para lidar com o comando "/start"
start_handler = CommandHandler('start', start)

# Adiciona o handler do comando "/start" ao Dispatcher
dispatcher.add_handler(start_handler)

# Cria um objeto do tipo MessageHandler para lidar com mensagens de texto
reply_handler = MessageHandler(Filters.text & ~Filters.command, reply)

# Adiciona o handler de mensagens de texto ao Dispatcher
dispatcher.add_handler(reply_handler)

# Inicia o bot
updater.start_polling()

# Mantém o bot ativo até que seja interrompido manualmente
updater.idle()


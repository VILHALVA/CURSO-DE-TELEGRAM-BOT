import openai
from telegram.ext import Updater, MessageHandler, Filters
from TOKEN import TOKEN
from API_KEY import *

# Inicializa o cliente OpenAI
openai.api_key = API_KEY

# Função para lidar com as mensagens dos usuários
def chat_gpt(bot, update):
    # Obtém a mensagem do usuário
    user_message = update.message.text

    # Chama a API do ChatGPT para obter uma resposta
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_message,
        temperature=0.7,
        max_tokens=150
    )

    # Extrai a resposta da API
    bot_response = response.choices[0].text.strip()

    # Envia a resposta do ChatGPT de volta para o usuário
    update.message.reply_text(bot_response)

def main():
    # Cria um Updater para receber atualizações do Telegram
    updater = Updater(TOKEN, use_context=True)

    # Obtém o despachante para registrar manipuladores de mensagens
    dp = updater.dispatcher

    # Registra um manipulador de mensagens para lidar com todas as mensagens dos usuários
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, chat_gpt))

    # Inicia o bot
    updater.start_polling()

    # Aguarda o bot receber mensagens
    updater.idle()

if __name__ == '__main__':
    main()


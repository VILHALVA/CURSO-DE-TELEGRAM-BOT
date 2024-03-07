import requests
from telegram.ext import Updater, CommandHandler
from TOKEN import TOKEN
from API_KEY import API_KEY

# Função para lidar com o comando /api
def call_api(bot, update):
    # Faz uma solicitação GET à API RESTful
    try:
        response = requests.get(API_KEY)
        
        # Verifica se a solicitação foi bem-sucedida (código 200)
        if response.status_code == 200:
            data = response.json()
            update.message.reply_text(f'Resposta da API: {data}')
        else:
            update.message.reply_text('Falha ao chamar a API.')
    except Exception as e:
        update.message.reply_text('Ocorreu um erro ao processar sua solicitação.')

def main():
    # Cria um Updater para receber atualizações do Telegram
    updater = Updater(TOKEN, use_context=True)

    # Obtém o despachante para registrar manipuladores de comando
    dp = updater.dispatcher

    # Registra um manipulador de comando para o comando /api
    dp.add_handler(CommandHandler("api", call_api))

    # Inicia o bot
    updater.start_polling()

    # Aguarda o bot receber comandos
    updater.idle()

if __name__ == '__main__':
    main()

import requests
from telegram.ext import Updater, CommandHandler
from TOKEN import TOKEN
from API_KEY import API_KEY

# Função para lidar com o comando /image
def image(bot, update):
    # Verifica se foi fornecido um termo de pesquisa
    if len(update.message.text.split()) == 1:
        update.message.reply_text('Por favor, forneça um termo de pesquisa.')
        return
    
    # Extrai o termo de pesquisa da mensagem do usuário
    search_term = ' '.join(update.message.text.split()[1:])
    
    # Chama a API de Pesquisa Customizada do Google para obter os resultados de imagem
    try:
        url = f'https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx=YOUR_CUSTOM_SEARCH_ENGINE_ID&q={search_term}&searchType=image'
        response = requests.get(url)
        data = response.json()
        
        # Verifica se há resultados de imagem
        if 'items' in data:
            # Pega a URL da primeira imagem encontrada
            image_url = data['items'][0]['link']
            
            # Envia a URL da imagem de volta para o usuário
            update.message.reply_text(image_url)
        else:
            update.message.reply_text('Nenhuma imagem encontrada para o termo de pesquisa fornecido.')
    except Exception as e:
        update.message.reply_text('Ocorreu um erro ao processar sua solicitação.')

def main():
    # Cria um Updater para receber atualizações do Telegram
    updater = Updater(TOKEN, use_context=True)

    # Obtém o despachante para registrar manipuladores de comando
    dp = updater.dispatcher

    # Registra um manipulador de comando para o comando /image
    dp.add_handler(CommandHandler("image", image))

    # Inicia o bot
    updater.start_polling()

    # Aguarda o bot receber comandos
    updater.idle()

if __name__ == '__main__':
    main()

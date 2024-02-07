import os
import requests
from telegram.ext import Updater, MessageHandler, Filters

# Chave da API do Azure Computer Vision
subscription_key = 'TOKEN_AQUI'
endpoint = 'https://seu_endpoint_aqui.cognitiveservices.azure.com/'

# Método para enviar uma imagem para a API do Azure e receber uma descrição em texto
def get_image_description(image_url):
    api_url = endpoint + '/vision/v3.0/describe'
    headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/json'}
    body = {'url': image_url}
    response = requests.post(api_url, headers=headers, json=body)
    response.raise_for_status()
    response_json = response.json()
    return response_json['description']['captions'][0]['text']

# Método para enviar uma foto correspondente à descrição em texto para o usuário
def send_image(bot, update, image_url):
    chat_id = update.message.chat_id
    image_path = 'imagem.jpg'
    response = requests.get(image_url)
    with open(image_path, 'wb') as f:
        f.write(response.content)
    bot.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'))
    os.remove(image_path)

# Função para tratar as mensagens recebidas pelo bot
def handle_message(bot, update):
    message = update.message
    if message.photo:
        # Obter a imagem em tamanho máximo
        photo = message.photo[-1].get_file()
        image_url = photo.file_path
        # Obter a descrição em texto da imagem
        image_description = get_image_description(image_url)
        # Enviar uma foto correspondente à descrição em texto
        image_search_url = 'https://www.bing.com/images/search?q=' + image_description + '&form=HDRSC2&first=1&tsc=ImageBasicHover'
        response = requests.get(image_search_url)
        image_search_html = response.text
        image_url_index = image_search_html.find('"originalHeight"')
        if image_url_index != -1:
            image_url_start_index = image_search_html.rfind('"http', 0, image_url_index) + 1
            image_url_end_index = image_search_html.find('"', image_url_start_index)
            image_url = image_search_html[image_url_start_index:image_url_end_index]
            send_image(bot, update, image_url)
        else:
            bot.send_message(chat_id=message.chat_id, text='Não foi possível encontrar uma imagem correspondente.')
    else:
        bot.send_message(chat_id=message.chat_id, text='Por favor, envie uma imagem.')

# Configurar o bot e adicionar um handler para as mensagens
updater = Updater(token='seu_token_aqui')
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text | Filters.photo, handle_message))

# Iniciar o bot
updater.start_polling()
updater.idle()


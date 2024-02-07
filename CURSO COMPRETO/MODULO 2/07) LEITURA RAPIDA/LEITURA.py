import os
import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Defina sua chave de API do Mercury Web Parser aqui
MERCURY_API_KEY = 'sua_chave_de_api_aqui'

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Envie-me a URL do artigo que deseja ler em modo de leitura rápida.")

def article_to_summary(url):
    mercury_url = f'https://mercury.postlight.com/parser?url={url}'
    headers = {'x-api-key': MERCURY_API_KEY}
    
    response = requests.get(mercury_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('title', ''), data.get('excerpt', '')
    else:
        return None, None

def process_article(update: Update, context: CallbackContext):
    url = update.message.text
    
    title, summary = article_to_summary(url)
    if title and summary:
        response = f"<b>{title}</b>\n\n{summary}"
    else:
        response = "Não foi possível recuperar o resumo do artigo. Verifique a URL e tente novamente."
    
    update.message.reply_html(response)

def main():
    # Inicializa o bot
    updater = Updater(token=os.getenv("TELEGRAM_BOT_TOKEN"), use_context=True)
    dispatcher = updater.dispatcher

    # Define um manipulador de comando '/start'
    dispatcher.add_handler(CommandHandler("start", start))

    # Define um manipulador para mensagens de texto
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, process_article))

    # Inicie o bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

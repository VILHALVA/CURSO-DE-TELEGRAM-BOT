import feedparser
from telegram.ext import Updater, CommandHandler
from TOKEN import TOKEN
from NEWS_FEED import *

# Função para lidar com o comando /news
def get_news(bot, update):
    news = []

    # Obtém notícias de cada feed RSS
    for feed_url in NEWS_FEED_URLS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            news.append(entry.title + "\n" + entry.link)
    
    # Envia as notícias de volta para o usuário
    if news:
        update.message.reply_text('\n\n'.join(news))
    else:
        update.message.reply_text('Nenhuma notícia encontrada.')

def main():
    # Cria um Updater para receber atualizações do Telegram
    updater = Updater(TOKEN, use_context=True)

    # Obtém o despachante para registrar manipuladores de comando
    dp = updater.dispatcher

    # Registra um manipulador de comando para o comando /news
    dp.add_handler(CommandHandler("news", get_news))

    # Inicia o bot
    updater.start_polling()

    # Aguarda o bot receber comandos
    updater.idle()

if __name__ == '__main__':
    main()

import telebot
import requests
from bs4 import BeautifulSoup
from telebot import types

API_KEY = 'YOUR_GOOGLE_API_KEY'
SEARCH_ENGINE_ID = 'YOUR_SEARCH_ENGINE_ID'
TOKEN = 'YOUR_BOT_TOKEN'

bot = telebot.TeleBot(TOKEN)

# Manipulador para consultas inline
@bot.inline_handler(lambda query: True)
def search_google(query):
    try:
        search_results = perform_google_search(query.query)

        # Processar os resultados da pesquisa e criar resultados de artigo inline
        results = []
        for i, result in enumerate(search_results[:10]):  # Limita a 10 resultados
            title = result['title']
            description = result['description']
            link = result['link']

            # Criar um resultado de artigo inline
            article_result = types.InlineQueryResultArticle(
                id=str(i),
                title=title,
                description=description,
                input_message_content=types.InputTextMessageContent(
                    message_text=f"{title}\n{description}\n{link}"
                ),
            )
            results.append(article_result)

        bot.answer_inline_query(query.id, results)

    except Exception as e:
        print(e)

# Função para realizar a pesquisa no Google
def perform_google_search(query):
    try:
        url = f'https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}'
        response = requests.get(url)
        data = response.json()

        search_results = []

        if 'items' in data:
            for item in data['items']:
                title = item.get('title', '')
                description = item.get('snippet', '')
                link = item.get('link', '')
                search_results.append({'title': title, 'description': description, 'link': link})

        return search_results

    except Exception as e:
        print(e)
        return []

if __name__ == '__main__':
    bot.polling()

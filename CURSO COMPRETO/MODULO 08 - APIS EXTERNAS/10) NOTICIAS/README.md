# NOTICIAS
## DESCRIÇÃO:
Neste exemplo, quando um usuário enviar o comando /news, o bot buscará as últimas notícias de cada feed RSS configurado e enviará os títulos e links das notícias de volta para o usuário. Você pode adicionar quantos feeds RSS desejar à lista NEWS_FEED_URLS para aumentar a variedade de fontes de notícias fornecidas pelo bot.

## INSTRUÇÃO:
Para criar um bot de notícias que forneça notícias de diferentes fontes, você pode usar a biblioteca feedparser para analisar feeds RSS de sites de notícias. Veja o exemplo de [MAIN.PY](./CODIGO/MAIN.py).

Certifique-se de substituir `'TOKEN.PY'` pelo token do seu bot do Telegram e 'url_feed_rss1', 'url_feed_rss2', etc., pelas URLs dos feeds RSS dos sites de notícias que você deseja incluir.
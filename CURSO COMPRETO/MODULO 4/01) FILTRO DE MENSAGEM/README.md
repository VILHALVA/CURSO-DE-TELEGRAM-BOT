# FILTRO DE MENSAGEM:
O "Bot de Filtragem de Mensagens no Telegram" é um aplicativo Python que utiliza a biblioteca Telebot para processar mensagens em conversas no Telegram com base em critérios de filtragem personalizados. Abaixo estão as principais características e funcionalidades deste bot:

1. **Filtragem Personalizada**: O bot permite a definição de filtros personalizados para mensagens de entrada. Atualmente, ele suporta dois tipos de filtros personalizados:
   
   - `TextMatchFilter`: Este filtro verifica se a mensagem de texto coincide com um conjunto específico de palavras ou frases. No exemplo dado, o filtro corresponde às mensagens que contêm "hi" ou "hello" (maiúsculas ou minúsculas).

   - `TextStartsFilter`: Este filtro verifica se a mensagem de texto começa com uma sequência específica de caracteres. No exemplo, ele verifica se a mensagem começa com "@admin".

2. **Respostas Personalizadas**: Quando uma mensagem atende aos critérios de filtragem, o bot envia uma resposta personalizada de acordo com o filtro aplicado. Por exemplo, se uma mensagem começar com "@admin", o bot responde com "Looks like you are calling admin, wait...", e se a mensagem contiver "hi" ou "hello", o bot responde com "Hi, {name}!", usando o nome do remetente da mensagem.

3. **Interação Amigável**: O bot se esforça para fornecer respostas amigáveis e personalizadas com base nas mensagens recebidas.

4. **Registro de Filtros**: Os filtros personalizados devem ser registrados no bot usando o método `bot.add_custom_filter()`. Isso permite que o bot reconheça e aplique os filtros durante o processamento das mensagens.

5. **Polling Infinito**: O bot utiliza a funcionalidade de polling infinito (`bot.infinity_polling()`) para permanecer ativo e responder às mensagens recebidas instantaneamente.

Este bot é um exemplo simples de como criar filtros personalizados para processar mensagens no Telegram. Ele pode ser estendido com filtros adicionais e respostas personalizadas de acordo com as necessidades específicas do desenvolvedor. É útil para demonstrar como criar uma lógica de processamento de mensagens personalizada no Telegram usando a biblioteca Telebot.

[CÓDIGO FONTE BAIXADO DE PY TELEGRAM BOT API](https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/custom_filters/text_filter_example.py)
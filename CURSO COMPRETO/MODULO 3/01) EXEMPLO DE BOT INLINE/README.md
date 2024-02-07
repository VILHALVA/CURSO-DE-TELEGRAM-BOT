# EXEMPLO DE BOT INLINE
Este exemplo mostra como criar um bot para o modo inline no Telegram usando a biblioteca pyTelegramBotAPI. Aqui está uma descrição das principais funcionalidades deste bot:

1. **Configuração Inicial**: O bot é configurado com o seu token API, que é obtido ao criar um bot no BotFather do Telegram. Certifique-se de substituir `<TOKEN>` pelo seu token real antes de usar o bot.

2. **Manuseio de Consultas Inline**: O bot usa a função `@bot.inline_handler` para definir manipuladores para diferentes consultas inline. Quando um usuário digita uma consulta específica no campo de pesquisa de um chat, o bot responderá de acordo com as regras definidas nos manipuladores.

3. **Consulta de Texto**: Quando um usuário envia a consulta "text", o bot responde com dois resultados de artigo inline. Cada resultado tem um título ("Result1" e "Result2") e envia a mensagem "hi" quando selecionado.

4. **Consulta de Foto**: Quando um usuário envia a consulta "photo1", o bot responde com dois resultados de foto inline. Cada resultado inclui uma imagem de gato ou galo e envia a mensagem "hi" quando selecionado.

5. **Consulta de Vídeo**: Quando um usuário envia a consulta "video", o bot responde com um resultado de vídeo inline. O resultado inclui um link para um vídeo e uma imagem de um galo. O título é definido como "Title".

6. **Consulta Padrão**: Se a consulta estiver em branco ou não corresponder a nenhum dos casos anteriores, o bot responde com um resultado de artigo inline com o título "default" e envia a mensagem "default" quando selecionado.

7. **Loop Principal**: O bot entra em um loop principal chamado `main_loop()` que usa `bot.infinity_polling()` para receber atualizações do Telegram. O bot continuará funcionando até ser interrompido pelo usuário (geralmente com Ctrl + C).

Este bot é um exemplo básico de um bot de modo inline que responde a consultas dos usuários com resultados de artigo, foto e vídeo. Ele pode ser expandido para responder a consultas mais complexas ou fornecer informações úteis com base nas consultas dos usuários. Certifique-se de substituir `<TOKEN>` pelo token real do seu bot antes de usá-lo.

[CÓDIGO FONTE BAIXADO DE PY TELEGRAM BOT API](https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/inline_example.py)
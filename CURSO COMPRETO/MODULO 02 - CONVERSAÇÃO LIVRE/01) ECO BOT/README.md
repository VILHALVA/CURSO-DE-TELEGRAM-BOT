# ECO BOT
## DESCRIÇÃO:
Este bot é um simples bot de eco que retorna qualquer mensagem de texto que o usuário enviar.

- **Eco de Mensagens:** Quando um usuário envia uma mensagem de texto, o bot a ecoa de volta para o usuário.

## COMO USAR?
1. Basta enviar uma mensagem de texto para o bot.
2. O bot responderá imediatamente com a mesma mensagem que você enviou.

## EXPLICAÇÃO:
1. **Função `echo`**: Esta função é chamada sempre que o bot recebe uma mensagem de texto. Ela obtém o texto da mensagem recebida usando `update.message.text` e responde enviando de volta o mesmo texto usando `update.message.reply_text`.

2. **Função `main`**: Esta função principal é responsável por iniciar o bot. Ela cria um objeto `Updater` passando o token do bot como argumento. Em seguida, registra um manipulador de mensagem usando `MessageHandler` que filtrará apenas mensagens de texto (usando `Filters.text`) e excluindo comandos (usando `~Filters.command`). Este manipulador chama a função `echo` sempre que uma mensagem de texto for recebida.

3. Por fim, o bot é iniciado chamando `updater.start_polling()` para começar a buscar atualizações do Telegram e `updater.idle()` para manter o bot em execução até que seja interrompido manualmente.


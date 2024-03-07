# ESTRUTURA DO TELEBOT
## DESCRIÇÃO:
O propósito desse capitulo inicial é te mostrar como funciona a estrutura base do `TELEBOT`.

## EXPLICAÇÃO:
Este é um exemplo de [código Python](./CODIGO.py) usando a biblioteca `python-telegram-bot` para criar um bot simples do Telegram. Vamos analisar cada parte:

1. **Importações e Configuração de Logging:**
   ```python
   from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
   import logging

   logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                       level=logging.INFO)

   logger = logging.getLogger(__name__)
   ```
   - Este trecho importa as classes e funções necessárias da biblioteca `python-telegram-bot`.
   - Configura o logging para registrar informações, como data, nome do logger, nível de registro e mensagem.

2. **Funções de Comando:**
   ```python
   def start(update, context):
       update.message.reply_text('Olá! Eu sou um bot de exemplo. Como posso ajudar?')

   def echo(update, context):
       update.message.reply_text(update.message.text)
   ```
   - `start(update, context)`: Esta função é chamada quando o comando "/start" é enviado ao bot. Ela responde ao remetente com uma mensagem de boas-vindas.
   - `echo(update, context)`: Esta função é chamada para lidar com mensagens de texto. Ela simplesmente envia de volta ao remetente a mesma mensagem que recebeu.

3. **Função Principal (`main`):**
   ```python
   def main():
       updater = Updater("TOKEN_DO_SEU_BOT", use_context=True)
       dp = updater.dispatcher

       dp.add_handler(CommandHandler("start", start))
       dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

       updater.start_polling()
       updater.idle()

   if __name__ == '__main__':
       main()
   ```
   - `main()`: Esta função é o ponto de entrada principal do programa.
   - Inicializa um `Updater` com o token do bot fornecido como argumento.
   - Obtém o despachante (`dispatcher`) para registrar os manipuladores.
   - Registra os manipuladores:
     - `CommandHandler` para lidar com o comando "/start" chamando a função `start`.
     - `MessageHandler` para lidar com mensagens de texto (exceto comandos), chamando a função `echo`.
   - Inicia o bot (`updater.start_polling()`) para começar a buscar atualizações do Telegram.
   - Mantém o bot em execução até que ele seja interrompido (`updater.idle()`).

Certifique-se de substituir "TOKEN_DO_SEU_BOT" pelo token real do seu bot antes de executar o código. Este exemplo cria um bot simples que responde a mensagens de texto e ao comando "/start" com uma mensagem de boas-vindas.

## QUAL É A DIFERENÇA ENTRE `REPLY_TO` E `SEND_MESSAGE`?
A diferença entre `reply_to` e `send_message` está na maneira como o bot responde a uma mensagem recebida:

1. **`reply_to`:**
   - Quando o bot usa `reply_to`, ele responde diretamente a uma mensagem específica, vinculando a resposta à mensagem original. Isso significa que a resposta é enviada como uma resposta direta à mensagem original no chat em que a mensagem foi recebida. Essa abordagem é útil quando o bot precisa responder contextualmente a uma mensagem específica.

2. **`send_message`:**
   - Por outro lado, `send_message` envia uma nova mensagem independente no chat, não vinculada a nenhuma mensagem anterior. Isso permite que o bot envie mensagens independentes no chat, sem necessariamente responder a uma mensagem específica. Essa abordagem é útil quando o bot precisa iniciar uma nova conversa ou enviar informações que não estão diretamente relacionadas a uma mensagem específica anterior.


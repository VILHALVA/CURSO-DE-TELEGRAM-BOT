# MENSAGEIRO
## DESCRIÇÃO:
- Os usuários podem iniciar uma conversa com o bot e se inscrever para receber mensagens de recados.
- O administrador do bot pode enviar mensagens de recados para todos os inscritos.

## EXPLICAÇÃO:
Este script Python cria um bot do Telegram que permite que um administrador envie mensagens de recado para todos os usuários que se inscreveram no bot. Vou explicar o funcionamento do código:

1. **Configuração de Logging:**
   ```python
   logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
   ```
   - Configura o formato e o nível de logging para o programa.

2. **Inicialização do Updater:**
   ```python
   token = 'YOUR_BOT_TOKEN'
   updater = Updater(token=token)
   ```
   - Substitua `'YOUR_BOT_TOKEN'` pelo token do seu bot. Isso inicializa o `Updater`, que é a parte central da biblioteca `python-telegram-bot` que recebe as atualizações do Telegram e envia comandos para os handlers correspondentes.

3. **Gerenciamento de Inscritos:**
   ```python
   subscribers = set()
   ```
   - Inicializa um conjunto vazio para armazenar os IDs dos usuários inscritos para receber mensagens de recado.

4. **Handler para o Comando "/start":**
   ```python
   def start(update, context):
       user_id = update.effective_user.id
       if user_id not in subscribers:
           subscribers.add(user_id)
           update.message.reply_text('Você foi inscrito para receber mensagens de recados!')
   ```
   - Esta função é chamada quando um usuário envia o comando "/start".
   - Ela verifica se o usuário já está inscrito. Se não estiver, adiciona o ID do usuário ao conjunto `subscribers` e envia uma mensagem confirmando a inscrição.

5. **Handler para o Comando "/send":**
   ```python
   def send(update, context):
       if update.effective_user.id == YOUR_ADMIN_USER_ID:
           message = ' '.join(context.args)
           for subscriber_id in subscribers:
               context.bot.send_message(subscriber_id, message)
           update.message.reply_text('Mensagem enviada para todos os inscritos!')
   ```
   - Esta função é chamada quando o administrador envia o comando "/send".
   - Ela verifica se o usuário que enviou o comando é o administrador (com base no ID do usuário).
   - Se for o administrador, a função envia a mensagem fornecida como argumento para todos os usuários inscritos.

6. **Registro dos Handlers:**
   ```python
   updater.dispatcher.add_handler(CommandHandler('start', start))
   updater.dispatcher.add_handler(CommandHandler('send', send))
   ```
   - Registra os handlers para os comandos "/start" e "/send".

7. **Início do Bot e Manutenção Ativa:**
   ```python
   updater.start_polling()
   updater.idle()
   ```
   - Inicia o bot, fazendo com que ele comece a buscar atualizações do Telegram e responda a comandos conforme configurado.
   - Mantém o bot em execução até que seja interrompido manualmente.

Certifique-se de substituir `'YOUR_BOT_TOKEN'` pelo token do seu bot e `YOUR_ADMIN_USER_ID` pelo ID do administrador real. Assim, o administrador pode enviar mensagens de recado para todos os usuários inscritos usando o comando "/send".



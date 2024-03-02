# SECRETARIO 1
## DESCRIÇÃO:
O bot recebe mensagens de texto dos usuários, extrai informações sobre o usuário e encaminha a mensagem para um chat privado do Telegram.

## EXPLICAÇÃO:
1. **Configuração do Logger:**
   ```python
   logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
   ```
   - Isso configura o formato e o nível de logging para o programa. Neste caso, o nível de logging é definido como `INFO`, o que significa que apenas mensagens de nível `INFO` ou superior serão registradas.

2. **Criação do Updater:**
   ```python
   updater = Updater(token=token)
   ```
   - Isso cria um objeto `Updater` para o bot, utilizando o token fornecido.

3. **Handler para o Comando "/start":**
   ```python
   def start(update, context):
       update.message.reply_text("Olá! Eu sou um bot de mensagens. Me envie uma mensagem e eu a encaminharei para o meu proprietário.")
   ```
   - Este handler responde ao comando "/start" com uma mensagem de boas-vindas.

4. **Handler para Todas as Mensagens:**
   ```python
   def handle_message(update, context):
       try:
           text = update.message.text
           user = update.effective_user
           name = user.full_name
           avatar = user.profile_photo
           context.bot.send_message(chat_id=updater.bot.get_me().id, text=f'**{name}:** {text}')
           update.message.reply_text("Sua mensagem foi encaminhada com sucesso para o proprietário do bot!")
       except Exception as e:
           logging.error(f"Ocorreu um erro ao lidar com a mensagem: {e}")
   ```
   - Este handler é chamado para todas as mensagens de texto recebidas pelo bot, exceto comandos.
   - Ele extrai o texto da mensagem, o nome e a foto de perfil do remetente.
   - Em seguida, envia a mensagem para o proprietário do bot, junto com o nome do remetente.
   - Se ocorrer algum erro durante o processamento da mensagem, o erro é registrado usando o logger configurado anteriormente.

5. **Registro dos Handlers:**
   ```python
   updater.dispatcher.add_handler(CommandHandler('start', start))
   updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
   ```
   - Aqui, os handlers criados são registrados no dispatcher do Updater para que o bot possa processar os comandos e mensagens recebidos.

